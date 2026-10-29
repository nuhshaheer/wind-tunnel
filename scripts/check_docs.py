#!/usr/bin/env python3
"""Check that the project documentation is internally consistent. Read-only; used by /wrap.

    python scripts/check_docs.py

Checks that the required files exist; every session log is indexed exactly once in
docs/sessions/SESSION_LOG.md; relative Markdown links and #anchors resolve; repository paths cited in
docs/data_catalog.md exist; PROJECT_STATUS.md is not older than the newest session log; and no
file Git would commit is too large for GitHub or contains an obvious secret.

Each result prints as PASS, WARN or FAIL. Exit code 1 if anything fails.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

REQUIRED_FILES = [
    "CLAUDE.md", "README.md", "PROJECT_STATUS.md", "PROJECT_BACKGROUND.md", "DECISIONS.md", "TODO.md",
    "docs/experimental_setup.md", "docs/data_catalog.md", "docs/sessions/SESSION_LOG.md", "data/README.md",
    ".claude/skills/catchup/SKILL.md", ".claude/skills/wrap/SKILL.md",
]
SESSIONS_DIR = "docs/sessions"
SESSION_INDEX = "docs/sessions/SESSION_LOG.md"
SESSION_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
STATUS_DATE = re.compile(r"Last updated:\**\s*(\d{4}-\d{2}-\d{2})")
# Layout folders documented in data/README.md before they hold any files.
LAYOUT_ROOTS = {"data/raw", "data/processed", "analysis", "results", "cad", "firmware", "docs/images"}
CATALOG_PATH = re.compile(r"`((?:data|analysis|results|cad|firmware|docs)/[^`]*)`")
PLACEHOLDER = re.compile(r"[<>*{}]|YYYY|NNN|\.\.\.")
LINK = re.compile(r"\]\((<[^>]+>|[^)\s]+)")
HEADING = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
FENCE = re.compile(r"^(```|~~~)[^\n]*\n.*?^\1", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")
URL_SCHEME = re.compile(r"^[a-z][a-z0-9+.-]*:", re.I)
WARN_BYTES = 25 * 1024 * 1024
FAIL_BYTES = 100 * 1024 * 1024  # GitHub rejects files above this size.
SCAN_BYTES = 2 * 1024 * 1024
SECRET_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}"),
    "AWS access key id": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Anthropic API key": re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}"),
    "OpenAI-style API key": re.compile(r"\bsk-[A-Za-z0-9]{32,}"),
    "Slack token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
    "hard-coded credential": re.compile(
        r"(?i)\b(?:password|passwd|api_?key|secret|token)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"),
}

Finding = tuple[str, str, str]  # (PASS | WARN | FAIL, check name, message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def committable_files(root: Path) -> list[Path]:
    """Files Git would commit: tracked plus untracked-but-not-ignored."""
    proc = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others",
                           "--exclude-standard"], cwd=root, capture_output=True)
    if proc.returncode == 0:
        names = proc.stdout.decode("utf-8", "replace").split("\0")
        return sorted({root / name for name in names if name and (root / name).is_file()})
    return sorted(p for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts)


def link_targets(text: str) -> list[str]:
    text = INLINE_CODE.sub("", FENCE.sub("", text))
    return [t[1:-1] if t.startswith("<") else t for t in LINK.findall(text)]


def check_required(root: Path) -> list[Finding]:
    missing = [rel for rel in REQUIRED_FILES if not (root / rel).is_file()]
    if missing:
        return [("FAIL", "required files", f"missing {rel}") for rel in missing]
    return [("PASS", "required files", f"all {len(REQUIRED_FILES)} present")]


def check_sessions(root: Path) -> tuple[list[Finding], list[str]]:
    check, findings, logs = "session index", [], {}
    folder, index = root / SESSIONS_DIR, root / SESSION_INDEX
    for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
        if path.name == index.name:
            continue
        match = SESSION_NAME.match(path.name)
        if match:
            logs[path.name] = match.group(1)
        else:
            findings.append(("WARN", check, f"{path.name} does not follow YYYY-MM-DD-topic.md"))
    listed = [Path(unquote(t.split("#")[0])).name for t in link_targets(read(index))] if index.is_file() else []
    for name in logs:
        count = listed.count(name)
        if count != 1:
            findings.append(("FAIL", check, f"{name} is listed {count} times in SESSION_LOG.md (expected once)"))
    if not any(level != "PASS" for level, _, _ in findings):
        findings.append(("PASS", check, f"{len(logs)} session log(s), each indexed once"))
    return findings, sorted(logs.values())


def heading_anchors(text: str) -> set[str]:
    """GitHub-style anchors: lowercase, punctuation dropped, spaces to hyphens, -1/-2 for repeats."""
    anchors: set[str] = set()
    for heading in HEADING.findall(FENCE.sub("", text)):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        anchor, n = slug, 0
        while anchor in anchors:
            n += 1
            anchor = f"{slug}-{n}"
        anchors.add(anchor)
    return anchors


def check_links(root: Path, files: list[Path]) -> list[Finding]:
    check, findings, count = "markdown links", [], 0
    for md in (f for f in files if f.suffix.lower() == ".md"):
        for target in link_targets(read(md)):
            if URL_SCHEME.match(target):
                continue
            count += 1
            path, _, anchor = unquote(target).partition("#")
            dest = (md.parent / path) if path else md
            if not dest.exists():
                findings.append(("FAIL", check, f"{md.relative_to(root).as_posix()} -> {target} (not found)"))
            elif anchor and dest.suffix.lower() == ".md" and anchor not in heading_anchors(read(dest)):
                findings.append(("FAIL", check, f"{md.relative_to(root).as_posix()} -> {target} (no such heading)"))
    return findings or [("PASS", check, f"{count} relative link(s) and anchor(s) resolve")]


def check_catalog(root: Path) -> list[Finding]:
    check, catalog = "data catalog paths", root / "docs/data_catalog.md"
    if not catalog.is_file():
        return []
    cited = {p.rstrip("/") for p in CATALOG_PATH.findall(read(catalog)) if not PLACEHOLDER.search(p)}
    cited -= LAYOUT_ROOTS
    missing = sorted(p for p in cited if not (root / p).exists())
    if missing:
        return [("FAIL", check, f"`{p}` is cited in docs/data_catalog.md but does not exist") for p in missing]
    return [("PASS", check, f"{len(cited)} cited path(s) exist")]


def check_status_date(root: Path, session_dates: list[str]) -> list[Finding]:
    check, status = "status freshness", root / "PROJECT_STATUS.md"
    if not status.is_file():
        return []
    match = STATUS_DATE.search(read(status))
    if not match:
        return [("FAIL", check, "PROJECT_STATUS.md has no 'Last updated: YYYY-MM-DD' line")]
    if session_dates and match.group(1) < session_dates[-1]:
        return [("FAIL", check, f"PROJECT_STATUS.md last updated {match.group(1)}, "
                                f"but the newest session log is {session_dates[-1]}")]
    return [("PASS", check, f"PROJECT_STATUS.md last updated {match.group(1)}")]


def lfs_tracked(root: Path, path: Path) -> bool:
    proc = subprocess.run(["git", "check-attr", "filter", "--", str(path.relative_to(root))],
                          cwd=root, capture_output=True, text=True)
    return proc.returncode == 0 and proc.stdout.strip().endswith(": lfs")


def check_files(root: Path, files: list[Path]) -> list[Finding]:
    findings = []
    for path in files:
        rel, size = path.relative_to(root).as_posix(), path.stat().st_size
        if size > WARN_BYTES and not lfs_tracked(root, path):
            level = "FAIL" if size > FAIL_BYTES else "WARN"
            findings.append((level, "file sizes", f"{rel} is {size / 2**20:.1f} MiB; use external storage or "
                                                  "Git LFS (DECISIONS.md D-004)"))
        if size > SCAN_BYTES:
            continue
        data = path.read_bytes()
        if b"\0" in data[:8192]:
            continue
        for lineno, line in enumerate(data.decode("utf-8", "replace").splitlines(), 1):
            for name, pattern in SECRET_PATTERNS.items():
                if pattern.search(line):
                    findings.append(("FAIL", "secrets", f"{rel}:{lineno} looks like a {name} (value not shown)"))
    checks = {check for _, check, _ in findings}
    if "file sizes" not in checks:
        findings.append(("PASS", "file sizes", f"{len(files)} committable file(s), none over "
                                               f"{WARN_BYTES // 2**20} MiB"))
    if "secrets" not in checks:
        findings.append(("PASS", "secrets", "no obvious secrets in committable text files"))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check project documentation consistency (read-only).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="project root (default: the repository containing this script)")
    root = parser.parse_args(argv).root.resolve()
    files = committable_files(root)
    session_findings, session_dates = check_sessions(root)
    findings = (check_required(root) + session_findings + check_links(root, files) + check_catalog(root)
                + check_status_date(root, session_dates) + check_files(root, files))
    for level, check, message in findings:
        print(f"{level:4}  {check}: {message}")
    failures = sum(level == "FAIL" for level, _, _ in findings)
    warnings = sum(level == "WARN" for level, _, _ in findings)
    print(f"\n{failures} failure(s), {warnings} warning(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")  # file paths may not fit the Windows console encoding
    sys.exit(main())
