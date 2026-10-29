#!/usr/bin/env python3
"""Report how the local branch relates to GitHub and fast-forward only when it is safe.

Used by /catchup and /wrap. This script never pushes, resets, stashes, rebases or creates merge
commits. The only change it can make is a fast-forward (--pull), and only when the branch is
strictly behind and no incoming file collides with an uncommitted local change.

    python scripts/sync_status.py                  # report from the last fetch
    python scripts/sync_status.py --fetch          # fetch from origin first
    python scripts/sync_status.py --fetch --pull   # also fast-forward when safe

The last line printed is "STATE: <NAME>". Exit code 0 = nothing needs a decision,
1 = a human decision is needed (see the printed advice), 2 = error.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REMOTE = "origin"
LIST_LIMIT = 20


class GitError(RuntimeError):
    pass


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(
        ["git", "-c", "core.quotepath=off", *args],
        cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if check and proc.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc


def out(repo: Path, *args: str) -> str:
    return git(repo, *args).stdout.strip()


def succeeds(repo: Path, *args: str) -> bool:
    return git(repo, *args, check=False).returncode == 0


def indent(text: str) -> str:
    return "\n".join(f"  {line}" for line in text.splitlines())


def dirty_paths(repo: Path) -> list[str]:
    """Paths with uncommitted changes, including untracked (not ignored) files."""
    fields = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all").stdout.split("\0")
    paths: list[str] = []
    i = 0
    while i < len(fields):
        entry = fields[i]
        i += 1
        if not entry:
            continue
        status, path = entry[:2], entry[3:]
        paths.append(path)
        if "R" in status or "C" in status:  # the next field is the rename/copy source
            if i < len(fields) and fields[i]:
                paths.append(fields[i])
            i += 1
    return paths


def run(args: argparse.Namespace) -> tuple[str, int]:
    if not succeeds(args.repo, "rev-parse", "--git-dir"):
        print(f"{args.repo} is not inside a Git repository.")
        return "NOT_A_REPO", 2
    repo = Path(out(args.repo, "rev-parse", "--show-toplevel"))
    print(f"Repository: {repo}")

    branch = git(repo, "symbolic-ref", "--quiet", "--short", "HEAD", check=False).stdout.strip()
    if not branch:
        print("HEAD is detached (not on a branch). Check out a branch before syncing.")
        return "DETACHED_HEAD", 1
    has_commits = succeeds(repo, "rev-parse", "--verify", "--quiet", "HEAD")
    print(f"Branch: {branch}")
    print(f"HEAD: {out(repo, 'log', '-1', '--format=%h %s (%ad)', '--date=short') if has_commits else 'no commits yet'}")

    dirty = dirty_paths(repo)
    print(f"Uncommitted changes: {len(dirty)} path(s)")
    for path in dirty[:LIST_LIMIT]:
        print(f"  {path}")
    if len(dirty) > LIST_LIMIT:
        print(f"  ... and {len(dirty) - LIST_LIMIT} more")

    for marker, operation in (("MERGE_HEAD", "merge"), ("rebase-merge", "rebase"),
                              ("rebase-apply", "rebase or am"), ("CHERRY_PICK_HEAD", "cherry-pick")):
        if (repo / out(repo, "rev-parse", "--git-path", marker)).exists():
            print(f"A {operation} is in progress. Finish or abort it before syncing.")
            return "OPERATION_IN_PROGRESS", 1

    remote_url = git(repo, "remote", "get-url", REMOTE, check=False).stdout.strip()
    if not remote_url:
        print(f"No '{REMOTE}' remote is configured. See README.md (Pushing to GitHub) to connect one.")
        return "NO_REMOTE", 1
    print(f"Remote: {REMOTE} -> {remote_url}")

    if args.fetch:
        fetched = git(repo, "fetch", REMOTE, check=False)
        if fetched.returncode != 0:
            print(f"Fetch failed:\n{indent(fetched.stderr.strip())}")
            print("Check the network connection and GitHub authentication (`gh auth status`).")
            return "FETCH_FAILED", 2
        print(f"Fetched from {REMOTE}.")
    else:
        print("Not fetched in this run; remote state is as of the last fetch.")

    upstream = git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}", check=False).stdout.strip()
    if upstream and not succeeds(repo, "rev-parse", "--verify", "--quiet", "@{u}"):
        upstream = ""  # tracking is configured, but the branch does not exist on the remote (yet)
    tracking = bool(upstream)
    if not upstream and succeeds(repo, "rev-parse", "--verify", "--quiet", f"refs/remotes/{REMOTE}/{branch}"):
        upstream = f"{REMOTE}/{branch}"
    note = "" if tracking or not upstream else " (exists, but tracking is not configured)"
    print(f"Upstream: {upstream or 'none'}{note}")

    if not upstream:
        if has_commits:
            print(f"'{branch}' exists only locally. The owner's first push creates it on GitHub:")
            print(f"  git push -u {REMOTE} {branch}")
            return "NOT_PUSHED", 0
        print("No commits locally and no matching branch on the remote: nothing to sync yet.")
        return "NO_COMMITS_YET", 0
    if not has_commits:
        print(f"The remote has history on {upstream}, but this repository has no commits.")
        print("Do not commit on an unrelated root. Ask the owner; the usual fix is a fresh clone,")
        print("then copying the local files into it.")
        return "REMOTE_HAS_HISTORY", 1

    ahead, behind = (int(n) for n in out(repo, "rev-list", "--left-right", "--count", f"HEAD...{upstream}").split())
    print(f"Ahead of {upstream}: {ahead} commit(s); behind: {behind} commit(s)")
    if ahead:
        print("Local commits not on GitHub (the owner pushes these manually):")
        print(indent(out(repo, "log", "--oneline", f"-{LIST_LIMIT}", f"{upstream}..HEAD")))
    if behind:
        print("Incoming commits from GitHub:")
        print(indent(out(repo, "log", "--oneline", f"-{LIST_LIMIT}", f"HEAD..{upstream}")))

    if ahead and behind:
        print("The branch has DIVERGED from GitHub. Nothing was changed. The owner should review both")
        print(f"sides and integrate manually, e.g. `git pull --rebase {REMOTE} {branch}`.")
        return "DIVERGED", 1
    if ahead:
        if not tracking:
            print(f"Tracking is not configured; the owner's push should set it: git push -u {REMOTE} {branch}")
        return "AHEAD", 0
    if not behind:
        return "UP_TO_DATE", 0

    incoming = set(out(repo, "diff", "--name-only", "--no-renames", "HEAD", upstream).splitlines())
    overlap = sorted(incoming.intersection(dirty))
    if overlap:
        print("Incoming commits touch files that have uncommitted local changes; no fast-forward attempted:")
        for path in overlap:
            print(f"  {path}")
        print("Ask the owner how to preserve the local work (commit it or move it aside), then rerun.")
        return "BEHIND_BLOCKED", 1
    if not args.pull:
        print(f"Safe to fast-forward: rerun with --pull (runs `git merge --ff-only {upstream}`).")
        return "BEHIND", 0
    merged = git(repo, "merge", "--ff-only", upstream, check=False)
    if merged.returncode != 0:
        print(f"Git refused the fast-forward; nothing was changed:\n{indent(merged.stderr.strip())}")
        return "PULL_REFUSED", 1
    print(f"Fast-forwarded {branch} to {out(repo, 'rev-parse', '--short', 'HEAD')}; uncommitted local changes kept.")
    return "FAST_FORWARDED", 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Report Git sync state; fast-forward only when safe. Never pushes.")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository to inspect (default: the one containing this script)")
    parser.add_argument("--fetch", action="store_true", help=f"run `git fetch {REMOTE}` first")
    parser.add_argument("--pull", action="store_true", help="fast-forward when strictly behind and safe")
    args = parser.parse_args(argv)
    try:
        state, code = run(args)
    except GitError as exc:
        print(f"ERROR: {exc}")
        state, code = "ERROR", 2
    print(f"STATE: {state}")
    return code


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")  # commit subjects may not fit the Windows console encoding
    sys.exit(main())
