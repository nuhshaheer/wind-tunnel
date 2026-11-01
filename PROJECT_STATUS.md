# Project Status

**Last updated:** 2026-11-01
**Last commit:** `9b42a07` (2026-11-01, blockage-correction review and tunnel concepts), pushed to `origin/main`.
`sync_status.py --fetch` reported `UP_TO_DATE` at this session's wrap.
This session's work (parts review and kit inventory, documentation only) is **not committed yet**. Commands are in the
[session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#13-manual-git-commands-as-given-to-the-owner).
**Current stage:** Planning / pre-build. Design research is under way, and candidate parts are being reviewed.
- Seven references reviewed: three tunnel-design papers, two blockage-correction papers, the ASEE 2024 balance paper
  and the HX711 datasheet. Nine more are filed in `resources/` but not yet read.
- Construction method chosen (segmented 3D printing).
- Parts on hand recorded: the owner's ECE kit (from its packing list) and an Elegoo Mega 2560 R3 board. The board is
  identified only by appearance and is untested; its USB cable is being ordered.
- No hardware built, no data collected, no analysis code written.

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
| Sensor interface circuit, designed by the owner: circuit → breadboard test → PCB | Planned (owner, 2026-11-01; [TODO.md](TODO.md) P2) |
| Airfoil pitch mechanism (servo) | Planned (after validation). Owner's idea, 2026-10-31, not final: set the angle with a dial ([TODO.md](TODO.md) P3) |
| Flow visualization with a water-mist generator | Planned, optional, **last** (owner, 2026-10-31). Only a capped injection port and a test-section window are planned now ([TODO.md](TODO.md) P2) |

## 2. Wind tunnel configuration

**Nothing built. Test-section size, airspeed, fan and tunnel type are not chosen.** Details and unknowns are in
[docs/experimental_setup.md](docs/experimental_setup.md).

| Item | State | Source |
|---|---|---|
| Construction | 3D-printed segments on the owner's Bambu Lab P1S, with alignment holes; glue Tentative. The tunnel will be "decently big" (owner) | [D-005](DECISIONS.md) (Accepted) |
| Tunnel type | **Not chosen.** Current lean (agent, 2026-10-31; owner: "nothing final"): open-circuit **blower** with an open exit. Reason: its test section sits near room pressure, so print seams and the sting slot barely leak. In a suction tunnel they leak inward right next to the sphere unless sealed (for example, a sealed box around the balance). Suction remains reasonable if the best available fan is axial. Decide with the fan in build step 1 | [Mehta1979](resources/notes/Mehta1979.md), [session log](docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md) |
| Fan type | Proposed (agent, 2026-11-01): an inline mixed-flow duct fan with a speed controller, mounted on its own stand and joined to the tunnel by a flexible coupling. Size follows the top speed (§3) | [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md) |
| Contraction | Proposed, not decided: contraction ratio 6–9, square section, 5th-order-polynomial wall, length about 1.0 × inlet height | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md), [Mehta1979](resources/notes/Mehta1979.md) |
| Settling chamber | Proposed: honeycomb (cell length 6–8 diameters, about 150 cells across), then screens about 0.2 D apart, the last one with open area above 57 %. Add a capped port after the last screen for optional mist injection | [Mehta1979](resources/notes/Mehta1979.md) |
| Test section | Proposed: **closed** section with a clear window. Sphere at least about 0.5 D downstream of the contraction exit; sphere blockage about 3 % (at most 5 %); reference pressure reading at least 1.5√C upstream of the sphere; sphere at least 4√S from the test-section end. Together about 2.7–2.9 h long for h = 200 mm (estimate) | [Mehta1979](resources/notes/Mehta1979.md), [Cooper1998](resources/notes/Cooper1998.md), [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed) |
| Model access | Proposed (owner's idea, 2026-11-01, preferred over a sliding panel): removable clear acrylic panels held by magnets. The agent's design points: pins or lips locate each panel; its inner face is flush with the wall; a foam gasket seals it; the floor (sting slot, balance) stays fixed; the pitot goes through a fixed wall; **no magnets near ferrous parts on the measured side of the balance**, and a non-magnetic sting | [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md) |

## 3. Hardware and instrumentation

Parts on hand are recorded from the owner's statements and the ECE kit's packing list (2026-11-01). The full kit list
is in [docs/experimental_setup.md](docs/experimental_setup.md#parts-on-hand). Prices below were seen on retailer
listings on 2026-11-01 unless marked otherwise; they are guides, not quotes.

| Item | Availability | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | On hand (owner has access, stated 2026-10-30) | Build volume 256 × 256 × 256 mm (manufacturer spec). Filament unknown |
| ECE2010 lab kit (WPI) | On hand, per its packing list (owner, 2026-11-01). Quantities are the packed ones, not counted | Includes LM741, LM348 and LMC6484 op-amps, LM311, 555, LM317T and LM7805CT regulators, transistors, MOSFETs, potentiometers (one 10 kΩ, a candidate for the angle dial), resistors, capacitors, breadboard and jumper wires. No multimeter, soldering iron or power supply in the list |
| Other electronics | Unknown | The owner thinks more is on hand (2026-11-01). Whether a multimeter, soldering iron or bench supply is on hand: asked, not answered |
| Microcontroller | **On hand: Elegoo Mega 2560 R3** (owner, 2026-11-01: "that is what it looks like at least"). Not yet powered or tested | 5 V logic; I²C on pins 20 (SDA) and 21 (SCL), also brought out next to AREF on R3 boards; ATmega16U2 USB-serial; USB Type-B socket (Mega 2560 Rev3 documentation via retailer pages, not checked on this board). Covers every planned sensor plus the servo and the dial |
| USB A-to-B cable for the board | To buy (owner ordering a UGREEN USB A-to-B 5 ft cable, 2026-11-01) | The board's original cable is lost. Verify with the Blink test (TODO P0) |
| Blower / fan | To buy | Proposed type: inline mixed-flow duct fan with a speed controller and a published fan curve. A 6-inch fan (listed about 402 CFM free air and about 500 Pa maximum static pressure, $90–120) would give roughly 9–13 m/s in a 120–100 mm test section (estimate, assuming 70 % of free-air flow). A larger section or 20 m/s needs an 8-inch fan or larger. The 120 mm Qirssyn fan from Aki's video (about 95 CFM) is far too small. Requirement estimates are in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#fan-requirement-estimates) |
| Ducting | To buy (may be printed, D-005) | |
| Honeycomb + screens | To buy | |
| Pitot tube | To buy | Pitot-static (two ports: total and static). A drone probe alone is about $5–20. The owner found an FPVDrone PX4 airspeed kit ($49.99): its probe is suitable, its sensor is not (next row). Placement during force runs is open (question 10) |
| Differential pressure sensor | To buy | Model and range not chosen. Candidates: Sensirion SDP810-125Pa or -500Pa (I²C, 3–5.5 V supply per distributor listings, so it suits the 5 V Mega; about $25–45), SDP31/SDP32 (3.3 V, surface-mount; the SparkFun SDP31 breakout is retired) and Honeywell TruStability HSC ±1 inH₂O. **Unsuitable:** drone airspeed modules built on the TE MS4525DO (±1 psi, about 29× our largest q). Datasheets not yet obtained |
| Load cell + HX711 | To buy | Capacity unknown. Buy a load cell that has a datasheet (rated output, creep, safe overload). Prices from Weakly2024 (2024): TAL220 $9.50, SparkFun HX711 $10.95. HX711 datasheet reviewed ([notes](resources/notes/HX711.md)) |
| Ambient pressure / temperature sensor | Not chosen | Needed for air density. Candidate: Bosch BME280 on a 5 V-compatible breakout. A BMP280 (no humidity) would also serve for density |
| Servo (airfoil pitch) | To buy (after validation) | Owner's idea (2026-10-31, not final): a potentiometer dial → microcontroller → servo, with the angle logged in the data. Points to plan for are in [TODO.md](TODO.md) P3 |
| Magnets | On hand (owner, 2026-11-01) | Type, size and strength unknown. Planned for the removable panels (§2) |
| Acrylic sheet | To buy (proposed) | For the window panels: 3–5 mm thick, cast acrylic (agent's proposal) |
| Mist or smoke generator (optional visualization) | Not decided; deferred to the end | The owner asked (2026-11-01) for one that makes thick smoke. Options compared in [TODO.md](TODO.md) P2; the agent's first choice is an ultrasonic mist maker |

Rough budget for the electronics plus a 6-inch fan: about $200, most of it the fan (agent's sum of the prices above).
Filament, screens, honeycomb and acrylic are extra.

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | Planned; not started |
| Analysis scripts (`analysis/`) | Planned; not started |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote). States seen live so far, each correct for the situation: `NO_COMMITS_YET`, `UP_TO_DATE`, `FETCH_FAILED`, `AHEAD` (the last two on 2026-10-31, in the owner's terminal) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and clean runs on this repo |
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30, 2026-10-31, 2026-11-01); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `b710093`, `7db221f` and `9b42a07`; `UP_TO_DATE` afterwards). One content error in its first run was corrected by the second ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only (developed with Python 3.13 on Windows 11). Git 2.54, Git LFS 3.7
(installed, not enabled), GitHub CLI 2.97. Agents reading PDFs used `pdftotext` (Git for Windows) and PyMuPDF 1.28.2,
which is installed on the owner's PC; neither is a project dependency.

## 5. Current experiments

None. No experiment has been run.

## 6. Work completed

- 2026-10-25: project plan written (original README: goal, hardware list, build order).
- 2026-10-29: repository, documentation system and agent workflow set up. See [the session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md).
- 2026-10-30/31: literature review and design inputs.
  - Created `resources/` and reviewed three papers (Abdelhamed2014, Bell1988, Mehta1979).
  - Recorded D-005 (segmented printing), estimates of printable sizes and fan requirements, a list of further
    documents, and the optional mist-visualization idea.
  - Committed and pushed as `5bc60f0` and `b710093`. See [the session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md).
- 2026-10-31: reference library and electronics references.
  - The owner downloaded the whole "Wanted" list, plus the full AGARD-AG-336 volume.
  - The agent filed 13 documents (14 files) under the naming rule and kept two files over 25 MB local only (D-006,
    Tentative).
  - It reviewed the HX711 datasheet and the ASEE 2024 balance paper (Weakly2024) and wrote a new "Wanted" list for
    the electronics.
  - Pushed as `7db221f`. See [the session log](docs/sessions/2026-10-31-reference-library-and-electronics.md).
- 2026-10-31: blockage-correction review and tunnel concepts.
  - Reviewed Maskell1963 and Cooper1998 from page images and proposed a blockage-correction method
    ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed)).
  - Explained the electronics plan and the measurement chain to the owner.
  - Answered the owner's questions on mist streaklines and blower vs suction, and recorded the owner's
    angle-of-attack dial idea.
  - Committed and pushed as `9b42a07` on 2026-11-01. See [the session log](docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md).
- 2026-11-01: parts review and kit inventory.
  - Recorded the ECE kit from its packing list and the owner's Elegoo Mega 2560 R3.
  - Assessed two parts the owner found: an FPV pitot kit (sensor range unsuitable) and a 120 mm fan (too small).
  - Proposed a fan type, pressure-sensor candidates, what to look for in each part with typical prices, removable
    magnetic panels and the interface-board plan.
  - See [the session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md).

## 7. Data and analyses

No data collected. No analyses completed. See [docs/data_catalog.md](docs/data_catalog.md).

## 8. Results

| Result | Status | Source |
|---|---|---|
| None yet | n/a | n/a |

Estimates are spread across these files; all are **calculations from assumed values, not results**:
- [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#order-of-magnitude-estimates): sphere drag, printable contraction
  sizes and fan requirements.
- [resources/notes/HX711.md](resources/notes/HX711.md): the HX711 noise floor for example load cells.
- [resources/notes/Cooper1998.md](resources/notes/Cooper1998.md#what-it-suggests-for-this-project-proposed):
  blockage-correction sizes and test-section positions.
- [2026-11-01 session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#6-measurements-and-results):
  airspeed from candidate fans, drone-sensor range against our pressures, and the force on removable panels.

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on choosing and buying hardware (fan, pressure sensor, load cell).
  - The fan size and the pressure-sensor range both wait on the owner's top speed and available space (open
    question 3).
  - The microcontroller is on hand but untested until the USB cable arrives.
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

1. **Microcontroller: largely answered.** The owner's Elegoo Mega 2560 R3 (5 V logic) is the candidate. It still
   needs:
   - its identity confirmed from the board markings;
   - a Blink upload once the cable arrives;
   - a check that the chosen pressure sensor and BME280 board work at 5 V on its I²C pins (20/21).
2. **What is the op-amp signal conditioning for?** Proposed (agent, 2026-11-01): nothing in the measurement chain.
   - The HX711, a digital pressure sensor and the BME280 need no analog conditioning, and commercial digital sensors
     will be more accurate than an analog front end built here.
   - The owner's circuit design work goes into the interface board instead: connectors, I²C pull-ups, decoupling,
     servo power from the kit's LM7805, the angle dial. See TODO P2.
   - If an analog sensor is ever used, the kit's LMC6484 suits a single 5 V supply better than the LM741, which
     needs split supplies (TI calls the LMC6484 rail-to-rail; its datasheet is not yet in `resources/`).
3. **Test-section size, top airspeed and sphere diameter.** These set Re, blockage, force, fan size and the
   pressure-sensor range. Not chosen. Owner inputs needed: available floor or bench length, target top speed, any fan
   already in mind.
4. **Pressure-sensor range.** Dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate).
   - Candidates: ±125 Pa (SDP810-125Pa, SDP32), ±249 Pa (Honeywell HSC ±1 inH₂O) and ±500 Pa (SDP810-500Pa, SDP31).
   - Drone airspeed sensors (MS4525DO, ±1 psi) are ruled out: at 10 m/s, q is 0.44 % of their span (our arithmetic).
   - Choose after the top speed.
5. **Load-cell capacity.** Expected sphere drag is only a few grams-force (estimate).
   - The load cell also carries the sphere's support (sting/mount), whose drag must be measured and subtracted.
   - A smaller cell lowers the HX711 noise in grams but has less overload margin
     ([HX711 notes](resources/notes/HX711.md)). Not chosen.
6. **Which published Cd value applies at the test Reynolds number?** Achenbach (1972) covers only Re ≥ 5×10⁴, while
   the planned Re is roughly 10⁴–10⁵. Morrison2013 (correlation) and Roos1971 (measurements) are in `resources/`,
   not yet reviewed (next agent task).
7. **Blower vs suction tunnel, and whether to fit an exit diffuser.**
   - The diffuser roughly halves fan power (estimate) but adds length and printing.
   - Current lean: blower (§2), because of test-section leaks. Note that an exit diffuser puts the test section below
     room pressure, which weakens that argument.
   - Fan type proposed 2026-11-01: inline mixed-flow duct fan (§3). Decide the tunnel type with the fan.
8. **Blockage correction for the sphere.** Proposed (2026-10-31): Maskell with θ = 2.5, plus a separate solid-blockage
   term ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed)). Still open:
   - the solid-blockage formula (confirm in Barlow1999 ch. 9–10);
   - whether Maskell's flat-plate theory holds for a sphere (Maskell §2.6 flags rounded bodies). Proposed check:
     two sphere sizes;
   - θ for a sphere (1.85–2.8 across the cases in the sources);
   - Anthoine2004 (cylinders) not reviewed.
9. **What else is on hand?** The ECE kit is now recorded from its packing list. Still unknown:
   - other electronics the owner thinks they have;
   - whether a multimeter, soldering iron or bench (split) supply is on hand;
   - the magnets' type and size.
10. **Where is the airspeed reference measured during force runs?** A pitot directly ahead of the sphere would put its
    wake on it. Options:
    - a probe off the centreline;
    - wall static taps calibrated against a pitot at the model position in the empty tunnel.

    Either way, at least 1.5√C upstream of the sphere ([Cooper1998](resources/notes/Cooper1998.md)). Check Barlow1999
    ch. 6 (test-section calibration).

## 11. Important measurements and findings

None measured yet. Literature findings that shape the design are summarized in the notes under `resources/notes/`.
Worth noting:

- The ASEE 2024 balance matched C_D = 0.47 within 6 % without blockage or mount-drag corrections. By Maskell's
  formula its 3.4 % blockage alone would raise C_D about 4 %, so its agreement may hide offsetting errors
  ([Weakly2024 notes](resources/notes/Weakly2024.md); our arithmetic).
- At the planned 3–5 % blockage, the blockage correction is about 3.5–6 % of C_D. Its uncertainty comes mainly from
  the blockage factor θ (about ±0.65 % of C_D at 3 %), not from the choice between Maskell's and Hackett's methods
  (which agree within 0.1 %). Neither source has sphere data, so the correction should be checked with two sphere
  sizes ([Cooper1998 notes](resources/notes/Cooper1998.md); our arithmetic).

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:**
   - commit and push this session's changes (commands in the
     [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#13-manual-git-commands-as-given-to-the-owner));
   - provide the sizing inputs (open question 3). They now decide the fan size and the pressure-sensor range as well;
   - when the USB cable arrives, confirm the board markings and run the Blink test;
   - say whether a multimeter, soldering iron and bench supply are on hand, and list any other electronics
     (open question 9);
   - confirm or change D-003, D-004 and D-006.
2. **Agent, can start now:** review Morrison2013 and Roos1971 for the Re-matched C_D reference (open question 6).
3. **Agent, with sizing:** read Barlow1999 ch. 9–10 (solid blockage) and ch. 6 (reference-pressure placement and
   test-section calibration).
4. **Build step 1:** size the contraction and test section, including the removable panels, using the papers' rules
   and the estimate tables. Choose blower vs suction with the fan, and record the choice as a decision.
5. **Owner:** download the electronics datasheets ("Wanted" items 1–4 in [resources/README.md](resources/README.md),
   now including the SDP8xx and LMC6484).
6. Choose the fan, pressure sensor and load cell from step 4's numbers, then buy.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer-2007/wind-tunnel (private; holds `cc51fff`, `5bc60f0`, `b710093`,
  `7db221f` and `9b42a07`)
- Branch: `main`
