# Dimension sheet: floor inserts, sting shield, sealed load-cell box, balance module and image sting (items 53–75)

**Status:** accepted so far:
- the replaceable floor inserts (D-014);
- the sting mount and thumb-screw sting lock (D-015);
- one full-length 1/8 in brass sting per ball (D-016);
- the ball's station (D-024);
- the sealed box with an access door (D-028);
- the image sting (D-029).

Everything else here is **Proposed** (agent, 2026-11-26) for the owner to adjust while drawing. All dimensions in mm.

**Coordinates:** x along the flow from the test-section entrance; y across from the centre line (+y = camera side); z up
from the floor's inside face. The ball's centre is at (206, 0, 50).

## The vertical stack at the ball

| z | What |
|---|---|
| 50 | Ball centre (both sizes). The sting's top end reaches the centre (press fit, D-016) |
| 37.3 / 40.5 | Bottom of the 1 in / 3/4 in ball |
| **32.3 / 35.5** | **Top of the floor shield** for the 1 in / 3/4 in ball: 5 below the ball (D-029) |
| 0 | Floor's inside face (the insert's top, flush) |
| −6 | Floor's underside; the box's top seals here |
| −23 | Top of the sting mount, where the blind hole opens |
| **−35** | **Bottom of the sting**: sting **85** long, from the ball's centre |
| −23 to −44 | Sting mount (PETG-CF): the blind hole above, and below it a clamp around the cell's top end, held by two M3 along the wind |
| −37 to −84 | TAL221, upright (47 long), directly under the ball, hole axes along the wind (D-015) |
| about −74 to −86 | Base post beside the cell's bottom end, on the module plate (z −86 to −92) |
| **about −95** | **Bottom of the box** (outside): 145 below the tunnel's axis, 30 above the bench |

## Floor inserts (items 53, 54)

| Item | Value | Status |
|---|---|---|
| Opening in the floor | x 176–236 × y ±35 (60 × 70), with a 4 wide ledge 3 below the floor's surface all round | Proposed |
| Inserts | **Three:** sphere insert for the 1 in ball, sphere insert for the 3/4 in ball (their shields differ in height), plain insert for model cars. 6 thick, top flush with the floor; they drop in from above with the top panel off | Proposed |
| Locating | Two Ø3.2 pins at opposite corners (pin holes in the ledge) | Proposed |
| Seal | Foam tape on the ledge, so **the only opening into the box is the sting's gap** (D-028). With two openings at different pressures, air could circulate in one and out the other, along the sting | Proposed |
| Sting hole | Ø5 at (206, 0), continuing the shield's bore | Proposed |

## Sting shield (item 64)

| Item | Value | Status |
|---|---|---|
| Section | Symmetric NACA 4-digit, **chord 22.5, thickness 7.5**, nose upstream; points: [`shield_section_cm.csv`](shield_section_cm.csv) (cm; from `python cad/sizing/profiles.py`). Trailing edge cut blunt at about 1.0 thick so it prints | Proposed |
| Bore | Ø5 for the 1/8 in (3.18) sting, centred 6.75 behind the nose (30 % chord); 0.9 clearance all round; 1.25 of wall each side | Proposed (buy list §6) |
| Height | From the insert's top (z = 0) to z = 32.3 (1 in insert) or 35.5 (3/4 in insert) | D-029 |
| Never touches the sting | Check with the wind off: tap the shield; the reading must not change | |

## Sting, mount, lock and stops (items 63, 65, 68, 69)

| Item | Value | Status |
|---|---|---|
| Sting | Solid brass rod 1/8 in (3.18), **85 long**, one per ball plus one for the calibration attachment, all within 0.5 of each other; top end pressed into the ball to its centre (hole Ø3.0–3.1 drilled with the printed jig) | Accepted (D-016); length Proposed |
| Mount | PETG-CF block about 14 × 14 × 21 (z −23 to −44): a blind hole Ø3.3 (coupon C6) × 12 deep at the top, opening upward (the sting bottoms out, so the ball height repeats), and a clamp around the cell's top end below it, screwed with two short M3 through the cell's top-end holes | Proposed |
| Sting lock | M3 into a heat-set insert in the mount's side, **axis along the wind** (D-015), a printed knob on an M3 × 10. Turning it twists the cell about its stiff axis, not its measuring one. Hold the mount while turning; finger-tight | Proposed |
| Overload stops | Two M3 screws with lock nuts in a printed bracket on the module plate, tips 1 from the mount's upstream and downstream faces at rest. Hang 120 g on the calibration attachment and turn each screw in until it just touches (TAL221 safe limit 150 g) | Proposed |

## Balance module and sealed box (items 66, 67, 70–72)

| Item | Value | Status |
|---|---|---|
| Module | One PETG-CF plate about 80 × 60 × 6 carrying the cell's base (a 10 thick post the cell's bottom end screws to), the stop bracket and the HX711. It slides into the box through the door onto two rails and is held by two M3 thumb screws. It comes out whole, to be laid on its side for calibration | Proposed (2026-11-08 plan) |
| Box | PLA, walls 3. Inside about 100 (x) × 90 (y) × 86 (z −6 to −92), x 156–256. A flange around its top screws to bosses under the test section's floor (four M3 into inserts), with foam tape between | Proposed |
| **Door** (D-028) | On the camera side (+y): opening about 80 × 70, door 3 thick, foam tape around the opening. Held by four 8 × 2 magnets, or two M3 thumb screws if the magnets don't pull it tight | Accepted (door); size Proposed |
| Cable exit | Downstream wall, a Ø6 hole with a rubber grommet, or sealed with silicone around the four-wire cable to the Arduino box | Proposed |
| Checks | Smoke held at the sting's gap with the fan on: not drawn in. Wind-off zero the same with the door shut twice in a row | Proposed |
| Magnets near the balance | None on the box's measured side: the door's magnets sit at its edges, at least 40 from the sting mount (buy list §4: a steady pull cancels in the wind-off zero anyway) | Proposed |

## Image sting (D-029)

| Item | Value | Status |
|---|---|---|
| Image panel | A spare top panel, printed opaque (black PLA), same outline and magnets as the clear one. A socket at x = 206, y = 0 takes a dummy shield, held by one M3 into an insert | Proposed |
| Dummy shields | Two, mirror copies of the floor shields: the same section and bore, hanging from the panel's inside face down to z = 67.7 (1 in) or 64.5 (3/4 in), so 5 above the ball's top | Proposed |
| Image balls | One spare ball of each size, drilled at both poles with the same jig | Accepted (D-029) |
| Stub | 1/8 in brass, **26 long**: 6 pressed into the image ball's top, 5 showing, 15 inside the dummy shield's bore (dead-ended there, like the real sting's bore into the sealed box). It must never touch the dummy shield | Proposed |
| Runs | Run 1 normal ball; Run 2 image ball with the image panel; same speed, one after the other. Ball alone = Run 1 − (Run 2 − Run 1) | Accepted (D-029) |

## Calibration attachment (items 74–76)

A printed hook body pressed on its own 85 mm sting, hook groove at z = 50 (the ball's centre height). With the module
out and laid on its side, the masses hang from the hook in the drag direction. Unchanged from the buy list §9.

## Still open

1. Coupon C6, the sting's fit in the mount (Ø3.2 / 3.3 / 3.4).
2. The cell's mounting holes, read off the cell itself: which end is tapped M3 and which has Ø3.2 clearance holes
   (TAL221 notes).
3. The module's rails and the door's final size, once the box is drawn around the real module.

Sources: D-014, D-015, D-016, D-024, D-028, D-029 in [DECISIONS.md](../../DECISIONS.md);
[Barlow1999 notes](../../resources/notes/Barlow1999.md) ch. 7; [TAL221 notes](../../resources/notes/TAL221.md);
[buy list](../../docs/buy_list.md) §4, §6, §9; drawing sheet WT-06.
