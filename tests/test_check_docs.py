"""Tests for scripts/check_docs.py on a minimal synthetic project tree."""
import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_docs  # noqa: E402


class CheckDocsTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="check_docs_test_"))
        for rel in check_docs.REQUIRED_FILES:
            self.write(rel, "# placeholder\n")
        self.write("PROJECT_STATUS.md", "**Last updated:** 2026-10-29\n")
        self.write("docs/sessions/2026-10-29-setup.md", "# Setup\n")
        self.write("docs/sessions/SESSION_LOG.md", "| 2026-10-29 | [Setup](2026-10-29-setup.md) |\n")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_check(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = check_docs.main(["--root", str(self.root)])
        return code, buffer.getvalue()

    def test_consistent_tree_passes(self):
        code, output = self.run_check()
        self.assertEqual(code, 0, output)

    def test_unindexed_session_log_fails(self):
        self.write("docs/sessions/2026-10-30-calibration.md", "# Calibration\n")
        self.write("PROJECT_STATUS.md", "**Last updated:** 2026-10-30\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("2026-10-30-calibration.md is listed 0 times", output)

    def test_duplicate_index_entry_fails(self):
        self.write("docs/sessions/SESSION_LOG.md",
                   "[Setup](2026-10-29-setup.md)\n[Setup again](2026-10-29-setup.md)\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("listed 2 times", output)

    def test_broken_relative_link_fails(self):
        self.write("README.md", "See [the setup](docs/missing.md).\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("README.md -> docs/missing.md", output)

    def test_link_anchors_must_match_a_heading(self):
        self.write("TODO.md", "## P0: Now (first)\n### Repeat\n### Repeat\nSee [here](#p0-now-first).\n")
        self.write("README.md", "[ok](TODO.md#repeat-1) and [bad](TODO.md#p1-later)\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("README.md -> TODO.md#p1-later (no such heading)", output)
        self.assertNotIn("#repeat-1", output)
        self.assertNotIn("#p0-now-first", output)

    def test_links_inside_code_are_ignored(self):
        self.write("README.md", "```\n[x](nowhere.md)\n```\nInline `[y](nowhere.md)` too.\n")
        code, output = self.run_check()
        self.assertEqual(code, 0, output)

    def test_stale_project_status_fails(self):
        self.write("PROJECT_STATUS.md", "**Last updated:** 2026-10-01\n")
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("newest session log is 2026-10-29", output)

    def test_cataloged_path_must_exist(self):
        self.write("docs/data_catalog.md", "Raw: `data/raw/2026-11-02_EXP-001_sphere/`\n")
        self.assertEqual(self.run_check()[0], 1)
        self.write("data/raw/2026-11-02_EXP-001_sphere/run01.csv", "t,F\n")
        self.assertEqual(self.run_check()[0], 0)

    def test_placeholders_and_layout_roots_are_not_checked(self):
        self.write("docs/data_catalog.md",
                   "`data/raw/YYYY-MM-DD_EXP-NNN_<name>/` and `data/processed/` and `analysis/`\n")
        code, output = self.run_check()
        self.assertEqual(code, 0, output)

    def test_secret_is_reported_without_printing_it(self):
        token = "ghp_" + "A1b2C3d4" * 5
        self.write("analysis/config.py", f'GITHUB = "{token}"\n')
        code, output = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("analysis/config.py:1 looks like a GitHub token", output)
        self.assertNotIn(token, output)


if __name__ == "__main__":
    unittest.main()
