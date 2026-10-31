# Wind Tunnel

> **Status (2026-10-29): planning / pre-build.** Nothing is built and no data has been collected yet.
> The authoritative current state is [PROJECT_STATUS.md](PROJECT_STATUS.md); the next tasks are in [TODO.md](TODO.md).

## Goal
Measure drag, and prove the tunnel reads true.

## What this project is about
A small wind tunnel with my own instrumentation: flow conditioning, a pitot tube for airspeed, and a load cell for drag force, with signal conditioning built from my ECE kit. Before trusting any other result, I validate the tunnel by measuring something with a known answer: the drag coefficient of a sphere (~0.47). It's the same move as the 100 MΩ resistor on the STM.

## Why it matters
Of the three projects, this is the only one that shows me as a mechanical engineer doing fluids, which is the work aerospace companies hire MEs into.

## Hardware

### Have (instrumentation half, from the ECE kit)
- LM741 / LM348 op-amps for signal conditioning
- LM317 regulator for a clean sensor supply

### To buy
- Blower / fan
- Ducting
- Honeycomb + screens (flow straightening)
- Pitot tube
- Differential pressure sensor
- Load cell + HX711
- Servo for the airfoil pitch mechanism

## Build order
1. Size the contraction and test section
2. Flow conditioning (honeycomb + screens)
3. Map flow uniformity across the test section with the pitot tube
4. Load cell and its conditioning circuit
5. Calibrate against known weights
6. Validation run (sphere Cd)
7. Airfoil pitch attachment

## Result / deliverable
The measured Cd of a sphere compared against the published value of ~0.47.

---

## Repository structure

```text
CLAUDE.md                 Instructions for AI agents (rules, reading order, conventions)
PROJECT_STATUS.md         Authoritative snapshot of the current state
PROJECT_BACKGROUND.md     Goals, physics and equations, uncertainty sources, references
DECISIONS.md              Chronological technical decisions
TODO.md                   Prioritized tasks with verification criteria
docs/
  experimental_setup.md   The physical setup as built (Unknown until decided)
  data_catalog.md         Every dataset/experiment and how it was processed
  sessions/               One log per work session + SESSION_LOG.md index
data/README.md            Data layout and rules (raw vs processed, naming, units, large files)
resources/                Reference papers (PDFs) with reading notes; index and naming rules in resources/README.md
scripts/                  Helper scripts used by /catchup and /wrap
tests/                    Tests for the helper scripts
.claude/                  Agent commands (skills/) and the no-push permission rule (settings.json)
```

Folders such as `data/raw/`, `data/processed/`, `analysis/`, `results/` and `cad/` are created when their first file
exists (see [data/README.md](data/README.md)).

## Documentation

Start with [PROJECT_STATUS.md](PROJECT_STATUS.md) and [TODO.md](TODO.md). Then
[PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md), [DECISIONS.md](DECISIONS.md),
[docs/experimental_setup.md](docs/experimental_setup.md), [docs/data_catalog.md](docs/data_catalog.md) and the
[session log index](docs/sessions/SESSION_LOG.md).

## Data and analysis workflow

- Raw sensor logs go in `data/raw/YYYY-MM-DD_EXP-NNN_description/` and are never edited.
- Scripts in `analysis/` turn raw data into `data/processed/` and `results/`; every result is reproducible from raw data + script.
- Every dataset gets an entry in [docs/data_catalog.md](docs/data_catalog.md).
- Videos stay out of Git (external storage, referenced from the catalog); Git LFS is not enabled yet ([DECISIONS.md](DECISIONS.md) D-004).

No analysis code exists yet, so there are no analysis commands to run.

## Requirements and checks

The helper scripts need only Python 3 (standard library; Python 3.9 or newer expected, developed and tested with
Python 3.13 on Windows 11) and Git.

```bash
python -m unittest discover -s tests -v   # tests for the helper scripts
python scripts/check_docs.py              # documentation consistency, file-size and secret checks
python scripts/sync_status.py --fetch     # where the local branch stands relative to GitHub
```

## Working with AI agents: `/catchup` and `/wrap`

These are Claude Code project skills in `.claude/skills/`. Type them in a Claude Code session opened in this folder.
They are plain Markdown, so other agents can follow them by reading the files.

- **`/catchup`** (start of a session): fetches from GitHub and fast-forwards only when that cannot touch local work;
  reads the docs in order; checks them against the actual files; reports the state, discrepancies and the first task.
  Add a request after it, e.g. `/catchup size the test section`.
- **`/wrap`** (end of a session): audits the whole project, updates every document that needs it, writes or updates
  the session log, runs the tests and checks, and prints the exact Git commands for you to run.
  `/wrap commit` also lets the agent make one local commit. **Agents never push.** `.claude/settings.json` denies
  `git push` for agents, and `CLAUDE.md` forbids it.

## Pushing to GitHub (manual)

GitHub repository: https://github.com/nuhshaheer-2007/wind-tunnel (private). Remote `origin`, branch `main`.
Run in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git status                       # what changed
git diff                         # review changes to tracked files
git add <files listed by /wrap>  # stage specific files, never blindly everything
git diff --cached                # review exactly what will be committed
git commit -m "Summary" -m "Why"
git push                         # first time: git push -u origin main
```

If GitHub has commits you don't have, run `git pull --rebase origin main` before pushing. `/wrap` tells you when that
applies and what to do about conflicts.
