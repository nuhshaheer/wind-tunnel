# 2026-10-29: GitHub setup and agent handoff system

- **Session ID:** 87b8e38e-7b05-46d0-b116-8e18cc4677ba (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** `cc51fff` (backfilled 2026-10-31)

## 1. Starting state and objective

**Starting state (inspected):** the project folder contained a single file, `README.md` (1,384 bytes, dated
2026-10-25): the project plan (goal, hardware on hand and to buy, build order, deliverable). No Git repository, no code,
no data, no CAD, no photos. No GitHub repository named `wind-tunnel` existed. GitHub CLI was authenticated as
`nuhshaheer-2007` (scopes include `repo`). Git LFS 3.7.1 was installed. The sibling project `1 - Mecanum SLAM Robot` had
been set up the same day with a private, empty `slam-robot` repo, and its `.gitignore`/`.gitattributes` conventions were reused.

**Objective (owner's request):** turn the project into a documented, GitHub-backed project that survives AI-agent
handoffs: documentation set, `/catchup` and `/wrap` commands, data-management policy, and no automatic pushes.

## 2. Work completed

- Created private GitHub repo `nuhshaheer-2007/wind-tunnel` (empty; description as requested). **Nothing pushed.**
- `git init -b main`; remote `origin` = https://github.com/nuhshaheer-2007/wind-tunnel.git; verified that `git fetch` and
  `git ls-remote` succeed (remote empty).
- Repo configuration: `.gitignore` (secrets, Claude Code runtime files, Python, firmware builds, videos, scratch,
  OS/OneDrive clutter), `.gitattributes` (LF normalization; `data/raw/**` stored byte-for-byte; binary types), and
  `.claude/settings.json` (denies `git push` for the agent's Bash and PowerShell tools).
- Documentation from evidence (the README only): `CLAUDE.md`, `PROJECT_STATUS.md`, `PROJECT_BACKGROUND.md`,
  `DECISIONS.md` (D-001 to D-004), `TODO.md`, `docs/experimental_setup.md`, `docs/data_catalog.md`, `data/README.md`,
  this log and the index. The original README text was kept verbatim; a status banner and new sections were added.
- Agent commands as Claude Code project skills: `.claude/skills/catchup/SKILL.md`, `.claude/skills/wrap/SKILL.md`.
- Helper scripts (standard-library Python): `scripts/sync_status.py` (sync state; fast-forward only when safe; never
  pushes) and `scripts/check_docs.py` (required files, session index, links and anchors, catalog paths, status
  freshness, file sizes, secrets). Tests: `tests/test_sync_status.py` (10), `tests/test_check_docs.py` (10).
- Order-of-magnitude design estimates (sphere drag, q, Re, blockage) computed and recorded in
  `PROJECT_BACKGROUND.md` as assumptions, not results.
- Fresh-agent `/catchup` handoff test run; its findings were fixed (see §7–§8).
- `/wrap` run on this session (this update).

## 3. Files and equipment affected

Created: `.gitignore`, `.gitattributes`, `.claude/settings.json`, `.claude/skills/catchup/SKILL.md`,
`.claude/skills/wrap/SKILL.md`, `CLAUDE.md`, `PROJECT_STATUS.md`, `PROJECT_BACKGROUND.md`, `DECISIONS.md`, `TODO.md`,
`data/README.md`, `docs/experimental_setup.md`, `docs/data_catalog.md`, `docs/sessions/SESSION_LOG.md`, this file,
`scripts/sync_status.py`, `scripts/check_docs.py`, `tests/test_sync_status.py`, `tests/test_check_docs.py`.
Modified: `README.md` (status banner at top, sections appended; original text unchanged).
Equipment: none.

## 4. Experimental procedures performed

None. No physical work this session; no hardware exists yet.

## 5. Commands and scripts executed

```bash
gh auth status; gh repo list nuhshaheer-2007; gh api repos/nuhshaheer-2007/wind-tunnel   # 404 before creation
gh repo create wind-tunnel --private --description "Wind tunnel project: experimental setup, data collection, analysis, and engineering development."
git init -b main
git remote add origin https://github.com/nuhshaheer-2007/wind-tunnel.git
git fetch origin; git ls-remote origin            # both exit 0; remote empty
python -m unittest discover -s tests -v
python scripts/check_docs.py
python scripts/sync_status.py --fetch
git push -h                                        # deny-rule probe (prints usage only; cannot push)
```

The design estimates were computed with a short inline Python calculation (formulas and assumed values are listed in
`PROJECT_BACKGROUND.md`, Order-of-magnitude estimates).

## 6. Measurements and results

No measurements. Calculated estimates only (assumptions: ρ = 1.20 kg/m³, μ = 1.81×10⁻⁵ Pa·s, C_D = 0.47):
a 50 mm sphere at 10 m/s gives q ≈ 60 Pa, drag ≈ 0.055 N (≈ 5.7 gf), Re ≈ 3.3×10⁴. Status: estimate, not a result.
The fresh agent independently re-checked this arithmetic and found it correct.

## 7. Tests, calibration checks and validation

| Check | Outcome |
|---|---|
| `python -m unittest discover -s tests -v` (first run) | 9 errors and 2 failures. Fixed (see §8). |
| `python -m unittest discover -s tests -v` (final) | **20 tests, all passed** |
| `python scripts/check_docs.py` (final) | **0 failures, 0 warnings**: 12 required files, 1 session log indexed once, 41 links and anchors resolve, 20 committable files, no secrets |
| `python scripts/sync_status.py --fetch` | `STATE: NO_COMMITS_YET` (correct: remote empty, no local commits) |
| No-push guard: `git push -h` via the agent's Bash tool and its PowerShell tool | **Blocked** by Claude Code in both ("Permission ... has been denied"). The probe only prints usage, so no push could have happened. |
| Fresh-agent handoff test of `/catchup` | **Passed.** A general-purpose subagent with no conversation history followed `.claude/skills/catchup/SKILL.md` read-only. It reported the correct state (planning/pre-build, nothing verified physically, open questions, Tentative decisions) and the correct first task (build step 1), and re-ran the checks (0 failures; 19 tests OK at that time). It found 5 issues, all fixed (§8). |
| `/wrap` | Run once by the agent that wrote it (this update). Not yet independently tested; TODO P0. |
| Calibration or equipment checks | **None performed.** No hardware exists. |

Only the `NO_COMMITS_YET` sync state was exercised live. The other states (behind, ahead, diverged, collisions with
local changes, missing remote) are covered by unit tests against throwaway local repositories, not by a live GitHub run.

## 8. Errors, failed approaches and troubleshooting

- `sync_status.py` first misread a fresh clone of an empty repository. Git reports an upstream (`origin/main`) from the
  tracking config even when that remote branch does not exist yet. Fixed by also checking that `@{u}` resolves.
  Covered by `test_no_commits_anywhere` and `test_local_commits_never_pushed`.
- `sys.stdout.reconfigure` crashed when the tests redirected stdout to `StringIO`. Moved it to the `__main__` block.
- `.gitignore` initially had a blanket `build/` rule (copied from the robot project). Removed, because in this project
  "build" can mean the physical tunnel build.
- An anchor link in DECISIONS.md D-001 was wrong (the `[Standard]` tag in the heading is part of the GitHub slug).
  Fixed by hand. `check_docs.py` did not catch it then.
- Issues found by the fresh-agent handoff test, all fixed:
  1. `.claude/scheduled_tasks.lock` (a Claude Code runtime file created by this session's wake-up timer) was not ignored.
     Added `.claude/*.lock` to `.gitignore`.
  2. `check_docs.py` ignored `#anchors`. It now validates them against GitHub-style heading slugs (new test
     `test_link_anchors_must_match_a_heading`).
  3. This log's Git-commands section was still a placeholder, which left the owner's P0 TODO without commands. Filled in by this `/wrap`.
  4. Status labels were inconsistent ("Implemented unverified" in CLAUDE.md vs "Implemented, unverified"
     elsewhere; TODO "Done" vs status "unverified"). Aligned. Inventory columns now say "Availability".
  5. `/catchup` did not say what to expect with no commits (`git log` exits 128). Added a `NO_COMMITS_YET` row and a note.
- Not changed: the session ID taken from the scratchpad path is shared by subagents of the same session. `/wrap`
  identifies "this session's log" primarily by the conversation that created it, so this is acceptable.

## 9. Decisions and reasoning

- D-003: repo, documentation system, skills, and the no-push rule enforced by a permission deny rule. Repo visibility
  private is Tentative.
- D-004: data management (raw immutable, videos external, no LFS yet). Tentative.
- D-001, D-002: recorded from the original README (sphere validation; sensor approach).

## 10. Open questions and blockers

See `PROJECT_STATUS.md` §10. Key ones: microcontroller/DAQ not identified; role of the op-amp circuit unclear
(HX711 already amplifies the bridge; LM741 not rail-to-rail); test-section size, speed and sphere diameter not chosen;
pressure-sensor range and load-cell capacity not chosen; Re-matched reference Cd not yet cited.

## 11. Remaining tasks

See `TODO.md`. Owner: review and push the initial commit; confirm D-003/D-004. Next session: verify `/wrap`
independently; start build step 1.

## 12. Recommended first task for the next agent

Run `/catchup`. If the owner has pushed, the sync state should be `UP_TO_DATE`; backfill this log's commit hash at
the next `/wrap`. Then start build step 1: **size the contraction and test section.** Pick a target airspeed range,
test-section cross-section and sphere diameter; recompute Re, blockage and expected drag; record the design and
reasoning in `docs/experimental_setup.md` and `DECISIONS.md`. Sensor ranges and load-cell capacity follow from these numbers.

## 13. Manual Git commands (as given to the owner)

See [Manual Git commands](#manual-git-commands) below.

## Manual Git commands

State at wrap time: `NO_COMMITS_YET`. Nothing committed or staged; GitHub repo empty. These commands make the first
commit and the first push. Run them in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git status
git add .gitignore .gitattributes .claude/settings.json .claude/skills/catchup/SKILL.md .claude/skills/wrap/SKILL.md
git add README.md CLAUDE.md PROJECT_STATUS.md PROJECT_BACKGROUND.md DECISIONS.md TODO.md
git add data/README.md docs/experimental_setup.md docs/data_catalog.md docs/sessions/SESSION_LOG.md docs/sessions/2026-10-29-github-setup-and-agent-handoff.md
git add scripts/sync_status.py scripts/check_docs.py tests/test_sync_status.py tests/test_check_docs.py
git status
git diff --cached --stat
git diff --cached
git commit -m "Set up project docs, agent handoff workflow and repo config" -m "Adds status, background, decisions, TODO, setup, data catalog and session-log docs; the /catchup and /wrap Claude Code skills with helper scripts and tests; .gitignore and .gitattributes; and a permission rule that blocks agent pushes. The original README plan is kept verbatim."
git push -u origin main
python scripts/sync_status.py --fetch
```

- `git status` lists 20 untracked files before staging; afterwards they appear as "new file". `.claude/scheduled_tasks.lock`
  and `__pycache__/` are ignored and must not appear.
- All files are new, so plain `git diff` shows nothing. Review with `git diff --cached` after staging (press `q` to leave the pager).
- `git push -u origin main` creates `main` on GitHub and sets tracking, so later pushes are just `git push`.
- The last command should end with `STATE: UP_TO_DATE`.
- If Git warns "LF will be replaced by CRLF", that is harmless: it is the Windows checkout setting; the repository stores LF.
- If the push asks for credentials: `gh auth status`, or `gh auth login`, then retry.
- If the push is rejected ("fetch first" / "non-fast-forward"), GitHub is no longer empty and its history is unrelated
  to yours. Do not force-push. Stop, run `python scripts/sync_status.py --fetch`, and decide (or ask an agent to
  explain the options) before changing anything.
