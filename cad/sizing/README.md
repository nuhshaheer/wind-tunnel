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
