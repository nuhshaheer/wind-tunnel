# 2026-11-26: Build step 1, the sizing

- **Session ID:** 232da8f2-034e-40d6-a20f-259c7903ef86
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** not committed yet

## 1. Starting state and objective

- `/catchup`: `python scripts/sync_status.py --fetch` gave `UP_TO_DATE` at `ac895a3` (the previous session, committed
  and pushed by the owner). No local changes. check_docs 0 failures, 0 warnings; 20 tests OK in 13.1 s.
- Discrepancies found at the catch-up:
  - PROJECT_STATUS's header and the SESSION_LOG row still called the 2026-11-25/26 session "not committed yet"
    (expected lag; backfilled in this wrap).
  - The TODO P1 task "Confirm the microcontroller / DAQ" was stale: most of its check had been met.
  - PROJECT_STATUS.md is about 110 KB, far from "a concise snapshot" (raised before; owner's call).
- Objective (owner): "lets work on build step one today", then "lets do all the decisions we can. finalize everything.
  then update the drawings in the main html. and then ill get started on the CAD".

## 2. Work completed

- **Tools advice** (owner's questions):
  - Buy a multimeter: the owner chose an AstroAI True RMS 6000-count meter.
  - Buy a heat-set insert tip for the Hakko FX-888DX (T18 series, with an M3 size), and flush cutters.
  - A heat gun is optional for the tunnel; it is mostly useful for the owner's robot projects. Keep it away from PLA
    and acrylic.
  - No oscilloscope is needed for the tunnel. For the owner's later myCobot 280 and lidar-robot projects: a FNIRSI
    DSO-510 (1 channel, 10 MHz, about $37) plus a USB logic analyzer, or a 2-channel 2C53T (about $100); borrow the
    friend's FNIRSI DST-201 (1 MHz) first.
  - Recorded in the shopping list's new "Tools for the build" table.
- **Facts recorded from the owner:**
  - The multimeter used so far is a friend's FNIRSI DST-201.
  - Soldering station: Hakko FX-888DX with T18 tips. Solder, flux and wick are at home.
  - Inserts: a Kadrick M2–M5 kit. M3 in 3/4/5/6/8 mm lengths; Ø4.5 top and Ø3.9 bottom per the seller's table (the
    owner sent the table; a caliper check is still pending).
  - Foam tape 1/4 in wide. Stainless M3 screws: 6, 8, 10, 12, 16, 20, 25 and 30 mm.
  - The owner made the repository public, to show recruiters.
- **Contraction:**
  - `cad/sizing/contraction.py` writes the 5th-order wall as a Fusion points file, in cm because ImportSplineCSV reads
    cm, plus a mm copy, and prints the station table, slopes, curvature, joint options and a filament estimate.
  - Sheet `cad/sizing/contraction.md`.
- **Decisions made with the owner,** each with numbers and my recommendation first (D-022 to D-031, below). Two
  to-scale explainer pages were published privately for the owner on claude.ai:
  - "Splitting the 250 mm Sections" (https://claude.ai/artifact/UFEmwtqjkPqvZEFhCvpwqZ): why the sections don't fit,
    options A and B, the S taps, and the flange with the inserts;
  - "Test Section Layout" (https://claude.ai/artifact/8apGKDE8i8ndfXCnXVSCdT): side view, the section at the ball, the
    three choices, the sealed box (leaky against sealed) and the image sting (runs 1 and 2).
- **Dimension sheets in `cad/sizing/`:**
  - files: README (index and drawing order), contraction, flanges, coupons (C1–C7), test_section, diffuser,
    settling_chamber, balance, supports;
  - points files from `profiles.py`: the diffuser's two loft rails and the NACA shield section, in cm, with mm copies.
- **Drawing package revision F:** stations, joints, bolt patterns, seams, taps, window and black wall, sealed box, image
  run (new view H on sheet 8, items 55–57), probe and cradles. Parts list, TBD register, findings and title blocks
  updated; every changed sheet previewed and fixed.
- **The owner confirmed** D-004, D-006, D-007's open exit, D-016, D-018, D-019 (`AVERAGE_OVER = 1`) and D-021,
  after plain explanations of D-004 and D-021.

## 3. Files and equipment affected

- New: `cad/sizing/`, 17 files. Sheets: `README.md`, `contraction.md`, `flanges.md`, `coupons.md`, `test_section.md`,
  `diffuser.md`, `settling_chamber.md`, `balance.md`, `supports.md`. Scripts: `contraction.py`, `profiles.py`. Outputs:
  `contraction_wall_fusion_cm.csv`, `contraction_wall_mm.csv`, `diffuser_rail_flats_cm.csv`,
  `diffuser_rail_diagonal_cm.csv`, `shield_section_cm.csv`, `profiles_mm.csv`.
- Changed: `DECISIONS.md` (D-022 to D-031; confirmation notes on D-003, D-004, D-006, D-007, D-016, D-018, D-019,
  D-021; D-011 marked superseded), `PROJECT_STATUS.md`, `TODO.md`, `README.md`, `CLAUDE.md`, `PROJECT_BACKGROUND.md`,
  `docs/experimental_setup.md`, `docs/buy_list.md`, `docs/shopping_list.md`, `resources/README.md`,
  `docs/sessions/SESSION_LOG.md`, the 2026-11-26 shield-order log (commit backfill only).
- Drawing package: `wtdata.py`, `wtsheets.py`, `wtlib.py`, `s_ga.py`, `s_ga2.py`, `s_d1.py`, `s_d1b.py`, `s_d2b.py`,
  `s_d3b.py`, `page.py`, `README.md` and the rebuilt `wind-tunnel-drawings.html`.
- Equipment: none changed. Nothing was built, printed or measured.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch
python cad/sizing/contraction.py          # points files + station table, slopes, joint options, filament estimate
python cad/sizing/profiles.py             # diffuser rails, shield section
python docs/drawings/page.py              # rebuild the drawing package (prints "parts never drawn: []")
python docs/drawings/preview.py 1 7 8 10  # then 2 5 6 8 9, then 4 9: PNG previews (Edge), ignored by Git
python scripts/check_docs.py
python -m unittest discover -s tests -v
```

Also run (scratchpad scripts, not kept):
- `cr_compare.py`: the chamber-size comparison.
- An inline diffuser and chamber station calculation.
- `patch_drawings_f.py`: 134 exact replacements across 9 drawing files; it writes nothing unless every one matches.
- `patch_items_f.py`: the parts list.
- `patch_page_f.py`: the register, findings and header.
- `patch_fix2.py` and `patch_fix3.py`: overlap fixes.
- The wrap scripts for PROJECT_STATUS, TODO, the setup doc and the other docs.

Web searches (standard):
- the FNIRSI DST-201 and DSO-510 specs;
- whether ImportSplineCSV reads cm (Autodesk forum: it does);
- budget multimeters and oscilloscopes;
- T18 heat-set insert tips.

## 6. Measurements and results

No measurements. All numbers below are our arithmetic or layout, not results.

- **Contraction** (D-022): y = 125 − 75(6s⁵ − 15s⁴ + 10s³), s = x/250.
  - Steepest wall 29.36° at x = 125. Tightest bend radius 158 mm, at x = 52.8 and 197.2.
  - Joint positions for a one-piece downstream part: x = 76.9 / 81.6 / 86.1 mm for 10 / 12 / 14 mm flanges. Chosen
    x = 82 (inside 219.69, flange 249.69).
  - A solid 3 mm shell is about 691 g of PLA, flanges not included.
- **Chamber-size comparison** (220 / 250 / 280 / 300 mm), at 13 m/s:

  | Chamber | 220 | 250 | 280 | 300 |
  |---|---|---|---|---|
  | Contraction ratio | 4.84 | 6.25 | 7.84 | 9.0 |
  | 1/c | 0.207 | 0.160 | 0.128 | 0.111 |
  | u′/U factor | 0.084 | 0.054 | 0.036 | 0.028 |
  | Loss per chamber screen (Pa) | 6.4 | 3.9 | 2.5 | 1.9 |
  | Diffuser K_sum needed | 1.46 | 2.14 | 2.91 | 3.47 |
  | Contraction shell (g, estimate) | about 471 | about 691 | about 971 | about 1194 |
  | Fits the bed in one piece | yes | no | no | no |

- **Blockage and wake room** (estimates):
  - 1 in ball: blockage 5.07 %, correction about 7 %. A 1¼ in ball would be about 7.9 % blockage, about 11 %
    correction, and need about 335 mm of test section.
  - Exposed sting tare: about 8–16 % of the 3/4 in ball's drag, 4–9 % of the 1 in ball's (estimate).
  - 4√S behind the 1 in ball is 90 mm, so the test section needs 309 mm; 270 mm gives 2.3√S.
- **Diffuser:** half-angle at mid-length 22.8° across the flats (2θ 45.6°) and 40.8° along the diagonal. The
  mid-section is 231 mm across with its flange. Three screens give K about 3.2 for about 8 Pa more than two.
- **Flange:** bolt line 9 mm from the inside face, leaving about 3.75 mm of plastic around the 4.5 mm insert.
  - Screw lengths: M3 × 12 engages about 4 mm (6 + 2 + 4). Screen joints: M3 × 16. Coarse-grid day: M3 × 20.
  - Foam-tape bending between bolts 90 mm apart: about 0.03 mm (assumes 20 kPa on the tape and E = 2.5 GPa).
- **Shield:** NACA 4-digit section, chord 22.5, t/c 1/3. Half-thickness 3.75 at 30 % chord, leaving 1.25 of wall
  around the Ø5 bore. Trailing edge cut at x = 21.27 (0.96 thick).
- **Heights:** box bottom 145 below the axis (with the mount stacked on the cell), chamber flanges 140. Axis 175 above
  the bench; the box clears by 30. Tunnel about 1.34 m.

## 7. Tests, calibration checks and validation

- `contraction.py` checks: y(0) = 125, y(250) = 50, zero slope and curvature at both ends, monotonic; y(125) = 87.5.
- `profiles.py`: rails run 76 → 125 and 76 → 176.78; the shield's maximum half-thickness is 3.750 at 30 % chord.
- Drawing package: `python docs/drawings/page.py` → `parts never drawn: []` (71 items).
- Previews of sheets 1, 2, 4, 5, 6, 7, 8, 9 and 10 were inspected. Overlaps found and fixed: view H on sheet 8, the
  probe note and plan dimension on sheet 7, two callouts on sheet 5, a schedule row on sheet 2, the probe dimension on
  sheet 9. Sheet 3 was not previewed (text-only changes).
- At the wrap: `python -m unittest discover -s tests -v` and `python scripts/check_docs.py`, results in §13.
- **Not performed:** nothing was printed or measured. The insert sizes are the seller's table, not a caliper reading.
  The Fusion import of the points files was not tried (the cm unit rests on Autodesk forum answers). The S6's collar
  and axis height are not measured.

## 8. Errors, failed approaches and troubleshooting

- **Option A first put its seams exactly where the S taps go** (mid-wall). The owner spotted it ("werent we planning
  on putting taps for the sdp 810?"). The agent's first fix, a pinwheel of unequal pieces with the seams 40 mm
  off-centre, was replaced by the owner's simpler layout: mid-wall seams with each tap about 20 mm beside its seam.
- **The balance stack:** the first balance sheet put the mount beside the cell (box 140 below the axis). The drawings
  stack it on the cell, so the box is 145. Corrected in the balance and supports sheets.
- **A cradle under the extension joint (x = 245) landed inside the load-cell box** (x 156–256). Moved to x ≈ 290.
- A Bash heredoc with typographic quotes failed to parse; the script was rerun from a file.
- The first drawing patch missed one note list (15 spaces of indent, not 16). The script wrote nothing until every
  replacement matched.
- Recorded on D-022: the owner's "250mm" answered a question about both the chamber and the contraction's 250 mm
  length and curve. Both were recorded as Accepted on that basis, with that note.

## 9. Decisions and reasoning

All in [DECISIONS.md](../../DECISIONS.md):

| Decision | What |
|---|---|
| D-022 | 250 mm chamber (ratio 6.25); 250 mm contraction with the 5th-order wall |
| D-023 | 250 mm sections as four identical corner pieces glued at mid-wall seams; S taps 20 mm beside the seams; contraction split at x = 82 |
| D-024 | Test section 310 mm (front body 245 + extension 65); one window and a black wall; E taps in all four walls at 56; M taps in the side walls at 206, 12 above the floor |
| D-025 | The S6 fan (supersedes D-011) |
| D-026 | Diffuser: three screens, 175 mm |
| D-027 | Compact 275 mm chamber |
| D-028 | Sealed load-cell box with a gasketed access door |
| D-029 | Image sting; 5 mm gap kept; image balls drilled at both poles |
| D-030 | Probe straight through the open exit on a stand |
| D-031 | Repository public (supersedes D-003's visibility) |

- The owner also confirmed D-004, D-006, D-007's open exit, D-016, D-018, D-019 and D-021.
- The flange standard, bolt patterns, wall thickness, heights, the honeycomb mount and the balance sizes are
  **Proposed** in the sheets, to be settled by the coupons and the owner's CAD.

## 10. Open questions and blockers

- The copyrighted PDFs in the public repository (D-031). Options: links, links plus a history purge, or leave them.
- Hole sizes, from coupons C1–C6. The fan's collar diameter and axis height, measured when the S6 arrives.
- One insert's real dimensions (caliper check).
- The 2026-11-22 proposals still undecided: #3, #4, #9 and #10 (procedures).
- Not affecting the CAD: the HX711's excitation voltage and the rest of the bring-up items.

## 11. Remaining tasks

- **Owner:**
  - commit and push (§13);
  - decide on the PDFs;
  - buy the tools;
  - CAD, coupons first;
  - solder and test the shield when it arrives (about 6–8 December).
- **Agent:**
  - put the coupon results into the sheets;
  - check the exported STLs;
  - estimate the filament for the whole tunnel;
  - the combined logging sketch with the owner at the bench.

## 12. Recommended first task for the next agent

Ask for the coupon results (C1–C5) or the first STL exports, and check them against the `cad/sizing/` sheets: bed fit,
key dimensions, bolt holes matching between mating parts. Put the measured hole sizes into `flanges.md` and
`coupons.md`. If the owner hasn't decided on the copyrighted PDFs yet, ask first: the repository is public.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `ac895a3`; nothing staged; 24 files modified and 2 new paths (`cad/sizing/`, 17
files, 96 KB; this log), all from this session.

Checks after editing:
- `python -m unittest discover -s tests -v`: 20 tests OK in 8.2 s.
- `python scripts/check_docs.py`: 0 failures, 0 warnings. 23 session logs indexed once, 1,098 links and anchors
  resolve, 5 catalogued paths exist, 179 committable files, none over 25 MiB, no secrets.
- `python cad/sizing/contraction.py`, `python cad/sizing/profiles.py` and `python docs/drawings/page.py` rerun cleanly
  (`parts never drawn: []`).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add CLAUDE.md DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md README.md TODO.md
git add docs/buy_list.md docs/shopping_list.md docs/experimental_setup.md resources/README.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-26-shield-order-and-load-cell-bench-test.md docs/sessions/2026-11-26-build-step-1-sizing.md
git add docs/drawings/README.md docs/drawings/page.py docs/drawings/s_d1.py docs/drawings/s_d1b.py docs/drawings/s_d2b.py docs/drawings/s_d3b.py
git add docs/drawings/s_ga.py docs/drawings/s_ga2.py docs/drawings/wtdata.py docs/drawings/wtlib.py docs/drawings/wtsheets.py docs/drawings/wind-tunnel-drawings.html
git add cad/sizing
git status
git diff --cached --stat
git commit -m "Size the tunnel for CAD (build step 1, D-022 to D-031)" -m "Every remaining tunnel decision was made with the owner: 250 mm chamber and 250 mm 5th-order contraction, four corner pieces glued at mid-wall seams, a 310 mm test section with one window and a black wall, the S6 fan, a three-screen diffuser, a compact chamber, a sealed load-cell box, the image sting and the probe route. Adds one dimension sheet per part and the Fusion points files in cad/sizing/, brings the drawing package to revision F, records the public repository (D-031) and the owner's confirmation of the older tentative decisions, and backfills ac895a3."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 42 paths under "Changes to be committed" (24 modified; 18 new: the 17
  files in `cad/sizing/` and this log) and nothing left over.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored. Several docs were rewritten with LF line endings;
  Git stores text as LF anyway (`.gitattributes`), so the diffs show only real changes.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
