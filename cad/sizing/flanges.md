# Dimension sheet: flanges, bolted joints and the glued corner pieces (drawing items 95–98)

**Status: Proposed (agent, 2026-11-26)** unless marked otherwise. These build on decisions that are already Accepted:
bolted flanges with M3 screws into brass heat-set inserts and foam tape between the faces (D-013), the 250 mm settling
chamber (D-022), and the four-corner-piece split (D-023). The hole sizes are only starting values: the
[test coupons](coupons.md) set the real ones. All dimensions are in mm.

**Inserts** (seller's table, owner's photo, 2026-11-26; one is still to be checked with calipers): Kadrick M3, 0.5 mm
pitch, Ø4.5 top (d1), Ø3.9 bottom (d2), 5 mm long. The kit has 230 M3 inserts: 50 each of 3, 4 and 5 mm, and 40 each
of 6 and 8 mm.

## The standard flange (every joint)

The joint is drawn to scale in the last section of the owner's private page "Splitting the 250 mm Sections"
(https://claude.ai/artifact/UFEmwtqjkPqvZEFhCvpwqZ).

| Item | Value | Why |
|---|---|---|
| Flange width | 12 beyond the outside of the 3 mm wall (15 from the inside face) | room for the Ø4.5 insert and a screw head |
| Bolt line | 6 beyond the wall's outside (9 from the inside face) | about 3.75 of plastic on each side of the insert; a head up to Ø7 (with washer) clears the wall |
| **Insert flange** (each section's upstream end) | 8 thick. M3 × 5 inserts pressed in from the joint face, flush. Hole about Ø4.0 × 6 deep (coupon C1) | the extra 1 mm of depth takes melted plastic; 2 mm of floor stays behind the hole |
| **Screw flange** (each section's downstream end) | 6 thick. Clearance holes about Ø3.4 (coupon C2). Its back face must be flat: the screw heads sit on it | |
| Screws | **M3 × 12 stainless** (on hand: the assortment has M3 × 6, 8, 10, 12, 16, 20, 25 and 30; owner, 2026-11-26): 6 flange + about 2 squeezed tape leaves about 4 of thread in the insert (about 2.8 if the tape hardly squeezes), and the tip cannot reach the bottom of the 6 deep hole. Where a screen frame is clamped in the joint, add its thickness and take the next length up (16 or 20) | D-013 |
| Seal | Foam weatherstrip tape, **1/4 in (6.4) wide** (owner, 2026-11-26), on the screw flange's face, **inside the bolt line**: from about 0.3 to 6.7 out from the inside edge (the clearance holes start at 7.3). If it touches a hole, the screw simply goes through it. It must never stick out into the duct | |

Every section has an insert flange at its upstream end and a screw flange at its downstream end. So every joint is
the same, and the screws always go in from upstream.

## Bolt patterns

Positions are measured from the section's centre line, across the flow.

| Joint | Where | Inside | Flange outside | Bolt square (centres) | Bolts | Spacing |
|---|---|---|---|---|---|---|
| **J250** | diffuser exit → settling chamber, between chamber sections, chamber → contraction | 250 | 280 | 268 | **12:** four corners (±134, ±134), and two per side at ±45 from the middle: (±45, ±134), (±134, ±45) | 89–90 |
| **J220** | contraction inlet ring → one-piece contraction, at x = 82 | 219.7 | 249.7 | 237.7 | **12:** four corners (±118.8, ±118.8), and two per side at ±45 from the middle | 74–90 |
| **J100** | contraction exit → test section | 100 | 130 | 118 | **8:** four corners (±59, ±59) and the middle of each side (0, ±59), (±59, 0) | 59 |

- **No bolt in the middle of a side on a split section:** that is where the glued seam is. With bolts at ±45 the seam
  stays clear, and the four corner pieces stay identical: each carries one corner bolt and one bolt on each arm, at
  each flange.
- **Why so few bolts** (estimate): at 13 m/s the inside is only about 100 Pa above the room, which is about 6 N on a whole
  250 mm wall. Between bolts 90 mm apart, a 6 mm PLA flange bends about 0.03 mm under the foam's push (assuming
  20 kPa on a 6.4 mm tape and E = 2.5 GPa). That is far less than the foam squeezes, so the seal stays even.
- **Joints, inserts and screws** (counted from the sheets, 2026-11-26; replaces the first estimate of 5–7 J250 joints and
  90–110 inserts): **9 bolted joints, 18 flanges.** Every part has an insert flange upstream and a screw flange
  downstream, except the fan inlet ring (socket upstream) and the test-section extension (open exit).

  | Joint | Bolts | Screen | Screws |
  |---|---|---|---|
  | Fan inlet ring → diffuser D1 (round) | 6 | 12a | M3 × 16 |
  | D1 → D2 (mid-diffuser) | 12 | 12b | M3 × 16 |
  | D2 → chamber C1, C1 → C2, C2 → C3 (J250) | 12 each | 12c, 12d, 12e | M3 × 16 |
  | C3 → contraction inlet ring (J250) | 12 | none | M3 × 12 |
  | Inlet ring → one-piece contraction (J220) | 12 | none | M3 × 12 |
  | Contraction → test section (J100) | 8, plus 2 pins | none | M3 × 12 |
  | Front body → extension (J100) | 8 | none | M3 × 12 |

  **94 inserts and 94 screws: 54 × M3 × 16 and 40 × M3 × 12.** Use the 5 mm (50) and 4 mm (50) inserts in the
  flanges, since a 6 mm deep hole takes both. That leaves only 6 spare. If more are needed, a 6 mm insert fits a 7
  deep hole: at the bolt line the chamfer under the insert flange adds about 6 to its 8. Keep the 6 and 8 mm ones for
  the balance and the panel frames. How many M3 × 12 and × 16 the screw assortment holds is not recorded yet.
- **Why the flange runs all the way round, not as corner tabs** (owner asked, 2026-11-26):
  - The foam tape needs a continuous face to seal against; the chamber runs about 100 Pa above the room at 13 m/s.
  - The screen frames must be clamped all round, or air slips around the screens' edges.
  - With bolts only at the corners (268 apart instead of about 90), the flange would bend about 80 times as much
    between bolts. That is about 2 mm, as much as the foam squeezes (estimate, scaled from the figure above).

## Lining up the inside walls at a joint

- **Slow joints (J250, J220):** the screws in Ø3.4 holes locate each section to within about ±0.2. Before tightening,
  lay a straightedge across the joint inside and push the walls flush, then tighten in a cross pattern.
- **J100, where the air is fastest:**
  - Add two Ø3.2 holes for pins, diagonally opposite on the bolt line, halfway between a corner bolt and a mid-side
    bolt: (−59, −29.5) and (59, 29.5). The pins can be 10 mm pieces cut from the leftover 1/8 in brass rod (3.18).
  - Make the test section's opening about 0.3 bigger than the contraction's exit (100.3 against 100.0). Any mismatch
    that is left is then a small step down, away from the flow, never a step up into it.
  - Settled in the test-section sheet.

## The corner pieces (D-023)

- **Four identical L pieces per section.** Each is two half-walls (3 thick) with its quarter of both flanges. The seams
  sit in the middle of the walls and run along the flow. The contraction inlet ring (x = 0 to 82) is made the same way,
  with its walls curved by the [points file](contraction.md).
- **Printing:** stand each piece on its screw flange, joint face down on the bed. That leaves the screw-head face flat and
  the clearance holes vertical. The insert flange is then on top, with its joint face up. Give its underside a 45°
  chamfer, from the wall out to the flange edge (12 out, 12 down), so it prints without supports. Nothing sits on that
  underside.
- **Length:** a piece can be up to about 250 long (the bed height is 256).
- **Joining:**
  - In each seam face, drill two Ø1.9–2.0 holes, 6 deep, in each flange. Short pieces of 1.75 mm filament go in these
    as pins, four per seam. **Positions (Proposed, agent, 2026-11-26):** at mid-thickness of the flange, 130 and 136
    from the section's centre line (2 and 8 beyond the wall's outside). That leaves 4 of plastic to the inside face
    and 3 to the flange edge. Model them at `pin_d`; the horizontal holes print slightly oval, so run the drill through
    them after printing.
  - Glue the whole seam with 5-minute epoxy, which fills gaps and gives time to line things up.
  - Glue with the four screw-flange faces down on a flat surface, so they end up in one plane.
  - Check the insert-flange face with a straightedge, then sand the inside seam flush (220 → 400 grit).
- **The S-tap section:** each piece carries one tap about 20 from its seam, at the S station's position along the
  chamber. The boss and the drilling are as tested on coupon C4.

## Still open

1. **Hole sizes:** from coupons C1 and C2.
2. **The settling chamber's sections and the screen joints** (settling-chamber sheet, next), with the S ring's position:
   after the last screen (Barlow1999 notes) and at least about 70 before the contraction (Morel1975 notes). So the last
   screen sits at least about 100 before the contraction (Proposed).

Sources: D-005, D-013, D-022 and D-023 in [DECISIONS.md](../../DECISIONS.md);
[Barlow1999 notes](../../resources/notes/Barlow1999.md); [Morel1975 notes](../../resources/notes/Morel1975.md);
[buy list](../../docs/buy_list.md) §2 and §5.
