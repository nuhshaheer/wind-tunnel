# Dimension sheet: settling chamber, honeycomb and S taps (drawing items 20–24)

**Status:** the 250 mm square inside (D-022), the compact spacing (D-027), the four-corner-piece split and the S-tap
layout (D-023) are **Accepted** (2026-11-26). The rest is **Proposed** (agent, 2026-11-26). Joints follow the
[flange sheet](flanges.md), screen frames the [diffuser sheet](diffuser.md). All dimensions in mm; x runs along the flow
from the chamber's inlet face (the diffuser's exit, screen 12c).

## Stations

| x | What | Rule |
|---|---|---|
| 0 | Joint J250 with screen 12c (diffuser exit) | D-026 |
| 25–75 | Honeycomb, 50 long | 6 mm hexagons (owner, 2026-11-08); about 25 mm clear behind screen 12c |
| 125 | Joint J250 with screen 12d | 50 after the honeycomb (0.2 D, Mehta1979) |
| 175 | Joint J250 with screen 12e | 50 after 12d (0.2 D) |
| **200** | **S taps**, one per wall (D-023) | after the last screen (Barlow1999 notes); at least about 70 before the contraction (Morel1975 notes): here 75 |
| 240 | Mist port (capped), camera side, mid-height | after the last screen (TODO P2, owner's idea) |
| 275 | Joint J250 to the contraction | D-027 |

## Sections (each printed as four identical corner pieces, D-023)

| Section | x | Length | Carries |
|---|---|---|---|
| C1 | 0–125 | 125 | the honeycomb, its upstream corner stops at x = 25 |
| C2 | 125–175 | 50 | nothing (between screens 12d and 12e) |
| C3 | 175–275 | 100 | the S taps (one per piece, about 20 beside its seam, at x = 200) and the mist port |

Walls 3, PLA. Insert flange at each section's upstream end, screw flange at its downstream end (flange sheet).

## Honeycomb (items 21, 22)

| Item | Value | Status |
|---|---|---|
| Honeycomb | Printed flat, cells vertical: 6 mm hexagons (across the flats), 0.4 walls, 50 long (cell length about 8 diameters; Mehta1979 asks 7–10), **249.4 square** outside (0.3 clearance each side) with a 1.2 rim | Proposed |
| Holding it | Four small corner stops printed into C1's corner pieces at x = 25 (triangles 8 on a side, in the corners only) take its upstream face. **Shape (agent, 2026-11-26):** a small corner pyramid. Its flat triangular face (two 8 legs along the walls) sits at x = 25, facing downstream, for the honeycomb to rest on. It tapers back to the corner over 8 toward the fan (to x = 17), so the air meets a ramp, not a ledge, and the layers shrink as C1 prints standing on its screw flange. The flat face prints as an 11 bridge between the two walls. The owner drew it this way in Fusion (2026-11-26). Four printed corner spacers, 50 long, run from its downstream face (x = 75) to the screen 12d frame at x = 125, which presses them when C2 is bolted on. It slides out once C2 is off, so drinking straws can replace it later | Proposed |
| Why corners only | The air here moves at about 2 m/s; small corner blocks barely matter, while anything across the flow would | |

## S taps (item 23)

At x = 200, one in each wall, each about 20 beside its piece's seam (D-023). Boss and drilling as on coupon C4. The four
stubs join through three barbed tees into one line: the High side of the SDP810 during force runs.

## Coarse grid (2026-11-22 proposal #8, at the end of the validation)

On test days only: a piece of 1/4 in galvanized hardware cloth (to buy then, a few dollars) in its own J250 frame,
clamped at the x = 175 joint downstream of screen 12e (frames stacked; **M3 × 20** screws there that day). No extra joint
is needed. Recalibrate S − E with the grid in (Proposed).

## Found while preparing the CAD (2026-11-26)

- **The mist port sits on a seam.** The stations table puts it on the camera side at mid-height, x = 240. The middle of
  every wall is a glued seam (D-023), so mid-height on the side wall is exactly on the seam. The port is optional and
  used last (TODO P2), so this does not hold up the coupons. The section C3 piece needs an answer before it is drawn.
  Options, for the owner to choose:
  1. **A port boss on all four pieces** at x = 240, about 20 beside the seam like the S taps. Only one boss is drilled
     and capped; the others stay solid bumps. The four pieces stay identical: one model, one print file
     (agent's recommendation).
  2. One piece only carries a port, 20 beside the seam. That piece becomes a separate model.
  3. Leave the port out of the chamber for now and add it later in a spare joint frame.
- **The S-tap boss clears the chamfer by about 1 mm.** In section C3 the insert flange (8) and its chamfer (12) take the
  first 20 along the wall from the x = 175 joint face. A Ø8 boss centred at x = 200 (25 into the section) starts at 21.
  Check it in the CAD, or let the boss merge into the chamfer.

## Length

Chamber 275. With the S6, the inlet ring, the 175 mm diffuser, the 250 mm contraction and the 310 mm test section, the
tunnel is about **1.34 m** from the fan's inlet face to the open exit (estimate; collar overlap 28).

Sources: D-022, D-023, D-026, D-027 in [DECISIONS.md](../../DECISIONS.md); [Mehta1979](../../resources/notes/Mehta1979.md),
[Mehta1977](../../resources/notes/Mehta1977.md), [Morel1975](../../resources/notes/Morel1975.md) and
[Barlow1999](../../resources/notes/Barlow1999.md) notes; drawing sheet WT-03.
