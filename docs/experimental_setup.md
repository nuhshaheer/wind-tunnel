# Experimental Setup

The physical setup as it actually exists. **Unknown** means not yet decided or not yet recorded. Do not replace it
with a guess. When the setup changes, update the **Current configuration** and add a row to the **Change history**.

**Current configuration as of 2026-11-01: nothing built.** Parts on hand are listed in [Parts on hand](#parts-on-hand):
the owner's ECE kit (from its packing list), an Elegoo Mega 2560 R3 (untested) and some magnets.

## Tunnel geometry

| Parameter | Value | Status / source |
|---|---|---|
| Tunnel type (open-circuit blower / suck-down / closed-return) | Unknown | Planned, build step 1 |
| Inlet / settling chamber size | Unknown | Planned |
| Contraction ratio and length | Unknown | Planned, build step 1 |
| Test section cross-section (W × H) | Unknown | Planned, build step 1 |
| Test section length | Unknown | Planned, build step 1 |
| Diffuser | Unknown | Planned |
| Construction material | 3D-printed segments on the owner's Bambu Lab P1S, aligned with holes or pins and glued; filament unknown | Planned ([D-005](../DECISIONS.md)) |
| Model access | Unknown. Proposed: removable clear acrylic panels (3–5 mm, cast) held by magnets, located by pins, flush inside, foam-gasketed; floor fixed; no magnets near ferrous parts of the balance | Proposed 2026-11-01 (owner's idea; [TODO.md](../TODO.md) P1 sizing task) |
| CAD / drawings | None yet | |

## Flow generation and control

| Parameter | Value | Status / source |
|---|---|---|
| Fan / blower model | Unknown. Proposed type: inline mixed-flow duct fan with a speed controller, on its own stand with a flexible coupling | To buy (README); type proposed 2026-11-01 ([TODO.md](../TODO.md) P1) |
| Motor and speed controller | Unknown | |
| Airspeed range | Unknown | Target not chosen |

## Flow conditioning

| Component | Value | Status / source |
|---|---|---|
| Honeycomb (cell size, length) | Unknown | To buy (README) |
| Screens (number, mesh, open-area ratio) | Unknown | To buy (README) |

## Instrumentation

| Measurement | Sensor | Range | Calibration | Location | Status |
|---|---|---|---|---|---|
| Airspeed | Pitot tube + differential pressure sensor | Unknown | None | Unknown | To buy (README) |
| Drag force | Load cell + HX711 | Unknown | None (planned: known weights) | Unknown | To buy (README) |
| Ambient pressure | Not chosen (candidate: Bosch BME280) | | | | Planned, TODO P1 (needed for ρ) |
| Ambient temperature | Not chosen (candidate: Bosch BME280) | | | | Planned, TODO P1 (needed for ρ) |
| Airfoil pitch actuator | Servo | Unknown | | | To buy (README), build step 7 |

Signal conditioning parts on hand: see [Parts on hand](#parts-on-hand). Circuit: not designed. Proposed 2026-11-01:
digital sensors (HX711, I²C pressure sensor, BME280) with no op-amps in the measurement chain, on an interface board
the owner designs ([TODO.md](../TODO.md) P2).

HX711 chip facts, confirmed from the Avia datasheet rev. V2.0 ([notes](../resources/notes/HX711.md)): 24-bit ADC,
10 or 80 samples/s, channel A gain 128 or 64 (channel B fixed at 32), input noise 50 nV rms at gain 128 and 10 SPS.
The module (and so its excitation voltage and RATE wiring) is not chosen.

## Data acquisition

| Parameter | Value |
|---|---|
| Microcontroller / DAQ | Candidate: the owner's **Elegoo Mega 2560 R3** (identified by appearance, 2026-11-01; not yet powered or tested; USB A-to-B cable on order). 5 V logic; I²C on pins 20 (SDA) and 21 (SCL) |
| Sample rate(s) | Unknown |
| Synchronization between pressure and force | Unknown |
| Logging format | Planned: CSV with units in column headers ([data/README.md](../data/README.md)) |

## Test models

| Model | Dimensions | Mount | Status |
|---|---|---|---|
| Validation sphere | Unknown diameter | Unknown. Proposed: a non-magnetic sting through a floor slot to an upright straight-bar load cell outside the tunnel (as in Weakly2024) | Planned |
| Airfoil | Unknown | Servo pitch mechanism | Planned (after validation) |

## Parts on hand

Recorded 2026-11-01. Nothing here has been tested.

| Item | Source | Notes |
|---|---|---|
| Bambu Lab P1S 3D printer | Owner, 2026-10-30 | Build volume 256 × 256 × 256 mm (manufacturer spec) |
| Elegoo Mega 2560 R3 | Owner, 2026-11-01 ("that is what it looks like at least") | Not yet powered or tested; USB A-to-B cable missing, owner ordering one |
| Magnets | Owner, 2026-11-01 | Type, size and strength unknown |
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

Not in the list: a multimeter, a soldering iron, a power supply, any load cell, HX711, pressure sensor or BME280.

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
