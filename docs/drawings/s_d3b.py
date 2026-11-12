"""Sheets 9-10, second layout."""
from wtsheets import *
from s_d3 import box


def sheet_airspeed():
    sh = Sheet(9, 'WT-07', 'PRESSURE TAPS, PROBE, AIRSPEED SENSOR, WIRING', '', 'NTS',
               ['Three tap stations (S, E, M) of four taps, one per wall, each joined into one line by three tees. Read each tap alone first.',
                'Force runs: S − E (contraction drop, ≈0.974 q in theory at CR 6.25), calibrated once against probe − M in the empty tunnel.',
                'Swap lines only at the couplers on the pigtails; check the wind-off zero returns within ≈0.1 Pa after each swap.',
                'Every SDP810 reading × 966 mbar / p_amb (Sensirion2024); p_amb from the BME280. Keep lines ≤ 0.5 m and pairs equal.',
                'Load-cell wires are soldered straight to the HX711 in the load-cell box: no breadboard in the bridge (Weakly2024).',
                'I²C at 100 kHz; pull-ups on the interface board (values TBD at circuit design, TODO P2). Arduino pins for the HX711 TBD.'])
    # ---------- detail H, wall tap 11:1 ----------
    s = 11
    v = View(300, 445, s)
    X, Y = v.X, v.Y
    sh.rect(X(-15), Y(3), v.L(30), v.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(-6), Y(11), v.L(12), v.L(8), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(-0.45), Y(3), v.L(0.9), v.L(3), cls='vis2', fill='#ffffff')
    sh.rect(X(-1.5875), Y(25), v.L(3.175), v.L(20), cls='vis2', fill='url(#hBr)')
    sh.rect(X(-1.1), Y(25), v.L(2.2), v.L(20), cls='vis2', fill='#ffffff')
    sh.rect(X(-1.1), Y(5), v.L(2.2), v.L(2), cls='vis2', fill='#ffffff')
    for s_ in (1, -1):
        x0 = 1.5875 if s_ > 0 else -1.5875 - 1.6
        sh.rect(X(x0), Y(32), v.L(1.6), v.L(15), cls='vis2', fill='#d8e4ee')
    sh.breakline(X(-15), Y(3.6), Y(-0.6))
    sh.breakline(X(15), Y(3.6), Y(-0.6))
    sh.text(X(0), Y(32) - 8, '(tube continues to the station tee)', cls='sm', anchor='middle')
    sh.flow(X(2.5), Y(-6.2), 110, label='FLOW ALONG THE WALL')
    sh.hdim(X(-0.45), X(0.45), Y(0) + 4, Y(0) + 4, Y(-1.4), 'Ø0.8–1.0', st='P', tx=X(0) + 62, ty=Y(-1.4) + 4)
    sh.hdim(X(-1.5875), X(1.5875), Y(14), Y(14), Y(14), 'Ø3.175', st='F', tx=X(-1.6) - 40, ty=Y(14) + 4, ext=False)
    sh.vdim(Y(25), Y(5), X(1.6), X(1.6), X(10), '≈20', st='P', side='r')
    sh.vdim(Y(11), Y(3), X(6), X(6), X(16), 'TBD', st='T', side='r')
    sh.vdim(Y(3), Y(0), X(15), X(15), X(16), 't TBD', st='T', side='r', ty=Y(0) + 14)
    sh.lnote(X(1.5875 + 0.8), Y(29), X(8), Y(30), 'silicone tube ID 3.2, wall ≈1.6', st='F', anchor='start')
    sh.text(X(0), 545, 'DETAIL H — WALL PRESSURE TAP (11:1)', cls='vt', anchor='middle')
    sh.line(X(0) - 150, 549, X(0) + 150, 549, cls='vtu')
    sh.text(X(0), 566, 'Hole drilled square to the wall after printing, deburred inside; boss sizes TBD', cls='vs', anchor='middle')
    B(sh, 83, X(-1.5875 - 1.6), Y(30), 200, Y(30), side='l')
    B(sh, 82, X(-1.5875), Y(20), 200, Y(20), side='l')
    B(sh, 81, X(-6), Y(8), 200, Y(8), side='l')
    B(sh, 80, X(-0.2), Y(1.5), 200, Y(-4), side='l')

    # ---------- view J, tap station ----------
    cx, cy, a = 800, 270, 66
    sh.rect(cx - a, cy - a, 2 * a, 2 * a, cls='vis', fill='#ffffff')
    sh.rect(cx - a - 8, cy - a - 8, 2 * a + 16, 2 * a + 16, cls='vis2')
    for x1, y1, x2, y2 in ((cx, cy - a - 8, cx, cy - a - 30), (cx + a + 8, cy, cx + a + 30, cy), (cx, cy + a + 8, cx, cy + a + 30), (cx - a - 8, cy, cx - a - 30, cy)):
        sh.line(x1, y1, x2, y2, cls='vis', extra='style="stroke:#8a6b16;stroke-width:4"')
    t1 = (cx + a + 30, cy - a - 30)
    t2 = (cx - a - 30, cy + a + 30)
    t3 = (cx + a + 70, cy + a + 30)
    sh.path(f'M{cx},{cy - a - 30} L{t1[0]},{t1[1]} L{cx + a + 30},{cy}', cls='tube')
    sh.path(f'M{cx},{cy + a + 30} L{t2[0]},{t2[1]} L{cx - a - 30},{cy}', cls='tube')
    sh.path(f'M{t1[0]},{t1[1]} L{t3[0]},{t1[1]} L{t3[0]},{t3[1]}', cls='tube')
    sh.path(f'M{t2[0]},{t2[1]} L{t3[0]},{t3[1]}', cls='tube')
    sh.path(f'M{t3[0]},{t3[1]} L{t3[0]},{t3[1] + 46}', cls='tube')
    for tx_, ty_ in (t1, t2, t3):
        sh.circ(tx_, ty_, 6, cls='vis2', fill='#ffffff')
    sh.text(t3[0] - 8, t3[1] + 44, 'to coupler', cls='sm', anchor='end')
    sh.text(cx, cy + 4, 'TUNNEL', cls='sm', anchor='middle')
    sh.text(cx, cy + 20, '(section, NTS)', cls='sm', anchor='middle')
    sh.text(cx + 20, 545, 'VIEW J — ONE TAP STATION (SCHEMATIC)', cls='vt', anchor='middle')
    sh.line(cx + 20 - 160, 549, cx + 20 + 160, 549, cls='vtu')
    sh.text(cx + 20, 566, 'Four taps → three tees → one line (S, E or M)', cls='vs', anchor='middle')
    B(sh, 84, t1[0] + 5, t1[1] - 4, t1[0] + 30, t1[1] - 40, side='r', name='Barbed tee (3 per station)')
    B(sh, 82, cx + 2, cy - a - 24, cx - 70, cy - a - 52, side='l', name='Brass tap stub')

    # ---------- view K, ladder schematic ----------
    k0 = 640
    srcs = [('S', 'Settling chamber, before the contraction', 23), ('E', 'Test-section entrance', 48),
            ('M', 'Model station (wall taps)', 49), ('P', 'Probe tip at M (empty tunnel)', 51)]
    for i, (lab, desc, it) in enumerate(srcs):
        yy = k0 + i * 58
        sh.rect(140, yy, 285, 38, cls='vis2', fill='#f4f5f7')
        sh.text(156, yy + 25, lab, cls='lbl', weight=700, size=15)
        sh.text(178, yy + 24, desc, cls='lbl')
        B(sh, it, 140, yy + 19, 100, yy + 19, side='l', name='')
    hcx, lcx = 640, 640
    hy, ly = k0 + 40, k0 + 150
    sh.path(f'M425,{k0 + 19} L470,{k0 + 19} L470,{hy} L{hcx - 8},{hy}', cls='tube')
    sh.path(f'M425,{k0 + 58 + 19} L500,{k0 + 58 + 19} L500,{ly} L{lcx - 8},{ly}', cls='tube')
    sh.path(f'M425,{k0 + 116 + 19} L530,{k0 + 116 + 19} L530,{ly + 8} L{lcx - 8},{ly + 8}', cls='tube', extra='style="stroke-dasharray:7 4"')
    sh.path(f'M425,{k0 + 174 + 19} L560,{k0 + 174 + 19} L560,{hy + 8} L{hcx - 8},{hy + 8}', cls='tube', extra='style="stroke-dasharray:7 4"')
    for yy in (hy + 4, ly + 4):
        sh.rect(hcx - 8, yy - 9, 16, 18, cls='vis2', fill='#ffffff')
        sh.path(f'M{hcx + 8},{yy} L760,{yy}', cls='tube')
    sxs, sys_ = 760, k0 + 20
    sh.rect(sxs, sys_, 130, 170, cls='vis2', fill='#e8eaee')
    sh.text(sxs + 65, sys_ + 80, 'SDP810', cls='lbl', anchor='middle', weight=700)
    sh.text(sxs + 65, sys_ + 98, '-125Pa', cls='lbl', anchor='middle', weight=700)
    sh.text(sxs + 10, hy + 8, 'H', cls='lbl', anchor='start', weight=700)
    sh.text(sxs + 10, ly + 8, 'L', cls='lbl', anchor='start', weight=700)
    sh.text(90, 880, 'Solid: force runs (S → High, E → Low). Dashed: probe calibration and flow map, empty tunnel (P → High, M → Low).', cls='sm')
    sh.text(90, 896, 'Contraction factor: read S − E, swap to P − M, swap back, average the two S − E. One line on each coupler at a time.', cls='sm')
    sh.text(470, 935, 'VIEW K — PNEUMATIC SCHEMATIC (NTS)', cls='vt', anchor='middle')
    sh.line(470 - 165, 939, 470 + 165, 939, cls='vtu')
    B(sh, 85, hcx, hy - 5, 600, k0 - 22, side='r', name='Barbed coupler (swap point, 2)')
    B(sh, 86, 720, ly + 4, 690, ly + 70, side='r', name='Sensor pigtail ≈100')
    B(sh, 87, sxs + 130, sys_ + 120, 930, sys_ + 150, side='r', name='Differential\npressure sensor')
    B(sh, 83, 450, k0 + 19, 450, k0 - 22, side='r', name='Silicone tubing')

    # ---------- view L, SDP810 6:1 ----------
    vl = View(1180, 240, 6)
    Xl, Yl = vl.X, vl.Y
    bw, bh = P['sdp_body']
    sh.rect(Xl(-bw / 2), Yl(bh / 2), vl.L(bw), vl.L(bh), cls='vis', fill='#e8eaee')
    for xx in (-12, 12):
        sh.circ(Xl(xx), Yl(0), vl.L(P['sdp_hole_d'] / 2), cls='vis2', fill='#ffffff')
    for xx in (-6.3, 6.3):
        sh.circ(Xl(xx), Yl(0), vl.L(2.6), cls='vis2', fill='#ffffff')
        sh.circ(Xl(xx), Yl(0), vl.L(1.75), cls='vis2')
    for k in range(4):
        sh.rect(Xl(-3 + 2 * k) - 1.5, Yl(-bh / 2), 3, vl.L(4), cls='vis2', fill='#c9a227')
    sh.centre(Xl(-bw / 2 - 4), Yl(0), Xl(bw / 2 + 4), Yl(0))
    sh.hdim(Xl(-bw / 2), Xl(bw / 2), Yl(bh / 2) - 4, Yl(bh / 2) - 4, Yl(bh / 2) - 40, '29', st='F')
    sh.hdim(Xl(-12), Xl(12), Yl(0) - 10, Yl(0) - 10, Yl(bh / 2) - 18, '24', st='F')
    sh.vdim(Yl(bh / 2), Yl(-bh / 2), Xl(bw / 2), Xl(bw / 2), Xl(bw / 2) + 22, '18', st='F', side='r')
    sh.hdim(Xl(-6.3), Xl(6.3), Yl(0) + 18, Yl(0) + 18, Yl(-bh / 2) + 44, '12.6', st='F')
    sh.lnote(Xl(-12) - 7, Yl(0) + 7, Xl(-bw / 2) - 16, Yl(-bh / 2) + 30, '2 × Ø2.9', st='F', anchor='end')
    sh.lnote(Xl(6.3) + 12, Yl(0) - 12, Xl(bw / 2) + 50, Yl(bh / 2) - 6, 'barbs\nØ5.2 / Ø3.5', st='F', anchor='start')
    sh.lnote(Xl(3), Yl(-bh / 2) - 22, Xl(bw / 2) + 50, Yl(-bh / 2) + 34, '4 pins,\n2 mm pitch', st='F', anchor='start')
    sh.text(1180, 410, 'VIEW L — SDP810-125Pa (6:1)', cls='vt', anchor='middle')
    sh.line(1180 - 130, 414, 1180 + 130, 414, cls='vtu')
    sh.text(1180, 431, 'Barbs and pins drawn centred: positions per datasheet p. 11', cls='vs', anchor='middle')
    B(sh, 88, Xl(-bw / 2) - 2, Yl(bh / 2) + 2, 1050, 110, side='r', name='Sensor bracket (TBD)')

    # ---------- view M, probe ----------
    vp = View(1478, 395, 1.9)
    Xp, Yp = vp.X, vp.Y
    sh.line(Xp(0), Yp(0), Xp(0), Yp(125), cls='vis', extra='style="stroke:#8a6b16;stroke-width:5"')
    sh.path(f'M{f(Xp(0))},{f(Yp(0))} Q{f(Xp(0))},{f(Yp(-6))} {f(Xp(-6))},{f(Yp(-6))} L{f(Xp(-25))},{f(Yp(-6))}', cls='vis',
            extra='style="stroke:#8a6b16;stroke-width:5;fill:none"')
    sh.vdim(Yp(125), Yp(-6), Xp(3), Xp(-3), Xp(18), '≈150\ntube', st='P', side='r')
    sh.hdim(Xp(-25), Xp(0), Yp(-6) + 6, Yp(-6) + 6, Yp(-6) + 24, 'TBD', st='T')
    sh.flow(Xp(-25) - 62, Yp(-6) - 16, 48, label=None)
    sh.text(1490, 452, 'VIEW M — PROBE', cls='vt', anchor='middle')
    B(sh, 51, Xp(-25), Yp(-6), 1440, 130, side='l', name='Total-pressure probe\n1/8 in brass, tip square')

    # ---------- view N, wiring ----------
    x0 = 1120
    box(sh, x0, 500, 140, 50, 'SDP810', 'I²C 0x25')
    box(sh, x0, 580, 140, 50, 'BME280', 'I²C 0x76 / 0x77')
    box(sh, x0, 720, 140, 50, 'HX711', 'DOUT, SCK')
    box(sh, x0, 820, 140, 50, 'LOAD CELL', 'TAL221 100 g')
    box(sh, 1290, 630, 140, 70, 'MEGA 2560', 'in Arduino box (91)')
    box(sh, 1460, 640, 110, 50, 'LAPTOP', 'log + live view')
    sh.path(f'M{x0 + 140},525 L1275,525 L1275,655 L1290,655', cls='cable')
    sh.path(f'M{x0 + 140},605 L1275,605', cls='cable')
    sh.text(1279, 570, 'I²C', cls='sm', anchor='start')
    sh.text(1295, 622, 'SDA 20 · SCL 21', cls='sm', anchor='start')
    sh.path(f'M{x0 + 140},745 L1275,745 L1275,680 L1290,680', cls='cable')
    sh.text(1295, 720, 'digital pins TBD', cls='sm', anchor='start', color=TBD)
    sh.path(f'M{x0 + 70},820 L{x0 + 70},770', cls='vis', extra='style="stroke:#a33;stroke-width:1.6"')
    sh.text(x0 + 78, 792, 'red E+ · black E− · green S+ · white S−', cls='sm', anchor='start')
    sh.text(x0 + 78, 808, 'soldered direct, in the load-cell box', cls='sm', anchor='start')
    sh.path('M1430,665 L1460,665', cls='cable')
    sh.text(1445, 658, 'USB', cls='sm', anchor='middle')
    sh.text(1340, 905, 'VIEW N — WIRING BLOCK DIAGRAM', cls='vt', anchor='middle')
    sh.line(1340 - 140, 909, 1340 + 140, 909, cls='vtu')
    sh.text(1340, 926, 'Mains never reaches the Arduino; the fan keeps its own controller', cls='vs', anchor='middle')
    B(sh, 92, 1275, 560, 1400, 545, side='r', name='Sensor cable (4-core)')
    B(sh, 89, x0 + 140, 598, 1400, 590, side='r', name='Ambient sensor')
    B(sh, 93, 1445, 665, 1545, 612, side='l', name='USB cable to laptop')
    B(sh, 90, 1420, 700, 1460, 742, side='r', name='Microcontroller')
    B(sh, 72, x0 + 140, 760, 1300, 762, side='r', name='HX711 amplifier board')
    return sh


# =====================================================================================
def sheet_joints():
    sh = Sheet(10, 'WT-08', 'FLANGED JOINTS, ALIGNMENT AND FEET', '', 'NTS',
               ['Joints bolt together rather than glue, so screen frames can come out for cleaning (buy list §2; refines D-005).',
                'Flange width and thickness, bolt count and pitch, pin size, and insert length are TBD at sizing. Drawn at layout values.',
                'Inside faces must meet with no step: a 1 mm step at the contraction exit disturbs the flow just ahead of the sphere.',
                'Stainless M3 screws throughout, short ones (73) at the balance; M4 bolts are the alternative.',
                'No plywood base (owner): each section stands on its own printed feet. Check alignment with the spirit level and a straight edge.',
                'Gasket arrangement either side of a screen frame is TBD; the docs specify foam tape between bolted flanges.'])
    s = 10
    v = View(330, 420, s)
    X, Y = v.X, v.Y
    ft, g = 6, 3.2
    sh.rect(X(-26), Y(3), v.L(26 - 14.4), v.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(11.2), Y(3), v.L(26 - 11.2), v.L(3), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(-14.4), Y(17), v.L(ft), v.L(17), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(5.2), Y(17), v.L(ft), v.L(17), cls='vis2', fill='url(#hPLA)')
    for x0 in (-8.4, 2):
        sh.rect(X(x0), Y(13), v.L(g), v.L(10), cls='vis2', fill='url(#hFoam)')
    sh.rect(X(-5.2), Y(16), v.L(3.2), v.L(16), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(-2), Y(16), v.L(2), v.L(16), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(0), Y(16), v.L(2), v.L(16), cls='vis2', fill='url(#hPETG)')
    sh.line(X(0), Y(16), X(0), Y(-12), cls='scr')
    yb = 10
    sh.rect(X(-17.4), Y(yb + 2.75), v.L(3), v.L(5.5), cls='vis2', fill='#b9bec6')
    sh.rect(X(-14.4), Y(yb + 1.5), v.L(14.4 + 9), v.L(3), cls='vis2', fill='#d6d9de')
    sh.rect(X(6.2), Y(yb + 2.6), v.L(5), v.L(5.2), cls='vis2', fill='url(#hBr)')
    sh.breakline(X(-26), Y(3.5), Y(-0.5))
    sh.breakline(X(26), Y(3.5), Y(-0.5))
    sh.line(X(-28), Y(0), X(28), Y(0), cls='ctr')
    sh.text(X(28) + 4, Y(0) + 18, 'inside face', cls='sm', anchor='start')
    sh.flow(X(-24), Y(-7), 110)
    sh.vdim(Y(17), Y(3), X(-14.4), X(-14.4), X(-26), 'TBD', st='T', side='l')
    sh.lnote(X(-20), Y(1.5), X(-24), Y(-12), 't TBD', st='T', anchor='end')
    sh.hdim(X(-14.4), X(-8.4), Y(17) - 4, Y(17) - 4, Y(17) - 30, 'TBD', st='T')
    sh.hdim(X(-8.4), X(-5.2), Y(13) - 4, Y(13) - 4, Y(17) - 60, '3.2', st='P', tx=X(-6.8) + 4)
    sh.lnote(X(8.7), Y(yb - 2.6), X(12), Y(-6), 'insert length TBD', st='T', anchor='start')
    sh.lnote(X(1), Y(0), X(8), Y(-11) + 0, 'no step at the inside face', st='P', anchor='start')
    sh.text(X(0), 590, 'DETAIL P — FLANGED JOINT WITH SCREEN FRAME (10:1)', cls='vt', anchor='middle')
    sh.line(X(0) - 210, 594, X(0) + 210, 594, cls='vtu')
    sh.text(X(0), 611, 'Section through one bolt, top wall · joints J2, J3, J4', cls='vs', anchor='middle')
    B(sh, 95, X(-11.4), Y(16), 120, 120, side='r', name='Bolted flange')
    B(sh, 46, X(-6.8), Y(12.5), 240, 160, side='r', name='Foam gasket tape')
    B(sh, 13, X(-1.5), Y(15.5), 380, 120, side='r', name='Screen frame (two-part)')
    B(sh, 12, X(0.2), Y(-8), 250, 530, side='l', name='Screen')
    B(sh, 97, X(-16), Y(yb + 2.75), 90, 222, side='r', name='M3 screw')
    B(sh, 96, X(8.7), Y(yb + 2.6), 540, 250, side='r', name='Heat-set insert (M3)')

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
    sh.flow(Xq(-18), Yq(-7), 90, label=None)
    sh.text(Xq(0), 590, 'DETAIL Q — PLAIN JOINT, PIN (10:1)', cls='vt', anchor='middle')
    sh.line(Xq(0) - 140, 594, Xq(0) + 140, 594, cls='vtu')
    sh.text(Xq(0), 611, 'Section through one pin · joints J5, J6', cls='vs', anchor='middle')
    B(sh, 98, Xq(-3), Yq(10), 680, 160, side='r', name='Alignment pin and hole')

    vr = View(1345, 300, 0.85)
    Xr, Yr = vr.X, vr.Y
    rr = HALF + T + 14
    sh.rect(Xr(-rr), Yr(rr), vr.L(2 * rr), vr.L(2 * rr), cls='vis', fill='url(#hPLA)')
    sh.rect(Xr(-HALF - T), Yr(HALF + T), vr.L(2 * (HALF + T)), vr.L(2 * (HALF + T)), cls='thin', fill='#ffffff')
    sh.rect(Xr(-HALF), Yr(HALF), vr.L(2 * HALF), vr.L(2 * HALF), cls='vis2', fill='#ffffff')
    for p_ in (-90, 0, 90):
        for (bx_, by_) in ((p_, rr - 7), (p_, -rr + 7), (rr - 7, p_), (-rr + 7, p_)):
            sh.circ(Xr(bx_), Yr(by_), vr.L(1.7) + 1.2, cls='vis2', fill='#ffffff')
    for (px_, py_) in ((rr - 7, rr - 7), (-rr + 7, -rr + 7)):
        sh.circ(Xr(px_), Yr(py_), vr.L(1.7) + 1.8, cls='vis2', fill='#3a3f47')
    sh.centre(Xr(-rr - 10), Yr(0), Xr(rr + 10), Yr(0))
    sh.centre(Xr(0), Yr(rr + 10), Xr(0), Yr(-rr - 10))
    sh.vdim(Yr(HALF), Yr(-HALF), Xr(HALF), Xr(HALF), Xr(rr) + 22, '250', st='P', side='r')
    sh.hdim(Xr(-rr), Xr(rr), Yr(rr) - 4, Yr(rr) - 4, Yr(rr) - 24, 'TBD', st='T')
    sh.flow(Xr(rr) + 30, Yr(-rr) + 6, d='d', label=None)
    sh.text(1345, Yr(-rr) + 34, 'VIEW R — FLANGE FACE, SETTLING CHAMBER', cls='vt', anchor='middle')
    sh.line(1345 - 170, Yr(-rr) + 38, 1345 + 170, Yr(-rr) + 38, cls='vtu')
    sh.text(1345, Yr(-rr) + 55, 'Bolt count and pitch TBD (drawn 12); two pins at opposite corners (filled)', cls='vs', anchor='middle')
    B(sh, 97, Xr(-rr + 7), Yr(0), 1160, 250, side='l', name='M3 screw (12 shown)')
    B(sh, 98, Xr(-rr + 7), Yr(-rr + 7), 1160, 380, side='l', name='Alignment pin')

    vs = View(270, 790, 1.6)
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
    sh.text(Xs(0), 905, 'VIEW S — PRINTED FOOT AND PAD (SHAPE NTS)', cls='vt', anchor='middle')
    sh.line(Xs(0) - 170, 909, Xs(0) + 170, 909, cls='vtu')
    sh.text(Xs(0), 926, 'Foot size TBD; heights set so the balance box clears the bench', cls='vs', anchor='middle')
    B(sh, 99, Xs(20), Ys(-20), Xs(60), Ys(-10), side='r')
    B(sh, 100, Xs(15), Ys(-38), Xs(60), Ys(-34), side='r')

    tx, ty = 620, 700
    sh.text(tx, ty, 'FASTENER AND JOINT SCHEDULE', cls='kh')
    rows = [('95', 'Bolted flange', 'Printed on each segment end; width, thickness TBD'),
            ('96', 'Heat-set insert', 'M3 brass; pack of 100'),
            ('97', 'M3 screw', 'Stainless; M4 alternative'),
            ('73', 'Short M3 screw', 'Stainless; load cell, mount and stops'),
            ('98', 'Alignment pin and hole', 'Pins or dowels (D-005); size TBD'),
            ('46', 'Foam gasket tape', '≈3.2 thick × 6.4–9.5 wide, closed-cell'),
            ('99', 'Printed foot', 'Height TBD; no plywood base'),
            ('100', 'Rubber pad', 'Stick-on feet from the 20-pack (7)')]
    for i, (n_, a_, b_) in enumerate(rows):
        yy = ty + 24 + i * 22
        sh.circ(tx + 12, yy - 4, 11, cls='bal')
        sh.text(tx + 12, yy, n_, cls='bnum', anchor='middle', size=10 if len(n_) > 2 else 12)
        sh.text(tx + 32, yy, a_, cls='tblc', weight=700)
        sh.text(tx + 200, yy, b_, cls='tblc')
        sh.line(tx, yy + 8, tx + 520, yy + 8, cls='thin', extra='stroke-opacity="0.22"')
    return sh
