# Data

No experimental data has been collected yet (as of 2026-10-29). This file defines where data goes
when it exists. The policy is recorded in [DECISIONS.md](../DECISIONS.md) (D-004) and every dataset is
listed in [docs/data_catalog.md](../docs/data_catalog.md).

## Layout

| Folder | Contents | Rules |
|---|---|---|
| `data/raw/` | Files exactly as acquired (sensor logs, calibration readings) | **Never edited, renamed or overwritten.** Stored byte-for-byte (`.gitattributes` disables line-ending conversion here). A bad run is kept and marked bad in the catalog, not deleted. |
| `data/processed/` | Files derived from raw data by a script (filtered, calibrated, averaged) | Must be reproducible from `data/raw/` + a script in `analysis/`. Regenerate rather than hand-edit. |
| `analysis/` | Scripts and notebooks that turn raw data into processed data, plots and numbers | Each script states its inputs, outputs and units at the top. |
| `results/` | Figures and tables cited by the docs | Each result names the script and data it came from. |

These folders are created when their first file arrives (Git does not track empty folders).

## Naming

One folder per acquisition session:

```text
data/raw/YYYY-MM-DD_EXP-NNN_short-description/
    run01.csv
    run02.csv
    metadata.md      # what, when, setup state, sensor config, sample rate, units, ambient conditions
```

`EXP-NNN` is the experiment identifier from the data catalog (EXP-001, EXP-002, ...).

## Units

SI throughout: m, m/s, Pa, N, kg, K or degC (say which), s. Column headers carry units, e.g.
`time_s,dp_Pa,force_N`. If a file stores raw ADC counts, say so in the header and in `metadata.md`.

## Large files

- CSV/text logs: committed directly (expected to be small).
- Photos: compressed to roughly 2 MB or less before committing.
- Videos: **not committed** (`.gitignore` excludes common video formats). Keep originals in external
  storage and record the location in the data catalog.
- Any file over 25 MB is flagged by `python scripts/check_docs.py`; GitHub rejects files over 100 MB.
  Git LFS is installed on the development machine but not enabled for this repository yet.
