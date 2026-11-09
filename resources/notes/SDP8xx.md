# SDP8xx: Sensirion SDP8xx-Digital differential pressure sensor (datasheet)

- Citation: Sensirion AG, *Datasheet SDP8xx-Digital: Digital Differential Pressure Sensor*, Version 1.1, April 2019,
  14 pages.
- Copy in this folder: [SDP8xx_sensirion-digital-dp-sensor-datasheet-v1.1.pdf](../SDP8xx_sensirion-digital-dp-sensor-datasheet-v1.1.pdf).
  Downloaded by the agent on 2026-11-08 from
  https://sensirion.com/media/documents/90500156/6167E43B/Sensirion_Differential_Pressure_Datasheet_SDP8xx_Digital.pdf
  (original file name `Sensirion_Differential_Pressure_Datasheet_SDP8xx_Digital.pdf`) and filed at the owner's
  request.
- Key: datasheets use the part number as the key ([resources/README.md](../README.md)); this one covers the whole
  SDP8xx family.
- Reviewed: 2026-11-08 by Claude Code. Full text read from the PyMuPDF text layer. Pages 11–12 (package outline,
  footprint) read from page images at 200 dpi. The printed page numbers equal the PDF page numbers (x/14).
  **Owner check pending** (checklist at the end).

## What it is

A digital (I²C) differential pressure sensor for air and N₂, calibrated and temperature compensated. It measures
with "a thermal sensor element using flow-through technology" (p. 1): a tiny flow passes through the sensor from the
High to the Low port. Two body styles: SDP80x for manifold mounting and **SDP81x with tube barbs**. Ranges ±500 Pa
and ±125 Pa (p. 2).

## Key numbers

**Differential pressure, SDP8xx-125Pa** (p. 2, §2.1). Footnote 1: all specs at 25 °C, VDD = 3.3 V and absolute
pressure 966 mbar. The table does not say whether the values are typical or maximum.

| Parameter | SDP8xx-125Pa | SDP8xx-500Pa |
|---|---|---|
| Measurement range | −125 to 125 Pa (−0.5 to 0.5 inH₂O) | −500 to 500 Pa |
| Zero point accuracy (footnotes 2, 3) | 0.08 Pa | 0.1 Pa |
| Span accuracy (footnotes 2, 3) | 3 % of reading | 3 % of reading |
| Zero point repeatability | 0.04 Pa | 0.05 Pa |
| Span repeatability | 0.5 % of reading | 0.5 % of reading |
| Span shift due to temperature variation | < 0.5 % of reading per 10 °C | same |
| Offset stability | < 0.05 Pa/year | same |
| Flow step response time (τ63) | < 3 ms | same |
| Resolution | 16 bit | same |
| Temperature compensation range | −20 °C to +85 °C | same |

Footnote 2: accuracy "includes repeatability". Footnote 3: "Total accuracy/repeatability is a sum of zero-point and
span accuracy/repeatability."

Temperature output (p. 2, §2.2): accuracy 2 °C (−10 to +60 °C). It is the temperature of the sensor's silicon, not of
the gas (footnote 4), so it cannot replace the ambient sensor.

**Electrical and timing** (p. 3):

- Supply 2.7–5.5 V; 3.8 mA typical, 5.5 mA maximum while measuring.
- SDA and SCL may go to VDD + 0.3 V (absolute maximum ratings, §3.5). So with VDD = 5 V the sensor accepts 5 V I²C
  levels (our reading of the ratings).
- I²C clock 400 kHz typical, 1000 kHz maximum. Power-up time 25 ms maximum.
- Continuous mode updates the pressure value at 1800–2200 Hz; a triggered measurement takes 40–50 ms.
- Allowable overpressure 1 bar; burst 5 bar; weight 6 g.

**I²C** (pp. 2, 6–10):

- Address **0x25 for every SDP800/SDP810 part, 125 Pa and 500 Pa alike**. Only the SDP801-500Pa and SDP811-500Pa use
  0x26 (p. 2 ordering table, p. 6 §6.1).
- Start continuous measurement with **differential-pressure temperature compensation and "average till read": command
  0x3615** (p. 7). The first result comes after 8 ms; "small accuracy deviations (few % of reading) can occur during the
  next 12 ms". Stop: 0x3FF9.
- "Average till read" (p. 5, §5.2): the sensor averages every 0.5 ms sample since the last read, so slow reads lose no
  information and do not alias. It takes the arithmetic mean for the first 25 ms, then exponential smoothing with
  α = 0.05.
- Scale factor for the 125 Pa part: 240 counts per Pa (p. 10, §6.5.1). The reading is a signed 16-bit integer.
- Each 16-bit word is followed by a CRC-8: polynomial 0x31, initial value 0xFF, no reflection; CRC(0xBEEF) = 0x92
  (p. 10).
- Product number read back: SDP810-125Pa = 0x03020B01 (p. 9).
- Order number SDP810-125Pa: 1-101597-01 (p. 2).

**Mechanical** (pp. 4, 11–13):

- Pins (p. 4): 1 SCL, 2 VDD, 3 GND, 4 SDA. Footprint (p. 12): pins at −3, −1, +1 and +3 mm, so a **2 mm pitch**,
  Ø0.8 mm holes. The pins are 0.5 mm wide (p. 11). They do not fit 0.1 in (2.54 mm) perfboard.
- SDP81x ports (p. 11, Fig. 2): barbs Ø5.2 ±0.2 mm at the widest, Ø3.5 ±0.2 mm at the tip; 12.6 ±0.2 mm apart;
  marked **High** and **Low**.
- Body 29 ±0.4 × 18 ±0.4 mm; two Ø2.9 mm mounting holes 24 mm apart (p. 11).
- Soldering (p. 13): wave soldering only, "Reflow soldering is not feasible"; protect the ports from solder splash and
  flux. Hand soldering is not mentioned.
- Cable mounting (p. 12): "In case the sensor is not mounted on a PCB and is connected with a cable, the SDP800 series
  cap is recommended."

## Limitations and caveats

- **Not stated:** any effect of tube length or diameter (the sensor draws a small flow, so long or narrow tubes can
  lower the reading); position sensitivity; warm-up time; whether the accuracy figures are typical or maximum.
- **The 966 mbar condition matters.** In differential-pressure mode the reading must be corrected for ambient
  pressure: dp_cor = dp_sensor × 966 mbar / p_amb (×0.95 at sea level). This is not in the datasheet; it is in
  Sensirion's signal-compensation note ([Sensirion2024](Sensirion2024.md)). The datasheet only points to it (§5.3,
  p. 5).
- Specified at VDD = 3.3 V. This project plans 5 V, which is inside the supply range; performance at 5 V is not
  separately specified.
- From a DigiKey listing, not this datasheet: the SDP800 series cap (DigiKey 1649-1042-ND, Mouser 403-SDP800CAP)
  works as a connector for a Molex DuraClik 4-circuit housing, 502351-0400. Not checked against Sensirion's cap
  datasheet.

## What it suggests for this project [Proposed]

Our reading and arithmetic, 2026-11-08:

- **q accuracy:** total accuracy = 0.08 Pa + 3 % of reading. That is 3.3 % of q at 6.5 m/s (25 Pa) and 3.1 % at
  13 m/s (101 Pa). Because C_D = F/(qA), this goes straight into C_D. The 3 % span part is a gain error: it shifts
  every reading by the same factor, so it affects the comparison with Eq. (19) but hardly the trend check (D-009).
  Repeatability is 0.04 Pa + 0.5 %.
- **Calibrate the span** against a water manometer, with the sensor's own tubing in place. That reduces the 3 % gain
  error and captures any tubing effect (buy list §9).
- **Apply the ambient-pressure correction** with the BME280's reading in every run.
- **Two sensors on one bus clash at 0x25,** so a second SDP810-125Pa needs an I²C multiplexer (for example a
  TCA9548A breakout).
- **Tubing:** about 3–4 mm inside diameter to grip the Ø3.5/5.2 mm barbs, as short as practical, both lines the same
  length.
- **Mounting:** solder thin wires straight to the four pins, with a quick joint and no flux near the ports, or use the
  cap and a DuraClik housing. Screw the body to a bracket through its two Ø2.9 mm holes so the wires carry no load.
  Mount the sensor above its tubing so any condensation drains away from the ports (Sensirion2024, §5).

## References worth following up

- Sensirion "SDP Engineering Guide" and "Differential Pressure Testing Guide": tubing effects (the SDP3x hose note
  says the pressure drop in a tube grows with its length and with 1/D⁴; search summary, not read).
- Sensirion's SDP800 series cap datasheet: the mating connector and crimp terminals.

## Owner check (values read from the PDF)

Please confirm against the PDF (printed page = PDF page):

1. p. 2, §2.1 table, SDP8xx-125Pa column: zero point accuracy, span accuracy, zero point repeatability and span
   repeatability.
2. p. 2, footnote 1: the conditions (temperature, VDD, absolute pressure).
3. p. 2, ordering table: the I²C address of the SDP810-125Pa.
4. p. 3: the supply voltage range, and the maximum voltage on SDA/SCL (§3.5).
5. p. 7, §6.3.1: the command code for differential-pressure compensation with "average till read".
6. p. 10, §6.5.1: the scale factor for the 125 Pa part.
7. p. 11, Fig. 2: the two barb diameters, and the port spacing.
8. p. 12, Fig. 3: the pin spacing.
