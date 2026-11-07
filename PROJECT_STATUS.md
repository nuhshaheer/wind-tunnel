# Project Status

**Last updated:** 2026-11-07
**Last commit:** `36f39eb` (2026-11-03, the Mega 2560 board test), pushed to `origin/main`. `/catchup` reported
`UP_TO_DATE` on 2026-11-05, and so did this session's `/wrap` on 2026-11-07.
- The owner renamed the GitHub account to `nuhshaheer` on 2026-11-02, so the repo is now
  https://github.com/nuhshaheer/wind-tunnel, and the local `origin` points there. The old URL redirects.
- **Not committed yet:** the top-speed recommendation and fan search of 2026-11-05 (documentation only;
  [session log](docs/sessions/2026-11-07-top-speed-and-fan-search.md), with the commit commands in §13).
**Current stage:** Planning / pre-build. The basic layout is decided, and parts are being chosen.
- Decided:
  - segmented 3D printing (D-005);
  - an open-circuit blower with the fan at the front (D-007);
  - a 100 mm × 100 mm test section (D-008);
  - **the sphere-validation reference: Brown and Lawler (2003) Eq. (19) at each run's Re, ±10 %, plus a trend check
    (D-009).**

  Estimated length 1.15–1.3 m including a 6-inch fan.
- **Proposed (agent, 2026-11-05), not yet confirmed by the owner: a top speed of 13 m/s**, with validation runs from
  about 6.5 m/s. One 6-inch fan listing about 500 Pa maximum static pressure should just reach it, and a ±125 Pa
  pressure sensor covers it (estimates; open question 3).
- Thirteen references reviewed:
  - tunnel design: Abdelhamed2014, Bell1988, Mehta1979, **Mehta1977**;
  - flow conditioning: **Scheiman1981, Wieghardt1953**;
  - blockage: Maskell1963, Cooper1998;
  - sphere C_D: **Morrison2013, Roos1971, Brown2003**;
  - the balance paper Weakly2024 and the HX711 datasheet.

  Five more are filed in `resources/` but not yet read.
- Parts and tools on hand: the owner's ECE kit (from its packing list), an Elegoo Mega 2560 board (**working**: Blink
  upload Verified 2026-11-02, §3), magnets, a multimeter, a soldering station and a bench power supply.
- No hardware built, no data collected, no analysis code written.

This is the authoritative snapshot of the project. Status labels used below:
**Verified**, **Implemented, unverified**, **Preliminary result**, **In progress**, **Planned**,
**Blocked**, **Tentative**. Session-by-session history is in [docs/sessions/SESSION_LOG.md](docs/sessions/SESSION_LOG.md).

## 1. Objectives

Build a small wind tunnel with my own instrumentation, measure drag, and prove the tunnel reads true. The validation
is the drag coefficient of a sphere, compared against a published value. Source: the original project README
(2026-10-25), which named "about 0.47". Long-term context is in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md).

**Since 2026-11-02 the comparison is Reynolds-number matched ([D-009](DECISIONS.md)):** Brown and Lawler (2003) Eq. (19)
at each run's Re, about 0.42–0.445 for the planned runs. The band is about ±10 %, because the published data at this Re
scatter that much. Runs at several speeds must also show C_D rising with Re, about 12 % from 5 to 15 m/s
([Brown2003 notes](resources/notes/Brown2003.md)).

| Objective | Status |
|---|---|
| Tunnel built with flow conditioning | Planned (design research In progress) |
| Airspeed measured with pitot tube + differential pressure sensor | Planned |
| Drag force measured with load cell + HX711 | Planned |
| Load cell calibrated against known weights | Planned |
| Sphere Cd validation run (deliverable) | Planned. Reference and pass criterion: [D-009](DECISIONS.md) (Accepted 2026-11-02) |
| Sensor interface circuit, designed by the owner: circuit → breadboard test → PCB | Planned (owner, 2026-11-01; [TODO.md](TODO.md) P2) |
| On-tunnel display with a knob and menu, like the Ender 3's | Planned (owner, 2026-11-01): show drag force and other readings, set the fan speed ([TODO.md](TODO.md) P2) |
| Airfoil tests at set angles of attack | Planned (after validation). Owner, 2026-11-01: **preset angles** instead of the 2026-10-31 dial-and-servo idea, because a pivot would ruin the force measurement ([TODO.md](TODO.md) P3) |
| Flow visualization with a water-mist generator | Planned, optional, **last** (owner, 2026-10-31). Only a capped injection port and a test-section window are planned now ([TODO.md](TODO.md) P2) |
| Model-car downforce with a second, vertical load cell | Tentative: the owner's idea (2026-11-02, "just an idea"), after validation. The same vertical cell would measure airfoil lift ([TODO.md](TODO.md) P3) |

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
| Fan-to-chamber diffuser | Proposed (2026-11-02): area ratio 3.44 (152 mm round → 250 mm square), so the screens need K_sum ≥ 2.1. **Two screens (K ≈ 1.1–1.5 each) allow about 150–200 mm**; the minimum is about 115 mm with two screens, 195 mm with one and 335 mm with none. Below about 220 mm use curved walls or radiused inlet and outlet corners. Fillet the corners. **No flow straightener at the fan outlet**: the fan's swirl helps keep the diffuser attached | [Mehta1977](resources/notes/Mehta1977.md) (Figs. 5 and 7, §6.1; owner-checked) |
| Contraction | Proposed: contraction ratio 6.25 (250 mm → 100 mm square), 5th-order-polynomial wall, about 250 mm long (1.0 × inlet) | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md), [Mehta1979](resources/notes/Mehta1979.md) |
| Settling chamber | Proposed: 250 mm square. A honeycomb (cell length 7–10 diameters, cells of about 2–3 mm, thin walls), then one or two screens at least 58 % open, then about 50 mm (0.2 D) to the contraction. Add a capped port after the last screen for optional mist injection. **Length 150–200 mm** with Mehta1979's 0.2 D spacing; **about 230–300 mm** if spaced for full turbulence decay: at least 500 wire diameters between screens (about 75–125 mm) and about 50 cell diameters from the honeycomb to the first screen (2026-11-02). Decide at sizing | [Mehta1979](resources/notes/Mehta1979.md), [Mehta1977](resources/notes/Mehta1977.md), [Scheiman1981](resources/notes/Scheiman1981.md) |
| Test section | Proposed: **closed** section with clear panels. Sphere at least about 0.5 D downstream of the contraction exit; sphere blockage about 3 % (at most 5 %); reference pressure reading at least 1.5√C upstream of the sphere; sphere at least 4√S from the test-section end. Together 2.7–2.9 h, i.e. 270–290 mm (estimate) | [Mehta1979](resources/notes/Mehta1979.md), [Cooper1998](resources/notes/Cooper1998.md), [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed) |
| Model access | **Owner's concept (2026-11-01):** one test chamber; the top and/or side acrylic panel comes off to swap the model, held by magnets (the owner's idea, preferred over a sliding panel). The agent's design points: pins or lips locate each panel; its inner face is flush with the wall; a foam gasket seals it; the floor (sting slot, balance) stays fixed; the pitot goes through a fixed wall; **no magnets near ferrous parts on the measured side of the balance**, and a non-magnetic sting | [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md) |
| Balance and controls layout | Proposed (2026-11-01): only the load cell and HX711 in a closed box under the floor (the sketch's "electronics house"). Display, knob and Arduino in a separate box on a cable. A sting lock, overload stops and a low-twist model attachment protect the load cell during swaps. Optional (2026-11-02): leave room for a second, vertical load cell for airfoil lift or model-car downforce (P3) | [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#measurement-and-analysis-approach-proposed) |

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
| Microcontroller | **On hand, working: Elegoo Mega 2560.** Blink upload **Verified** 2026-11-02 (owner's test) | Evidence, 2026-11-02:<br>• The owner read ATMEGA2560 on the main chip. Whether the board itself is marked "R3" is not yet recorded.<br>• Windows listed it on COM3 with USB ID 2341:0042, which the Arduino AVR core (1.8.8, `boards.txt`) lists under "Arduino Mega or Mega 2560". USB serial number `13448474939351C0E828` identifies this board.<br>• The owner uploaded Blink with both delays changed from 1000 to 200 ms (Arduino IDE 2.3.10, board "Arduino Mega or Mega 2560", processor ATmega2560), and the "L" LED blinked faster. A faster blink proves the upload, because a blinking LED alone could be a factory-loaded sketch.<br>From the Mega 2560 Rev3 documentation (retailer pages; not checked on this board): 5 V logic; I²C on pins 20 (SDA) and 21 (SCL), also brought out next to AREF on R3 boards; ATmega16U2 USB-serial. Covers every planned sensor plus the display and knob |
| USB A-to-B cable for the board | On hand, carries data: the board enumerated on COM3 through it (2026-11-02) | The board's original cable was lost. The owner was ordering a UGREEN 5 ft cable (2026-11-01); which cable was used on 2026-11-02 is not recorded |
| Blower / fan | To buy; not chosen. The owner is looking for something cheaper than the Cloudline S6 (2026-11-05) | **Requirement (corrected 2026-11-05):** for the proposed 13 m/s, about 275 CFM against 127–152 Pa (estimate). On a straight-line fan curve that needs about 400 CFM free air **and** a listed maximum static pressure of about 410–490 Pa or more; more free-air flow allows less pressure (500 CFM: about 280–340 Pa). Better still, a published fan curve showing at least 275 CFM at 150 Pa (0.6 inH₂O). The earlier "300–500 Pa" was wrong at its low end: 400 CFM and 300 Pa give only about 11.5–12 m/s.<br>Candidates (prices and specs from web-search results, 2026-11-05; pages not opened):<br>• **AC Infinity Cloudline S6**: 402 CFM, 503 Pa listed, EC motor; $99 on AC Infinity's site, $119–175 elsewhere; about 320 mm long; about 13.1–13.7 m/s (estimate). The only candidate whose listed figures meet 13 m/s.<br>• **VIVOSUN AeroZesh S6**: mixed-flow EC with PWM control, 405 CFM, 35 W, 3100 rpm, 45 dBA, from about $63. **Static pressure still not published** (searched 2026-11-05). Best value if VIVOSUN gives about 450 Pa or more.<br>• **Two Delta PFR1212UHE-SP00** 120 mm 12 V server fans (228.6 CFM and 300 Pa each, 2.7 A at 12 V, PWM input and speed output, 65.5 dBA each; about $30 each from the price of a sibling model; about 12 m/s for the pair, estimate).<br>Unsuitable or impossible to size:<br>• the **VEVOR 6-inch 400 CFM AC fan** the owner found (2026-11-05): 60 W, 2600 rpm, $84.49 on eBay, no pressure on its listing. A Lowe's listing that probably matches gives 300 Pa, so about 11–12 m/s at best. Its "34 dB" is unlikely at 400 CFM;<br>• **Skyshalo 6-inch** ($53.89, AC; the same listing wording as the VEVOR, so probably the same fan, our inference);<br>• **HFS 6-inch** ($62.49, 120 W, 65 dB, no pressure listed);<br>• VIVOSUN 6-inch "booster" fans ($32–39, axial, no pressure listed);<br>• the 120 mm Qirssyn fan from Aki's video (about 95 CFM).<br>Estimates in [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#top-speed-trade-off-proposed) |
| Ducting | To buy (may be printed, D-005) | |
| Honeycomb + screens | To buy; not chosen | Proposed (2026-11-02):<br>• Screens: metal square-mesh, at least 58 % open, for example 20–30 wires/in with 0.19–0.23 mm wire (the sizes Scheiman tested). At the settling chamber's roughly 2 m/s, K is about 1.1–1.8, about twice the high-speed value (Wieghardt's formula, extrapolated), and the wires shed no eddies (u₁d/βν below 85).<br>• Honeycomb: thin-walled (paper, aluminium or drinking straws), cell length 7–10 diameters. A 3D-printed honeycomb has thick walls (about 25 % blocked at 0.4 mm walls on 3 mm cells; our arithmetic).<br>Sources: [Scheiman1981](resources/notes/Scheiman1981.md), [Wieghardt1953](resources/notes/Wieghardt1953.md), [Mehta1977](resources/notes/Mehta1977.md) |
| Pitot tube | To buy | Pitot-static (two ports: total and static). A drone probe alone is about $5–20. The owner found an FPVDrone PX4 airspeed kit ($49.99): its probe is suitable, its sensor is not (next row). Placement during force runs is open (question 10) |
| Differential pressure sensor | To buy | Model and range not chosen. Candidates: Sensirion SDP810-125Pa or -500Pa (I²C, 3–5.5 V supply per distributor listings, so it suits the 5 V Mega; about $25–45), SDP31/SDP32 (3.3 V, surface-mount; the SparkFun SDP31 breakout is retired) and Honeywell TruStability HSC ±1 inH₂O. **Unsuitable:** drone airspeed modules built on the TE MS4525DO (±1 psi, about 29× our largest q). Datasheets not yet obtained. **If the 13 m/s top speed is confirmed:** the SDP810-125Pa (full scale at 14.4 m/s; q = 101 Pa at 13 m/s; agent, 2026-11-05) |
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
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-05); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `b710093`, `7db221f`, `9b42a07`, `748dae9`, `8fda08f`, `c04de1b`, `b22a45b` and `36f39eb`; `UP_TO_DATE` afterwards). One content error in its first run was corrected by the second ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only, developed with Python 3.13 on Windows 11.
- On 2026-11-02, `python` on the owner's PC was **3.11.0** in both Git Bash and PowerShell. The `py` launcher listed
  3.10, 3.11, 3.12 and 3.14, but no 3.13. The 20 tests pass under 3.11.
- Git 2.54, Git LFS 3.7 (installed, not enabled), GitHub CLI 2.97.
- Arduino IDE 2.3.10 with the Arduino AVR Boards core 1.8.8, installed by the owner on 2026-11-02 (versions read from
  the program file and the core's folder). `arduino-cli` is not installed.
- Agents reading PDFs used `pdftotext` (Git for Windows) and PyMuPDF 1.28.2, which is installed on the owner's PC
  (Python 3.11). Neither is a project dependency.

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
  - Part 2 committed and pushed as `8fda08f`. See [the session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md).
- 2026-11-02: sphere C_D reference and flow-conditioning review.
  - Reviewed Morrison2013, Roos1971, Mehta1977 and Scheiman1981, then two papers the owner added the same day,
    Wieghardt1953 and Brown2003.
  - The owner checked the key values against the PDFs.
  - Recorded D-009 (the validation reference), the fan-to-chamber diffuser and settling-chamber design inputs, and the
    owner's model-car downforce idea.
  - Committed and pushed as `c04de1b`. See [the session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md).
  - The follow-up (push record and the new repo URL) was committed and pushed as `b22a45b`.
- 2026-11-02/03: the Mega 2560 board brought up. The owner installed the Arduino IDE and uploaded a modified Blink,
  which Verified the board, the cable and the upload path (§3). Committed and pushed as `36f39eb`. See
  [the session log](docs/sessions/2026-11-03-mega-2560-board-test.md).
- 2026-11-05/07: top speed and fan search (documentation only; nothing bought or built).
  - The agent recommended a 13 m/s top speed, with validation runs from about 6.5 m/s (estimates; open question 3).
    The owner has not confirmed it.
  - Explained what a fan's listed maximum static pressure means, and corrected the fan requirement: 400 CFM and
    300 Pa give only about 11.5–12 m/s, so 13 m/s needs about 500 Pa at 400 CFM.
  - Assessed the VEVOR 6-inch AC fan the owner found (unsuitable as listed), then searched for cheaper fans. None
    with a published pressure figure meets 13 m/s for less than the Cloudline S6's $99 (§3).
  - Not committed yet. See [the session log](docs/sessions/2026-11-07-top-speed-and-fan-search.md).

## 7. Data and analyses

No data collected. No analyses completed. See [docs/data_catalog.md](docs/data_catalog.md).

## 8. Results

| Result | Status | Source |
|---|---|---|
| None yet | n/a | n/a |

Estimates are spread across these files; all are **calculations from assumed values, not results**:
- [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#order-of-magnitude-estimates): sphere drag, printable contraction
  sizes, fan requirements, the [tunnel length budget](PROJECT_BACKGROUND.md#tunnel-length-budget) with fan
  top-speed estimates, and the [top-speed trade-off](PROJECT_BACKGROUND.md#top-speed-trade-off-proposed) with the
  fan pressure needed for 13 m/s (2026-11-05).
- [resources/notes/HX711.md](resources/notes/HX711.md): the HX711 noise floor for example load cells.
- [resources/notes/Cooper1998.md](resources/notes/Cooper1998.md#what-it-suggests-for-this-project-proposed):
  blockage-correction sizes and test-section positions.
- [2026-11-01 session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#6-measurements-and-results):
  airspeed from candidate fans, drone-sensor range against our pressures, and the force on removable panels.
- [resources/notes/Brown2003.md](resources/notes/Brown2003.md): the reference C_D at the planned test conditions, and a
  pixel measurement of the paper's data near this project's Re. These are literature values, not our results.
- [resources/notes/Mehta1977.md](resources/notes/Mehta1977.md),
  [Scheiman1981.md](resources/notes/Scheiman1981.md) and [Wieghardt1953.md](resources/notes/Wieghardt1953.md):
  diffuser length and screen counts, screen K at low speed, and settling-chamber spacings.

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on choosing and buying hardware (fan, pressure sensor, load cell).
  - The fan choice and the pressure-sensor range wait on the owner confirming the target top speed (13 m/s proposed
    2026-11-05, open question 3) and choosing a fan (§3).
  - The owner wants a fan cheaper than the Cloudline S6 ($99). The cheaper EC candidate, the AeroZesh S6, has no
    published static pressure, so it cannot be checked yet.
  - The microcontroller is no longer a blocker: the board works (2026-11-02, §3).
- Resolved: the owner committed the 10.2 MiB sketch PDF uncompressed in `8fda08f` (under D-004's 25 MB limit). It stays
  in Git history.
- No known software bugs.
- Watch: at the 2026-11-02 `/wrap` the test suite took about 28 minutes (1,662.7 s) instead of the usual 13–16 s, and
  all 20 tests still passed. Cause unknown, not investigated. If it recurs, run the tests with `-v` to see which one
  stalls ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md#8-errors-failed-approaches-and-troubleshooting)).
  It has not recurred since: 20 tests in 7.9–11.3 s at every run from 2026-11-02 to 2026-11-07.
- Network (resolved 2026-10-31): the PC lost its IPv4 address, which blocked GitHub and some other sites. If
  `FETCH_FAILED` with "Could not resolve host" comes back, see Lessons learned in
  [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#lessons-learned).
- Risk: the project folder is inside OneDrive. OneDrive syncing a `.git` folder can cause conflicts if the repo is
  edited from two machines. GitHub, not OneDrive, is the source of truth between machines.
- Local-only references: Barlow1999 and Ewald1998 (full AGARD-AG-336) are ignored by Git (D-006). A fresh clone from
  GitHub on a machine without OneDrive will not have them.
- Copyright: several PDFs are publisher-copyrighted (Mehta1979 and Wieghardt1953 under Cambridge Core terms; Roos1971
  AIAA; Brown2003 ASCE, "for personal use only"; Mehta1977 and Bradshaw1964 journal reprints; Morel1975 ASME), and the
  Abdelhamed2014 licence is not checked. Fine
  while the repo is private (D-003); review before making it public. Barlow1999 is a commercial textbook and stays out
  of Git. AGARD-AG-336 states there are no restrictions on its distribution.

## 10. Open engineering questions

1. **Microcontroller: answered for the board itself.** The owner's Elegoo Mega 2560 (5 V logic) works: the main chip
   reads ATMEGA2560 and a modified Blink uploaded (2026-11-02, §3). Still needed:
   - a check that the chosen pressure sensor and BME280 board work at 5 V on its I²C pins (20/21);
   - minor: whether the board is marked "R3", which tells whether SDA/SCL are also brought out next to AREF.
2. **What is the op-amp signal conditioning for?** Proposed (agent, 2026-11-01): nothing in the measurement chain.
   - The HX711, a digital pressure sensor and the BME280 need no analog conditioning, and commercial digital sensors
     will be more accurate than an analog front end built here.
   - The owner's circuit design work goes into the interface board instead: connectors, I²C pull-ups, decoupling,
     the display and knob headers (the servo and angle dial are no longer needed with preset angles). See TODO P2.
   - If an analog sensor is ever used, the kit's LMC6484 suits a single 5 V supply better than the LM741, which
     needs split supplies (TI calls the LMC6484 rail-to-rail; its datasheet is not yet in `resources/`).
3. **Top airspeed and sphere diameter.** The test section is 100 mm (D-008), and the length target is about 1 m,
   with more allowed. Still open:
   - the owner's target top speed. **Proposed (agent, 2026-11-05): 13 m/s**, with validation runs from about
     6.5 m/s. Reasons (estimates; [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#top-speed-trade-off-proposed)):
     - the trend check gains little above it. Eq. (19) rises 8.7 % from the 20 mm sphere at 6.5 m/s to the 25 mm
       sphere at 13 m/s, and 9.8 % at 15 m/s;
     - one 6-inch fan listing about 500 Pa should just reach it. 15 m/s needs an 8-inch fan or two fans, and 1.5×
       the power;
     - q = 101 Pa fits a ±125 Pa sensor (full scale at 14.4 m/s).

     The cost: drag grows with V², so 15 m/s would give about 35 % more force (1.9 instead of 1.4 gf on the 20 mm
     sphere). If the real fan reaches only 11–12 m/s, the validation still works (about 1.0 gf and a 7 % rise at
     11 m/s). The owner asked follow-up questions about the fan but has not confirmed the speed;
   - the sphere diameters: proposed about 20 mm (3.1 % blockage) and 25 mm (4.9 %) for the two-size check.
     Run the two sizes at **matched Re**, not matched speed: at the same speed the 25 mm sphere sits at 25 % higher Re
     and about 2 % higher reference C_D (D-009).
   - D-009's trend check needs runs over a range of speeds, so the fan should run steadily at low speed as well.
     The proposed low end is about 6.5 m/s (2026-11-05): below that the 20 mm sphere's drag is only 0.2–0.3 gf and q
     about 15–25 Pa, so fixed zero errors dominate.
4. **Pressure-sensor range.** Dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate).
   - Candidates: ±125 Pa (SDP810-125Pa, SDP32), ±249 Pa (Honeywell HSC ±1 inH₂O) and ±500 Pa (SDP810-500Pa, SDP31).
   - Drone airspeed sensors (MS4525DO, ±1 psi) are ruled out: at 10 m/s, q is 0.44 % of their span (our arithmetic).
   - Choose after the top speed. With the proposed 13 m/s: ±125 Pa (the SDP810-125Pa).
5. **Load-cell capacity.** Expected sphere drag is only about 1–2 grams-force at 10–15 m/s in the 100 mm section
   (estimate).
   - Overload protection for model swaps is needed: small bar cells are typically rated for only about 120 % of
     capacity (§2).
   - The load cell also carries the sphere's support (sting/mount), whose drag must be measured and subtracted.
   - A smaller cell lowers the HX711 noise in grams but has less overload margin
     ([HX711 notes](resources/notes/HX711.md)). Not chosen.
6. **Which published Cd value applies at the test Reynolds number? Answered 2026-11-02 ([D-009](DECISIONS.md),
   Accepted).**
   - The reference is Brown and Lawler (2003) Eq. (19) at each run's Re: about 0.42–0.445 for Re 1.3–2.5×10⁴. The band
     is about ±10 %.
   - Morrison2013 reads 7–11 % low here. Roos1971's points at this Re were excluded by Brown and Lawler for vibration.
   - Still open: the band could shrink with the original data tables near Re = 10⁴ (likely Lunnon 1928 and Vlajinac
     and Covert 1972, not checked).
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
13. **Screens and honeycomb: bought or printed, and which mesh?** Added 2026-11-02.
    - Bought or printed honeycomb: a printed one has thick walls.
    - Screen mesh and open area: at least 58 % open.
    - Whether to measure a sample screen's pressure drop at about 2 m/s, where the formulas are extrapolated.
    - Settling-chamber length: 150–200 mm or about 230–300 mm (§2).
14. **Plan now for a second, vertical load cell?** The owner's model-car downforce idea (2026-11-02) and airfoil lift
    (P3) both need one. Leaving room in the balance box costs little now. The owner said it was "just an idea"; no
    decision yet.

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
- **The expected sphere C_D at the planned Re is about 0.42–0.445, not 0.47, and it is known only to about ±10 %**
  (2026-11-02; [Brown2003 notes](resources/notes/Brown2003.md)).
  - Brown and Lawler's Eq. (19) and Clift's standard curve agree within about 1 %. Clift was fitted to almost the same
    data, so this is not an independent check.
  - Brown and Lawler's own plotted data at this Re sit about 7 % above Eq. (19), with about ±8 % scatter. That is our
    pixel measurement, with the axes checked against the Stokes region.
  - Brown and Lawler excluded Roos1971's high-Re points for vibration, the same judgement made independently here.
- **Fan-to-chamber diffuser and settling chamber** (2026-11-02; Mehta1977, Scheiman1981, Wieghardt1953):
  - two diffuser screens allow a diffuser of about 150–200 mm;
  - at about 2 m/s the settling-chamber screens have about twice their high-speed K and make no turbulence of their
    own;
  - a honeycomb followed by one screen gave far better turbulence reduction than screens alone.

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:**
   - commit and push this session's changes (commands in the
     [session log](docs/sessions/2026-11-07-top-speed-and-fan-search.md#13-manual-git-commands-as-given-to-the-owner));
   - confirm or change the proposed 13 m/s top speed (open question 3);
   - choose the fan (§3). The agent's advice (2026-11-05): first ask VIVOSUN for the AeroZesh S6's maximum static
     pressure or fan curve (the agent offered to draft the message). Buy it if the figure is about 450 Pa or more;
     otherwise buy the Cloudline S6 ($99 on AC Infinity's site). A used or open-box S6 is fine if its bearings run
     quiet. For the Delta pair, give the bench supply's maximum voltage and current;
   - answer the settling-chamber spacing question (open question 13), asked 2026-11-02;
   - list any other electronics and the magnets' type and size (open question 9);
   - confirm or change D-003, D-004, D-006 and D-007's open exit;
   - optionally, say whether to leave room for a second load cell (open question 14).
2. **Agent, build step 1:** once the owner confirms the top speed, record it as D-010 (and under "Requirements and
   constraints" in PROJECT_BACKGROUND.md). Then detail the 100 mm tunnel. All the design inputs are now reviewed.
   - Fan-to-chamber diffuser: Mehta1977.
   - Settling-chamber stack: Scheiman1981 and Mehta1977 (open question 13).
   - Contraction, test section, removable panels, balance box, sting lock and overload stops.
   - Then recompute the [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget) and the fan pressure, using the
     low-speed screen K from Wieghardt1953.
3. **Agent, with sizing:** read Barlow1999 ch. 9–10 (solid blockage) and ch. 6 (reference-pressure placement and
   test-section calibration).
4. **Owner:** download the electronics datasheets ("Wanted" items 1–4 in [resources/README.md](resources/README.md),
   now including the SDP8xx and LMC6484), and the chosen fan's datasheet or fan curve.
5. Choose the pressure sensor, load cell, screens and honeycomb from step 2's numbers, then buy.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer/wind-tunnel (private; holds `cc51fff`, `5bc60f0`, `b710093`,
  `7db221f`, `9b42a07`, `748dae9`, `8fda08f`, `c04de1b`, `b22a45b` and `36f39eb`). The account was `nuhshaheer-2007` until
  2026-11-02, and the old URL redirects. The local `origin` points at the new URL (checked 2026-11-02).
- Branch: `main`
