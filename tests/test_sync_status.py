"""Tests for scripts/sync_status.py on throwaway local repositories (no network, no GitHub).

A local bare repository stands in for GitHub; a second clone stands in for another machine.
"""
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_status.py"


def _make_writable(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)  # Git marks objects read-only, which blocks deletion on Windows.
    func(path)


def rmtree(path: Path) -> None:
    hook = {"onexc": _make_writable} if sys.version_info >= (3, 12) else {"onerror": _make_writable}
    shutil.rmtree(path, **hook)


@unittest.skipUnless(shutil.which("git"), "git is not installed")
class SyncStatusTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="sync_status_test_"))
        config = self.tmp / "gitconfig"  # isolate from the user's global Git config
        config.write_text("[init]\n\tdefaultBranch = main\n")
        self.env = {**os.environ, "GIT_CONFIG_GLOBAL": str(config), "GIT_CONFIG_NOSYSTEM": "1",
                    "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.com",
                    "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.com"}
        self.remote = self.tmp / "remote.git"
        self.git(self.tmp, "init", "-q", "--bare", "-b", "main", str(self.remote))
        self.local = self.clone("local")
        self.other = self.clone("other")

    def tearDown(self):
        rmtree(self.tmp)

    def git(self, cwd, *args):
        return subprocess.run(["git", *args], cwd=cwd, env=self.env, capture_output=True, text=True,
                              check=True).stdout.strip()

    def clone(self, name):
        self.git(self.tmp, "clone", "-q", str(self.remote), name)
        return self.tmp / name

    def commit(self, repo, path, content):
        (repo / path).write_text(content)
        self.git(repo, "add", path)
        self.git(repo, "commit", "-q", "-m", f"edit {path}")

    def publish(self, repo):
        self.git(repo, "push", "-q", "origin", "HEAD:main")  # to the local stand-in remote only

    def shared_base(self):
        self.commit(self.local, "notes.md", "base\n")
        self.commit(self.local, "data.csv", "t,v\n")
        self.publish(self.local)
        self.git(self.other, "pull", "-q", "origin", "main")

    def status(self, *flags):
        proc = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(self.local), *flags],
                              env=self.env, capture_output=True, text=True)
        state = proc.stdout.strip().splitlines()[-1].removeprefix("STATE: ")
        return state, proc.returncode, proc.stdout

    def test_no_commits_anywhere(self):
        self.assertEqual(self.status("--fetch")[:2], ("NO_COMMITS_YET", 0))

    def test_local_commits_never_pushed(self):
        self.commit(self.local, "notes.md", "base\n")
        self.assertEqual(self.status("--fetch")[:2], ("NOT_PUSHED", 0))

    def test_up_to_date(self):
        self.shared_base()
        self.assertEqual(self.status("--fetch")[:2], ("UP_TO_DATE", 0))

    def test_behind_without_pull_changes_nothing(self):
        self.shared_base()
        self.commit(self.other, "notes.md", "remote edit\n")
        self.publish(self.other)
        self.assertEqual(self.status("--fetch")[:2], ("BEHIND", 0))
        self.assertEqual((self.local / "notes.md").read_text(), "base\n")

    def test_behind_fast_forwards_and_keeps_unrelated_local_changes(self):
        self.shared_base()
        self.commit(self.other, "notes.md", "remote edit\n")
        self.publish(self.other)
        (self.local / "data.csv").write_text("t,v\n0,1\n")  # uncommitted edit to another file
        (self.local / "draft.md").write_text("untracked\n")
        state, code, output = self.status("--fetch", "--pull")
        self.assertEqual((state, code), ("FAST_FORWARDED", 0), output)
        self.assertEqual((self.local / "notes.md").read_text(), "remote edit\n")
        self.assertEqual((self.local / "data.csv").read_text(), "t,v\n0,1\n")
        self.assertTrue((self.local / "draft.md").exists())

    def test_behind_with_overlapping_local_change_is_blocked(self):
        self.shared_base()
        self.commit(self.other, "notes.md", "remote edit\n")
        self.publish(self.other)
        (self.local / "notes.md").write_text("local edit\n")
        head = self.git(self.local, "rev-parse", "HEAD")
        state, code, output = self.status("--fetch", "--pull")
        self.assertEqual((state, code), ("BEHIND_BLOCKED", 1))
        self.assertIn("notes.md", output)
        self.assertEqual((self.local / "notes.md").read_text(), "local edit\n")
        self.assertEqual(self.git(self.local, "rev-parse", "HEAD"), head)

    def test_untracked_file_colliding_with_incoming_file_is_blocked(self):
        self.shared_base()
        self.commit(self.other, "results.md", "remote\n")
        self.publish(self.other)
        (self.local / "results.md").write_text("local, untracked\n")
        self.assertEqual(self.status("--fetch", "--pull")[:2], ("BEHIND_BLOCKED", 1))
        self.assertEqual((self.local / "results.md").read_text(), "local, untracked\n")

    def test_ahead_is_left_for_the_owner_to_push(self):
        self.shared_base()
        remote_head = self.git(self.remote, "rev-parse", "main")
        self.commit(self.local, "notes.md", "local commit\n")
        self.assertEqual(self.status("--fetch", "--pull")[:2], ("AHEAD", 0))
        self.assertEqual(self.git(self.remote, "rev-parse", "main"), remote_head)

    def test_diverged_changes_nothing(self):
        self.shared_base()
        self.commit(self.other, "notes.md", "remote edit\n")
        self.publish(self.other)
        self.commit(self.local, "data.csv", "t,v\n9,9\n")
        head = self.git(self.local, "rev-parse", "HEAD")
        self.assertEqual(self.status("--fetch", "--pull")[:2], ("DIVERGED", 1))
        self.assertEqual(self.git(self.local, "rev-parse", "HEAD"), head)
        self.assertEqual((self.local / "notes.md").read_text(), "base\n")

    def test_missing_remote(self):
        self.git(self.local, "remote", "remove", "origin")
        self.assertEqual(self.status("--fetch")[:2], ("NO_REMOTE", 1))


if __name__ == "__main__":
    unittest.main()
