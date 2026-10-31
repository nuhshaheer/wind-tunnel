# Project Status

**Last updated:** 2026-10-31
**Last commit:** `5bc60f0` (2026-10-31, literature review), pushed to `origin/main`; `sync_status.py --fetch`
reported `UP_TO_DATE` afterwards. The second `/wrap`'s doc updates are **not committed yet** (commands in the
[session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md#follow-up-commit-second-wrap)).
**Current stage:** Planning / pre-build. Design research under way: three reference papers reviewed, construction
method chosen (segmented 3D printing). No hardware built, no data collected, no analysis code written.

This is the authoritative snapshot of the project. Status labels used below:
**Verified**, **Implemented, unverified**, **Preliminary result**, **In progress**, **Planned**,
**Blocked**, **Tentative**. Session-by-session history is in [docs/sessions/SESSION_LOG.md](docs/sessions/SESSION_LOG.md).

## 1. Objectives

Build a small wind tunnel with my own instrumentation, measure drag, and prove the tunnel reads true. The validation
is the drag coefficient of a sphere, compared against the published value of about 0.47. Source: the original
project README (2026-10-25). Long-term context is in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md).

| Objective | Status |
|---|---|
| Tunnel built with flow conditioning | Planned (design research In progress) |
| Airspeed measured with pitot tube + differential pressure sensor | Planned |
| Drag force measured with load cell + HX711 | Planned |
| Load cell calibrated against known weights | Planned |
| Sphere Cd validation run (deliverable) | Planned |
| Airfoil pitch mechanism (servo) | Planned (after validation) |
| Flow visualization with a water-mist generator | Planned, optional (owner's idea, 2026-10-30; [TODO.md](TODO.md) P2) |

## 2. Wind tunnel configuration

**Nothing built. Test-section size, airspeed, fan and tunnel type are not chosen.** Details and unknowns are in
[docs/experimental_setup.md](docs/experimental_setup.md).

| Item | State | Source |
|---|---|---|
| Construction | 3D-printed segments on the owner's Bambu Lab P1S, with alignment holes; glue Tentative. The tunnel will be "decently big" (owner) | [D-005](DECISIONS.md) (Accepted) |
| Tunnel type | Not chosen. The papers favour an open-circuit **blower** tunnel (centrifugal fan at the inlet); a suction tunnel would make mist injection easier | [Mehta1979](resources/notes/Mehta1979.md) |
| Contraction | Proposed, not decided: contraction ratio 6–9, square section, 5th-order-polynomial wall, length about 1.0 × inlet height | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md), [Mehta1979](resources/notes/Mehta1979.md) |
| Settling chamber | Proposed: honeycomb (cell length 6–8 diameters, about 150 cells across), then screens about 0.2 D apart, the last one with open area above 57 % | [Mehta1979](resources/notes/Mehta1979.md) |
| Test section | Proposed: sphere at least about 0.5 D downstream of the contraction exit; sphere blockage a few percent | [Mehta1979](resources/notes/Mehta1979.md), [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#printable-contraction-sizes) |

## 3. Hardware and instrumentation

| Item | Availability | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | On hand (owner has access, stated 2026-10-30) | Build volume 256 × 256 × 256 mm (manufacturer spec). Filament unknown |
| LM741 / LM348 op-amps | On hand (per README) | Intended for signal conditioning; exact role not defined (see open questions) |
| LM317 regulator | On hand (per README) | Intended for a clean sensor supply |
| Blower / fan | To buy | Model unknown. Required flow and pressure estimated in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#fan-requirement-estimates) (assumptions, not specs) |
| Ducting | To buy (may be printed, D-005) | |
| Honeycomb + screens | To buy | |
| Pitot tube | To buy | Type (pitot vs pitot-static) not specified |
| Differential pressure sensor | To buy | Model and range unknown |
| Load cell + HX711 | To buy | Capacity unknown. HX711 datasheet not yet obtained (on the resources "Wanted" list) |
| Servo (airfoil pitch) | To buy | |
| Microcontroller / DAQ | **Not identified** | Not listed in the original plan; needed to read the HX711 and pressure sensor |
| Ultrasonic mist maker (optional visualization) | Not decided | Product in the video the owner found is unidentified |

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | Planned; not started |
| Analysis scripts (`analysis/`) | Planned; not started |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote). States seen live so far, each correct for the situation: `NO_COMMITS_YET`, `UP_TO_DATE`, `FETCH_FAILED`, `AHEAD` (the last two on 2026-10-31, in the owner's terminal) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and clean runs on this repo |
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `UP_TO_DATE`). The push first failed because of a PC network fault, not the commands. One content error: the first run's log blamed that failure on the agent sandbox; the second run corrected it ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only (developed with Python 3.13 on Windows 11). Git 2.54, Git LFS 3.7
(installed, not enabled), GitHub CLI 2.97.

## 5. Current experiments

None. No experiment has been run.

## 6. Work completed

- 2026-10-25: project plan written (original README: goal, hardware list, build order).
- 2026-10-29: repository, documentation system and agent workflow set up. See [the session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md).
- 2026-10-30/31: literature review and design inputs. Created `resources/` and reviewed three papers
  (Abdelhamed2014, Bell1988, Mehta1979). Recorded D-005 (segmented printing), estimates of printable sizes and fan
  requirements, a list of further documents, and the optional mist-visualization idea. See
  [the session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md).
- 2026-10-31: the owner committed and pushed this as `5bc60f0`, after fixing a network fault on the PC (no IPv4
  address). `/wrap` verified. Same session log.

## 7. Data and analyses

No data collected. No analyses completed. See [docs/data_catalog.md](docs/data_catalog.md).

## 8. Results

| Result | Status | Source |
|---|---|---|
| None yet | n/a | n/a |

Design estimates are in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#order-of-magnitude-estimates): sphere drag,
printable contraction sizes and fan requirements. They are **calculations from assumed values, not results**.

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on choosing and buying hardware (fan, sensors, load cell, microcontroller).
  Sizing waits on owner inputs (open question 3).
- No known software bugs.
- Network (resolved 2026-10-31): the PC lost its IPv4 address, which blocked GitHub and some other sites. If
  `FETCH_FAILED` with "Could not resolve host" comes back, see Lessons learned in
  [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#lessons-learned).
- Risk: the project folder is inside OneDrive. OneDrive syncing a `.git` folder can cause conflicts if the repo is
  edited from two machines. GitHub, not OneDrive, is the source of truth between machines.
- Copyright: `resources/Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf` is under Cambridge Core terms of
  use, and the Abdelhamed2014 licence is not checked. Fine while the repo is private (D-003); review before making it public.

## 10. Open engineering questions

1. Which microcontroller or DAQ reads the HX711 and the pressure sensor? (Not in the original plan.) The ASEE 2024
   paper on the resources "Wanted" list used an Arduino with HX711s.
2. What is the op-amp signal conditioning for? The HX711 already amplifies and digitizes the load-cell bridge, so the
   op-amps may be meant for the pressure sensor. LM741 needs roughly ±(5–15) V supplies and is not rail-to-rail,
   which may not suit a single low-voltage supply. Unresolved.
3. **Test-section size, top airspeed and sphere diameter.** These set Re, blockage, force and fan size. Not chosen.
   Owner inputs needed: available floor or bench length, target top speed, any fan already in mind.
4. Pressure-sensor range: dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate). A sensor with a ±2 kPa
   range would use a small fraction of its span. Not chosen.
5. Load-cell capacity: expected sphere drag is only a few grams-force (estimate). The load cell also carries
   the sphere's support (sting/mount), whose drag must be measured and subtracted. Not chosen.
6. Which published Cd value applies at the test Reynolds number? Achenbach (1972) covers only Re ≥ 5×10⁴, while the
   planned Re is roughly 10⁴–10⁵. Candidates: the Morrison (2013) correlation and Roos & Willmarth (1971) data
   (resources "Wanted" list).
7. Blower vs suction tunnel, and whether to fit an exit diffuser. The diffuser roughly halves fan power (estimate)
   but adds length and printing.
8. Blockage correction method for the sphere (Maskell 1963; AGARD-AG-336 chapter 6; both on the "Wanted" list).

## 11. Important measurements and findings

None measured yet. Literature findings that shape the design are summarized in the notes under `resources/notes/`.

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:** commit and push the second `/wrap`'s small doc update (commands in the
   [session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md#follow-up-commit-second-wrap)). Then
   provide the sizing inputs (open question 3), and confirm or change D-003 and D-004.
2. **Build step 1:** size the contraction and test section using the papers' rules and the estimate tables, and
   record the choice as a decision.
3. Get and review the free documents on the resources "Wanted" list: the ASEE 2024 balance paper, the Morrison
   correlation, AGARD chapter 6, Maskell, and the HX711 datasheet.
4. Choose the fan, microcontroller/DAQ, pressure-sensor range and load-cell capacity from step 2's numbers, then buy.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer-2007/wind-tunnel (private; holds `cc51fff` and `5bc60f0`)
- Branch: `main`
