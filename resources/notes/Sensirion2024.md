# Sensirion2024: SDP Signal Compensation (application note)

- Citation: Sensirion AG, *SDP Signal Compensation: How to compensate environmental influence on the sensor signal*,
  application note, Version 1.0, June 2024, 9 pages.
- Copy in this folder: [Sensirion2024_sdp-signal-compensation-app-note.pdf](../Sensirion2024_sdp-signal-compensation-app-note.pdf).
  Downloaded by the agent on 2026-11-08 from
  https://sensirion.com/media/documents/FEAE3023/667EC183/DP_AN_Signal_Compensation_V1.0_1.pdf (original file name
  `DP_AN_Signal_Compensation_V1.0_1.pdf`).
- Key: no personal author, so the organization's name plus the year.
- Reviewed: 2026-11-08 by Claude Code. Full text read from the PyMuPDF text layer; the figures were not examined.
  Printed page = PDF page (x/9). **Owner check pending** (checklist at the end).

## What it says

- SDP sensors are microthermal flow sensors: a heater between two temperature sensors. The gas flow through the
  sensor makes a temperature difference that "correlates to the mass flow"; the sensor is then calibrated to
  differential pressure (§1, p. 3).
- Two temperature-compensation modes (§2, pp. 3–5). For measuring differential pressure directly, choose
  "differential pressure temperature compensation"; then "no further action is required" for temperature (§2.1,
  Table 2).
- **Altitude (ambient-pressure) correction for differential pressure** (§3.1, pp. 5–6). The sensors are calibrated at
  425 m above sea level and 966 mbar. "A pressure correction must be applied for accurate direct differential pressure
  measurements … for absolute pressures deviating from 966 mbar" (§3, p. 5). Formula (1):

  dp_cor = dp_sensor × p_cal / p_amb, with p_cal = 966 mbar and p_amb the ambient pressure at the moment of measurement.

  Table 3 (p. 6), correction factor p_cal/p_amb: 0 m, 1013 mbar → 0.95; 250 m, 984 mbar → 0.98; 425 m, 966 mbar → 1;
  500 m, 958 mbar → 1.01; 750 m, 925 mbar → 1.04. Worked example: 40 Pa read at 750 m is 41.8 Pa.
- Mass-flow measurements need no altitude correction (§3.2.1); volume flow does (§3.2.2). Table 5 (p. 7) repeats this:
  for an SDP, pressure compensation is "required" for differential pressure.
- Condensation (§5, p. 7): rare indoors. If droplets could run into the sensor, place it on the top side so gravity
  pulls them away from the ports; avoid making the sensor the coldest part of the system.
- Calibrated for air and N₂; other gases need their own conversion (§6, p. 8).

## Limitations and caveats

- A general note for all SDP sensors; it does not name the SDP8xx specifically. The SDP8xx datasheet (§5.3) points to
  Sensirion's guidance for absolute-pressure compensation, which is consistent with this.
- The table gives two-digit factors; the formula is exact.

## What it suggests for this project [Proposed]

- The pitot reading is a direct differential pressure, so use the SDP8xx's DP temperature compensation (command
  0x3615, [SDP8xx notes](SDP8xx.md)) and **multiply every reading by 966 mbar / p_amb**, with p_amb from the BME280.
  Without it, q, and so C_D, would be about 5 % off near sea level (our arithmetic from Table 3). The direction: the
  raw reading is high when p_amb > 966 mbar.
- p_amb changes by a few percent with the weather, so apply the correction per run, not once.
- Mount the pressure sensors above their tubing (condensation), and keep mist away from the measurement lines, as
  already planned.

## Owner check (values read from the PDF)

1. p. 5, §3: the calibration altitude and pressure.
2. pp. 5–6, §3.1: formula (1), and which pressure goes on top of the fraction.
3. p. 6, Table 3: the correction factor at 0 m.
4. p. 7, Table 5: whether pressure compensation is "required" for differential pressure with an SDP.
