# Project Status

**Last updated:** 2026-11-01
**Last commit:** `748dae9` (2026-11-01, parts review and kit inventory), pushed to `origin/main`.
`sync_status.py --fetch` reported `UP_TO_DATE` at this session's second wrap.
The rest of this session's work (the owner's sketch, D-007 and D-008, fan candidates, controls; documentation only) is
**not committed yet**. Commands are in the
[session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#13-manual-git-commands-as-given-to-the-owner).
**Current stage:** Planning / pre-build. The basic layout is decided, and parts are being chosen.
- Decided: segmented 3D printing (D-005), an open-circuit blower with the fan at the front (D-007), and a
  100 mm × 100 mm test section (D-008). Estimated length 1.15–1.3 m including a 6-inch fan.
- Seven references reviewed: three tunnel-design papers, two blockage-correction papers, the ASEE 2024 balance paper
  and the HX711 datasheet. Nine more are filed in `resources/` but not yet read.
- Parts and tools on hand: the owner's ECE kit (from its packing list), an Elegoo Mega 2560 R3 board (identified by
  appearance, untested, USB cable on order), magnets, a multimeter, a soldering station and a bench power supply.
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
| On-tunnel display with a knob and menu, like the Ender 3's | Planned (owner, 2026-11-01): show drag force and other readings, set the fan speed ([TODO.md](TODO.md) P2) |
| Airfoil tests at set angles of attack | Planned (after validation). Owner, 2026-11-01: **preset angles** instead of the 2026-10-31 dial-and-servo idea, because a pivot would ruin the force measurement ([TODO.md](TODO.md) P3) |
| Flow visualization with a water-mist generator | Planned, optional, **last** (owner, 2026-10-31). Only a capped injection port and a test-section window are planned now ([TODO.md](TODO.md) P2) |

## 2. Wind tunnel configuration

**Nothing built. Tunnel type and test-section size are decided; the top airspeed and the fan are not.** Details and
unknowns are in [docs/experimental_setup.md](docs/experimental_setup.md). The owner's first sketch is in
[docs/sketches/](docs/sketches/README.md).

| Item | State | Source |
|---|---|---|
| Construction | 3D-printed segments on the owner's Bambu Lab P1S, with alignment holes; glue Tentative. Still segmented at 100 mm: the 250 mm settling chamber leaves no room for walls on the 256 mm bed | [D-005](DECISIONS.md) (Accepted) |
| Tunnel type | **Accepted (owner, 2026-11-01): open-circuit blower, fan at the front.** Proposed order: fan → flexible coupling → wide-angle diffuser with screens → settling chamber → contraction → test section → **open exit** (no exit diffuser; Tentative) | [D-007](DECISIONS.md) |
| Test section size | **Accepted (owner, 2026-11-01): 100 mm × 100 mm.** Proposed length 270–290 mm. Estimated total length 1.15–1.3 m with a 6-inch fan (owner's first target was about 1 m; more is allowed) | [D-008](DECISIONS.md), [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget) |
| Fan type | Proposed (agent, 2026-11-01): a 6-inch mixed-flow EC inline duct fan with a speed controller, on its own stand with a flexible coupling. Candidates in §3 | [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget) |
| Contraction | Proposed: contraction ratio 6.25 (250 mm → 100 mm square), 5th-order-polynomial wall, about 250 mm long (1.0 × inlet) | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md), [Mehta1979](resources/notes/Mehta1979.md) |
| Settling chamber | Proposed: 250 mm square, about 150–200 mm long. Honeycomb (cell length 6–8 diameters, about 150 cells across), then screens about 0.2 D apart, the last one with open area above 57 %. Add a capped port after the last screen for optional mist injection | [Mehta1979](resources/notes/Mehta1979.md) |
| Test section | Proposed: **closed** section with clear panels. Sphere at least about 0.5 D downstream of the contraction exit; sphere blockage about 3 % (at most 5 %); reference pressure reading at least 1.5√C upstream of the sphere; sphere at least 4√S from the test-section end. Together 2.7–2.9 h, i.e. 270–290 mm (estimate) | [Mehta1979](resources/notes/Mehta1979.md), [Cooper1998](resources/notes/Cooper1998.md), [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed) |
| Model access | **Owner's concept (2026-11-01):** one test chamber; the top and/or side acrylic panel comes off to swap the model, held by magnets (the owner's idea, preferred over a sliding panel). The agent's design points: pins or lips locate each panel; its inner face is flush with the wall; a foam gasket seals it; the floor (sting slot, balance) stays fixed; the pitot goes through a fixed wall; **no magnets near ferrous parts on the measured side of the balance**, and a non-magnetic sting | [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md) |
| Balance and controls layout | Proposed (2026-11-01): only the load cell and HX711 in a closed box under the floor (the sketch's "electronics house"). Display, knob and Arduino in a separate box on a cable. A sting lock, overload stops and a low-twist model attachment protect the load cell during swaps | [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#measurement-and-analysis-approach-proposed) |

## 3. Hardware and instrumentation

Parts on hand are recorded from the owner's statements and the ECE kit's packing list (2026-11-01). The full kit list
is in [docs/experimental_setup.md](docs/experimental_setup.md#parts-on-hand). Prices below were seen on retailer
listings on 2026-11-01 unless marked otherwise; they are guides, not quotes.

| Item | Availability | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | On hand (owner has access, stated 2026-10-30) | Build volume 256 × 256 × 256 mm (manufacturer spec). Filament unknown |
| ECE2010 lab kit (WPI) | On hand, per its packing list (owner, 2026-11-01). Quantities are the packed ones, not counted | Includes LM741, LM348 and LMC6484 op-amps, LM311, 555, LM317T and LM7805CT regulators, transistors, MOSFETs, potentiometers (1 × 10 kΩ, 2 × 1 kΩ, 1 × 100 kΩ, 1 × 1 MΩ), resistors, capacitors, breadboard and jumper wires. No multimeter, soldering iron or power supply in the list (the owner has them separately) |
| Tools | On hand (owner, 2026-11-01): multimeter, soldering station, bench power supply, access to a workbench | Models unknown. The bench supply's maximum voltage and current are unknown; they matter only if a 12 V DC fan is chosen |
| Other electronics | Unknown | The owner thinks more is on hand (2026-11-01); not listed yet |
| Microcontroller | **On hand: Elegoo Mega 2560 R3** (owner, 2026-11-01: "that is what it looks like at least"). Not yet powered or tested | 5 V logic; I²C on pins 20 (SDA) and 21 (SCL), also brought out next to AREF on R3 boards; ATmega16U2 USB-serial; USB Type-B socket (Mega 2560 Rev3 documentation via retailer pages, not checked on this board). Covers every planned sensor plus the display and knob |
| USB A-to-B cable for the board | To buy (owner ordering a UGREEN USB A-to-B 5 ft cable, 2026-11-01) | The board's original cable is lost. Verify with the Blink test (TODO P0) |
| Blower / fan | To buy; not chosen | Needed for the 100 mm section: rated about 400 CFM free air with a listed maximum static pressure of 300–500 Pa (about 320 CFM against 170–200 Pa at 15 m/s, estimate). Candidates (2026-11-01): **VIVOSUN AeroZesh S6** (mixed-flow EC, 405 CFM, 35 W, from about $63; static pressure not published); **AC Infinity Cloudline S6** (402 CFM, about 500 Pa listed, $90–120, about 320 mm long; about 13 m/s, estimate); **two Delta PFR1212UHE-SP00** 120 mm 12 V server fans (228.6 CFM and 300 Pa each, 2.7 A at 12 V, PWM input and speed output, 65.5 dBA each; about $30 each from the price of a sibling model; about 12 m/s for the pair, estimate). The agent's pick: a 6-inch mixed-flow EC fan. Unsuitable: VIVOSUN 6-inch "booster" fans ($32–39, axial, no pressure listed) and the 120 mm Qirssyn fan from Aki's video (about 95 CFM). Estimates in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#tunnel-length-budget) |
| Ducting | To buy (may be printed, D-005) | |
| Honeycomb + screens | To buy | |
| Pitot tube | To buy | Pitot-static (two ports: total and static). A drone probe alone is about $5–20. The owner found an FPVDrone PX4 airspeed kit ($49.99): its probe is suitable, its sensor is not (next row). Placement during force runs is open (question 10) |
| Differential pressure sensor | To buy | Model and range not chosen. Candidates: Sensirion SDP810-125Pa or -500Pa (I²C, 3–5.5 V supply per distributor listings, so it suits the 5 V Mega; about $25–45), SDP31/SDP32 (3.3 V, surface-mount; the SparkFun SDP31 breakout is retired) and Honeywell TruStability HSC ±1 inH₂O. **Unsuitable:** drone airspeed modules built on the TE MS4525DO (±1 psi, about 29× our largest q). Datasheets not yet obtained |
| Load cell + HX711 | To buy | Capacity unknown. Expected sphere drag in the 100 mm section: about 0.9 gf at 10 m/s and 2.0 gf at 15 m/s (estimate). Buy a load cell that has a datasheet (rated output, creep, safe overload), and plan overload protection for model swaps (§2). Prices from Weakly2024 (2024): TAL220 $9.50, SparkFun HX711 $10.95. HX711 datasheet reviewed ([notes](resources/notes/HX711.md)) |
| Ambient pressure / temperature sensor | Not chosen | Needed for air density. Candidate: Bosch BME280 on a 5 V-compatible breakout. A BMP280 (no humidity) would also serve for density |
| Display and knob | To buy (proposed) | For the menu (owner, 2026-11-01). Proposed: a 20×4 character LCD with an I²C adapter plus a push-button rotary encoder (KY-040 module or EC11). Typical prices, not checked: LCD $8–12, encoder $1–3. Upgrade option: a 128×64 graphic LCD like the Ender 3's ($10–20) for live graphs |
| Servo (airfoil pitch) | Probably not needed | The owner switched to preset angles of attack (2026-11-01). The 2026-10-31 dial-and-servo idea is kept in [TODO.md](TODO.md) P3 for reference |
| Magnets | On hand (owner, 2026-11-01) | Type, size and strength unknown. Planned for the removable panels (§2) |
| Acrylic sheet | To buy (proposed) | For the window panels: 3–5 mm thick, cast acrylic (agent's proposal) |
| Mist or smoke generator (optional visualization) | Not decided; deferred to the end | The owner asked (2026-11-01) for one that makes thick smoke. Options compared in [TODO.md](TODO.md) P2; the agent's first choice is an ultrasonic mist maker |

Budget: no fixed budget (owner, 2026-11-01). Rough total for the electronics plus a 6-inch fan: about $120–200,
depending mostly on the fan (agent's sum of the prices above). The load cell and HX711 are about $20 of it.
Filament, screens, honeycomb and acrylic are extra.

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | Planned; not started |
| Analysis scripts (`analysis/`) | Planned; not started |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote). States seen live so far, each correct for the situation: `NO_COMMITS_YET`, `UP_TO_DATE`, `FETCH_FAILED`, `AHEAD` (the last two on 2026-10-31, in the owner's terminal) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and clean runs on this repo |
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30, 2026-10-31, 2026-11-01); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `b710093`, `7db221f`, `9b42a07` and `748dae9`; `UP_TO_DATE` afterwards). One content error in its first run was corrected by the second ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
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
  - Committed and pushed as `748dae9`. After that wrap, the same session:
    - filed the owner's first sketch in `docs/sketches/`;
    - recorded the owner's decisions: a blower with the fan at the front (D-007) and a 100 mm test section (D-008);
    - estimated the tunnel length by section, sting length and fan candidates;
    - recorded the owner's single test chamber with removable panels, the Ender 3–style knob menu, preset airfoil
      angles, and the tools on hand.
  - See [the session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md).

## 7. Data and analyses

No data collected. No analyses completed. See [docs/data_catalog.md](docs/data_catalog.md).

## 8. Results

| Result | Status | Source |
|---|---|---|
| None yet | n/a | n/a |

Estimates are spread across these files; all are **calculations from assumed values, not results**:
- [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#order-of-magnitude-estimates): sphere drag, printable contraction
  sizes, fan requirements, and the [tunnel length budget](PROJECT_BACKGROUND.md#tunnel-length-budget) with fan
  top-speed estimates.
- [resources/notes/HX711.md](resources/notes/HX711.md): the HX711 noise floor for example load cells.
- [resources/notes/Cooper1998.md](resources/notes/Cooper1998.md#what-it-suggests-for-this-project-proposed):
  blockage-correction sizes and test-section positions.
- [2026-11-01 session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#6-measurements-and-results):
  airspeed from candidate fans, drone-sensor range against our pressures, and the force on removable panels.

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on choosing and buying hardware (fan, pressure sensor, load cell).
  - The fan choice and the pressure-sensor range wait on the owner's target top speed (open question 3) and the
    owner's choice among the fan candidates (§3).
  - The microcontroller is on hand but untested until the USB cable arrives.
- The owner's sketch PDF is 10.2 MiB, over the roughly 2 MB guideline for photos and scans
  ([data/README.md](data/README.md)). Compress it before committing, or commit as is (under D-004's 25 MB limit):
  the owner's call.
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
     the display and knob headers (the servo and angle dial are no longer needed with preset angles). See TODO P2.
   - If an analog sensor is ever used, the kit's LMC6484 suits a single 5 V supply better than the LM741, which
     needs split supplies (TI calls the LMC6484 rail-to-rail; its datasheet is not yet in `resources/`).
3. **Top airspeed and sphere diameter.** The test section is 100 mm (D-008), and the length target is about 1 m,
   with more allowed. Still open:
   - the owner's target top speed. 10–13 m/s is enough for the sphere validation, and a 6-inch fan should reach about
     13 m/s (estimate);
   - the sphere diameters: proposed about 20 mm (3.1 % blockage) and 25 mm (4.9 %) for the two-size check.
4. **Pressure-sensor range.** Dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate).
   - Candidates: ±125 Pa (SDP810-125Pa, SDP32), ±249 Pa (Honeywell HSC ±1 inH₂O) and ±500 Pa (SDP810-500Pa, SDP31).
   - Drone airspeed sensors (MS4525DO, ±1 psi) are ruled out: at 10 m/s, q is 0.44 % of their span (our arithmetic).
   - Choose after the top speed.
5. **Load-cell capacity.** Expected sphere drag is only about 1–2 grams-force at 10–15 m/s in the 100 mm section
   (estimate).
   - Overload protection for model swaps is needed: small bar cells are typically rated for only about 120 % of
     capacity (§2).
   - The load cell also carries the sphere's support (sting/mount), whose drag must be measured and subtracted.
   - A smaller cell lowers the HX711 noise in grams but has less overload margin
     ([HX711 notes](resources/notes/HX711.md)). Not chosen.
6. **Which published Cd value applies at the test Reynolds number?** Achenbach (1972) covers only Re ≥ 5×10⁴, while
   the planned Re is roughly 10⁴–10⁵. Morrison2013 (correlation) and Roos1971 (measurements) are in `resources/`,
   not yet reviewed (next agent task).
7. **Exit diffuser: answered Tentatively (none).** The blower is decided (D-007). An exit diffuser would roughly halve
   the fan power (estimate) but add about 0.75 m, against the owner's 1 m target, so the proposal is an open exit.
   The owner has not confirmed it.
8. **Blockage correction for the sphere.** Proposed (2026-10-31): Maskell with θ = 2.5, plus a separate solid-blockage
   term ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed)). Still open:
   - the solid-blockage formula (confirm in Barlow1999 ch. 9–10);
   - whether Maskell's flat-plate theory holds for a sphere (Maskell §2.6 flags rounded bodies). Proposed check:
     two sphere sizes;
   - θ for a sphere (1.85–2.8 across the cases in the sources);
   - Anthoine2004 (cylinders) not reviewed.
9. **What else is on hand? Mostly answered.** The ECE kit, a multimeter, a soldering station, a bench power supply
   and a workbench are recorded (2026-11-01). Still unknown:
   - other electronics the owner thinks they have;
   - the bench supply's maximum voltage and current (needed only for a 12 V DC fan);
   - the magnets' type and size.
10. **Where is the airspeed reference measured during force runs?** A pitot directly ahead of the sphere would put its
    wake on it. Options:
    - a probe off the centreline;
    - wall static taps calibrated against a pitot at the model position in the empty tunnel.

    Either way, at least 1.5√C upstream of the sphere ([Cooper1998](resources/notes/Cooper1998.md)). Check Barlow1999
    ch. 6 (test-section calibration).
11. **Fan speed control from the menu knob.** The 6-inch duct fans plug into the wall and come with their own
    controller. The owner's menu can set the fan speed only if the fan has a documented low-voltage control input
    (PWM or 0–10 V), or with the Delta 12 V PWM fans on the bench supply. Proposed: the fan's own controller for the
    first build; the Arduino never switches mains.
12. **Model attachment and sting lock.** How the sphere fixes to the sting without twisting the load cell (push fit
    and set screw, or similar), and the form of the sting lock and overload stops. Decide in build step 1.

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
   - decide whether to compress the sketch PDF, then commit and push this session's changes (commands in the
     [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#13-manual-git-commands-as-given-to-the-owner));
   - give the target top speed (open question 3);
   - choose the fan from the candidates (§3). Before buying the AeroZesh S6, find its static pressure in its manual
     or from VIVOSUN. For the Delta pair, give the bench supply's maximum voltage and current;
   - when the USB cable arrives, confirm the board markings and run the Blink test;
   - list any other electronics and the magnets' type and size (open question 9);
   - confirm or change D-003, D-004, D-006 and D-007's open exit.
2. **Agent, can start now:** review Morrison2013 and Roos1971 for the Re-matched C_D reference (open question 6).
   Then Mehta1977 (wide-angle diffuser) and Scheiman1981 (screens and honeycomb), which the 250 mm settling chamber
   and the fan-to-chamber diffuser need.
3. **Agent, with sizing:** read Barlow1999 ch. 9–10 (solid blockage) and ch. 6 (reference-pressure placement and
   test-section calibration).
4. **Build step 1:** detail the 100 mm tunnel: section dimensions, the removable panels, the balance box, the sting
   lock and overload stops, from the papers' rules and the [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget).
5. **Owner:** download the electronics datasheets ("Wanted" items 1–4 in [resources/README.md](resources/README.md),
   now including the SDP8xx and LMC6484), and the chosen fan's datasheet or fan curve.
6. Choose the pressure sensor and load cell from step 4's numbers, then buy.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer-2007/wind-tunnel (private; holds `cc51fff`, `5bc60f0`, `b710093`,
  `7db221f`, `9b42a07` and `748dae9`)
- Branch: `main`
