"""Sheets 9-10: pressure taps and airspeed; joints, flanges and feet."""
from wtsheets import *


def box(sh, x, y, w, hgt, title, sub=None, fill='#f4f5f7'):
    sh.rect(x, y, w, hgt, cls='vis2', fill=fill)
    sh.text(x + w / 2, y + hgt / 2 + (0 if sub else 5), title, cls='lbl', anchor='middle', weight=700)
    if sub:
        sh.text(x + w / 2, y + hgt / 2 + 17, sub, cls='sm', anchor='middle')


# =====================================================================================
def sheet_airspeed():
    sh = Sheet(9, 'WT-07', 'PRESSURE TAPS, PROBE, AIRSPEED SENSOR AND WIRING', '', 'NTS',
               ['Three tap stations (S, E, M) of four taps, one per wall, each joined into one line by three tees. Read each tap alone first.',
                'Force runs: S − E (contraction drop, ≈0.974 q in theory at CR 6.25), calibrated once against probe − M in the empty tunnel.',
                'Swap lines only at the couplers on the pigtails; check the wind-off zero returns within ≈0.1 Pa after each swap.',
                'Every SDP810 reading × 966 mbar / p_amb (Sensirion2024); p_amb from the BME280. Keep lines ≤ 0.5 m and pairs equal.',
                'Load-cell wires are soldered straight to the HX711 in the load-cell box: no breadboard in the bridge (Weakly2024).',
                'I²C at 100 kHz; pull-ups on the interface board (values TBD at circuit design, TODO P2). Arduino pins for the HX711 TBD.'])
    # ---------- detail H, wall tap 12:1 ----------
    s = 12
    v = View(290, 470, s)
    X, Y = v.X, v.Y
    sh.rect(X(-15), Y(3), v.L(30), v.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(-6), Y(11), v.L(12), v.L(8), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(-0.45), Y(3), v.L(0.9), v.L(3), cls='vis2', fill='#ffffff')       # tap hole
    sh.rect(X(-1.5875), Y(25), v.L(3.175), v.L(20), cls='vis2', fill='url(#hBr)')  # stub
    sh.rect(X(-1.1), Y(25), v.L(2.2), v.L(20), cls='vis2', fill='#ffffff')         # stub bore (ID not recorded)
    sh.rect(X(-1.1), Y(5), v.L(2.2), v.L(2), cls='vis2', fill='#ffffff')
    for s_ in (1, -1):
        x0 = 1.5875 if s_ > 0 else -1.5875 - 1.6
        sh.rect(X(x0), Y(32), v.L(1.6), v.L(15), cls='vis2', fill='#d8e4ee')
    sh.breakline(X(-15), Y(3.6), Y(-0.6))
    sh.breakline(X(15), Y(3.6), Y(-0.6))
    sh.text(X(0), Y(32) - 8, '(tube continues to the station tee)', cls='sm', anchor='middle')
    sh.flow(X(-12), Y(-3.2), 120, label='FLOW ALONG THE WALL')
    sh.text(X(0), Y(-7) + 4, 'TUNNEL INSIDE', cls='sm', anchor='middle')
    sh.hdim(X(-0.45), X(0.45), Y(0) + 4, Y(0) + 4, Y(-1.2), 'Ø0.8–1.0', st='P', tx=X(0) + 70, ty=Y(-1.2) + 4)
    sh.vdim(Y(3), Y(0), X(-15), X(-15), X(-15) - 26, 't TBD', st='T', side='l')
    sh.vdim(Y(11), Y(3), X(-6), X(-6), X(-15) - 26, 'TBD', st='T', side='l')
    sh.hdim(X(-1.5875), X(1.5875), Y(25) - 4, Y(25) - 4, Y(25) - 30, 'Ø3.175', st='F', tx=X(0) - 60)
    sh.vdim(Y(25), Y(5), X(1.6), X(1.6), X(10), '≈20', st='P', side='r')
    sh.lnote(X(1.5875 + 0.8), Y(29), X(8), Y(30), 'silicone tube ID 3.2, wall ≈1.6', st='F', anchor='start')
    sh.lnote(X(1.1), Y(16), X(8), Y(16.5), 'stub bore: K&S tube ID (not recorded)', st='T', anchor='start')
    sh.lnote(X(0), Y(1.6), X(8), Y(-5.2), 'drilled square after printing; deburr inside', st='P', anchor='start')
    sh.text(X(0), 540, 'DETAIL H — WALL PRESSURE TAP (12:1)', cls='vt', anchor='middle')
    sh.line(X(0) - 150, 544, X(0) + 150, 544, cls='vtu')
    sh.text(X(0), 561, 'Section square to the wall; boss and wall sizes TBD', cls='vs', anchor='middle')
    B(sh, 80, X(0.3), Y(1.5), 70, Y(1.5) + 70, side='r')
    B(sh, 81, X(-6), Y(9), 70, Y(9))
    B(sh, 82, X(-1.5875), Y(20), 70, Y(20))
    B(sh, 83, X(-1.5875 - 1.6), Y(30), 70, Y(30) - 10)

    # ---------- view J, tap station (schematic) ----------
    cx, cy, a = 790, 280, 70
    sh.rect(cx - a, cy - a, 2 * a, 2 * a, cls='vis', fill='#ffffff')
    sh.rect(cx - a - 8, cy - a - 8, 2 * a + 16, 2 * a + 16, cls='vis2')
    stubs = [(cx, cy - a - 8, cx, cy - a - 30), (cx + a + 8, cy, cx + a + 30, cy), (cx, cy + a + 8, cx, cy + a + 30), (cx - a - 8, cy, cx - a - 30, cy)]
    for x1, y1, x2, y2 in stubs:
        sh.line(x1, y1, x2, y2, cls='vis', extra='style="stroke:#8a6b16;stroke-width:4"')
    t1 = (cx + a + 30, cy - a - 30)
    t2 = (cx - a - 30, cy + a + 30)
    sh.path(f'M{cx},{cy - a - 30} L{t1[0]},{t1[1]} L{cx + a + 30},{cy}', cls='tube')
    sh.path(f'M{cx},{cy + a + 30} L{t2[0]},{t2[1]} L{cx - a - 30},{cy}', cls='tube')
    t3 = (cx + a + 70, cy + a + 30)
    sh.path(f'M{t1[0]},{t1[1]} L{t3[0]},{t1[1]} L{t3[0]},{t3[1]}', cls='tube')
    sh.path(f'M{t2[0]},{t2[1]} L{t3[0]},{t3[1]}', cls='tube')
    sh.path(f'M{t3[0]},{t3[1]} L{t3[0]},{t3[1] + 50}', cls='tube')
    for tx_, ty_ in (t1, t2, t3):
        sh.circ(tx_, ty_, 6, cls='vis2', fill='#ffffff')
    sh.text(t3[0] + 8, t3[1] + 46, 'one line per station', cls='sm', anchor='start')
    sh.text(cx, cy + 4, 'TUNNEL', cls='sm', anchor='middle')
    sh.text(cx, cy + 20, '(section, NTS)', cls='sm', anchor='middle')
    sh.text(cx + 20, 515, 'VIEW J — ONE TAP STATION (SCHEMATIC)', cls='vt', anchor='middle')
    sh.line(cx + 20 - 160, 519, cx + 20 + 160, 519, cls='vtu')
    sh.text(cx + 20, 536, 'Four taps → three tees → one line (S, E or M)', cls='vs', anchor='middle')
    B(sh, 84, t1[0] + 5, t1[1] - 4, t1[0] + 40, t1[1] - 30, side='r', name='Barbed tee (3 per station)')
    B(sh, 82, cx + 2, cy - a - 24, cx - 70, cy - a - 50, side='l', name='Brass tap stub')

    # ---------- view K, pneumatic schematic ----------
    ty0 = 640
    sx = [130, 300, 500, 760]
    # tunnel strip
    sh.path(f'M90,{ty0} L230,{ty0} C300,{ty0} 330,{ty0 + 30} 400,{ty0 + 30} L700,{ty0 + 30}', cls='vis')
    sh.path(f'M90,{ty0 + 120} L230,{ty0 + 120} C300,{ty0 + 120} 330,{ty0 + 90} 400,{ty0 + 90} L700,{ty0 + 90}', cls='vis')
    sh.text(160, ty0 + 64, 'SETTLING CHAMBER', cls='sm', anchor='middle')
    sh.text(315, ty0 + 64, 'CONTRACTION', cls='sm', anchor='middle')
    sh.text(560, ty0 + 112, 'TEST SECTION', cls='sm', anchor='middle')
    sh.flow(110, ty0 + 40, 60, label=None)
    sh.circ(610, ty0 + 60, 8, cls='vis2', fill='#f4f4f2')
    sh.text(610, ty0 + 84, 'sphere', cls='sm', anchor='middle')
    st_x = {'S': 200, 'E': 440, 'M': 610}
    for k_, xx in st_x.items():
        ytop = ty0 if k_ == 'S' else ty0 + 30
        sh.rect(xx - 3, ytop - 14, 6, 14, cls='vis2', fill='url(#hBr)')
        sh.text(xx, ytop - 20, k_, cls='lbl', anchor='middle', weight=700)
    # probe (dashed: empty tunnel only)
    sh.line(585, ty0 + 60, 600, ty0 + 60, cls='hid', extra='style="stroke-width:1.6"')
    sh.line(600, ty0 + 60, 600, ty0 + 30, cls='hid', extra='style="stroke-width:1.6"')
    # sensor
    sxs, sys_ = 820, 760
    sh.rect(sxs, sys_, 120, 60, cls='vis2', fill='#e8eaee')
    sh.text(sxs + 60, sys_ + 28, 'SDP810-125Pa', cls='lbl', anchor='middle', weight=700)
    sh.text(sxs + 60, sys_ + 46, 'H          L', cls='sm', anchor='middle')
    hx, lx = sxs + 30, sxs + 90
    for xx in (hx, lx):
        sh.line(xx, sys_, xx, sys_ - 40, cls='tube')
        sh.rect(xx - 6, sys_ - 52, 12, 12, cls='vis2', fill='#ffffff')
    # force-run lines (solid) and calibration lines (dashed)
    sh.path(f'M200,{ty0 - 14} L200,{ty0 - 50} L{hx - 10},{ty0 - 50} L{hx - 10},{sys_ - 60} L{hx},{sys_ - 52}', cls='tube')
    sh.path(f'M440,{ty0 + 16} L440,{ty0 - 30} L{lx},{ty0 - 30} L{lx},{sys_ - 52}', cls='tube')
    sh.path(f'M600,{ty0 + 30} L600,{ty0 + 160} L{hx},{ty0 + 160} L{hx},{sys_ - 40}', cls='tube', extra='style="stroke-dasharray:7 4"')
    sh.path(f'M610,{ty0 + 16} L640,{ty0 + 16} L640,{ty0 + 190} L{lx + 10},{ty0 + 190} L{lx + 10},{sys_ - 60} L{lx},{sys_ - 52}', cls='tube',
            extra='style="stroke-dasharray:7 4"')
    sh.text(90, 900, 'Solid: force runs (S → High, E → Low).  Dashed: probe calibration and flow map in the empty tunnel (probe → High, M → Low).', cls='sm')
    sh.text(90, 916, 'Swap at the two couplers only. Calibrate the contraction factor: read S − E, swap to probe − M, swap back, average the two S − E.', cls='sm')
    sh.text(420, 950, 'VIEW K — PNEUMATIC SCHEMATIC (NTS)', cls='vt', anchor='middle')
    sh.line(420 - 165, 954, 420 + 165, 954, cls='vtu')
    B(sh, 85, hx - 6, sys_ - 46, 940, 640, side='r', name='Barbed coupler (swap point)')
    B(sh, 86, lx + 1, sys_ - 22, 980, 700, side='r', name='Sensor pigtail ≈100')
    B(sh, 87, sxs + 120, sys_ + 40, 980, 850, side='r', name='Differential pressure sensor')
    B(sh, 51, 593, ty0 + 60, 520, ty0 + 200, side='l', name='Total-pressure probe')
    B(sh, 23, 200, ty0 - 4, 130, ty0 - 70, side='l', name='Tap station S')
    B(sh, 48, 440, ty0 + 28, 330, ty0 - 90, side='l', name='Tap station E')
    B(sh, 49, 613, ty0 + 24, 720, ty0 - 90, side='r', name='Tap station M')

    # ---------- view L, SDP810 outline 6:1 ----------
    s6 = 6
    vl = View(1210, 235, s6)
    Xl, Yl = vl.X, vl.Y
    bw, bh = P['sdp_body']
    sh.rect(Xl(-bw / 2), Yl(bh / 2), vl.L(bw), vl.L(bh), cls='vis', fill='#e8eaee')
    for xx in (-12, 12):
        sh.circ(Xl(xx), Yl(0), vl.L(P['sdp_hole_d'] / 2), cls='vis2', fill='#ffffff')
    for xx in (-6.3, 6.3):
        sh.circ(Xl(xx), Yl(0), vl.L(2.6), cls='vis2', fill='#ffffff')
        sh.circ(Xl(xx), Yl(0), vl.L(1.75), cls='vis2')
    for k in range(4):
        xx = -3 + 2 * k
        sh.rect(Xl(xx) - 1.5, Yl(-bh / 2), 3, vl.L(4), cls='vis2', fill='#c9a227')
    sh.centre(Xl(-bw / 2 - 4), Yl(0), Xl(bw / 2 + 4), Yl(0))
    sh.hdim(Xl(-bw / 2), Xl(bw / 2), Yl(bh / 2) - 4, Yl(bh / 2) - 4, Yl(bh / 2) - 40, '29', st='F')
    sh.hdim(Xl(-12), Xl(12), Yl(0) - 10, Yl(0) - 10, Yl(bh / 2) - 18, '24', st='F')
    sh.vdim(Yl(bh / 2), Yl(-bh / 2), Xl(bw / 2), Xl(bw / 2), Xl(bw / 2) + 24, '18', st='F', side='r')
    sh.hdim(Xl(-6.3), Xl(6.3), Yl(0) + 18, Yl(0) + 18, Yl(-bh / 2) + 40, '12.6', st='F')
    sh.lnote(Xl(-12) - 7, Yl(0) + 7, Xl(-bw / 2) - 20, Yl(-bh / 2) + 30, '2 × Ø2.9', st='F', anchor='end')
    sh.lnote(Xl(6.3) + 12, Yl(0) - 12, Xl(bw / 2) + 20, Yl(bh / 2) + 10, 'barbs Ø5.2 / Ø3.5', st='F', anchor='start')
    sh.lnote(Xl(3), Yl(-bh / 2) - 22, Xl(bw / 2) + 20, Yl(-bh / 2) + 30, '4 pins, 2 mm pitch', st='F', anchor='start')
    sh.text(1210, 402, 'VIEW L — SDP810-125Pa (6:1)', cls='vt', anchor='middle')
    sh.line(1210 - 130, 406, 1210 + 130, 406, cls='vtu')
    sh.text(1210, 423, 'Barb and pin positions on the body: datasheet p. 11 (drawn centred)', cls='vs', anchor='middle')
    B(sh, 88, Xl(-bw / 2) - 2, Yl(bh / 2) + 2, 1060, 110, side='r', name='Sensor bracket (TBD)')

    # ---------- view M, probe ----------
    vp = View(1500, 380, 1.9)
    Xp, Yp = vp.X, vp.Y
    sh.line(Xp(0), Yp(0), Xp(0), Yp(125), cls='vis', extra='style="stroke:#8a6b16;stroke-width:5"')
    sh.path(f'M{f(Xp(0))},{f(Yp(0))} Q{f(Xp(0))},{f(Yp(-6))} {f(Xp(-6))},{f(Yp(-6))} L{f(Xp(-25))},{f(Yp(-6))}', cls='vis',
            extra='style="stroke:#8a6b16;stroke-width:5;fill:none"')
    sh.vdim(Yp(125), Yp(-6), Xp(3), Xp(-3), Xp(20), '≈150\ntube', st='P', side='r')
    sh.hdim(Xp(-25), Xp(0), Yp(-6) + 6, Yp(-6) + 6, Yp(-6) + 26, 'TBD', st='T')
    sh.flow(Xp(-25) - 64, Yp(-6) - 18, 50, label=None)
    sh.text(1490, 432, 'VIEW M — PROBE', cls='vt', anchor='middle')
    B(sh, 51, Xp(-25), Yp(-6), 1440, 108, side='l', name='Total-pressure probe\n1/8 in brass, tip square')

    # ---------- view N, wiring block diagram ----------
    bx0, by0 = 1060, 470
    box(sh, bx0 + 170, by0 + 160, 150, 70, 'MEGA 2560', 'in Arduino box (91)')
    box(sh, bx0 + 380, by0 + 170, 110, 50, 'LAPTOP', 'USB log + live view')
    box(sh, bx0, by0 + 30, 140, 50, 'SDP810', 'I²C 0x25')
    box(sh, bx0, by0 + 110, 140, 50, 'BME280', 'I²C 0x76 / 0x77')
    box(sh, bx0, by0 + 250, 140, 50, 'HX711', 'DOUT, SCK')
    box(sh, bx0, by0 + 350, 140, 50, 'LOAD CELL', 'TAL221 100 g')
    sh.path(f'M{bx0 + 140},{by0 + 55} L{bx0 + 155},{by0 + 55} L{bx0 + 155},{by0 + 185} L{bx0 + 170},{by0 + 185}', cls='cable')
    sh.path(f'M{bx0 + 140},{by0 + 135} L{bx0 + 155},{by0 + 135}', cls='cable')
    sh.text(bx0 + 160, by0 + 100, 'I²C', cls='sm', anchor='start')
    sh.text(bx0 + 175, by0 + 152, 'SDA 20 · SCL 21', cls='sm', anchor='start')
    sh.path(f'M{bx0 + 140},{by0 + 275} L{bx0 + 155},{by0 + 275} L{bx0 + 155},{by0 + 210} L{bx0 + 170},{by0 + 210}', cls='cable')
    sh.text(bx0 + 175, by0 + 250, 'digital pins TBD', cls='sm', anchor='start', color=TBD)
    sh.path(f'M{bx0 + 70},{by0 + 350} L{bx0 + 70},{by0 + 300}', cls='vis', extra='style="stroke:#a33;stroke-width:1.6"')
    sh.text(bx0 + 78, by0 + 322, 'red E+ · black E− · green S+ · white S−', cls='sm', anchor='start')
    sh.text(bx0 + 78, by0 + 338, 'soldered direct, in the load-cell box', cls='sm', anchor='start')
    sh.path(f'M{bx0 + 320},{by0 + 195} L{bx0 + 380},{by0 + 195}', cls='cable')
    sh.text(bx0 + 350, by0 + 188, 'USB', cls='sm', anchor='middle')
    sh.text(1300, 905, 'VIEW N — WIRING BLOCK DIAGRAM', cls='vt', anchor='middle')
    sh.line(1300 - 140, 909, 1300 + 140, 909, cls='vtu')
    sh.text(1300, 926, 'Mains never reaches the Arduino; the fan keeps its own controller', cls='vs', anchor='middle')
    B(sh, 92, bx0 + 155, by0 + 120, bx0 + 230, by0 + 90, side='r', name='Sensor cable (4-core)')
    B(sh, 93, bx0 + 350, by0 + 195, bx0 + 420, by0 + 270, side='r', name='USB cable to laptop')
    B(sh, 89, bx0 + 140, by0 + 125, bx0 + 230, by0 + 40, side='r', name='Ambient sensor')
    B(sh, 90, bx0 + 245, by0 + 230, bx0 + 260, by0 + 330, side='r', name='Microcontroller')
    B(sh, 72, bx0 + 140, by0 + 290, bx0 + 260, by0 + 380, side='r', name='HX711 amplifier board')
    return sh


# =====================================================================================
def sheet_joints():
    sh = Sheet(10, 'WT-08', 'FLANGED JOINTS, ALIGNMENT AND FEET', '', 'NTS',
               ['Joints bolt together rather than glue, so screen frames can come out for cleaning (buy list §2; refines D-005).',
                'Flange width and thickness, bolt count and pitch, pin size, and insert length are TBD at sizing. Drawn at layout values.',
                'Inside faces must meet with no step: a 1 mm step at the contraction exit disturbs the flow just ahead of the sphere.',
                'Brass M3 screws near the balance; stainless elsewhere (M4 bolts are the alternative).',
                'No plywood base (owner): each section stands on its own printed feet. Check alignment with the spirit level and a straight edge.',
                'Gasket arrangement either side of a screen frame is TBD; the docs specify foam tape between bolted flanges.'])
    s = 10
    # ---------- detail P, flange joint with screen frame ----------
    v = View(330, 420, s)
    X, Y = v.X, v.Y
    ft, fw, g = 6, 14, 3.2
    xs = [-14.4, -8.4, -5.2, -2, 0, 2, 5.2, 11.2]   # flange A | gasket | frame half | frame half | gasket | flange B
    # walls (y: 0 = inside face, up = outward)
    sh.rect(X(-26), Y(3), v.L(26 - 14.4), v.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(11.2), Y(3), v.L(26 - 11.2), v.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(-14.4), Y(17), v.L(ft), v.L(17), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(5.2), Y(17), v.L(ft), v.L(17), cls='vis2', fill='url(#hPLA)')
    for x0 in (-8.4, 2):
        sh.rect(X(x0), Y(13), v.L(g), v.L(10), cls='vis2', fill='url(#hFoam)')
    sh.rect(X(-5.2), Y(16), v.L(3.2), v.L(16), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(-2 + 0.0), Y(16), v.L(2), v.L(16), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(0), Y(16), v.L(2), v.L(16), cls='vis2', fill='url(#hPETG)')
    sh.line(X(0), Y(16), X(0), Y(-12), cls='scr')
    # screw and insert at y = 10
    yb = 10
    sh.rect(X(-17.4), Y(yb + 2.75), v.L(3), v.L(5.5), cls='vis2', fill='#b9bec6')
    sh.rect(X(-14.4), Y(yb + 1.5), v.L(14.4 + 9), v.L(3), cls='vis2', fill='#d6d9de')
    sh.rect(X(6.2), Y(yb + 2.6), v.L(5), v.L(5.2), cls='vis2', fill='url(#hBr)')
    sh.breakline(X(-26), Y(3.5), Y(-0.5))
    sh.breakline(X(26), Y(3.5), Y(-0.5))
    sh.line(X(-28), Y(0), X(28), Y(0), cls='ctr')
    sh.text(X(-28) - 4, Y(0) + 4, 'inside face', cls='sm', anchor='end')
    sh.flow(X(-24), Y(-7), 110)
    sh.vdim(Y(17), Y(3), X(-14.4), X(-14.4), X(-26), 'TBD', st='T', side='l')
    sh.vdim(Y(3), Y(0), X(-26), X(-26), X(-26), '', st='T', ext=False)
    sh.lnote(X(-20), Y(1.5), X(-24), Y(-4) + 0, 't TBD', st='T', anchor='end')
    sh.hdim(X(-14.4), X(-8.4), Y(17) - 4, Y(17) - 4, Y(17) - 30, 'TBD', st='T')
    sh.hdim(X(-8.4), X(-5.2), Y(13) - 4, Y(13) - 4, Y(17) - 60, '3.2', st='P', tx=X(-6.8) + 4)
    sh.lnote(X(-15.9), Y(yb), X(-22), Y(22), 'M3 screw', st='P', anchor='end')
    sh.lnote(X(8.7), Y(yb + 2.6), X(14), Y(22), 'M3 heat-set insert (length TBD)', st='P', anchor='start')
    sh.lnote(X(0), Y(-10), X(6), Y(-10) + 4, 'no step at the inside face', st='P', anchor='start')
    sh.text(X(0), 590, 'DETAIL P — FLANGED JOINT WITH SCREEN FRAME (10:1)', cls='vt', anchor='middle')
    sh.line(X(0) - 210, 594, X(0) + 210, 594, cls='vtu')
    sh.text(X(0), 611, 'Section through one bolt, top wall · joints J2, J3, J4', cls='vs', anchor='middle')
    B(sh, 95, X(-11.4), Y(16), 120, 120, side='r', name='Bolted flange')
    B(sh, 46, X(-6.8), Y(12.5), 240, 160, side='r', name='Foam gasket tape')
    B(sh, 13, X(-1.5), Y(15.5), 380, 120, side='r', name='Screen frame (two-part)')
    B(sh, 12, X(0.2), Y(-6), 500, 520, side='r', name='Screen')
    B(sh, 97, X(-16), Y(yb + 2.75), 90, 300, side='r')
    B(sh, 96, X(8.7), Y(yb - 2.6), 540, 300, side='r')

    # ---------- detail Q, plain joint with alignment pin ----------
    vq = View(820, 420, s)
    Xq, Yq = vq.X, vq.Y
    sh.rect(Xq(-20), Yq(3), vq.L(20 - 7.6), vq.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xq(7.6), Yq(3), vq.L(20 - 7.6), vq.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xq(-7.6), Yq(17), vq.L(ft), vq.L(17), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xq(1.6), Yq(17), vq.L(ft), vq.L(17), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xq(-1.6), Yq(13), vq.L(3.2), vq.L(10), cls='vis2', fill='url(#hFoam)')
    sh.rect(Xq(-6.5), Yq(11.5), vq.L(13), vq.L(3), cls='vis2', fill='#d6d9de')
    sh.breakline(Xq(-20), Yq(3.5), Yq(-0.5))
    sh.breakline(Xq(20), Yq(3.5), Yq(-0.5))
    sh.line(Xq(-22), Yq(0), Xq(22), Yq(0), cls='ctr')
    sh.lnote(Xq(4), Yq(10), Xq(10), Yq(24), 'pin Ø and length TBD', st='T', anchor='start')
    sh.text(Xq(0), 590, 'DETAIL Q — PLAIN JOINT, PIN (10:1)', cls='vt', anchor='middle')
    sh.line(Xq(0) - 140, 594, Xq(0) + 140, 594, cls='vtu')
    sh.text(Xq(0), 611, 'Section through one pin · joints J5, J6', cls='vs', anchor='middle')
    B(sh, 98, Xq(-3), Yq(10), 680, 160, side='r', name='Alignment pin and hole')

    # ---------- view R, flange face ----------
    vr = View(1290, 300, 0.85)
    Xr, Yr = vr.X, vr.Y
    rr = HALF + T + 14
    sh.rect(Xr(-rr), Yr(rr), vr.L(2 * rr), vr.L(2 * rr), cls='vis', fill='url(#hPLA)')
    sh.rect(Xr(-HALF - T), Yr(HALF + T), vr.L(2 * (HALF + T)), vr.L(2 * (HALF + T)), cls='thin', fill='#ffffff')
    sh.rect(Xr(-HALF), Yr(HALF), vr.L(2 * HALF), vr.L(2 * HALF), cls='vis2', fill='#ffffff')
    sh.rect(Xr(-HALF - T - 1), Yr(HALF + T + 1), vr.L(2 * (HALF + T + 1)), vr.L(2 * (HALF + T + 1)), cls='hid')
    pos = [-90, 0, 90]
    for p_ in pos:
        for (bx_, by_) in ((p_, rr - 7), (p_, -rr + 7), (rr - 7, p_), (-rr + 7, p_)):
            sh.circ(Xr(bx_), Yr(by_), vr.L(1.7) + 1.2, cls='vis2', fill='#ffffff')
    for (px_, py_) in ((rr - 7, rr - 7), (-rr + 7, -rr + 7)):
        sh.circ(Xr(px_), Yr(py_), vr.L(1.7) + 1.8, cls='vis2', fill='#3a3f47')
    sh.centre(Xr(-rr - 10), Yr(0), Xr(rr + 10), Yr(0))
    sh.centre(Xr(0), Yr(rr + 10), Xr(0), Yr(-rr - 10))
    sh.vdim(Yr(HALF), Yr(-HALF), Xr(HALF), Xr(HALF), Xr(rr) + 22, '250', st='P', side='r')
    sh.hdim(Xr(-rr), Xr(rr), Yr(rr) - 4, Yr(rr) - 4, Yr(rr) - 24, 'TBD', st='T')
    sh.text(1290, Yr(-rr) + 34, 'VIEW R — FLANGE FACE, SETTLING CHAMBER', cls='vt', anchor='middle')
    sh.line(1290 - 170, Yr(-rr) + 38, 1290 + 170, Yr(-rr) + 38, cls='vtu')
    sh.text(1290, Yr(-rr) + 55, 'Bolt count and pitch TBD (drawn 12); two pins at opposite corners (filled)', cls='vs', anchor='middle')
    B(sh, 98, Xr(rr - 7), Yr(rr - 7), Xr(rr) + 40, Yr(rr) - 40, side='r', name='Alignment pin')
    B(sh, 97, Xr(90), Yr(rr - 7), Xr(90) + 30, Yr(rr) - 60, side='r', name='M3 screw (12 shown)')

    # ---------- view S, printed foot ----------
    vs = View(270, 800, 1.6)
    Xs, Ys = vs.X, vs.Y
    sh.rect(Xs(-90), Ys(0), vs.L(180), vs.L(3), cls='vis2', fill='url(#hPLA)')
    sh.text(Xs(0), Ys(0) - 8, 'bottom wall of a section', cls='sm', anchor='middle')
    sh.pl([(Xs(-30), Ys(-3)), (Xs(-22), Ys(-40)), (Xs(22), Ys(-40)), (Xs(30), Ys(-3))], cls='vis2', close=True, fill='url(#hPLA)')
    sh.rect(Xs(-22), Ys(-40), vs.L(44), vs.L(4), cls='fill-neo')
    sh.line(Xs(-100), Ys(-44), Xs(100), Ys(-44), cls='vis2')
    xx = Xs(-100)
    while xx < Xs(100) - 8:
        sh.line(xx, Ys(-44), xx + 8, Ys(-44) + 8, cls='thin')
        xx += 16
    sh.vdim(Ys(-3), Ys(-40), Xs(-30), Xs(-22), Xs(-60), 'TBD', st='T', side='l')
    sh.hdim(Xs(-22), Xs(22), Ys(-44) + 4, Ys(-44) + 4, Ys(-44) + 26, 'TBD', st='T')
    sh.text(Xs(0), 905, 'VIEW S — PRINTED FOOT AND PAD (NTS SHAPE)', cls='vt', anchor='middle')
    sh.line(Xs(0) - 170, 909, Xs(0) + 170, 909, cls='vtu')
    sh.text(Xs(0), 926, 'Feet heights set so the balance box clears the bench', cls='vs', anchor='middle')
    B(sh, 99, Xs(20), Ys(-20), Xs(60), Ys(-10), side='r')
    B(sh, 100, Xs(15), Ys(-38), Xs(60), Ys(-34), side='r')

    # ---------- fastener schedule ----------
    tx, ty = 620, 700
    sh.text(tx, ty, 'FASTENER AND JOINT SCHEDULE', cls='kh')
    rows = [('95', 'Bolted flange', 'Printed on each segment end; width, thickness TBD'),
            ('96', 'Heat-set insert', 'M3 brass; pack of 100'),
            ('97', 'M3 screw', 'Stainless; M4 alternative'),
            ('73', 'Brass M3 screw', 'Near the balance (non-magnetic)'),
            ('98', 'Alignment pin and hole', 'Pins or dowels (D-005); size TBD'),
            ('46', 'Foam gasket tape', '≈3.2 thick × 6.4–9.5 wide, closed-cell'),
            ('99', 'Printed foot', 'Height TBD; no plywood base'),
            ('100', 'Rubber pad', 'Or spare 1.6 mm neoprene')]
    for i, (n_, a_, b_) in enumerate(rows):
        yy = ty + 24 + i * 22
        sh.circ(tx + 12, yy - 4, 11, cls='bal')
        sh.text(tx + 12, yy, n_, cls='bnum', anchor='middle', size=10 if len(n_) > 2 else 12)
        sh.text(tx + 32, yy, a_, cls='tblc', weight=700)
        sh.text(tx + 200, yy, b_, cls='tblc')
        sh.line(tx, yy + 8, tx + 520, yy + 8, cls='thin', extra='stroke-opacity="0.22"')
    return sh
