# Experimental Setup

The physical setup as it actually exists. **Unknown** means not yet decided or not yet recorded. Do not replace it
with a guess. When the setup changes, update the **Current configuration** and add a row to the **Change history**.

**Current configuration as of 2026-11-10: nothing built; nearly every part ordered (2026-11-09/10), including the
aluminium window screen, the SDP810-125Pa, two TAL221 100 g load cells, the SparkFun HX711, the Waveshare BME280 and
four 8 × 12 in sheets of 1/8 in cast acrylic.
The fan is bought last. Order status: [shopping_list.md](shopping_list.md).**
- Decided so far:
  - an open-circuit blower with the fan at the front ([D-007](../DECISIONS.md));
  - a 100 mm × 100 mm test section ([D-008](../DECISIONS.md));
  - a 13 m/s target top speed ([D-010](../DECISIONS.md));
  - no display or knob ([D-012](../DECISIONS.md)).
- The fan is open between the AC Infinity S6 and the VEVOR VV-GDFJ-AC6 ([D-011](../DECISIONS.md)).
- Parts chosen and their prices: [buy_list.md](buy_list.md); the owner's tracker of what is still to buy:
  [shopping_list.md](shopping_list.md).
- Parts on hand: [Parts on hand](#parts-on-hand).
- The owner's sketches: [docs/sketches/](sketches/README.md).

## Tunnel geometry

| Parameter | Value | Status / source |
|---|---|---|
| Tunnel type (open-circuit blower / suck-down / closed-return) | Open-circuit blower, fan at the front. Proposed order: fan → flexible coupling → wide-angle diffuser with screens → settling chamber → contraction → test section → open exit | Accepted 2026-11-01 ([D-007](../DECISIONS.md)); open exit Tentative |
| Inlet / settling chamber size | Proposed: 250 mm × 250 mm (2.5 × the test section at contraction ratio 6.25). About 150–200 mm long with Mehta1979's 0.2 D screen spacing, or about 230–300 mm if screens are spaced for full turbulence decay (2026-11-02, [Mehta1977](../resources/notes/Mehta1977.md), [Scheiman1981](../resources/notes/Scheiman1981.md)). **2026-11-09:** with the chosen window screen and 6 mm printed cells, full-decay spacing gives about 380–390 mm plus frames ([PROJECT_STATUS](../PROJECT_STATUS.md) open question 15); settle at sizing | Proposed 2026-11-01, updated 2026-11-02 and 2026-11-09 ([estimate](../PROJECT_BACKGROUND.md#tunnel-length-budget)) |
| Contraction ratio and length | Proposed: 6.25 (250 mm → 100 mm square), about 250 mm long | Proposed 2026-11-01; build step 1 |
| Test section cross-section (W × H) | 100 mm × 100 mm | Accepted 2026-11-01 ([D-008](../DECISIONS.md)) |
| Test section length | Proposed: 270–290 mm (2.7–2.9 × its height, from the position rules) | Proposed 2026-11-01 ([estimate](../PROJECT_BACKGROUND.md#tunnel-length-budget)) |
| Diffuser | Wide-angle diffuser between the fan and the settling chamber: area ratio 3.44 (152 mm round → 250 mm square). With two screens (K_sum ≥ 2.1) it can be about 150–200 mm long, with curved walls or radiused corners and filleted corners, and no flow straightener at the fan outlet (2026-11-02, [Mehta1977](../resources/notes/Mehta1977.md)). **2026-11-09:** three window screens are planned for margin; two of the ordered 0.011 in wire give K_sum 2.15, just enough. Replaces the earlier 0.2–0.35 m estimate. No exit diffuser: open exit | Proposed / Tentative 2026-11-01, updated 2026-11-02 ([D-007](../DECISIONS.md)) |
| Overall length | About 1.15–1.3 m including a 6-inch fan (estimate). The 2026-11-02 diffuser and settling-chamber changes roughly cancel; recompute at sizing. Owner's target: about 1 m, more allowed | Estimate 2026-11-01 |
| Construction material | 3D-printed segments on the owner's Bambu Lab P1S, aligned with holes or pins. **Joints (owner, 2026-11-09):** bolted flanges, M3 screws into brass heat-set inserts, foam tape between the faces, screens clamped between the flanges in printed frames. Proposed: PLA shells and PETG-CF for clamped or loaded parts (both on hand, amounts unknown) | Planned ([D-005](../DECISIONS.md)); joints Accepted ([D-013](../DECISIONS.md)), sizes TBD; filament Proposed ([buy list](buy_list.md) §2) |
| Model access | One test chamber. **The top clear acrylic panel lifts off, held by magnets; the floor under the model is a replaceable insert:** a sphere insert carrying the sting hole and the sting shield, and a plain insert for model cars (owner, 2026-11-09). A removable side panel is still open. Proposed details: 1/8 in cast acrylic (four 8 × 12 in sheets ordered; owner, 2026-11-10) in a printed frame, located by pins or lips, flush inside, foam-gasketed; the inserts drop in from above onto a ledge, flush, on two pins; no magnets near ferrous parts of the balance; the sting lift-out and overload stops protect the load cell during swaps ([D-015](../DECISIONS.md)) | Accepted 2026-11-09 ([D-014](../DECISIONS.md)); details Proposed ([TODO.md](../TODO.md) P1 sizing task) |
| CAD / drawings | No CAD yet. A preliminary 2D drawing package (pre-sizing, not for manufacture): [docs/drawings/](drawings/README.md), 2026-11-09. The owner's hand sketches: [sketches](sketches/README.md) | Drawings Implemented; design Proposed |

## Flow generation and control

| Parameter | Value | Status / source |
|---|---|---|
| Fan / blower model | **Open between two ([D-011](../DECISIONS.md), Tentative since 2026-11-09):** AC Infinity CLOUDLINE S6, model AI-CLS6 ($99; 425 CFM, 503 Pa, EC motor, 10 speed levels; about 13.0–13.4 m/s estimated) or VEVOR VV-GDFJ-AC6 ($53.90; 400 CFM, 300 Pa seller's figures, AC motor; about 11.3 m/s). Own stand; the collar, wrapped in neoprene, slides into a printed inlet, sealed with duct tape ([buy list](buy_list.md) §1) | To buy (owner to choose on budget) |
| Motor and speed controller | The fan's own controller. No Arduino speed control (no menu since D-012); the Arduino never switches mains | Proposed 2026-11-01; updated 2026-11-08 |
| Airspeed range | **Target 13 m/s, validation runs from about 6.5 m/s ([D-010](../DECISIONS.md), Accepted 2026-11-08).** The real top speed depends on the fan chosen (about 11–13.4 m/s, estimates) and is measured with the pitot | Accepted target; real range to be measured |

## Flow conditioning

| Component | Value | Status / source |
|---|---|---|
| Honeycomb (cell size, length) | **Printed (owner, 2026-11-08)**, for example 6 mm hexagonal cells with 0.4 mm walls, about 50 mm long, ahead of the screens in the settling chamber. Straws (about 5 mm, 40 mm long) are the upgrade if the flow map shows a problem. The 2026-11-02 proposal was thin-walled cells of about 2–3 mm, 7–10 diameters long | Printed, after sizing ([buy list](buy_list.md) §3) |
| Screens (number, mesh, open-area ratio) | **Proposed 2026-11-09: aluminium window insect screen ("bright aluminum", 18 × 16 mesh, wire about 0.010–0.011 in, 66–69 % open).** Two or three in the fan-to-chamber diffuser (K_sum ≥ 2.1; three if the wire is 0.010 in) and two in the settling chamber, at least 500 wire diameters apart. Estimated K about 0.75–0.85 at the fan outlet and 1.15–1.30 in the settling chamber; four or five screens lose about 33–48 Pa at 13 m/s (Wieghardt's formula; [buy list](buy_list.md) §3) | **Ordered 2026-11-09 (owner):** Saint-Gobain ADFORS FCS9222-M, Bright, 36 × 84 in roll; the maker's spec gives 18 × 16 mesh and 0.011 in wire, so 66.1 % open. With 0.011 in wire two diffuser screens just meet K_sum ≥ 2.1 (2.15); three are planned for margin (five in all). Wire count and diameter to be checked on arrival. [Scheiman1981](../resources/notes/Scheiman1981.md), [Mehta1977](../resources/notes/Mehta1977.md) |

## Instrumentation

| Measurement | Sensor | Range | Calibration | Location | Status |
|---|---|---|---|---|---|
| Airspeed | **One Sensirion SDP810-125Pa** with a home-made 1/8 in brass total-pressure probe and wall-tap rings at S, E and M ([buy list](buy_list.md) §5) | ±125 Pa (full scale at 14.4 m/s) | Planned: inclined water manometer for the gain; ×966 mbar / p_amb correction on every reading ([Sensirion2024 notes](../resources/notes/Sensirion2024.md)) | Probe − M at the model station; S − E (contraction drop) during force runs | Chosen 2026-11-08; **ordered 2026-11-09 (Mouser 403-SDP810-125PA, maker's part SDP810-125PA; confirmed from the order 2026-11-10)** |
| Drag force | **TAL221 100 g** straight-bar load cell (two bought, one spare) + **SparkFun HX711** | 100 g (safe overload 150 g) | Planned: budget weight set, each piece weighed on a school lab balance, balance module laid on its side | Upright under the ball, in the load-cell box under the floor. The sting stands in a printed mount on the cell's top end, clamped by the owner's thumb-screw sting lock ([D-015](../DECISIONS.md), 2026-11-09) | Chosen 2026-11-08; **ordered 2026-11-09 (SparkFun)** |
| Ambient pressure | **Waveshare BME280 Environmental Sensor** (onboard 3.3/5 V level translator per the maker; replaces the Adafruit 2652, owner 2026-11-09) | | | In room air near the fan inlet | Chosen 2026-11-08; **ordered 2026-11-09** |
| Ambient temperature | Same BME280 | | | | Chosen 2026-11-08; **ordered 2026-11-09** |
| Airfoil angle of attack | Preset angles (owner, 2026-11-01), not a servo. Proposed: an indexed hub with a pin and holes at set angles | | | | Planned, build step 7 |

Signal conditioning parts on hand: see [Parts on hand](#parts-on-hand). Circuit: not designed. Proposed 2026-11-01:
digital sensors (HX711, I²C pressure sensor, BME280) with no op-amps in the measurement chain, on an interface board
the owner designs ([TODO.md](../TODO.md) P2).

HX711 chip facts, confirmed from the Avia datasheet rev. V2.0 ([notes](../resources/notes/HX711.md)): 24-bit ADC,
10 or 80 samples/s, channel A gain 128 or 64 (channel B fixed at 32), input noise 50 nV rms at gain 128 and 10 SPS.
The module was chosen on 2026-11-08: the SparkFun HX711 breakout (SEN-13879), to buy. Its excitation voltage and RATE
wiring have not been checked against its schematic yet.

## Data acquisition

| Parameter | Value |
|---|---|
| Microcontroller / DAQ | Candidate: the owner's **Elegoo Mega 2560**, working. 2026-11-02: main chip ATMEGA2560 (owner); COM3, USB ID 2341:0042, serial number `13448474939351C0E828`; a modified Blink (200 ms delays) uploaded from Arduino IDE 2.3.10 with the AVR core 1.8.8, board "Arduino Mega or Mega 2560", and the "L" LED blinked faster. 5 V logic; I²C on pins 20 (SDA) and 21 (SCL) |
| Sample rate(s) | Unknown |
| Synchronization between pressure and force | Unknown |
| Logging format | Planned: CSV with units in column headers ([data/README.md](../data/README.md)), sent over USB to a laptop |
| Display and controls | **None ([D-012](../DECISIONS.md), owner, 2026-11-08):** all output on the laptop over USB (the Arduino IDE's Serial Plotter for a live view). Planned 2026-11-01 as a 20×4 LCD and knob menu; dropped |

## Test models

| Model | Dimensions | Mount | Status |
|---|---|---|---|
| Validation sphere | **Delrin (acetal) balls, 3/4 in (19.05 mm, 2.85 % blockage) and 1 in (25.4 mm, 5.07 %), ±0.001 in** (owner, 2026-11-08), run at matched Re (3/4 in at 13 m/s against 1 in at 9.75 m/s). Reference C_D: Brown and Lawler Eq. (19) at each run's Re, ±10 % ([D-009](../DECISIONS.md)) | Proposed: each ball press-fit on its own non-magnetic 1/8 in brass sting about 80–90 mm long, swapped whole (no 5/32 in sleeve since 2026-11-09); the sting passes inside a fixed, streamlined printed shield and a floor slot to an upright TAL221 in a closed box under the floor (as in Weakly2024) | Chosen; to buy |
| Airfoil | Unknown | Same sting, with a preset-angle adapter | Planned (after validation) |

## Parts on hand

Recorded 2026-11-01. Nothing here has been tested except the Mega 2560 board (2026-11-02).

| Item | Source | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | Owner, 2026-10-30 | Build volume 256 × 256 × 256 mm (manufacturer spec) |
| Elegoo Mega 2560 | Owner, 2026-11-01 ("that is what it looks like at least"); main chip ATMEGA2560 (owner, 2026-11-02) | **Working:** Blink upload Verified 2026-11-02 (see Data acquisition). A USB A-to-B cable that carries data is on hand. Whether the board is printed "R3" is not recorded |
| Magnets | Owner, 2026-11-01; count and size 2026-11-09 | **43, round, 8 mm × 2 mm**; probably neodymium (not confirmed); strength unknown |
| Digital calipers | Owner, 2026-11-08 | 6 in (150 mm) range; model and accuracy unknown; battery thought dead (button cell, LR44/SR44 size) |
| Hand drill | Owner, 2026-11-08 | Model unknown |
| Spirit level | Owner, 2026-11-08 | Size unknown |
| Filament and nozzle | Owner, 2026-11-09 | PLA and PETG-CF, amounts unknown; a hardened-steel nozzle for the P1S |
| School lab balance | Owner, 2026-11-08 (access) | Model and readability unknown; to be used once to weigh the calibration masses |
| Multimeter | Owner, 2026-11-01 | Model unknown |
| Soldering station | Owner, 2026-11-01 | Model unknown |
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

See [PROJECT_BACKGROUND.md](../PROJECT_BACKGROUND.md#known-sources-of-uncertainty). None quantified yet.

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
