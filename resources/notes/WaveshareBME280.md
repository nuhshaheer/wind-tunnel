# WaveshareBME280: BME280 Environmental Sensor board (schematic)

- Citation: Waveshare, *BME280 Environmental Sensor* board schematic, one page, undated (PDF 1.3). Linked from Waveshare's
  wiki page "BME280 Environmental Sensor" (https://www.waveshare.com/wiki/BME280_Environmental_Sensor).
- Copy in this folder: [WaveshareBME280_environmental-sensor-schematic.pdf](../WaveshareBME280_environmental-sensor-schematic.pdf);
  downloaded by the agent on 2026-11-17 from
  https://files.waveshare.com/upload/4/42/BME280-Environmental-Sensor-Schematic.pdf (original name
  `BME280-Environmental-Sensor-Schematic.pdf`).
- Key: there is no maker's part number for the board, so the key is the maker plus the chip.
- Reviewed: 2026-11-17 by Claude Code. Read from the PDF's text layer (net names, values) and a 200 dpi page image.
  The wiki page was read the same day through a web-fetch agent (its quotes are below, marked "wiki"). Waveshare's
  product page returned HTTP 503 and was not read. **Owner check pending** (checklist at the end).

## What it is

The board the project bought for ambient pressure and temperature (ordered 2026-11-09, arrived by 2026-11-17): a Bosch
BME280 chip on a small board with its own 3.3 V regulator and a level translator, so it can sit on the 5 V Mega's I²C
bus.

## Key numbers (from the schematic unless marked)

- **Header H1, 6 pins:** 1 VCC, 2 GND, 3 SDA/MOSI, 4 SCL/SCK, 5 ADDR/MISO, 6 CS.
- **Regulator U1:** RT9193-33 (VCC in, 3V3 out), with 10 µF and 1 µF on the input, 10 µF on the output, 22 nF on BP.
- **Level translator:** two NDC7002N dual MOSFETs (U3, U4), one channel each for SDA, SCL, ADDR/MISO (SDO) and CS (CSB).
- **Pull-ups:** each translator channel has **4.7 kΩ to VCC on the header side** (NDC1.R2, R4 and NDC2.R2, R4) and
  4.7 kΩ to 3V3 on the chip side (NDC1.R1, R3 and NDC2.R1, R3). So SDA and SCL arrive at the header already pulled up
  to VCC (5 V on the Mega) through 4.7 kΩ, and ADDR and CS are pulled high when left open.
- **Address solder pad J1** joins ADDR/MISO to GND.
- **Chip U2 (BME280):** VDD and VDDIO on 3V3, with two 100 nF capacitors.
- Wiki: I²C is the default; "When the voltage is high, the address is 0x77. When the voltage is low, the address is:
  0x76"; ADDR "default is high"; for an Arduino, CS is "NC" in I²C mode. Operating voltage "5V/3.3V".

## Limitations and caveats

- The schematic is undated and has no revision mark; it is assumed to match the board delivered to the owner. Check the
  board's printed labels against the header order above.
- The schematic gives no part numbers for the resistors and capacitors beyond values, and no layout.
- The wiki does not name the cable that ships with the board (the buy list's "PH2.0 6-pin cable" came from a listing,
  not checked).
- The wiki's Raspberry Pi section reads "If ADDR is connected to GND76 it will print 77", which looks garbled;
  everywhere else, grounded ADDR means 0x76.

## What it suggests for this project [Proposed]

Our reading, 2026-11-17 (drawing package sheet 12 and [the walk-through](../../docs/electronics_walkthrough.md)):

- **No extra I²C pull-ups are needed while this board is on the bus:** its 4.7 kΩ to VCC on SDA and SCL do the job, so R1
  and R2 on sheet 12 are not fitted (DNP). With the Mega's own pull-ups (about 10 kΩ on official boards, if this clone
  has them), the bus sees about 3.2 kΩ.
- **Leave ADDR and CS unconnected:** both are pulled high on the board, which gives I²C mode at 0x77, clear of the
  SDP810's 0x25.
- **The power-only arrival check is predicted to read about 5 V** on SDA and SCL (they are pulled up to VCC). About 3.3 V
  would contradict this schematic: stop and check before wiring SDA and SCL to the Mega.

## The delivered board (added 2026-11-18)

- Owner's [photo](../../docs/images/2026-11-17_bme280-board-and-cable.jpg): a 5-pin regulator, two 6-pin translator chips and
  eight resistors marked 472 (4.7 kΩ), consistent with the schematic. No pin labels on the photographed side.
- The cable is a white 6-pin plug to six female Dupont sockets. Its wire order at the plug is red, black, blue, yellow,
  orange, green, taken as header pins 1–6 (inferred).
- Owner's meter, unpowered, cable in the board: red to blue, yellow, orange and green 4.605, 4.617, 4.597 and 4.617 kΩ;
  black to blue 145.3 kΩ. This fits red being VCC with four 4.7 kΩ pull-ups. It does not identify the four signal wires.

## References worth following up

- Bosch's BME280 datasheet (on the resources "Wanted" list): chip ID 0xD0 = 0x60, accuracy, measurement modes.

## Owner check (values read from the PDF)

Please confirm against the PDF (one page):

1. Header H1 (right side): the pin order 1 VCC, 2 GND, 3 SDA/MOSI, 4 SCL/SCK, 5 ADDR/MISO, 6 CS.
2. The four resistors next to each NDC7002N: the value (4.7K) and which ones connect to VCC rather than 3V3.
3. J1 (top right): it joins ADDR/MISO to GND.
4. U1 is labelled RT9193-33.
