---
name: catchup
description: Start-of-session handoff for the wind tunnel project. Safely fetches from GitHub (fast-forward only, never pushes), reads the project docs in order, checks them against the real files, and reports the current state, discrepancies and the first task. Use at the start of a session or when asked to catch up on the project.
argument-hint: "[optional: what you want to work on this session]"
---

# /catchup: start-of-session handoff

Goal: understand the project as it actually is, from the repository alone, without changing anyone's work.
`/catchup` may fast-forward the branch; it does **not** edit documentation (that is `/wrap`'s job) and never pushes.

Run every command from the repository root.

## Step 1: Check the repository and sync safely

```bash
python scripts/sync_status.py --fetch
```

Read the final `STATE:` line and act on it:

| STATE | Meaning | Action |
|---|---|---|
| `UP_TO_DATE`, `AHEAD`, `NOT_PUSHED` | Nothing to pull | Continue. `AHEAD`/`NOT_PUSHED`: local commits await the owner's push. Mention them. |
| `NO_COMMITS_YET` | Repository has never been committed | The whole project is uncommitted work awaiting the owner's first commit. Commit-based checks in Step 3 do not apply (`git log` exits with "does not have any commits yet"; that is expected). |
| `BEHIND` | Strictly behind; no collision with local changes | Note `git rev-parse --short HEAD` as OLD, run `python scripts/sync_status.py --pull` (already fetched above), then summarize what arrived with `git log --oneline OLD..HEAD` and `git diff --stat OLD..HEAD`. |
| `FAST_FORWARDED` | Only if you passed `--pull` | Summarize incoming changes as above. |
| `BEHIND_BLOCKED`, `PULL_REFUSED` | Incoming changes collide with uncommitted local work | **Do not pull.** Report the overlapping files and ask the owner how to preserve the local work. Continue read-only. |
| `DIVERGED` | Local and GitHub both have new commits | **Do not integrate.** Report both commit lists; the owner decides. Continue read-only. |
| `OPERATION_IN_PROGRESS`, `DETACHED_HEAD`, `REMOTE_HAS_HISTORY`, `NO_REMOTE` | Repository needs human attention | Report the script's advice verbatim. Continue read-only. |
| `FETCH_FAILED`, `ERROR` | Network/auth/Git problem | Say clearly that the remote state is unknown. Continue with local state. |

Never run `git push`, `reset`, `stash`, `rebase`, `merge` (other than the script's fast-forward), `checkout`/`restore`
over modified files, or `clean`. Uncommitted local changes belong to someone. List them; do not touch them.

## Step 2: Read the documentation in order

1. `CLAUDE.md`
2. `PROJECT_STATUS.md`
3. `TODO.md`
4. `PROJECT_BACKGROUND.md`
5. `DECISIONS.md`
6. `docs/experimental_setup.md`
7. `docs/data_catalog.md`
8. `docs/sessions/SESSION_LOG.md`, then the newest one or two session logs (especially "Recommended first task" and
   "Remaining tasks"). Open older logs or source files only when needed.

## Step 3: Verify the real state against the docs

```bash
git status --short                 # may list files created since Step 1
git log --oneline -15              # fails harmlessly when there are no commits yet
python scripts/check_docs.py
python -m unittest discover -s tests
```

Then check, and note every mismatch:

- **Files vs data catalog:** list `data/raw/`, `data/processed/`, `results/`, `analysis/` (whichever exist). Is every
  dataset catalogued? Does every catalogued path exist?
- **Code vs status:** scripts, firmware or analysis present in the repo but not described in `PROJECT_STATUS.md`, or
  described but missing.
- **Claims vs evidence:** anything labelled *Verified* must point to a measurement, calibration or test. If it does not,
  treat it as unverified and say so. Never upgrade a *Preliminary result* to a finding.
- **Commits vs session logs:** commits after the newest session log's date that no log explains.
- **Uncommitted changes** that no document mentions (possibly an unfinished earlier session).
- **TODO vs status:** done tasks still open, or open tasks that the status says are complete.

Do not fix discrepancies now unless the owner asks; list them so the work (or `/wrap`) can reconcile them.

## Step 4: Report the handoff summary

Use this structure; keep it tight and cite files for claims.

```markdown
## Catch-up: <YYYY-MM-DD>

**Sync:** <STATE>. <what was fetched or pulled; incoming commits; or why nothing was pulled>
**Local uncommitted changes:** <none | list>

**Goal and stage:** <one or two lines>
**Current setup:** <tunnel, instruments, DAQ, software, with status labels>
**Completed and verified:** <items + evidence links>
**Implemented or preliminary (not verified):** <items>
**Recent changes from GitHub:** <commits/files, or "none">
**Experiments and key results:** <EXP IDs, values with units and status, or "none yet">
**Bugs, equipment issues, blockers, uncertainties:** <list>
**Docs vs reality discrepancies:** <list, or "none found">
**Check results:** check_docs <n failures/warnings>, tests <pass/fail>

**Next steps (priority order):** <from TODO.md, adjusted for what you found>
**First task:** <one concrete, actionable task, and why it is first>
```

## Step 5: Continue

If the owner gave a request (`$ARGUMENTS`), start on it with this context. If it conflicts with the documented
priorities or a blocker, say so briefly first. With no request, propose the first task and ask whether to begin.
