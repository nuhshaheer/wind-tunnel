---
name: wrap
description: End-of-session wrap-up for the wind tunnel project. Audits the whole project (git state, code, data, docs), updates every document that needs it, writes or updates this session's log, runs the checks, and gives the owner exact manual commit-and-push commands. Never pushes; makes a local commit only when invoked as "/wrap commit".
argument-hint: "[commit] [session topic]"
disable-model-invocation: true
---

# /wrap: end-of-session audit, documentation and Git handoff

Arguments: `$ARGUMENTS`

- If the arguments contain the word `commit`, the owner authorizes **one local commit** at Step 5. Otherwise leave
  everything uncommitted and unstaged.
- Any other words are a hint for the session topic (used in the session-log filename).
- **Never run `git push`**, under any arguments. The owner pushes.

`/wrap` audits the **whole project**, not just this conversation. It must be safe to run more than once per session.
Run commands from the repository root.

## Step 1: Audit the project

```bash
python scripts/sync_status.py --fetch      # never --pull here; integration is the owner's call at push time
git status --short
git diff --stat
git log --oneline -20
```

Read the actual diffs (`git diff`, and `git diff --cached` if anything is staged) and any new untracked files.
Then list, with evidence:

1. **Work done this session:** from this conversation *and* the diff. They must agree; flag anything in one but not the other.
2. **Earlier work missing from the docs:** commits or files that no session log, status entry or catalog entry describes.
3. **Current implementation and equipment state:** code, firmware, analysis and physical setup as they exist now.
4. **New data, measurements or findings:** new files under `data/`, `results/`; numbers reported by the owner this session.
5. **Bugs, failed approaches, unresolved issues.**
6. **Outdated or contradictory documentation:** statements that are no longer true.
7. **Sensitive or unrelated changes:** secrets, credentials, personal files, scratch output, or edits outside this
   session's scope (for example, the owner's own in-progress edits). These are not yours to stage.

Do not infer experimental success from code. A script that runs is *Implemented, unverified*; a result is
*Preliminary* until validated; *Verified* requires evidence you can link.

## Step 2: Update the documentation

Update every file whose content is now wrong or incomplete, and only those. Do not touch a file just to touch it.

| File | Update when |
|---|---|
| `PROJECT_STATUS.md` | **Every wrap.** Reflect the whole current state; set `**Last updated:**` to today; update stage, tables, blockers, open questions, next steps, last commit. |
| `TODO.md` | **Every wrap.** Move finished tasks to Done (date + session-log link), add new tasks with outcome + verification, re-prioritize. |
| Session log + `docs/sessions/SESSION_LOG.md` | **Every wrap.** See below. |
| `DECISIONS.md` | A meaningful technical decision was made or reversed (append; supersede, never delete). |
| `docs/experimental_setup.md` | Equipment, dimensions, sensors, wiring, DAQ settings or procedures changed (update current config + change history). |
| `docs/data_catalog.md` | Data was acquired, processed or analysed, or a result was produced. |
| `PROJECT_BACKGROUND.md` | Lasting context changed: goals, constraints, governing approach, references reviewed, lessons learned. |
| `README.md`, `CLAUDE.md` | Their instructions or descriptions became inaccurate (structure, commands, workflow). |

### The session log

1. **Find or create it.** If a log for *this* session already exists (you created it earlier in this conversation,
   or its Session ID matches), **update it in place**. Otherwise create
   `docs/sessions/YYYY-MM-DD-<short-topic>.md` (lowercase, hyphens; today's date). If that name is taken by a different
   session, add `-2`, `-3`.
2. **Index it exactly once** in `docs/sessions/SESSION_LOG.md` (newest at the bottom). On a rerun, edit the existing row.
3. **Backfill commit hashes** of earlier sessions: for any log or index row whose commit is "not committed yet", run
   `git log --format=%h -1 -- docs/sessions/<file>` and fill it in. This is the only permitted edit to old logs.
4. Use this structure (write "None" rather than dropping a section):

```markdown
# <YYYY-MM-DD>: <Topic>

- **Session ID:** <Claude Code session ID if visible, e.g. the UUID in the scratchpad path; else "unknown">
- **Agent:** <model / tool>
- **Commit:** not committed yet   <!-- backfilled by a later /wrap -->

## 1. Starting state and objective
## 2. Work completed
## 3. Files and equipment affected
## 4. Experimental procedures performed   <!-- "None. No physical work this session." if so -->
## 5. Commands and scripts executed        <!-- exact commands, so they can be rerun -->
## 6. Measurements and results             <!-- values WITH units, uncertainty, status label, data path -->
## 7. Tests, calibration checks and validation   <!-- each check: command/procedure -> outcome -->
## 8. Errors, failed approaches and troubleshooting
## 9. Decisions and reasoning               <!-- link DECISIONS.md entries -->
## 10. Open questions and blockers
## 11. Remaining tasks
## 12. Recommended first task for the next agent
## 13. Manual Git commands (as given to the owner)
```

Never fabricate history. If something is unknown (e.g. what happened in an unlogged earlier session), say "unknown".

## Step 3: Validate

Run what applies and record each command and its outcome in the session log (§7):

```bash
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

- Changed analysis scripts: rerun them on their documented inputs when practical. Outputs go to `data/processed/` or
  `results/`, **never** over `data/raw/`.
- Experimental work: record units, acquisition settings, calibration and preprocessing, uncertainty and limitations.
  Keep raw observation, processed result and interpretation separate. Do not claim a conclusion the data cannot support.
- State explicitly when no physical experiment or equipment check was performed. An agent cannot perform one; only the owner's reported results count.

## Step 4: Audit consistency

Rerun `python scripts/check_docs.py` after editing. It must report **0 failures** (fix them or explain why not). Then confirm by reading:

- [ ] `PROJECT_STATUS.md` matches the actual code, data and setup, and labels match the evidence.
- [ ] Every result links to its data and analysis script; every catalogued path exists; every data folder is catalogued.
- [ ] `TODO.md` matches the status (no done items open, no open items marked done).
- [ ] The session log records what actually happened, including failures and checks not performed.
- [ ] Decisions and open questions are written down.
- [ ] No invented numbers, specs, citations or results.
- [ ] A new agent could find the next task from `PROJECT_STATUS.md` + `TODO.md` + this session log alone.

## Step 5: Prepare local Git changes

Classify every path in `git status --short`:

- **Include:** this session's work and the documentation updates. New raw data that is catalogued and within the size policy.
- **Exclude:** secrets, credentials, `.env`, scratch output, generated files that `.gitignore` should cover (fix
  `.gitignore` if needed), files over 25 MB (see DECISIONS.md D-004).
- **Ask the owner:** unrelated edits not made in this session, large or binary files, anything ambiguous.

Never `git add -A` or `git add .`. Name files explicitly.

- **Default (no `commit` argument):** stage nothing, commit nothing.
- **`/wrap commit`:** `git add <explicit include list>`, check `git diff --cached --stat`, then
  `git commit -m "<summary>" -m "<body>"`. Make exactly one commit, only if Steps 3–4 pass. Report the hash. Do not
  amend existing commits and do not create empty commits. The session log's commit field stays "not committed yet"
  until the next `/wrap` backfills it.

## Step 6: Give the owner exact manual Git commands

Base them on the real state from `sync_status.py` and `git status`, not on a template. Always state:

- **Where:** `cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"` (forward slashes and quotes work in
  both PowerShell and Git Bash; the VS Code terminal is fine).
- **Which files** will be staged, as an explicit `git add` list (quote paths with spaces).
- **Inspect:** `git status`, `git diff` before staging; `git diff --cached` after.
- **Commit:** `git commit -m "<summary>" -m "<body>"` (skip if `/wrap commit` already committed).
- **Push**, and what each command does, chosen by state:

| STATE | Push instructions |
|---|---|
| `NOT_PUSHED` / first push | `git push -u origin main` (creates the branch on GitHub and sets tracking). |
| `UP_TO_DATE` / `AHEAD` | `git push origin HEAD` (or `git push` once tracking is set). |
| `BEHIND` (no overlap) | Before committing: `git pull --ff-only`. Then commit and push. |
| `BEHIND_BLOCKED` or `DIVERGED` | Commit first, then `git pull --rebase origin main`; resolve any conflicts (`git status` shows them; edit, `git add <file>`, `git rebase --continue`; `git rebase --abort` returns to the pre-rebase state). Rerun the tests, then push. Explain which files will conflict if known. |
| `FETCH_FAILED` | Remote state unknown: run `git fetch origin` and `git status` first, then follow the matching row. |

If push asks for credentials: `gh auth status` / `gh auth login`, or sign in through Git Credential Manager.
Put the same commands in the session log (§13).

## Step 7: Rerun safety

Same session → same log file, same index row; no duplicate entries. Do not rewrite historical records beyond the
commit-hash backfill. Do not discard or revert anyone's changes. No meaningless commits. If any step fails, leave
local work in place and report exactly what is incomplete.

## Step 8: Handoff report (final message to the owner)

1. Current project state (stage and one-line summary).
2. Work completed this session.
3. Documentation updated (file → what changed).
4. Experiments, results and verification performed, plus checks **not** performed.
5. Known issues and uncertainties.
6. Next recommended tasks (first one marked).
7. Local Git status and changed files (staged? committed?).
8. Exact commands to commit and push (from Step 6).
9. Remaining manual actions for the owner.

End with "Nothing has been pushed to GitHub." **only after confirming it** (`python scripts/sync_status.py` shows
local commits as ahead, or nothing was committed).
