# 2026-11-26: Copyrighted PDFs untracked, decisions register, CAD started

- **Session ID:** 58385934-435c-40fe-952c-80e6f4ec17a2
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** `83d6fad`

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `f210b9e` (build step 1, the sizing, pushed by the owner). The first task found was the
  copyrighted PDFs still tracked in the repository, which went public earlier that day (D-031).
- The owner's requests, in order:
  1. "do a": D-031 option (a). Untrack the publisher PDFs, keep the local copies, link them online.
  2. Make PROJECT_STATUS clear about what is decided and what is not, so later agents don't mix them up.
  3. "lets work on the cad": guide the owner's Fusion 360 drawing (D-017). The owner's method is to draw each piece
     whole, then cut it and add the flanges.

## 2. Work completed

**Copyrighted PDFs (D-031 option (a)).**
- 13 publisher PDFs untracked with `git rm --cached` (staged as deletions) and listed in `.gitignore`.
- The local copies were not touched: SHA-256 of all 23 PDFs was taken before and after, and every hash matched.
- `resources/README.md` links each one online (DOI or publisher page) and says "PDF local only (D-031)". A new step in
  "Adding a paper" says to check the licence first.
- The 12 notes files no longer link the PDF files.
- Still tracked, all NASA, AGARD or vendor documents: Bell1988, Cooper1998, HX711, SDP8xx, Scheiman1981,
  Sensirion2024, TAL221 and WaveshareBME280.
- Not done: the PDFs are still in the old commits on GitHub. That would need option (b), a history purge, which was not
  chosen.

**Decisions register.**
- New section in PROJECT_STATUS: "Decisions: what is decided and what is not". It sets the rules (only the owner
  decides; a Proposed value is not a decision) and has three parts:
  - a table of D-001 to D-031 with their current status;
  - the owner's choices that are recorded outside DECISIONS.md;
  - a "Not decided yet" table.
- DECISIONS.md: every Status line now starts with the current status and keeps the older wording after it. Rewritten:
  D-002, D-003, D-004, D-006, D-007, D-008, D-011, D-016, D-018, D-019, D-020, D-021, D-030 and D-031. D-027 has a
  note that 1.34 m is the length to use.
- Stale "Tentative" labels fixed in PROJECT_STATUS, TODO and docs/experimental_setup.md.
- The rule is now in CLAUDE.md and in the `/wrap` checklist.

**CAD guidance.** The owner drew these in Fusion this session. None of them is exported to `cad/` yet. The agent
checked them only from the owner's screenshots and measurements.

| Part | What the owner has drawn | Status |
|---|---|---|
| Diffuser, whole | Curved loft from Ø152 to the 250 square (end condition Direction, 0°); 3 mm wall by Shell, direction Outside | In progress: still to cut at x = 87.5 |
| Diffuser round flange | 8 thick, Ø152 / Ø182, 6 × Ø4.0 × 6 deep holes on a Ø170 circle, 30° from the top | Drawn |
| Diffuser square flange | 6 thick, 280 square, 12 × Ø3.4 through (J250 pattern) | Drawn |
| Fan inlet ring | 40 long overall. Socket 156.1 inside / 162.1 outside, then a Ø152 step, then a Ø182 flange with 6 × Ø3.4 | Drawn, using the 6 in collar placeholder |
| Screen 12a frame | Ø152 / Ø182, 6 holes; print two layers | Drawn |
| Settling chamber C1 | 125 long overall (flanges included); four corner wedges with the point at x = 17 and the flat face at x = 25, 8 legs | Drawn |

The ring's and frame's holes line up with the diffuser's (checked from an end view).

Questions answered along the way:
- **Equation curves:** Fusion has no equation-curve tool, but two of the three curves are exactly Bézier curves.
  - The contraction wall is a degree-5 control point spline.
  - Each diffuser rail is a degree-3 control point spline.
  - Both scripts now print the control points and check them against the equations.
- **Fan inlet socket:** inside Ø = collar + 2 × 1.6 neoprene + 0.5 = 156.1 with the nominal 6 in collar (owner: "we can
  say 6 in for now"). The wall is added outside the hole. The owner's first figure of 158.75 is not used.
- **Flanges:** they run all the way round, not as four corner tabs. Reasons: the foam seal, clamping the screens, and
  about 80 times less bending between bolts.
- **The Ø170 bolt circle:** it is a construction circle, not a visible edge.
- **Why the whole diffuser is cut at x = 87.5:** that is screen 12b's joint, and both halves then share the same
  section.
- **Section lengths:** the chamber sections' 125, 50 and 100 include their flanges.
- **Wedge size:** 8 legs, flat face toward the honeycomb. No chamfer is needed: the air there is about 2 m/s and the
  honeycomb straightens it. The owner left them as drawn.

**Sheet corrections found while preparing the CAD (all agent, Proposed):**
- **[diffuser.md](../../cad/sizing/diffuser.md):**
  - the "Simpler alternative" (Direction, 0°) and the Shell Outside step, with a warning about Ø155;
  - D1 now prints standing on its mid-section screw flange. The first version stood it on its inlet end, which put
    the screw-head face underneath;
  - the "lands" claim now holds only at screens 12a and 12c. At 12b the walls are at their steepest.
- **[flanges.md](../../cad/sizing/flanges.md):**
  - pin holes at 130 and 136 from the centre line;
  - a counted joint table: 9 joints, 18 flanges, 94 inserts and 94 screws (54 M3 × 16, 40 M3 × 12). It replaces
    the first estimate;
  - why the flange is continuous.
- **[settling_chamber.md](../../cad/sizing/settling_chamber.md):**
  - the corner-wedge shape;
  - the mist port lands on a glued seam (three options for the owner);
  - the S-tap boss clears the chamfer by about 1 mm.
- **[test_section.md](../../cad/sizing/test_section.md):** "Still open" items 1–3 marked as settled (balance sheet,
  D-030, D-029).
- **[contraction.md](../../cad/sizing/contraction.md):** Option A, the degree-5 control point spline, with its check
  values.
- **[README.md](../../cad/sizing/README.md):**
  - a table of Fusion user parameters;
  - the fan inlet socket formula;
  - derived positions (125, 128, 134, 140);
  - the "Curves without importing points" table.

## 3. Files and equipment affected

- **Untracked, kept on disk (staged deletions):** 13 PDFs in `resources/`: Abdelhamed2014, Anthoine2004,
  Bradshaw1964, Brown2003, Maskell1963, Mehta1977, Mehta1979, Morel1975, Morrison2013 (2 files), Roos1971, Weakly2024
  and Wieghardt1953.
- **Modified:**
  - `.gitignore`, `resources/README.md` and 12 files in `resources/notes/`;
  - `DECISIONS.md`, `PROJECT_STATUS.md`, `TODO.md`, `CLAUDE.md`, `.claude/skills/wrap/SKILL.md` and
    `docs/experimental_setup.md`;
  - in `cad/sizing/`: `README.md`, `contraction.md`, `contraction.py`, `diffuser.md`, `flanges.md`, `profiles.py`,
    `settling_chamber.md` and `test_section.md`;
  - `docs/sessions/SESSION_LOG.md`, and the build-step-1 log's commit hash backfilled to `f210b9e`.
- **New:** this log.
- **Not changed:** the points-file CSVs (the scripts reproduce them byte for byte), `data/` and the drawing package.
- **Equipment:** none.

## 4. Experimental procedures performed

None. No physical work this session. The owner drew CAD in Fusion 360. Nothing was printed or measured.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch
sha256sum resources/*.pdf > <scratchpad>/pdf_hashes_before.txt
python <scratchpad script> resources/*.pdf      # PyMuPDF: searched each PDF's first 40 pages for licence wording
git rm --cached --quiet resources/<the 13 PDFs listed in §3>
sha256sum resources/*.pdf | diff - <scratchpad>/pdf_hashes_before.txt   # no output: all identical
git ls-files resources                           # 8 PDFs left, all NASA, AGARD or vendor
python cad/sizing/contraction.py
python cad/sizing/profiles.py
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

## 6. Measurements and results

No measurements. Computed checks (Verified by script, `python cad/sizing/contraction.py` and `profiles.py`):
- **Contraction:** the degree-5 spline with control points (0, 125), (50, 125), (100, 125), (150, 50), (200, 50),
  (250, 50) mm matches the 5th-order equation to 2.2 × 10⁻¹³ mm over 2001 points.
- **Diffuser rails:** the degree-3 splines match the S-curve to 4.3 × 10⁻¹⁴ mm (flats) and 5.7 × 10⁻¹⁴ mm (diagonal).
  The flats run (0, 76), (58.333, 76), (116.667, 125), (175, 125); the diagonal is the same with 176.777.
- **Check values for Fusion:**
  - contraction: y = 120.656 at x = 50, and 87.500 at x = 125;
  - diffuser at x = 43.75: flats 83.656, diagonal 91.746.

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests -v`: 20 tests OK.
- `python scripts/check_docs.py`: 0 failures, 0 warnings, before and after the wrap's edits. After them: 24 session
  logs indexed once, 1,132 links and anchors resolve, 167 committable files, none over 25 MiB, no secrets.
- Both sizing scripts reran. `git status` shows no change to any CSV.
- PDF untracking: the SHA-256 comparison above matched, and `git ls-files resources` lists 8 PDFs.
- The owner's CAD was checked only from screenshots and measurements: wall thickness, flange diameters, hole circle and
  angle, the ring and frame holes against the diffuser's, and the wedge position. No STL or STEP export was checked.
- Not performed: any print, coupon or physical check.

## 8. Errors, failed approaches and troubleshooting

- **Agent replies too full of jargon.** The owner said "im confused… idk what all this means" after replies full of
  sheet jargon, parameter names and option tables. From then on the agent gave short, numbered Fusion steps, and those
  worked.
- **The owner's first diffuser loft was straight.** It used the default loft, which gives about 31° across the flats
  and breaks Mehta1977's curved-wall rule. Fixed with end condition Direction, 0°, on both profiles.
- **Ø155 outside gave a 1.5 mm wall.** Ø155 against Ø152 is 1.5 per side. Fixed with Shell, 3 mm, direction Outside,
  on the solid inside shape.
- **The corner wedges were first placed 8 mm too far in.** The owner caught it by measuring, and the point is now at
  x = 17.
- **The owner sent the old drawing (revision B) twice.** That is the private claude.ai copy, never republished. The
  repo's `docs/drawings/wind-tunnel-drawings.html` is revision F. Republishing needs the owner's go-ahead (asked, no
  answer yet).
- **Sheet errors found and corrected** (§2): D1's print orientation, the 12b lands, and the mist port on a seam (the
  mist port is still open).
- **Tooling:**
  - printing PDF text failed with UnicodeEncodeError (cp1252). Fixed with `sys.stdout.reconfigure(encoding="utf-8")`
    in the script; `python -I` ignores PYTHONIOENCODING;
  - a heredoc patch to `contraction.py` turned `'\\n'` into a real newline. Its match check stopped it before
    anything was written, and the change was redone with the Edit tool.

## 9. Decisions and reasoning

- **D-031 option (a)** (owner, "do a"): untrack the files now and keep the history. Recorded in a note on
  [D-031](../../DECISIONS.md).
- **Collar placeholder 6 in (152.4 mm)** (owner) until the S6's collar is measured.
- No new D-entry. Every CAD value given this session stays **Proposed** in the sheets until coupons or the owner settle
  it.

## 10. Open questions and blockers

- **Mist port:**
  1. a boss on all four C3 pieces at x = 240, 20 beside the seam (agent's recommendation);
  2. one piece only;
  3. leave it out for now.
- **Is the S6 being bought now?** The owner said "im buying the s6". D-025 and the 2026-11-10 choice say it is bought
  last, once the airspeed readout works.
- **Screws:** whether the assortment holds 54 M3 × 16 and 40 M3 × 12 (owner: "we can order more").
- **Tools and settings:** whether the T18 insert tip is ordered; the real print settings for the coupons.
- **Drawings:** whether to republish the drawings' claude.ai copy (revision B → F).
- **Optional:** a `check_docs.py` check that the register matches DECISIONS.md's Status lines (offered, no answer).

## 11. Remaining tasks

CAD, continuing in the owner's order:
1. **Settling chamber:**
   - C2: 50 long, 8 mm insert flange (12 × Ø4.0 × 6 deep) at the fan end, 6 mm screw flange (12 × Ø3.4) at the
     contraction end, 280 square, 45° chamfer under the insert flange;
   - C3: 100 long, the same flanges, plus four S-tap bosses 25 from its fan end, 20 off each wall's middle.
2. **Diffuser:**
   - cut at x = 87.5 and add the mid flanges: 6 thick Ø3.4 on D1, 8 thick Ø4.0 × 6 on D2, 12 holes on the curve 9
     out from the inside face;
   - cut D2 into four corner pieces.
3. **Corner pieces:** cut the chamber sections into four, with the pin holes.
4. **Small parts:** the honeycomb, four 50 mm corner spacers, and the screen frames 12b–12e.
5. **The rest:** the contraction, test section, balance and supports.

Coupons C1–C5 before any big part is printed. The owner will "do a test print later".

## 12. Recommended first task for the next agent

Ask the owner for screenshots of where they are in Fusion, then continue the CAD with settling chamber C2, in short
numbered steps ([settling_chamber.md](../../cad/sizing/settling_chamber.md), [flanges.md](../../cad/sizing/flanges.md)).
Remind them to commit and push this session first if they haven't.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `f210b9e`. The 13 PDF deletions are already staged (by `git rm --cached`). The
other changes are not staged.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first.
git status
git diff --stat
git add .gitignore CLAUDE.md DECISIONS.md PROJECT_STATUS.md TODO.md .claude/skills/wrap/SKILL.md
git add docs/experimental_setup.md docs/sessions/SESSION_LOG.md docs/sessions/2026-11-26-build-step-1-sizing.md docs/sessions/2026-11-26-pdfs-decisions-register-and-cad-start.md
git add resources/README.md resources/notes
git add cad/sizing/README.md cad/sizing/contraction.md cad/sizing/contraction.py cad/sizing/diffuser.md cad/sizing/flanges.md cad/sizing/profiles.py cad/sizing/settling_chamber.md cad/sizing/test_section.md
git status
git diff --cached --stat
git commit -m "Untrack publisher PDFs and add a decisions register" -m "The repository is public (D-031), so the 13 journal and publisher PDFs are untracked (kept on disk, listed in .gitignore) and linked online instead (option (a); they remain in the old history). PROJECT_STATUS gains one register of what is decided and what is not, and every DECISIONS.md Status line now starts with its current status. The sizing sheets gain Fusion user parameters, exact control point splines for the contraction and diffuser curves, a counted joint table and corrections found while the owner started the CAD."
git push origin HEAD
python scripts/sync_status.py --fetch
```
