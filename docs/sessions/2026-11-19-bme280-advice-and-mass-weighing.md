# 2026-11-19: BME280 advice and calibration mass weighing

- **Session ID:** 7aeaf588-f591-40d7-8bbd-9e8c175822d0
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** not committed yet

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `ff2ac6e` (the 2026-11-18 breadboard session, committed and pushed by the owner). Clean
  working tree; the owner's original photos (three with GPS data) were no longer in `docs/images/`. `check_docs.py`
  0 failures and 0 warnings (777 links); 20 tests OK in 17.4 s.
- Discrepancies found and fixed at this wrap: PROJECT_STATUS still named `8904785` as the last commit and the
  breadboard session as uncommitted; the 2026-11-18 log and index row lacked `ff2ac6e`; the original-photo warning
  was out of date.
- No set objective. The owner, at school, asked about the BME280 and then asked for a spreadsheet to weigh their
  calibration weights on a school balance.

## 2. Work completed

- **BME280 questions answered** (advice, no hardware change):
  - What it is for: the SDP810's ×966 mbar / p_amb correction (about 5 % near sea level, the important job), and air
    density and temperature for the airspeed and the Reynolds number that picks the reference C_D. C_D itself
    (F / qA) does not use density.
  - Inside the tunnel or not: room air near the fan inlet, as already planned in the buy list §7. Inside, pressure
    differs by at most about 0.15 % and temperature by under about 0.4 °C (fan heating), changing the reference C_D by
    about 0.02 % (estimates, §6), while a board in the test section or after the screens would disturb the flow.
  - Its own box: yes, but an open, vented printed holder, not a closed box and not the Arduino box (the Mega's heat).
    Keep it away from the fan motor, lamps and sunlight. Added to the sizing task (TODO P1). A one-time fan-heating
    check with the BME280 in the exit jet was added (TODO P2).
- **Weighing form** made at the owner's request (simple, Times New Roman): `docs/forms/calibration-mass-weighing.xlsx`.
  One sheet: balance details, one row per piece (three readings, then mean, spread and mean − nominal by formula), an
  example row, spare rows and eight weighing steps. Saved in the OneDrive project folder so the owner could open it at
  school.
  - From the owner's messages the agent filled in the balance: CGOLDENWALL HZ50002B, 5000 g, d = 0.01 g, and changed
    the example row to two decimals. At the owner's request a hanging-rod row was added, after the owner closed the
    file (an earlier attempt was held back because the owner had it open; see §8).
- **The owner weighed every piece** (§4, §6). The filled file was copied byte-for-byte into
  `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/` with a `metadata.md`, and catalogued as **EXP-001**, the
  project's first dataset. `docs/forms/` was then reset to a blank template (with the hanging-rod row built in).
- **The weight set is not the one the docs listed.** The owner bought one set, from Amazon: 50, 2 × 20, 6 × 10, 2 × 5
  and 3 × 2 g plus a 10 g hanging rod, not the 17-piece 10 mg–100 g set in the buy list. Corrected in the buy list §9,
  the shopping list, the drawings' parts list (item 76, page rebuilt) and the setup.
- **Advice: no masses under 2 g are needed** (owner asked whether the 2 g pieces must be reweighed: no). The drag range
  (0.3–2.3 g) lies between the wind-off zero and the 2 g pieces, so the calibration interpolates there; solder cut by
  length can make small masses if a low-end check is ever wanted.

## 3. Files and equipment affected

- New:
  - `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/calibration-mass-weighing.xlsx` (the owner's filled
    sheet, SHA-256 `d317eff4…2b1c`) and `metadata.md`
  - `docs/forms/calibration-mass-weighing.xlsx` (blank template)
  - this log
- Modified: `PROJECT_STATUS.md`, `TODO.md`, `README.md`, `data/README.md`, `docs/data_catalog.md`,
  `docs/experimental_setup.md`, `docs/buy_list.md`, `docs/shopping_list.md`, `docs/drawings/README.md`,
  `docs/drawings/page.py`, `docs/drawings/wtdata.py`, `docs/drawings/wind-tunnel-drawings.html` (rebuilt),
  `docs/sessions/SESSION_LOG.md`, `docs/sessions/2026-11-18-breadboard-power-and-part-checks.md` (commit backfill only).
- Equipment: none changed. The breadboard was not touched this session.
- PC: openpyxl 3.1.5 installed for Python 3.11 (user site-packages).

## 4. Experimental procedures performed

The owner, at school, 2026-11-19 (the agent performed none of it):

1. Labelled each multiple piece with tape and a number (#1, #2, ...); the single 50 g piece and the hanging rod were not
   taped.
2. Balance CGOLDENWALL HZ50002B (capacity 5000 g, d = 0.01 g), level bubble centred; empty pan read 0.
3. Each piece weighed three times, taken off between readings, with the balance **re-zeroed before every reading**.
   No separate empty-pan reading was written at the end (owner: re-zeroing gives 0). Room temperature not recorded;
   handling (tweezers or fingers) not recorded.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                      # UP_TO_DATE at ff2ac6e (catch-up and wrap)
python scripts/check_docs.py; python -m unittest discover -s tests
python -m pip install --user openpyxl                      # openpyxl 3.1.5; not a project dependency
# Scratchpad scripts (not kept in the repo):
#   make_weighing_form.py <out.xlsx>   builds the form (openpyxl; Times New Roman default font; fullCalcOnLoad)
#   check_form.py / peek*.py / dump.py  read the form back: fonts, formula rows, typed values, Excel's cached results
#   fill_balance.py, add_rod.py         in-place edits (balance cells, example row, hanging-rod row), each checked to
#                                       change only the intended cells
#   summarize.py                        means, deviations and the pooled repeatability (§6)
cp --preserve=timestamps docs/forms/calibration-mass-weighing.xlsx data/raw/2026-11-19_EXP-001_calibration-mass-weighing/
sha256sum docs/forms/calibration-mass-weighing.xlsx data/raw/2026-11-19_EXP-001_calibration-mass-weighing/calibration-mass-weighing.xlsx
python docs/drawings/page.py                               # "parts never drawn: []"
```

## 6. Measurements and results

**Raw observations** (owner, 2026-11-19; `data/raw/2026-11-19_EXP-001_calibration-mass-weighing/`): three readings
per piece in g, on a balance with d = 0.01 g whose accuracy has not been checked against a reference mass.

**Processed** (means by the sheet's formulas; Excel's cached values match the agent's recomputation). Status:
**Preliminary result.**

| Piece | Mean (g) | Mean − nominal | Spread (g) |
|---|---|---|---|
| 50 g | 50.097 | +0.19 % | 0.02 |
| 20 g #1 / #2 | 19.763 / 19.787 | −1.18 % / −1.07 % | 0.01 / 0.02 |
| 10 g #1–#6 | 9.940, 10.043, 9.967, 9.940, 9.953, 9.977 | −0.60 to +0.43 % | 0.00–0.02 |
| 5 g #1 / #2 | 5.057 / 5.053 | +1.13 % / +1.07 % | 0.01 / 0.01 |
| 2 g #1 / #2 / #3 | 1.983 / 1.950 / 1.973 | −0.83 / −2.50 / −1.33 % | 0.01 / 0.00 / 0.01 |
| Hanging rod (10 g per the Amazon listing) | 9.803 | −1.97 % | 0.02 |

- Repeatability: single-reading standard deviation 0.0077 g (root-mean-square deviation from each piece's mean,
  45 readings, 30 degrees of freedom). Each mean is known to about ±0.01 g relative to this balance.
- Totals: 165.48 g for the 14 pieces, 175.3 g with the rod.
- Interpretation: the deviations run both ways, so they belong to the pieces, not to a scaling error of the balance.
  Use the measured masses. The balance's absolute accuracy remains not quantified.

**Estimates (not measurements)** behind the BME280 advice:

- Fan heating: ≤ 60 W (the VEVOR's listed power, taken as an upper value; the S6's is not recorded) into
  13 m/s × 0.01 m² × 1.2 kg/m³ = 0.156 kg/s of air with c_p = 1005 J/(kg·K) gives at most about 0.38 K.
- Effect: density 0.13 %; Re ∝ √(qρ)/μ ∝ T^−1.27 (Sutherland, μ ∝ T^0.77 near 293 K), so Re 0.17 %; Eq. (19) C_D
  changes about 0.10 × that (12 % over a threefold Re range), about 0.02 %.
- Pressure: settling chamber up to about 100–150 Pa above room, test section about room pressure (open exit): at most
  about 0.15 % of 101 kPa.
- Mega in a closed box: about a third of a watt could warm the box air by a degree or more (rough, not computed).

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests -v`: 20 tests OK in 19.1 s (Python 3.11.0).
- `python scripts/check_docs.py`: 0 failures, 0 warnings (809 links; 19 session logs, each indexed once; 114 committable
  files, none over 25 MiB).
- Form checks (read back with openpyxl): every formula in columns F–H refers only to its own row; every filled cell is
  Times New Roman, and Times New Roman is the workbook's default font. LibreOffice is not installed, so `recalc.py`
  could not run; the formulas were first evaluated by Excel on the owner's copy, and those cached values agree with
  `summarize.py`.
- Raw copy: SHA-256 of the filed copy equals the owner's saved file; checked again with `cmp` before the form was reset.
- In-place edits of the owner's file changed only the intended cells (before/after comparison of every cell value).
- Drawings: `python docs/drawings/page.py` rebuilt the page, "parts never drawn: []"; only parts-list item 76 and the
  revision note changed. `preview.py` not run (no sheet geometry changed).
- **Not performed:** any check of the balance against a reference mass; any electronics work (the BME280 step 1 is
  still next); any load-cell calibration.

## 8. Errors, failed approaches and troubleshooting

- openpyxl was not installed for any Python on the PC; installed with `pip install --user`. `python -I` then could not
  import it (isolated mode skips user site-packages), so the form scripts ran without `-I`; they read no downloaded
  files.
- LibreOffice is not installed, so formulas could not be recalculated before delivery (see §7).
- A long Bash heredoc holding the status edits failed to parse ("unexpected EOF"); the script was written with the
  Write tool instead.
- Printing non-ASCII text failed on the cp1252 console; fixed with `PYTHONIOENCODING=utf-8`.
- A number format with a Unicode minus sign was replaced with an ASCII one, since Excel may reject unquoted symbols.
- **OneDrive conflict avoided:** when the owner asked for the hanging-rod row, the file had been saved from the owner's
  device minutes earlier and was probably open. The agent did not write to it and asked; it edited only after the owner
  closed the file.
- **Agent errors corrected in the conversation:** (1) it first said a spread of 0.02 g meant reweighing; two display
  steps are normal for a 0.01 g balance, and no piece needed it. (2) It assumed the weighed set was the buy list's
  17-piece set and asked about weighing its small pieces; the owner bought only this set. (3) The brand "CGOLDENWALL"
  is the agent's reading of the owner's "cggoldenvial"; the owner did not correct it.

## 9. Decisions and reasoning

- No new DECISIONS.md entry. Agent's advice recorded as Proposed, not decided: the BME280 stays in room air near the fan
  inlet in its own vented holder; no calibration masses under 2 g are needed.
- Agent's choices: file the owner's sheet in `data/raw/` unchanged and keep the facts that could not change in
  `metadata.md`, with interpretation in the data catalog (raw files are never edited); reset `docs/forms/` to a blank
  template, since the readings are kept in `data/raw/`; correct the drawings' parts list (item 76) as a dated note on
  revision D rather than a new revision, since no sheet changed.

## 10. Open questions and blockers

- The weight set's Amazon listing (link or name), to record next to the data. Optional.
- Whether the hanging rod can hang from the calibration hook in place of the pan (check its shape at build step 5).
- The school balance's accuracy against a reference mass: Unknown.
- Still open from 2026-11-18: whether R1, R2, their feed jumpers and the clipped wire were removed; the HX711 RATE
  jumper; how the SDP810 connects (open question 19); the BME280 step 1.

## 11. Remaining tasks

- **Owner:** commit and push (§13); the BME280 step 1 at the bench; choose the SDP810 connection; the remaining arrival
  checks; choose the fan; send the sizing inputs (heat-set inserts, filament).
- **Agent:** the I²C scanner and the other bring-up sketches when wanted; sheet 12 pad names when approved; the sizing,
  now including the BME280 holder.

## 12. Recommended first task for the next agent

Unchanged from 2026-11-18. Ask whether the owner is at the bench. If so, confirm R1, R2, their two feed jumpers and the
clipped wire are gone, then continue the BME280 step 1
([2026-11-18 log §12](2026-11-18-breadboard-power-and-part-checks.md#12-recommended-first-task-for-the-next-agent)),
and write the I²C scanner in `firmware/` when the owner reaches step 4. If the owner is away from the bench, start the
sizing with the settling-chamber spacing (PROJECT_STATUS open questions 13 and 15).

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `ff2ac6e`; nothing staged. 14 files modified and 4 new to commit.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add PROJECT_STATUS.md TODO.md README.md data/README.md
git add docs/data_catalog.md docs/experimental_setup.md docs/buy_list.md docs/shopping_list.md
git add docs/drawings/README.md docs/drawings/page.py docs/drawings/wtdata.py docs/drawings/wind-tunnel-drawings.html
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-18-breadboard-power-and-part-checks.md docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md
git add docs/forms/calibration-mass-weighing.xlsx
git add data/raw/2026-11-19_EXP-001_calibration-mass-weighing/calibration-mass-weighing.xlsx data/raw/2026-11-19_EXP-001_calibration-mass-weighing/metadata.md
git status
git diff --cached --stat
git commit -m "Record calibration mass weighing (EXP-001) and BME280 advice" -m "The owner weighed every calibration piece three times on the school's 0.01 g balance. The pieces are -2.5 % to +1.1 % off nominal, so the measured masses are used. Adds the raw sheet and its metadata as the first dataset and a blank weighing form, and corrects the weight-set and balance entries: the set bought is not the planned 17-piece set. Records where the BME280 sits and why. Backfills ff2ac6e."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should show 18 paths under "Changes to be committed" and nothing left over.
- **Harmless warnings:** "CRLF will be replaced by LF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
