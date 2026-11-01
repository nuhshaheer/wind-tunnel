# 2026-11-01: Parts review and kit inventory

- **Session ID:** edc44a90-0a86-45f3-8527-50425c926745 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

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

## 4. Experimental procedures performed

None. No physical work this session; no hardware has been tested.

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

## 12. Recommended first task for the next agent

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed this session's commit; the next `/wrap` backfills its
hash here and in the index.

- **If the owner has given the sizing inputs,** start build step 1 (TODO P1). Size the fan (6-inch vs 8-inch inline)
  and choose the pressure-sensor range from the top speed.
- **If the owner reports the Blink test,** record the board as working and write the microcontroller D-entry.
- **Otherwise,** review **Morrison2013 and Roos1971** and write a notes file for each.
  - Extract the C_D value(s) at Re of about 10⁴–10⁵, with the figure or table each comes from.
  - Morrison2013 is a correlation: check it against Roos1971's measurements.
  - Read the numbers from page images, not text layers.

## 13. Manual Git commands (as given to the owner)

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
