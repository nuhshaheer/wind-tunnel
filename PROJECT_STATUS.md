# Project Status

**Last updated:** 2026-11-09
**Last commit:** `0558370` (2026-11-09, the shopping-list session's follow-up), pushed to `origin/main` (`UP_TO_DATE`
on 2026-11-09).
- The repo is https://github.com/nuhshaheer/wind-tunnel (account renamed from `nuhshaheer-2007` on 2026-11-02; the old
  URL redirects).
- **Not committed yet:** the drawing-package session: the owner's 2026-11-09 sketch, a preliminary drawing package in
  `docs/drawings/`, and D-013 to D-015 ([session log](docs/sessions/2026-11-09-drawing-package.md), with the commit
  commands in §13).

**Current stage:** Planning / pre-build. The layout is decided and **a full buy list exists
([docs/buy_list.md](docs/buy_list.md), about $315–505 before tax and shipping). Nothing has been ordered.** The owner
tracks orders in [docs/shopping_list.md](docs/shopping_list.md) (2026-11-09): only what is still to buy, about
$255–360 plus the fan. **A preliminary drawing package** of the whole tunnel (10 sheets, parts list, TBD register;
pre-sizing, not for manufacture) is in [docs/drawings/](docs/drawings/README.md) (2026-11-09).
- Decided:
  - segmented 3D printing (D-005);
  - an open-circuit blower with the fan at the front (D-007);
  - a 100 mm × 100 mm test section (D-008);
  - the sphere-validation reference: Brown and Lawler (2003) Eq. (19) at each run's Re, ±10 %, plus a trend check
    (D-009);
  - **a 13 m/s target top speed, validation runs from about 6.5 m/s (D-010, 2026-11-08).** Not a must-have: 11–12 m/s
    still validates, with less force;
  - **no on-tunnel display or knob; all output on the laptop (D-012, 2026-11-08);**
  - **bolted flange joints (D-013); the top panel lifting off on magnets, with replaceable floor inserts under the
    model (D-014); a printed sting mount with the owner's thumb-screw sting lock (D-015)** (owner, 2026-11-09).
- **Open: the fan (D-011, Tentative since 2026-11-09).** The owner will choose on budget between the AC Infinity
  CLOUDLINE S6 ($99; about 13.0–13.4 m/s, estimate) and the VEVOR VV-GDFJ-AC6 ($53.90; about 11.3 m/s).
- Parts chosen in the buy list (owner, 2026-11-08/09):
  - one Sensirion SDP810-125Pa with a home-made brass total-pressure probe and wall taps;
  - two TAL221 100 g load cells, a SparkFun HX711 board and an Adafruit BME280;
  - 3/4 in and 1 in Delrin balls;
  - aluminium window screen and a printed honeycomb.
- Sixteen references reviewed:
  - tunnel design: Abdelhamed2014, Bell1988, Mehta1979, Mehta1977;
  - flow conditioning: Scheiman1981, Wieghardt1953;
  - blockage: Maskell1963, Cooper1998;
  - sphere C_D: Morrison2013, Roos1971, Brown2003;
  - the balance paper Weakly2024;
  - datasheets and notes: HX711, **SDP8xx, TAL221, and Sensirion2024**, an app note on correcting the SDP810 for
    ambient pressure (2026-11-08).

  Five more are filed in `resources/` but not yet read.
- On hand:
  - the ECE kit (from its packing list) and the Elegoo Mega 2560 (**working**: Blink upload Verified 2026-11-02, §3);
  - 43 magnets (8 × 2 mm);
  - tools: a multimeter, a soldering station, a bench power supply, 6 in digital calipers (battery may be dead), a
    hand drill and a spirit level;
  - for printing: PLA and PETG-CF (amounts unknown) and a hardened-steel nozzle;
  - access to a school lab balance.
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
| On-tunnel display with a knob and menu, like the Ender 3's | **Dropped (owner, 2026-11-08; [D-012](DECISIONS.md)):** "this isnt a device", so all output goes to the laptop. Planned 2026-11-01 |
| Airfoil tests at set angles of attack | Planned (after validation). Owner, 2026-11-01: **preset angles** instead of the 2026-10-31 dial-and-servo idea, because a pivot would ruin the force measurement ([TODO.md](TODO.md) P3) |
| Flow visualization with a water-mist generator | Planned, optional, **last** (owner, 2026-10-31). Only a capped injection port and a test-section window are planned now ([TODO.md](TODO.md) P2) |
| Model-car downforce with a second, vertical load cell | Tentative: the owner's idea (2026-11-02, "just an idea"), after validation. The same vertical cell would measure airfoil lift ([TODO.md](TODO.md) P3). **2026-11-09:** lift may never be measured. If not, the owner will plug the sting hole, set a model car on the floor and study it with mist only (no force measurement) |

## 2. Wind tunnel configuration

**Nothing built. Tunnel type, test-section size and target top speed are decided; the fan is not.** Details and
unknowns are in [docs/experimental_setup.md](docs/experimental_setup.md). The owner's sketches are in
[docs/sketches/](docs/sketches/README.md); a preliminary drawing package (pre-sizing, layout values for every TBD) is
in [docs/drawings/](docs/drawings/README.md).

| Item | State | Source |
|---|---|---|
| Construction | 3D-printed segments on the owner's Bambu Lab P1S, with alignment holes. Still segmented at 100 mm: the 250 mm settling chamber leaves no room for walls on the 256 mm bed. **Joints, Accepted 2026-11-09 (owner's sketch, [D-013](DECISIONS.md)):** bolted flanges, M3 screws into brass heat-set inserts, foam tape between the faces, screens clamped between the flanges in printed frames, so they can come out; sizes TBD. Proposed: PLA shells (black for the contraction and test section) and PETG-CF for clamped or loaded parts; **printed feet under each section instead of a plywood base (owner)** | [D-005](DECISIONS.md) (Accepted), [D-013](DECISIONS.md), [buy list](docs/buy_list.md) §2 |
| Tunnel type | **Accepted (owner, 2026-11-01): open-circuit blower, fan at the front.** Proposed order: fan → flexible coupling → wide-angle diffuser with screens → settling chamber → contraction → test section → **open exit** (no exit diffuser; Tentative) | [D-007](DECISIONS.md) |
| Test section size | **Accepted (owner, 2026-11-01): 100 mm × 100 mm.** Proposed length 270–290 mm. Estimated total length 1.15–1.3 m with a 6-inch fan (owner's first target was about 1 m; more is allowed) | [D-008](DECISIONS.md), [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget) |
| Fan type | A 6-inch inline duct fan with its own speed controller, on its own stand. **Model open (D-011, Tentative): AC Infinity CLOUDLINE S6 or VEVOR VV-GDFJ-AC6** (§3). Fan-to-tunnel joint (owner's design, 2026-11-08): the fan collar, wrapped in one layer of neoprene, slides snugly into a printed inlet sized from the measured collar; duct tape seals it | [D-011](DECISIONS.md), [buy list](docs/buy_list.md) §1 |
| Fan-to-chamber diffuser | Proposed (2026-11-02): area ratio 3.44 (152 mm round → 250 mm square), so the screens need K_sum ≥ 2.1. **Two screens (K ≈ 1.1–1.5 each) allow about 150–200 mm**; the minimum is about 115 mm with two screens, 195 mm with one and 335 mm with none. Below about 220 mm use curved walls or radiused inlet and outlet corners. Fillet the corners. **No flow straightener at the fan outlet**: the fan's swirl helps keep the diffuser attached. **2026-11-09:** with aluminium window screen (K about 0.75–0.85 at the fan outlet), plan **three** diffuser screens if the delivered wire is 0.010 in; the first screen at the fan outlet costs about 24–28 Pa at 13 m/s, so consider placing it slightly into the diffuser | [Mehta1977](resources/notes/Mehta1977.md) (Figs. 5 and 7, §6.1; owner-checked), [buy list](docs/buy_list.md) §3 |
| Contraction | Proposed: contraction ratio 6.25 (250 mm → 100 mm square), 5th-order-polynomial wall, about 250 mm long (1.0 × inlet) | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md), [Mehta1979](resources/notes/Mehta1979.md) |
| Settling chamber | Proposed: 250 mm square. A honeycomb (cell length 7–10 diameters, cells of about 2–3 mm, thin walls), then one or two screens at least 58 % open, then about 50 mm (0.2 D) to the contraction. Add a capped port after the last screen for optional mist injection. **Length 150–200 mm** with Mehta1979's 0.2 D spacing; **about 230–300 mm** if spaced for full turbulence decay: at least 500 wire diameters between screens (about 75–125 mm) and about 50 cell diameters from the honeycomb to the first screen (2026-11-02). Decide at sizing. **2026-11-09:** two settling-chamber screens (four or five screens in all, per Mehta1977/1979); a **printed honeycomb** (owner; for example 6 mm hexagons, 0.4 mm walls, about 50 mm long), with straws as the upgrade; wall pressure taps (S) for the airspeed reference. **Found while drawing (2026-11-09; open question 15):** with the chosen window screen and 6 mm cells, full-decay spacing gives about 380–390 mm plus frames, not 230–300 mm (our arithmetic) | [Mehta1979](resources/notes/Mehta1979.md), [Mehta1977](resources/notes/Mehta1977.md), [Scheiman1981](resources/notes/Scheiman1981.md) |
| Test section | Proposed: **closed** section with clear panels. Sphere at least about 0.5 D downstream of the contraction exit; sphere blockage about 3 % (at most 5 %); reference pressure reading at least 1.5√C upstream of the sphere; sphere at least 4√S from the test-section end. Together 2.7–2.9 h, i.e. 270–290 mm (estimate). **2026-11-08:** wall pressure taps at the entrance (E) and at the model station (M); a printed probe guide; a streamlined **sting shield** about 7.5 mm wide (5 mm hole for the 1/8 in sting) up to about 5 mm below the ball, because a bare sting would have about 115 % of the ball's drag. **2026-11-09 ([D-014](DECISIONS.md)):** the shield is fixed to a replaceable floor insert under the model | [Mehta1979](resources/notes/Mehta1979.md), [Cooper1998](resources/notes/Cooper1998.md), [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed) |
| Model access | **Accepted 2026-11-09 ([D-014](DECISIONS.md), owner): the top clear acrylic panel lifts off, held by magnets** (design later); whether a side panel also comes off is open. **The floor under the model is a replaceable insert:** a sphere insert carrying the sting hole and the shield, and a plain insert for model cars (replaces the floor plug). Agent's design points (Proposed): pins or lips locate each panel and insert; inner faces flush with the walls (the insert's front edge is just upstream of the ball); a foam gasket seals each panel; the pitot goes through a fixed wall; **no magnets near ferrous parts on the measured side of the balance**, and a non-magnetic sting. Owner's concept since 2026-11-01; the owner's 43 magnets (8 × 2 mm) suffice; 1/8 in acrylic | [D-014](DECISIONS.md), [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md), [buy list](docs/buy_list.md) §4 |
| Balance and controls layout | Proposed (2026-11-01): only the load cell and HX711 in a closed box under the floor (the sketch's "electronics house"). The Arduino in a separate box on a cable (no display or knob since D-012). **2026-11-09 ([D-015](DECISIONS.md), owner):** a printed sting mount screwed to the cell's top end; the owner's sting lock, a hand screw from the side, clamps the sting in the mount without glue; the sting is lifted out to change balls; overload stops at about 120 g; no separate hold-still pin. Optional (2026-11-02): leave room for a second, vertical load cell for airfoil lift or model-car downforce (P3). **2026-11-08:** the cell stands upright directly under the ball, the sting clamped only to its top end, its screw holes along the wind ([owner's sketch](docs/sketches/README.md)); the balance is a removable module so it can be laid on its side for calibration; each ball has its own 1/8 in stem that slides into a 5/32 in sleeve at the top of the sting (press-fit into the ball: Delrin cannot be glued) | [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#measurement-and-analysis-approach-proposed) |

## 3. Hardware and instrumentation

Parts on hand are recorded from the owner's statements and the ECE kit's packing list (2026-11-01). The full kit list
is in [docs/experimental_setup.md](docs/experimental_setup.md#parts-on-hand). Prices below were seen on retailer
listings on 2026-11-01 unless marked otherwise; they are guides, not quotes.

| Item | Availability | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | On hand (owner has access, stated 2026-10-30) | Build volume 256 × 256 × 256 mm (manufacturer spec). **2026-11-09 (owner):** PLA and PETG-CF on hand (amounts unknown) and a hardened-steel nozzle, so PETG-CF can be printed |
| ECE2010 lab kit (WPI) | On hand, per its packing list (owner, 2026-11-01). Quantities are the packed ones, not counted | Includes LM741, LM348 and LMC6484 op-amps, LM311, 555, LM317T and LM7805CT regulators, transistors, MOSFETs, potentiometers (1 × 10 kΩ, 2 × 1 kΩ, 1 × 100 kΩ, 1 × 1 MΩ), resistors, capacitors, breadboard and jumper wires. No multimeter, soldering iron or power supply in the list (the owner has them separately) |
| Tools | On hand (owner): multimeter, soldering station, bench power supply, access to a workbench (2026-11-01); **6 in (150 mm) digital calipers** (battery thought dead; LR44/SR44 size), a **hand drill** and a **spirit level** (2026-11-08); access to a **school lab balance** (2026-11-08) | Models unknown. The bench supply's maximum voltage and current are unknown; they matter only if a 12 V DC fan is chosen. Tools still to buy (tube cutter, drill bits, etc.): [buy list](docs/buy_list.md) §10 |
| Other electronics | Unknown | The owner thinks more is on hand (2026-11-01); not listed yet |
| Microcontroller | **On hand, working: Elegoo Mega 2560.** Blink upload **Verified** 2026-11-02 (owner's test) | Evidence, 2026-11-02:<br>• The owner read ATMEGA2560 on the main chip. Whether the board itself is marked "R3" is not yet recorded.<br>• Windows listed it on COM3 with USB ID 2341:0042, which the Arduino AVR core (1.8.8, `boards.txt`) lists under "Arduino Mega or Mega 2560". USB serial number `13448474939351C0E828` identifies this board.<br>• The owner uploaded Blink with both delays changed from 1000 to 200 ms (Arduino IDE 2.3.10, board "Arduino Mega or Mega 2560", processor ATmega2560), and the "L" LED blinked faster. A faster blink proves the upload, because a blinking LED alone could be a factory-loaded sketch.<br>From the Mega 2560 Rev3 documentation (retailer pages; not checked on this board): 5 V logic; I²C on pins 20 (SDA) and 21 (SCL), also brought out next to AREF on R3 boards; ATmega16U2 USB-serial. Covers every planned sensor (no display or knob since D-012) |
| USB A-to-B cable for the board | On hand, carries data: the board enumerated on COM3 through it (2026-11-02) | The board's original cable was lost. The owner was ordering a UGREEN 5 ft cable (2026-11-01); which cable was used on 2026-11-02 is not recorded |
| Blower / fan | To buy; **open between two (D-011, Tentative since 2026-11-09); the owner will choose on budget** | • **AC Infinity CLOUDLINE S6, model AI-CLS6**: $99.00; maker's page (read 2026-11-08): 425 CFM, 503 Pa, PWM-controlled EC motor, 10 speed levels, 32.0 cm long. Retailers list 402 CFM. About 13.0–13.4 m/s with five window screens (straight-line estimate; 12.3–12.7 at 90 % of the curve).<br>• **VEVOR 6-inch inline duct fan, model VV-GDFJ-AC6**: $53.90 (owner, 2026-11-09); seller's figures 400 CFM, 300 Pa, AC motor with a speed controller, 60 W. About 11.3 m/s (10.8). Its "34 dB" claim is unlikely, so its 300 Pa may be optimistic.<br>Both validate; the VEVOR gives about 73 % of the S6's force at top speed. Earlier candidates and the unsuitable fans: [2026-11-07 log](docs/sessions/2026-11-07-top-speed-and-fan-search.md). Estimates: [buy list](docs/buy_list.md) §1 |
| Fan-to-tunnel joint | Owner's design (2026-11-08) | The fan's collar, wrapped in one layer of 1/16 in 40A neoprene (to buy, $13.78 a pair), slides snugly into a printed inlet sized from the measured collar (paper strip ÷ π); duct tape seals it. The fan stands on its own feet and never touches the print. [Buy list](docs/buy_list.md) §1 |
| Honeycomb + screens | Screens to buy; honeycomb printed | **Screens (proposed 2026-11-09): aluminium window insect screen, "bright aluminum", 18 × 16 mesh**, wire about 0.010–0.011 in, 66–69 % open; about $9.50 a 36 × 84 in roll (Home Depot). Four or five screens (two or three in the diffuser, two in the settling chamber; Mehta1977/1979, Scheiman1981). Rejected: McMaster 30 × 30 filter mesh (0.012–0.013 in wire, 37–41 % open: about 11.8 m/s top speed and patchy flow), Online Metals 24 × 24 × 0.014 in (44 %), McNichols perforated sheet, a TWP quote of about $200, Zoro's $65.59 sheet (too expensive). **Honeycomb: printed (owner, 2026-11-08)**, for example 6 mm hexagons with 0.4 mm walls, about 50 mm long; straws as the upgrade. Details: [buy list](docs/buy_list.md) §3 |
| Pitot tube | **Made in-house (owner, 2026-11-08)** | A 1/8 in brass total-pressure tube facing upstream, with wall static taps (four per station) at three stations: S (settling chamber), E (test-section entrance), M (model station). Probe − M gives q at the model position (flow map, calibration); S − E gives the airspeed during force runs, calibrated once against the probe (open question 10). Brass tube, 1/8 in silicone tubing and barbed tees to buy ([buy list](docs/buy_list.md) §5). The Dwyer 166-6 ($140–167) was not chosen |
| Differential pressure sensor | To buy: **one Sensirion SDP810-125Pa** (owner chose one, 2026-11-08), $29–35 (DigiKey 1649-1073-ND, Mouser 403-SDP810-125PA) | Datasheet reviewed 2026-11-08 ([notes](resources/notes/SDP8xx.md)): 0.08 Pa + 3 % of reading; 2.7–5.5 V; I²C address 0x25 on every 125 Pa part (a second sensor would need a multiplexer); four solder pins at 2 mm pitch; Ø3.5/5.2 mm barbs. **Every reading must be multiplied by 966 mbar / p_amb** (×0.95 at sea level; [Sensirion2024 notes](resources/notes/Sensirion2024.md)). Tubes are swapped between probe/M and S/E at two couplers on short pigtails |
| Load cell + HX711 | To buy: **two TAL221 100 g** (SparkFun SEN-14727, about $16 each; one spare/possible lift cell; owner, 2026-11-08) and **one SparkFun HX711** (SEN-13879, $11.50) | Datasheet reviewed 2026-11-08 ([notes](resources/notes/TAL221.md)): 0.6 ± 0.15 mV/V, safe overload 150 % (150 g), errors ±0.05 % FS each, zero tempco ±0.1 % FS/10 °C. At gram loads the %FS figures are unspecified, so build step 5 must measure them. Drag 0.30–1.27 gf (3/4 in ball) and 0.54–2.31 gf (1 in) at 6.5–13 m/s (estimate) |
| Ambient pressure / temperature sensor | To buy: **Adafruit BME280 (2652)**, $14.95 | Regulator and level shifting for the 5 V Mega. Gives air density and the SDP810's ambient-pressure correction. Check the chip ID (0x60, not a BMP280's 0x58) on arrival |
| Display and knob | **Not needed (D-012, owner, 2026-11-08)** | All output goes to the laptop (the Arduino IDE's Serial Plotter for a live view) |
| Servo (airfoil pitch) | Probably not needed | The owner switched to preset angles of attack (2026-11-01). The 2026-10-31 dial-and-servo idea is kept in [TODO.md](TODO.md) P3 for reference |
| Magnets | **On hand: 43, round, 8 mm × 2 mm** (owner, 2026-11-09; probably neodymium, not confirmed) | Enough for the removable top panel (about 8 per panel; D-014) and a side panel if one is made removable |
| Acrylic sheet | To buy: clear acrylic, 1/8 in (3.2 mm), 12 × 24 in, $10.45 cast (Online Metals) | For the window panels; cut by scoring and snapping |
| Mist or smoke generator (optional visualization) | Not decided; deferred to the end | The owner asked (2026-11-01) for one that makes thick smoke. Options compared in [TODO.md](TODO.md) P2; the agent's first choice is an ultrasonic mist maker |

Budget: no fixed budget (owner, 2026-11-01), but price-conscious. **The full buy list,
[docs/buy_list.md](docs/buy_list.md), totals about $315–505 before tax and shipping** (2026-11-09; the low end
with the VEVOR fan), plus up to about $100 for items that may already be in the house. Nothing has been ordered.
The owner's tracker, [docs/shopping_list.md](docs/shopping_list.md) (2026-11-09), lists what is still to buy with qty,
price, link and status: about $255–360 plus the fan, and up to about $90–150 more for "check house" items if none are
at home (our sums of the listed prices; many are typical prices, not checked).

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | Planned; not started. Since D-012 (2026-11-08): log raw counts over USB to the laptop, which is also the live view (the Arduino IDE's Serial Plotter to start); no display or knob code. SDP810 commands and scale factor are in the [SDP8xx notes](resources/notes/SDP8xx.md) |
| Analysis scripts (`analysis/`) | Planned; not started |
| Drawing package ([docs/drawings/](docs/drawings/README.md)) | Implemented 2026-11-09; a preliminary, pre-sizing design, not checked against anything built. `python docs/drawings/page.py` rebuilds the page (standard library only). Checked: every callout has a parts-list row and every part is drawn (`parts never drawn: []`), and the repo copy rebuilds byte-identical to the published one |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote). States seen live so far, each correct for the situation: `NO_COMMITS_YET`, `UP_TO_DATE`, `FETCH_FAILED`, `AHEAD` (the last two on 2026-10-31, in the owner's terminal) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and clean runs on this repo |
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-05, 2026-11-08, 2026-11-09); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `b710093`, `7db221f`, `9b42a07`, `748dae9`, `8fda08f`, `c04de1b`, `b22a45b`, `36f39eb`, `d7f5cdf`, `0351407`, `b08a151` and `0558370`; `UP_TO_DATE` afterwards). One content error in its first run was corrected by the second ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only, developed with Python 3.13 on Windows 11.
- On 2026-11-02, `python` on the owner's PC was **3.11.0** in both Git Bash and PowerShell. The `py` launcher listed
  3.10, 3.11, 3.12 and 3.14, but no 3.13. The 20 tests pass under 3.11.
- Git 2.54, Git LFS 3.7 (installed, not enabled), GitHub CLI 2.97.
- Arduino IDE 2.3.10 with the Arduino AVR Boards core 1.8.8, installed by the owner on 2026-11-02 (versions read from
  the program file and the core's folder). `arduino-cli` is not installed.
- Agents reading PDFs used `pdftotext` (Git for Windows) and PyMuPDF 1.28.2, which is installed on the owner's PC
  (Python 3.11). Neither is a project dependency. Claude Code's own PDF page rendering needs `pdftoppm` (poppler),
  which is not installed (2026-11-08), so render pages with PyMuPDF instead.

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
  - Committed and pushed as `d7f5cdf`. See [the session log](docs/sessions/2026-11-07-top-speed-and-fan-search.md).
- 2026-11-08/09: the buy list (documentation only; nothing bought or built).
  - Wrote [docs/buy_list.md](docs/buy_list.md) with the owner, section by section: everything the tunnel needs, what
    each part does, prices seen and what is on hand. Total about $315–505.
  - Recorded D-010 (13 m/s target), D-011 (fan: the S6, reopened the next day as S6 or VEVOR) and D-012 (no display
    or knob).
  - Filed and reviewed three documents with notes: the SDP8xx and TAL221 datasheets, and Sensirion's
    signal-compensation note, which shows that SDP810 readings need the ×966 mbar / p_amb correction.
  - Filed the owner's load-cell sketch in `docs/sketches/`.
  - Committed and pushed as `0351407`. See [the session log](docs/sessions/2026-11-09-buy-list.md).
- 2026-11-09: the owner's shopping tracker (documentation only; nothing bought).
  - Wrote [docs/shopping_list.md](docs/shopping_list.md): what is still to buy, with qty, price, link and status,
    grouped by store, and a "check the house first" section. It adds the pin vise for the wall taps, which the buy
    list named but never listed.
  - Corrected stale entries from before D-012 and the buy list (PROJECT_BACKGROUND, TODO, experimental_setup, a
    status note on D-002).
  - Committed and pushed as `b08a151`. After it: how the calibration masses hang (a printed attachment on the sting's
    end with a hook at the ball's centre, the owner's idea, and a light pan on a thread;
    [buy list](docs/buy_list.md) §9), committed and pushed as `0558370`. See
    [the session log](docs/sessions/2026-11-09-shopping-list.md).
- 2026-11-09: the drawing package and the owner's second sketch (documentation only; nothing bought, built or tested).
  - Drew a preliminary engineering drawing package of the whole tunnel from the docs: 10 sheets, a 70-item parts list,
    a TBD register and seven findings ([docs/drawings/](docs/drawings/README.md); pre-sizing, not for manufacture).
  - Filed the owner's sketch of the flanges, the load cell and the test chamber, compressed from 10.2 MB to 0.4 MB.
  - Recorded the owner's decisions: bolted flange joints (D-013), the top panel on magnets and replaceable floor
    inserts (D-014), and the sting mount with a thumb-screw sting lock (D-015).
  - Not committed yet. See [the session log](docs/sessions/2026-11-09-drawing-package.md).

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
- [docs/buy_list.md](docs/buy_list.md) (2026-11-08/09):
  - top speed of each fan with the real screen losses;
  - K and pressure loss of each candidate mesh;
  - sting drag with and without a shield, and load-cell error sizes at gram loads;
  - the inclined-manometer resolution, and straw and filament counts.

  Scripts in the [session log](docs/sessions/2026-11-09-buy-list.md#5-commands-and-scripts-executed).

## 9. Bugs, equipment issues, blockers

- **Blocked:** all physical work waits on buying hardware. Nothing has been ordered (2026-11-09).
  - The buy list is complete ([docs/buy_list.md](docs/buy_list.md)); orders are tracked in
    [docs/shopping_list.md](docs/shopping_list.md).
  - Only the fan waits on a decision: S6 or VEVOR, on the owner's budget (D-011).
  - The electronics (SDP810, two TAL221, HX711, BME280) and most small parts do not depend on the fan or on the
    sizing, and can be ordered now.
  - The owner will check on 2026-11-10 which small items are already in the house (filament amounts, glue, sandpaper,
    screws, rubber feet, duct tape).
  - The microcontroller is no longer a blocker: the board works (2026-11-02, §3).
- Resolved: the owner committed the 10.2 MiB sketch PDF uncompressed in `8fda08f` (under D-004's 25 MB limit). It stays
  in Git history.
- No known software bugs.
- Watch: at the 2026-11-02 `/wrap` the test suite took about 28 minutes (1,662.7 s) instead of the usual 13–16 s, and
  all 20 tests still passed. Cause unknown, not investigated. If it recurs, run the tests with `-v` to see which one
  stalls ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md#8-errors-failed-approaches-and-troubleshooting)).
  It has not recurred since: 20 tests in 7.9–11.3 s at every run from 2026-11-02 to 2026-11-09.
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
   - a check that the chosen pressure sensor and BME280 board work at 5 V on its I²C pins (20/21). On paper both do:
     the SDP810 takes 2.7–5.5 V with I²C up to VDD + 0.3 V (datasheet), and the Adafruit BME280 has level shifting.
     To confirm on the breadboard;
   - minor: whether the board is marked "R3", which tells whether SDA/SCL are also brought out next to AREF.
2. **What is the op-amp signal conditioning for?** Proposed (agent, 2026-11-01): nothing in the measurement chain.
   - The HX711, a digital pressure sensor and the BME280 need no analog conditioning, and commercial digital sensors
     will be more accurate than an analog front end built here.
   - The owner's circuit design work goes into the interface board instead: connectors, I²C pull-ups, decoupling.
     No display or knob headers since D-012; no servo or angle dial with preset angles. See TODO P2.
   - **Owner's plan (2026-11-09):** breadboard first, then a PCB with female header sockets for the modules and DIP
     sockets for any chips such as op-amps, so parts plug in and can be swapped.
   - If an analog sensor is ever used, the kit's LMC6484 suits a single 5 V supply better than the LM741, which
     needs split supplies (TI calls the LMC6484 rail-to-rail; its datasheet is not yet in `resources/`).
3. **Top airspeed and sphere diameter. Answered 2026-11-08: 13 m/s target (D-010, Accepted); 3/4 in and 1 in Delrin
   balls (owner).** The fan that sets the real top speed is open (D-011): about 13.0–13.4 m/s with the S6, about
   11.3 m/s with the VEVOR (estimates). 13 m/s is not a must-have: at 11 m/s the force is 71 % of that at 13 m/s and
   the predicted C_D rise is 7.8 % instead of 9.2 % (3/4 in ball at 6.5 m/s to the 1 in ball at the top speed). The
   history:
   - the owner's target top speed. **Proposed (agent, 2026-11-05): 13 m/s**, with validation runs from about
     6.5 m/s. Reasons (estimates; [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#top-speed-trade-off-proposed)):
     - the trend check gains little above it. Eq. (19) rises 8.7 % from the 20 mm sphere at 6.5 m/s to the 25 mm
       sphere at 13 m/s, and 9.8 % at 15 m/s;
     - one 6-inch fan listing about 500 Pa should just reach it. 15 m/s needs an 8-inch fan or two fans, and 1.5×
       the power;
     - q = 101 Pa fits a ±125 Pa sensor (full scale at 14.4 m/s).

     The cost: drag grows with V², so 15 m/s would give about 35 % more force (1.9 instead of 1.4 gf on the 20 mm
     sphere). If the real fan reaches only 11–12 m/s, the validation still works (about 1.0 gf and a 7 % rise at
     11 m/s). The owner confirmed it on 2026-11-08 (D-010);
   - the sphere diameters: proposed about 20 mm (3.1 % blockage) and 25 mm (4.9 %) for the two-size check.
     **Chosen 2026-11-08: 3/4 in (19.05 mm, 2.85 %) and 1 in (25.4 mm, 5.07 %) Delrin balls**, because inch balls are
     easier to buy in the US. Run the two sizes at **matched Re**, not matched speed: the 3/4 in ball at 13 m/s
     matches the 1 in ball at 9.75 m/s (D-009).
   - D-009's trend check needs runs over a range of speeds, so the fan should run steadily at low speed as well.
     The proposed low end is about 6.5 m/s (2026-11-05): below that the 20 mm sphere's drag is only 0.2–0.3 gf and q
     about 15–25 Pa, so fixed zero errors dominate.
4. **Pressure-sensor range. Answered 2026-11-08: one SDP810-125Pa** (owner chose one sensor over two). Its gain error
   (3 % of reading) is to be calibrated against a home-made inclined water manometer; every reading gets the
   ×966 mbar / p_amb correction. Background: dynamic pressure is only about 15–240 Pa for 5–20 m/s (estimate).
   - Candidates: ±125 Pa (SDP810-125Pa, SDP32), ±249 Pa (Honeywell HSC ±1 inH₂O) and ±500 Pa (SDP810-500Pa, SDP31).
   - Drone airspeed sensors (MS4525DO, ±1 psi) are ruled out: at 10 m/s, q is 0.44 % of their span (our arithmetic).
   - Choose after the top speed. With the proposed 13 m/s: ±125 Pa (the SDP810-125Pa).
5. **Load-cell capacity.** Expected sphere drag is only about 1–2 grams-force at 10–15 m/s in the 100 mm section
   (estimate).
   - Overload protection for model swaps is needed: small bar cells are typically rated for only about 120 % of
     capacity (§2).
   - The load cell also carries the sphere's support (sting/mount), whose drag must be measured and subtracted.
   - A smaller cell lowers the HX711 noise in grams but has less overload margin
     ([HX711 notes](resources/notes/HX711.md)).
   - **Answered 2026-11-08: the TAL221 100 g** (the smallest in its family with a datasheet), two of them, protected by
     overload stops set at about 120 g and by changing balls with the sting lifted out (D-015, 2026-11-09). Its errors are ±0.05 g each at full scale; how they scale at
     0.3–2.3 g loads is unspecified and must be measured in build step 5.
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
9. **What else is on hand? Mostly answered.** Recorded:
   - 2026-11-01: the ECE kit, a multimeter, a soldering station, a bench power supply and a workbench;
   - 2026-11-08/09: 6 in calipers, a hand drill, a spirit level, 43 magnets (8 × 2 mm), PLA, PETG-CF, a
     hardened-steel nozzle, and access to a school lab balance.

   Still unknown:
   - other electronics the owner thinks they have;
   - the bench supply's maximum voltage and current (needed only for a 12 V DC fan);
   - the filament amounts, and the household items (glue, sandpaper, screws, rubber feet, duct tape). The owner will
     report these on 2026-11-10.
10. **Where is the airspeed reference measured during force runs?** A pitot directly ahead of the sphere would put its
    wake on it. Options:
    - a probe off the centreline;
    - wall static taps calibrated against a pitot at the model position in the empty tunnel.

    Either way, at least 1.5√C upstream of the sphere ([Cooper1998](resources/notes/Cooper1998.md)). Check Barlow1999
    ch. 6 (test-section calibration).

    **Proposed 2026-11-08, accepted in the owner's choices:** the contraction method. Wall-tap rings in the settling
    chamber (S) and at the test-section entrance (E) give Δp = q × (1 − 1/6.25²) = 0.974 q in theory. The real factor
    is calibrated against a home-made total-pressure probe and wall taps at the model station (M) in the empty tunnel.
    One sensor reads both pairs by swapping tubes at two couplers. Still to confirm in Barlow1999 ch. 4 and 6.
11. **Fan speed control from the menu knob. No longer a goal (D-012, 2026-11-08):** there is no menu. The fan keeps
    its own controller, and the Arduino never switches mains. If the S6 is chosen, hobbyists report driving it with a
    10 V PWM signal on its UIS port (not confirmed; D-011).
12. **Model attachment and sting lock. Mostly answered 2026-11-09 ([D-015](DECISIONS.md)).** How the sphere fixes to
    the sting without twisting the load cell, and the form of the sting lock and overload stops.
    **Proposed 2026-11-08:**
    - each Delrin ball is press-fit onto its own 1/8 in brass stem (Delrin cannot be glued), drilled to the centre
      with a printed jig and the owner's hand drill;
    - the stem slides into a 5/32 in sleeve at the top of the sting;
    - stops set at about 120 g.

    **Owner, 2026-11-09 (D-015):** the sting lock is a printed mount on the cell's top end with a hand screw that
    clamps the sting; the sting is lifted out to change balls, and the separate hold-still pin is dropped. Still to
    size in build step 1: the hole fit and depth, the screw length (printed knob on a brass M3 screw, or a bought
    thumb screw) and the stop gap.
13. **Screens and honeycomb: bought or printed, and which mesh?** Added 2026-11-02. **Mostly answered 2026-11-09:**
    aluminium window insect screen (18 × 16 mesh, 66–69 % open, about $10 a roll), four or five screens, and a printed
    honeycomb (owner). Still open:
    - two or three diffuser screens (decide after measuring the delivered wire, 0.010 or 0.011 in);
    - where the first diffuser screen sits (at the fan outlet it costs about 24–28 Pa at 13 m/s);
    - whether to measure a sample screen's pressure drop at about 2 m/s, where the formulas are extrapolated;
    - settling-chamber length: 150–200 mm, or about 380–390 mm plus frames with the chosen parts if spaced for full
      decay (the 2026-11-02 figure of 230–300 mm assumed finer wire and cells; open question 15).
14. **Plan now for a second, vertical load cell?** The owner's model-car downforce idea (2026-11-02) and airfoil lift
    (P3) both need one. Leaving room in the balance box costs little now. **2026-11-09:** a second TAL221 is being
    bought as a spare that could become the lift cell. The owner may never measure lift: a model car can instead be
    studied with mist, on the plain floor insert (D-014, 2026-11-09).
15. **Findings from the drawing package (2026-11-09); settle at sizing.** Our layout reasoning, not measurements
    ([docs/drawings/](docs/drawings/README.md), "Findings"):
    - **settling-chamber length:** with the chosen window screen (500 wire diameters = 127–140 mm between screens) and
      6 mm printed cells (≥ 150 mm after the honeycomb), full-decay spacing gives about 380–390 mm plus frames, not the
      230–300 mm in §2; Mehta1979's 0.2 D spacing gives about 200 mm (open question 13);
    - **taps meet the removable top panel:** E and M taps "one per wall" would put taps in the top panel (D-014), to be
      unplugged at every swap. Options: taps only in fixed walls, or a panel that stops short of the stations;
    - **the M-station floor tap** cannot sit at the sting hole; drawn 30 mm upstream on the sphere insert (offset TBD),
      or the station uses three taps;
    - **250 mm sections need splitting in cross-section:** with walls and flanges they are wider than the 256 mm bed,
      so the settling chamber and contraction inlet are printed in halves or as flat panels (D-005 covers splits along
      the flow only);
    - **the balance box sets the tunnel's height:** at layout values it hangs to about 158 mm below the centre line,
      lower than the chamber flanges (142 mm), so the test-section feet are the tallest and the fan stand must match;
    - **I²C length places the Arduino box:** with the BME280 near the fan inlet and the SDP810 near the test section,
      runs under about 1 m put the box near the middle of the tunnel;
    - **turning the sting-lock screw twists the load cell** unless the mount is held (D-015).

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
- **The SDP810 reads about 5 % high near sea level unless corrected** (2026-11-08;
  [Sensirion2024 notes](resources/notes/Sensirion2024.md)). Sensirion's thermal sensors are calibrated at 966 mbar,
  and direct differential-pressure readings must be multiplied by 966 mbar / p_amb (×0.95 at 1013 mbar). Not in the
  datasheet; the BME280 supplies p_amb.
- **Screens cost more fan pressure than first assumed** (2026-11-08/09; our arithmetic, [buy list](docs/buy_list.md)
  §3). Four or five good screens lose about 33–48 Pa at 13 m/s, against the 18 Pa (0.18 q₀) taken from Mehta1979's
  typical figures. Most of it is the screen at the fan outlet, where the air is fastest. The fan then needs about
  1.55 q₀. A 41 %-open mesh would lose about 142 Pa and cut the S6's top speed to about 11.8 m/s.
- **A bare sting would weigh as much as the sphere in the drag reading** (2026-11-08; our arithmetic). A 1/8 in
  sting with 40 mm in the flow under a 3/4 in ball has about 115 % of the ball's drag (cylinder C_D 1.1 assumed). A
  fixed shield leaving about 5 mm exposed cuts it to about 0.1–0.2 gf.
- **The load cell's error figures are as large as the signal at low speed** (2026-11-08; [TAL221
  notes](resources/notes/TAL221.md)). 0.05 % FS is 0.05 g: 4 % of the drag at 13 m/s and 17 % at 6.5 m/s on the 3/4 in
  ball, if the full-scale figures held at gram loads. Its zero drifts 0.01 g/°C regardless of load. The calibration
  must measure the real behaviour at 0.2–3 g.
- **Drawing the whole tunnel exposed seven layout gaps** (2026-11-09; open question 15; our reasoning). The two
  largest: the settling chamber grows to about 380–390 mm with the chosen screen and honeycomb if spaced for full
  decay, and the 250 mm sections must be split in cross-section to fit the printer bed.

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:**
   - commit and push this session's changes (commands in the
     [session log](docs/sessions/2026-11-09-drawing-package.md#13-manual-git-commands-as-given-to-the-owner));
   - report what is on hand (filament amounts; glue, epoxy, sandpaper, screws, rubber feet, duct tape, scoring knife,
     power strip): the "Check the house first" section of [docs/shopping_list.md](docs/shopping_list.md);
   - choose the fan, the S6 or the VEVOR, on budget (D-011), and record it as a new decision;
   - order the parts, tracking each in [docs/shopping_list.md](docs/shopping_list.md). The electronics and small parts
     can go now. Weigh the PLA spools to see whether more rolls are needed;
   - check the values read from the three new datasheets (checklists at the end of the
     [SDP8xx](resources/notes/SDP8xx.md), [Sensirion2024](resources/notes/Sensirion2024.md) and
     [TAL221](resources/notes/TAL221.md) notes);
   - still open from before: the settling-chamber spacing (open question 13), the bench supply's rating, and
     confirming D-003, D-004, D-006 and D-007's open exit.
2. **Agent, build step 1 (sizing):** detail the 100 mm tunnel with the parts now chosen.
   - Fan-to-chamber diffuser: Mehta1977, with two or three window-screen positions.
   - Settling-chamber stack: printed honeycomb, two screens (open question 13).
   - Contraction, test section with S/E/M tap stations and the probe guide, the removable top panel with the 8 × 2 mm
     magnets, the two floor inserts (D-014), the removable balance module, sting shield, sting mount and lock
     (D-015), and stops.
   - Settle the drawing findings (open question 15), starting with the settling-chamber spacing and how the 250 mm
     sections split.
   - Then recompute the [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget), the fan pressure (with the screen
     losses in [buy list](docs/buy_list.md) §3) and the filament amount, and update the drawings: the numbers in
     `docs/drawings/wtdata.py`, then `python docs/drawings/page.py` ([README](docs/drawings/README.md)).
3. **Agent, with sizing:** read Barlow1999 ch. 4 and 6 (instruments, the contraction-pressure method, test-section
   calibration) and ch. 9–10 (solid blockage).
4. **Owner:** download the remaining electronics datasheets (BME280, LM741/LM348/LMC6484) and the chosen fan's manual.
5. **When parts arrive (owner):** the first equipment checks:
   - the load cells' baseline resistances and zero;
   - the BME280 chip ID;
   - the SDP810 zero with the tubes capped;
   - weighing the calibration pieces on the school balance.

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer/wind-tunnel (private; holds `cc51fff`, `5bc60f0`, `b710093`,
  `7db221f`, `9b42a07`, `748dae9`, `8fda08f`, `c04de1b`, `b22a45b`, `36f39eb`, `d7f5cdf`, `0351407`, `b08a151` and
  `0558370`). The account was `nuhshaheer-2007` until
  2026-11-02, and the old URL redirects. The local `origin` points at the new URL (checked 2026-11-02).
- Branch: `main`
