# Project Status

**Last updated:** 2026-10-31
**Last commit:** `b710093` (2026-10-31, the second `/wrap`'s doc update), pushed to `origin/main`;
`sync_status.py --fetch` reported `UP_TO_DATE` at this session's wrap. This session's work (reference library and
electronics references) is **not committed yet**: commands in the
[session log](docs/sessions/2026-10-31-reference-library-and-electronics.md#13-manual-git-commands-as-given-to-the-owner).
**Current stage:** Planning / pre-build. Design research under way: five references reviewed (three tunnel-design
papers, the ASEE 2024 balance paper and the HX711 datasheet) and eleven more filed in `resources/` but not yet read.
Construction method chosen (segmented 3D printing). No hardware built, no data collected, no analysis code written.

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

The only record of parts on hand is the original README's list from the owner's ECE kit (the two op-amp rows and the
regulator). **The rest of the kit is not recorded** (open question 9).

| Item | Availability | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | On hand (owner has access, stated 2026-10-30) | Build volume 256 × 256 × 256 mm (manufacturer spec). Filament unknown |
| LM741 / LM348 op-amps | On hand (per README) | Intended for signal conditioning; exact role not defined (open question 2). Datasheets not yet obtained (resources "Wanted" item 3) |
| LM317 regulator | On hand (per README) | Intended for a clean sensor supply |
| Rest of the ECE kit (passives, breadboard, meters, power supply, any microcontroller) | Unknown | Not recorded anywhere; owner to list (TODO P0) |
| Blower / fan | To buy | Model unknown. Required flow and pressure estimated in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#fan-requirement-estimates) (assumptions, not specs) |
| Ducting | To buy (may be printed, D-005) | |
| Honeycomb + screens | To buy | |
| Pitot tube | To buy | Type (pitot vs pitot-static) not specified |
| Differential pressure sensor | To buy | Model and range unknown. Candidates (Sensirion SDP3x, Honeywell TruStability HSC) listed under "Wanted" in [resources/README.md](resources/README.md); datasheets not yet obtained |
| Load cell + HX711 | To buy | Capacity unknown. HX711 datasheet obtained and reviewed ([notes](resources/notes/HX711.md)); load-cell candidates (TAL220, TAL221) under "Wanted" |
| Ambient pressure / temperature sensor | Not chosen | Needed for air density. Candidate: Bosch BME280 ("Wanted" item 4) |
| Servo (airfoil pitch) | To buy | |
| Microcontroller / DAQ | **Not identified** | Baseline from [Weakly2024](resources/notes/Weakly2024.md): one Arduino Uno read two HX711s over USB serial. Whether a board is already on hand is unknown |
| Ultrasonic mist maker (optional visualization) | Not decided | Product in the video the owner found is unidentified |

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | Planned; not started |
| Analysis scripts (`analysis/`) | Planned; not started |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote). States seen live so far, each correct for the situation: `NO_COMMITS_YET`, `UP_TO_DATE`, `FETCH_FAILED`, `AHEAD` (the last two on 2026-10-31, in the owner's terminal) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and clean runs on this repo |
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30, 2026-10-31); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `b710093`; `UP_TO_DATE` afterwards). One content error in its first run was corrected by the second ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only (developed with Python 3.13 on Windows 11). Git 2.54, Git LFS 3.7
(installed, not enabled), GitHub CLI 2.97. Agents reading PDFs used `pdftotext` (Git for Windows) and PyMuPDF, which is
installed on the owner's PC; neither is a project dependency.

## 5. Current experiments

None. No experiment has been run.

## 6. Work completed

- 2026-10-25: project plan written (original README: goal, hardware list, build order).
- 2026-10-29: repository, documentation system and agent workflow set up. See [the session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md).
- 2026-10-30/31: literature review and design inputs. Created `resources/` and reviewed three papers
  (Abdelhamed2014, Bell1988, Mehta1979). Recorded D-005 (segmented printing), estimates of printable sizes and fan
  requirements, a list of further documents, and the optional mist-visualization idea. Committed and pushed as
  `5bc60f0` and `b710093`. See [the session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md).
- 2026-10-31: reference library and electronics references. The owner downloaded the whole "Wanted" list (plus the
  full AGARD-AG-336 volume). The agent filed 13 documents (14 files) under the naming rule, kept two files over 25 MB local only
  (D-006, Tentative), and reviewed the HX711 datasheet and the ASEE 2024 balance paper (Weakly2024). It also wrote a
  new "Wanted" list for the electronics. See [the session log](docs/sessions/2026-10-31-reference-library-and-electronics.md).

## 7. Data and analyses

No data collected. No analyses completed. See [docs/data_catalog.md](docs/data_catalog.md).

## 8. Results

| Result | Status | Source |
|---|---|---|
| None yet | n/a | n/a |

Design estimates are in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#order-of-magnitude-estimates): sphere drag,
printable contraction sizes and fan requirements. The HX711 noise floor for example load cells is estimated in
[resources/notes/HX711.md](resources/notes/HX711.md). These are **calculations from assumed values, not results**.

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on choosing and buying hardware (fan, sensors, load cell, microcontroller).
  Sizing waits on owner inputs (open question 3). Parts choices also wait on knowing what is already in the ECE kit
  (open question 9).
- No known software bugs.
- Network (resolved 2026-10-31): the PC lost its IPv4 address, which blocked GitHub and some other sites. If
  `FETCH_FAILED` with "Could not resolve host" comes back, see Lessons learned in
  [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#lessons-learned).
- Risk: the project folder is inside OneDrive. OneDrive syncing a `.git` folder can cause conflicts if the repo is
  edited from two machines. GitHub, not OneDrive, is the source of truth between machines.
- Local-only references: Barlow1999 and Ewald1998 (full AGARD-AG-336) are ignored by Git (D-006). A fresh clone from
  GitHub on a machine without OneDrive will not have them.
- Copyright: several PDFs are publisher-copyrighted (Mehta1979 under Cambridge Core terms; Roos1971 AIAA;
  Mehta1977 and Bradshaw1964 journal reprints; Morel1975 ASME), and the Abdelhamed2014 licence is not checked. Fine
  while the repo is private (D-003); review before making it public. Barlow1999 is a commercial textbook and stays out
  of Git. AGARD-AG-336 states there are no restrictions on its distribution.

## 10. Open engineering questions

1. Which microcontroller or DAQ reads the HX711 and the pressure sensor? (Not in the original plan.) Baseline from
   [Weakly2024](resources/notes/Weakly2024.md): an Arduino Uno with one HX711 per load cell, logging over USB serial.
   Still to check: the pressure sensor's interface and voltage on the same board.
2. What is the op-amp signal conditioning for? The HX711 already amplifies and digitizes the load-cell bridge, so the
   op-amps may be meant for the pressure sensor; a digital (I²C) pressure sensor would need none. LM741 needs roughly
   ±(5–15) V supplies and is not rail-to-rail, so whether a split supply is on hand matters. Unresolved.
3. **Test-section size, top airspeed and sphere diameter.** These set Re, blockage, force and fan size. Not chosen.
   Owner inputs needed: available floor or bench length, target top speed, any fan already in mind.
4. Pressure-sensor range: dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate). Candidates span ±125,
   ±249 and ±500 Pa (resources "Wanted" item 1); the choice follows the top speed. Not chosen.
5. Load-cell capacity: expected sphere drag is only a few grams-force (estimate). The load cell also carries the
   sphere's support (sting/mount), whose drag must be measured and subtracted. A smaller cell lowers the HX711 noise
   in grams but has less overload margin ([HX711 notes](resources/notes/HX711.md)). Not chosen.
6. Which published Cd value applies at the test Reynolds number? Achenbach (1972) covers only Re ≥ 5×10⁴, while the
   planned Re is roughly 10⁴–10⁵. Morrison2013 (correlation) and Roos1971 (measurements) are now in `resources/`,
   not yet reviewed.
7. Blower vs suction tunnel, and whether to fit an exit diffuser. The diffuser roughly halves fan power (estimate)
   but adds length and printing.
8. Blockage correction method for the sphere. Maskell1963, Cooper1998 (AGARD-AG-336 chapter 6) and Anthoine2004 are
   now in `resources/`, not yet reviewed. Maskell's summary gives Δq/q = ε·C_D·S/C with ε a little above 5/2 for
   axisymmetric bodies.
9. **What else is in the ECE kit?** Only the op-amps and the LM317 are recorded. A microcontroller, a bench (split)
   supply or a multimeter on hand would change the parts choices.

## 11. Important measurements and findings

None measured yet. Literature findings that shape the design are summarized in the notes under `resources/notes/`.
One worth noting: the ASEE 2024 balance matched C_D = 0.47 within 6 % without blockage or mount-drag corrections; by
Maskell's formula its 3.4 % blockage alone would raise C_D about 4 %, so its agreement may hide offsetting errors
([Weakly2024 notes](resources/notes/Weakly2024.md); our arithmetic).

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:** commit and push this session's changes (commands in the
   [session log](docs/sessions/2026-10-31-reference-library-and-electronics.md#13-manual-git-commands-as-given-to-the-owner)).
   Then provide the sizing inputs (open question 3), list the rest of the ECE kit (open question 9), and confirm or
   change D-003, D-004 and D-006.
2. **Agent, can start now:** review Maskell1963, Cooper1998, Morrison2013 and Roos1971 to choose the blockage
   correction and the Re-matched C_D reference. Both feed into build step 1.
3. **Build step 1:** size the contraction and test section using the papers' rules and the estimate tables, and
   record the choice as a decision.
4. **Owner:** download the electronics datasheets ("Wanted" items 1–4: pressure-sensor and load-cell candidates, TI
   LM741/LM348/LM317, BME280).
5. Choose the fan, microcontroller/DAQ, pressure-sensor range and load-cell capacity from step 3's numbers, then buy.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer-2007/wind-tunnel (private; holds `cc51fff`, `5bc60f0` and `b710093`)
- Branch: `main`
