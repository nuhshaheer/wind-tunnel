# Project Status

**Last updated:** 2026-10-29
**Last commit:** none yet. The repository has been initialized locally and has no commits; the owner makes the first commit and push.
**Current stage:** Planning / pre-build. No hardware has been built, no data collected, no analysis code written.

This is the authoritative snapshot of the project. Status labels used below:
**Verified**, **Implemented, unverified**, **Preliminary result**, **In progress**, **Planned**,
**Blocked**, **Tentative**. Session-by-session history is in [docs/sessions/SESSION_LOG.md](docs/sessions/SESSION_LOG.md).

## 1. Objectives

Build a small wind tunnel with my own instrumentation, measure drag, and prove the tunnel reads true. The validation
is the drag coefficient of a sphere, compared against the published value of about 0.47. Source: the original
project README (2026-10-25). Long-term context is in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md).

| Objective | Status |
|---|---|
| Tunnel built with flow conditioning | Planned |
| Airspeed measured with pitot tube + differential pressure sensor | Planned |
| Drag force measured with load cell + HX711 | Planned |
| Load cell calibrated against known weights | Planned |
| Sphere Cd validation run (deliverable) | Planned |
| Airfoil pitch mechanism (servo) | Planned (after validation) |

## 2. Wind tunnel configuration

**Planned; nothing built.** No dimensions, fan, contraction ratio or test-section size have been chosen. Details and
unknowns are tracked in [docs/experimental_setup.md](docs/experimental_setup.md).

## 3. Hardware and instrumentation

| Item | Availability | Notes |
|---|---|---|
| LM741 / LM348 op-amps | On hand (per README) | Intended for signal conditioning; exact role not defined (see open questions) |
| LM317 regulator | On hand (per README) | Intended for a clean sensor supply |
| Blower / fan | To buy | Model, flow rate, pressure: unknown |
| Ducting | To buy | |
| Honeycomb + screens | To buy | |
| Pitot tube | To buy | Type (pitot vs pitot-static) not specified |
| Differential pressure sensor | To buy | Model and range unknown |
| Load cell + HX711 | To buy | Capacity unknown |
| Servo (airfoil pitch) | To buy | |
| Microcontroller / DAQ | **Not identified** | Not listed in the original plan; needed to read the HX711 and pressure sensor |

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | Planned; not started |
| Analysis scripts (`analysis/`) | Planned; not started |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and a clean run on this repo |
| `/catchup` | Verified 2026-10-29: a fresh agent with no conversation history ran it read-only and produced a correct handoff. Only the `NO_COMMITS_YET` sync state was exercised live; the other states are covered by the script's unit tests. |
| `/wrap` | Implemented, unverified. Run once on 2026-10-29 by the agent that wrote it (this setup session); not yet run by a fresh agent or on a repository with commits. |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only (developed with Python 3.13 on Windows 11). Git 2.54, Git LFS 3.7
(installed, not enabled), GitHub CLI 2.97.

## 5. Current experiments

None. No experiment has been run.

## 6. Work completed

- 2026-10-25: project plan written (original README: goal, hardware list, build order).
- 2026-10-29: repository, documentation system and agent workflow set up. See [the session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md).

## 7. Data and analyses

No data collected. No analyses completed. See [docs/data_catalog.md](docs/data_catalog.md).

## 8. Results

| Result | Status | Source |
|---|---|---|
| None yet | n/a | n/a |

Order-of-magnitude design estimates (sphere drag of a few grams-force at 10 m/s) are in
[PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#order-of-magnitude-estimates). They are **calculations from assumed values,
not results**.

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on choosing and buying hardware (fan, sensors, load cell, microcontroller).
- No known software bugs.
- Risk: the project folder is inside OneDrive. OneDrive syncing a `.git` folder can cause conflicts if the repo is
  edited from two machines. GitHub, not OneDrive, is the source of truth between machines.

## 10. Open engineering questions

1. Which microcontroller or DAQ reads the HX711 and the pressure sensor? (Not in the original plan.)
2. What is the op-amp signal conditioning for? The HX711 already amplifies and digitizes the load-cell bridge, so the
   op-amps may be meant for the pressure sensor. LM741 needs roughly ±(5–15) V supplies and is not rail-to-rail,
   which may not suit a single low-voltage supply. Unresolved.
3. Test-section size, target airspeed and sphere diameter: these set the Reynolds number, the blockage ratio and the
   force to be measured. Not chosen.
4. Pressure-sensor range: dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate). A sensor with a ±2 kPa
   range would use a small fraction of its span. Not chosen.
5. Load-cell capacity: expected sphere drag is only a few grams-force (estimate). The load cell also carries
   the sphere's support (sting/mount), whose drag must be measured and subtracted. Not chosen.
6. Which published Cd value applies at the test Reynolds number? "~0.47" needs a cited, Re-matched source.

## 11. Important measurements and findings

None measured yet.

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:** review and push the initial commit (commands in the 2026-10-29 session log).
2. **Build step 1:** size the contraction and test section. Choose a target airspeed, test-section cross-section
   and sphere diameter, and check Reynolds number, blockage and expected force.
3. Choose the microcontroller/DAQ, the pressure-sensor range and the load-cell capacity from step 2's numbers, then buy.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer-2007/wind-tunnel (private, empty until the first push)
- Branch: `main`
