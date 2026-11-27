---
name: check-cad
description: Check one of the owner's CAD exports (3MF files in "cad/main cad files/") against its dimension sheet in cad/sizing/, by measuring the mesh with scripts/check_mesh.py - bodies, size, wall, flanges, holes and their depth, chamfers versus fillets, curves, and whether mating holes line up. Use whenever the owner says a part is drawn, exported, finished or changed, or asks for a CAD check.
argument-hint: "[part name or file; default: the newest export]"
---

# /check-cad: check a CAD export against its sheet

The owner draws every part in Fusion 360 (D-017) and exports it to `cad/main cad files/`. The agent checks the export
against the part's dimension sheet. **Measure the mesh; never judge from screenshots.** On 2026-11-26, screenshot checks
had passed a tapered socket, a part made of six bodies and missing chamfers, and later fillets drawn where chamfers
were meant; the mesh caught every one. `scripts/check_mesh.py` (standard library, tested by `tests/test_check_mesh.py`)
does the measuring, so no checker is rewritten per session.

The owner's own files are read-only to the agent: never move, rename, delete or "fix" an export.

## Step 1: find the file

```bash
ls -la "cad/main cad files/"
git status --short "cad/main cad files/"
```

The newest file is usually the one. It must be a **.3mf**:
- `.f3d` (a Fusion archive): its shape is in Autodesk's own format and Python cannot even unzip it. Ask for a 3MF:
  right-click the body in the browser → **Save As Mesh** (or File → Export) → **3MF**, unit **mm**, saved as
  `cad/main cad files/<Part name>.3mf`.
- STL works but carries no unit; ask for 3MF.
- A screenshot alone: ask for the export.

## Step 2: measure

```bash
python scripts/check_mesh.py info   "cad/main cad files/<Part>.3mf"
python scripts/check_mesh.py layers "cad/main cad files/<Part>.3mf"
```

- `info`: bodies (must be **1**, a **closed solid**, **1 piece**), size, P1S bed fit, volume and a solid-PLA mass bound.
- `layers`: every plane along the part's axis (default z; `--axis x|y` otherwise) where the shape changes, and each
  stretch between: the outline, the opening (the duct), the holes with their pattern. A stretch whose size changes is
  `CHANGING` and each loop in it is `straight` (chamfer, cone), `curved` (fillet, loft) or `unchanged`.

Then, as needed:

```bash
python scripts/check_mesh.py cut   FILE Z [Z ...] --rays 0,45   # full section; rays give inside/outside radii
python scripts/check_mesh.py cut   FILE Z --list                 # every hole's centre
python scripts/check_mesh.py match FILE_A Z_A FILE_B Z_B         # do the holes of two mating faces line up?
```

- Cut **between** planes, not on one (a cut on a face plane is taken just above it, and says so).
- For `match`, cut each part inside the flange that meets the joint. The command exits 1 if any hole is unmatched.
  `--mirror x|y` and `--rotate DEG` handle a part exported the other way round.
- Curves (diffuser, contraction): compare `cut --rays 0,45` at the sheet's stations with the points file
  (`cad/sizing/profiles_mm.csv`, `contraction_wall_mm.csv`) or the sheet's check values; state the largest difference.

## Step 3: compare with the sheet

Find the part's sheet in the table in `cad/sizing/README.md`. Read its "As drawn" or "Found while preparing the CAD"
notes too: a value the owner chose to keep (for example the diffuser at 189 overall, the fan socket 27 deep) is not an
error. Check the register "Decisions: what is decided and what is not" in `PROJECT_STATUS.md` before calling anything
settled. Check, for every part:

| Check | What a pass looks like |
|---|---|
| Bodies | 1 body, closed solid, 1 piece |
| Size and position | overall size as the sheet; centred on the axis (outline centre 0, 0) |
| Wall | outline minus opening = 2 × `wall` on a plain stretch |
| Insert flange | its thickness is the stretch lengths (6 with holes plus 2 without, for 6-deep holes in an 8 flange); holes `ins_hole_d`, count and pattern from `flanges.md` |
| Screw flange | its thickness; holes `clr_d`, through the whole stretch |
| Chamfer under the insert flange | a `CHANGING` stretch, outline `straight`, 12 long, outline 12 smaller each side; `curved` means a fillet |
| No chamfer under screw flanges | the outline steps straight from the flange to the wall |
| Curves | within about 0.1 of the points file |
| Mating parts | `match` finds every hole with offset 0.000 |
| Bed fit | fits 256, or will once cut into the corner pieces the sheet plans |

Reading the numbers:
- Holes and round outlines are sized from the mesh vertices, which lie on the true circle, so the reading is the drawn
  diameter (Ø4.000, not the 3.98 an area-based reading gives).
- On curved or lofted surfaces Fusion's triangles make sizes jitter by about ±0.05; use `cut --rays` for precise values.
- A part's parameters can change after the coupons (C1–C7); compare with the sheet's current values.

## Step 4: report to the owner

The owner is proficient in CAD but asked for plain words: no sheet jargon (say "the flange the screws go into", not
"J250 insert flange", unless the term is explained), short numbered Fusion steps, the answer first.
- One small table: check, the sheet's value, the export's value, ✓ or ✗.
- For each ✗: what is wrong in one plain sentence, then 3–5 numbered Fusion steps to fix it, tied to the sheet.
- Then what comes next (the next part, or a decision the next part waits on).
- Never call a part Verified: it is CAD geometry checked against the sheet, not printed or measured.

## Step 5: record it

At `/wrap` (or straight away if the session will not wrap):
- the part's sizing sheet: an "As drawn" line with the date and the key numbers, plus any owner's kept change;
- `PROJECT_STATUS.md` §4 (owner's CAD exports row) and the CAD task in `TODO.md` P0;
- the session log §5 (the exact commands) and §6 (the numbers), with failed rounds in §8.

Known mistakes so far (check for them every time): a part split into several bodies; a fillet where a chamfer was
meant; a chamfer on the wrong edge (the joint face or the back rim instead of under the insert flange); a loft left
in a socket that should be a straight bore; holes on the wrong face or at the wrong depth.
