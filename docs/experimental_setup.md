# Experimental Setup

The physical setup as it actually exists. **Unknown** means not yet decided or not yet recorded. Do not replace it
with a guess. When the setup changes, update the **Current configuration** and add a row to the **Change history**.

**Current configuration as of 2026-10-31: nothing built.** Only the instrumentation parts listed as "On hand" exist.
The README lists only the op-amps and regulator from the owner's ECE kit; the rest of the kit is not recorded.

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
| CAD / drawings | None yet | |

## Flow generation and control

| Parameter | Value | Status / source |
|---|---|---|
| Fan / blower model | Unknown | To buy (README) |
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

Signal conditioning parts on hand (README): LM741 / LM348 op-amps, LM317 regulator. Circuit: not designed.

HX711 chip facts, confirmed from the Avia datasheet rev. V2.0 ([notes](../resources/notes/HX711.md)): 24-bit ADC,
10 or 80 samples/s, channel A gain 128 or 64 (channel B fixed at 32), input noise 50 nV rms at gain 128 and 10 SPS.
The module (and so its excitation voltage and RATE wiring) is not chosen.

## Data acquisition

| Parameter | Value |
|---|---|
| Microcontroller / DAQ | **Unknown** (not in the original plan) |
| Sample rate(s) | Unknown |
| Synchronization between pressure and force | Unknown |
| Logging format | Planned: CSV with units in column headers ([data/README.md](../data/README.md)) |

## Test models

| Model | Dimensions | Mount | Status |
|---|---|---|---|
| Validation sphere | Unknown diameter | Unknown (sting/strut) | Planned |
| Airfoil | Unknown | Servo pitch mechanism | Planned (after validation) |

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
