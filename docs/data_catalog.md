# Data Catalog

Every dataset and experiment, with enough detail to reproduce the analysis. Storage rules:
[data/README.md](../data/README.md). Only list data that actually exists. Mark planned experiments as Planned with
no paths. Repository paths written in backticks here are checked by `python scripts/check_docs.py`.

## Summary

| ID | Date | Objective | Status | Raw data | Processed / results |
|---|---|---|---|---|---|
| none | | No data has been collected (as of 2026-11-10) | | | |

Planned experiments (from the build order; no data yet): flow-uniformity map, load-cell calibration, sphere Cd
validation. They get IDs (EXP-001, ...) when first run.

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

None yet.
