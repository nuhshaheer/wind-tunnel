# Experimental Setup

The physical setup as it actually exists. **Unknown** means not yet decided or not yet recorded. Do not replace it
with a guess. When the setup changes, update the **Current configuration** and add a row to the **Change history**.

**Current configuration as of 2026-11-26: the tunnel is not built, but it is sized (build step 1, 2026-11-26;
D-022 to D-031; dimension sheets in [cad/sizing/](../cad/sizing/README.md)). The bench breadboard carries the whole sensor circuit:
the SDP810, the BME280 board and the HX711 with one TAL221 soldered to it, all wired as sheet 12 and each brought up
with its own test sketch in `firmware/` ([as built](#breadboard-as-built)). Since 2026-11-26 it matches the shield
exactly (C1 the 0.1 µF film capacitor, R1 and R2 removed), and the TAL221 sits on the printed
[bench scale](#bench-load-cell-scale-printed), where EXP-002 characterised it. Every part ordered on
2026-11-09/10 has arrived (owner, 2026-11-17; most arrival checks not done yet), including the
aluminium window screen, the SDP810-125Pa, two TAL221 100 g load cells, the SparkFun HX711, the Waveshare BME280,
four 8 × 12 in sheets of 1/8 in cast acrylic, the 3/4 in and 1 in Delrin balls and two 1/8 in brass rods for the
stings. The fan is bought last. Order status: [shopping_list.md](shopping_list.md). The sensor circuit is drawn and built on
the breadboard ([D-018](../DECISIONS.md), Accepted 2026-11-26; drawing package sheet 12; [walk-through](electronics_walkthrough.md)).
The shield PCB that replaces the breadboard is designed and **ordered (2026-11-26, JLCPCB, 5 boards)**, not yet
received ([shield PCB](#shield-pcb-ordered-not-received), [D-020](../DECISIONS.md)).**
- Decided so far:
  - an open-circuit blower with the fan at the front ([D-007](../DECISIONS.md));
  - a 100 mm × 100 mm test section ([D-008](../DECISIONS.md));
  - a 13 m/s target top speed ([D-010](../DECISIONS.md));
  - no display or knob ([D-012](../DECISIONS.md));
  - bolted flange joints ([D-013](../DECISIONS.md)); the top panel lifting off on magnets, and a replaceable floor
    insert under the model with the sting shield attached to it ([D-014](../DECISIONS.md)); a printed sting mount with
    a thumb-screw sting lock ([D-015](../DECISIONS.md)); one full-length sting per ball, no sleeve
    ([D-016](../DECISIONS.md), Accepted 2026-11-26).
- The sensor circuit ([D-018](../DECISIONS.md), 2026-11-17, Accepted 2026-11-26): laptop USB power; the SDP810 and BME280 on I²C
  pins 20/21; the HX711 on pins 2/3; breadboard first, then a shield PCB on the Mega. The shield
  ([D-020](../DECISIONS.md), owner, 2026-11-23): KiCad, jumper-wire headers in each part's pin order; ordered
  2026-11-26.
- The fan: the AC Infinity CLOUDLINE S6 ([D-025](../DECISIONS.md), 2026-11-26, supersedes D-011), bought last.
- The sizing (2026-11-26): 250 mm chamber and 250 mm 5th-order contraction (D-022); four-corner-piece split (D-023);
  310 mm test section with one window and a black wall, E and M taps (D-024); three-screen 175 mm diffuser (D-026);
  compact 275 mm chamber (D-027); sealed load-cell box with a door (D-028); image sting (D-029); probe through the
  open exit (D-030).
- Parts chosen and their prices: [buy_list.md](buy_list.md); the owner's tracker of what is still to buy:
  [shopping_list.md](shopping_list.md).
- Parts on hand: [Parts on hand](#parts-on-hand).
- The owner's sketches: [docs/sketches/](sketches/README.md).

## Tunnel geometry

| Parameter | Value | Status / source |
|---|---|---|
| Tunnel type (open-circuit blower / suck-down / closed-return) | Open-circuit blower, fan at the front. Proposed order: fan → flexible coupling → wide-angle diffuser with screens → settling chamber → contraction → test section → open exit | Accepted 2026-11-01 ([D-007](../DECISIONS.md)); open exit Accepted 2026-11-26 |
| Inlet / settling chamber size | **Sized 2026-11-26: 250 × 250 mm inside (D-022), 275 mm long with compact spacing (D-027; [sheet](../cad/sizing/settling_chamber.md)).** Earlier: 250 mm × 250 mm (2.5 × the test section at contraction ratio 6.25). About 150–200 mm long with Mehta1979's 0.2 D screen spacing, or about 230–300 mm if screens are spaced for full turbulence decay (2026-11-02, [Mehta1977](../resources/notes/Mehta1977.md), [Scheiman1981](../resources/notes/Scheiman1981.md)). **2026-11-09:** with the chosen window screen and 6 mm printed cells, full-decay spacing gives about 380–390 mm plus frames ([PROJECT_STATUS](../PROJECT_STATUS.md) open question 15); settle at sizing | Proposed 2026-11-01, updated 2026-11-02 and 2026-11-09 ([estimate](../PROJECT_BACKGROUND.md#tunnel-length-budget)) |
| Contraction ratio and length | 6.25 (250 mm → 100 mm square), 250 mm long, 5th-order wall; split at x = 82 mm ([sheet](../cad/sizing/contraction.md)) | Accepted 2026-11-26 ([D-022](../DECISIONS.md), [D-023](../DECISIONS.md)) |
| Test section cross-section (W × H) | 100 mm × 100 mm | Accepted 2026-11-01 ([D-008](../DECISIONS.md)) |
| Test section length | 310 mm: a 245 mm front body and a 65 mm extension; inside 100.3 mm square; E taps 56 mm in, ball at 206 mm ([sheet](../cad/sizing/test_section.md)) | Accepted 2026-11-26 ([D-024](../DECISIONS.md)); the 2026-11-01 proposal was 270–290 mm |
| Diffuser | **Sized 2026-11-26: 175 mm, three screens (D-026), S-curve loft, sharp corners ([sheet](../cad/sizing/diffuser.md)). Drawn 189 mm overall: the 175 mm curve with its two end flanges added on (owner kept it, 2026-11-26).** Earlier: wide-angle diffuser between the fan and the settling chamber: area ratio 3.44 (152 mm round → 250 mm square). With two screens (K_sum ≥ 2.1) it can be about 150–200 mm long, with curved walls or radiused corners and filleted corners, and no flow straightener at the fan outlet (2026-11-02, [Mehta1977](../resources/notes/Mehta1977.md)). **2026-11-09:** three window screens are planned for margin; two of the ordered 0.011 in wire give K_sum 2.15, just enough. Replaces the earlier 0.2–0.35 m estimate. No exit diffuser: open exit | Accepted 2026-11-26 ([D-026](../DECISIONS.md)); shape Proposed. Earlier: Proposed / Tentative 2026-11-01, updated 2026-11-02 ([D-007](../DECISIONS.md)) |
| Overall length | **About 1.40 m from the S6’s inlet to the open exit (estimate, CAD session 2026-11-26: the diffuser drawn 189 mm long, plus about 38 mm of screen frames and foam tape in the joints; note on [D-027](../DECISIONS.md)); tunnel axis 175 mm above the bench ([sheet](../cad/sizing/supports.md)).** At sizing (2026-11-26) it was given as about 1.34 m, without the joints. Earlier: about 1.15–1.3 m including a 6-inch fan (estimate). The 2026-11-02 diffuser and settling-chamber changes roughly cancel; recompute at sizing. Owner's target: about 1 m, more allowed | Estimate 2026-11-01 |
| Construction material | 3D-printed segments on the owner's Bambu Lab P1S, aligned with holes or pins. **Joints (owner, 2026-11-09):** bolted flanges, M3 screws into brass heat-set inserts, foam tape between the faces, screens clamped between the flanges in printed frames. Proposed: PLA shells and PETG-CF for clamped or loaded parts (both on hand, amounts unknown) | Planned ([D-005](../DECISIONS.md)); joints Accepted ([D-013](../DECISIONS.md)), sizes TBD; filament Proposed ([buy list](buy_list.md) §2) |
| Model access | **2026-11-26:** top panel over x 80–235 mm, one fixed window on the camera side and a black printed wall (D-024); floor inserts 60 × 70 mm; sealed load-cell box with a door (D-028); an image panel for the image runs (D-029). One test chamber. **The top clear acrylic panel lifts off, held by magnets; the floor under the model is a replaceable insert:** a sphere insert carrying the sting hole and the sting shield, and a plain insert for model cars (owner, 2026-11-09). A removable side panel is still open. Proposed details: 1/8 in cast acrylic (four 8 × 12 in sheets ordered; owner, 2026-11-10) in a printed frame, located by pins or lips, flush inside, foam-gasketed; the inserts drop in from above onto a ledge, flush, on two pins; no magnets near ferrous parts of the balance; the sting lift-out and overload stops protect the load cell during swaps ([D-015](../DECISIONS.md)) | Accepted 2026-11-09 ([D-014](../DECISIONS.md)); details Proposed ([TODO.md](../TODO.md) P1 sizing task) |
| CAD / drawings | **CAD in progress (2026-11-26):** the owner draws it in Fusion 360 from the dimension sheets and points files in [cad/sizing/](../cad/sizing/README.md) ([D-017](../DECISIONS.md)). Exported and checked so far, as 3MF in `cad/main cad files/`: the honeycomb, settling chamber C1 (whole), the whole diffuser (189 overall) and the fan inlet ring (socket 27 deep). The drawing package is at revision F and differs from the CAD in those two lengths ([drawings README](drawings/README.md)). A preliminary 2D drawing package (pre-sizing, not for manufacture): [docs/drawings/](drawings/README.md), 2026-11-09, revision D 2026-11-17 (revision C: no sleeve, stainless screws at the balance; revision D: electrical sheets 11–12, statuses On hand; sheet 12 at revision E since 2026-11-23). Also in `cad/`: a downloaded bench fixture, the TAL221 scale in `cad/third-party/` (printed 2026-11-26). The owner's hand sketches: [sketches](sketches/README.md) | Drawings Implemented; design Proposed |

## Flow generation and control

| Parameter | Value | Status / source |
|---|---|---|
| Fan / blower model | **AC Infinity CLOUDLINE S6, model AI-CLS6 ([D-025](../DECISIONS.md), Accepted 2026-11-26), bought last.** Earlier: open between two ([D-011](../DECISIONS.md), 2026-11-09): AC Infinity CLOUDLINE S6, model AI-CLS6 ($99; 425 CFM, 503 Pa, EC motor, 10 speed levels; about 13.0–13.4 m/s estimated) or VEVOR VV-GDFJ-AC6 ($53.90; 400 CFM, 300 Pa seller's figures, AC motor; about 11.3 m/s). Own stand; the collar, wrapped in neoprene, slides into a printed inlet, sealed with duct tape ([buy list](buy_list.md) §1) | To buy (owner to choose on budget) |
| Motor and speed controller | The fan's own controller. No Arduino speed control (no menu since D-012); the Arduino never switches mains | Proposed 2026-11-01; updated 2026-11-08 |
| Airspeed range | **Target 13 m/s, validation runs from about 6.5 m/s ([D-010](../DECISIONS.md), Accepted 2026-11-08).** The real top speed depends on the fan chosen (about 11–13.4 m/s, estimates) and is measured with the pitot | Accepted target; real range to be measured |

## Flow conditioning

| Component | Value | Status / source |
|---|---|---|
| Honeycomb (cell size, length) | **Sized 2026-11-26:** 249.4 mm square, 50 mm long, 6 mm cells, held by corner stops and spacers in chamber section C1, 25 mm after screen 12c ([sheet](../cad/sizing/settling_chamber.md)). **Printed (owner, 2026-11-08)**, for example 6 mm hexagonal cells with 0.4 mm walls, about 50 mm long, ahead of the screens in the settling chamber. Straws (about 5 mm, 40 mm long) are the upgrade if the flow map shows a problem. The 2026-11-02 proposal was thin-walled cells of about 2–3 mm, 7–10 diameters long | Printed, after sizing ([buy list](buy_list.md) §3) |
| Screens (number, mesh, open-area ratio) | **2026-11-26: three in the diffuser (D-026) and two in the chamber, 50 mm apart (D-027).** **Aluminium window insect screen ("bright aluminum", 18 × 16 mesh, 0.011 in wire per the maker, 66 % open; chosen 2026-11-09).** Three in the fan-to-chamber diffuser (planned for margin: two give K_sum 2.15, just over the 2.1 needed) and two in the settling chamber, at least 500 wire diameters apart. Estimated K about 0.75–0.85 at the fan outlet and 1.15–1.30 in the settling chamber; four or five screens lose about 33–48 Pa at 13 m/s (Wieghardt's formula; [buy list](buy_list.md) §3) | **Ordered 2026-11-09 (owner):** Saint-Gobain ADFORS FCS9222-M, Bright, 36 × 84 in roll; the maker's spec gives 18 × 16 mesh and 0.011 in wire, so 66.1 % open. With 0.011 in wire two diffuser screens just meet K_sum ≥ 2.1 (2.15); three are planned for margin (five in all). Wire count and diameter to be checked on arrival. [Scheiman1981](../resources/notes/Scheiman1981.md), [Mehta1977](../resources/notes/Mehta1977.md) |

## Instrumentation

| Measurement | Sensor | Range | Calibration | Location | Status |
|---|---|---|---|---|---|
| Airspeed | **One Sensirion SDP810-125Pa** with a home-made 1/8 in brass total-pressure probe and wall-tap rings at S, E and M ([buy list](buy_list.md) §5) | ±125 Pa (full scale at 14.4 m/s) | Planned: inclined water manometer for the gain; ×966 mbar / p_amb correction on every reading ([Sensirion2024 notes](../resources/notes/Sensirion2024.md)) | Probe − M at the model station; S − E (contraction drop) during force runs | Chosen 2026-11-08; **ordered 2026-11-09 (Mouser 403-SDP810-125PA, maker's part SDP810-125PA; confirmed from the order 2026-11-10)**; **on hand since 2026-11-17** |
| Drag force | **TAL221 100 g** straight-bar load cell (two bought, one spare) + **SparkFun HX711** | 100 g (safe overload 150 g) | Planned: balance module laid on its side, with the owner's weight set (50–2 g pieces and a hanging rod), each piece weighed on a school balance on 2026-11-19 ([EXP-001](data_catalog.md#exp-001-calibration-mass-weighing)); the measured masses are used, not the stamped ones. **Bench characterisation 2026-11-26 ([EXP-002](data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale), Preliminary):** 13,727.5 counts/g on the printed scale, straight within 0.025 g to 79 g; the zero (wander and lag 0.005–0.025 g) is the limit | Upright under the ball, in the load-cell box under the floor. The sting stands in a printed mount on the cell's top end, clamped by the owner's thumb-screw sting lock ([D-015](../DECISIONS.md), 2026-11-09) | Chosen 2026-11-08; **ordered 2026-11-09 (SparkFun)**; **on hand since 2026-11-17** |
| Ambient pressure | **Waveshare BME280 Environmental Sensor** (onboard 3.3/5 V level translator per the maker; replaces the Adafruit 2652, owner 2026-11-09) | | | In room air near the fan inlet, in its own open, vented printed holder away from the Arduino, the fan motor and lamps (proposed 2026-11-19); not inside the tunnel | Chosen 2026-11-08; **ordered 2026-11-09; on hand since 2026-11-17** |
| Ambient temperature | Same BME280 | | | | Chosen 2026-11-08; **ordered 2026-11-09; on hand since 2026-11-17** |
| Airfoil angle of attack | Preset angles (owner, 2026-11-01), not a servo. Proposed: an indexed hub with a pin and holes at set angles | | | | Planned, build step 7 |

Signal conditioning parts on hand: see [Parts on hand](#parts-on-hand). **Circuit: designed on paper 2026-11-17; breadboard
started 2026-11-18 and completed 2026-11-23, every sensor reading** ([D-018](../DECISIONS.md), Accepted 2026-11-26; drawing package sheets 11–12; [walk-through](electronics_walkthrough.md)):
the SDP810 and BME280 on I²C pins 20 (SDA) and 21 (SCL), the HX711 DAT and CLK on pins 2 and 3, C1 0.1 µF at the
SDP810 (as built: at the cable's breadboard end; a 1 µF electrolytic until 2026-11-26, then the kit's 0.1 µF film), C2 10 µF at the 5 V entry, no extra pull-ups (R1 and R2 removed from the breadboard 2026-11-26; the BME280 board has 4.7 kΩ to VCC on SDA and SCL,
[notes](../resources/notes/WaveshareBME280.md)), all powered from the laptop's USB. Proposed 2026-11-01:
digital sensors (HX711, I²C pressure sensor, BME280) with no op-amps in the measurement chain, on an interface board
the owner designs ([TODO.md](../TODO.md) P2).

HX711 chip facts, confirmed from the Avia datasheet rev. V2.0 ([notes](../resources/notes/HX711.md)): 24-bit ADC,
10 or 80 samples/s, channel A gain 128 or 64 (channel B fixed at 32), input noise 50 nV rms at gain 128 and 10 SPS.
The module was chosen on 2026-11-08: the SparkFun HX711 breakout (SEN-13879), ordered 2026-11-09, on hand since
2026-11-17. The owner's photo shows its pads labelled RED, BLK, WHT, GRN, YLW and VDD, VCC, DAT, CLK, GND. **RATE: the 10
samples/s setting**, found from the reading interval (95.5 ms, 2026-11-23; [as built](#breadboard-as-built)); the jumper
itself was not looked at. Excitation voltage (RED to BLK): not measured yet.

## Data acquisition

| Parameter | Value |
|---|---|
| Microcontroller / DAQ | Candidate: the owner's **Elegoo Mega 2560**, working. 2026-11-02: main chip ATMEGA2560 (owner); COM3, USB ID 2341:0042, serial number `13448474939351C0E828`; a modified Blink (200 ms delays) uploaded from Arduino IDE 2.3.10 with the AVR core 1.8.8, board "Arduino Mega or Mega 2560", and the "L" LED blinked faster. 5 V logic; I²C on pins 20 (SDA) and 21 (SCL) |
| Wiring and power | Planned 2026-11-17 ([D-018](../DECISIONS.md), sheet 12): SDA 20, SCL 21, HX711 DAT 2 and CLK 3; everything powered from the laptop's USB through the Mega's 5V pin (about 100 mA in all, estimate). **Breadboard complete 2026-11-23: all three sensors connected and answering** ([as built](#breadboard-as-built)) |
| Firmware | Bring-up sketches only, one per walk-through step ([firmware/README.md](../firmware/README.md)): `i2c_scan`, `hx711_raw_counts` (`AVERAGE_OVER = 1` since 2026-11-26), `sdp810_read`, `bme280_read` (2026-11-23; each run on the bench). No combined logging sketch yet (walk-through step 4) |
| Sample rate(s) | Bench values: HX711 about 10.5 readings/s, 95 ms apart (RATE at 10 SPS; steady over 32 min in EXP-002); SDP810 in continuous "average till read" mode, read every 100 ms by `sdp810_read`; BME280 read once a second by `bme280_read` (library default oversampling). The logging rate is not chosen yet |
| Synchronization between pressure and force | Unknown |
| Logging format | CSV with units in column headers ([data/README.md](../data/README.md)), sent over USB to the laptop. **Captured to a file by [`scripts/serial_capture.ps1`](../scripts/serial_capture.ps1)** ([D-021](../DECISIONS.md), 2026-11-26): every line kept, with the PC's time in a `pc_time` column. Close the Arduino IDE first (it holds COM3); opening the port resets the Mega |
| Display and controls | **None ([D-012](../DECISIONS.md), owner, 2026-11-08):** all output on the laptop over USB (the Arduino IDE's Serial Plotter for a live view). Planned 2026-11-01 as a 20×4 LCD and knob menu; dropped |

## Breadboard as built

**Status: complete as a bench circuit (2026-11-23).** The owner wired this on the ECE kit's breadboard: power and signal
rows on 2026-11-18, then every sensor on 2026-11-23, each tested (results below). The table is the 2026-11-18 power and
signal wiring; the sensor connections follow it. Row numbers are read from photos and may be off by one; check them on
the board.

| Connection | As built | Evidence |
|---|---|---|
| +5 V | Mega 5V → left + rail; left + → right + by a jumper at the bottom | Hole count in the photos; continuity; 4.962 V |
| GND | Mega GND (first of the two beside 5V) → left − rail; left − → right − at the bottom | Hole count in the photos; continuity; 4.962 V |
| C2 (10 µF, 50 V) | + leg in row 1 → + rail; other leg in row 6 → − rail | Photos; 4.962 V from row 1 to row 6. The stripe's side is seen only at an angle |
| SDA | Mega pin 20 → row 24 → jumper → right half, about row 23 | Photos; the wire's end at the Mega is hidden |
| SCL | Mega pin 21 → row 35 → jumper → right half, about row 39 | Photos |
| HX711 DAT | Mega pin 2 → right half, about row 32 | Photos |
| HX711 CLK | Mega pin 3 → right half, about row 33 | Photos |
| R1, R2 | Two 5.1 kΩ resistors, each from the + rail through a feed jumper to the SDA or SCL row | Photos. Sheet 12 marks them not fitted. **Removed by the owner on 2026-11-26**, with their two +5 V feed wires (removal of the wires implied by the owner's messages, not stated); the two wires carrying SDA and SCL to the right half stay (they are the bus) |
| C1 | Across the SDP810's VDD and GND at the cable's breadboard end | **1 µF electrolytic until 2026-11-26** (its marking, read by the owner); **since then the kit's 0.1 µF film capacitor** (108.9 nF on the owner's meter) |

**Bench checks, 2026-11-18** (owner's meter, model and accuracy Unknown; uncertainty not quantified; USB from the laptop
for the voltages). **Verified for this power wiring only:**

| Check | Condition | Result |
|---|---|---|
| + to − at C2 | USB unplugged, continuity | No beep |
| Left + to right +; left − to right − | USB unplugged, continuity | Beep on both |
| Left + to left − | Powered, DC volts | 4.962 V |
| Right + to right − | Powered, DC volts | 4.962 V |
| C2 row 1 to row 6 | Powered, DC volts | 4.962 V |
| BME280 cable, red to blue / yellow / orange / green | Unpowered, plugged into the board only | 4.605 / 4.617 / 4.597 / 4.617 kΩ |
| BME280 cable, black to blue | Unpowered, plugged into the board only | 145.3 kΩ |

Not done on 2026-11-18: the BME280's powered 5 V check, any I²C scan, and every SDP810, HX711 and load-cell test (all
done on 2026-11-23, below). Procedure and reasoning: [session log](sessions/2026-11-18-breadboard-power-and-part-checks.md).

**SDP810 cable (owner, 2026-11-19; Implemented, unverified).** A ready-made 4-pin JST PH 2.0 cable with metal contacts
in its holes (seller not recorded) is pushed onto the sensor's four pins. It is a stiff fit ("it was just a bit hard to
push"), not a misfit. As of 2026-11-19 it was not on the breadboard and had not been powered (it was wired and worked on
2026-11-23, below). The plug has no key, so before power:
mark its orientation, check the pins are straight, check by continuity that no neighbouring wires short, and match each
wire colour to its pin from the datasheet's p. 4 bottom view (owner to send a photo; the colour-to-pin map is
**Unknown**). C1 moves to the breadboard end of the cable. The I²C scan finding 0x25 is the real test
([PROJECT_STATUS](../PROJECT_STATUS.md) open question 19).

**HX711 header (owner, 2026-11-23; Implemented, unverified).** A 5-way **female** header socket is soldered on the
HX711 board's Arduino side (VDD, VCC, DAT, CLK, GND), so it connects with male-to-male jumpers and does not plug into
the breadboard (the walk-through's step 3 assumed male pins; either works). Soldered at about 700 °F (371 °C). The owner
reported checking it afterwards; the neighbouring-pin continuity results were not given as numbers. **TAL221 resistance
check at the free wire ends** (owner, 2026-11-23, before soldering): red–black and green–white "about" the datasheet's
1090 Ω and 1000 Ω; the exact readings were not recorded. The owner then soldered all four load-cell wires to the matching
pads (red → RED, black → BLK, white → WHT, green → GRN; YLW empty), 2026-11-23. Bridge check between neighbouring pads:
not yet reported. Test sketch for step 3: `firmware/hx711_raw_counts/hx711_raw_counts.ino` (written 2026-11-23 and run
the same day, below).

**Whole circuit powered, 2026-11-23** (owner's meter, model and accuracy Unknown; USB from the laptop). Everything wired
as sheet 12: BME280 (red +5 V, black GND, blue SDA, yellow SCL; orange ADDR and green CS open), HX711 (VDD and VCC
joined to +5 V, DAT to pin 2, CLK to pin 3), SDP810 by its PH 2.0 cable (the owner located pin 1 by the moulded "1" and
wired by pin number: 1 SCL, 2 VDD, 3 GND, 4 SDA), C1 at the breadboard end with its longer leg to +5 V (the owner later
recalled it is **1 µF, not 0.1 µF**, 2026-11-23: likely, since the kit's 1 µF parts are leaded electrolytics and its
0.1 µF parts mylar; marking not read). Whether R1 and
R2 are still fitted: Unknown. Power LED on.

| Check | Result |
|---|---|
| + rail to − rail | 4.947 V |
| SDA row to − rail | 4.814 V |
| SCL row to − rail | 4.815 V |

SDA and SCL sit high, so the BME280 board's pull-ups work (its step 1 check passes).

**I²C scan, 2026-11-23: Verified** (`firmware/i2c_scan/i2c_scan.ino`, uploaded from Arduino IDE 2.3.10, Serial
Monitor at 115200 baud; owner's pasted output):

```
Scanning...
  found 0x25  SDP810
  found 0x77  BME280 board? chip ID 0x60 = BME280, correct
```

Both sensors answer at their design addresses on one bus at 100 kHz, and the BME280's chip ID is 0x60 (a genuine
BME280, not a BMP280). The SDP810 answering also confirms its pin mapping and power. This verifies communication only;
neither sensor's readings are checked yet.

**HX711 first readings, 2026-11-23** (`firmware/hx711_raw_counts/hx711_raw_counts.ino`, first version: one line per
reading; owner's pasted output, 14 consecutive lines). The load cell was taped down at its wire end with the other end
overhanging (not clamped). The owner did a penny test during the run, but the 14 lines copied hold no step, so whether
the penny was on during them is Unknown; the Serial Monitor appears to copy only the visible lines.

| Quantity | Value | How found |
|---|---|---|
| Time between readings | 95–97 ms (mean 95.5 ms, 13 gaps) | `time_ms` column |
| Sample rate | about 10.5 readings/s, so the **RATE jumper is at the 10 samples/s setting** (open question 17) | 1000 / 95.5 ms; the datasheet's 10 SPS is nominal for the internal oscillator |
| Mean count | −14,818 counts | mean of 14 readings |
| Scatter | standard deviation 26 counts; 78 counts from lowest to highest | 14 readings over 1.4 s |
| Scatter in grams | about 0.002 g (0.0016–0.0027 g) | **estimate**, from the TAL221's rated 0.6 ± 0.15 mV/V (about 9,700–16,100 counts per gram, ratiometric); not a calibration |

Preliminary: 1.4 s of data only, so slow drift is not measured. The HX711 reads and its noise is near the datasheet's
floor (about 21 counts rms at 5 V excitation, gain 128, 10 SPS; our arithmetic). The sketch was then changed to print
the mean of 10 readings per line (`AVERAGE_OVER = 10`) so a whole penny test fits on screen.

**HX711 penny test, 2026-11-23: Verified that the load cell and HX711 read and respond** (walk-through §6 step 3 pass
criteria: steady with nothing on, a clear change with a penny, back on removal). Same sketch with `AVERAGE_OVER = 10`
(one line ≈ 955 ms, the mean of 10 readings). A first try was spoiled (owner: "i messed it up"; the copied lines moved
by at most 252 counts). For the run below the cell lay flat on its 12 mm face, taped only at its wire end, with the
rest overhanging; one US penny was set on the free end and lifted off by hand. Owner's pasted output:

```
78154,-14548
79109,-14654
80063,-14714
81017,-14789
81972,-14786
82926,-14803
83880,5259
84835,18887
85789,18479
86744,18425
87698,18454
88652,18535
89607,18018
90561,-8651
91515,-15094
92470,-14969
93425,-14869
94380,-14810
95334,-14825
```

| Quantity | Value | How found |
|---|---|---|
| Zero before | −14,793 counts | mean of the 3 lines before the penny (the first 3 were still drifting down, by about 250 counts over 3 s) |
| Penny on | +18,466 counts (standard deviation 277 between lines) | mean of the 6 full lines with the penny on; the lines at 83880 and 90561 ms are part-on, part-off and left out |
| **Step from the penny** | **about 33,300 counts** (33,259 against the zero before, 33,301 against the zero after) | difference of means |
| Return to zero | −42 counts (about 0.003 g) | mean of the 3 last lines minus the zero before |
| Counts per gram | about 13,300 if the penny is 2.5 g (US, 1983 or later), about 10,700 if 3.11 g (1982 or earlier, copper) | step / nominal penny mass. **The penny was not weighed and its year not recorded: Preliminary** |
| Implied rated output | about 0.62 mV/V (2.5 g) or 0.50 mV/V (3.11 g); datasheet 0.6 ± 0.15 mV/V | counts per gram ÷ (256 × 2²³ / 100 g), ratiometric |

Observed, not explained: after loading, the reading settled about 400 counts within a second and the last "on" line
fell about 450 counts more; after unloading it undershot by about 300 counts and recovered over about 3 s. Likely the
soft tape mount letting the bar sag and recover (not tested). Load-cell creep is to be measured on the real mount at the
calibration (build step 5). Still to do for step 3: the excitation voltage across the RED and BLK pads.

**SDP810 zero and direction, 2026-11-23: Verified that it reads, zeroes and has the right sign** (walk-through §6
step 2). `firmware/sdp810_read/sdp810_read.ino`: continuous mode 0x3615 (average till read), 10 reads 100 ms apart per
line, dp = raw / scale factor read from the sensor. **Not corrected for ambient pressure** (× 966 mbar / p_amb), which
does not matter at zero. Owner's pasted output:

- Start-up: `# scale factor read from the sensor: 240 counts per Pa (expected 240)`, so the part is the ±125 Pa one.
- **Zero, High and Low barbs joined by a short loop of the 1/8 in silicone tubing:** 8 lines over 8 s, dp −0.018 to
  −0.027 Pa (mean −0.022 Pa), sensor temperature 25.47–25.51 °C, 0 bad reads. Inside the datasheet's 0.08 Pa zero-point
  accuracy.
- **Direction:** a short tube on one barb, the owner breathing toward its open end from a few cm. High: up to +30.5 Pa
  (+14.5, +29.7, +25.6, +30.5, +29.0, +11.9 on the lines with breath). Low: down to −31.6 Pa (−5.8, −29.9, −25.4, −31.6).
  The owner identified High and Low this way.
- With the ports open between breaths the reading sat at −0.03 to −0.10 Pa (room air movement at the open ports), and
  the sensor's own temperature rose to 27.5 °C over about 2.5 min (its heater, hands and breath nearby; not air
  temperature).

Not verified: the span (3 % of reading in the datasheet), which needs the water-manometer calibration (buy list §9).

**BME280 readings, 2026-11-23** (walk-through §6 step 1, item 6). `firmware/bme280_read/bme280_read.ino` with the
Adafruit BME280 Library (version not yet recorded) at its default settings, one line per second. Owner's pasted
output, summarized:

| Period | Pressure | Temperature | Humidity | Notes |
|---|---|---|---|---|
| 0–10 s, untouched | 99,606.8–99,613.8 Pa | 23.23–23.31 °C | 44.4–44.6 % | `sdp_factor` = 96600 / p = 0.9697–0.9698 |
| 11–29 s, breath, then a fingertip on the chip | unchanged (99,606–99,620 Pa) | up to 26.26 °C | up to 78.2 % | both respond: step 1 item 6 passes |
| From 30 s | one line −12,878.8 Pa, 181.94 °C, 100 % | then 71,853.4 Pa, 23.90 °C, 80.2 % on every line for about a minute | | one more nonsense line at 49.6 s and one line of 90,476.4 Pa at 47.6 s |

**Verified** for the first 30 s: the board reads plausible room values and responds to breath and touch. Accuracy is
not checked against any reference.

**Failure from 30 s (kept for the record).** It began while the owner touched the board for the fingertip test (the
owner breathed and blew on the board and touched it during this run). Our
interpretation, not tested: the nonsense lines are failed reads (the bus read as all ones), and the frozen values are
the chip's power-on reset values. The chip appears to have lost power or reset, woke in sleep mode, and the library
went on reading the unchanged data registers. The most likely cause is a momentary contact loss on the BME280's
Dupont connections (VCC or GND); a static discharge from the fingertip is the other candidate. A wiggle test with the
updated sketch is to tell them apart.

**Re-test with the updated sketch, 2026-11-23** (after unplugging USB and reseating; owner breathed on the board,
wiggled wires and held a fingertip on it). Owner's pasted output, about 46–73 s after start:

- Pressure 99,616.0–99,633.4 Pa throughout; humidity rose to 85.4 % with breath; temperature rose to 31.43 °C with the
  fingertip (still rising at the end).
- At about 63 s the sketch printed `# BME280 not measuring (mode 0)` and set the chip up again; the next line
  (99,624.6 Pa, 26.93 °C, 82.9 %) and all after it were normal. Mode 0 means the chip answered on the bus but had
  reset to sleep mode, so SDA and SCL were connected at that moment; the likely cause is a brief loss of VCC or GND
  contact while wiggling, or a static discharge (not yet known which wire was being moved).

**BME280: Verified that it reads plausible values, responds to breath and touch, and that the sketch detects and
recovers from a chip reset.** Its Dupont connections are not reliable under handling: a firmer connection (a male
header strip in the breadboard, then the PCB's locking connectors, D-018) is needed, and the logging firmware must keep
the reset check and flag affected lines. Action: the owner to reseat the connections; the sketch now checks the mode bits
(register 0xF4) before each line and sets the chip up again, with a message, if it is not in normal mode. Lesson for
the logging firmware: check for this and log it, so a reset never passes as data.

Photos: [overview 1](images/2026-11-18_breadboard-overview-1.jpg), [overview 2](images/2026-11-18_breadboard-overview-2.jpg),
[C2 and R1](images/2026-11-18_breadboard-c2-and-r1.jpg), [signal rows](images/2026-11-18_breadboard-signal-rows.jpg).

Photos of the whole circuit, 2026-11-23 (owner's, taken after the tests; compressed copies without metadata):
[close-up](images/2026-11-23_breadboard-complete-closeup.jpg), [view 1](images/2026-11-23_breadboard-complete-1.jpg),
[view 2](images/2026-11-23_breadboard-complete-2.jpg), [from above](images/2026-11-23_breadboard-complete-top.jpg).
Seen in them: two resistors still on the board beside the SDA and SCL rows, which look like R1 and R2 (bands not
read), so they appear to be still fitted (harmless: pull-ups, and SDA and SCL read 4.81 V); the signal jumpers flagged
with masking tape (CLK, DAT, SDA, SCL); the SDP810 cable's joints wrapped in blue tape at staggered positions; the
BME280 at the end of a hanging bundle of jumpers; the load cell taped at the desk's edge with its free end overhanging.

**Breadboard brought to the shield's configuration, 2026-11-26** (owner at the bench; owner's pasted outputs;
[session log](sessions/2026-11-26-shield-order-and-load-cell-bench-test.md)). One change at a time, USB unplugged for
each:

| Change | Check | Result |
|---|---|---|
| C1: the 1 µF electrolytic replaced by the kit's 0.1 µF film capacitor | `i2c_scan` | 0x25 and 0x77, chip ID 0x60 |
| | `sdp810_read`, ports looped | −0.036 to −0.045 Pa, mean −0.042 Pa (18 lines); chip 24.4–24.9 °C; 0 bad reads |
| | tube off, a puff on each port | +17.5 to +46.6 Pa, then −3.0 to −82.3 Pa; 0 bad reads (taken as High then Low, the order asked) |
| R1 and R2 removed | `i2c_scan`; `sdp810_read`, ports looped | 0x25 and 0x77 (ID 0x60); −0.071 to −0.079 Pa, mean about −0.075 Pa (10 lines), chip 26.6–26.8 °C after the puffs; 0 bad reads |
| Their two +5 V feed wires removed | `i2c_scan` | 0x25 and 0x77 (ID 0x60) |

**Verified for function:** the 0.1 µF film works as C1, and the BME280 board's pull-ups alone carry the bus, as on the
shield. All three SDP810 zeros so far (−0.022, −0.042, −0.075 Pa) are inside the datasheet's ±0.08 Pa zero-point
accuracy; they differ by more than its 0.04 Pa repeatability, at different chip temperatures. The capacitor does not set
the zero.

## Shield PCB (ordered, not received)

**Status: Implemented, unverified (designed 2026-11-23; ordered 2026-11-26).** The owner drew a shield for the Mega in
KiCad 10 from KiCad's Arduino Mega shield template; it carries what the breadboard carries ([D-020](../DECISIONS.md),
[session log](sessions/2026-11-23-sensor-shield-pcb.md)). Files: `PCB/arduino_shield/` (design) and `PCB/arduino_shield/gerbers/` (manufacturing files).
**Ordered by the owner on 2026-11-26** from JLCPCB (order Y6-12005915A): 5 boards, FR-4 TG135, 2 layers, 1.6 mm, 1 oz,
green with white silkscreen, **OSP finish**, tented vias, flying-probe test, order mark removed; build 2 days, shipping
8–10 days (arrival about 6–8 December, estimate); price not recorded. Uploaded: the zip of `gerbers/` as committed in
`397c671` (checked byte for byte). The schematic's title block was filled in afterwards (revision 1); a KiCad
local-history restore the same night left the copper unchanged ([session log](sessions/2026-11-26-shield-order-and-load-cell-bench-test.md)).
OSP is bare copper under a thin organic coat: keep the boards sealed until soldering, solder within a few months, hold
them by the edges, and add flux if solder is slow to wet. Not received, built or tested.

| Item | As designed |
|---|---|
| Board | Full Mega outline, 101.6 × 53.34 mm; 2 copper layers, 1.6 mm; 0.25 mm tracks, 5 vias, no copper fill |
| To the Mega | The template's headers P1–P7 (all Mega pins; only 5V, GND, SDA/SCL beside AREF, 20/21, 2 and 3 are used, and the duplicate 5V, GND and I²C pins are joined in copper) and six 3.2 mm mounting holes |
| J1, SDP810 | 4-pin 2.54 mm header: 1 SCL, 2 +5V, 3 GND, 4 SDA (the sensor's own order) |
| J2, BME280 board | 4-pin 2.54 mm header: 1 +5V, 2 GND, 3 SDA, 4 SCL (the board's header order; ADDR and CS stay unconnected) |
| J3, HX711 board | 5-pin 2.54 mm header: 1 +5V (VDD), 2 +5V (VCC), 3 DAT (Mega pin 2), 4 CLK (pin 3), 5 GND (the board's header order) |
| C1 | 0.1 µF film beside J1, +5V to GND; footprint 5.0 mm lead spacing. **Checked 2026-11-26:** the kit's part (108.9 nF) has legs 6.5–6.7 mm apart, to be bent to 5.0 mm; the nearest other pad is 6.6 mm from its centre |
| C2 | 10 µF 50 V electrolytic by the Mega's 5V pin; footprint 5 mm diameter, 2.0 mm lead spacing. **Checked 2026-11-26:** lead spacing about 2.0 mm (owner); diameter not reported, but a can up to about 8 mm fits. + leg to +5V |
| R1, R2 | 5.1 kΩ pads for SDA and SCL pull-ups, marked "do not populate" |
| Silkscreen | Each connector's sensor and pin names; "By: Nuh Shaheer 2026" |
| Checks | Final ERC: 0 errors (69 warnings: the template's labels on unused pins). Final DRC with schematic parity: 0 unconnected items, 0 parity issues, 9 harmless warnings |

Jumper wires plug onto J1–J3 (male pins or female sockets fit the same holes; to choose at soldering). Every cable runs
pin 1 to pin 1. The breadboard stays the working circuit until the shield is made and passes the same checks: an I²C
scan finding 0x25 and 0x77 through it, and a steady HX711 zero.

## Bench load-cell scale (printed)

**Status: printed, assembled and used (2026-11-26).** A printed kitchen-scale fixture for the TAL221, to hold it firmly
on the bench before the balance module exists: "TAL221 Load Cell Scale" by Thingiverse user bwilless (thing:4665143,
Creative Commons Attribution), filed unchanged in `cad/third-party/tal221-scale-bwilless/` ([note on D-017](../DECISIONS.md)).

- **As printed (owner, 2026-11-26):** PLA, 20 % infill. Slicer estimates (not weighed): pan 9.34 g (9.42 g with
  supports, which were removed), base 9.40 g (9.48 g). The TAL221 soldered to the HX711 is screwed on, wire end on the
  base; screw lengths used not recorded.
- **The designer's settings** (Thingiverse page, as pasted by the owner): Anet A8, no raft, supports, 0.16 mm layers,
  25 % infill, PLA ("Polymaker Polyflex" given as the brand); **2 × M3 × 10 screws** fixing the cell to the base and
  **2 × M3 × 20 screws with nuts** fixing it to the top part.
- **Used for [EXP-002](data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale)** (2026-11-26): 0–79.44 g, pan
  plus masses at most about 89 g.

| Item | From the design files (not measured on a print) |
|---|---|
| Base | Horseshoe, 71 × 106 × 8.5 mm. The cell's fixed (wire) end screws onto a raised block: two Ø3.2 mm holes 6 mm apart, a 2.5 mm deep recess underneath for the screw heads |
| Pan | Ø60 mm, 15 mm tall, on the cell's free end: two Ø3.2 mm holes 6 mm apart through a 10 mm hub, a 5 mm deep recess on top for the screw heads. Print upside down (its underside is a shallow cone) |
| Fit to the TAL221 | Hole pairs 39.9 mm apart and a 6 mm gap between base and pan, matching the datasheet's 40 mm span and 6 mm thickness ([TAL221 notes](../resources/notes/TAL221.md)) |
| Screws | M3, about 10 mm (base, button or pan head) and 20 mm (pan, with nuts at an untapped end): estimates, to check with calipers |
| Load limit | The pan (about 7–17 g, estimate) rests on the cell all the time. Keep at most about 80 g on it and never press it: there is no overload stop, and the TAL221's safe overload is 150 g |

Uses: the several-minute no-load zero on a firm mount and calibration practice with the EXP-001 masses (both done in
EXP-002). Both are practice; the tunnel's calibration is done on the balance module.

## Test models

| Model | Dimensions | Mount | Status |
|---|---|---|---|
| Validation sphere | **Delrin (acetal) balls, 3/4 in (19.05 mm, 2.85 % blockage) and 1 in (25.4 mm, 5.07 %), ±0.001 in** (owner, 2026-11-08), run at matched Re (3/4 in at 13 m/s against 1 in at 9.75 m/s). Reference C_D: Brown and Lawler Eq. (19) at each run's Re, ±10 % ([D-009](../DECISIONS.md)) | Proposed: each ball press-fit on its own non-magnetic 1/8 in brass sting about 80–90 mm long, swapped whole (no 5/32 in sleeve since 2026-11-09; [D-016](../DECISIONS.md), Accepted 2026-11-26). The sting rises through the sting hole of the replaceable sphere floor insert, inside a streamlined printed shield attached to that insert, which lifts out with it once the sting is out ([D-014](../DECISIONS.md)); below the floor it stands in the printed sting mount on an upright TAL221 in a closed box (as in Weakly2024; [D-015](../DECISIONS.md)) | Chosen; **on hand since 2026-11-17** (one pack of 10 of each size, and the brass rods for the stings) |
| Airfoil | Unknown | Same sting, with a preset-angle adapter | Planned (after validation) |

## Parts on hand

Recorded 2026-11-01. Nothing here has been tested except the Mega 2560 board (2026-11-02); the calibration weights were weighed on 2026-11-19 (EXP-001).

| Item | Source | Notes |
|---|---|---|
| Every part ordered on 2026-11-09/10 (sensors and boards, screen, tubing and fittings, brass, balls, acrylic, fasteners, tools, PLA) | Owner, 2026-11-17 ("all of the packages i bought have arrived") | Listed in [shopping_list.md](shopping_list.md), marked Got it. **Most arrival checks not done yet**; the instruments are in the Instrumentation table above |
| Ribbon cable and connector kit (elechawk) | Owner's [photo](images/2026-11-17_ph2-ribbon-connector-kit.jpg), 2026-11-17 | 24 AWG 20-wire ribbon, PH2.0 "male" connectors 2P–8P, PH2.0 male crimp pins, heat-shrink. No crimp tool shown; quantities not counted |
| Bambu Lab P1S 3D printer | Owner, 2026-10-30 | Build volume 256 × 256 × 256 mm (manufacturer spec) |
| Elegoo Mega 2560 | Owner, 2026-11-01 ("that is what it looks like at least"); main chip ATMEGA2560 (owner, 2026-11-02) | **Working:** Blink upload Verified 2026-11-02 (see Data acquisition). A USB A-to-B cable that carries data is on hand. The 2026-11-18 photos show the R3 layout (IOREF; SDA1 and SCL1 beside AREF) |
| Magnets | Owner, 2026-11-01; count and size 2026-11-09 | **43, round, 8 mm × 2 mm**; probably neodymium (not confirmed); strength unknown |
| Digital calipers | Owner, 2026-11-08 | 6 in (150 mm) range; model and accuracy unknown; battery thought dead (button cell, LR44/SR44 size); an LR44 is on hand since 2026-11-17 |
| Hand drill | Owner, 2026-11-08 | Model unknown |
| Spirit level | Owner, 2026-11-08 | Size unknown |
| Filament and nozzle | Owner, 2026-11-09 | PLA and PETG-CF, amounts unknown; a hardened-steel nozzle for the P1S |
| School lab balance | Owner, 2026-11-08 (access); model 2026-11-19 | CGOLDENWALL HZ50002B, capacity 5000 g, d = 0.01 g (owner); calibration status Unknown. Used 2026-11-19 to weigh the calibration masses ([EXP-001](data_catalog.md#exp-001-calibration-mass-weighing)) |
| Calibration weight set | Owner, 2026-11-19 | Bought on Amazon (listing not recorded): 50, 2 × 20, 6 × 10, 2 × 5 and 3 × 2 g, plus a 10 g hanging rod; the multiples labelled #1, #2, ... on tape. Measured masses in [EXP-001](data_catalog.md#exp-001-calibration-mass-weighing) |
| Multimeter | A friend’s FNIRSI DST-201, borrowed (owner, 2026-11-26: "i have been using my friends so far"); an AstroAI 6000-count meter to buy | The bench readings since 2026-11-18 were taken on it |
| Soldering station | Owner, 2026-11-01 | Hakko FX-888DX with T18 tips (owner, 2026-11-26); an M3 heat-set insert tip (T18) to buy |
| Bench power supply | Owner, 2026-11-01 | Model, maximum voltage and current unknown |
| Workbench | Owner, 2026-11-01 ("a bench that I have access to") | Size unknown |
| ECE2010 Lab 2 kit (WPI) | Its packing list, scanned as `PartsListECE2010.pdf` (owner's Downloads folder, not in the repo) | Quantities below are the packed ones; the owner has not counted what remains |

ECE2010 Lab 2 kit, transcribed from the packing list ("#32WORMAECE2010", Worcester Polytechnic Institute, packaged by
RSR Electronics, Inc., Rahway, NJ; "100118-vn"):

| Group | Contents (quantity × value or part) |
|---|---|
| Resistors (1/4 W) | 2 × 10 Ω, 4 × 51 Ω, 4 × 100 Ω, 2 × 200 Ω, 2 × 300 Ω, 2 × 510 Ω, 2 × 750 Ω, 6 × 1 kΩ, 2 × 1.5 kΩ, 3 × 2 kΩ, 3 × 3 kΩ, 2 × 4.3 kΩ, 2 × 5.1 kΩ, 2 × 6.8 kΩ, 2 × 7.5 kΩ, 6 × 10 kΩ, 2 × 12 kΩ, 2 × 15 kΩ, 4 × 20 kΩ, 2 × 30 kΩ, 2 × 43 kΩ, 3 × 51 kΩ, 2 × 75 kΩ, 4 × 100 kΩ, 2 × 200 kΩ, 2 × 300 kΩ, 2 × 430 kΩ, 2 × 510 kΩ, 2 × 750 kΩ, 2 × 1 MΩ, 1 × 5.1 MΩ, 1 × 10 MΩ |
| Potentiometers (1/2 W) | 1 × 10 kΩ, 2 × 1 kΩ, 1 × 100 kΩ, 1 × 1 MΩ |
| Inductor | 1 × 33 µH |
| Diodes and LEDs | 4 × 1N4004, 4 × 1N4148/914, 1 × 1N5231B, 2 × 08L53RD red LED |
| Transistors | 4 × 2N2222A (PN2222), 4 × 2N3904, 2 × 2N3906, 2 × IRF520/521, 2 × IRF9520 |
| ICs | 2 × LM348N, 2 × LM741N, 1 × LM311N, 1 × LM317T, 1 × LM7805CT, 1 × 555, 1 × LMC6484 |
| Capacitors | 1 × 330 µF 25 V radial, 2 × 100 µF 25 V radial, 2 × 10 µF 50 V radial, 2 × 1 µF 50 V radial, 4 × 0.1 µF mylar, 4 × 0.01 µF mylar, 4 × 0.001 µF mylar; disc: 2 each of 5, 10, 33, 47, 75, 100, 150, 220, 470 and 680 pF |
| Miscellaneous | 03MB102 breadboard, 0602BNP1 pliers, 4" × 9" foam (1/4" thick), 2700WJW60B jumper wire kit, 060220 wire stripper, resistor colour-code card, 26MPFET microphone, 26SP08WR speaker with wires |

Not in the kit list: a multimeter, a soldering iron or a power supply (the owner has all three separately, see
above), or any load cell, HX711, pressure sensor or BME280.

## Operating procedure

Not written yet. Draft in [PROJECT_BACKGROUND.md](../PROJECT_BACKGROUND.md#measurement-and-analysis-approach-proposed)
(proposed: tare, wind-on average, wind-off zero, repeat; subtract mount drag).

## Known limitations and sources of error

See [PROJECT_BACKGROUND.md](../PROJECT_BACKGROUND.md#known-sources-of-uncertainty). The first one measured: the load
cell's zero wander and lag, about 0.005–0.025 g on the bench scale ([EXP-002](data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale),
Preliminary). The rest are not quantified yet.

## Change history

| Date | Change | Session log |
|---|---|---|
| 2026-10-29 | Document created; no hardware built | [2026-10-29](sessions/2026-10-29-github-setup-and-agent-handoff.md) |
| 2026-10-30 | Construction method recorded: segmented 3D printing on the P1S (D-005). Planning only; nothing built. Row added retrospectively on 2026-10-31 | [2026-10-31](sessions/2026-10-31-literature-review-and-design-inputs.md) |
| 2026-10-31 | HX711 chip specs confirmed from its datasheet (documentation only; no hardware change) | [2026-10-31](sessions/2026-10-31-reference-library-and-electronics.md) |
| 2026-10-31 | Ambient-sensor rows corrected from "Not planned yet" to the TODO P1 task and the BME280 candidate (documentation only; no hardware change) | [2026-10-31](sessions/2026-10-31-blockage-review-and-tunnel-concepts.md) |
| 2026-11-01 | Parts on hand recorded: the ECE2010 kit (from its packing list), the Elegoo Mega 2560 R3 and magnets. Proposals added for model access (magnetic acrylic panels), fan type, sting mounting and the interface board (documentation only; nothing built or tested) | [2026-11-01](sessions/2026-11-01-parts-review-and-kit-inventory.md) |
| 2026-11-01 | Blower with the fan at the front (D-007) and a 100 mm test section (D-008) decided. Added: proposed section sizes and lengths, fan candidates, display and knob, preset airfoil angles, load-cell protection; multimeter, soldering station, bench supply and workbench on hand (documentation only; nothing built or tested) | [2026-11-01](sessions/2026-11-01-parts-review-and-kit-inventory.md) |
| 2026-11-02 | Proposals updated from Mehta1977, Scheiman1981 and Wieghardt1953: diffuser length and screens, settling-chamber length, honeycomb and screen choices. Sphere reference set by D-009 (documentation only; nothing built or tested) | [2026-11-02](sessions/2026-11-02-cd-reference-and-flow-conditioning.md) |
| 2026-11-02 | Mega 2560 board tested: Blink upload Verified by the owner; Arduino IDE 2.3.10 installed. First hardware test; nothing built | [2026-11-03](sessions/2026-11-03-mega-2560-board-test.md) |
| 2026-11-05 | 13 m/s top speed proposed; fan requirement corrected (about 500 Pa listed at 400 CFM, not 300–500 Pa); fan candidates updated after the owner's search for a cheaper fan (documentation only; nothing bought, built or tested) | [2026-11-07](sessions/2026-11-07-top-speed-and-fan-search.md) |
| 2026-11-08/09 | Buy list written ([buy_list.md](buy_list.md)). Instruments chosen: SDP810-125Pa with a home-made probe, two TAL221 100 g with a SparkFun HX711, an Adafruit BME280. Also chosen: 3/4 in and 1 in Delrin balls, aluminium window screen and a printed honeycomb. Target 13 m/s (D-010); no display (D-012); fan open between the S6 and the VEVOR (D-011). Parts on hand updated (documentation only; nothing bought, built or tested) | [2026-11-09](sessions/2026-11-09-buy-list.md) |
| 2026-11-09 | Owner's shopping tracker added ([shopping_list.md](shopping_list.md)). Stale entries corrected: construction material (bolted flanges, PLA and PETG-CF) and the HX711 module (SparkFun, chosen 2026-11-08). Documentation only; nothing bought, built or tested | [2026-11-09](sessions/2026-11-09-shopping-list.md) |
| 2026-11-09 | Preliminary drawing package added ([drawings/](drawings/README.md)). Owner's decisions from a new sketch: bolted flange joints (D-013), the top panel on magnets and replaceable floor inserts (D-014), the sting mount and thumb-screw sting lock (D-015). Documentation only; nothing bought, built or tested | [2026-11-09](sessions/2026-11-09-drawing-package.md) |
| 2026-11-09 | First part ordered: the aluminium window screen (Saint-Gobain ADFORS FCS9222-M, Bright; 18 × 16, 0.011 in wire per the maker's spec, 66 % open); three diffuser screens planned (five in all). Nothing built or tested; the fan is still open (agent recommends the S6) | [2026-11-09](sessions/2026-11-09-fan-advice-and-screen-order.md) |
| 2026-11-09/10 | Parts ordered: everything on the buy list except the fan (bought last). Changes: Waveshare BME280 instead of the Adafruit; stainless screws at the balance instead of brass; one full-length sting per ball, no 5/32 in sleeve ([D-016](../DECISIONS.md), Tentative). Nothing arrived, built or tested yet | [2026-11-10](sessions/2026-11-10-parts-ordering.md) |
| 2026-11-10 | Order details recorded: four 8 × 12 in acrylic sheets; the SDP810 order confirmed as Mouser 403-SDP810-125PA. Stale settling-chamber and diffuser-screen entries updated. Documentation only; nothing arrived, built or tested | [2026-11-10](sessions/2026-11-10-order-details-and-cylinders.md) |
| 2026-11-10 | Consistency audit against the latest decisions (owner's request): the sphere mount now described through the replaceable floor insert with the shield attached (D-014) instead of "a fixed shield and a floor slot"; balls, sting rods and HX711 marked ordered; screens as ordered; drawings revised to C (no sleeve or separate stems, stainless screws at the balance). Documentation only; nothing arrived, built or tested | [2026-11-10](sessions/2026-11-10-consistency-audit.md) |
| 2026-11-17 | Every ordered part reported arrived (owner). Sensor circuit designed on paper: laptop USB power, one I²C bus for the SDP810 and BME280, the HX711 on pins 2/3, a shield PCB later ([D-018](../DECISIONS.md), Tentative; drawing package revision D, sheets 11–12; [walk-through](electronics_walkthrough.md)). Nothing wired or tested | [2026-11-17](sessions/2026-11-17-sensor-circuit-design.md) |
| 2026-11-18 | Breadboard started by the owner: Mega power, rails, C2 and signal rows wired, no sensor connected; rails and C2 read 4.962 V; BME280 cable checked by resistance; delivered boards' labels recorded | [2026-11-18](sessions/2026-11-18-breadboard-power-and-part-checks.md) |
| 2026-11-19 | Calibration weights weighed by the owner on the school balance (CGOLDENWALL HZ50002B, d = 0.01 g; EXP-001); the weight set recorded as bought. BME280 placement: room air near the fan inlet, in its own vented holder (proposed). Breadboard unchanged. After the wrap the owner pushed a ready-made PH 2.0 cable onto the SDP810's pins (stiff fit; not powered, colours not yet mapped to pins) | [2026-11-19](sessions/2026-11-19-bme280-advice-and-mass-weighing.md) |
| 2026-11-23 | Breadboard completed by the owner: female header on the HX711, one TAL221 soldered to it, the SDP810's cable spliced to jumpers (taped joints), the BME280 on jumpers, C1 at the breadboard end. Rails 4.947 V, SDA/SCL 4.81 V. Four bring-up sketches in `firmware/`; I²C scan found 0x25 and 0x77 (chip ID 0x60); HX711 penny step about 33,300 counts at 10 SPS; SDP810 zero −0.022 Pa, scale 240, correct sign; BME280 99.6 kPa, responds to breath and touch, reset once under handling (detected and recovered) | [2026-11-23](sessions/2026-11-23-sensor-bring-up.md) |
| 2026-11-23 | Shield PCB designed by the owner in KiCad (not made): jumper-wire headers J1–J3 in each part's pin order, five-pin J3, C1 beside J1, R1/R2 unfitted pads, full Mega size, Gerbers ready ([D-020](../DECISIONS.md); [shield PCB](#shield-pcb-ordered-not-received)). The owner recalls the breadboard's C1 is 1 µF. Sheet 12 redrawn as revision E. Breadboard unchanged | [2026-11-23 shield PCB](sessions/2026-11-23-sensor-shield-pcb.md) |
| 2026-11-24 | A printable TAL221 bench scale filed (Thingiverse thing:4665143 by bwilless, CC BY) in `cad/third-party/`; checked against the TAL221 notes; not printed ([bench scale](#bench-load-cell-scale-printed)) | [2026-11-23 shield PCB, continued](sessions/2026-11-23-sensor-shield-pcb.md) |
| 2026-11-26 | Breadboard brought to the shield's configuration: C1 changed from the 1 µF electrolytic to the 0.1 µF film; R1, R2 and their +5 V wires removed; scan, SDP810 zero and sign pass. Shield footprints confirmed and the shield ordered (JLCPCB, 5 boards, OSP). TAL221 bench scale printed and the soldered cell mounted on it; EXP-002 recorded through `scripts/serial_capture.ps1` with `hx711_raw_counts` at `AVERAGE_OVER = 1` | [2026-11-26](sessions/2026-11-26-shield-order-and-load-cell-bench-test.md) |
| 2026-11-26 | Sized (build step 1; design and documentation only, nothing built or tested): decisions D-022 to D-031, dimension sheets and Fusion points files in `cad/sizing/`, drawing package revision F. The S6 fan chosen. Tools recorded: the meter so far is a friend’s FNIRSI DST-201, the soldering station a Hakko FX-888DX; the M3 inserts are a Kadrick kit | [2026-11-26 build step 1](sessions/2026-11-26-build-step-1-sizing.md) |
| 2026-11-26 | First CAD exports (design only, nothing printed): the honeycomb, settling chamber C1, the whole diffuser and the fan inlet ring, drawn by the owner and checked by the agent from the meshes. Owner's changes kept: diffuser 189 overall (curve 175 plus end flanges), socket 27 deep; tunnel about 1.40 m long including the joints (estimate) | [2026-11-26 first CAD exports](sessions/2026-11-26-first-cad-exports-checked.md) |
