# Sizing: dimension sheets and points files for the CAD

Build step 1. The owner draws every tunnel part in Fusion 360 ([D-017](../../DECISIONS.md)). This folder holds what the
agent supplies for it: one dimension sheet per printed part, the contraction's points file, and the scripts that
compute them (Python standard library; run from the repository root). Each sheet gives a status for every value:
Proposed, Tentative, Accepted or TBD. Exported models go in `cad/`, not here.

| Part | Sheet | Files | Status |
|---|---|---|---|
| Contraction (item 30) | [contraction.md](contraction.md) | `contraction.py` → `contraction_wall_fusion_cm.csv`, `contraction_wall_mm.csv` | Inside shape (D-022) and split (D-023) Accepted, 2026-11-26; flanges Proposed |
| Flanges, bolted joints, glued corner pieces (items 95–98) | [flanges.md](flanges.md) | | Split Accepted (D-023); flange sizes and bolt patterns Proposed, 2026-11-26 |
| Fan inlet ring and diffuser (items 10–13) | [diffuser.md](diffuser.md) | `profiles.py` → `diffuser_rail_flats_cm.csv`, `diffuser_rail_diagonal_cm.csv`, `profiles_mm.csv` | Screens and length Accepted (D-026); shape Proposed |
| Settling chamber, honeycomb, S taps (items 20–24) | [settling_chamber.md](settling_chamber.md) | | Spacing Accepted (D-027); details Proposed |
| Test section (items 40–49) | [test_section.md](test_section.md) | | Layout, window and taps Accepted (D-024, 2026-11-26); details Proposed |
| Floor inserts, shield, sealed box, balance module, image sting (items 53–75) | [balance.md](balance.md) | `profiles.py` → `shield_section_cm.csv` | Box (D-028) and image sting (D-029) Accepted; sizes Proposed |
| Heights, feet, fan stand, probe stand, small parts | [supports.md](supports.md) | | Fan (D-025) and probe route (D-030) Accepted; the rest Proposed |
| Test coupons | [coupons.md](coupons.md) | | Proposed, 2026-11-26; C1–C5 ready to draw, C6–C7 later |

Every part of the tunnel now has a sheet (2026-11-26). Order to draw: coupons C1–C5 first, then the contraction, test
section, settling chamber, diffuser, balance and supports. The fan ring (C7) waits on the fan.
The owner started on 2026-11-26 from the fan end instead: the diffuser, the fan ring (on the 6 in placeholder) and
settling chamber C1. The coupons are still printed before any big part, and the sizes they settle change only the
parameters below.

## Fusion user parameters (Proposed, agent, 2026-11-26)

Enter these once in Fusion (Modify → Change Parameters → User Parameters, unit mm) and draw every coupon and part from
them. When a coupon settles a size, change the one parameter, and every hole of that kind updates. The values are the
sheets' starting values. The coupon named beside each one replaces it.

| Name | Value | What it is | Settled by |
|---|---|---|---|
| `wall` | 3 | wall thickness | Proposed ([flange sheet](flanges.md)) |
| `flange_w` | 12 | flange, beyond the wall's outside | Proposed |
| `bolt_off` | 6 | bolt line, beyond the wall's outside | Proposed |
| `ins_fl_t` | 8 | insert flange thickness (upstream end of every section) | Proposed |
| `scr_fl_t` | 6 | screw flange thickness (downstream end) | Proposed |
| `chamfer` | 12 | 45° chamfer under the insert flange (12 out, 12 down) | Proposed |
| `ins_hole_d` | 4.0 | hole for the M3 × 5 heat-set inserts | coupon C1 |
| `ins_hole_depth` | 6 | its depth | coupon C1 |
| `clr_d` | 3.4 | M3 clearance hole | coupon C2 |
| `pin_d` | 2.0 | holes for the 1.75 mm filament pins in the seam faces | coupon C5 |
| `pin_depth` | 6 | their depth | coupon C5 |
| `mag_d` | 8.3 | pocket for the 8 × 2 magnets | coupon C3 |
| `mag_depth` | 2.2 | its depth | coupon C3 |
| `tap_sock_d` | 3.3 | socket for the 1/8 in brass tap stub | coupon C4 |
| `tap_boss_d` | 8 | pressure-tap boss | coupon C4 |
| `sc_in` | 250 | settling chamber inside, square | D-022 (Accepted) |
| `ts_in` | 100 | test section inside at the contraction exit | D-008 (Accepted) |
| `con_len` | 250 | contraction length | D-022 (Accepted) |
| `dif_len` | 175 | diffuser length | D-026 (Accepted) |
| `fan_in_d` | 152 | diffuser inlet, inside diameter: match the S6 collar's **inside** diameter, so the air sees no step | Proposed; measure the S6's collar on arrival |
| `collar_d` | 152.4 | the S6 collar's **outside** diameter. Placeholder: the nominal 6 in (owner, 2026-11-26). Measure the real one (paper strip ÷ π, or calipers in two directions) | measurement on arrival, then coupon C7 |
| `neo_t` | 1.6 | the neoprene wrap, one layer of 1/16 in | on hand (buy list §1) |
| `ring_clear` | 0.5 | print clearance on the socket's diameter | coupon C7 |

**Fan inlet ring socket** (item 10, owner's design, 2026-11-08):
- Inside Ø = `collar_d + 2*neo_t + ring_clear`, 28 deep: 156.1 with the 6 in placeholder, outside Ø 162.1.
- Outside Ø = inside Ø + `2*wall`: the wall is added outside the hole, never taken from it.
- The owner's first figure, 6.25 in (158.75), is not used. On a 150 collar it would leave about 4.4 per side against
  1.6 of neoprene, so the fan would sit loose.
| `side_bolt` | 45 | J250 side bolts, distance from the seam (from the middle of the side) | Proposed |

Derived positions for a 250 mm section, measured from its centre line: inside face 125, wall outside 128, bolt line 134,
flange edge 140. In Fusion: `sc_in/2`, `sc_in/2 + wall`, `sc_in/2 + wall + bolt_off`, `sc_in/2 + wall + flange_w`.

## Curves without importing points (2026-11-26)

Fusion has no built-in tool that draws a curve from an equation. Two of the three curves here don't need one, because
they are exactly Bézier curves, which Fusion's **Control Point Spline** draws natively. Their control points can be
dimensioned with the parameters above.

| Curve | Spline | Control points | Sheet |
|---|---|---|---|
| Contraction wall, 5th order (D-022) | degree 5, 6 points | x every `con_len/5`; y = `sc_in/2` for the first three, `ts_in/2` for the last three | [contraction.md](contraction.md) |
| Diffuser rails, S-curve (D-026) | degree 3, 4 points per rail | x every `dif_len/3`; y = h0, h0, h1, h1 | [diffuser.md](diffuser.md) |
| Sting-shield section, NACA 4-digit | none exact (the thickness formula has a square root) | use [`shield_section_cm.csv`](shield_section_cm.csv) (68 points, far finer than the printer) | [balance.md](balance.md) |

`contraction.py` and `profiles.py` print these control points and check them against the equations (they agree to about
10⁻¹³ mm, i.e. exactly). Always check one point in Fusion against the sheet's check value.

For a future curve with no exact form, there are two routes: import points (ImportSplineCSV, as now), or a third-party
add-in such as CodeReclaimers' free "Equation Driven Curve" (not tried). It also makes a spline through computed
points, so it is no more exact than an import.
