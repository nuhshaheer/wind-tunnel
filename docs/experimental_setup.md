# Experimental Setup

The physical setup as it actually exists. **Unknown** means not yet decided or not yet recorded. Do not replace it
with a guess. When the setup changes, update the **Current configuration** and add a row to the **Change history**.

**Current configuration as of 2026-11-07: nothing built.** Decided so far: an open-circuit blower with the fan at the
front ([D-007](../DECISIONS.md)) and a 100 mm × 100 mm test section ([D-008](../DECISIONS.md)). Parts on hand are
listed in [Parts on hand](#parts-on-hand): the owner's ECE kit (from its packing list), an Elegoo Mega 2560
(working: Blink upload Verified 2026-11-02), magnets, and tools (multimeter, soldering station, bench power supply). The owner's first sketch is in
[docs/sketches/](sketches/README.md).

## Tunnel geometry

| Parameter | Value | Status / source |
|---|---|---|
| Tunnel type (open-circuit blower / suck-down / closed-return) | Open-circuit blower, fan at the front. Proposed order: fan → flexible coupling → wide-angle diffuser with screens → settling chamber → contraction → test section → open exit | Accepted 2026-11-01 ([D-007](../DECISIONS.md)); open exit Tentative |
| Inlet / settling chamber size | Proposed: 250 mm × 250 mm (2.5 × the test section at contraction ratio 6.25). About 150–200 mm long with Mehta1979's 0.2 D screen spacing, or about 230–300 mm if screens are spaced for full turbulence decay (2026-11-02, [Mehta1977](../resources/notes/Mehta1977.md), [Scheiman1981](../resources/notes/Scheiman1981.md)) | Proposed 2026-11-01, updated 2026-11-02 ([estimate](../PROJECT_BACKGROUND.md#tunnel-length-budget)) |
| Contraction ratio and length | Proposed: 6.25 (250 mm → 100 mm square), about 250 mm long | Proposed 2026-11-01; build step 1 |
| Test section cross-section (W × H) | 100 mm × 100 mm | Accepted 2026-11-01 ([D-008](../DECISIONS.md)) |
| Test section length | Proposed: 270–290 mm (2.7–2.9 × its height, from the position rules) | Proposed 2026-11-01 ([estimate](../PROJECT_BACKGROUND.md#tunnel-length-budget)) |
| Diffuser | Wide-angle diffuser between the fan and the settling chamber: area ratio 3.44 (152 mm round → 250 mm square). With two screens (K_sum ≥ 2.1) it can be about 150–200 mm long, with curved walls or radiused corners and filleted corners, and no flow straightener at the fan outlet (2026-11-02, [Mehta1977](../resources/notes/Mehta1977.md)). Replaces the earlier 0.2–0.35 m estimate. No exit diffuser: open exit | Proposed / Tentative 2026-11-01, updated 2026-11-02 ([D-007](../DECISIONS.md)) |
| Overall length | About 1.15–1.3 m including a 6-inch fan (estimate). The 2026-11-02 diffuser and settling-chamber changes roughly cancel; recompute at sizing. Owner's target: about 1 m, more allowed | Estimate 2026-11-01 |
| Construction material | 3D-printed segments on the owner's Bambu Lab P1S, aligned with holes or pins and glued; filament unknown | Planned ([D-005](../DECISIONS.md)) |
| Model access | One test chamber; the top and/or side clear acrylic panel comes off to swap the model (owner's concept). Proposed details: 3–5 mm cast acrylic held by magnets, located by pins, flush inside, foam-gasketed; floor fixed; no magnets near ferrous parts of the balance; a sting lock and overload stops protect the load cell during swaps | Owner's concept 2026-11-01; details Proposed ([TODO.md](../TODO.md) P1 sizing task) |
| CAD / drawings | No CAD yet. The owner's hand sketch: [2026-11-01 concept sketch](sketches/README.md) | |

## Flow generation and control

| Parameter | Value | Status / source |
|---|---|---|
| Fan / blower model | Unknown. Proposed type: a 6-inch mixed-flow EC inline duct fan with a speed controller, on its own stand with a flexible coupling. For 13 m/s it should list about 400 CFM free air **and** about 500 Pa maximum static pressure (corrected 2026-11-05 from 300–500 Pa; [table](../PROJECT_BACKGROUND.md#top-speed-trade-off-proposed)). Candidates: AC Infinity Cloudline S6 (402 CFM, 503 Pa, $99) and VIVOSUN AeroZesh S6 (static pressure not published). Alternative: two Delta PFR1212UHE-SP00 12 V PWM server fans. The VEVOR 6-inch AC fan the owner found is unsuitable as listed (PROJECT_STATUS §3) | To buy; candidates 2026-11-01, updated 2026-11-05 ([TODO.md](../TODO.md) P0) |
| Motor and speed controller | Unknown. First build: the fan's own controller. Setting the speed from the Arduino menu needs a fan with a documented low-voltage control input (PWM or 0–10 V); the Arduino never switches mains | Proposed 2026-11-01 |
| Airspeed range | Unknown. Proposed (agent, 2026-11-05): a 13 m/s top speed, with validation runs from about 6.5 m/s. A 6-inch fan listing about 500 Pa should just reach 13 m/s in the 100 mm section (estimate; [trade-off](../PROJECT_BACKGROUND.md#top-speed-trade-off-proposed)) | Proposed; not confirmed by the owner |

## Flow conditioning

| Component | Value | Status / source |
|---|---|---|
| Honeycomb (cell size, length) | Unknown. Proposed (2026-11-02): thin-walled (paper, aluminium or drinking straws), cells about 2–3 mm, length 7–10 cell diameters, ahead of the screens in the settling chamber | To buy (README); [TODO.md](../TODO.md) P1 "Choose the screens and honeycomb" |
| Screens (number, mesh, open-area ratio) | Unknown. Proposed (2026-11-02): metal square-mesh at least 58 % open (for example 20–30 wires/in, 0.19–0.23 mm wire). Two in the fan-to-chamber diffuser (K_sum ≥ 2.1) and one or two in the settling chamber, at least 500 wire diameters apart. Expected K at the settling chamber's roughly 2 m/s is about 1.1–1.8 (extrapolated from [Wieghardt1953](../resources/notes/Wieghardt1953.md)) | To buy (README); [Scheiman1981](../resources/notes/Scheiman1981.md), [Mehta1977](../resources/notes/Mehta1977.md) |

## Instrumentation

| Measurement | Sensor | Range | Calibration | Location | Status |
|---|---|---|---|---|---|
| Airspeed | Pitot tube + differential pressure sensor | Unknown (±125 Pa proposed with the 13 m/s top speed, 2026-11-05) | None | Unknown | To buy (README) |
| Drag force | Load cell + HX711 | Unknown | None (planned: known weights) | Unknown | To buy (README) |
| Ambient pressure | Not chosen (candidate: Bosch BME280) | | | | Planned, TODO P1 (needed for ρ) |
| Ambient temperature | Not chosen (candidate: Bosch BME280) | | | | Planned, TODO P1 (needed for ρ) |
| Airfoil angle of attack | Preset angles (owner, 2026-11-01), not a servo. Proposed: an indexed hub with a pin and holes at set angles | | | | Planned, build step 7 |

Signal conditioning parts on hand: see [Parts on hand](#parts-on-hand). Circuit: not designed. Proposed 2026-11-01:
digital sensors (HX711, I²C pressure sensor, BME280) with no op-amps in the measurement chain, on an interface board
the owner designs ([TODO.md](../TODO.md) P2).

HX711 chip facts, confirmed from the Avia datasheet rev. V2.0 ([notes](../resources/notes/HX711.md)): 24-bit ADC,
10 or 80 samples/s, channel A gain 128 or 64 (channel B fixed at 32), input noise 50 nV rms at gain 128 and 10 SPS.
The module (and so its excitation voltage and RATE wiring) is not chosen.

## Data acquisition

| Parameter | Value |
|---|---|
| Microcontroller / DAQ | Candidate: the owner's **Elegoo Mega 2560**, working. 2026-11-02: main chip ATMEGA2560 (owner); COM3, USB ID 2341:0042, serial number `13448474939351C0E828`; a modified Blink (200 ms delays) uploaded from Arduino IDE 2.3.10 with the AVR core 1.8.8, board "Arduino Mega or Mega 2560", and the "L" LED blinked faster. 5 V logic; I²C on pins 20 (SDA) and 21 (SCL) |
| Sample rate(s) | Unknown |
| Synchronization between pressure and force | Unknown |
| Logging format | Planned: CSV with units in column headers ([data/README.md](../data/README.md)), sent over USB to a laptop |
| Display and controls | Planned (owner, 2026-11-01): a display with a push-button rotary encoder (knob) and a menu like the Ender 3's. Proposed: a 20×4 character LCD with an I²C adapter (sharing pins 20/21 with the pressure sensor), encoder on interrupt pins 2/3 or 18/19, screen refreshed 2–5 times a second, in a control box separate from the load-cell box |

## Test models

| Model | Dimensions | Mount | Status |
|---|---|---|---|
| Validation sphere | Proposed: about 20 mm (3.1 % blockage); about 25 mm (4.9 %) as the second size, run at matched Re. Reference C_D: Brown and Lawler Eq. (19) at each run's Re, ±10 % ([D-009](../DECISIONS.md)) | Proposed: a non-magnetic sting about 80–90 mm long through a floor slot to an upright straight-bar load cell in a closed box under the floor (as in Weakly2024) | Planned |
| Airfoil | Unknown | Same sting, with a preset-angle adapter | Planned (after validation) |

## Parts on hand

Recorded 2026-11-01. Nothing here has been tested except the Mega 2560 board (2026-11-02).

| Item | Source | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | Owner, 2026-10-30 | Build volume 256 × 256 × 256 mm (manufacturer spec) |
| Elegoo Mega 2560 | Owner, 2026-11-01 ("that is what it looks like at least"); main chip ATMEGA2560 (owner, 2026-11-02) | **Working:** Blink upload Verified 2026-11-02 (see Data acquisition). A USB A-to-B cable that carries data is on hand. Whether the board is printed "R3" is not recorded |
| Magnets | Owner, 2026-11-01 | Type, size and strength unknown |
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
