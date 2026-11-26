# Test coupons: print these before any big part

**Status: Proposed (agent, 2026-11-26).** These are small, quick prints that settle hole sizes and techniques before kilograms
of PLA go into the tunnel (TODO P1, D-017). Print them in the same PLA, with the same settings (layer height, wall
count, infill, temperature) as the real parts, and **write the settings down**: a hole size only holds for the settings it
was printed with. The results replace the starting values in the [flange sheet](flanges.md). All dimensions are in mm.

Emboss each hole's size beside it (for example "3.9") so the pieces can't get mixed up.

| Coupon | What it settles | Shape | Holes / features to try | Pass test |
|---|---|---|---|---|
| **C1: insert holes** | the hole for the M3 × 5 heat-set inserts | block 60 × 16 × 8, holes vertical (opening up) | Ø3.8, 3.9, 4.0, 4.1, each 6 deep, centres 14 apart | Press each insert in with the T18 insert tip (start about 200–220 °C for PLA and adjust), straight down until flush; let it cool. **Pass:** it went in straight and flush, the plastic didn't bulge around it, and an M3 screw tightened firmly doesn't spin it. Too small a hole tilts or bulges; too big a hole lets the insert spin. Pick the best |
| **C2: screw holes and the joint stack** | the clearance hole, the screw length, the tape | plate 60 × 16 × 6 | Ø3.3, 3.4, 3.5, centres 14 apart | **Pass:** an M3 screw drops through by hand without much wobble (3.4 expected). Then stack C2 on C1 with a strip of the foam tape between them and screw the chosen M3 into an insert: about 4 mm of thread should engage, and the screw must not bottom out in the hole |
| **C3: magnet pockets** | the pocket for the 8 × 2 mm magnets (panels, D-014) | plate 50 × 16 × 4 | pockets Ø8.2, 8.3, 8.4, each 2.2 deep | **Pass:** a magnet presses in snugly and sits flush or just below the surface. A drop of super glue is fine if it's loose. Mark the poles (one flipped magnet repels) |
| **C4: pressure tap** | the tap boss, the stub fit and the drilling | plate 40 × 40 × 3 (the wall), with three bosses about Ø8 × 8 on one face | sockets for the 1/8 in (3.18) brass tube: Ø3.2, 3.3, 3.4, each stopping 1.5–2 short of the other face (the duct's inside), with a small pilot dimple on the inside face at each tap | From the inside face, drill through with a 0.8–1.0 bit in the pin vise, square to the face. Flatten the inside edge with 400–600 wet/dry on a flat block. Push in a 20 mm brass stub (cut with the tube cutter) and seal it with a drop of glue. **Pass:** under a magnifier the hole is round and has no burr or rounded edge; the stub is square and doesn't leak (cover the hole with a finger and suck gently on the tube) |
| **C5: corner-piece slice** | the real corner piece from your CAD, before a full-length print | your settling-chamber L piece, cut to about 30 long (screw flange, a short wall, insert flange with its chamfer); print **two** | everything in the flange sheet: the chamfer, filament-pin holes, insert and clearance holes, the bolt pattern | **Pass:** the chamfer prints cleanly without supports. Two copies glue at one seam with filament pins and sit square on a flat surface. Bolted face to face with foam tape, the inside walls line up within about 0.2 (feel with a fingernail; check with a straightedge) |

## Later coupons (wait on other sheets or parts)

- **C6: sting hole and sting-lock clamp:** the fit of the 1/8 in brass sting in the printed mount (D-015), and the 5.0
  bore of the sting shield, where the sting must never touch. Waits on the balance sheet.
- **C7: fan ring slice:** a 10 tall ring sized from the measured fan collar (buy list §1). Waits on the fan.

## Record the results

For each coupon, record the printer settings, the chosen size and anything odd (photos help). The agent then updates
the flange sheet, and the drawings once they are rebuilt.
