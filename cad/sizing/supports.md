# Dimension sheet: heights, feet, fan stand, probe stand and small parts (items 6–8, 50–51, 88–91, 99–100)

**Status: Proposed (agent, 2026-11-26)**, except the fan (S6, D-025) and the probe route (through the open exit,
D-030), which are Accepted. All dimensions in mm.

## Heights

The lowest parts set the height: the load-cell box reaches **145 below the tunnel's axis** and the settling chamber's
flanges 140. With the axis 175 above the bench:

| Item | Height |
|---|---|
| **Tunnel axis above the bench** | **175** |
| Bottom of the chamber's flanges | 35 |
| Bottom of the load-cell box (hangs free) | 30 |
| Bottom of the contraction's exit and test section's flanges (65 below the axis) | 110 |
| S6 fan's outlet axis | 175: the stand lifts the fan about 69 if its outlet axis is at the middle of its 212 tall body (check on arrival) |

The box hangs freely, clear of the bench, so the balance never carries the tunnel's weight.

## Feet (items 99, 100)

Printed PLA cradles the tunnel rests in, each with two stick-on bumper feet (on hand). They are not bolted, so a section
can come off without touching them.

| Foot | Under | Height to the flange's bottom |
|---|---|---|
| F1 | diffuser → chamber joint (x = 0 of the chamber) | 35 |
| F2 | chamber → contraction joint | 35 |
| F3 | contraction → test section joint | 110 |
| F4 | under the extension, near the exit (test section x ≈ 290; the load-cell box occupies x 156–256) | 118 to the extension's bottom wall |

Each cradle cups the flange's lower edge over about 60 of its width, with a 2 lip on each side so the tunnel can't slide
sideways.

## Fan stand (items 6, 7) and inlet guard (item 8)

- A printed cradle under the S6 (body 200 × 320 × 212, maker), raising its outlet axis to 175, with four bumper feet.
  The fan touches the tunnel only through the neoprene-wrapped collar in the inlet ring (owner's design, 2026-11-08).
  Size it from the fan on arrival.
- Inlet guard: a printed open grille over the fan's inlet. Later.

## Probe stand (items 50, 51; D-030)

| Item | Value |
|---|---|
| Probe | K&S 1/8 in brass tube, about 290 long (one whole 12 in tube; the other tube gives the 12 tap stubs). Straight; the tip cut square with the tube cutter, its outside edge chamfered, burr-free (2026-11-22 proposal #5) |
| Tip position | At the ball's station (test section x = 206) for the S − E calibration; anywhere across the section for the flow map |
| Stand | On the bench behind the open exit: a slotted upright for height (z) and a slotted cross-bar for side position (y), marked every 10 mm, so the tip can be set within about ±40 of the centre. Two clamps 80 apart hold the probe parallel to the axis (check with a square); its holder stays at least 100 behind the exit plane |
| Alignment | Within a few degrees of the flow (Barlow1999: errors from about 8°). Check by turning it slightly each way and setting it where the reading stays highest |
| Tube | Silicone tube from the probe's back end to the SDP810's High side (calibration days) |

## Small parts

| Item | Value |
|---|---|
| **BME280 holder** (item 89) | An open, vented printed box with slots on every side, the sensor chip facing one slot. Screwed or snapped onto the fan stand's side, about 100 from the fan's motor body, in room air, out of lamp or sun light (2026-11-19). Measure the board (outline, holes, connector side) before drawing |
| **SDP810 bracket** (item 88) | Two Ø2.9 holes 24 apart (datasheet), holding the sensor above its tubes so condensation drains away. On the test section's black wall near x = 0, so the S, E and probe lines stay under about 0.5 m and equal in pairs |
| **Arduino box** (item 91) | Holds the Mega with the shield on its standoffs (101.6 × 53.34 board), with openings for USB and the cables. On the bench beside the contraction, so every I²C run stays under about 1 m |

Sources: D-025, D-030 in [DECISIONS.md](../../DECISIONS.md); [buy list](../../docs/buy_list.md) §1, §5, §7, §8;
[Barlow1999 notes](../../resources/notes/Barlow1999.md) ch. 4; PROJECT_STATUS open question 15.
