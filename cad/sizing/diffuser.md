# Dimension sheet: fan inlet ring and wide-angle diffuser (drawing items 10–13)

**Status:** three screens and 175 mm length are **Accepted** ([D-026](../../DECISIONS.md), 2026-11-26); the S6 fan is
**Accepted** (D-025); the four-corner-piece split of the 250 mm end is **Accepted** (D-023). The rest is **Proposed**
(agent, 2026-11-26). Joints follow the [flange sheet](flanges.md). All dimensions in mm; x runs along the flow from the
diffuser's inlet face.

## What it does

The diffuser widens the flow from the fan's round 152 mm outlet to the 250 mm square settling chamber in a short
length. Its area ratio is 3.44, more than an unaided diffuser can manage, so three screens hold the flow attached:
Mehta1977's rule A < 1.14 K_sum + 1 needs K_sum ≥ 2.1, and three window screens give about 3.2.

## Shape

| Item | Value | Status |
|---|---|---|
| Inlet | Round, inside Ø152 (6 in fan outlet; **check against the S6's collar on arrival**) | Proposed |
| Exit | 250 × 250 square, sharp corners (matches the settling chamber) | Accepted (D-022) |
| Length | 175 | Accepted (D-026) |
| Wall growth | Smooth S-curve, zero slope at both ends: half-width h = h0 + (h1 − h0)(3u² − 2u³), u = x/175. Across the flats 76 → 125; along the diagonal 76 → 176.8 | Proposed |
| Steepest wall | At mid-length (x = 87.5): 22.8° each side across the flats (2θ = 45.6°, inside Mehta1977's three-screen limit of about 53°), 40.8° along the diagonal | computed |
| Loft rails | [`diffuser_rail_flats_cm.csv`](diffuser_rail_flats_cm.csv) and [`diffuser_rail_diagonal_cm.csv`](diffuser_rail_diagonal_cm.csv) (cm, for ImportSplineCSV; mm values in `profiles_mm.csv`). Loft from the Ø152 circle to the 250 square through both rails, mirrored to all four flats and corners | Proposed |
| Walls | 3, PLA | Proposed |

**In Fusion:** make the whole diffuser as one loft, then split it at x = 87.5. Both halves then share exactly the same
section at the joint. The corners expand about twice as steeply as the flats (Mehta1977 notes). Screen 12b sits at the
steepest point, where it helps most. Corner fillets (Mehta1977's advice) were weighed and left out: they would have to
fade out through the settling chamber, and the third screen already gives about 50 % K margin.

## Parts and joints

| Part | x | Print | Joints |
|---|---|---|---|
| **Fan inlet ring** (item 10) | −40 to 0 | One piece | Upstream: a socket for the fan collar, inside Ø = collar Ø + 2 × 1.6 (neoprene) + about 0.5, 28 deep. Size it from the measured collar; print a 10 mm test ring first (coupon C7). Downstream: a round screw flange, 6 thick |
| **Screen 12a** | 0 | Round frame | Clamped between the ring and the diffuser's front half |
| **Diffuser, front half** (D1) | 0 to 87.5 | **One piece**, standing on its inlet end: 231 across its back flange | Upstream: round insert flange (Ø152 inside, Ø182 outside, 6 bolts on a Ø170 circle). Downstream: screw flange around the mid-section, 12 beyond the wall |
| **Screen 12b** | 87.5 | Frame of the mid-section's shape | Clamped in the mid joint |
| **Diffuser, back half** (D2) | 87.5 to 175 | **Four corner pieces** (D-023), seams mid-wall | Upstream: insert flange around the mid-section. Downstream: J250 screw flange |
| **Screen 12c** | 175 | J250 frame | Clamped between the diffuser and the settling chamber |

| Joint | Bolts |
|---|---|
| Ring → D1 (round, with 12a) | 6 on a Ø170 circle, 60° apart, none at the top or bottom centre |
| D1 → D2 (mid-section, with 12b) | 12: four on the diagonals and two each side of every flat, ±45 from its middle, all on the curve 9 out from the inside face (D2's seams stay clear) |
| D2 → chamber (J250, with 12c) | 12, the J250 pattern |

**Screw lengths:** joints with a screen frame use **M3 × 16** (6 flange + 2 tape + 4 frame + about 4 into the insert);
see the screen frame below.

## Screens and frames (items 12, 13)

| Item | Value | Status |
|---|---|---|
| Screens 12a, 12b, 12c | Aluminium window screen (Saint-Gobain ADFORS FCS9222-M, 18 × 16 mesh, 0.011 in wire, 66 % open, on hand); K about 0.75–1.3 each depending on the local speed (buy list §3) | Accepted (D-026) |
| Frame | Two printed layers, each **2 thick**, the joint's own outline (inside = the duct's inside, outside = the flange's outside, bolt holes Ø3.4 on the bolt line). Stretch the screen over one layer, glue it with super glue along the band, press the second layer on and trim the screen at the outer edge and the bolt holes. 250 frames are made of four corner pieces glued flat (D-023) | Proposed |
| Seal at a frame joint | Foam tape on the screw-flange side only; the frame's other face meets the insert flange directly | Proposed |
| Lands | Each frame meets flat, parallel walls on both sides: the walls at every joint run parallel to the axis for at least 5 before they start to grow (2026-11-22 proposal #7, Bradshaw1964) | Proposed |

## Still open

1. The fan's collar diameter: measure on arrival; it sets the ring's socket (coupon C7).
2. Whether the inlet Ø152 matches the collar's inside: adjust the loft's inlet circle to the collar's inside diameter.

Sources: D-023, D-025, D-026 in [DECISIONS.md](../../DECISIONS.md); [Mehta1977](../../resources/notes/Mehta1977.md) and
[Mehta1979](../../resources/notes/Mehta1979.md) notes; [buy list](../../docs/buy_list.md) §1, §3; drawing sheet WT-02.
