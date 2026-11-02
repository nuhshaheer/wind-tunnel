# 2026-11-01: Parts review, kit inventory and tunnel layout

- **Session ID:** edc44a90-0a86-45f3-8527-50425c926745 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** `748dae9` (part 1, up to the first `/wrap`; pushed 2026-11-01). Part 2 (after that wrap): `8fda08f`
  (committed 2026-11-01; found on GitHub at the 2026-11-02 `/catchup`)

This session was wrapped twice. **Part 1** (up to the first `/wrap`) is in `748dae9`. **Part 2** is everything after
it: the owner's sketch, the tunnel layout decisions (D-007, D-008), fan candidates and the controls. Each section below
covers part 1 first, then part 2.

## 1. Starting state and objective

**Starting state** (from `/catchup`, 2026-11-01):

- Sync state `UP_TO_DATE` at `7db221f`.
- 10 uncommitted paths (7 modified, 3 new): exactly the previous session's `git add` list. That session had been
  wrapped but not committed.
- `check_docs.py`: 0 failures, 0 warnings. Tests: 20/20 passed.
- No docs-vs-reality discrepancies: the docs correctly said that session was "not committed yet". No stashes, no other
  branches. Ignored files: Barlow1999 and Ewald1998 (D-006) and `__pycache__/`.

**Objectives (owner requests, in order):**

1. "Check my disk as well, is there anything uncommitted?"
2. "git commit isn't committing the uncommitted changes."
3. Questions on the TODO list, what to get out of the resources ("I haven't read any of our resources yet"), the main
   plan, how objects are placed in the tunnel, and what is measured and how.
4. The owner shared the ECE kit's packing list (`PartsListECE2010.pdf`) and said they have an Elegoo Arduino and
   possibly more electronics. They also shared:
   - their plan to design the circuit, maybe test it on a breadboard, then make a PCB;
   - an FPV pitot kit they found ($50);
   - a variable fan link;
   - a request for a "bubbler that can make thick smoke".

   They asked what to look for in each part and at what price.
5. Board identified as an "ELEGOO Mega 2560 R3" ("that is what it looks like at least"); its cable is lost. Questions:
   - What is the cable called?
   - How do you check that it carries data?
   - Is the UGREEN USB A-to-B printer cable (5 ft, 480 Mbps) right? The owner is ordering it.
6. The owner found magnets and proposed removable acrylic panels held by magnets instead of a sliding mechanism.
7. "What fans are we thinking? Should they look like a PC fan?"
8. Run `/wrap`.

**Part 2 objectives (owner requests after the first `/wrap`, in order):**

9. The owner has "a multimeter, a soldering station, and … a bench that I have access to". Won't a load cell be too
   big and disturb the flow?
10. "What's a sting?" What is a good sting length; is longer better or worse?
11. What length should the tunnel itself be?
12. "I was thinking about a 1m length total for everything." The owner added a drawing of the tunnel
    (`resources/Wind Tunnel - diagram #1.pdf`) and asked for a review.
13. Correction: not two swappable test chambers, but one chamber whose side and/or top acrylic panel comes off to swap
    the model. The knob is for a menu "like the menu for an Ender 3 with a knob": choose what to see (drag force),
    change the fan speed.
14. Answers: the 1 m includes the fan, and "we can also go more than 1m if needed"; "The fan will go at the front.
    That will be better"; "I have a bench power supply as well"; "you may move the sketch".
15. "Would a longer test section be better? like a 200 mm test section".
16. "Let's keep it at 100mm." "I don't really have a budget … most projects would be under 50 cuz they aren't doing a
    load cell." What fan are we looking for?
17. Run `/wrap` again.

## 2. Work completed

**Uncommitted work and the commit problem:**
- The agent listed the 10 uncommitted paths and confirmed nothing else was pending.
- The owner's `git commit` committed nothing: `git status` showed no files staged. The agent explained staging and
  gave the `git add` lines again.
- The owner then committed and pushed `9b42a07` (2026-11-01 00:18 −0400). It holds the same 10 files and the
  message the previous log gave. `/wrap` confirmed `UP_TO_DATE`.

**Plan explained to the owner** (no doc change needed; it restates existing content):
- the TODO list by priority;
- the tunnel layout: fan → settling chamber (honeycomb, screens) → contraction → closed test section → open exit;
- mounting: sphere on a sting through a floor slot to an upright load cell outside the tunnel;
- what is measured: F, q, p and T, and d;
- what is computed: ρ, V, Re and C_D;
- the run procedure and the corrections.

The mounting description was added to PROJECT_BACKGROUND's measurement approach.

**Reading guide for the owner** (now TODO P1, owner task):
- Read Mehta1979 and Weakly2024 in full, and the notes files for Bell1988, Maskell1963, Cooper1998 and HX711.
- The goal is to answer five questions: what each part does; what sets the sizes; how gram-level forces are
  measured; why 0.47 holds only over a Re range; why walls change drag.
- The agent pointed out a gap: no way of reaching the model had been planned.

**ECE kit inventory:** transcribed from the packing list (WPI ECE2010 Lab 2) into
[docs/experimental_setup.md](../experimental_setup.md#parts-on-hand). Points that matter for the project:
- LMC6484: TI's page confirms a rail-to-rail CMOS quad op-amp with a 3–15 V supply.
- LM7805CT and LM317T regulators.
- A 10 kΩ potentiometer, a candidate for the angle dial.
- Pull-up resistors and decoupling capacitors, a breadboard and jumper wires.
- Not in the list: a multimeter, soldering iron or power supply.

**Microcontroller:** the owner's Elegoo Mega 2560 R3 recorded as on hand and untested.
- Facts from Mega 2560 Rev3 documentation, via retailer pages: 5 V logic; I²C on pins 20/21, also brought out next to
  AREF on R3; ATmega16U2 USB-serial; USB Type-B socket.
- Cable: "USB A to USB B" (printer cable), or USB-C to USB-B for a USB-C-only laptop.
- How to confirm data transfer: a new COM port in Device Manager, then a Blink upload. The power LED alone proves
  nothing.
- The owner is ordering the UGREEN cable; the agent confirmed it is a USB 2.0 data cable.

**Circuit plan** [Proposed]:
- Digital modules (HX711, an I²C pressure sensor, BME280) with no op-amps in the measurement chain.
- The owner designs a Mega shield PCB (KiCad) carrying connectors, pull-ups, decoupling, servo power from the LM7805
  and the dial input.
- Breadboard testing for the digital wiring only; the load-cell leads are soldered to the HX711 (Weakly2024 lesson).

**FPV pitot kit assessed** (FPVDrone "PX4 Differential Airspeed Pitot Tube", $49.99, I²C, from the owner's
screenshot):
- The probe is a suitable pitot-static type.
- The sensor is not. The listing does not name the chip, but these kits use the TE MS4525DO, and the white dual-port
  package in the photo matches. That chip reads ±1 psi.
- Recommendation: buy the probe alone and a Sensirion SDP810 (125 or 500 Pa).

**Fan link assessed:**
- The link carries Aki's affiliate tag (`akitechspace-20`), so it is probably the "variable fan" from his video.
- Amazon title: "Computer Fan with AC Plug, AC 100-240V Vriable Speed Fan …" (sic).
- Retailer listings: Qirssyn QYN1225BSP1, 120 mm, about 95 CFM at 3000 RPM; one lists a 2 × 120 mm version.
- Far too small (§6).

**Fan type** [Proposed]: an inline mixed-flow duct fan with a speed controller and a published fan curve.
- Compared with PC fans, box fans and centrifugal blowers.
- Mounted on its own stand with a flexible coupling, and a printed round-to-square widening section.
- 6-inch vs 8-inch decided by the top speed.

**Part criteria and prices:** a table of what to look for in each part with prices seen online (PROJECT_STATUS §3,
TODO P1). Rough total for the electronics plus a 6-inch fan: about $200.

**Smoke or mist options** (owner deferred visualization on 2026-10-31):
- ultrasonic mist maker (agent's first choice);
- glycol fog machine: thickest, but warm, oily residue, smoke alarms;
- smoke wire: a possible owner circuit project.

**Magnetic removable panels** (owner's idea) [Proposed], with the agent's design points:
- pins or lips locate each panel; flush inner face; foam gasket;
- the floor stays fixed; the pitot goes through a fixed wall;
- a non-magnetic sting, with no magnets near ferrous parts of the balance;
- holding-force estimate (§6); 3–5 mm cast acrylic; mark the magnet poles.

### Part 2 (after the first `/wrap`)

**Load cell, sting and tunnel length explained** (answers to objectives 9–11):
- The load cell sits outside the airflow, in a closed box under the floor; only the sphere and a thin sting are in
  the wind. Sting points: never touching the slot edges; a closed box so slot leakage cannot blow on it; measure the
  sting alone and subtract it; an optional fixed fairing; calibrate by pulling at the sphere's position.
- A sting should be as short and stiff as the layout allows (cantilever deflection ∝ L³). The vibration estimate and
  the length-by-section rules are in §6 and in
  [PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#tunnel-length-budget).
- The agent asked whether "a bench" meant a workbench or a bench power supply. The owner later said they also have a
  bench power supply ("as well"), so both are recorded.

**The owner's sketch reviewed** (objective 12). It shows a contraction, a test chamber with the sphere on a thin rod
from below, an "electronics house" box under the test chamber, an exit diffuser, and a close-up of the electronics
house with a screen and a knob. The test chamber is drawn twice, once with the sphere and once with an airfoil on a
pivot, with the owner's note that a pivoting airfoil ruins the force measurement, so the angles should be preset.
- The agent first misread the two chamber drawings as two swappable chambers; the owner corrected this (objective 13).
- Not drawn: the fan, the settling chamber, the honeycomb and screens.
- Agent's points: the electronics house is the closed balance box; keep only the load cell and HX711 in it and put
  the display, knob and Arduino in a separate box (a pressed knob bumps the balance, warm electronics drift the cell);
  a 1 m budget fits about a 100 mm test section; the drawn exit diffuser cannot fit (about 0.75 m by Mehta1979's
  rule); preset angles via an indexed hub; lift would need a second load cell (Weakly2024 used two).
- The sketch's shape is a suction tunnel. The agent noted that its sealed electronics box removes the main argument
  against suction (inward leakage through the sting slot) and asked where the fan goes. The owner chose the front
  (blower).

**One chamber with removable panels and the Ender 3–style menu** (objective 13):
- Floor fixed; the top panel gives the best reach to the sting tip.
- **Load-cell protection for model swaps** (new): small bar cells are typically rated for only about 120 % of capacity,
  and screwing a model on twists and pushes the sting. Proposed: a sting lock, overload stops, a low-twist attachment,
  and a wind-off zero after every swap.
- Menu hardware compared (20×4 I²C LCD, 128×64 graphic LCD as on the Ender 3, 1.3" OLED, a KY-040/EC11 encoder;
  typical prices from memory, not checked). Recommendation: a 20×4 LCD and an encoder first.
- Design points: the fan speed can be set from the menu only if the fan has a documented low-voltage control input,
  and the Arduino never switches mains; the laptop log stays the data record; refresh the screen 2–5 times a second;
  the encoder on interrupt pins 2/3 or 18/19, the display on I²C 20/21.

**Sketch filed** (owner's permission, objective 14): moved from `resources/Wind Tunnel - diagram #1.pdf` (untracked,
never committed) to [docs/sketches/2026-11-01_tunnel-concept-sketch-1.pdf](../sketches/2026-11-01_tunnel-concept-sketch-1.pdf),
with a new index [docs/sketches/README.md](../sketches/README.md) and a line in the README's repository structure.
The file is unchanged: a single-page PDF from iOS, 10,731,621 bytes (10.2 MiB). That is over the roughly 2 MB
guideline for photos and scans in data/README.md; the owner was asked whether to compress it and has not answered.

**Layout decisions by the owner** (objectives 14–16):
- **D-007:** an open-circuit blower with the fan at the front. The agent's proposed order: fan → flexible coupling →
  wide-angle diffuser with screens → settling chamber → contraction → test section → open exit (no exit diffuser).
- **D-008:** a 100 mm × 100 mm test section. The agent first recommended 100 mm to fit the 1 m target. When the owner
  allowed more length and asked about 200 mm, the agent showed a 100/150/200 mm comparison and suggested 150 mm as a
  middle ground or 200 mm for the easiest force measurement. The owner chose 100 mm.
- Clarified for the owner: "test section" size means its width and height. Its length follows from them (about
  2.8 h), and a longer chamber does not help.

**Budget and fan** (objective 16):
- The agent explained that the load cell and HX711 are only about $20; the fan and the pressure sensor are the main
  costs. Estimated total: about $120–200.
- Fan requirement for the 100 mm section, and candidates with their listed specs: VIVOSUN 6-inch booster fans
  (unsuitable), VIVOSUN AeroZesh S6, AC Infinity Cloudline S6, and Delta PFR1212UHE-SP00 12 V PWM server fans. The
  agent's pick is a 6-inch mixed-flow EC fan; the Delta pair is the route to menu control of the fan from day one.
  Details in §6 and PROJECT_STATUS §3.

## 3. Files and equipment affected

**Created:** this log.

**Modified:**

- `PROJECT_STATUS.md`:
  - header and stage;
  - objectives: interface board added;
  - §2: fan type and model access added;
  - §3: hardware table rewritten with on-hand items, candidates and prices;
  - §4: `/catchup` and `/wrap` evidence;
  - §6 work completed; §8 estimate pointers; §9 blockers;
  - open questions 1, 2, 4, 7 and 9;
  - next steps and repository (`9b42a07`).
- `TODO.md`:
  - P0: the commit task now points to this session; new board-setup task; kit task narrowed to what is still unknown;
  - P1: new owner reading task; sizing gains the magnetic-panel design points; the fan, pressure-sensor, load-cell,
    ambient-sensor, microcontroller and op-amp tasks gain criteria and candidates;
  - P2: new interface-board task; mist task gains the generator options;
  - two Done entries.
- `docs/experimental_setup.md`:
  - current configuration;
  - model-access, fan, mount and microcontroller rows;
  - new "Parts on hand" section with the full kit list;
  - a change-history row.
- `PROJECT_BACKGROUND.md`:
  - requirements: kit list pointer, the owner's circuit → breadboard → PCB plan, the Mega;
  - measurement approach: the mounting step;
  - uncertainty: magnetic pull on the balance;
  - two lessons learned (`git commit` without `git add`; Amazon pages too large to fetch).
- `resources/README.md`:
  - Aki video row: fan probably identified;
  - Wanted item 1: SDP810 added, MS4525DO kits marked unsuitable;
  - Wanted item 3: LMC6484 and LM7805CT added;
  - "Later": Mega 2560 documentation.
- `docs/sessions/SESSION_LOG.md`: `9b42a07` backfilled; this session's row added.
- `docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md`: commit field backfilled to `9b42a07` (the only
  edit to that log).

**Not changed:**
- DECISIONS.md: no decision was made. The Mega is untested and the panels and fan are proposals.
- docs/data_catalog.md: no data.
- README.md: its original hardware list is incomplete but not wrong, and it points to PROJECT_STATUS.
- CLAUDE.md.

**Equipment:**
- Recorded as on hand (owner's statements and packing list): the ECE2010 kit, an Elegoo Mega 2560 R3 and magnets.
- Being ordered by the owner: a UGREEN USB A-to-B cable.
- Nothing bought, built or tested by the agent.

**Not in the repo:** `PartsListECE2010.pdf` stays in the owner's Downloads folder. Whether to file it in the repo
is a question for the owner (§10).

**Scratch files** (session scratchpad, outside the repo):
- `estimates_2026-11-01.py` (§6 arithmetic);
- `sensor_crop.png` (crop of the owner's product screenshot; the chip label was unreadable).

### Part 2

**Created:**
- `docs/sketches/README.md` (index of the owner's sketches);
- `docs/sketches/2026-11-01_tunnel-concept-sketch-1.pdf` (the owner's file, moved from `resources/`, unchanged).

**Modified:**
- `DECISIONS.md`: D-007 and D-008 appended; D-005's status line notes that its size intent is superseded by D-008.
- `PROJECT_STATUS.md`: header, stage, objectives (menu, preset angles), §2 rewritten (tunnel type, size, contraction,
  settling chamber, model access, balance and controls layout), §3 (tools, fan candidates, display and knob, servo,
  budget, load cell), §4 `/wrap` row, §6, §8, §9, open questions 2, 3, 5, 7, 9 and new 11–12, §12, §13.
- `TODO.md`: P0 (commit with the sketch decision, top speed, fan choice, parts list, tentative decisions); P1
  (sizing, papers, fan, sphere, load cell, buy); P2 (interface board, new firmware-and-menu task); P3 (preset
  angles); four Done entries.
- `docs/experimental_setup.md`: current configuration, tunnel geometry, flow generation, instrumentation, data
  acquisition, test models, parts on hand, change history.
- `PROJECT_BACKGROUND.md`: motivation (preset angles), requirements (blower, 100 mm, length, model access, controls,
  tools, budget), new "Tunnel length budget" estimate section, measurement step 3 (box layout and swap protection).
- `README.md`: `docs/sketches/` added to the repository structure.
- This log and its index row.

**Not changed:** `CLAUDE.md`; `docs/data_catalog.md` (no data); `resources/README.md` (no new references). The
README's original hardware list still names a servo; it is the owner's original plan and points to PROJECT_STATUS for
the current state.

**Equipment:** recorded as on hand (owner's statements): a multimeter, a soldering station, a bench power supply and
access to a workbench. Nothing bought, built or tested.

**Scratch files** (session scratchpad, outside the repo; the rules in §6 reproduce them):
- `tunnel_length.py` (length by section, three sizes, CR 6.25 and 9);
- `blower_budget.py` (blower lengths with a 6-inch fan, forces, speeds);
- `size_compare.py` (100/150/200 mm comparison);
- `fan_operating_point.py` (straight-line fan-curve top speeds);
- `edit_setup.py` (a one-off text replacement used to edit docs/experimental_setup.md).

## 4. Experimental procedures performed

None. No physical work this session (either part); no hardware has been tested.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch            # /catchup: UP_TO_DATE at 7db221f; /wrap: UP_TO_DATE at 9b42a07
git status --short; git status --short --ignored; git diff --stat; git log --oneline -15; git stash list; git branch -a -vv
git diff <small files>; git show --stat 9b42a07
python scripts/check_docs.py
python -m unittest discover -s tests [-v]
find /c/Users/nuhbm/Downloads /c/Users/nuhbm/OneDrive/Desktop /c/Users/nuhbm/Desktop -maxdepth 3 -iname "*PartsList*"
python -I <scratch>/estimates_2026-11-01.py
python -I -c "<PyMuPDF crop of the owner's screenshot>"   # chip label unreadable at that resolution
```

Web lookups (WebSearch and WebFetch), all on 2026-11-01:
- the Amazon fan page (B092C65F3P);
- the Qirssyn fan specs;
- MS4525DO airspeed modules and the TE datasheet's error band;
- SDP31/SDP32/SDP810 prices, supply voltage and breakouts;
- Dwyer 160 pitot prices and drone pitot probe prices;
- AC Infinity 6-inch inline fans;
- Arduino Mega 2560 Rev3 pins and USB;
- the TI LMC6484 and LM7805 pages and the LM7805CT maker.

Sources used:
- [Desertcart: Qirssyn QYN1225BSP1](https://www.desertcart.com.sa/products/331448582)
- [Newegg: 2 × 120 mm version](https://www.newegg.com/p/3C6-020A-00J50)
- [Evelta: Matek ASPD-4525 (±1 psi, 0.84 Pa)](https://evelta.com/matek-aspd-4525-digital-airspeed-sensor-for-rc-fpv-racing-drone-flight-controller/)
- [Holybro MS4525DO](https://holybro.com/products/digital-air-speed-sensor)
- [TE MS4525DO datasheet](https://www.mouser.com/datasheet/2/418/MS4525DO-710170.pdf)
- [JLCPCB: SDP810-125PA](https://jlcpcb.com/partdetail/SDP810-125PA-D/C153055)
- [Newark: SDP810-500PA](https://canada.newark.com/sensirion/sdp810-500pa/pressure-sensor-diff-500pa-digital/dp/10AC5102)
- [SOS Electronic: SDP810-125Pa](https://soselectronic.com/it-sm/products/sensirion/sdp810-125pa-1-232972)
- [Hubtronics: SDP810-125Pa](https://hubtronics.in/sensirion/sdp810-125pa-digital-differential-pressure-sensor)
- [Farnell: SDP31 (3.3 V)](https://ch.farnell.com/en-CH/sensirion/sdp31-500pa/pressure-sensor-500pa-3-3v/dp/2627785)
- [SparkFun SDP31 breakout (retired)](https://www.sparkfun.com/sparkx-differential-pressure-sensor-sdp31-qwiic.html)
- [Tequipment: Dwyer 160](https://www.tequipment.net/Dwyer/series_160-ss-pitot-tubes)
- [Unmanned Tech: pitot probe](https://www.unmannedtechshop.co.uk/products/arduplane-pitot-tube-for-apm-2-5-2-6-2-8-airspeed-sensors)
- [VXB: pitot tube](https://vxb.com/products/airspeed-pitot-tube-for-pixhawk-px4-flight-control)
- [Trimleaf: Cloudline S6](https://trimleaf.com/products/ac-infinity-cloudline-s6-inline-fan-system)
- [Hydrobuilder: Cloudline A6](https://hydrobuilder.com/products/ac-infinity-6-cloudline-a6-quiet-inline-fan-with-speed-controller-352-cfm)
- [Pololu: Arduino Mega 2560 R3](https://pololu.com/product/1699)
- [Farnell: Mega 2560 datasheet](https://www.farnell.com/datasheets/1658657.pdf)
- [TI LMC6484](https://www.ti.com/product/LMC6484)
- [DigiKey: onsemi LM7805CT](https://www.digikey.ph/en/products/detail/onsemi/LM7805CT/458698)
- [Octopart: LM7805CT](https://octopart.com/part/onsemi/LM7805CT)

### Part 2

```bash
python -I <scratch>/tunnel_length.py; python -I <scratch>/blower_budget.py
python -I <scratch>/size_compare.py; python -I <scratch>/fan_operating_point.py
mkdir -p docs/sketches
mv "resources/Wind Tunnel - diagram #1.pdf" docs/sketches/2026-11-01_tunnel-concept-sketch-1.pdf
python scripts/check_docs.py
python -I <scratch>/edit_setup.py docs/experimental_setup.md
# a short Python reader over this session's Claude Code transcript (.jsonl), to quote the earlier sting and
# length answers accurately after the conversation was compacted
# /wrap (second run):
python scripts/sync_status.py --fetch; git status --short; git diff --stat; git log --oneline -20
git log --format=%h -1 -- docs/sessions/2026-11-01-parts-review-and-kit-inventory.md   # -> 748dae9
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

Web searches (WebSearch, standard mode), 2026-11-01:
- AC Infinity Cloudline S6 dimensions;
- 6-inch inline duct fans (VIVOSUN, iPower) with prices;
- the Delta PFR1212UHE specs and price;
- the VIVOSUN AeroZesh S6's static pressure (not found).

Sources used:
- [Eddis Wholesale: Cloudline S6 (7.9 × 12.6 × 8.4 in)](https://eddiswholesale.com/cloudline-s6-quiet-inline-duct-system-fan-speed-controller)
- [Happy Hydro: Cloudline S6](https://happyhydro.com/collections/environment-fans-ducting-ventilation/products/cloudline-s6-quiet-inline-duct-fan-system-with-speed-controller-6-inch)
- [Hydrobuilder: Cloudline PRO S6](https://hydrobuilder.com/products/ac-infinity-6-cloudline-pro-s6-quiet-inline-fan-with-speed-controller-402-cfm)
- [VIVOSUN: 6″ booster fan](https://vivosun.com/vivosun-inline-booster-duct-fan-6-inch-p145955416053478450-v145958679691764021)
- [Walmart: inline duct fans (AeroZesh S6 from $62.99; VIVOSUN booster $38.99)](https://www.walmart.com/c/kp/inline-duct-fans)
- [VIVOSUN: AeroZesh S6](https://vivosun.com/-p90271565918111669-v90271565918111650)
- [Home Depot: AeroZesh S6 with E12 controller](https://www.homedepot.com/p/VIVOSUN-AeroZesh-S6-6-in-405-CFM-Inline-Duct-Fan-with-E12-Speed-Controller-wal-VSV-AZS6/328082850)
- [DigiKey: Delta PFR1212UHE-SP00](https://digikey.cn/en/products/detail/delta-electronics/PFR1212UHE-SP00/3083223)
- [Delta PFR series datasheet (Chipdip)](https://static.chipdip.ru/lib/302/DOC012302441.pdf)
- [Avnet: Delta PFR1212DHE-SP00 ($30.90)](https://www.avnet.com/americas/product/delta-group/pfr1212dhe-sp00/evolve-2271306/)

## 6. Measurements and results

No measurements. Calculated estimates only; status: estimate, not a result. Assumptions: ρ = 1.20 kg/m³,
q = ½ρV². Computed by `python -I <scratch>/estimates_2026-11-01.py`.

**MS4525DO (±1 psi) against our pressures:**
- Span 13,790 Pa, about 28.7× our largest q (240 Pa at 20 m/s). At 10 m/s, q = 60 Pa is 0.44 % of the span.
- One count (0.84 Pa, Matek listing) is 1.4 % of q at 10 m/s and 5.6 % at 5 m/s.
- TE's total error band, ±1 % of span (as summarized online), is about ±138 Pa. Wind-off zeroing removes part of that,
  not all.

**Fans:**

| Fan | Rating used | Result |
|---|---|---|
| Qirssyn 120 mm | 95 CFM = 161 m³/h, free air | At most 4.5 m/s through a 100 mm section, even with no screens |
| 6-inch inline (AC Infinity Cloudline S6/T6) | 402 CFM = 683 m³/h free air, listed about 503 Pa maximum; **assumed 70 % of free-air flow at the operating point** (no fan curve found) | 478 m³/h: about 13.3 m/s in a 100 mm section (needs about 132 Pa of fan static pressure, open exit) and 9.2 m/s in a 120 mm section (about 64 Pa) |

**Panel holding force:**
- Assumed: in a blower with an open exit, the settling chamber sits above room pressure by roughly the test section's
  q.
- A 0.5 m × 0.5 m panel would see about 15 N at 10 m/s and 60 N at 20 m/s.
- Test-section panels sit near room pressure.

**Prices seen** (retailer listings, 2026-11-01; guides, not quotes):
- pitot-static drone probe about $5–20; Dwyer 160 about $130–200;
- SDP810 about €21–26 or $41 per unit; SDP31 about €20–30 bare;
- FPV airspeed kits $29–92;
- 6-inch Cloudline $90–120.
- From Weakly2024 (2024): TAL220 $9.50, SparkFun HX711 $10.95.
- Typical, not checked: generic HX711 $2–5, BME280 breakout $5–15, USB A-to-B cable $5–10.

### Part 2

No measurements. Calculated estimates only; status: estimate, not a result. Assumptions: ρ = 1.20 kg/m³,
μ = 1.81×10⁻⁵ Pa·s, C_D = 0.47, sphere d = 0.2 h (3.1 % blockage), contraction ratio 6.25, open exit. Section rules
and full tables: [PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#tunnel-length-budget).

**Tunnel length by section, not counting the fan** (as told to the owner before the blower was chosen; the
wide-angle diffuser assumes a fan outlet of half the chamber width): 100 mm → about 0.86–1.03 m; 150 mm → 1.29–1.55 m;
200 mm → 1.72–2.07 m. About 8.6–10.3 h at CR 6.25, and about 9.8–11.8 h at CR 9. An exit diffuser (5°, area ratio
2.5) adds about 7.5 h.

**Blower with a 6-inch fan** (outlet 152 mm, body about 320 mm from S6 listings):

| h (mm) | Fan outlet to exit (mm) | With fan (m) | Drag at 10 / 15 m/s (gf) | 6-inch fan top speed (70 % of 402 CFM) |
|---|---|---|---|---|
| 80 | 625–729 | 0.95–1.05 | 0.58 / 1.31 | about 20.8 m/s (least reliable) |
| 100 | 827–983 | 1.15–1.30 | 0.90 / 2.03 | about 13.3 m/s |
| 120 | 1029–1236 | 1.35–1.56 | 1.30 / 2.93 | about 9.2 m/s |
| 150 | 1332–1616 | 1.65–1.94 | 2.03 / 4.58 | about 5.9 m/s |

**Size comparison** (8-inch fan outlet for 150 mm, 10-inch for 200 mm; fan bodies not included): 150 mm → tunnel
1271–1521 mm, about 1000 CFM rated for 15 m/s; 200 mm → 1714–2059 mm, about 1800 CFM rated; 100 mm → about 450 CFM.
Shaft power at 15 m/s from the existing fan table (open exit, efficiency 0.8): about 30 / 70 / 130 W. Given to the
owner as totals of about 1.15–1.3 / 1.6–1.9 / 2.0–2.5 m; the 150 and 200 mm fan lengths were guesses.

**Fan requirement and top-speed estimates for h = 100 mm:** about 210 CFM delivered against 75–90 Pa at 10 m/s, and
about 320 CFM against 170–200 Pa at 15 m/s (fan pressure 1.25–1.5 q). With a straight-line fan curve between the
listed maximum pressure and the free-air flow: AC Infinity S6 13.1–13.7 m/s; one Delta PFR1212UHE 8.5–8.7 m/s; two
in parallel 12.1–12.8 m/s. Real fan curves sag, so real speeds are lower. The S6 result agrees with part 1's 70 %
method (13.3 m/s).

**Sting** (as told to the owner): a 6 mm aluminium rod carrying a 40 g sphere, ignoring the load cell's flex,
vibrates at about 90 Hz if 100 mm long and about 30 Hz if 200 mm long. For h = 100 mm the sting is about 80–90 mm
long. A 20 mm sphere sheds vortices at about 0.2 V/d: about 100 Hz at 10 m/s and 150 Hz at 15 m/s.

**Listed specs and prices seen** (retailer and distributor pages, 2026-11-01; guides, not quotes):
- AC Infinity Cloudline S6: 7.9 × 12.6 × 8.4 in, 402 CFM;
- VIVOSUN AeroZesh S6: 405 CFM, about 35 W, mixed-flow EC with a PWM-controlled motor, from $62.99 (Walmart); no
  static pressure published;
- VIVOSUN 6-inch booster fans: 275–345 CFM, $31.99–38.99; no static pressure;
- Delta PFR1212UHE-SP00: 228.6 CFM, 1.206 inH₂O (300.4 Pa), PWM and tachometer; 12 V, 2.70 A, 32.4 W, 6600 RPM and
  65.5 dBA from the datasheet row for the -R00/-F00 variants (not stated for -SP00); price not found, and the sibling
  PFR1212DHE-SP00 is $30.90 at Avnet;
- typical, from memory and not checked: 20×4 I²C LCD $8–12, 128×64 graphic LCD $10–20, 1.3" OLED $5–10, rotary
  encoder module $1–3.

## 7. Tests, calibration checks and validation

| Check | Outcome |
|---|---|
| `/catchup`: `python scripts/check_docs.py` | 0 failures, 0 warnings |
| `/catchup`: `python -m unittest discover -s tests` | 20 tests, all passed |
| `/wrap`: `python scripts/sync_status.py --fetch` | `UP_TO_DATE` at `9b42a07`; 0 uncommitted paths before this wrap's edits |
| `/wrap`: `git show --stat 9b42a07` | 10 files, the same list and message as the previous log's §13 |
| `/wrap`: `python -m unittest discover -s tests -v` | 20 tests, all passed (no code changed) |
| `/wrap`: `python scripts/check_docs.py` (final, after this log) | 0 failures, 0 warnings: 5 session logs each indexed once, 196 links and anchors resolve, 47 committable files, none over 25 MiB, no secrets. `git status --short`: 8 paths (7 modified, 1 new), matching the §13 `git add` list |
| Estimates | Recomputed by the scratch script; they match the figures given to the owner in chat |
| Kit transcription | Read from the owner's scanned packing list (one page); quantities are the packed ones |
| Not checked | The FPV kit's actual chip (label unreadable); SDP810 and MS4525DO specs against the makers' own datasheets (only distributor and search summaries); any fan curve; whether the owner's board really is a Mega 2560 R3 |
| Calibration or equipment checks | **None performed.** The board has not been powered |
| Part 2: `python scripts/check_docs.py` after moving the sketch | 0 failures, 0 warnings (199 links) |
| Second `/wrap`: `python scripts/sync_status.py --fetch` | `UP_TO_DATE` at `748dae9` (owner pushed part 1); 3 uncommitted paths before this wrap's edits (README.md, the two sketch files) |
| Second `/wrap`: `git log --format=%h -1 -- docs/sessions/2026-11-01-parts-review-and-kit-inventory.md` | `748dae9`, backfilled into this log's Commit field and the index |
| Second `/wrap`: `python -m unittest discover -s tests -v` | 20 tests, all passed (no code changed) |
| Second `/wrap`: `python scripts/check_docs.py` (final, after this log) | 0 failures, 0 warnings: 5 session logs each indexed once, 248 links and anchors resolve, 49 committable files, none over 25 MiB, no secrets. `git status --short`: 8 modified paths and the new `docs/sketches/` folder (2 files), matching the §13 `git add` list |
| Part 2 estimates | Recomputed by the scratch scripts; they match the figures given to the owner, except one rounding: the 200 mm shaft power was given as about 130 W, which the existing fan table supports (38 W at 10 m/s × 1.5³ = 128 W) |
| Earlier answers quoted in this log | The sting and tunnel-length answers were read back from the session transcript, not reconstructed from memory |
| Not checked | The AeroZesh S6's static pressure and Arduino-control port; the Delta fan's -SP00 current and price; any fan curve; the menu hardware prices; the sketch PDF's legibility after any compression (none done) |

## 8. Errors, failed approaches and troubleshooting

- **The owner's `git commit` committed nothing.**
  - Cause: no files were staged (`git status` showed all 10 paths unstaged or untracked).
  - Fix: run the `git add` lines first. `git commit -a` would also have missed the 3 new files.
  - The owner then committed `9b42a07`. Recorded as a lesson in PROJECT_BACKGROUND.md.
- **WebFetch of the Amazon product page returned only the title.** The page is 1,286,527 characters, and the
  fetch read the first 100,000. Specs came from other retailers' listings, which disagree on one fan vs two. Recorded
  as a lesson.
- **The FPV kit's chip could not be read** from a crop of the owner's screenshot (too low resolution). It is
  identified as an MS4525DO by inference (PX4 digital airspeed kits, dual-side-port package), not by its label.
- **TI has no LM7805 product page** (HTTP 404). The kit's LM7805CT is listed under onsemi (formerly Fairchild) and is
  obsolete; the resources entry points to the DigiKey listing instead.
- **Pressure-sensor prices are patchy:** mixed currencies, zero stock at several distributors, and a retired SparkFun
  breakout. The figures are guides only.

**Part 2:**
- **The agent misread the owner's sketch** as two swappable test chambers; it shows one chamber drawn twice with
  different models. The owner corrected it.
- **The size recommendation changed twice.** The agent recommended 100 mm for the 1 m target, then 150 mm (or 200 mm)
  once the owner allowed more length. The owner chose 100 mm. Both recommendations and the reasons are in §2.
- **No static pressure found for the VIVOSUN AeroZesh S6**, and no price for the Delta PFR1212UHE-SP00 (only for
  a sibling model). Both are recorded as unknown.
- **A bash heredoc holding a Python edit script failed to parse** (bash: "unexpected EOF while looking for
  matching" quote).
  The script was written to a scratch file and run from there instead.
- **`python -I` ignores `PYTHONIOENCODING`**, so printing the transcript failed with a cp1252 UnicodeEncodeError on
  "→". Fixed with `sys.stdout.reconfigure(encoding="utf-8")` in the script.

## 9. Decisions and reasoning

No DECISIONS.md entry. The Mega is untested and not yet confirmed by its markings, and the fan, panels and interface
board are proposals. Recorded as proposals or recommendations:

- **Pressure sensing:** buy the pitot-static probe separately and an SDP810 (range after the top speed). Drone kits
  with the MS4525DO are ruled out because ±1 psi is about 29× our largest q.
- **Fan type:** an inline mixed-flow duct fan. PC and box fans cannot push through the screens and honeycomb, and a
  centrifugal blower is loud, bulky and often has few speeds. Choose its size with the top speed.
- **Measurement electronics:** digital modules and no op-amps in the measurement chain; the owner's circuit work goes
  into the interface PCB.
- **Model access:** magnetic removable acrylic panels (owner's idea). Magnets clamp and pins locate, and the sting is
  non-magnetic.
- **Visualization generator:** an ultrasonic mist maker first, when the time comes (still deferred).
- **Microcontroller:** the owner's Mega 2560 R3 is the candidate. It becomes a D-entry after the Blink test.

**Part 2** (owner decisions, recorded in DECISIONS.md):
- **[D-007](../../DECISIONS.md): open-circuit blower, fan at the front** (owner). Open exit with no exit diffuser:
  the agent's proposal, Tentative.
- **[D-008](../../DECISIONS.md): 100 mm × 100 mm test section** (owner). Contraction ratio 6.25 and the section
  lengths are Tentative.
- **D-005** stays Accepted for segmented printing; its status line now says the "decently big" intent is superseded
  by D-008.

Owner choices recorded without a D-entry (design concepts, not yet engineering decisions):
- one test chamber with a removable top and/or side panel;
- an Ender 3–style knob menu;
- preset airfoil angles instead of a servo.

Agent proposals (not decided):
- the balance box holds only the load cell and HX711;
- a sting lock and overload stops;
- a 20×4 LCD and an encoder;
- a 6-inch mixed-flow EC fan;
- spheres of about 20 and 25 mm.

## 10. Open questions and blockers

- **Owner inputs needed for sizing** (unchanged, now the main blocker): bench or floor length, target top speed, any
  fan in mind. They decide the fan size and the pressure-sensor range.
- **Board:** confirm its markings, then the Blink test once the cable arrives.
- **Still unknown on hand:**
  - a multimeter, soldering iron or bench supply (asked, not answered);
  - the other electronics the owner thinks they have;
  - the magnets' type and size.
- **Owner question:** should `PartsListECE2010.pdf` be filed in the repo as evidence for the kit inventory? Where to
  put it is not decided. It is not a reference paper, so probably not `resources/`.
- D-003, D-004 and D-006 are still Tentative.
- **Carried over:** the C_D reference (Morrison2013, Roos1971), the blockage details, and the airspeed-reference
  placement (open question 10).

**Part 2, status at the second wrap:**
- **Answered:** the tunnel type (D-007), the test-section size (D-008), the length target (about 1 m, more allowed),
  and the tools on hand (multimeter, soldering station, bench supply, workbench).
- **Still needed from the owner:**
  - the target top speed;
  - the fan choice; for the AeroZesh S6, its static pressure; for the Delta pair, the bench supply's maximum voltage
    and current;
  - whether to compress the sketch PDF before committing it;
  - confirmation of D-007's open exit;
  - the magnets' type and size, and any other electronics;
  - whether to file `PartsListECE2010.pdf` (asked in part 1, not answered).
- **Open design questions** (PROJECT_STATUS 11–12): fan speed control from the menu; the model attachment, sting lock
  and overload stops.

## 11. Remaining tasks

See TODO.md:

- **P0 (owner):**
  - commit and push this session;
  - sizing inputs;
  - board setup (cable, markings, Blink);
  - the rest of the parts-on-hand list;
  - confirm D-003, D-004 and D-006.
- **P1:**
  - review Morrison2013 and Roos1971;
  - the owner's optional reading;
  - size the tunnel, including the access panels;
  - datasheets;
  - choose the fan, pressure sensor, load cell and ambient sensor; confirm the microcontroller.
- **P2:** the new interface-board task; the mist-generator options; the rest unchanged.

**After part 2** (see TODO.md):
- **P0 (owner):**
  - the sketch-size decision, then commit and push;
  - the top speed;
  - the fan choice;
  - board setup;
  - the bench supply's rating, the magnets and other electronics;
  - confirm D-003, D-004, D-006 and D-007's open exit.
- **P1:**
  - Morrison2013 and Roos1971, then Mehta1977 and Scheiman1981;
  - detail the 100 mm layout, including the balance box, the sting lock and overload stops;
  - check the fan choice;
  - the sphere sizes (20 and 25 mm proposed);
  - the load cell with overload rating.
- **P2:** a new firmware-and-menu task; the interface board now carries the display and encoder headers.
- **P3:** airfoil tests at preset angles.

## 12. Recommended first task for the next agent

(Updated at the second wrap; part 1's version is in `748dae9`.)

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed part 2's commit; the next `/wrap` backfills its hash
here and in the index (this log's Commit field then lists `748dae9` and the new hash).

- **If the owner has chosen a fan or given the top speed,** record them, check the fan against the
  [length budget](../../PROJECT_BACKGROUND.md#tunnel-length-budget) (TODO P1 fan task), and choose the
  pressure-sensor range.
- **If the owner reports the Blink test,** record the board as working and write the microcontroller D-entry.
- **If the owner asks for a smaller sketch PDF,** make a compressed copy (PyMuPDF is on the owner's PC) and check it
  is still legible before replacing the original. Only do this if the owner asks.
- **Otherwise,** review **Morrison2013 and Roos1971** and write a notes file for each.
  - Extract the C_D value(s) at Re of about 10⁴ (a 20 mm sphere at 10–15 m/s is about 1.3–2.0×10⁴), with the figure
    or table each comes from.
  - Morrison2013 is a correlation: check it against Roos1971's measurements.
  - Read the numbers from page images, not text layers.
  - Then Mehta1977 and Scheiman1981, which the 100 mm layout's diffuser and screens need.

## 13. Manual Git commands (as given to the owner)

### First wrap (part 1; the owner committed and pushed these as `748dae9`)

State at this wrap: `UP_TO_DATE` at `9b42a07`. Nothing is staged or committed. Eight files changed: 7 modified, 1 new
(this log).

Run in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add PROJECT_STATUS.md TODO.md PROJECT_BACKGROUND.md docs/experimental_setup.md resources/README.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md docs/sessions/2026-11-01-parts-review-and-kit-inventory.md
git status
git diff --cached --stat
git diff --cached
git commit -m "Record parts review, ECE kit inventory and Mega 2560 board" -m "Lists the ECE2010 kit from its packing list and the owner's Elegoo Mega 2560 R3, assesses the FPV pitot kit and the 120 mm fan the owner found (both unsuitable), and proposes an inline duct fan, SDP810 pressure-sensor candidates, part criteria with prices, magnetic removable acrylic panels and the interface-board plan. Backfills 9b42a07."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Stage before committing.** `git commit` on its own commits nothing: the `git add` lines must run first.
- **Staging:** after the `git add` lines, `git status` should show 8 files under "Changes to be committed" and
  nothing left unstaged.
- **After `git diff --cached`**, press `q` to leave the pager.
- **Pushing:** `git push origin HEAD`. The last command should end with `STATE: UP_TO_DATE`.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"), GitHub has commits you do not. Do not
  force-push. Run `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then
  `git push origin HEAD`.

### Second wrap (part 2)

State at this wrap: `UP_TO_DATE` at `748dae9`. Nothing is staged or committed. Ten files changed: 8 modified, 2 new
(`docs/sketches/README.md` and the sketch PDF).

**First decide about the sketch PDF** (10.2 MiB). To shrink it, replace the file at the same path and name before
running the commands. Otherwise commit it as is: it is under the 25 MB limit, but it stays in Git history for good.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add DECISIONS.md PROJECT_STATUS.md TODO.md PROJECT_BACKGROUND.md README.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-01-parts-review-and-kit-inventory.md
git add docs/sketches/README.md docs/sketches/2026-11-01_tunnel-concept-sketch-1.pdf
git status
git diff --cached --stat
git commit -m "Record blower layout, 100 mm test section and fan candidates" -m "Adds the owner's decisions D-007 (blower, fan at the front) and D-008 (100 mm test section) with the tunnel length budget and fan candidates for that size. Records the single test chamber with removable panels, the Ender 3-style knob menu, preset airfoil angles and the tools on hand, and files the owner's first sketch in docs/sketches/. Backfills 748dae9."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** after the `git add` lines, `git status` should show 10 files under "Changes to be committed" and
  nothing left unstaged.
- **Inspecting:** `git diff --cached` shows the full staged diff; press `q` to leave the pager. The PDF shows only as
  a binary file.
- **Pushing:** `git push origin HEAD`. The last command should end with `STATE: UP_TO_DATE`.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
