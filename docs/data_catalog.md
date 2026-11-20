# Data Catalog

Every dataset and experiment, with enough detail to reproduce the analysis. Storage rules:
[data/README.md](../data/README.md). Only list data that actually exists. Mark planned experiments as Planned with
no paths. Repository paths written in backticks here are checked by `python scripts/check_docs.py`.

## Summary

| ID | Date | Objective | Status | Raw data | Processed / results |
|---|---|---|---|---|---|
| EXP-001 | 2026-11-19 | True masses of the calibration weights, on a school balance | Complete | `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/` | Means computed in the sheet itself; no processed files |

Planned experiments (from the build order; no data yet): flow-uniformity map, load-cell calibration, sphere Cd
validation. They get IDs (EXP-002, ...) when first run.

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
