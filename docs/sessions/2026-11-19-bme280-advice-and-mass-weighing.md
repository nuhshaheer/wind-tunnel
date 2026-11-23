# 2026-11-19: BME280 advice and calibration mass weighing (continued to 2026-11-22: SDP810 cable, wiring advice, paper reviews)

- **Session ID:** 7aeaf588-f591-40d7-8bbd-9e8c175822d0
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** `fd20afe` (the work up to the first `/wrap`, 2026-11-19); the continuation (2026-11-19 evening to
  2026-11-22, second `/wrap`) not committed yet

The session ran over four days with one conversation. Each section below covers the first part (to the first `/wrap`)
and then, under **Continued**, the rest.

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `ff2ac6e` (the 2026-11-18 breadboard session, committed and pushed by the owner). Clean
  working tree; the owner's original photos (three with GPS data) were no longer in `docs/images/`. `check_docs.py`
  0 failures and 0 warnings (777 links); 20 tests OK in 17.4 s.
- Discrepancies found and fixed at this wrap: PROJECT_STATUS still named `8904785` as the last commit and the
  breadboard session as uncommitted; the 2026-11-18 log and index row lacked `ff2ac6e`; the original-photo warning
  was out of date.
- No set objective. The owner, at school, asked about the BME280 and then asked for a spreadsheet to weigh their
  calibration weights on a school balance.
- **Continued:** after the first `/wrap` the owner committed and pushed `fd20afe` (`sync_status.py`: `UP_TO_DATE` on
  2026-11-22). The owner then asked bench questions (SDP810 plug, load-cell wiring) and, on 2026-11-22, asked the agent
  to read the five papers left unreviewed ("please go through these 5 papers thoroughly").

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

**Continued (2026-11-19 evening to 2026-11-22):**

- **SDP810 cable.** The owner's ready-made 4-pin PH 2.0 cable first would not push onto the sensor's pins. The agent
  ruled out a wrong plug or pitch (the holes lined up), advised not to force it and recommended soldering wires on.
  The owner then pushed it on: a stiff fit, not a misfit. Soldering advice withdrawn; before-power checks given (mark
  the orientation, pins straight, no shorts, wire colours mapped to pins from a photo). Recorded in open question 19,
  TODO and the setup (§4).
- **Another builder's sensor mounting** (owner's video frames). The barbs on the box edge are tube fittings through the
  wall, one pair per sensor; the sensors sit behind them, probably each on its own small board. From the perfboard
  pitch the ports look about 5 mm apart, against the SDP810's 12.6 mm, so probably a different sensor (rough estimate
  from a blurry frame). The idea carries over: fix the sensor to a bracket through its two mounting holes and run the
  outside tubes to fittings, so nothing pulls on the sensor or its plug. A thin grey strip in the frame could not be
  identified; best guess, the holder's side wall catching the light. An SDP810 bracket was offered for the sizing list;
  the owner did not take it up.
- **Load-cell wiring advice** (TAL221 to HX711):
  - Soldering an extension with heat-shrink (shrunk with a lighter held above the flame, at least 5 cm from the cell's
    body) is fine, but probably not needed: the HX711 can sit beside the cell, whose own 110 mm wires reach its pads.
    The TUOFENG 24 AWG silicone wire is for the HX711-to-Arduino cable, whose length depends on the layout (buy list
    estimate about 3 m for all sensor cables, a guess).
  - The load-cell wires go to the pads of the same colour: red RED (E+), black BLK (E−), green GRN (A+), white WHT
    (A−); YLW stays empty. Checked against the TAL221 datasheet notes and SparkFun's labels. Never through a plug or
    breadboard. If adding weight lowers the reading, swap green and white or flip the sign in software.
  - Calibration happens through the HX711, on the finished balance module. The cell alone gives only about 0.06 mV for
    2 g (about 3 mV at 100 g). Order: resistance check at the free ends, solder to the HX711, coin test, then the real
    calibration.
  - Datasheets offered (Bosch BME280, SparkFun's HX711 schematic for the RATE jumper); the owner said "nvmr".
- **Papers reviewed thoroughly** at the owner's request, chapter by chapter, with equations, tables and charts read
  from the page images where the text layer was garbled:
  - [Barlow1999](../../resources/notes/Barlow1999.md): chapters 7 (balances), 12.1–12.3 (uncertainty), 4 (pressure
    and flow measurement), 6 (test-section calibration), 9 and 10 (boundary corrections, 2-D and 3-D). PDF page =
    printed page + 11. Summary, chapter notes, follow-up references and a 13-item owner checklist.
  - [Morel1975](../../resources/notes/Morel1975.md) (6-item checklist), [Anthoine2004](../../resources/notes/Anthoine2004.md)
    (6 items), [Bradshaw1964](../../resources/notes/Bradshaw1964.md) (8 items).
  - The resources index rows set to Reviewed 2026-11-22. The places in the docs that said "confirm in Barlow1999"
    (open questions 8 and 10, the buy list §5, the Cooper1998 notes, PROJECT_BACKGROUND) updated.
  - TODO: the review task replaced by two tasks, the owner's check of the notes and a decision on ten proposals
    (image sting, sealed load-cell box, calibration details, S − E calibration with the shield in and at every speed,
    chamfered probe tip, E-ring and last-screen positions, diffuser screen lands, coarse-grid repeat, static-pressure
    gradient, uncertainty method). All Proposed.
- **Follow-up questions answered:** for the probe chamfer and alignment nothing new is needed (tube cutter, pin vise,
  drill bits and 220–600 sandpaper are on hand; a printed guide plus a rock-the-probe check). For the coarse-grid test,
  a piece of ¼ in galvanized hardware cloth clamped at a spare settling-chamber joint; **the owner agreed it runs at the
  end**, after the main validation, so only the spare joint goes into the sizing and the mesh is bought later. g =
  9.81 m/s² is adequate (within about 0.2 % at latitudes 25–60°).

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
- **Continued:**
  - New: `resources/notes/Barlow1999.md`, `resources/notes/Morel1975.md`, `resources/notes/Anthoine2004.md`,
    `resources/notes/Bradshaw1964.md`.
  - Modified: `PROJECT_STATUS.md`, `TODO.md`, `PROJECT_BACKGROUND.md`, `docs/buy_list.md`, `docs/experimental_setup.md`,
    `resources/README.md`, `resources/notes/Cooper1998.md`, this log, `docs/sessions/SESSION_LOG.md` (this row).
  - Equipment: the SDP810 now has its PH 2.0 cable pushed on (owner); not powered, not on the breadboard. Nothing else
    changed.

## 4. Experimental procedures performed

The owner, at school, 2026-11-19 (the agent performed none of it):

1. Labelled each multiple piece with tape and a number (#1, #2, ...); the single 50 g piece and the hanging rod were not
   taped.
2. Balance CGOLDENWALL HZ50002B (capacity 5000 g, d = 0.01 g), level bubble centred; empty pan read 0.
3. Each piece weighed three times, taken off between readings, with the balance **re-zeroed before every reading**.
   No separate empty-pan reading was written at the end (owner: re-zeroing gives 0). Room temperature not recorded;
   handling (tweezers or fingers) not recorded.

**Continued:** the owner pushed the ready-made PH 2.0 cable onto the SDP810's four pins (2026-11-19 evening; "it was
just a bit hard to push so i thought i was breaking it"). No power, continuity or orientation check reported yet. No
other physical work; the agent performed none.

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

**Continued:**

```bash
python scripts/sync_status.py --fetch                      # UP_TO_DATE at fd20afe (2026-11-22, during the review and at this wrap)
python scripts/check_docs.py; python -m unittest discover -s tests -v
# Paper reading, in the scratchpad (scripts not kept in the repo):
#   PyMuPDF (fitz, Python 3.11) extracted each PDF's text layer page by page into <key>.txt
#   sections.py <key> [first page] [offset]   lists chapter and section starts (Barlow1999: PDF page = printed + 11)
#   pp.py <key> <first> <last>                prints PDF pages from the text dump
#   PyMuPDF page renders (PNG) for every equation, table and chart used in the notes, read as images
#   short Python checks of the blockage and gravity arithmetic (results in the Barlow1999 notes, ch. 4, 7 and 10)
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

**Continued.** No measurements. Literature values and our arithmetic from them (not results; owner check of the
readings pending), details in the [Barlow1999 notes](../../resources/notes/Barlow1999.md):

- Sphere blockage in the 100 mm test section, with C_Du = 0.44 for illustration: wake blockage ε_wb = (5/4)(S/C)C_Du
  = 0.0157 (3/4 in) and 0.0279 (1 in); solid blockage ε_sb = 0.35 % and 0.82 % (Thom, K = 0.96), or 0.43 % and 1.03 %
  (1.5 V, τ₁ ≈ 0.8). Total q correction (1 + ε)²: **+3.9 to +4.0 %** (3/4 in) and **+7.4 to +7.8 %** (1 in). Spread
  between the two solid-blockage forms: about 0.08 % and 0.2 % in q.
- Horizontal buoyancy: ΔC_D,B = −λ₃ t (dp/dx)/q with λ₃ = 1 for a sphere (our derivation); an illustrative gradient of
  1 % of q per 100 mm gives about +0.0019 in C_D (0.4 %) for the 3/4 in ball. The real gradient is Unknown until
  measured.
- Sting tare plus interference: Barlow gives 10–50 % of an airplane's minimum drag; our earlier estimate for the
  shielded sting is 8–16 % of the 3/4 in ball's drag (0.1–0.2 gf with about 5 mm exposed).
- Square-nosed total-pressure tube: errors begin near 8° of flow inclination (Barlow p. 154), not ±10° as the buy
  list assumed.
- Local gravity: 9.7896, 9.8062 and 9.8192 m/s² at latitudes 25°, 45° and 60° (Barlow Eq. 7.13), so 9.81 m/s² is
  within about 0.2 % there.
- Morel1975's last-screen rule: about 0.2 D₁ before the contraction, about 50 mm with the 250 mm side or about 56 mm
  with the equivalent diameter (282 mm); about 60 mm proposed for the sizing.
- Anthoine2004 arithmetic for a possible 6.35 mm rod in the 100 mm section: −4.8 % (Allen and Vincenti) or −6.8 %
  (Maskell) in C_D (not planned; cylinders only).

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
- **Continued:**
  - During the review: `check_docs.py` 0 failures, 0 warnings (847 links); 20 tests OK.
  - At the second wrap: `python -m unittest discover -s tests -v`: 20 tests OK in 20.1 s (Python 3.11.0).
    `python scripts/check_docs.py`: 0 failures, 0 warnings (857 links; 19 session logs, each indexed once; 118
    committable files, none over 25 MiB).
  - Paper readings: each equation, table and chart value used was read from the PDF page image, not only the text
    layer. The arithmetic (blockage totals, gravity values) was rechecked with Python, which corrected two of the
    agent's figures (§8). The owner has **not** yet checked the readings against the PDFs (checklists at the end of
    each notes file).
  - **Not performed:** any SDP810 power, continuity or orientation check (owner task); any TAL221 resistance check;
    any physical test.

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

**Continued:**

- **SDP810 plug, a false alarm:** the agent first recommended soldering wires to the pins because the plug would not
  go on; the owner then pushed it on. Advice withdrawn. Lesson recorded: this PH 2.0 cable is a stiff fit on these pins.
- **The agent's earlier assumption was wrong:** the buy list said the home-made probe is good to about ±10° of
  misalignment; Barlow1999 says errors start near 8° for a square nose. Corrected in the buy list §5.
- **Barlow1999 misprint:** p. 138 prints the gravity formula's second coefficient as 0.053024; it should be 0.0053024
  (Eq. 7.13 on p. 242 prints it correctly). Noted in the Barlow1999 notes and the owner checklist.
- **Arithmetic corrected before it reached the docs:** the 1 in ball's total q correction, first written 7.3–7.7 %, is
  7.4–7.8 %; the spread between the solid-blockage forms, first written ±0.1 %, is 0.08 % (3/4 in) and 0.2 % (1 in).
- **A wrong link fixed:** the matched-Re two-ball plan was linked to D-009; it lives in docs/experimental_setup.md.
- **Tooling:** a long Bash heredoc of notes text failed to parse ("unexpected EOF"), so the notes were written in parts
  with the Write tool and joined with `cat`; an awk command with an escaped `$` failed and was replaced by a Python
  script; an over-long tool output was written to a scratch file and read back; one Edit of resources/README.md did not
  match and was re-anchored.

## 9. Decisions and reasoning

- No new DECISIONS.md entry. Agent's advice recorded as Proposed, not decided: the BME280 stays in room air near the fan
  inlet in its own vented holder; no calibration masses under 2 g are needed.
- Agent's choices: file the owner's sheet in `data/raw/` unchanged and keep the facts that could not change in
  `metadata.md`, with interpretation in the data catalog (raw files are never edited); reset `docs/forms/` to a blank
  template, since the readings are kept in `data/raw/`; correct the drawings' parts list (item 76) as a dated note on
  revision D rather than a new revision, since no sheet changed.
- **Continued:**
  - No new DECISIONS.md entry. The ten proposals from the reading are listed in TODO P1 for the owner to accept,
    change or reject; accepted ones become sizing items or D-entries.
  - **Owner's decision (2026-11-22):** the coarse-grid turbulence test (proposal 8) runs at the end, after the main
    validation runs. Only a spare settling-chamber joint goes into the sizing; the mesh is bought later.
  - Owner's choice: SDP810 connects by the ready-made PH 2.0 cable (open question 19 answered; Implemented,
    unverified).
  - Agent's choices: log the continuation in this session's existing log (same session ID, as `/wrap` requires) rather
    than a new file; keep Bell1988 as the contraction basis, since Morel1975's separation criterion assumes Re of order
    10⁶ and the settling chamber here runs at about 4 × 10⁴; leave figure values out of the owner checklists (blind
    checks).

## 10. Open questions and blockers

- The weight set's Amazon listing (link or name), to record next to the data. Optional.
- Whether the hanging rod can hang from the calibration hook in place of the pan (check its shape at build step 5).
- The school balance's accuracy against a reference mass: Unknown.
- **After the wrap (owner):** the ready-made 4-pin PH 2.0 cable bought for the SDP810 (metal contacts in its holes;
  seller not recorded) lines up with the sensor's pins but cannot be pushed on by hand. Cause unknown: pins thicker
  than the contacts take, or too short to reach past the housing face. The agent advised not to force it and now
  recommends soldering wires to the pins, for example the cable's own wires with the plug cut off (PROJECT_STATUS open
  question 19). **Then the owner pushed it on:** "it was just a bit hard to push so i thought i was breaking it". A stiff
  fit, not a misfit, so the soldering advice is withdrawn. Before power: mark the plug's orientation (no key), check the
  pins are straight and that neighbouring wires do not short, and match each wire colour to its pin from the
  datasheet's p. 4 bottom view. The I²C scan (0x25) is the real test.
- Still open from 2026-11-18: whether R1, R2, their feed jumpers and the clipped wire were removed; the HX711 RATE
  jumper; how the SDP810 connects (open question 19); the BME280 step 1.
- **Continued (open at the second wrap):**
  - The SDP810 cable's wire colours against its pins: Unknown until the owner's photo; no power before then.
  - The owner's check of the four paper notes (33 checklist items in all: 13, 6, 6 and 8).
  - The ten proposals in TODO P1: undecided apart from the coarse-grid timing.
  - τ₁ for a square section (Barlow Fig. 10.3) and λ₃ at l/t = 1 (Fig. 10.1): owner's blind chart readings.
  - The tunnel's static-pressure gradient along the test section: Unknown until measured.
  - Optional: a rough latitude, to replace 9.81 m/s² with the local value.

## 11. Remaining tasks

- **Owner:** commit and push (§13); the BME280 step 1 at the bench; choose the SDP810 connection; the remaining arrival
  checks; choose the fan; send the sizing inputs (heat-set inserts, filament).
- **Agent:** the I²C scanner and the other bring-up sketches when wanted; sheet 12 pad names when approved; the sizing,
  now including the BME280 holder.
- **Continued (at the second wrap):**
  - **Owner:** commit and push the continuation (§13); the SDP810 before-power checks and photo; the TAL221 resistance
    check at the free wire ends before soldering to the HX711; check the paper notes; decide the proposals with the
    agent; the BME280 step 1.
  - **Agent:** map the SDP810 wire colours from the photo; fold accepted proposals into the sizing (at least the spare
    settling-chamber joint, the E-ring and last-screen positions if accepted).

## 12. Recommended first task for the next agent

Unchanged from 2026-11-18. Ask whether the owner is at the bench. If so, confirm R1, R2, their two feed jumpers and the
clipped wire are gone, then continue the BME280 step 1
([2026-11-18 log §12](2026-11-18-breadboard-power-and-part-checks.md#12-recommended-first-task-for-the-next-agent)),
and write the I²C scanner in `firmware/` when the owner reaches step 4. If the owner is away from the bench, start the
sizing with the settling-chamber spacing (PROJECT_STATUS open questions 13 and 15).

**Updated at the second wrap (2026-11-22):** the bench task above is unchanged. If the owner sends the SDP810 cable
photo, map each wire colour to SDA, GND, VDD and SCL from the SDP8xx datasheet's p. 4 bottom view (render the page with
PyMuPDF) and record it in docs/experimental_setup.md before any power. Away from the bench, go through the ten proposals
in TODO P1 with the owner first, because several change the sizing (image sting, sealed load-cell box, E-ring and
last-screen positions, diffuser screen lands, the spare joint); then start the sizing.

## 13. Manual Git commands (as given to the owner)

### First wrap (2026-11-19; the owner committed and pushed these as `fd20afe`)

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

### Second wrap (2026-11-22)

State at the wrap: `UP_TO_DATE` at `fd20afe`; nothing staged. 9 files modified and 4 new to commit.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add PROJECT_STATUS.md TODO.md PROJECT_BACKGROUND.md docs/buy_list.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md
git add resources/README.md resources/notes/Cooper1998.md
git add resources/notes/Barlow1999.md resources/notes/Morel1975.md resources/notes/Anthoine2004.md resources/notes/Bradshaw1964.md
git status
git diff --cached --stat
git commit -m "Record paper reviews (Barlow, Morel, Anthoine, Bradshaw)" -m "Reviews Barlow1999 chapters 4, 6, 7, 9, 10 and 12.1-12.3, Morel1975, Anthoine2004 and Bradshaw1964, with notes and owner checklists. Confirms the S-E airspeed method, works out the sphere blockage correction (+3.9-4.0 % in q for the 3/4 in ball, +7.4-7.8 % for the 1 in ball), corrects the probe's angle tolerance (errors from about 8 degrees) and lists ten proposals for decision. Also records that the SDP810's PH 2.0 cable is a stiff fit and is pushed on, not yet powered."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should show 13 paths under "Changes to be committed" and nothing left over.
- **Harmless warnings:** "LF will be replaced by CRLF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
