# EXP-002: TAL221 load cell on the printed bench scale (metadata)

- **What:** a bench characterisation of the load-cell chain (TAL221 100 g + SparkFun HX711 + Elegoo Mega 2560) on a firm
  printed mount: sensitivity, straightness, hysteresis, return to zero, creep under 50 g, zero drift and noise, with the
  EXP-001 calibration masses. **Practice and a risk check, not the tunnel's calibration**, which is done later on the
  balance module (different mount and load direction).
- **When and where:** 2026-11-26, 01:34:12 to 02:06:23 local time (UTC−05:00), at the owner's bench. Masses placed by
  the owner; the agent recorded the data and checked each step live in the session.
- **Files** (written by `scripts/serial_capture.ps1`; never edited):
  - `run01.csv`: **empty (0 bytes), a failed start** at 01:33:05. The Arduino IDE still held COM3 ("Access to the
    port 'COM3' is denied"), and the first version of the script created the file before opening the port (fixed the
    same night: the port is now opened first). SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
  - `run02.csv`: the run. 20,180 lines, started 01:34:11.950, stopped 02:06:23.738 by the script's stop file.
    SHA-256 `bca1203414da37b5b3a98d3a2b16850ebe9cf86b655237f31a75499f8ba84063`.
- **Columns of run02.csv:** `pc_time` (the PC's local time when the line was read, ISO 8601 with UTC offset),
  `time_ms` (ms since the Mega reset), `counts` (raw HX711 ADC counts, channel A, gain 128; no calibration applied).
  Lines 1–15 are serial-buffer leftovers from before the port opened (time_ms about 48 s, some repeated); the Mega
  reset when the port opened, printed two `#` message lines at 01:34:12.857 and then the header `pc_time,time_ms,counts`
  (line 18). The sketch's messages say to ignore its first second.
- **Firmware:** `firmware/hx711_raw_counts/hx711_raw_counts.ino` as committed in `397c671` with one change,
  `AVERAGE_OVER = 1` (every raw reading; committed value 10), uploaded by the owner from Arduino IDE 2.3.10. Reading
  interval 95 ms (about 10.5 readings/s), the HX711's 10 SPS setting.
- **Electronics:** the breadboard as wired on 2026-11-26 (all three sensors connected; C1 the 0.1 µF film capacitor;
  R1 and R2 and their 5 V wires removed), powered from the laptop's USB. Whether the laptop was on its charger: not
  recorded. HX711 board taped down (asked for; not confirmed).
- **Scale:** "TAL221 Load Cell Scale" by bwilless (`cad/third-party/tal221-scale-bwilless/`), printed by the owner in
  PLA at 20 % infill (the designer used 25 %). The TAL221 soldered to the HX711 is screwed to it, wire end on the base;
  the designer specifies M3 × 10 at the base and M3 × 20 with nuts at the pan; the lengths actually used were not
  recorded. Pan mass: **9.34 g, the slicer's estimate** (9.42 g with supports, removed), not weighed. It rests on the
  cell throughout, so it is part of the zero.
- **Masses:** the EXP-001 measured means (g): 2 g #1 1.983, #2 1.950, #3 1.973; 5 g #1 5.057; 10 g #1 9.940, #2 10.043,
  #3 9.967, #4 9.940; 20 g #1 19.763, #2 19.787; 50 g 50.097. Each about ±0.01 g relative to the school balance, whose
  own accuracy is Unknown.
- **Sequence (owner's messages; times approximate, from the live checks):**
  1. Empty pan, 01:34:12 to about 01:43:08 (warm-up and zero; hands off).
  2. Low range up, about 30–60 s per step: 2 g #1 (01:43:10), 2 g #2 (01:43:47), 2 g #3 (01:44:09), 5 g #1 (01:45:45;
     **stacked on top of the 2 g pieces**, the pan's centre recess leaving little room).
  3. Low range down: 5 g #1 off (01:46:08), 2 g #3 off (01:46:35), 2 g #2 off (01:47:16), 2 g #1 off (01:47:45).
  4. Empty pan about 1.5 min.
  5. Full range up: 10 g #1 (01:49:38), 10 g #2 (01:50:00), 10 g #3 (01:50:22), 20 g #1 (01:50:55), 20 g #2 (01:51:10),
     10 g #4 (01:52:16; 79.440 g, the most loaded; pan plus masses about 89 g against the cell's 100 g rating).
  6. Full range down: 10 g #4 off (01:53:12), 20 g #2 off (01:54:05), 20 g #1 off (01:54:32), 10 g #3 off (01:55:08),
     10 g #2 off (01:55:36), 10 g #1 off (01:56:04).
  7. Empty pan about 30 s; then **50 g on at about 01:56:37 for about 6 min** (creep), off at about 02:02:00.
  8. Empty pan until the stop, 02:06:23.

  Pieces were placed with tweezers near the pan's centre, side by side or stacked; exact positions not recorded.
- **Disturbances seen in the data:** tweezer bumps while placing or removing, at about 01:44:09 and 01:44:12 (peaks about
  16 g above the empty pan), 01:47:19 (about 19 g) and 01:54:32 (about 77 g above the empty pan, so about 87 g on the
  cell for an instant, below its 100 g rating and 150 g safe overload), and a touch before lifting the 50 g. All are
  short spikes; the analysis excludes every stretch with a jump between consecutive readings.
- **Ambient:** not recorded (the BME280 was not logged; a room at night).
- **Analysis:** `analysis/exp002_bench_scale.py`, run as `python analysis/exp002_bench_scale.py`, writes
  `data/processed/2026-11-26_EXP-002_plateaus.csv` and `results/2026-11-26_EXP-002_bench-scale-summary.txt`.
- **Session log:** the 2026-11-25/26 session (see `docs/sessions/SESSION_LOG.md`).
