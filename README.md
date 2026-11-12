# Wind Tunnel

> **Status (2026-11-10): planning / pre-build.** Every part except the fan is ordered (2026-11-09/10); nothing is
> built yet and no data has been collected. Next: sizing the tunnel (build step 1) while the parts arrive.
> The authoritative current state is [PROJECT_STATUS.md](PROJECT_STATUS.md); the next tasks are in [TODO.md](TODO.md).
> The complete parts list is [docs/buy_list.md](docs/buy_list.md), and the order tracker is
> [docs/shopping_list.md](docs/shopping_list.md).

## Goal
Measure drag, and prove the tunnel reads true.

## What this project is about
A small wind tunnel with my own instrumentation: flow conditioning, a pitot tube for airspeed, and a load cell for drag force, read through an interface board I design with parts from my ECE kit. Before trusting any other result, I validate the tunnel by measuring something with a known answer: the drag coefficient of a sphere (about 0.42–0.445 at this tunnel's Reynolds number, ±10 %; the original plan said ~0.47). It's the same move as the 100 MΩ resistor on the STM.

## Why it matters
Of the three projects, this is the only one that shows me as a mechanical engineer doing fluids, which is the work aerospace companies hire MEs into.

## Hardware (as of 2026-11-10)

The tunnel: an open-circuit blower with the fan at the front, a 100 mm × 100 mm test section, 3D-printed in bolted
segments, with a 13 m/s target top speed ([DECISIONS.md](DECISIONS.md) D-005, D-007, D-008, D-010, D-013).
The model sits on a brass sting that rises through a replaceable floor insert, with the sting shield attached to the
insert; the top window lifts off on magnets, and the sting clamps into a printed mount on the load cell (D-014 to
D-016). Reasons, prices and alternatives for every part: [docs/buy_list.md](docs/buy_list.md).

### On hand
- Bambu Lab P1S 3D printer, PLA, PETG-CF and a hardened-steel nozzle
- Elegoo Mega 2560 (working: Blink upload verified 2026-11-02)
- ECE2010 lab kit (op-amps, regulators, breadboard, jumpers)
- Multimeter, soldering station, bench power supply, calipers, hand drill, spirit level, 43 magnets (8 × 2 mm), and
  access to a school lab balance

### Ordered (2026-11-09/10)
- Airspeed: a Sensirion SDP810-125Pa differential pressure sensor, with a home-made brass pitot probe and wall
  pressure taps
- Drag: two TAL221 100 g load cells and a SparkFun HX711
- Air density: a Waveshare BME280 (pressure, temperature, humidity)
- Flow conditioning: aluminium window screen (the honeycomb is printed)
- Validation models: 3/4 in and 1 in Delrin balls, each on its own brass sting
- Build parts: black PLA, 1/8 in cast acrylic windows, heat-set inserts, screws, tubing and fittings, neoprene, tools
  and a calibration weight set

### Still to buy
- The fan: AC Infinity CLOUDLINE S6 (recommended) or VEVOR 6-inch, bought last (D-011)

### Changed from the original plan
- No servo for the airfoil pitch: preset angles instead (2026-11-01)
- No ducting: the fan's collar slides into a printed inlet
- No bought pitot tube: made in-house from brass tube
- No on-tunnel display or knob: all output goes to the laptop (D-012)
- Op-amp signal conditioning probably not needed, because the sensors are digital (proposed); the circuit work goes
  into an interface board, breadboard first, then a PCB

## Build order
1. Size the contraction and test section ← **next**
2. Flow conditioning (honeycomb + screens)
3. Map flow uniformity across the test section with the pitot tube
4. Load cell and its conditioning circuit
5. Calibrate against known weights
6. Validation run (sphere Cd)
7. Airfoil tests at preset angles

## Result / deliverable
The measured Cd of a sphere compared against the published value at the same Reynolds number: Brown and Lawler (2003)
Eq. (19), about 0.42–0.445 for the planned runs, ±10 %, plus a check that Cd rises with Re as predicted
([DECISIONS.md](DECISIONS.md) D-009). The original plan compared against ~0.47.

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
  buy_list.md             Everything to buy, what each part does, prices, and what is on hand
  shopping_list.md        The owner's order tracker: item, qty, price, link, status (To buy → Ordered → Got it)
  data_catalog.md         Every dataset/experiment and how it was processed
  sessions/               One log per work session + SESSION_LOG.md index
  sketches/               The owner's hand sketches of the tunnel (intent, not as built)
  drawings/               Preliminary drawing package (HTML) and the Python scripts that generate it
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

The helper scripts need only Python 3 (standard library; Python 3.9 or newer expected) and Git. The tests pass on
Python 3.11 on Windows 11 (last run 2026-11-10); earlier sessions used 3.13.

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

GitHub repository: https://github.com/nuhshaheer/wind-tunnel (private; the account was `nuhshaheer-2007` until
2026-11-02, and the old URL redirects). Remote `origin`, branch `main`.
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
