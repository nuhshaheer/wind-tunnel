# Firmware

Arduino sketches for the Elegoo Mega 2560 that reads the sensors (wiring: drawing package sheet 12,
[DECISIONS.md](../DECISIONS.md) D-018). Each sketch sits in a folder of the same name, as the Arduino IDE requires, and
states its wiring, output columns and units at the top.

**To run one:** Arduino IDE 2 → File → Open the `.ino` → Tools → Board "Arduino Mega or Mega 2560", Processor
ATmega2560, Port (COM3 on the owner's PC) → Upload → Tools → Serial Monitor at **115200 baud**. The IDE may keep an old
copy open: after a sketch changes on disk, close its window and open it again before uploading.

| Sketch | Walk-through step | What it does | Needs | Bench result |
|---|---|---|---|---|
| [i2c_scan](i2c_scan/i2c_scan.ino) | 1–2 | Lists every I²C address that answers; reads the BME280's chip ID | nothing extra | 2026-11-23: 0x25 and 0x77, chip ID 0x60; again 2026-11-26 with R1/R2 removed |
| [hx711_raw_counts](hx711_raw_counts/hx711_raw_counts.ino) | 3 | Raw HX711 counts (channel A, gain 128), the mean of `AVERAGE_OVER` readings per line; no calibration. **`AVERAGE_OVER = 1` since 2026-11-26** (every reading; set 10 for one averaged line a second in the Serial Monitor) | nothing extra (protocol written from the HX711 datasheet) | 2026-11-23: 10.5 readings/s, penny step about 33,300 counts. 2026-11-26: EXP-002, 32 min recorded, 13,727.5 counts/g on the bench scale ([data catalog](../docs/data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale)) |
| [sdp810_read](sdp810_read/sdp810_read.ino) | 2 | SDP810 differential pressure (Pa, not corrected for ambient pressure) and chip temperature, 1 line/s | nothing extra (commands from the SDP8xx datasheet) | 2026-11-23: scale 240, zero −0.022 Pa, correct sign. 2026-11-26 (0.1 µF film C1, no R1/R2): zero −0.042 then −0.075 Pa, correct sign, 0 bad reads |
| [bme280_read](bme280_read/bme280_read.ino) | 1 | BME280 pressure (Pa), temperature, humidity and the SDP810 factor 96600 / p, 1 line/s; re-initializes the chip if it resets | **Adafruit BME280 Library** (Library Manager; version not yet recorded) | 2026-11-23: 99.6 kPa, 23.3 °C, 44.5 %; one reset under handling, recovered |

Results and the pasted outputs: [docs/experimental_setup.md](../docs/experimental_setup.md#breadboard-as-built).
None of these is the logging firmware: the combined sketch that reads all three into one CSV line (walk-through step 4)
is not written yet.

Lessons from the bring-up (2026-11-23):

- The Serial Monitor copies only the lines on screen, so print one averaged line per second for anything to be pasted.
  **Since 2026-11-26, record to a file instead:** close the Arduino IDE (it holds the port), then from the repository
  root run `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\serial_capture.ps1 -Port COM3 -OutFile
  data\raw\<folder>\run01.csv` and stop it with Ctrl+C ([D-021](../DECISIONS.md)). Every line is kept with the PC's time.
- The sensors keep power when the Mega resets after an upload, so a sketch must not assume a fresh sensor (the SDP810
  sketch stops a running measurement first).
- A BME280 that loses power for an instant wakes asleep and repeats its reset values (71,853.4 Pa, 23.90 °C, 80.2 %
  here). Check its mode before trusting a reading, and flag any reset in logged data.
