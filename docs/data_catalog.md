# Data Catalog

Every dataset and experiment, with enough detail to reproduce the analysis. Storage rules:
[data/README.md](../data/README.md). Only list data that actually exists. Mark planned experiments as Planned with
no paths. Repository paths written in backticks here are checked by `python scripts/check_docs.py`.

## Summary

| ID | Date | Objective | Status | Raw data | Processed / results |
|---|---|---|---|---|---|
| EXP-001 | 2026-11-19 | True masses of the calibration weights, on a school balance | Complete | `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/` | Means computed in the sheet itself; no processed files |
| EXP-002 | 2026-11-26 | Load cell (TAL221 + HX711) on the printed bench scale: sensitivity, straightness, hysteresis, zero, creep, noise | Complete | `data/raw/2026-11-26_EXP-002_tal221-bench-scale/` (`run02.csv`; `run01.csv` is an empty failed start) | `data/processed/2026-11-26_EXP-002_plateaus.csv`, `results/2026-11-26_EXP-002_bench-scale-summary.txt` |

Planned experiments (from the build order; no data yet): flow-uniformity map, the load cell's calibration on the
balance module, sphere Cd validation. They get IDs (EXP-003, ...) when first run.

Bench checks of the electronics produce no dataset; they are recorded in
[experimental_setup.md](experimental_setup.md#breadboard-as-built).

## Entry template

Copy this block for each experiment, newest last.

```markdown
### EXP-NNN: <short title>

- Date(s):
- Objective:
- Status: In progress | Complete | Failed (kept for the record) | Superseded
- Raw data: `data/raw/YYYY-MM-DD_EXP-NNN_<name>/` (or external location for videos)
- Processed data / results: `data/processed/...`, `results/...`
- Format and units: e.g. CSV; time_s, dp_Pa, force_counts
- Setup state: link to docs/experimental_setup.md change-history row
- Acquisition settings: board, sample rate, gain, averaging, duration
- Ambient conditions: p (Pa), T (degC), used for density
- Calibration applied: which calibration dataset / fit
- Processing: script path + exact command
- Results: key numbers with units and uncertainty; status Verified / Preliminary
- Known limitations / missing information:
- Session log: link
```

## Entries

### EXP-001: Calibration mass weighing

- Date(s): 2026-11-19
- Objective: weigh each calibration piece once on an accurate balance, so the load-cell calibration uses measured masses
  instead of the stamped ones (TODO P2; [buy list](buy_list.md) §9).
- Status: Complete
- Raw data: `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/` (the filled form and `metadata.md`)
- Processed data / results: none; the means are formulas in the sheet (columns F–H)
- Format and units: Excel workbook, one sheet; masses in g
- Setup state: no tunnel or electronics involved
- Acquisition settings: school balance CGOLDENWALL HZ50002B, capacity 5000 g, d = 0.01 g; three readings per piece,
  re-zeroed before each (owner)
- Ambient conditions: not recorded
- Calibration applied: none. The balance was not checked against a reference mass; its accuracy is Unknown.
- Processing: the sheet's own formulas (mean, max − min, mean − nominal). The repeatability figure below is the agent's
  calculation: the root-mean-square deviation of each reading from its piece's mean, 45 readings, 30 degrees of freedom.
- Results (Preliminary result: on an unchecked balance):
  - Means (g): 50 g 50.097; 20 g #1 19.763, #2 19.787; 10 g #1–#6 9.940, 10.043, 9.967, 9.940, 9.953, 9.977;
    5 g #1 5.057, #2 5.053; 2 g #1 1.983, #2 1.950, #3 1.973; hanging rod 9.803.
  - Off from the stamped values by −2.5 % (2 g #2) to +1.1 % (both 5 g), in both directions, so the pieces differ and
    the balance's scaling does not explain it. The hanging rod is 2.0 % under the 10 g on its Amazon listing.
  - Repeatability: spreads 0–0.02 g; single-reading standard deviation about 0.008 g, under one display step. Each
    mean is known to about ±0.01 g relative to this balance.
  - All pieces together: 165.5 g, 175.3 g with the rod, more than the TAL221's 150 g safe overload.
- Known limitations / missing information: balance accuracy not checked; room temperature not recorded; the set's
  Amazon listing not recorded. This is the only weight set bought (owner, 2026-11-19); the buy list's "17-piece set,
  10 mg to 100 g" does not describe it. It has no pieces under 2 g, so the drag range (0.3–2.3 g) lies between the
  empty-pan zero and the 2 g pieces.
- Session log: [2026-11-19 BME280 advice and mass weighing](sessions/2026-11-19-bme280-advice-and-mass-weighing.md)

### EXP-002: Load cell on the printed bench scale

- Date(s): 2026-11-26, 01:34–02:06 local time (UTC−05:00)
- Objective: characterise the load-cell chain on a firm mount before the tunnel exists: counts per gram, straightness
  from 2 to 80 g, hysteresis, return to zero, creep under a steady load, zero drift and noise, with the EXP-001 masses.
  Practice and a risk check; **not the tunnel's calibration**, which is done on the balance module (TODO P2).
- Status: Complete
- Raw data: `data/raw/2026-11-26_EXP-002_tal221-bench-scale/`: `run02.csv` (the run), `run01.csv` (empty, a failed
  start: the IDE held the port), `metadata.md` (setup, sequence with times, disturbances, file hashes)
- Processed data / results: `data/processed/2026-11-26_EXP-002_plateaus.csv` (one row per load state);
  `results/2026-11-26_EXP-002_bench-scale-summary.txt`
- Format and units: CSV; `pc_time` (PC local time, ISO 8601), `time_ms` (ms since the Mega reset), `counts` (raw HX711
  ADC counts, channel A, gain 128). Masses in g; forces in N use g = 9.81 m/s² (assumed).
- Setup state: [bench load-cell scale](experimental_setup.md#bench-load-cell-scale-printed) and the breadboard as of
  2026-11-26 ([change history](experimental_setup.md#change-history))
- Acquisition settings: `firmware/hx711_raw_counts` with `AVERAGE_OVER = 1` (every reading), 10 SPS (95 ms interval),
  recorded by `scripts/serial_capture.ps1` ([D-021](../DECISIONS.md)); laptop USB power
- Ambient conditions: not recorded
- Calibration applied: none to the counts. The loads are the EXP-001 measured masses (each ±0.01 g relative to the
  school balance, whose own accuracy is Unknown).
- Processing: `python analysis/exp002_bench_scale.py`. It skips lines before the header and the first second, marks
  any jump over 1,500 counts between readings as a disturbance (±1 s excluded), takes stretches of 4.8 s or more as
  plateaus, merges neighbours within 3,000 counts, matches the 23 states to the logged sequence, takes each state's
  level as the mean of its last 20 s, and fits a straight line.
- Results (**Preliminary result**: one run; unchecked balance; temperature not logged; printed scale, not the tunnel's
  balance):
  - Sensitivity **13,727.5 counts/g** (standard error 1.4, 0.010 %), 1.399 × 10⁶ counts/N; the 0–11 g slope is 0.14 %
    below the 0–79 g slope. Implied output 0.639 mV/V (assuming excitation = the HX711's AVDD reference).
  - Straight-line residuals max 0.025 g, rms 0.012 g, dominated by hysteresis (down minus up +0.004 to +0.022 g).
  - Return to zero +0.011 to +0.013 g after each cycle, +0.026 g over the whole 32 min; creep +0.008 g in about 6 min
    at 50 g.
  - Zero after the first 3 min: 10 s means sd 0.0045 g, span 0.017 g; reading noise sd 40 counts (0.003 g).
  - The 2026-11-23 penny step corresponds to 2.43 g, so it was a 2.5 g penny.
  - Meaning for the tunnel: the zero, not the sensitivity, limits the drag measurement: 0.005–0.025 g is 2–8 % of the
    smallest drag (0.3 g); take a wind-off zero right before and after every wind-on reading.
- Known limitations / missing information: hysteresis and drift are not separable in this sequence; pieces were placed
  near the centre, not at a measured spot (the 5 g was stacked on the 2 g pieces); tweezer bumps at four steps
  (excluded); the pan's mass (9.34 g) is a slicer estimate; the scale's screw lengths and the laptop's charger state were
  not recorded; the reading noise is about 5× the 2026-11-23 figure on a taped cell (cause not tested).
- Session log: [2026-11-26 shield order and load-cell bench test](sessions/2026-11-26-shield-order-and-load-cell-bench-test.md)
