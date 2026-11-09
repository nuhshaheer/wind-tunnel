"""Single source of dimensions and the master parts list.

Every value is tagged with where it comes from. 'layout' values are only used to draw a TBD item somewhere on the
sheet; they are never printed as a dimension.
"""

# ---------------- dimensions (mm) ----------------
P = dict(
    # fan (D-011 open). S6: 7.87 x 12.60 x 8.35 in = 200 x 320 x 212 (maker page); VEVOR 306 x 255 x 212 (seller)
    fan_L=320,          # layout: S6 overall length 32.0 cm (maker). Model not chosen -> TBD
    fan_W=200, fan_H=212,
    collar_D=150,       # layout only: collar diameter TBD (measure on arrival); 6 in nominal duct
    collar_L=40,        # layout only
    wrap_t=1.6,         # 1/16 in neoprene, one layer (buy list 1)
    clear=0.5,          # about 0.5 mm print clearance (buy list 1)
    sock_depth=28,      # proposed 25-30 (buy list 1)
    sock_wall=4,        # layout only (wall t TBD)
    gap_fan=12,         # layout only: fan body to socket face, TBD (fan must never touch the print)
    # diffuser
    diff_L=175,         # proposed 150-200 (Mehta1977 notes), drawn mid-range
    # settling chamber
    ch=250,             # proposed 250 x 250 inside (CR 6.25)
    ch_gap0=25,         # layout: diffuser exit -> honeycomb, TBD
    hc_L=50,            # proposed about 48-50 (buy list 3)
    hc_s1=100,          # layout: honeycomb -> screen 1, TBD
    s1_s2=75,           # layout: screen 1 -> screen 2, TBD
    s2_c=50,            # proposed 0.2 D = 50 (Mehta1979)
    # contraction
    con_L=250,          # proposed 1.0 x inlet (Bell1988, Abdelhamed2014)
    # test section
    ts=100,             # accepted D-008
    ts_L=280,           # proposed 270-290, drawn mid-range
    xE=50,              # min 0.5 h (Mehta1979) -> E taps
    xM=200,             # E + 1.5 sqrt(C) = 50 + 150 -> sphere station (Cooper1998)
    t=3,                # layout only: wall thickness TBD (2-3 mm used in the filament estimate)
    fl_t=6, fl_w=14,    # layout only: flange thickness and width TBD
    # balance
    ball34=19.05, ball1=25.4,   # Delrin balls (owner, 2026-11-08)
    ball_zc=50,                  # ball centre 50 above floor (centre of section)
    sting_d=3.175,               # 1/8 in brass rod
    sleeve_d=3.97,               # 5/32 in OD brass tube
    sting_L=85,                  # proposed 80-90
    below_floor=35,              # proposed 30-40 through the floor to the cell
    shield_w=7.5, shield_bore=5.0, shield_len=22.5, shield_gap=5,  # proposed (buy list 6)
    cell_L=47, cell_W=12, cell_T=6, cell_hole=40, cell_hole_x=6,  # TAL221 datasheet
    floor_t=6,                   # layout only, TBD
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
# status words: On hand / To buy / Printed / Feature / Choice open
ITEMS = [
    # num, name, what it does (plain), spec / material, qty, cost seen, status, source
    (1, 'Inline duct fan', 'Pushes air through the tunnel.',
     '6 in inline duct fan, model TBD (D-011): AC Infinity CLOUDLINE S6 AI-CLS6 (425 CFM, 503 Pa, 200 × 320 × 212 mm) or VEVOR VV-GDFJ-AC6 (400 CFM, 300 Pa, 306 × 255 × 212 mm, axis order not stated)',
     '1', '$99.00 (S6) or $53.90 (VEVOR)', 'Choice open', 'buy_list §1'),
    (2, 'Fan speed controller', 'Sets the fan speed; the Arduino never switches mains.',
     'Supplied with the fan (S6: 10 speed levels)', '1', 'with fan', 'Choice open', 'buy_list §1'),
    (3, 'Fan outlet collar', 'Round spigot that slides into the diffuser socket.',
     'Part of item 1. Diameter TBD: measure on arrival (paper strip ÷ π)', '—', '—', 'Feature', 'buy_list §1, §10'),
    (4, 'Neoprene collar wrap', 'Keeps the fan from touching the print, so its vibration does not reach the balance; centres the collar.',
     'Neoprene 40A, 1/16 in (1.6 mm), one layer, no adhesive (Rubber-Cal 30-004-062)', '1 wrap', '$13.78 a pair of sheets', 'To buy', 'buy_list §1'),
    (5, 'Duct-tape seal', 'Seals the outside of the collar joint.',
     'Cloth duct tape; re-tape as the adhesive ages', '1 roll', '$5–10', 'Check house', 'buy_list §1'),
    (6, 'Fan stand (cradle)', 'Carries the fan’s weight apart from the tunnel.',
     'Printed (or scrap plywood). Size TBD', '1', 'filament', 'Printed', 'buy_list §1'),
    (7, 'Stand feet', 'Soft feet that keep fan vibration off the bench.',
     '4 soft rubber or silicone bumper feet, about 20–25 mm', '4', '$5–10', 'To buy', 'buy_list §1'),
    (8, 'Inlet guard', 'Open grille that keeps fingers and loose items out of the fan inlet.',
     'Printed. Size TBD', '1', 'filament', 'Printed (later)', 'buy_list §1'),
    (10, 'Diffuser inlet socket', 'Receives the wrapped collar with a snug slide fit.',
     'Printed. ID = collar Ø + 2 × 1.6 + ≈0.5 mm; 25–30 mm deep. Print a 10 mm test ring first', '1', 'filament', 'Printed', 'buy_list §1'),
    (11, 'Wide-angle diffuser shell', 'Widens the flow from the round fan outlet to the square chamber in a short length.',
     'Printed PLA. Round → 250 × 250 square, area ratio 3.44, length 150–200 (TBD), curved walls or radiused ends, filleted corners', '1 (segments TBD)', 'filament', 'Printed', 'Mehta1977 notes'),
    (12, 'Screen', 'Woven mesh that evens out the speed and keeps the diffuser flow attached.',
     'Aluminium insect screen, “bright aluminum”, 18 × 16 mesh, wire 0.010–0.011 in, 66–69 % open. Positions: 12a diffuser inlet, 12b diffuser middle (only if the wire is 0.010 in), 12c diffuser exit, 12d and 12e settling chamber',
     '4 or 5', '$9.49–9.68 a 36 × 84 in roll', 'To buy', 'buy_list §3'),
    (13, 'Screen frame', 'Two-part clamp that holds a screen taut and wrinkle-free; removable for cleaning.',
     'Printed PETG-CF, clamped between bolted flanges', '4 or 5', 'filament', 'Printed', 'buy_list §3'),
    (20, 'Settling-chamber shell', 'Slow, calm section where the honeycomb and screens clean up the flow.',
     'Printed PLA, 250 × 250 inside, length TBD (see register)', '1 (segments TBD)', 'filament', 'Printed', 'Mehta1979, Mehta1977 notes'),
    (21, 'Honeycomb', 'Straightens swirl from the fan.',
     'Printed: 6 mm hexagonal cells, 0.4 mm walls, about 48–50 mm long, about 250 × 250 mm. Upgrade: 5 mm drinking straws', '1', 'filament', 'Printed', 'buy_list §3'),
    (22, 'Honeycomb frame', 'Holds the honeycomb; removable so straws can replace it.',
     'Printed. Size TBD', '1', 'filament', 'Printed', 'buy_list §3'),
    (23, 'Wall pressure-tap station S', 'Settling-chamber static pressure; the high side of the S − E airspeed reading.',
     'Four taps (one per wall) joined into one line; see items 80–84', '1 station', 'see 80–84', 'Printed + brass', 'buy_list §5'),
    (24, 'Mist port with cap', 'Capped opening after the last screen for optional mist visualisation later.',
     'Printed. Size and position TBD', '1', 'filament', 'Printed', 'buy_list §4'),
    (30, 'Contraction shell', 'Speeds the air up 6.25 times and makes it uniform.',
     'Printed black PLA. 250 × 250 → 100 × 100 inside, 250 long, 5th-order polynomial walls. Inside sanded 220–600 grit', '1 (segments TBD)', 'filament + $10–15 sandpaper', 'Printed', 'Bell1988 notes'),
    (40, 'Test-section frame', 'Holds the windows, floor and taps around the 100 × 100 mm working space.',
     'Printed black PLA; clamped details PETG-CF. Length 270–290 (TBD)', '1', 'filament', 'Printed', 'PROJECT_STATUS §2'),
    (41, 'Test-section floor', 'Fixed floor around the insert opening; carries the E-station floor tap.',
     'Printed. Thickness TBD; ledge for the inserts (proposed)', '1', 'filament', 'Printed', 'PROJECT_STATUS §2; owner sketch 2026-11-09'),
    (42, 'Top window panel (removable)', 'Clear lid; lift off to swap the model.',
     'Cast acrylic 1/8 in (3.2 mm) set in item 44. About 300 × 120 cut (buy list); final size TBD', '1', '$10.45 per 12 × 24 in sheet', 'To buy', 'buy_list §4; D-014'),
    (43, 'Side window panel', 'Clear side wall for viewing; removable or fixed is TBD (the top panel comes off: D-014).',
     'Cast acrylic 1/8 in (3.2 mm) set in item 44', '1–2', 'same sheet', 'To buy', 'buy_list §4'),
    (44, 'Panel frame', 'Printed frame that holds the acrylic flush with the inside wall and carries the magnets.',
     'Printed. Section TBD', '1 per panel', 'filament', 'Printed', 'buy_list §4'),
    (45, 'Magnet', 'Holds a panel down; the lips locate it.',
     'Round 8 × 2 mm (probably neodymium), in pockets Ø8.2–8.3 × 2.2 deep under a thin skin. About 8 per panel (4 panel + 4 frame). Mark the poles', '≈16 of 43', 'on hand', 'On hand', 'buy_list §4'),
    (46, 'Foam gasket tape', 'Seals the panels and the bolted joints and stops buzzing.',
     'Closed-cell foam, about 1/8 in (3.2 mm) thick × 1/4–3/8 in (6.4–9.5 mm) wide, adhesive-backed', '1 roll', '$5–8', 'To buy', 'buy_list §2, §4'),
    (47, 'Locating lip / pin', 'Makes each panel and floor insert land in the same place, flush inside.',
     'Printed lips on the panels; two pins per floor insert at opposite corners (proposed). Form and size TBD', 'per panel / insert', 'filament', 'Printed', 'buy_list §4'),
    (48, 'Wall pressure-tap station E', 'Test-section entrance static pressure; the low side of the S − E airspeed reading.',
     'Four taps joined into one line, at least 150 mm (1.5√C) ahead of the sphere', '1 station', 'see 80–84', 'Printed + brass', 'buy_list §5'),
    (49, 'Wall pressure-tap station M', 'Static pressure at the model station, paired with the probe.',
     'Four taps joined into one line, at the sphere’s station', '1 station', 'see 80–84', 'Printed + brass', 'buy_list §5'),
    (50, 'Probe guide', 'Holds the total-pressure probe and lets it traverse for the flow map; plugged when not in use.',
     'Printed, through a fixed wall. Position TBD', '1', 'filament', 'Printed', 'buy_list §4'),
    (51, 'Total-pressure probe', 'Brass tube facing upstream; reads total pressure (empty tunnel only).',
     'K&S 1/8 in (3.175 mm) OD brass tube, about 150 mm, one 90° bend; square, burr-free tip', '1', 'from $1.79–6.29 tube', 'To buy', 'buy_list §5'),
    (52, 'Open exit', 'Air leaves straight into the room; no exit diffuser.',
     'Tentative (D-007)', '—', '—', 'Feature', 'DECISIONS D-007'),
    (53, 'Floor insert, sphere', 'Removable piece of floor under the model (D-014). Carries the sting shield, the sting hole and the M-station floor tap, and lifts out with them.',
     'Printed. Drops in from above onto a ledge in the floor opening, top flush with the floor, on two pins (47) (proposed). Size, hold-down and seal TBD', '1', 'filament', 'Printed', 'owner sketch 2026-11-09'),
    (54, 'Floor insert, plain (cars)', 'Swaps in for the sphere insert, so a model car can sit on a plain floor for mist studies (no force measured).',
     'Printed, same outline as item 53, no holes. Replaces the floor plug in buy list §11', '1', 'filament', 'Printed (later)', 'owner sketch 2026-11-09; D-014'),
    (60, 'Validation sphere', 'The known-answer model whose C_D is checked against Brown and Lawler Eq. (19).',
     'Acetal (Delrin) ball, 3/4 in (19.05 mm, 2.85 % blockage) or 1 in (25.4 mm, 5.07 %), ±0.001 in', '2 of each', '≈$2.78 / $4.42 each (bulk)', 'To buy', 'buy_list §6'),
    (61, 'Ball stem', 'Short brass pin each ball is pressed onto; slides into the sting sleeve.',
     '1/8 in (3.175 mm) brass, pressed into a Ø3.0–3.1 hole drilled to the ball centre (9.5 deep for 3/4 in, 12.7 for 1 in). Length TBD', '1 per ball', 'from item 63 stock', 'To buy', 'buy_list §6'),
    (62, 'Sting sleeve', 'Socket at the top of the sting that takes a ball’s stem.',
     'K&S 5/32 in (3.97 mm) OD brass tube, short; friction or set screw. Length TBD', '1', '$2–3', 'To buy', 'buy_list §6'),
    (63, 'Sting', 'Rod that carries the sphere’s drag down to the load cell.',
     'K&S solid brass rod 1/8 in (3.175 mm), about 80–90 mm, non-magnetic', '1–2', '$1–3', 'To buy', 'buy_list §6'),
    (64, 'Sting shield', 'Fairing fixed to the sphere floor insert (53) that hides the sting from the wind; never touches it.',
     'Printed, teardrop or airfoil section about 7.5 mm wide × 20–25 mm long, Ø5 mm bore, from the floor to about 5 mm below the ball', '1', 'filament', 'Printed', 'buy_list §6'),
    (65, 'Sting mount', 'Printed block screwed to the load cell’s top end; the sting stands in its blind hole, which faces up.',
     'Printed PETG-CF; brass M3 screws (73) into the cell. The sting bottoms out in the hole, so the ball height repeats. Hole fit and depth TBD', '1', 'filament', 'Printed', 'owner sketch 2026-11-09; D-015'),
    (66, 'Load cell', 'Bends very slightly under drag; its strain gauges give the force.',
     'TAL221 100 g straight bar (SparkFun SEN-14727), 47 × 12 × 6 mm, holes 40 mm apart, 6 mm across; M3 tapped one end, Ø3.2 the other. Safe overload 150 g', '2 (1 spare)', '$15.95 each', 'To buy', 'TAL221 notes'),
    (67, 'Load-cell base', 'Holds the cell’s bottom end rigidly.',
     'Printed PETG-CF, thick; a metal bracket if the zero drifts. Size TBD', '1', 'filament', 'Printed', 'buy_list §2, §6'),
    (68, 'Sting lock (thumb screw)', 'Hand screw in a side hole of the sting mount; clamps the sting without glue, like the locking screw on a caliper.',
     'M3, brass (non-magnetic), into a brass heat-set insert (96) in the mount; axis along the wind (proposed). A bought knurled brass thumb screw, or a printed knob on a brass M3 screw (73). Length TBD', '1', 'printed knob: filament; thumb screw: price not checked', 'Choice open', 'owner sketch 2026-11-09; D-015'),
    (69, 'Overload stops', 'Catch the sting at about 120 g, below the cell’s 150 g safe limit.',
     'Printed PETG-CF with brass M3 screws. Gap TBD: set with a known mass', '1 set', 'filament', 'Printed', 'buy_list §6'),
    (70, 'Balance module plate', 'Carries the cell, base and stops as one module that comes out and lies on its side for calibration.',
     'Printed PETG-CF; mounts to the test-section frame. Size TBD', '1', 'filament', 'Printed', 'buy_list §9'),
    (71, 'Load-cell box', 'Closed box that keeps draughts and heat off the cell; holds only the cell and HX711.',
     'Printed. Size TBD', '1', 'filament', 'Printed', 'buy_list §8'),
    (72, 'HX711 amplifier board', 'Reads the load cell’s tiny bridge voltage as a 24-bit number.',
     'SparkFun HX711 breakout SEN-13879; bridge wires soldered straight to it (no breadboard)', '1', '$11.50', 'To buy', 'buy_list §6'),
    (73, 'Brass M3 screw', 'Non-magnetic fastener near the balance.',
     'M3 brass, short enough not to reach the cell’s middle', 'set', '$8–10', 'To buy', 'buy_list §2, §6'),
    (74, 'Calibration attachment', 'Fits the sting top in place of a ball; its groove hooks the pan at the ball-centre height.',
     'Printed: a cap over the 5/32 in sleeve, or a hook body on a 1/8 in brass stem (not a printed 1/8 in peg). Form TBD', '1', 'filament', 'Printed', 'buy_list §9'),
    (75, 'Calibration pan and thread', 'Light pan hung on a thread loop, so the pull always acts at the hook.',
     'Printed pan or foil cup; fine nylon thread or light fishing line', '1', 'a few dollars', 'Check house', 'buy_list §9'),
    (76, 'Calibration mass set', 'Known masses for the load-cell calibration; each piece weighed once on the school lab balance.',
     'Budget 17-piece set, 10 mg–100 g (sellers claim ±0.003 g, not certified). Leave the 100 g piece out', '1', '$20–40', 'To buy', 'buy_list §9'),
    (80, 'Wall pressure tap hole', 'Small hole that senses the wall static pressure.',
     'Ø0.8–1.0 mm, drilled square to the wall after printing (pin vise), deburred inside', '12', 'pin vise + bits (price not checked)', 'To buy (tool)', 'buy_list §5, §10'),
    (81, 'Tap boss', 'Thickened spot outside the wall that holds the brass stub.',
     'Printed with the wall. Size TBD', '12', 'filament', 'Printed', 'buy_list §5'),
    (82, 'Brass tap stub', 'Short tube the silicone line pushes onto.',
     'K&S 1/8 in (3.175 mm) OD brass tube, about 20 mm, glued (super glue or 5-minute epoxy)', '12', 'from 2 × 12 in tubes', 'To buy', 'buy_list §5'),
    (83, 'Silicone tubing', 'Carries pressure to the sensor; keep each line ≤ 0.5 m and pairs equal.',
     '1/8 in (3.2 mm) ID, about 1/16 in (1.6 mm) wall', '≈3 m', '$8–12', 'To buy', 'buy_list §5'),
    (84, 'Barbed tee', 'Joins a station’s four taps into one line.',
     'For 1/8 in tubing; 3 per station', '9', '$6–10 assortment', 'To buy', 'buy_list §5'),
    (85, 'Barbed straight coupler', 'Swap point where lines change between S/E and probe/M.',
     'For 1/8 in tubing', '2', 'in assortment', 'To buy', 'buy_list §5'),
    (86, 'Sensor pigtail', 'Short permanent tube on each sensor barb, so swaps never pull on the sensor.',
     'About 10 cm of item 83 ending in item 85', '2', '—', 'To buy', 'buy_list §5'),
    (87, 'Differential pressure sensor', 'Measures the pressure difference that gives airspeed.',
     'Sensirion SDP810-125Pa: ±125 Pa, body 29 × 18 mm, barbs Ø5.2/Ø3.5 at 12.6 mm, I²C 0x25. Multiply every reading by 966 mbar / p_amb', '1', '$29.39–34.72', 'To buy', 'SDP8xx, Sensirion2024 notes'),
    (88, 'Sensor bracket', 'Holds the sensor above its tubes so condensation drains away.',
     'Printed; 2 × Ø2.9 mm holes 24 mm apart', '1', 'filament', 'Printed', 'buy_list §5'),
    (89, 'Ambient sensor', 'Room pressure and temperature, for air density and the SDP810 correction.',
     'Adafruit BME280 (2652), 5 V-safe; in room air near the fan inlet, away from heat', '1', '$14.95', 'To buy', 'buy_list §7'),
    (90, 'Microcontroller', 'Reads the sensors and streams CSV to the laptop over USB.',
     'Elegoo Mega 2560 (working, Blink Verified 2026-11-02)', '1', 'on hand', 'On hand', 'PROJECT_STATUS §3'),
    (91, 'Arduino box', 'Keeps the Arduino apart from the balance so its heat and handling do not disturb the cell.',
     'Printed. Size TBD', '1', 'filament', 'Printed', 'buy_list §8'),
    (92, 'Sensor cable', 'Four-core leads from each sensor to the Arduino box.',
     '4-core, shielded if available, ≈3 m in all; each I²C run under about 1 m', '≈3 m', '$5–10', 'To buy', 'buy_list §8'),
    (93, 'USB cable to laptop', 'Power and data; the laptop is the log and the live view (D-012).',
     'USB A-to-B, carries data (2026-11-02)', '1', 'on hand', 'On hand', 'PROJECT_STATUS §3'),
    (95, 'Bolted flange', 'Joins two printed segments so they can come apart (screen frames come out). Owner’s design, D-013.',
     'Printed on each segment end. Width, thickness and bolt pattern TBD', 'per joint', 'filament', 'Printed', 'buy_list §2'),
    (96, 'Heat-set insert', 'Brass thread melted into the print for repeated assembly.',
     'M3 brass', '≈100 pack', '$11–20', 'To buy', 'buy_list §2'),
    (97, 'M3 screw', 'Clamps the flanges.',
     'M3 stainless (M4 alternative); brass (item 73) near the balance', 'set', '$10–15', 'To buy', 'buy_list §2'),
    (98, 'Alignment pin and hole', 'Lines up the inside walls of neighbouring segments (no steps).',
     'Pins or dowels in printed holes (D-005). Size TBD', 'per joint', 'TBD', 'To buy / Printed', 'DECISIONS D-005'),
    (99, 'Printed foot', 'Supports each section; no plywood base.',
     'Printed. Height TBD (the balance box must clear the bench)', 'per section', 'filament', 'Printed', 'buy_list §2'),
    (100, 'Rubber pad', 'Under each foot: grip and damping.',
     'Rubber pad or spare neoprene', '6–8', '≈$5', 'Check house', 'buy_list §2'),
]

ITEM = {n: dict(name=nm, does=d, spec=s, qty=q, cost=c, status=st, src=src)
        for (n, nm, d, s, q, c, st, src) in ITEMS}
