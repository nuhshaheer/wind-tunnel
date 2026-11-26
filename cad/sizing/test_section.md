# Dimension sheet: test section (drawing items 40–49)

**Status:** the length and its split, the window and black wall, and the E and M tap positions are **Accepted**
([D-024](../../DECISIONS.md), owner, 2026-11-26). Everything else here is **Proposed** (agent, 2026-11-26). The floor
insert, the sting shield and the balance box get their own sheet (next). Hole sizes come from the
[test coupons](coupons.md), joints from the [flange sheet](flanges.md). The layout is drawn to scale on the owner's
private page "Test Section Layout" (https://claude.ai/artifact/8apGKDE8i8ndfXCnXVSCdT). All dimensions are in mm.

**Coordinates:** x runs along the flow from the test-section entrance (the contraction's exit; tunnel x = 250). z is
height above the floor's inside face. y is across, from the centre line; the window is on the camera side.

## Layout (Accepted, D-024)

| Item | x | Rule |
|---|---|---|
| Joint to the contraction (J100) | 0 | flange sheet |
| Printed entrance band, closed on all four sides | 0–80 | keeps E off the lift-off panel |
| **E taps**, one in the middle of each of the four walls | **56** | ≥ 0.5 D₂ after the contraction exit (Morel1975 notes) |
| Window and top-panel openings | 80–235 | the ball must be visible and reachable |
| **Ball centre** (z = 50, y = 0) | **206** | ≥ 1.5√C = 150 after E (Cooper1998 notes) |
| **M taps**, one in each side wall, z = 12 | **206** | opposite walls (Barlow1999 notes); below the line of sight to the ball (z 37–63) |
| Joint to the extension (J100) | 245 | the front body prints standing (bed height 256) |
| Open exit | 310 | ball base + 4√S: 218.7 + 90 for the 1 in ball (blockage positions, PROJECT_BACKGROUND) |

## Front body (x = 0–245, one print)

| Item | Value | Status |
|---|---|---|
| Inside | **100.3 × 100.3** (0.15 per side bigger than the contraction's 100.0 exit, so any mismatch at the joint is a step down, away from the flow). **Measure the printed inside** and use the real area C in the blockage correction | Proposed |
| Walls | 3, black PLA | Proposed |
| Upstream end (x = 0) | Insert flange, 8 thick; J100: 8 M3 × 5 inserts on a 118 bolt square (corners and mid-sides), plus two Ø3.2 pin holes at (y, z) = (−59, −29.5) and (59, 29.5) measured from the section's centre | Proposed (flange sheet) |
| Downstream end (x = 245) | Screw flange, 6 thick, J100 pattern (8 clearance holes), no pins | Proposed |
| Entrance band (x = 0–80) | Closed, all four walls printed. One E tap boss in the middle of each wall at x = 56 (coupon C4) | Proposed |
| Black wall (far side) | Solid, full height, x = 0–245. M tap at x = 206, z = 12 | Accepted position; Proposed details |
| Camera side | Printed rail z = 0–20 from x = 80 to 235 (carries the M tap at x = 206, z = 12); window opening above it: x = 80–235, z = 20–100.3 | Accepted position |
| Window | 1/8 in (3.2) cast acrylic, **inside face flush with the wall**. Proposed mounting: thicken the wall around the opening outward to about 5.2. Cut a pocket from the inside, the acrylic's size + 0.2 and 3.2 deep, with a 5 wide lip behind it. Fit the acrylic from inside through the top opening; the inside pressure (at or just above room pressure) pushes it out against the lip. A thin bead of clear silicone at the edges seals and holds it. Acrylic about 165 × 90 (opening + lip overlap; fits one 8 × 12 in sheet) | Proposed |
| Top opening | x = 80–235, full width. The top panel (below) fills it | Accepted (D-014) |
| Floor | 6 thick (layout), printed. E tap at x = 56 in the middle. Opening for the floor insert around the ball, layout x = 176–236 × 70 wide; size, ledges, pins and seal in the insert sheet | Proposed |
| Printing | Stand it on the downstream screw flange; 45° chamfer under the top (insert) flange. The upstream edges of the window and top openings become 80–100 wide bridges in that position: give them a 45° chamfer on the outside, or support them | Proposed |
| Filament | About 300 g (estimate) | |

## Top panel (D-014: lifts off on magnets)

| Item | Value | Status |
|---|---|---|
| Panel | 1/8 in acrylic in a printed frame, **inside face flush with the top wall** (same pocket-and-lip method as the window, open to the inside) | Proposed |
| Locating | Lips or two pins so it lands in the same place every time | Proposed |
| Holding | 8 × 2 mm magnets: about 4 in the frame and 4 facing them in the body (pockets from coupon C3). Mark the poles; one flipped magnet repels | Proposed (buy list §4) |
| Seal | A strip of the foam tape under the frame, outside the flow | Proposed |
| Force | Well under 1 N from the air (buy list §4): the magnets only locate it | |
| No taps in it | E and M are in fixed walls (D-024) | Accepted |

## Extension (x = 245–310)

| Item | Value | Status |
|---|---|---|
| Body | Printed tube, inside 100.3 × 100.3, 3 walls, black PLA | Proposed |
| Upstream end | Insert flange, 8 thick, J100 pattern (no pins) | Proposed |
| Downstream end | Open exit, square cut, no flange | Proposed |
| Printing | Stand it on the open end; 45° chamfer under the flange | Proposed |
| Later (optional) | A small window to watch the wake with mist | Idea |

## Still open

Items 1–3 were open when this sheet was written and were settled later on 2026-11-26:

1. ~~The floor insert, sting shield, sting hole and balance box~~: in the [balance sheet](balance.md), which also sets the
   tunnel's height ([supports sheet](supports.md)).
2. ~~The calibration probe~~: **D-030**, a straight probe through the open exit on a stand
   ([supports sheet](supports.md), "Probe stand"). No port in the black wall.
3. ~~The image-sting proposal~~: **D-029**, the image panel and stub in the [balance sheet](balance.md).
4. A window-pocket coupon (C8) if the owner wants to test the flush window before the full body.

Sources: D-008, D-013, D-014, D-022, D-023 and D-024 in [DECISIONS.md](../../DECISIONS.md);
[Morel1975](../../resources/notes/Morel1975.md), [Cooper1998](../../resources/notes/Cooper1998.md) and
[Barlow1999](../../resources/notes/Barlow1999.md) notes; [buy list](../../docs/buy_list.md) §4.
