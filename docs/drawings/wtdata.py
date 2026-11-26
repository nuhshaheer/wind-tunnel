"""Single source of dimensions and the master parts list.

Every value is tagged with where it comes from. 'layout' values are only used to draw a TBD item somewhere on the
sheet; they are never printed as a dimension.
"""

# ---------------- dimensions (mm) ----------------
P = dict(
    # fan: AC Infinity CLOUDLINE S6 (D-025). 7.87 x 12.60 x 8.35 in = 200 x 320 x 212 (maker page)
    fan_L=320,          # S6 overall length 32.0 cm (maker)
    fan_W=200, fan_H=212,
    collar_D=150,       # layout only: collar diameter TBD (measure on arrival); 6 in nominal duct
    collar_L=40,        # layout only
    wrap_t=1.6,         # 1/16 in neoprene, one layer (buy list 1)
    clear=0.5,          # about 0.5 mm print clearance (buy list 1)
    sock_depth=28,      # cad/sizing/diffuser.md (inlet ring)
    sock_wall=4,        # layout only (wall t TBD)
    gap_fan=12,         # layout only: fan body to socket face, TBD (fan must never touch the print)
    # diffuser
    diff_L=175,         # D-026 (three screens)
    # settling chamber
    ch=250,             # D-022 (CR 6.25)
    ch_gap0=25,         # D-027 compact spacing (cad/sizing/settling_chamber.md)
    hc_L=50,            # 6 mm cells, 50 long
    hc_s1=50,           # D-027: honeycomb -> screen 12d (0.2 D)
    s1_s2=50,           # D-027: 12d -> 12e (0.2 D)
    s2_c=100,           # D-027: 12e -> contraction; S taps 25 after 12e, 75 before the contraction
    # contraction
    con_L=250,          # D-022 (1.0 x inlet, Bell1988); split at x = 82 (D-023)
    # test section
    ts=100,             # accepted D-008
    ts_L=310,           # D-024: front body 245 + extension 65
    xE=56,              # D-024: >= 0.5 D2 (Morel1975)
    xM=206,             # D-024: E + 1.5 sqrt(C) (Cooper1998)
    t=3,                # cad/sizing (Proposed)
    fl_t=7, fl_w=12,    # flanges: 12 beyond the wall; insert flange 8, screw flange 6 (drawn 7) (cad/sizing/flanges.md)
    # balance
    ball34=19.05, ball1=25.4,   # Delrin balls (owner, 2026-11-08)
    ball_zc=50,                  # ball centre 50 above floor (centre of section)
    sting_d=3.175,               # 1/8 in brass rod; one full-length sting per ball, no sleeve (D-016)
    sting_L=85,                  # cad/sizing/balance.md
    below_floor=37,              # floor face to the cell's top end (cad/sizing/balance.md)
    shield_w=7.5, shield_bore=5.0, shield_len=22.5, shield_gap=5,  # proposed (buy list 6)
    cell_L=47, cell_W=12, cell_T=6, cell_hole=40, cell_hole_x=6,  # TAL221 datasheet
    floor_t=6,                   # cad/sizing/test_section.md
    # pressure taps and probe
    tap_hole=(0.8, 1.0), stub_od=3.175, stub_L=20, tube_id=3.175, tube_wall=1.6,
    probe_L=150,
    # SDP810
    sdp_body=(29, 18), sdp_holes=24, sdp_hole_d=2.9, sdp_port_pitch=12.6, sdp_barb=(5.2, 3.5),
    # panels and magnets
    acr_t=3.2, mag_d=8, mag_t=2, mag_pocket=(8.2, 8.3, 2.2), gasket_t=3.2, gasket_w=(6.4, 9.5),
)

# 5th-order contraction wall, half-width (Bell1988 notes): y = Hi - (Hi - He)(6x^5 - 15x^4 + 10x^3)
def contraction_half(xi, hi=125.0, he=50.0):
    return hi - (hi - he) * (6 * xi ** 5 - 15 * xi ** 4 + 10 * xi ** 3)


# ---------------- parts list ----------------
# status words: On hand / Ordered / To buy / Printed / Feature / Choice open / Check house
# Revision F (2026-11-26): entries updated from the sizing decisions D-022 to D-031 and cad/sizing; items 55-57 added (D-029).
ITEMS = [
    # num, name, what it does (plain), spec / material, qty, cost seen, status, source
    (1, 'Inline duct fan', 'Pushes air through the tunnel.',
     'AC Infinity CLOUDLINE S6, model AI-CLS6 (D-025): 425 CFM, 503 Pa (maker), 200 × 320 × 212 mm, EC motor, 10 speed levels. Bought last, once the airspeed readout works', '1', '$99.00', 'To buy', 'D-025; buy_list §1'),
    (2, 'Fan speed controller', 'Sets the fan speed; the Arduino never switches mains.',
     'Supplied with the S6 (10 speed levels)', '1', 'with fan', 'To buy', 'buy_list §1'),
    (3, 'Fan outlet collar', 'Round spigot that slides into the diffuser socket.',
     'Part of item 1. Diameter TBD: measure on arrival (paper strip ÷ π)', '—', '—', 'Feature', 'buy_list §1, §10'),
    (4, 'Neoprene collar wrap', 'Keeps the fan from touching the print, so its vibration does not reach the balance; centres the collar.',
     'Neoprene 40A, 1/16 in (1.6 mm), one layer, no adhesive; two ≈240 mm pieces butted end to end (two 12 × 12 in sheets bought)', '1 wrap', 'price paid not recorded', 'On hand', 'buy_list §1'),
    (5, 'Duct-tape seal', 'Seals the outside of the collar joint.',
     'Cloth duct tape; re-tape as the adhesive ages', '1 roll', '$5–10', 'On hand', 'buy_list §1'),
    (6, 'Fan stand (cradle)', 'Carries the fan’s weight apart from the tunnel.',
     'Printed cradle raising the S6’s outlet axis to 175 above the bench (cad/sizing/supports.md); sized from the fan on arrival', '1', 'filament', 'Printed', 'buy_list §1'),
    (7, 'Stand feet', 'Soft feet that keep fan vibration off the bench.',
     'Stick-on polyurethane bumper feet, about 20 × 10 mm (one 20-pack also covers the pads 100)', '4', '$5–10 a 20-pack', 'On hand', 'buy_list §1'),
    (8, 'Inlet guard', 'Open grille that keeps fingers and loose items out of the fan inlet.',
     'Printed. Size TBD', '1', 'filament', 'Printed (later)', 'buy_list §1'),
    (10, 'Fan inlet ring', 'Receives the wrapped collar with a snug slide fit.',
     'Printed, its own part, bolted to the diffuser (6 bolts on Ø170) with screen 12a between. Socket ID = collar Ø + 2 × 1.6 + ≈0.5, 28 deep; print coupon C7 first', '1', 'filament', 'Printed', 'cad/sizing/diffuser.md'),
    (11, 'Wide-angle diffuser shell', 'Widens the flow from the round fan outlet to the square chamber in a short length.',
     'Printed PLA, walls 3. Ø152 round → 250 × 250 square, 175 long (D-026); S-curve loft through two rails (cad/sizing/profiles.py); sharp corners. Front half (to the mid joint) one piece, back half four corner pieces (D-023)', '2 parts', 'filament', 'Printed', 'D-026; cad/sizing/diffuser.md'),
    (12, 'Screen', 'Woven mesh that evens out the speed and keeps the diffuser flow attached.',
     'Aluminium insect screen, Saint-Gobain ADFORS FCS9222-M, Bright: 18 × 16 mesh, 0.011 in wire (maker), 66 % open. Positions: 12a diffuser inlet, 12b diffuser mid joint, 12c diffuser exit (D-026), 12d and 12e settling chamber (D-027)', '5', 'about $10 a 36 × 84 in roll', 'On hand', 'buy_list §3'),
    (13, 'Screen frame', 'Two-part clamp that holds a screen taut and wrinkle-free; removable for cleaning.',
     'Two printed layers, 2 thick each, in the joint’s outline with Ø3.4 bolt holes; screen glued between. M3 × 16 at screen joints; 250 frames of four glued corner pieces', '5', 'filament', 'Printed', 'cad/sizing/diffuser.md'),
    (20, 'Settling-chamber shell', 'Slow, calm section where the honeycomb and screens clean up the flow.',
     'Printed PLA, 250 × 250 inside, walls 3, 275 long (D-027) in three sections (125, 50, 100), each four identical corner pieces glued at mid-wall seams (D-023)', '3 sections', 'filament', 'Printed', 'D-027; cad/sizing/settling_chamber.md'),
    (21, 'Honeycomb', 'Straightens swirl from the fan.',
     'Printed: 6 mm hexagons, 0.4 walls, 50 long, 249.4 square with a 1.2 rim; slides out of section C1. Upgrade: 5 mm drinking straws', '1', 'filament', 'Printed', 'buy_list §3'),
    (22, 'Honeycomb stops and spacers', 'Hold the honeycomb in place; it slides out once the next section is off.',
     'Corner stops (triangles 8 on a side) in C1 at x = 25; four corner spacers 50 long, pressed by the 12d frame', '1 set', 'filament', 'Printed', 'cad/sizing/settling_chamber.md'),
    (23, 'Wall pressure-tap station S', 'Settling-chamber static pressure; the high side of the S − E airspeed reading.',
     'Four taps, one per wall, each about 20 beside its piece’s seam (D-023), 25 after 12e and 75 before the contraction; joined into one line', '1 station', 'see 80–84', 'Printed + brass', 'buy_list §5'),
    (24, 'Mist port with cap', 'Capped opening after the last screen for optional mist visualisation later.',
     'Printed, capped; camera side, mid-height, 65 after 12e', '1', 'filament', 'Printed', 'cad/sizing/settling_chamber.md'),
    (30, 'Contraction shell', 'Speeds the air up 6.25 times and makes it uniform.',
     'Printed black PLA, walls 3. 250 × 250 → 100 × 100 inside, 250 long, 5th-order walls (D-022). Inlet ring x 0–82 of four corner pieces; one-piece part 82–250 (D-023). Inside sanded 220–600 grit', '2 parts', 'filament + $10–15 sandpaper', 'Printed', 'D-022; cad/sizing/contraction.md'),
    (40, 'Test-section body', 'Holds the window, panel, floor and taps around the 100 mm working space.',
     'Printed black PLA, inside 100.3 × 100.3, walls 3. Front body 245 (one print) + extension 65 = 310 (D-024)', '2 parts', 'filament', 'Printed', 'D-024; cad/sizing/test_section.md'),
    (41, 'Test-section floor', 'Fixed floor around the insert opening; carries the E-station floor tap.',
     'Printed, 6 thick; insert opening x 176–236 × 70 with a 4 ledge; E floor tap at 56', '1', 'filament', 'Printed', 'PROJECT_STATUS §2; owner sketch 2026-11-09'),
    (42, 'Top window panel (removable)', 'Clear lid; lift off to swap the model.',
     'Cast acrylic 1/8 in (3.2 mm) in a printed frame (44), inside face flush; covers the 155 × 100.3 opening at x 80–235; 4 + 4 magnets', '1', 'four 8 × 12 in sheets bought (price paid not recorded)', 'On hand', 'buy_list §4; D-014'),
    (43, 'Side window panel', 'Clear wall on the camera side, for viewing and mist photographs.',
     'Cast acrylic 1/8 in, about 165 × 90, fixed in a pocket cut from the inside against a 5 lip, flush; thin bead of clear silicone (D-024)', '1', 'from the same 8 × 12 in sheets', 'On hand', 'D-024; cad/sizing/test_section.md'),
    (44, 'Panel frame', 'Printed frame that holds the acrylic flush with the inside wall and carries the magnets.',
     'Printed; the acrylic sits in a pocket from the inside (flush) against a 5 lip; magnet pockets from coupon C3', '1 per panel', 'filament', 'Printed', 'buy_list §4'),
    (45, 'Magnet', 'Holds a panel down; the lips locate it.',
     'Round 8 × 2 mm (probably neodymium), pockets from coupon C3 (Ø8.2–8.4 × 2.2) under a thin skin. About 8 per panel (4 panel + 4 body); also the box door. Mark the poles', '≈16 of 43', 'on hand', 'On hand', 'buy_list §4'),
    (46, 'Foam gasket tape', 'Seals the panels and the bolted joints and stops buzzing.',
     'Closed-cell foam, about 1/8 in thick × 1/4 in (6.4 mm) wide (owner, 2026-11-26), adhesive-backed; inside the bolt line', '1 roll', '$5–8', 'On hand', 'buy_list §2, §4'),
    (47, 'Locating lip / pin', 'Makes each panel and floor insert land in the same place, flush inside.',
     'Printed lips on the panels; two Ø3.2 pins per floor insert at opposite corners', 'per panel / insert', 'filament', 'Printed', 'buy_list §4'),
    (48, 'Wall pressure-tap station E', 'Test-section entrance static pressure; the low side of the S − E airspeed reading.',
     'Four taps, one in each wall of the printed entrance band, at 56 (D-024); 150 ahead of the ball', '1 station', 'see 80–84', 'Printed + brass', 'D-024'),
    (49, 'Wall pressure-tap station M', 'Static pressure at the model station, paired with the probe.',
     'Two taps, one in each side wall at the ball (206), 12 above the floor (D-024); used on calibration days only', '1 station', 'see 80–84', 'Printed + brass', 'D-024'),
    (50, 'Probe stand', 'Holds the straight probe through the open exit and sets its tip position for the flow map.',
     'Printed: slotted upright and cross-bar with positions every 10 mm, two clamps 80 apart; on the bench at least 100 behind the exit (D-030)', '1', 'filament', 'Printed', 'D-030; cad/sizing/supports.md'),
    (51, 'Total-pressure probe', 'Brass tube facing upstream; reads total pressure (empty tunnel only).',
     'K&S 1/8 in (3.175 mm) brass tube, ≈290 straight (one 12 in tube), facing upstream through the open exit (D-030); tip square, outside edge chamfered, burr-free', '1', 'from $1.79–6.29 tube', 'On hand', 'D-030; buy_list §5'),
    (52, 'Open exit', 'Air leaves straight into the room; no exit diffuser.',
     'Accepted (D-007)', '—', '—', 'Feature', 'DECISIONS D-007'),
    (53, 'Floor insert, sphere', 'Removable piece of floor under the model (D-014). The sting shield (64) is attached to it; it also carries the sting hole and the M-station floor tap, and lifts out with them once the sting is out.',
     'Printed, 60 × 70 × 6, on the floor’s ledge with foam tape (sealed, D-028) and two pins (47); sting hole Ø5. Two: for the 1 in ball (shield to 32.3) and the 3/4 in ball (to 35.5)', '2', 'filament', 'Printed', 'D-014; cad/sizing/balance.md'),
    (54, 'Floor insert, plain (cars)', 'Swaps in for the sphere insert, so a model car can sit on a plain floor for mist studies (no force measured).',
     'Printed, same outline as item 53, no holes, no shield (D-014)', '1', 'filament', 'Printed (later)', 'owner sketch 2026-11-09; D-014'),
    (55, 'Image panel', 'Spare top panel that carries the dummy shield for the image runs (D-029).',
     'Printed black PLA, same outline and magnets as the top panel; a socket at x 206 for a dummy shield, held by one M3 into an insert', '1', 'filament', 'Printed', 'D-029; cad/sizing/balance.md'),
    (56, 'Dummy shield', 'Mirror copy of the floor shield, hung from the image panel; its drag goes to the tunnel, not the balance.',
     'Printed, same NACA section and Ø5 bore as item 64; down to 5 above the ball (z 67.7 for the 1 in, 64.5 for the 3/4 in)', '2', 'filament', 'Printed', 'D-029'),
    (57, 'Image stub and image ball', 'A 5 mm stub of sting on top of a spare ball, mirroring the real sting’s exposed length.',
     '1/8 in brass, 26 long: 6 in the ball, 5 showing, 15 inside the dummy shield’s bore, never touching. One spare ball of each size drilled at both poles', '2', 'from the rods and ball packs', 'On hand', 'D-029'),
    (60, 'Validation sphere', 'The known-answer model whose C_D is checked against Brown and Lawler Eq. (19).',
     'Acetal (Delrin) ball, 3/4 in (19.05 mm, 2.85 % blockage) or 1 in (25.4 mm, 5.07 %), ±0.001 in. Press-fit on its own sting (63): Ø3.0–3.1 hole drilled to the centre. Image balls: item 57', '1 of each in use', 'one pack of 10 of each size (spares for drilling trials)', 'On hand', 'buy_list §6'),
    (63, 'Sting', 'Rod that carries the sphere’s drag down to the load cell. Each ball has its own; the whole sting is swapped (D-016).',
     'Solid brass rod, true 1/8 in (3.175 mm), non-magnetic, 85 long, all cut to the same length within ≈0.5 mm and rolled to check straight. Top end pressed into the ball to its centre; bottom end in the mount’s blind hole. One more carries the calibration attachment (74). No sleeve (D-016)', '3 + spares', 'two 12 in rods (up to six stings)', 'On hand', 'D-016; cad/sizing/balance.md'),
    (64, 'Sting shield', 'Fairing attached to the sphere floor insert (53), lifting out with it, that hides the sting from the wind; never touches it.',
     'Printed NACA 4-digit section, chord 22.5, 7.5 thick (points file in cad/sizing), Ø5 bore at 30 % chord; from the floor to 5 below the ball', '2 (one per sphere insert)', 'filament', 'Printed', 'D-029; cad/sizing/balance.md'),
    (65, 'Sting mount', 'Printed block screwed to the load cell’s top end; the sting stands in its blind hole, which faces up.',
     'Printed PETG-CF, about 14 × 14 × 21: blind hole Ø3.3 (coupon C6) × 12 deep above a clamp round the cell’s top end, two short M3 (73). The sting bottoms out, so the ball height repeats', '1', 'filament', 'Printed', 'D-015; cad/sizing/balance.md'),
    (66, 'Load cell', 'Bends very slightly under drag; its strain gauges give the force.',
     'TAL221 100 g straight bar (SparkFun SEN-14727), 47 × 12 × 6 mm, holes 40 mm apart, 6 mm across; M3 tapped one end, Ø3.2 the other. Safe overload 150 g', '2 (1 spare)', '$15.95 each', 'On hand', 'TAL221 notes'),
    (67, 'Load-cell base', 'Holds the cell’s bottom end rigidly.',
     'Printed PETG-CF post beside the cell’s bottom end, on the module plate (70)', '1', 'filament', 'Printed', 'buy_list §2, §6'),
    (68, 'Sting lock (thumb screw)', 'Hand screw in a side hole of the sting mount; clamps the sting without glue, like the locking screw on a caliper.',
     'M3 into a brass heat-set insert (96) in the mount; axis along the wind (D-015); a printed knob on an M3 × 10', '1', 'filament', 'Printed', 'owner sketch 2026-11-09; D-015'),
    (69, 'Overload stops', 'Catch the sting at about 120 g, below the cell’s 150 g safe limit.',
     'Two M3 screws with lock nuts in a printed bracket, tips 1 from the mount at rest; turned in until they just touch with 120 g hung', '1 set', 'filament', 'Printed', 'buy_list §6'),
    (70, 'Balance module plate', 'Carries the cell, base and stops as one module that comes out and lies on its side for calibration.',
     'Printed PETG-CF, about 80 × 60 × 6; slides into the box through the door on two rails, held by two thumb screws; comes out whole for calibration', '1', 'filament', 'Printed', 'buy_list §9'),
    (71, 'Load-cell box (sealed)', 'Airtight box (except the sting’s gap) that keeps draughts and heat off the cell (D-028).',
     'Printed, inside ≈100 × 90 × 86, walls 3; bolted to bosses under the floor with foam tape; door ≈80 × 70 on the camera side on magnets; cable through a grommet. Bottom 145 below the axis', '1', 'filament', 'Printed', 'D-028; cad/sizing/balance.md'),
    (72, 'HX711 amplifier board', 'Reads the load cell’s tiny bridge voltage as a 24-bit number.',
     'SparkFun HX711 breakout SEN-13879; bridge wires soldered straight to it (no breadboard)', '1', '$11.50', 'On hand', 'buy_list §6'),
    (73, 'Short M3 screw', 'Fastens the load cell, sting mount and stops.',
     'M3 stainless from the 97 assortment, short enough not to reach the cell’s middle. The brass set was dropped: the panel magnets pull on even a plain steel M3 screw at 60 mm with only ≈1 µN (buy list §4)', 'set', 'in the 97 assortment', 'On hand', 'buy_list §2, §4, §6'),
    (74, 'Calibration attachment', 'Takes a ball’s place, on its own sting; its groove hooks the pan at the ball-centre height.',
     'Printed hook body pressed on its own full-length 1/8 in brass sting (63), cut to the ball stings’ length, so it seats in the mount like a ball (D-016). Not a printed 1/8 in peg. Form TBD', '1', 'filament', 'Printed', 'buy_list §9'),
    (75, 'Calibration pan and thread', 'Light pan hung on a thread loop, so the pull always acts at the hook.',
     'Printed pan or foil cup; fine nylon thread or light fishing line', '1', 'a few dollars', 'Check house', 'buy_list §9'),
    (76, 'Calibration mass set', 'Known masses for the load-cell calibration; each piece weighed once on the school lab balance.',
     'Amazon set (owner, 2026-11-19): 50, 2 × 20, 6 × 10, 2 × 5 and 3 × 2 g, plus a 10 g hanging rod; nothing under 2 g. Weighed 2026-11-19 on a 0.01 g balance (EXP-001): −2.5 % to +1.1 % off nominal, so the measured masses are used. Masses plus preload stay under 100 g', '1', 'not recorded', 'On hand', 'buy_list §9'),
    (80, 'Wall pressure tap hole', 'Small hole that senses the wall static pressure.',
     'Ø0.8–1.0 mm, drilled square to the wall after printing (pin vise), deburred inside', '12', 'pin vise + 0.7–3.0 mm bit set', 'On hand', 'buy_list §5, §10'),
    (81, 'Tap boss', 'Thickened spot outside the wall that holds the brass stub.',
     'Printed with the wall. Size TBD', '12', 'filament', 'Printed', 'buy_list §5'),
    (82, 'Brass tap stub', 'Short tube the silicone line pushes onto.',
     'K&S 1/8 in (3.175 mm) OD brass tube, about 20 mm, glued (super glue or 5-minute epoxy)', '12', 'from 2 × 12 in tubes', 'On hand', 'buy_list §5'),
    (83, 'Silicone tubing', 'Carries pressure to the sensor; keep each line ≤ 0.5 m and pairs equal.',
     '1/8 in (3.2 mm) ID, about 1/16 in (1.6 mm) wall', '≈3 m', '$8–12', 'On hand', 'buy_list §5'),
    (84, 'Barbed tee', 'Joins a station’s four taps into one line.',
     'For 1/8 in tubing; 3 per station (a 10th for the manometer)', '9', '$6–10 assortment', 'On hand', 'buy_list §5'),
    (85, 'Barbed straight coupler', 'Swap point where lines change between S/E and probe/M.',
     'For 1/8 in tubing', '2', 'in assortment', 'On hand', 'buy_list §5'),
    (86, 'Sensor pigtail', 'Short permanent tube on each sensor barb, so swaps never pull on the sensor.',
     'About 10 cm of item 83 ending in item 85', '2', '—', 'On hand', 'buy_list §5'),
    (87, 'Differential pressure sensor', 'Measures the pressure difference that gives airspeed.',
     'Sensirion SDP810-125Pa (Mouser 403-SDP810-125PA): ±125 Pa, body 29 × 18 mm, barbs Ø5.2/Ø3.5 at 12.6 mm, I²C 0x25. Multiply every reading by 966 mbar / p_amb', '1', '$29.39–34.72 (price paid not recorded)', 'On hand', 'SDP8xx, Sensirion2024 notes'),
    (88, 'Sensor bracket', 'Holds the sensor above its tubes so condensation drains away.',
     'Printed; 2 × Ø2.9 mm holes 24 mm apart; on the black wall near the test-section entrance, lines under 0.5 m', '1', 'filament', 'Printed', 'buy_list §5'),
    (89, 'Ambient sensor', 'Room pressure and temperature, for air density and the SDP810 correction.',
     'Waveshare BME280 Environmental Sensor, onboard 3.3/5 V level translator (maker); in room air near the fan inlet, away from heat', '1', '$9.58 seen (price paid not recorded)', 'On hand', 'buy_list §7'),
    (90, 'Microcontroller', 'Reads the sensors and streams CSV to the laptop over USB.',
     'Elegoo Mega 2560 (working, Blink Verified 2026-11-02)', '1', 'on hand', 'On hand', 'PROJECT_STATUS §3'),
    (91, 'Arduino box', 'Keeps the Arduino apart from the balance so its heat and handling do not disturb the cell.',
     'Printed; holds the Mega with the shield (101.6 × 53.34); on the bench beside the contraction, so every I²C run stays under ≈1 m', '1', 'filament', 'Printed', 'cad/sizing/supports.md'),
    (92, 'Sensor cable', 'Four-core leads from each sensor to the Arduino box.',
     'Four colours of the TUOFENG 24 AWG stranded silicone hook-up wire twisted together (hand drill); a 4-core shielded cable only if needed. ≈3 m in all; each I²C run under about 1 m', '≈3 m', '$15.79 (6-colour wire set)', 'On hand', 'buy_list §8'),
    (93, 'USB cable to laptop', 'Power and data; the laptop is the log and the live view (D-012).',
     'USB A-to-B, carries data (2026-11-02)', '1', 'on hand', 'On hand', 'PROJECT_STATUS §3'),
    (95, 'Bolted flange', 'Joins two printed segments so they can come apart (screen frames come out). Owner’s design, D-013.',
     'Printed on each section: 12 beyond the 3 wall; insert flange 8 at the upstream end, screw flange 6 at the downstream end; J250 12 bolts, J220 12, J100 8 (cad/sizing/flanges.md)', 'per joint', 'filament', 'Printed', 'D-013; cad/sizing/flanges.md'),
    (96, 'Heat-set insert', 'Brass thread melted into the print for repeated assembly.',
     'Kadrick M3 × 5 (Ø4.5 top, Ø3.9 bottom, 0.5 pitch; seller’s table), flush in the insert flange; hole ≈Ø4.0 × 6 deep (coupon C1). Kit of 230 M3 in five lengths', '≈90–110', 'kit, price paid not recorded', 'On hand', 'buy_list §2'),
    (97, 'M3 screw', 'Clamps the flanges.',
     'M3 stainless from the assortment (6, 8, 10, 12, 16, 20, 25 and 30 on hand): × 12 at plain joints, × 16 at screen joints; short ones (73) at the balance', 'set', '$10–15', 'On hand', 'buy_list §2'),
    (98, 'Alignment pins', 'Line up the glued corner pieces and the fast joint at the contraction exit.',
     '1.75 mm filament pins in Ø1.9–2.0 holes across each glued seam (D-023); two 10 mm brass pins (1/8 in rod) in Ø3.2 holes at J100', 'per seam; 2 at J100', 'filament; leftover rod', 'Printed', 'D-023; cad/sizing/flanges.md'),
    (99, 'Printed foot (cradle)', 'Supports each section; no plywood base.',
     'PLA cradles under the joints, not bolted: 35 under the chamber’s flanges, 110 under the test section’s (axis 175 above the bench)', '4', 'filament', 'Printed', 'cad/sizing/supports.md'),
    (100, 'Rubber pad', 'Under each foot: grip and damping.',
     'Stick-on polyurethane feet from the 20-pack (item 7), or spare neoprene', '6–8', 'in the 20-pack', 'On hand', 'buy_list §2'),
]

ITEM = {n: dict(name=nm, does=d, spec=s, qty=q, cost=c, status=st, src=src)
        for (n, nm, d, s, q, c, st, src) in ITEMS}
