# 2026-11-26: First CAD exports checked

- **Session ID:** 753e5d08-9cba-4cbf-ae82-09674414c3d2
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** not committed yet

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `83d6fad`. The owner had committed and pushed the previous session (the copyrighted PDFs
  and the decisions register) with the commands it gave. `check_docs.py` 0 failures, 20 tests pass.
- Discrepancies found at catch-up, all fixed at this wrap:
  - PROJECT_STATUS still named `f210b9e` as the last commit and listed the previous session's work as uncommitted;
  - the previous log and its index row said "not committed yet";
  - README.md called D-018 Tentative and marked build step 1 (sizing) as next.
- The owner's requests, in order:
  1. the honeycomb's size against the 250 mm chamber;
  2. "maybe you could just access the fusion files to check yourself": check the owner's first four exports;
  3. guidance on which edges to chamfer;
  4. recheck after each round of fixes, then record the decisions.

## 2. Work completed

**Honeycomb sizing.** The owner thought 249.4 was the wall's inside. Explained with a text diagram:
- the chamber is 250 inside;
- the honeycomb is 249.4 outside, a 0.3 gap on each side;
- the rim is 1.2, so 247 inside the rim.

The owner had suggested 244 inside; the agent recommended 247 (thinner rim, 1.9 % of the area blocked against 4.3 %).
The owner drew 247. It only has to slide in: the corner blocks at x = 25 and the spacers hold it, so it needs no grip.

**A gap in the sheet: what the spacers push on.** The air pushes the honeycomb onto four 50 mm corner spacers.
The sheet said screen 12d's frame stops them, but the frame's inside is 250, the same as the duct. So the corners hold
only the screen mesh, about 4 mm on past the foam tape and the frame's first layer.
- Proposed: four corner tabs on the upstream layer of 12d's frame, with the spacers kept 50 long (about 2 mm of play).
- The owner has not chosen yet.

**The exports.** The owner exported four parts from Fusion 360 as 3MF into `cad/main cad files/`. 3MF is better than
STL here, because it carries the units. The agent wrote standard-library scripts in the scratchpad (not kept, §5) to
read the meshes and measure them:
- cut sections at chosen planes;
- loop areas give the hole diameters, and loop centroids their positions;
- rays from the axis give the radii.

Three rounds:

| Part | Round 1 (19:05) | Round 2 (19:15–19:29) | Round 3 (20:01–20:07) |
|---|---|---|---|
| Honeycomb | Matches the sheet | not re-exported | not re-exported (needed nothing) |
| C1 | Six separate bodies (wall, insert flange, four corner blocks); no chamfer under the insert flange | One body; the slope is a **fillet** of radius 12, not a chamfer | **Matches:** straight 45° chamfer, 12 × 12 |
| Diffuser | 189 overall (flanges outside the 175 curve); no chamfer under the round flange | A fillet of about radius 10, plus a 2 mm flat strip | **Matches:** straight chamfer from the flange's edge to the wall |
| Fan ring | Socket tapered along an S-curve, Ø156.2 at the mouth to Ø152 at 28 deep | A straight cone, Ø156.2 to Ø152 | **Matches:** straight Ø156.1 bore, 27 deep, flat step to Ø152 |

Chamfer guidance. Some of the owner's screenshots marked the wrong edges:
- the front (joint) face's outer rim and its inner edge;
- then the back face's outer rim.

The agent explained the right edge with a text section: the inside corner where the flange's back face meets the wall's
outside, and only under insert flanges (never under screw flanges, where the screw heads sit). Equal distance 12.
Fusion refused 12 on the diffuser at first, probably because a 12 chamfer uses up the whole 12-wide face. The owner then
tried 10, but that was a fillet; the final chamfer reaches the flange's edge.

**Owner's decisions** (§9): keep the socket 27 deep and the diffuser 189 overall.

**Length.** The 1.34 m figure was the parts laid end to end, 1,342 mm. It now adds up to about 1.40 m (estimate):
- the diffuser and socket bring the parts to 1,357 mm;
- the five screen frames and the foam tape in nine joints add about 38 mm.

**Recorded in the docs:**
- notes on D-026 and D-027;
- the diffuser sheet's "As drawn" section;
- the settling-chamber sheet: the honeycomb and C1 as drawn, the corner blocks as drawn (flat-ended, not tapered), the
  spacer gap;
- the sizing README;
- the length, everywhere it was quoted;
- the drawings README: a list of where revision F now differs from the CAD;
- the catch-up discrepancies.

## 3. Files and equipment affected

- **New:**
  - `cad/main cad files/` with four 3MF files (owner's exports, 1.3 MB in all; metadata only a title and a thumbnail):
    - `Fan to Tunnel Joint.3mf` (104 kB)
    - `Honeycomb Section.3mf` (758 kB)
    - `Settling Chamber 1.3mf` (125 kB)
    - `Wide Angle Diffuser.3mf` (361 kB)
  - this log.
- **Modified:**
  - `DECISIONS.md` (notes on D-026 and D-027), `PROJECT_STATUS.md`, `TODO.md`, `README.md`, `PROJECT_BACKGROUND.md`;
  - `docs/experimental_setup.md`, `docs/drawings/README.md`;
  - `cad/sizing/README.md`, `cad/sizing/diffuser.md`, `cad/sizing/settling_chamber.md`;
  - `docs/sessions/SESSION_LOG.md`, and the previous log's commit hash backfilled to `83d6fad`.
- **Not changed:** the drawing package's sheets and `wtdata.py` (differences listed in its README), `data/`, firmware,
  scripts.
- **Equipment:** none.

## 4. Experimental procedures performed

None. No physical work this session. The owner drew and exported CAD; nothing was printed or measured.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch
python scripts/check_docs.py
python -m unittest discover -s tests
# Scratch scripts in the session scratchpad (not kept), run with python -I, standard library only:
python -I mesh3mf.py "cad/main cad files/"*.3mf        # units, size, triangle count, closed-solid check, volume
python -I check_parts.py <scratch> "cad/main cad files" ring|c1   # sections and holes, round 1
python -I check2.py <scratch> "cad/main cad files"     # ring socket profile, corner block, diffuser stations
python -I check_hc.py <scratch> "cad/main cad files/Honeycomb Section.3mf"   # rim, cells, pitch, wall
python -I recheck.py <scratch> "cad/main cad files"    # rounds 2 and 3: ring, C1 chamfer, diffuser chamfer
python -I hc_pitch.py <screenshot>                    # Pillow: cell pitch from a screenshot (before the exports)
```

How to recreate the method:
1. A 3MF is a zip file. Read `3D/3dmodel.model`: core namespace `.../3dmanufacturing/core/2015/02`, `unit="millimeter"`,
   vertices and triangles, with the build items' transforms applied.
2. A plane z = c cuts each triangle into a segment; chain the segments into loops.
3. A loop's area A gives a hole diameter 2√(A/π), and its centroid the hole's position. Rays from the axis at 0°, 45°
   and 90° give the inside and outside radii.

## 6. Measurements and results

All are from the exported meshes, computed by the scripts above. They are CAD geometry, not physical measurements. The
coordinate z runs along each part's axis.

- **Honeycomb:**
  - 249.400 × 249.400 × 50.000; cells reach ±123.5, so 247.0 inside the rim;
  - 1,777 cells (1,613 whole, 164 cut at the rim), 6.0000 across the flats, centres 6.4000 apart, walls 0.4000;
  - smallest cut cell 1.7 wide; no web thinner than the 0.4 walls;
  - volume 426.38 cm³: about 530 g of PLA at 1.24 g/cm³ if solid (estimate; the buy list allowed 0.5 kg).
  - Before the exports, the pitch measured from a screenshot was 6.42–6.45.
- **C1, final:**
  - one body, 280 × 280 × 125, inside 250.0, wall 3.0;
  - insert flange 8 thick with 12 × Ø3.98 holes, 6 deep from the joint face, at (±134, ±45), (±45, ±134), (±134, ±134);
  - screw flange 6 thick with 12 × Ø3.38 holes through, same pattern;
  - chamfer: outside 139.0 at 1 below the flange, 136.0 at 4, 132.0 at 8, 128.0 at 12;
  - corner blocks: 8 legs, x = 17–25, flat-ended;
  - volume 635.11 cm³.
  - Round 2's fillet stuck out 7.25, 3.12 and 0.73 at 1, 4 and 8 below the flange (radius 12).
- **Diffuser, final:**
  - 280 × 280 × 189;
  - round flange Ø152/Ø182, 8 thick, 6 × Ø3.98 holes 6 deep on Ø170 at 0°, ±60°, ±120°, 180°;
  - the curve against the S-curve, inside, flats and diagonal (S-curve in brackets):
    - x = 43.75: 83.619 (83.656) and 91.746 (91.746);
    - x = 87.5: 100.473 (100.500) and 126.388 (126.388);
    - x = 131.25: 117.317 (117.344) and 161.030 (161.031);
    - largest difference at the stations checked 0.07 (x = 8, diagonal), most within 0.04;
  - J250 flange 280/250, 6 thick, 12 × Ø3.38 through;
  - chamfer from r 90.94 at the flange to the wall at about 12 down, slope 0.945 (about 43° from the axis);
  - wall 3.0 measured across the axis, about 2.8 square to the wall at the steepest flats;
  - volume 586.70 cm³.
- **Fan ring, final:**
  - 182 × 40;
  - socket Ø156.12 inside from z = 0 to 27, outside Ø162.02 from z = 0 to 28, so a 1 mm floor;
  - Ø152/Ø158 from 28 to 34;
  - flange 34–40, Ø182, 6 × Ø3.38 holes on Ø170 at the same angles as the diffuser's;
  - volume 97.94 cm³.
  - Round 1's socket: Ø156.20, 155.65, 152.84 and 152.00 at z = 0, 6, 20 and 28. Round 2's: Ø156.19, 155.45, 153.20 and
    152.00 at 0, 5, 20 and 28.
- **Tunnel length** (estimate):
  - at sizing: 320 − 28 + 40 + 175 + 275 + 250 + 310 = 1,342 mm;
  - now: 320 − 27 + 40 + 189 + 275 + 250 + 310 = 1,357 mm, plus about 38 mm of frames and tape, so about 1,395 mm.

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests`: 20 tests OK at catch-up (8.6 s); rerun at the wrap, see below.
- `python scripts/check_docs.py`: 0 failures, 0 warnings at catch-up and after the mid-session edits; rerun at the
  wrap, see below.
- The CAD checks: each export read and sectioned by the scripts in §5, three rounds. All four final exports match the
  sheets, except the two values the owner chose to keep. The checks were geometric only: no slicer preview, no print.
- Not performed: any print, coupon, slicer run or physical measurement; the drawing package was not rebuilt.

Wrap checks:
- `python -m unittest discover -s tests -v`: 20 tests OK.
- `python scripts/check_docs.py`: 0 failures, 0 warnings after the wrap's edits.

## 8. Errors, failed approaches and troubleshooting

- **The previous session's screenshot checks missed real errors:** the ring's tapered socket, C1's six bodies and the
  missing chamfers. That log's table called these parts "Drawn" from screenshots. Checking the exported meshes caught
  all of them. Lesson: check exports, not screenshots.
- **Fillet instead of Chamfer**, on both C1 and the diffuser. The agent saw it from a curved end profile in a zoomed
  screenshot and confirmed it from the mesh (a radius-12 curve). The owner then swapped to Chamfer.
- **The ring's first fix kept the loft**, so the socket became a straight cone instead of a straight bore. Fixed in
  round 3 with an extruded tube.
- **Edge selection:** the owner's first picks were on the joint face, then the back face's outer rim. The agent zoomed
  into the screenshots (Pillow crops) to tell which loop was selected.
- **Fusion refused a 12 chamfer** on the diffuser's round flange at first (probably because it would use up the whole
  face). The final export's chamfer reaches the flange's edge anyway.
- **Agent's misstatement:** the agent told the owner the diffuser curve was within 0.04 mm. The largest difference at
  the stations checked is 0.07 mm. Corrected in the diffuser sheet and in the wrap report.
- **Sheet errors found:**
  - the spacers' stop (§2);
  - the corner blocks described as tapered when they were drawn flat-ended (the previous log says the owner left them
    so);
  - the 1.34 m length left out the joints.
- **The owner measured 28 on the socket's outside.** The bore is 27; explained with a text section.

## 9. Decisions and reasoning

- **Diffuser 189 overall** (owner, "keep the diffuser at 189"; note on [D-026](../../DECISIONS.md)):
  - the curve keeps its full 175 and its designed angles;
  - the straight ends give screens 12a and 12c flat walls;
  - the tunnel gets 14 mm longer;
  - the mid cut is 87.5 from the curve's start.
- **Socket 27 deep** (owner, "ok keep 27"): the 1 mm floor joins the socket's wall solidly to the Ø158 section.
- **Honeycomb 247 inside the rim**: the owner drew the sheet's value after the agent's recommendation.
- **Tunnel length about 1.40 m** (note on D-027): a corrected estimate, not a choice.
- **Not decided:** the spacers' stop. Proposed: corner tabs on 12d's frame.

## 10. Open questions and blockers

- What the honeycomb's spacers push on (corner tabs proposed).
- Still open from the previous session:
  - the mist port's place on C3;
  - whether the S6 is bought now or last;
  - whether the screw assortment holds 54 M3 × 16 and 40 M3 × 12;
  - whether the T18 tip is ordered;
  - the real print settings for the coupons;
  - whether to republish the drawings' claude.ai copy.
- Optional: a 0.5 mm chamfer on the honeycomb's bottom outside edge (elephant's foot), not added; the slicer's
  compensation may do.
- Whether to keep the 3MF checker in the repo (TODO P2, optional).

## 11. Remaining tasks

1. CAD (owner):
   - C2 and C3;
   - cut the diffuser at the middle of the curve (87.5 from its start, 95.5 from the round flange's face), flanges around
     the wall there, D2 into corner pieces;
   - the chambers into corner pieces with pin holes;
   - the spacers and frames 12b–12e (after the spacer choice);
   - then the contraction, test section, balance and supports.
2. Coupons C1–C5 before any big print.
3. Agent: check each new export the same way; bring the drawing package to the CAD (revision G) once more parts are
   drawn.

## 12. Recommended first task for the next agent

Ask the owner where the CAD stands (screenshot or the latest exports in `cad/main cad files/`), then continue with
settling chamber C2 in short numbered Fusion steps. Check every new export by cutting sections through the mesh (§5),
not from screenshots. Remind the owner to commit and push this session first if they haven't.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `83d6fad`. Nothing is staged.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first.
git status
git diff
git add DECISIONS.md PROJECT_STATUS.md TODO.md README.md PROJECT_BACKGROUND.md
git add docs/experimental_setup.md docs/drawings/README.md docs/sessions/SESSION_LOG.md docs/sessions/2026-11-26-pdfs-decisions-register-and-cad-start.md docs/sessions/2026-11-26-first-cad-exports-checked.md
git add cad/sizing/README.md cad/sizing/diffuser.md cad/sizing/settling_chamber.md
git add "cad/main cad files/Fan to Tunnel Joint.3mf" "cad/main cad files/Honeycomb Section.3mf" "cad/main cad files/Settling Chamber 1.3mf" "cad/main cad files/Wide Angle Diffuser.3mf"
git status
git diff --cached --stat
git commit -m "Add first CAD exports and record diffuser and socket choices" -m "The owner exported the honeycomb, settling chamber C1, the whole diffuser and the fan inlet ring as 3MF; each was checked by cutting sections through the mesh and fixed until it matched the sizing sheets. The owner kept the diffuser at 189 mm overall (the 175 mm curve plus its end flanges) and the fan socket 27 mm deep (notes on D-026 and D-027). The tunnel length estimate is corrected to about 1.40 m, since the old 1.34 m left out the joints. Found: the honeycomb's corner spacers have nothing to push on (fix proposed)."
git push origin HEAD
python scripts/sync_status.py --fetch
```
