# Experimental Setup

The physical setup as it actually exists. **Unknown** means not yet decided or not yet recorded. Do not replace it
with a guess. When the setup changes, update the **Current configuration** and add a row to the **Change history**.

**Current configuration as of 2026-10-29: nothing built.** Only the instrumentation parts listed as "On hand" exist.

## Tunnel geometry

| Parameter | Value | Status / source |
|---|---|---|
| Tunnel type (open-circuit blower / suck-down / closed-return) | Unknown | Planned, build step 1 |
| Inlet / settling chamber size | Unknown | Planned |
| Contraction ratio and length | Unknown | Planned, build step 1 |
| Test section cross-section (W × H) | Unknown | Planned, build step 1 |
| Test section length | Unknown | Planned, build step 1 |
| Diffuser | Unknown | Planned |
| Construction material | Unknown | |
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
| Ambient pressure | Unknown | | | | Not planned yet (needed for ρ) |
| Ambient temperature | Unknown | | | | Not planned yet (needed for ρ) |
| Airfoil pitch actuator | Servo | Unknown | | | To buy (README), build step 7 |

Signal conditioning parts on hand (README): LM741 / LM348 op-amps, LM317 regulator. Circuit: not designed.

HX711 datasheet facts (general, not yet confirmed on this project's module): 24-bit ADC, selectable 10 or 80 samples/s,
channel A gain 128 or 64.

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
