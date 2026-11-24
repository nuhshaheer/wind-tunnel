# Project Status

**Last updated:** 2026-11-24
**Last commit:** `f10f315` (2026-11-23, sensor shield PCB), pushed to `origin/main` (`UP_TO_DATE` at the 2026-11-24
wrap).
- The repo is https://github.com/nuhshaheer/wind-tunnel (account renamed from `nuhshaheer-2007` on 2026-11-02; the old
  URL redirects).
- **Not committed yet:** the 2026-11-24 continuation: a downloaded TAL221 bench-scale design in `cad/third-party/tal221-scale-bwilless/`, a note on
  D-017 and the documentation updates. Commit commands:
  [the session log §13](docs/sessions/2026-11-23-sensor-shield-pcb.md#13-manual-git-commands-as-given-to-the-owner)
  ("Continued").

**Current stage:** Planning / pre-build. The layout is decided and **a full buy list exists
([docs/buy_list.md](docs/buy_list.md), about $315–505 before tax and shipping). Everything ordered on 2026-11-09/10 has
arrived (owner, 2026-11-17): all the sensors and boards, the screen, tubing and fittings, brass, balls, acrylic,
fasteners, tools, 4 kg of black PLA. Most arrival checks are not done yet. Still to buy: the fan (bought last, once the airspeed
readout works), and any "check house" items not at home.** The owner tracks orders in
[docs/shopping_list.md](docs/shopping_list.md). **A preliminary drawing package** of the whole tunnel (10 mechanical
sheets, parts list, TBD register; pre-sizing, not for manufacture) is in [docs/drawings/](docs/drawings/README.md)
(2026-11-09; revision C 2026-11-10). **Revision D (2026-11-17) adds the sensor circuit:** a system block diagram
(sheet 11) and an interface schematic (sheet 12) with its parts and net lists ([D-018](DECISIONS.md), Tentative),
explained for a beginner in [docs/electronics_walkthrough.md](docs/electronics_walkthrough.md). **The breadboard carries
the whole sensor circuit, and every sensor reads (2026-11-23):** the I²C scan finds the SDP810 and the BME280, a penny
moves the load cell's reading, the SDP810 zeroes within 0.03 Pa with the right sign, and the BME280 reads room values
([as built](docs/experimental_setup.md#breadboard-as-built)). Nothing is calibrated yet. **The shield PCB is designed
(2026-11-23, [D-020](DECISIONS.md)):** the owner drew it in KiCad 10 (`PCB/arduino_shield/`); its checks pass and its
Gerbers are ready, but it is not ordered until the two capacitors' lead spacing is measured. **A printable TAL221 bench
scale** (a downloaded design, CC BY, in `cad/third-party/tal221-scale-bwilless/`; 2026-11-24) will give the load cell a firm mount on the bench; not
printed yet. **The calibration weights are weighed (2026-11-19, [EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing)):** on the school's
0.01 g balance they are −2.5 % to +1.1 % off their stamped values, so the measured masses are used.
**The owner draws all the CAD from the sizing's dimension sheets (D-017, 2026-11-15), in Fusion 360 (owner,
2026-11-17).** Planning estimate (not a result): about 70–155 h of the owner's time to the sphere validation, roughly
mid-January to mid-May 2027 at 6–8 h a week; the owner has school and other commitments
([estimates](docs/sessions/2026-11-17-time-estimates-and-cad.md#6-measurements-and-results)).
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
    model (D-014); a printed sting mount with the owner's thumb-screw sting lock (D-015)** (owner, 2026-11-09);
  - one full-length 1/8 in brass sting per ball, no 5/32 in sleeve (D-016, **Tentative**, 2026-11-09);
  - **the owner draws all the CAD; the agent supplies dimension sheets, the contraction points file and checks of the
    exported files (D-017, 2026-11-15).** The owner uses Fusion 360 (2026-11-17);
  - the sensor circuit: laptop USB power, the SDP810 and BME280 on one I²C bus (pins 20/21), the HX711 on pins 2/3,
    breadboard first and then a shield PCB on the Mega (D-018, **Tentative**, agent's design, 2026-11-17; the breadboard
    test passed on 2026-11-23);
  - bring-up firmware: one plain sketch per sensor in `firmware/`, raw CSV output, the Adafruit library for the BME280
    only (D-019, **Tentative**, agent's choice, 2026-11-23);
  - **the shield PCB (D-020, owner, 2026-11-23):** KiCad, the Mega shield template, 2.54 mm pin headers for jumper
    wires, each connector in its part's own pin order so every cable runs straight, a five-pin J3, C1 on the shield.
- **Open: the fan (D-011, Tentative since 2026-11-09).** The owner will choose on budget between the AC Infinity
  CLOUDLINE S6 ($99; about 13.0–13.4 m/s, estimate) and the VEVOR VV-GDFJ-AC6 ($53.90; about 11.3 m/s). **The agent
  recommends the S6** (2026-11-09; [buy list](docs/buy_list.md) §1).
- Parts chosen in the buy list (owner, 2026-11-08/09), **all arrived by 2026-11-17** (owner):
  - one Sensirion SDP810-125Pa (**ordered 2026-11-09** from Mouser) with a home-made brass total-pressure probe and
    wall taps;
  - two TAL221 100 g load cells and a SparkFun HX711 board (**ordered 2026-11-09** from SparkFun), and a **Waveshare
    BME280** (ordered 2026-11-09, instead of the Adafruit 2652);
  - 3/4 in and 1 in Delrin balls (**ordered**, a pack of 10 of each, reported 2026-11-10);
  - aluminium window screen (**ordered 2026-11-09**: Saint-Gobain ADFORS FCS9222-M) and a printed honeycomb.
- Twenty-one references reviewed:
  - tunnel design and testing: Abdelhamed2014, Bell1988, Mehta1979, Mehta1977; **Barlow1999 (chapters 4, 6, 7, 9, 10
    and §§12.1–12.3), Bradshaw1964 and Morel1975 (2026-11-22)**;
  - flow conditioning: Scheiman1981, Wieghardt1953;
  - blockage: Maskell1963, Cooper1998; **Anthoine2004 (cylinders, 2026-11-22)**;
  - sphere C_D: Morrison2013, Roos1971, Brown2003;
  - the balance paper Weakly2024;
  - datasheets and notes: HX711, **SDP8xx, TAL221, and Sensirion2024**, an app note on correcting the SDP810 for
    ambient pressure (2026-11-08); **WaveshareBME280**, the ambient board's schematic (2026-11-17).

  One more is filed in `resources/` but not yet read: Ewald1998, the full AGARD-AG-336 (its chapter 6 is Cooper1998).
- On hand:
  - the ECE kit (from its packing list) and the Elegoo Mega 2560 (**working**: Blink upload Verified 2026-11-02, §3);
  - 43 magnets (8 × 2 mm);
  - tools: a multimeter, a soldering station, a bench power supply, 6 in digital calipers (battery may be dead), a
    hand drill and a spirit level;
  - for printing: PLA and PETG-CF (amounts unknown) and a hardened-steel nozzle;
  - access to a school lab balance (CGOLDENWALL HZ50002B, 5000 g, d = 0.01 g; used 2026-11-19);
  - a calibration weight set: 50, 2 × 20, 6 × 10, 2 × 5 and 3 × 2 g, plus a 10 g hanging rod (owner, 2026-11-19; the
    only set bought, not the 17-piece set the buy list planned);
  - since 2026-11-17, every part ordered on 2026-11-09/10 (owner: "all of the packages i bought have arrived"; arrival
    checks pending).
- The tunnel is not built. No analysis code exists; the firmware is four bring-up sketches
  ([firmware/README.md](firmware/README.md), 2026-11-23). The only thing built is the bench breadboard with every sensor
  ([as built](docs/experimental_setup.md#breadboard-as-built)); the shield PCB exists as a design only (2026-11-23). The only data: the calibration weights' masses
  ([EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing), 2026-11-19).

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
| Airspeed measured with pitot tube + differential pressure sensor | Planned. The SDP810 reads on the bench: zero −0.022 Pa, correct sign (2026-11-23) |
| Drag force measured with load cell + HX711 | Planned. The load cell and HX711 read on the bench: a penny moves the reading about 33,300 counts (2026-11-23) |
| Load cell calibrated against known weights | Planned. The masses were weighed on 2026-11-19 ([EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing)) |
| Sphere Cd validation run (deliverable) | Planned. Reference and pass criterion: [D-009](DECISIONS.md) (Accepted 2026-11-02) |
| Sensor interface circuit, designed by the owner: circuit → breadboard test → PCB | In progress: circuit drawn on paper 2026-11-17 (sheets 11–12, [D-018](DECISIONS.md), Tentative; the agent drew it at the owner's request, and the owner, a beginner in electronics, learns it from [the walk-through](docs/electronics_walkthrough.md) and will draw it in the PCB program). Breadboard started 2026-11-18 (power wiring Verified by meter) and **completed 2026-11-23: every sensor connected and reading** ([as built](docs/experimental_setup.md#breadboard-as-built)). **Shield PCB designed by the owner in KiCad, 2026-11-23** ([D-020](DECISIONS.md), `PCB/arduino_shield/`): checks pass, Gerbers ready, not ordered. Planned 2026-11-01 ([TODO.md](TODO.md) P2) |
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
| Fan-to-chamber diffuser | Proposed (2026-11-02): area ratio 3.44 (152 mm round → 250 mm square), so the screens need K_sum ≥ 2.1. **Two screens (K ≈ 1.1–1.5 each) allow about 150–200 mm**; the minimum is about 115 mm with two screens, 195 mm with one and 335 mm with none. Below about 220 mm use curved walls or radiused inlet and outlet corners. Fillet the corners. **No flow straightener at the fan outlet**: the fan's swirl helps keep the diffuser attached. **2026-11-09:** with aluminium window screen (K about 0.75–0.85 at the fan outlet), plan **three** diffuser screens if the delivered wire is 0.010 in. **The ordered roll is 0.011 in (maker's spec,
2026-11-09):** two diffuser screens give K_sum 2.15, just enough; three are planned for margin. The first screen at the fan outlet costs about 24–28 Pa at 13 m/s, so consider placing it slightly into the diffuser | [Mehta1977](resources/notes/Mehta1977.md) (Figs. 5 and 7, §6.1; owner-checked), [buy list](docs/buy_list.md) §3 |
| Contraction | Proposed: contraction ratio 6.25 (250 mm → 100 mm square), 5th-order-polynomial wall, about 250 mm long (1.0 × inlet) | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md), [Mehta1979](resources/notes/Mehta1979.md) |
| Settling chamber | Proposed: 250 mm square. A honeycomb (cell length 7–10 diameters, cells of about 2–3 mm, thin walls), then one or two screens at least 58 % open, then about 50 mm (0.2 D) to the contraction. Add a capped port after the last screen for optional mist injection. **Length 150–200 mm** with Mehta1979's 0.2 D spacing; **about 230–300 mm** if spaced for full turbulence decay: at least 500 wire diameters between screens (about 75–125 mm) and about 50 cell diameters from the honeycomb to the first screen (2026-11-02). Decide at sizing. **2026-11-09:** two settling-chamber screens (four or five screens in all, per Mehta1977/1979); a **printed honeycomb** (owner; for example 6 mm hexagons, 0.4 mm walls, about 50 mm long), with straws as the upgrade; wall pressure taps (S) for the airspeed reference. **Found while drawing (2026-11-09; open question 15):** with the chosen window screen and 6 mm cells, full-decay spacing gives about 380–390 mm plus frames, not 230–300 mm (our arithmetic) | [Mehta1979](resources/notes/Mehta1979.md), [Mehta1977](resources/notes/Mehta1977.md), [Scheiman1981](resources/notes/Scheiman1981.md) |
| Test section | Proposed: **closed** section with clear panels. Sphere at least about 0.5 D downstream of the contraction exit; sphere blockage about 3 % (at most 5 %); reference pressure reading at least 1.5√C upstream of the sphere; sphere at least 4√S from the test-section end. Together 2.7–2.9 h, i.e. 270–290 mm (estimate). **2026-11-08:** wall pressure taps at the entrance (E) and at the model station (M); a printed probe guide; a streamlined **sting shield** about 7.5 mm wide (5 mm hole for the 1/8 in sting) up to about 5 mm below the ball, because a bare sting would have about 115 % of the ball's drag. **2026-11-09 ([D-014](DECISIONS.md)):** the shield is fixed to a replaceable floor insert under the model | [Mehta1979](resources/notes/Mehta1979.md), [Cooper1998](resources/notes/Cooper1998.md), [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed) |
| Model access | **Accepted 2026-11-09 ([D-014](DECISIONS.md), owner): the top clear acrylic panel lifts off, held by magnets** (design later); whether a side panel also comes off is open. **The floor under the model is a replaceable insert:** a sphere insert carrying the sting hole and the shield, and a plain insert for model cars (replaces the floor plug). Agent's design points (Proposed): pins or lips locate each panel and insert; inner faces flush with the walls (the insert's front edge is just upstream of the ball); a foam gasket seals each panel; the pitot goes through a fixed wall; **no magnets near ferrous parts on the measured side of the balance**, and a non-magnetic sting. Owner's concept since 2026-11-01; the owner's 43 magnets (8 × 2 mm) suffice; 1/8 in acrylic | [D-014](DECISIONS.md), [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md), [buy list](docs/buy_list.md) §4 |
| Balance and controls layout | Proposed (2026-11-01): only the load cell and HX711 in a closed box under the floor (the sketch's "electronics house"). The Arduino in a separate box on a cable (no display or knob since D-012). **2026-11-09 ([D-015](DECISIONS.md), owner):** a printed sting mount screwed to the cell's top end; the owner's sting lock, a hand screw from the side, clamps the sting in the mount without glue; the sting is lifted out to change balls; overload stops at about 120 g; no separate hold-still pin. Optional (2026-11-02): leave room for a second, vertical load cell for airfoil lift or model-car downforce (P3). **2026-11-08:** the cell stands upright directly under the ball, the sting clamped only to its top end, its screw holes along the wind ([owner's sketch](docs/sketches/README.md)); the balance is a removable module so it can be laid on its side for calibration; each ball is press-fit (Delrin cannot be glued) onto its own full-length 1/8 in brass sting, so balls are changed by swapping the whole sting; the 5/32 in sleeve of 2026-11-08 is dropped ([D-016](DECISIONS.md), Tentative, 2026-11-09; the owner found the tube would arrive only by 2026-11-19) | [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#measurement-and-analysis-approach-proposed) |

## 3. Hardware and instrumentation

Parts on hand are recorded from the owner's statements and the ECE kit's packing list (2026-11-01). The full kit list
is in [docs/experimental_setup.md](docs/experimental_setup.md#parts-on-hand). Prices below were seen on retailer
listings on 2026-11-01 unless marked otherwise; they are guides, not quotes.

| Item | Availability | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | On hand (owner has access, stated 2026-10-30) | Build volume 256 × 256 × 256 mm (manufacturer spec). **2026-11-09 (owner):** PLA and PETG-CF on hand (amounts unknown) and a hardened-steel nozzle, so PETG-CF can be printed |
| ECE2010 lab kit (WPI) | On hand, per its packing list (owner, 2026-11-01). Quantities are the packed ones, not counted | Includes LM741, LM348 and LMC6484 op-amps, LM311, 555, LM317T and LM7805CT regulators, transistors, MOSFETs, potentiometers (1 × 10 kΩ, 2 × 1 kΩ, 1 × 100 kΩ, 1 × 1 MΩ), resistors, capacitors, breadboard and jumper wires. No multimeter, soldering iron or power supply in the list (the owner has them separately) |
| Tools | On hand (owner): multimeter, soldering station, bench power supply, access to a workbench (2026-11-01); **6 in (150 mm) digital calipers** (battery thought dead; LR44/SR44 size), a **hand drill** and a **spirit level** (2026-11-08); access to a **school lab balance** (2026-11-08; a CGOLDENWALL HZ50002B, 5000 g, d = 0.01 g, owner 2026-11-19) | Models unknown. The bench supply's maximum voltage and current are unknown; they matter only if a 12 V DC fan is chosen. **Arrived by 2026-11-17 (ordered 2026-11-09/10):** tube cutter, a 0.7–3.0 mm drill-bit set, a pin vise, an LR44 for the calipers, an acrylic scoring knife ([buy list](docs/buy_list.md) §10) |
| Other electronics | Unknown | The owner thinks more is on hand (2026-11-01); not listed yet |
| Microcontroller | **On hand, working: Elegoo Mega 2560.** Blink upload **Verified** 2026-11-02 (owner's test) | Evidence, 2026-11-02:<br>• The owner read ATMEGA2560 on the main chip. The owner's 2026-11-18 photos show the R3 header layout: IOREF on the power header and pins marked SDA1 and SCL1 beside AREF. Whether those two pins join pins 20/21 is not measured.<br>• Windows listed it on COM3 with USB ID 2341:0042, which the Arduino AVR core (1.8.8, `boards.txt`) lists under "Arduino Mega or Mega 2560". USB serial number `13448474939351C0E828` identifies this board.<br>• The owner uploaded Blink with both delays changed from 1000 to 200 ms (Arduino IDE 2.3.10, board "Arduino Mega or Mega 2560", processor ATmega2560), and the "L" LED blinked faster. A faster blink proves the upload, because a blinking LED alone could be a factory-loaded sketch.<br>From the Mega 2560 Rev3 documentation (retailer pages; not checked on this board): 5 V logic; I²C on pins 20 (SDA) and 21 (SCL), also brought out next to AREF on R3 boards; ATmega16U2 USB-serial. Covers every planned sensor (no display or knob since D-012). **Wired to the breadboard 2026-11-18 (sheet 12, D-018; [as built](docs/experimental_setup.md#breadboard-as-built)):** SDA 20, SCL 21, HX711 DAT 2 and CLK 3, powered from the laptop's USB. **Reads all three sensors with the bring-up sketches (2026-11-23; [as built](docs/experimental_setup.md#breadboard-as-built))** |
| USB A-to-B cable for the board | On hand, carries data: the board enumerated on COM3 through it (2026-11-02) | The board's original cable was lost. The owner was ordering a UGREEN 5 ft cable (2026-11-01); which cable was used on 2026-11-02 is not recorded |
| Blower / fan | To buy; **open between two (D-011, Tentative since 2026-11-09); the owner will choose on budget. The agent recommends the S6 (2026-11-09)** | • **Why the S6 (agent, 2026-11-09; [buy list](docs/buy_list.md) §1):** about 2.0–2.1 m/s faster whatever the tunnel's true loss factor; maker's figures, where the VEVOR's 300 Pa is a seller's (at 250 Pa it would reach about 10.75 m/s, at 200 Pa about 10.0); an EC motor, likely steadier at low speed; a wider matched-Re range for the two-ball check.<br>• **AC Infinity CLOUDLINE S6, model AI-CLS6**: $99.00; maker's page (read 2026-11-08): 425 CFM, 503 Pa, PWM-controlled EC motor, 10 speed levels, 32.0 cm long. Retailers list 402 CFM. About 13.0–13.4 m/s with five window screens (straight-line estimate; 12.3–12.7 at 90 % of the curve).<br>• **VEVOR 6-inch inline duct fan, model VV-GDFJ-AC6**: $53.90 (owner, 2026-11-09); seller's figures 400 CFM, 300 Pa, AC motor with a speed controller, 60 W. About 11.3 m/s (10.8). Its "34 dB" claim is unlikely, so its 300 Pa may be optimistic.<br>Both validate; the VEVOR gives about 73 % of the S6's force at top speed. Earlier candidates and the unsuitable fans: [2026-11-07 log](docs/sessions/2026-11-07-top-speed-and-fan-search.md). Estimates: [buy list](docs/buy_list.md) §1 |
| Fan-to-tunnel joint | Owner's design (2026-11-08) | The fan's collar, wrapped in one layer of 1/16 in 40A neoprene (on hand: 2 sheets of 12 × 12 in, arrived by 2026-11-17; no single 480 mm strip fits, so two ~240 mm pieces butted end to end), slides snugly into a printed inlet sized from the measured collar (paper strip ÷ π); duct tape seals it. The fan stands on its own feet and never touches the print. [Buy list](docs/buy_list.md) §1 |
| Honeycomb + screens | **Screens on hand** (ordered 2026-11-09; arrived by 2026-11-17, owner; wire count not checked yet); honeycomb printed | **Screens: aluminium window insect screen, Saint-Gobain ADFORS FCS9222-M, Bright, 36 × 84 in roll from Home Depot, ordered 2026-11-09.** The maker's spec gives 18 × 16 mesh and 0.011 in wire, so 66.1 % open (computed); price paid not recorded; wire count and diameter to be checked on arrival. Also checked 2026-11-09: a 35 × 35 × 0.011 in mesh (37.9 % open) rejected; McNichols' and New York Wire's 18 × 16 × 0.011 in screens suitable ([buy list](docs/buy_list.md) §3). Four or five screens (two or three in the diffuser, two in the settling chamber; Mehta1977/1979, Scheiman1981). Rejected: McMaster 30 × 30 filter mesh (0.012–0.013 in wire, 37–41 % open: about 11.8 m/s top speed and patchy flow), Online Metals 24 × 24 × 0.014 in (44 %), McNichols perforated sheet, a TWP quote of about $200, Zoro's $65.59 sheet (too expensive). **Honeycomb: printed (owner, 2026-11-08)**, for example 6 mm hexagons with 0.4 mm walls, about 50 mm long; straws as the upgrade. Details: [buy list](docs/buy_list.md) §3 |
| Pitot tube | **Made in-house (owner, 2026-11-08)** | A 1/8 in brass total-pressure tube facing upstream, with wall static taps (four per station) at three stations: S (settling chamber), E (test-section entrance), M (model station). Probe − M gives q at the model position (flow map, calibration); S − E gives the airspeed during force runs, calibrated once against the probe (open question 10). Brass tube, 1/8 in silicone tubing and barbed tees **on hand** (ordered, reported 2026-11-10; arrived by 2026-11-17; [buy list](docs/buy_list.md) §5). The Dwyer 166-6 ($140–167) was not chosen |
| Differential pressure sensor | **On hand, arrived by 2026-11-17** (owner). The owner's photo shows `SDP810 - 125Pa`, `PN:1-101597-01`, the datasheet's order number. **On the breadboard, 2026-11-23: it reports scale factor 240 (the ±125 Pa part), zeroes at −0.022 Pa with the ports looped and reads + on High, − on Low (Verified for function; span not calibrated).** Connected by a PH 2.0 cable spliced to jumpers. Ordered 2026-11-09 from Mouser (owner; price paid not recorded; **order confirmed 2026-11-10: Mouser 403-SDP810-125PA, maker's part SDP810-125PA**, the ±125 Pa part): **one Sensirion SDP810-125Pa** (owner chose one, 2026-11-08), $29–35 (DigiKey 1649-1073-ND, Mouser 403-SDP810-125PA) | Datasheet reviewed 2026-11-08 ([notes](resources/notes/SDP8xx.md)): 0.08 Pa + 3 % of reading; 2.7–5.5 V; I²C address 0x25 on every 125 Pa part (a second sensor would need a multiplexer); four solder pins at 2 mm pitch; Ø3.5/5.2 mm barbs. **Every reading must be multiplied by 966 mbar / p_amb** (×0.95 at sea level; [Sensirion2024 notes](resources/notes/Sensirion2024.md)). Tubes are swapped between probe/M and S/E at two couplers on short pigtails |
| Load cell + HX711 | **On hand, arrived by 2026-11-17** (owner). Photo, 2026-11-17: the HX711 board's pads are RED, BLK, WHT, GRN, YLW and VDD, VCC, DAT, CLK, GND; the load cell's wires are red, black, white and green. **2026-11-23:** one TAL221 soldered straight to the HX711's pads after a resistance check at its free wire ends ("about" 1090 and 1000 Ω), and a female header on the HX711's Arduino side. RATE at 10 samples/s (from the 95.5 ms reading interval). A penny moves the reading about 33,300 counts, about 13,300 counts per gram if the penny is 2.5 g (Verified response; the size is Preliminary). Excitation voltage not measured yet. Ordered 2026-11-09 from SparkFun (owner; price paid not recorded): **two TAL221 100 g** (SparkFun SEN-14727, about $16 each; one spare/possible lift cell; owner, 2026-11-08) and **one SparkFun HX711** (SEN-13879, $11.50) | Datasheet reviewed 2026-11-08 ([notes](resources/notes/TAL221.md)): 0.6 ± 0.15 mV/V, safe overload 150 % (150 g), errors ±0.05 % FS each, zero tempco ±0.1 % FS/10 °C. At gram loads the %FS figures are unspecified, so build step 5 must measure them. Drag 0.30–1.27 gf (3/4 in ball) and 0.54–2.31 gf (1 in) at 6.5–13 m/s (estimate) |
| Ambient pressure / temperature sensor | **On hand, arrived by 2026-11-17** (owner; cable resistance check 2026-11-18. **2026-11-23: SDA and SCL 4.81 V, chip ID 0x60, reads 99.6 kPa, 23.3 °C and 44.5 %, and responds to breath and touch. It reset once when its Dupont wiring was handled; the sketch detects that and sets it up again**): **Waveshare BME280 Environmental Sensor**, ordered 2026-11-09 instead of the Adafruit BME280 (2652, $14.95); seller and price paid not recorded | An RT9193-33 regulator and, per Waveshare's product page, an onboard 3.3/5 V level translator for the 5 V Mega. Gives air density and the SDP810's ambient-pressure correction. **Placement (agent, 2026-11-19):** in room air near the fan inlet, in its own open, vented printed holder, not inside the tunnel and not in the Arduino box. Inside, the air differs from the room by at most about 0.15 % in pressure and under about 0.4 °C (fan heating; estimate assuming ≤ 60 W into 0.156 kg/s), which moves the reference C_D by about 0.02 %, while a board in the flow would disturb it. The fan heating is to be checked once with the fan running (TODO P2). On arrival: SDA and SCL read about 5 V with only power connected, then the chip ID reads 0x60 (not a BMP280's 0x58) ([buy list](docs/buy_list.md) §7). **Waveshare's schematic** (filed 2026-11-17, [notes](resources/notes/WaveshareBME280.md)): header 1 VCC, 2 GND, 3 SDA, 4 SCL, 5 ADDR, 6 CS; 4.7 kΩ pull-ups to VCC on SDA, SCL, ADDR and CS, so the I²C address is 0x77 with ADDR left open and no extra pull-ups are needed. **Delivered cable (photo):** a 6-pin plug to six female Dupont sockets; red, black, blue, yellow, orange, green are taken as VCC, GND, SDA, SCL, ADDR, CS (inferred from the wire order). **Measured 2026-11-18, unpowered:** red to blue, yellow, orange and green 4.605, 4.617, 4.597 and 4.617 kΩ; black to blue 145.3 kΩ |
| Interface circuit | **Designed 2026-11-17 ([D-018](DECISIONS.md), Tentative). Breadboard complete 2026-11-23: every sensor reads** | Sheet 12 of the [drawing package](docs/drawings/README.md): SDP810 and BME280 on I²C pins 20/21, HX711 DAT/CLK on pins 2/3; C1 0.1 µF at the SDP810, C2 10 µF at the 5 V entry, R1/R2 5.1 kΩ pull-ups drawn but not fitted, connectors J1–J3. All from the ECE kit and parts on hand: nothing to buy. **Laptop USB is the only supply** (about 100 mA in all against 500 mA, estimate). Breadboard first, then a shield PCB (KiCad recommended, or EasyEDA; owner to choose). Explained in the [walk-through](docs/electronics_walkthrough.md). **Bench result 2026-11-18:** 4.962 V at both pairs of rails and across C2, with USB from the laptop (meter model Unknown; [as built](docs/experimental_setup.md#breadboard-as-built)). **2026-11-23, every sensor connected:** 4.947 V on the rails, SDA and SCL 4.81 V; the I²C scan finds 0x25 and 0x77. Two resistors that look like R1 and R2 are still on the board (photos; harmless). **C1 on the breadboard is probably 1 µF, not 0.1 µF** (owner's recollection, 2026-11-23; to confirm from its marking); the SDP810 read correctly with it, and the SDP8xx datasheet names no value. **Shield PCB designed 2026-11-23 ([D-020](DECISIONS.md), Implemented, unverified):** J1–J3 are 2.54 mm headers for jumper wires in each part's pin order (J1 SCL, +5V, GND, SDA; J2 +5V, GND, SDA, SCL; J3 +5V, +5V, DAT, CLK, GND); C1 0.1 µF beside J1, C2 at the 5 V entry, R1/R2 unfitted pads; 101.6 × 53.34 mm, 2 layers; Gerbers in `PCB/arduino_shield/gerbers/`. Not ordered: the C1 and C2 footprints are placeholders until measured |
| Ribbon cable and connector kit | **On hand** (owner's photo, 2026-11-17) | elechawk kit: 24 AWG 20-wire ribbon cable, PH2.0 "male" connectors 2P–8P, PH2.0 male crimp pins, heat-shrink. No crimp tool is shown. The parts look male, so they would not mate with the SDP810's male pins (open question 19) |
| Display and knob | **Not needed (D-012, owner, 2026-11-08)** | All output goes to the laptop (the Arduino IDE's Serial Plotter for a live view) |
| Servo (airfoil pitch) | Probably not needed | The owner switched to preset angles of attack (2026-11-01). The 2026-10-31 dial-and-servo idea is kept in [TODO.md](TODO.md) P3 for reference |
| Magnets | **On hand: 43, round, 8 mm × 2 mm** (owner, 2026-11-09; probably neodymium, not confirmed) | Enough for the removable top panel (about 8 per panel; D-014) and a side panel if one is made removable |
| Acrylic sheet | **On hand** (ordered, reported 2026-11-10; arrived by 2026-11-17): clear cast acrylic, 1/8 in (3.2 mm), **four 8 × 12 in sheets** (owner, 2026-11-10) | For the window panels; cut by scoring and snapping. Each sheet (203 × 305 mm) gives one panel of about 300 × 120 mm plus a strip about 80 mm wide, so a window can be up to about 305 mm long (our arithmetic) |
| TAL221 bench scale (printed fixture) | **Planned: design filed 2026-11-24, not printed** | "TAL221 Load Cell Scale" by Thingiverse user bwilless (thing:4665143, CC BY), in `cad/third-party/tal221-scale-bwilless/` ([setup](docs/experimental_setup.md#bench-load-cell-scale-to-print)). A horseshoe base holds the cell's fixed end; a Ø60 mm pan sits on the free end. The STLs match the TAL221 notes (Ø3.2 mm holes 6 mm apart, 39.9 mm span, a 6 mm gap for the cell). No overload stop: keep at most about 80 g on the pan, never press it. For the several-minute zero and calibration practice |
| Calibration weights | **On hand** (owner, 2026-11-19) | The only set bought, from Amazon (listing and price not recorded): 50, 2 × 20, 6 × 10, 2 × 5 and 3 × 2 g, plus a 10 g hanging rod (10 g from the listing); the multiples labelled #1, #2, ... on tape. Not the 17-piece 10 mg–100 g set planned in the [buy list](docs/buy_list.md) §9. **Weighed 2026-11-19** ([EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing)): −2.5 % to +1.1 % off nominal; together 165.5 g, 175.3 g with the rod, more than the TAL221's 150 g safe overload |
| Mist or smoke generator (optional visualization) | Not decided; deferred to the end | The owner asked (2026-11-01) for one that makes thick smoke. Options compared in [TODO.md](TODO.md) P2; the agent's first choice is an ultrasonic mist maker |

Budget: no fixed budget (owner, 2026-11-01), but price-conscious. **The full buy list,
[docs/buy_list.md](docs/buy_list.md), totals about $315–505 before tax and shipping** (2026-11-09; the low end
with the VEVOR fan), plus up to about $100 for items that may already be in the house. Everything ordered on
2026-11-09/10 has arrived (owner, 2026-11-17). The owner's tracker, [docs/shopping_list.md](docs/shopping_list.md) (2026-11-10), lists what is
still to buy: the fan ($53.90 or $99), and up to about
$65–100 of "check house" items if none are at home (our sums of the listed prices; many are typical prices, not
checked).

## 4. Software and tooling

| Component | Status |
|---|---|
| Data acquisition firmware | **Bring-up sketches Implemented and run on the bench, 2026-11-23** ([firmware/README.md](firmware/README.md), [D-019](DECISIONS.md), Tentative): `i2c_scan`, `hx711_raw_counts`, `sdp810_read`, `bme280_read`, each passing its walk-through test. **The logging firmware (one CSV line with every sensor, walk-through step 4) is Planned, not started.** Since D-012 (2026-11-08): log raw counts over USB to the laptop, which is also the live view (the Arduino IDE's Serial Plotter to start); no display or knob code. SDP810 commands and scale factor are in the [SDP8xx notes](resources/notes/SDP8xx.md). Pins and buses: sheet 12 ([D-018](DECISIONS.md)). Bring-up sketches proposed 2026-11-17, written 2026-11-23 |
| Analysis scripts (`analysis/`) | Planned; not started |
| Drawing package ([docs/drawings/](docs/drawings/README.md)) | Implemented 2026-11-09; a preliminary, pre-sizing design, not checked against anything built. **Revision C, 2026-11-10:** one full-length sting per ball, no sleeve or separate stems (D-016); stainless short M3 screws at the balance; the shield attached to the sphere floor insert; every parts-list status as ordered; the unused draft sheet code deleted (the page rebuilt byte-identical before the content changes). `python docs/drawings/page.py` rebuilds the page (standard library only). Checked: every callout has a parts-list row and every part is drawn (`parts never drawn: []`). The owner's private published copy on claude.ai matched revision B and has not been republished as C or D (owner's call; TODO P0). **Revision D, 2026-11-17:** electrical sheets 11 (system block diagram) and 12 (interface schematic, electrical parts list, net list); sheet 9's wiring note and HX711 pins point to sheet 12; parts-list statuses Ordered → On hand. `wtlib.py` gained an electrical key and title-block fields, refactored first with byte-identical output. **Sheet 12 revision E, 2026-11-23:** the connectors in each part's pin order (straight cables), a five-pin J3, C1 on the shield, the HX711 in board order with its pad names (D-020); sheets 1–11 unchanged; the last text-only edits could not be previewed (Edge stopped writing screenshots) |
| Electronics walk-through ([docs/electronics_walkthrough.md](docs/electronics_walkthrough.md)) | Written 2026-11-17 for a beginner: the ideas needed, how the wiring and pins were decided, reading the schematic, power, the breadboard bring-up steps (Planned), breadboard to PCB, self-check questions, resources. Documentation only. Corrected 2026-11-18 from the delivered parts (HX711 pad names, SDP810 pin view, BME280 cable and first checks); steps 1–3 done on the bench 2026-11-23; §7 and §10 updated 2026-11-23 for the shield PCB (pin order, connector type, KiCad) |
| Shield PCB (`PCB/arduino_shield/`, KiCad 10) | **Implemented, unverified (2026-11-23):** drawn by the owner from KiCad's Arduino Mega shield template ([D-020](DECISIONS.md)). Final ERC: 69 warnings, all the template's labels on unused pins, 0 errors. Final DRC with schematic parity: 0 unconnected items, 0 parity issues, 9 harmless warnings. Gerbers (7 layers) and drill files in `gerbers/`, checked by the agent (layers, outline 101.6 × 53.34 mm, 112 pads and 113 mask openings per side, 118 holes); not ordered, not made. Agents check it with `kicad-cli` on a copy (commands in the [session log](docs/sessions/2026-11-23-sensor-shield-pcb.md#5-commands-and-scripts-executed)) |
| Weighing form ([docs/forms/calibration-mass-weighing.xlsx](docs/forms/calibration-mass-weighing.xlsx)) | Implemented 2026-11-19 and used once ([EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing)): one sheet in Times New Roman (owner's request), the balance details, three readings per piece, and mean, spread and mean − nominal by formula; Excel computed them on the owner's copy. Reset to a blank template after the filled copy was filed in `data/raw/`. Built by an agent script in the scratchpad (not kept) |
| `scripts/sync_status.py`: Git sync check for agents | Verified by `tests/test_sync_status.py` (10 tests on throwaway local repos: behind, ahead, diverged, local-change collisions, empty remote). States seen live so far, each correct for the situation: `NO_COMMITS_YET`, `UP_TO_DATE`, `FETCH_FAILED`, `AHEAD` (the last two on 2026-10-31, in the owner's terminal) |
| `scripts/check_docs.py`: documentation consistency check | Verified by `tests/test_check_docs.py` (10 tests) and clean runs on this repo |
| `/catchup` | Verified 2026-10-29 by a fresh agent. States exercised live so far: `NO_COMMITS_YET` (2026-10-29) and `UP_TO_DATE` (2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-05, 2026-11-08, 2026-11-09, 2026-11-10, 2026-11-15, 2026-11-17, 2026-11-19, 2026-11-22, 2026-11-23); the others are covered by unit tests. |
| `/wrap` | Verified 2026-10-31. Run by an agent that did not write the skill, with `check_docs.py` at 0 failures. The owner committed and pushed with the commands it gave (`cc51fff..5bc60f0`, then `b710093`, `7db221f`, `9b42a07`, `748dae9`, `8fda08f`, `c04de1b`, `b22a45b`, `36f39eb`, `d7f5cdf`, `0351407`, `b08a151`, `0558370`, `507f71c`, `c768e2c`, `f4fa904`, `f5616a3`, `2ac0809`, `5cb8b7a`, `ce69a57`, `8904785`, `ff2ac6e`, `fd20afe`, `604ee42`, `1ffd4a1` and `f10f315`; `UP_TO_DATE` afterwards). One content error in its first run was corrected by the second ([log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)). |
| No-push guard (`.claude/settings.json`) | Verified 2026-10-29: `git push -h` was blocked by Claude Code for both the Bash and PowerShell tools. |

Dependencies: Python 3 standard library only, developed with Python 3.13 on Windows 11.
- On 2026-11-02, `python` on the owner's PC was **3.11.0** in both Git Bash and PowerShell. The `py` launcher listed
  3.10, 3.11, 3.12 and 3.14, but no 3.13. The 20 tests pass under 3.11.
- Git 2.54, Git LFS 3.7 (installed, not enabled), GitHub CLI 2.97.
- openpyxl 3.1.5, installed for Python 3.11 by the agent on 2026-11-19 (`python -m pip install --user openpyxl`) to write
  the weighing form; not a project dependency. LibreOffice is not installed.
- Arduino IDE 2.3.10 with the Arduino AVR Boards core 1.8.8, installed by the owner on 2026-11-02 (versions read from
  the program file and the core's folder). `arduino-cli` is not installed, so agents cannot compile sketches; the owner's
  IDE compiles them on upload.
- Adafruit BME280 Library (Arduino), installed by the owner on 2026-11-23 for `firmware/bme280_read`; version not
  recorded yet.
- KiCad 10.0.7, installed by the owner (version from `kicad-cli version`, 2026-11-23) at
  `C:/Program Files/KiCad/10.0/`. Its `kicad-cli` lets agents export the net list, run ERC and DRC and plot PDFs from
  a copy of the project without opening it.
- Pillow 12.1.1 is installed for Python 3.11 (used 2026-11-23 to strip and compress photos); not a project dependency.
- Agents reading PDFs used `pdftotext` (Git for Windows) and PyMuPDF 1.28.2, which is installed on the owner's PC
  (Python 3.11). Neither is a project dependency. Claude Code's own PDF page rendering needs `pdftoppm` (poppler),
  which is not installed (2026-11-08), so render pages with PyMuPDF instead.

## 5. Current experiments

None running. EXP-001, the calibration mass weighing (2026-11-19), is complete ([data catalog](docs/data_catalog.md#exp-001-calibration-mass-weighing)).
The bench bring-up of every sensor (2026-11-23) is recorded as bench checks, not a dataset ([as built](docs/experimental_setup.md#breadboard-as-built)).

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
  - Committed and pushed as `507f71c`. See [the session log](docs/sessions/2026-11-09-drawing-package.md).
- 2026-11-09: fan advice and the first order (documentation only; nothing built or tested).
  - Recommended the S6 over the VEVOR, with worst cases if the VEVOR's 300 Pa is optimistic, and explained how the
    top-speed and force estimates are made. The owner has not chosen yet.
  - Listed other experiments the tunnel could do later (ideas, not chosen; TODO P3).
  - Checked three mesh listings: a 35 × 35 × 0.011 in mesh (37.9 % open) is not suitable; McNichols' and New York
    Wire's 18 × 16 × 0.011 in screens are.
  - **The owner ordered the first part: the aluminium window screen** (Saint-Gobain ADFORS FCS9222-M, Bright).
  - Committed and pushed as `c768e2c`. See [the session log](docs/sessions/2026-11-09-fan-advice-and-screen-order.md).
- 2026-11-09/10: parts ordering (documentation only; nothing built or tested).
  - **The owner ordered everything on the buy list except the fan**, which is bought last, once the airspeed readout
    works, so its 30-day return window covers the real test.
  - Parts changed along the way: a Waveshare BME280 instead of the Adafruit (Waveshare states a 3.3/5 V level
    translator); the TUOFENG hook-up wire, with the 4-core cable now optional; stainless screws instead of a brass set
    (the panel magnets' pull is negligible, our estimate); one full-length sting per ball instead of the 5/32 in sleeve
    ([D-016](DECISIONS.md), Tentative).
  - Advice recorded: a later top-down light for mist; how to make the wall taps (print a pilot, drill to finish);
    inch drill sizes; a straight probe through the open exit as an idea; the fan inlet as a separate printed ring.
  - Committed and pushed as `f4fa904`; the README was then brought up to date, committed and pushed as `f5616a3`. See
    [the session log](docs/sessions/2026-11-10-parts-ordering.md).
- 2026-11-10: order details and cylinder advice (documentation only; nothing arrived, built or tested).
  - Recorded the owner's answers: the acrylic is four 8 × 12 in sheets, and the Mouser order is 403-SDP810-125PA (maker's
    part SDP810-125PA), the ±125 Pa part.
  - Named the BME280 as the Waveshare in PROJECT_BACKGROUND and the drawings' parts list (rebuilt); fixed stale
    settling-chamber, diffuser-screen and sphere entries.
  - Advised against buying cylinders now (a 3/8 in brass tube, then McMaster plastic rod): not needed for the
    validation; a full-span 1/4 in Delrin rod would give about 6–8 gf at 13 m/s if a cylinder test is wanted later
    (estimate). See [the session log](docs/sessions/2026-11-10-order-details-and-cylinders.md).
  - Committed and pushed as `2ac0809`.
- 2026-11-10: consistency audit (documentation only; nothing arrived, built or tested).
  - At the owner's request, every folder checked against the latest decisions. Fixed: the sphere mount in
    docs/experimental_setup.md and PROJECT_BACKGROUND ("a fixed shield and a floor slot" → the replaceable sphere
    insert with the shield attached, D-014); leftover sleeve and stem wording (D-016); brass screws at the balance
    (stainless since 2026-11-09); order statuses in the buy list summary, the setup and the drawings' parts list;
    stale notes in the sketches, resources and data indexes. A dated note added to D-015.
  - Drawings revised to C: the sleeve and stem (items 61, 62) removed and one sting drawn from the ball to the mount.
  - Committed and pushed as `5cb8b7a` (2026-11-11). See [the session log](docs/sessions/2026-11-10-consistency-audit.md).
- 2026-11-15/17: time estimates and the CAD approach (planning only; nothing arrived, built or tested).
  - Estimated the owner's time: CAD 12–25 h (the owner's own estimate about 10 h); the whole project to the sphere
    validation about 70–155 h, roughly mid-January to mid-May 2027 at 6–8 h a week (estimates, not results).
  - Discussed agent-drawn CAD (Python CAD scripts) and desktop control; neither chosen. The owner draws all the CAD
    ([D-017](DECISIONS.md)). See [the session log](docs/sessions/2026-11-17-time-estimates-and-cad.md).
  - Committed and pushed as `ce69a57` (2026-11-17).
- 2026-11-17: the sensor circuit (documentation only; nothing wired or tested).
  - `/catchup`: `UP_TO_DATE` at `ce69a57`. The owner reported that every part ordered on 2026-11-09/10 has arrived,
    and that they use Fusion 360 (a dated note on D-017).
  - Drew the circuit as revision D of the drawing package: sheet 11, the system block diagram, and sheet 12, the
    interface schematic with an electrical parts list and net list ([D-018](DECISIONS.md), Tentative). Filed
    Waveshare's BME280 board schematic ([notes](resources/notes/WaveshareBME280.md)): the board has its own I²C
    pull-ups, so none are fitted.
  - Answered the owner's questions: block diagram, schematic and flow chart; EasyEDA or KiCad (KiCad recommended;
    the owner's choice); the laptop as the only power supply; how the circuit becomes a shield PCB on the Mega.
  - Wrote [docs/electronics_walkthrough.md](docs/electronics_walkthrough.md) for a beginner (the owner has no
    electronics background), with snapshots of sheets 11 and 12 in `docs/images/`.
  - Marked the arrived parts On hand (shopping list "Got it", a note in the buy list, the drawings' parts list). See
    [the session log](docs/sessions/2026-11-17-sensor-circuit-design.md).
  - Committed and pushed as `8904785`.
- 2026-11-17/18: first breadboard work (no sensor connected).
  - Read the delivered parts from the owner's photos. The HX711 pads are named by wire colour, and the SDP810's pin order
    must be read from the datasheet's bottom view; the walk-through is corrected.
  - The owner wired the Mega, rails, C2 and signal rows. Continuity passed and the rails read 4.962 V.
  - The BME280 cable's resistances matched the schematic. Its 5 V check is next. See
    [the session log](docs/sessions/2026-11-18-breadboard-power-and-part-checks.md).
  - Committed and pushed as `ff2ac6e`.
- 2026-11-19: BME280 advice and the calibration mass weighing.
  - `/catchup`: `UP_TO_DATE` at `ff2ac6e`; the owner had moved the original photos out of the repo.
  - Answered: what the BME280 is for, and why it stays in room air in its own vented holder rather than inside the
    tunnel (estimates in §3).
  - Made a weighing form in Times New Roman at the owner's request; at school the owner weighed every calibration
    piece three times on a CGOLDENWALL HZ50002B (d = 0.01 g), re-zeroing before each reading. Filed as EXP-001, the
    first dataset. The set is not the one the buy list planned; corrected in the buy list, shopping list and
    drawings' parts list (item 76). Agent's advice: no pieces under 2 g are needed. See
    [the session log](docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md).
  - Committed and pushed as `fd20afe`.
- 2026-11-19 to 2026-11-22: the same session, continued after its first `/wrap`.
  - The owner pushed a ready-made PH 2.0 cable onto the SDP810's pins (a stiff fit; not powered yet; open question 19).
  - Questions answered (advice only): another builder's sensor mounting from a video frame (pressure fittings through
    the box wall, so nothing pulls on the sensor; not the same sensor as ours); the load-cell wire colours match the
    HX711 pad names directly; the cell's own 110 mm wires can reach an HX711 placed beside it, so the TUOFENG wire is for
    the HX711-to-Arduino cable; the calibration is done through the HX711, on the finished balance module.
  - **Reviewed the remaining papers** at the owner's request: Barlow1999 chapters 4, 6, 7, 9, 10 and §§12.1–12.3,
    Morel1975, Anthoine2004 and Bradshaw1964, with notes and owner checklists; ten proposals listed in TODO P1 for
    decision (findings in §11). See [the session log](docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md).
  - Committed and pushed as `604ee42`.
- 2026-11-22/23: sensor bring-up on the breadboard.
  - `/catchup`: `UP_TO_DATE` at `604ee42`.
  - The owner soldered a female header to the HX711 and one TAL221 to its pads (after a resistance check), spliced the
    SDP810's cable to jumpers and wired every sensor as sheet 12, with advice on soldering (700 °F; tip tinning),
    jumpers, breadboard rows, pin numbering and C1.
  - The agent wrote four bring-up sketches in `firmware/` ([D-019](DECISIONS.md), Tentative). All passed: the I²C scan
    found 0x25 and 0x77 (chip ID 0x60); the HX711 runs at 10 SPS and a penny moves it about 33,300 counts; the SDP810
    reports scale 240, zeroes at −0.022 Pa and has the right sign; the BME280 reads 99.6 kPa, 23.3 °C and 44.5 % and
    responds. The BME280 reset under handling; the sketch now detects and recovers from that.
  - Four photos of the finished circuit compressed without GPS. See [the session log](docs/sessions/2026-11-23-sensor-bring-up.md).
  - Committed and pushed as `1ffd4a1`.
- 2026-11-23: the sensor shield PCB (design only; nothing ordered, built or tested).
  - `/catchup`: `UP_TO_DATE` at `1ffd4a1`.
  - The owner drew the Mega shield in KiCad 10 from its Arduino Mega shield template (`PCB/arduino_shield/`); the agent
    checked each save with `kicad-cli` on a copy. Fixed along the way: bare-chip symbols for the BME280 and HX711
    replaced by connectors; J1–J3 renumbered to each part's pin order (sheet 12's order would have put 5 V on the
    SDP810's SCL pin through a straight cable); a five-pin J3; parts kept off the Mega's USB and power-jack outlines;
    tracks kept off mounting holes and away from header pads.
  - Final ERC no errors, DRC 0 unconnected items; Gerbers re-exported with the outline and masks, checked and zipped for
    JLCPCB; not ordered ([D-020](DECISIONS.md)). The owner recalls using 1 µF for C1 on the breadboard.
  - At the wrap: sheet 12 redrawn as revision E. See [the session log](docs/sessions/2026-11-23-sensor-shield-pcb.md).
  - Committed and pushed as `f10f315`.
- 2026-11-24: the same session, continued after its first `/wrap`: confirmed the KiCad project is on GitHub; the owner
  found a printable TAL221 bench scale (Thingiverse, CC BY), which the agent checked against the TAL221 notes and filed
  in `cad/third-party/tal221-scale-bwilless/` (note on [D-017](DECISIONS.md)). Nothing printed.

## 7. Data and analyses

One dataset: [EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing), the calibration weights' masses (2026-11-19). No analysis beyond the means the sheet
computes. See [docs/data_catalog.md](docs/data_catalog.md). Bench checks of
the electronics, including the pasted sketch outputs of 2026-11-23, are in
[docs/experimental_setup.md](docs/experimental_setup.md#breadboard-as-built).

## 8. Results

| Result | Status | Source |
|---|---|---|
| True masses of the 14 calibration pieces and the hanging rod, each a mean of three readings, about ±0.01 g on the school balance; −2.5 % to +1.1 % off nominal | Preliminary result (the balance was not checked against a reference mass) | `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/`; [EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing) |
| Every sensor reads on the breadboard: I²C scan 0x25 + 0x77 (chip ID 0x60); SDP810 scale 240, zero −0.022 Pa (looped), correct sign; HX711 at 10 SPS, zero scatter 26 counts over 1.4 s, a penny step of about 33,300 counts; BME280 99.6 kPa, 23.3 °C, 44.5 %, responding | Verified for function only (no calibration) | Bench checks, 2026-11-23: [as built](docs/experimental_setup.md#breadboard-as-built); sketches in `firmware/` |
| Load-cell sensitivity about 13,300 counts per gram (0.62 mV/V) if the penny is 2.5 g; 10,700 (0.50 mV/V) if 3.11 g | Preliminary result (penny not weighed; taped mount) | Same |

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
- [docs/buy_list.md](docs/buy_list.md) §1 and §3 (2026-11-09): the S6-against-VEVOR comparison (top speed with lower
  VEVOR pressures and other loss factors, force, matched-Re range) and the 35 × 35 mesh's loss. Scripts in the
  [fan-advice log](docs/sessions/2026-11-09-fan-advice-and-screen-order.md#5-commands-and-scripts-executed).
- The [parts-ordering log](docs/sessions/2026-11-10-parts-ordering.md#6-measurements-and-results) (2026-11-09/10):
  the magnets' pull on screws at the balance, air heating by a light, the effect of humidity on density, press-fit
  interference for inch drill sizes, ball masses by material, and solder lengths for small calibration masses.
- The [time-estimates log](docs/sessions/2026-11-17-time-estimates-and-cad.md#6-measurements-and-results)
  (2026-11-15): CAD hours by part, the owner's hours by build stage, printer time and calendar time at assumed weekly
  hours.

## 9. Bugs, equipment issues, blockers

- **Blocked:** the tunnel's physical build waits on sizing (build step 1). The parts are here (every ordered part
    arrived by 2026-11-17); the arrival checks need no sizing and are under way, and
    the electronics bring-up ([walk-through](docs/electronics_walkthrough.md) §6, steps 1–3) is done (2026-11-23). The fan is bought last.
  - The buy list is complete ([docs/buy_list.md](docs/buy_list.md)); orders are tracked in
    [docs/shopping_list.md](docs/shopping_list.md).
  - Only the fan waits on a decision: S6 or VEVOR, on the owner's budget (D-011). The agent recommends the S6. The
    owner will buy it last, when the prints are ready (2026-11-10), but the model is needed before the fan stand is
    designed.
  - Still to report: the filament amounts on hand (PLA, PETG-CF), and which "check house" items are at home (power
    strip, sealant, glue and epoxy, heat-shrink, solder, steel rule, files, hacksaw, tin snips).
  - The microcontroller is no longer a blocker: the board works (2026-11-02, §3).
- **The shield PCB order waits on two measurements** (2026-11-23): C1's lead spacing and C2's diameter and lead spacing
  must match the placeholder footprints (5.0 mm; 5 mm and 2.0 mm) before the Gerbers are uploaded (TODO P0).
- Still open (2026-11-23): the HX711's excitation voltage; the penny's mass; the Adafruit library version; which
  capacitor is in the breadboard's C1 position (owner recalls 1 µF). Two resistors
  that look like R1 and R2 are still on the board (photos; harmless as pull-ups); whether the loose clipped wire near
  the Mega's power header was removed is not confirmed. Sheet 12 still shows the HX711 chip's pad names (TODO P2).
  Answered 2026-11-23: the RATE setting (10 SPS, from timing), the SDP810's pin order (by the moulded "1"; the scan and
  readings confirm it) and the BME280's wires (it reads).
- **Equipment issue (2026-11-23): the BME280 resets when its Dupont wiring is handled.** It then sleeps and repeats its
  reset values (71,853.4 Pa, 23.90 °C, 80.2 %). `bme280_read` now checks its mode and sets it up again, with a message.
  Fix: a firmer connection (a male header strip in the breadboard, the hanging bundle taped down; locking connectors on
  the PCB), and a reset flag in the logging firmware.
- Resolved by 2026-11-19: the owner's original photos (three with an EXIF GPS block) are out of the repo; only the
  compressed copies are committed.
- Resolved: the owner committed the 10.2 MiB sketch PDF uncompressed in `8fda08f` (under D-004's 25 MB limit). It stays
  in Git history.
- No known software bugs.
- Watch: at the 2026-11-02 `/wrap` the test suite took about 28 minutes (1,662.7 s) instead of the usual 13–16 s, and
  all 20 tests still passed. Cause unknown, not investigated. If it recurs, run the tests with `-v` to see which one
  stalls ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md#8-errors-failed-approaches-and-troubleshooting)).
  It has not recurred since: 20 tests in 7.9–21.9 s at every run from 2026-11-02 to 2026-11-19.
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
     the SDP810 takes 2.7–5.5 V with I²C up to VDD + 0.3 V (datasheet), and the Waveshare BME280 has an onboard level translator (maker's page).
     To confirm on the breadboard. **Answered 2026-11-23:** both answer on pins 20/21 at 5 V (scan 0x25 and 0x77) and
     read correctly;
   - **Answered from photos, 2026-11-18:** the board has the R3 layout, with pins marked SDA1 and SCL1 beside AREF.
     Keep using pins 20/21 until the two are shown by continuity to be joined. **2026-11-23:** the shield PCB joins
     SDA1/SCL1 to pins 20/21 in copper, so the continuity check is no longer needed for the shield.
   - **2026-11-17:** the wiring is drawn (sheet 12, [D-018](DECISIONS.md)). Waveshare's schematic shows the level
     translator with 4.7 kΩ pull-ups to VCC, so the board's SDA and SCL should sit at 5 V; to confirm on the
     breadboard (walk-through §6, step 1). An R3 board would let the shield PCB be Uno-sized.
2. **What is the op-amp signal conditioning for? Answered Tentatively 2026-11-17 ([D-018](DECISIONS.md)): nothing.**
   Proposed (agent, 2026-11-01): nothing in the measurement chain.
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
   - the solid-blockage formula (confirm in Barlow1999 ch. 9–10). **2026-11-22:** Barlow gives Thom's
     K V/C^{3/2} with K = 0.96 for bodies of revolution, but no chart covers a sphere; the total correction is worked
     out in the [Barlow1999 notes](resources/notes/Barlow1999.md), ch. 10, and is ready to propose for decision;
   - whether Maskell's flat-plate theory holds for a sphere (Maskell §2.6 flags rounded bodies). Proposed check:
     two sphere sizes;
   - θ for a sphere (1.85–2.8 across the cases in the sources);
   - Anthoine2004 (cylinders) reviewed 2026-11-22: for 2-D cylinders no correction works in every flow regime, which
     matters only for a later cylinder test ([notes](resources/notes/Anthoine2004.md)).
9. **What else is on hand? Mostly answered.** Recorded:
   - 2026-11-01: the ECE kit, a multimeter, a soldering station, a bench power supply and a workbench;
   - 2026-11-08/09: 6 in calipers, a hand drill, a spirit level, 43 magnets (8 × 2 mm), PLA, PETG-CF, a
     hardened-steel nozzle, and access to a school lab balance.

   Still unknown:
   - other electronics the owner thinks they have;
   - the bench supply's maximum voltage and current (needed only for a 12 V DC fan);
   - the filament amounts, and which "check house" items are at home (power strip, sealant, glue and epoxy,
     heat-shrink, solder, steel rule, files, hacksaw, tin snips); not yet reported. Sandpaper, duct tape, screws,
     rubber feet and the scoring knife were bought instead (2026-11-09/10).
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
    **Confirmed 2026-11-22:** it is Barlow1999's standard method (Eq. 6.6). Refinements proposed from the reading (TODO
    P1): calibrate with the sting shield in place and at every speed, keep the S and E lines undisturbed during force
    runs, and place the E ring at least about 56 mm downstream of the contraction exit
    ([Barlow1999 notes](resources/notes/Barlow1999.md), ch. 6; [Morel1975 notes](resources/notes/Morel1975.md)).
11. **Fan speed control from the menu knob. No longer a goal (D-012, 2026-11-08):** there is no menu. The fan keeps
    its own controller, and the Arduino never switches mains. If the S6 is chosen, hobbyists report driving it with a
    10 V PWM signal on its UIS port (not confirmed; D-011).
12. **Model attachment and sting lock. Mostly answered 2026-11-09 ([D-015](DECISIONS.md)).** How the sphere fixes to
    the sting without twisting the load cell, and the form of the sting lock and overload stops.
    **Proposed 2026-11-08:**
    - each Delrin ball is press-fit onto its own 1/8 in brass stem (Delrin cannot be glued), drilled to the centre
      with a printed jig and the owner's hand drill;
    - the stem slides into a 5/32 in sleeve at the top of the sting (**dropped 2026-11-09:** each ball now gets its
      own full-length 1/8 in sting, swapped whole, since D-015 lifts the sting out anyway; [D-016](DECISIONS.md), Tentative);
    - stops set at about 120 g.

    **Owner, 2026-11-09 (D-015):** the sting lock is a printed mount on the cell's top end with a hand screw that
    clamps the sting; the sting is lifted out to change balls, and the separate hold-still pin is dropped. Still to
    size in build step 1: the hole fit and depth, the screw length (printed knob on a stainless M3 screw, or a bought
    thumb screw) and the stop gap.
13. **Screens and honeycomb: bought or printed, and which mesh?** Added 2026-11-02. **Mostly answered 2026-11-09:**
    aluminium window insect screen (18 × 16 mesh, 66–69 % open, about $10 a roll), four or five screens, and a printed
    honeycomb (owner). Still open:
    - two or three diffuser screens. **2026-11-09:** the ordered roll is 0.011 in wire (maker's spec), so two just
      meet K_sum 2.1 (2.15); three are planned for margin, to be confirmed at sizing;
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
16. **What does the school lab balance read to? Answered 2026-11-19: 0.01 g** (CGOLDENWALL HZ50002B, capacity
    5000 g; owner). Added 2026-11-10. Every calibration mass is weighed on it, and the
    small check at 0.2–3 g needs about 0.001 g readability to know a 0.2 g mass to 1 %; at 0.01 g it is about ±5 %
    (our arithmetic). Owner to check the display or label. If it reads only to 0.01 g, use larger small masses or
    weigh several together.
    **2026-11-19:** 0.01 g is enough for the 2–50 g pieces (one step is 0.02–0.5 % of a piece). The set bought has no
    pieces under 2 g, and none are needed: the drag range (0.3–2.3 g) lies between the wind-off zero and the 2 g
    pieces, so the calibration interpolates (agent; [buy list](docs/buy_list.md) §9). The balance's own accuracy is
    unknown.
17. **Details to read off the delivered electronics. Mostly answered 2026-11-17/18 from photos:** the HX711 pad labels
    (by wire colour), the BME280 cable (6-pin plug to female Dupont sockets), and the Mega's R3 layout. The HX711's RATE
    setting: **10 samples/s** (2026-11-23, from the 95.5 ms reading interval). Still open: whether the Mega has its own
    I²C pull-ups (about 10 kΩ from pin 20 to 5V, measured unpowered with R1 removed).
18. **Which PCB program? Answered 2026-11-23: KiCad 10** (the owner drew the shield in it; [D-020](DECISIONS.md)). The
    connectors are 2.54 mm pin headers for jumper wires (owner). The history: added 2026-11-17. The agent recommended **KiCad**: free and open, text files that live in
    the repo, widely used at work, and it exports a STEP model of the board for Fusion 360. EasyEDA is easier and orders
    boards from JLCPCB in one click. Fusion 360's electronics workspace is a third option (the free licence's limits
    not checked). The owner's choice (TODO P2). Also open for the PCB: the J1–J3 connector type (Dupont pins on the
    breadboard; locking Grove/JST-style plugs likely on the PCB, ordered when needed; owner, 2026-11-17).
19. **How does the SDP810 connect?** Added 2026-11-18. Its pins are male, 0.5 mm wide at 2 mm spacing. The owner's PH2.0
    kit looks male too, so it will not mate. Agent's suggestion: a pre-crimped female 4-pin JST PH 2.0 cable. JST's
    contact is made for a 0.5 mm post at 2.0 mm pitch, but the fit on this sensor is unproven: only 2.7 ± 0.7 mm of pin
    projects, its thickness is not stated, nothing latches or keys the plug, and C1 would move to the breadboard end.
    Fallback: solder wires to the pins, as first planned. Owner's choice. **2026-11-19 (owner): the plug the owner bought
    for the SDP810 would not push onto its pins.** It is a ready-made 4-pin PH 2.0 cable with metal contacts in the
    holes (seller not recorded); its holes line up with the pins, so the pitch is right, but it cannot be pushed on by
    hand. **Later the same day the owner pushed it on: it is a stiff fit, not a misfit** ("it was just a bit hard to
    push"). So the SDP810 connects by this cable (Implemented, unverified): C1 moves to the breadboard end, and the
    plug has no key, so its orientation must be marked and each wire's pin confirmed against the datasheet's p. 4
    bottom view before power. The I²C scan finding 0x25 is the real test. The soldering advice given in between is
    no longer needed. **2026-11-23: works.** The cable's far ends are spliced to jumpers; the owner wired it by pin
    number from the moulded "1", the scan found 0x25, and the sensor zeroes and reads the right sign (Verified on the
    bench).

## 11. Important measurements and findings

Measurements so far: EXP-001 and the bench checks of 2026-11-18 and 2026-11-23 (§8). Literature findings that shape the
design are summarized in the notes under `resources/notes/`. Worth noting:

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
- **The panel magnets cannot pull measurably on screws at the balance** (2026-11-09; our dipole estimate, not
  measured). An 8 × 2 mm neodymium magnet makes about 90 µT at 60 mm and 19 µT at 100 mm. On an M3 × 10 screw at
  60 mm that is about 0.001 µN if weakly magnetic stainless and about 1 µN even if plain steel, about 1 % of the
  0.01 gf (98 µN) the balance aims to resolve; a steady pull also cancels in the wind-off zero. So stainless screws are
  used at the balance; the sting stays brass ([buy list](docs/buy_list.md) §4; script in the
  [session log](docs/sessions/2026-11-10-parts-ordering.md#5-commands-and-scripts-executed)). To check when built: the
  zero must not move when the top panel is lifted off and replaced.
- **The BME280 board needs no extra parts on the Mega's I²C bus** (2026-11-17;
  [Waveshare schematic notes](resources/notes/WaveshareBME280.md)). It carries 4.7 kΩ pull-ups to VCC on SDA and SCL and
  pulls ADDR and CS high, so R1 and R2 are not fitted and its address is 0x77, clear of the SDP810's 0x25. Confirmed
  on the bench 2026-11-23: SDA and SCL sit at 4.81 V and the scan finds 0x77.
- **The electronics run from the laptop's USB alone** (2026-11-17; our estimate): about 100 mA in all (Mega about
  50–80 mA, typical; SDP810 ≤ 5.5 mA; HX711 1.5 mA plus about 4.6 mA through the load cell; BME280 under 1 mA) against
  500 mA. A sagging supply cancels for the HX711 (ratiometric) and does not affect the two digital sensors. To check
  when built: the load-cell noise on battery against on the charger.
- **A pinout drawing's viewing side can reverse the order** (2026-11-18). The SDP8xx datasheet's p. 4 drawing is the bottom
  view and p. 12 the top view, so their pin orders run opposite ways. Reading the wrong one would swap VDD and GND.
- **The breadboard's power wiring works** (2026-11-18, owner's meter, Verified for this wiring only): 4.962 V at the left
  rails, the right rails and across C2, on the laptop's USB.
- **The calibration weights are up to 2.5 % off their stamped values** (2026-11-19, [EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing), Preliminary
  result). Both 20 g pieces are about 1.1 % light, both 5 g pieces 1.1 % heavy, one 2 g piece 2.5 % light. The errors go
  both ways, so they belong to the pieces, not to the balance's scaling. Stamped values would put up to about 1 % into
  the load cell's slope; the measured masses are used instead. Repeatability: about 0.008 g per reading.
- **Inside or outside the tunnel makes almost no difference to the BME280's readings** (2026-11-19; our estimate):
  at most about 0.15 % in pressure and under about 0.4 °C from fan heating, about 0.02 % in the reference C_D. Its
  big job is the SDP810's ×966 mbar / p_amb correction (about 5 %), which needs only room pressure.
- **From the 2026-11-22 paper reviews** (literature, not measurements; [Barlow1999](resources/notes/Barlow1999.md),
  [Bradshaw1964](resources/notes/Bradshaw1964.md), [Morel1975](resources/notes/Morel1975.md),
  [Anthoine2004](resources/notes/Anthoine2004.md); owner check pending):
  - **The sting's drag cannot be found by running the sting without the ball.** Tare plus interference is measured with
    an image (mirror) support; Barlow puts it at 10–50 % of an airplane's minimum drag. Our estimate for the shielded
    sting is 8–16 % of the 3/4 in ball's drag.
  - **The planned S − E airspeed method is the textbook method** (Barlow Eq. 6.6). Bradshaw warns that in very small
    tunnels its factor may vary with speed, so it is calibrated at every speed (already planned), with the sting shield
    in place.
  - **The home-made probe's angle tolerance is smaller than assumed:** a square-nosed tube starts to read low near 8°,
    not ±10°.
  - **Sphere blockage, worked out:** about +3.9–4.0 % in q for the 3/4 in ball and +7.4–7.8 % for the 1 in ball (wake
    blockage about four-fifths of it); no published chart covers a sphere's solid blockage. Testing two sizes at the
    same Re is Barlow's own check of the corrections.
  - **Morel's contraction charts do not replace Bell1988 here:** their separation criterion assumes Re of order 10⁶; the
    settling chamber here runs at about 4 × 10⁴.

- **Every sensor works on the breadboard** (2026-11-23, owner's bench tests with the agent's sketches; Verified for
  function, [as built](docs/experimental_setup.md#breadboard-as-built)). The SDP810 zeroes at −0.022 Pa with its ports looped, inside its 0.08 Pa spec; the
  HX711's zero scatter (26 counts over 1.4 s, about 0.002 g by the rated output) is near the datasheet's floor and
  about 150 times smaller than the smallest expected drag (0.3 g); a penny gives about 33,300 counts, consistent with
  the TAL221's rated 0.6 ± 0.15 mV/V. None of this is a calibration.
- **Here the SDP810 factor 966 mbar / p_amb is about 0.970** (BME280: 99.6 kPa, 2026-11-23), so uncorrected readings
  would be about 3 % high on that day.
- **A BME280 that loses power for an instant goes to sleep and repeats its reset values** (2026-11-23), which look
  like plausible data (71,853.4 Pa, 23.90 °C, 80.2 %). Firmware must check its mode and flag resets.
- **A schematic's pin order is not the part's physical order** (2026-11-23, while drawing the shield). Sheet 12 numbered
  every connector 1 +5V, 2 GND, then signals, which is fine for loose jumpers; a plug-in cable keeps its wires in order,
  so a straight cable from that J1 would have put 5 V on the SDP810's SCL pin and ground on its VDD pin. The shield's
  connectors now follow each part's own order ([D-020](DECISIONS.md)).
- **The SDP8xx datasheet names no decoupling capacitor** (2026-11-23, text search of the PDF). The 0.1 µF on sheet 12
  was the agent's choice; the bench readings of 2026-11-23 were taken with what the owner recalls as 1 µF.

## 12. Highest-priority next steps

See [TODO.md](TODO.md) for the full list. In order:

1. **Owner:**
   - commit and push this session (commands in the
     [session log](docs/sessions/2026-11-23-sensor-shield-pcb.md#13-manual-git-commands-as-given-to-the-owner));
   - **measure the two capacitors** (C1's lead spacing; C2's diameter and lead spacing). If they fit the placeholder
     footprints, order the shield from JLCPCB with `PCB/arduino_shield/gerbers/` zipped; if not, swap the footprint,
     re-export and have the agent recheck (TODO P0). Also read the marking on the breadboard's C1;
   - **close the bring-up** (TODO P0): the penny's year or mass, the HX711's excitation voltage (RED to BLK), the
     Adafruit BME280 Library version, and which wire moved when the BME280 reset; mark the SDP810's High barb; firm up
     the BME280's connection; remove R1 and R2 or say to keep them;
   - say whether to start the sizing now (asked 2026-11-15), and, if you like, your hours a week and any deadline, to
     narrow the schedule estimate;
   - say whether to republish the drawings' private claude.ai copy, which still shows revision B; the repo copy is
     revision D (TODO P0);
   - say whether to shorten this file by moving its dated history (§6 and the history inside §2, §3 and §10) into the
     session logs; it is about 800 lines against CLAUDE.md's "concise snapshot" (raised at the 2026-11-10 catch-up);
   - say whether sizing should leave room for a cylinder test (a full-span rod on the balance; not planned; TODO P3);
   - send the agent the heat-set inserts' length and outside diameter;
   - report what is on hand: filament amounts (PLA, PETG-CF) and the "Check the house first" items in
     [docs/shopping_list.md](docs/shopping_list.md);
   - choose the fan, the S6 or the VEVOR, on budget (D-011; the agent recommends the S6), and record it as a new
     decision;
   - the screen has arrived: count 18 and 16 wires per inch, check one wire reads about 0.28 mm, store it flat;
   - check the values read from four documents (checklists at the end of the
     [SDP8xx](resources/notes/SDP8xx.md), [Sensirion2024](resources/notes/Sensirion2024.md),
     [TAL221](resources/notes/TAL221.md) and [WaveshareBME280](resources/notes/WaveshareBME280.md) notes);
   - still open from before: the settling-chamber spacing (open question 13), the bench supply's rating, and
     confirming D-003, D-004, D-006, D-007's open exit, D-016, D-018 and D-019.
   - when the boards arrive: solder the shield (the header strips on hand should cover its 99 pins) and test it (TODO P2);
   - optional, at the bench: print the TAL221 bench scale (base as is, pan upside down), mount the soldered cell and run
     a several-minute zero (TODO P0).
2. **Agent, with the owner at the bench: the combined logging sketch** (walk-through step 4, TODO P0): one CSV line per
   sample with every sensor and a flag column for BME280 resets and failed reads (D-019), then a 10-minute run with a
   steady sample rate.
3. **Agent, build step 1 (sizing):** detail the 100 mm tunnel with the parts now chosen.
   - Fan-to-chamber diffuser: Mehta1977, with two or three window-screen positions.
   - Settling-chamber stack: printed honeycomb, two screens (open question 13).
   - Contraction, test section with S/E/M tap stations and the probe guide, the removable top panel with the 8 × 2 mm
     magnets, the two floor inserts (D-014), the removable balance module, sting shield, sting mount and lock
     (D-015), stops, and a small vented holder for the BME280 (2026-11-19).
   - Settle the drawing findings (open question 15), starting with the settling-chamber spacing and how the 250 mm
     sections split.
   - Then recompute the [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget), the fan pressure (with the screen
     losses in [buy list](docs/buy_list.md) §3) and the filament amount, and update the drawings: the numbers in
     `docs/drawings/wtdata.py`, then `python docs/drawings/page.py` ([README](docs/drawings/README.md)).
   - Deliver the results as one dimension sheet per printed part and the contraction wall as a points file, for the
     owner's CAD in Fusion 360 ([D-017](DECISIONS.md)).
4. **Owner, after sizing:** CAD each part (estimate 12–25 h), print test coupons (insert holes, magnet pockets, sting
   hole, fan ring) before the large parts; the agent checks the exported STLs on request.
5. **Owner, with the agent:** check the 2026-11-22 paper notes against the PDFs (checklists at the end of each notes
   file), and decide which of the ten proposals from that reading to adopt (TODO P1; several affect the sizing and the
   CAD: the image sting, the sealed load-cell box, the E-ring and last-screen positions, the diffuser screen lands).
6. **Owner:** download the remaining electronics datasheets (Bosch BME280, LM741/LM348/LMC6484) and the chosen fan's
   manual.
7. **Owner, remaining equipment checks** (TODO P2): the spare TAL221's resistances, a several-minute load-cell zero on a
   firm mount (the bench scale, 2026-11-24), the Mega's own I²C pull-ups, the calipers, the screen and the 2026-11-10 items. (Done 2026-11-23: the
   soldered TAL221's resistances, the BME280's 5 V check and chip ID, the SDP810's zero, the HX711's rate.)

## 13. Repository

- Local path: `C:\Users\nuhbm\OneDrive\Desktop\nuhs projects\2 - Wind Tunnel`
- Remote: `origin` → https://github.com/nuhshaheer/wind-tunnel (private; holds `cc51fff`, `5bc60f0`, `b710093`,
  `7db221f`, `9b42a07`, `748dae9`, `8fda08f`, `c04de1b`, `b22a45b`, `36f39eb`, `d7f5cdf`, `0351407`, `b08a151`,
  `0558370`, `507f71c`, `c768e2c`, `f4fa904`, `f5616a3`, `2ac0809`, `5cb8b7a`, `ce69a57`, `8904785`, `ff2ac6e`, `fd20afe`, `604ee42`, `1ffd4a1` and `f10f315`). The account was `nuhshaheer-2007` until
  2026-11-02, and the old URL redirects. The local `origin` points at the new URL (checked 2026-11-02, 2026-11-15, 2026-11-17, 2026-11-18, 2026-11-19, 2026-11-22 and 2026-11-23).
- Branch: `main`
