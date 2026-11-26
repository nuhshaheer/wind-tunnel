"""Sheet 2: general arrangement plan, exit end view and joint schedule."""
from wtsheets import *


def sheet_ga2():
    sh = Sheet(2, 'WT-00-2', 'GENERAL ARRANGEMENT — PLAN, EXIT VIEW, JOINTS', '', 'NTS',
               ['Plan from above. Off-tunnel items are schematic: Arduino box beside the contraction, BME280 on the fan stand (cad/sizing/supports.md).',
                'Keep each I²C run (SDP810, BME280) under about 1 m: this limits where the Arduino box can go.',
                'S and E: four taps, one per wall, in fixed walls. M: one tap in each side wall at the ball, 12 above the floor (D-024).',
                'Top panel 80–235 lifts off; one clear window on the camera side (near), black printed wall opposite (D-024).',
                'Load-cell box (sealed, D-028) and feet hidden under the tunnel (dashed). Force runs: S → High, E → Low.',
                'Joint schedule lists every connection; flanges, bolt patterns and screws on sheet 10 and in cad/sizing/flanges.md.'])
    v = View(88, 330, 0.95)
    X, Y = v.X, v.Y
    cr = P['collar_D'] / 2
    h = P['ts'] / 2
    # guard and fan (top view)
    sh.rect(X(-14), Y(cr + 6), v.L(8), v.L(2 * cr + 12), cls='vis2')
    sh.rect(X(0), Y(cr), v.L(P['collar_L']), v.L(2 * cr), cls='vis2')
    sh.rect(X(P['collar_L']), Y(P['fan_W'] / 2), v.L(P['fan_L'] - 2 * P['collar_L']), v.L(P['fan_W']), cls='vis', rx=14)
    sh.rect(X(P['fan_L'] - P['collar_L']), Y(cr), v.L(P['collar_L'] - P['sock_depth']), v.L(2 * cr), cls='vis2')
    sh.rect(X(70), Y(95), v.L(180), v.L(190), cls='hid')
    # socket and duct outline
    sh.rect(X(SOCK0), Y(RS + P['sock_wall']), v.L(P['sock_depth']), v.L(2 * (RS + P['sock_wall'])), cls='vis2')
    for xa, xb in ((D0, D1), (D1, C0), (C0, C1)):
        for s_ in (1, -1):
            pts = [v.P(xa + (xb - xa) * i / 60, s_ * (r_in(xa + (xb - xa) * i / 60) + T)) for i in range(61)]
            sh.pl(pts, cls='vis')
    for xj in JOINTS:
        r = r_in(xj - 0.01) if xj != D0 else RS
        r2 = r_in(xj + 0.01) if xj != C1 else h
        rr = max(r, r2) + T + P['fl_w']
        x0 = xj - P['fl_t']
        x1 = xj + (P['fl_t'] if xj != C1 else 0)
        sh.rect(X(x0), Y(rr), v.L(x1 - x0), v.L(2 * rr), cls='vis2', fill='#ffffff')
        sh.line(X(xj), Y(rr), X(xj), Y(-rr), cls='thin')
    # test section from above
    sh.rect(X(C1), Y(h + 12), v.L(P['ts_L']), v.L(2 * (h + 12)), cls='vis')
    sh.rect(X(C1 + 12), Y(h + 10), v.L(P['ts_L'] - 24), v.L(2 * (h + 10)), cls='vis2')
    sh.rect(X(C1 + 80), Y(h + 3), v.L(155), v.L(2 * h + 6), cls='fill-acr')
    sh.circ(X(XM), Y(0), v.L(P['ball34'] / 2), cls='vis2', fill='#f4f4f2')
    sh.path(f'M{f(X(XM-7.5))},{f(Y(0))} Q{f(X(XM-7.5))},{f(Y(3.75))} {f(X(XM))},{f(Y(3.75))} L{f(X(XM+15))},{f(Y(0))} '
            f'L{f(X(XM))},{f(Y(-3.75))} Q{f(X(XM-7.5))},{f(Y(-3.75))} {f(X(XM-7.5))},{f(Y(0))} Z', cls='hid')
    for mx, my in ((C1 + 86, h + 6), (C1 + 229, h + 6), (C1 + 86, -h - 6), (C1 + 229, -h - 6)):
        sh.circ(X(mx), Y(my), v.L(4), cls='vis2', fill='#3a3f47')
    sh.rect(X(XM - 50), Y(45), v.L(100), v.L(90), cls='hid')
    # mist port and taps
    sh.circ(X(XMIST), Y(0), v.L(10), cls='vis2', fill='#ffffff')
    sh.circ(X(XMIST), Y(0), v.L(8), cls='thin')
    sh.circ(X(XS_TAP), Y(0), v.L(1.6), cls='vis2', fill='url(#hBr)')
    for xt, yo in ((XS_TAP, HALF + T), (XE, h + 12), (XM, h + 12)):
        for s_ in (1, -1):
            y0, y1 = s_ * yo, s_ * (yo + 12)
            sh.rect(X(xt) - 1.6, Y(max(y0, y1)), 3.2, v.L(12), cls='vis2', fill='url(#hBr)')
    for fx in FEET:
        sh.rect(X(fx - 10), Y(60), v.L(20), v.L(120), cls='hid')
    sh.centre(X(-40), Y(0), X(T1 + 30), Y(0))
    sh.flow(X(C0 + 40), Y(-90), 60)
    sh.flow(X(C1 + 30), Y(-24), 56)

    # off-tunnel equipment, near side (schematic)
    ctrl = (120, -168, 70, 34)
    sh.rect(X(ctrl[0]), Y(ctrl[1]), v.L(ctrl[2]), v.L(ctrl[3]), cls='vis2', fill='#eef0f3')
    sh.path(f'M{f(X(160))},{f(Y(-P["fan_W"] / 2))} C{f(X(160))},{f(Y(-130))} {f(X(155))},{f(Y(-150))} {f(X(155))},{f(Y(-168))}', cls='thin')
    sh.rect(X(-34), Y(-160), v.L(25), v.L(18), cls='fill-pcb')
    ard = (600, -185, 150, 80)
    sh.rect(X(ard[0]), Y(ard[1]), v.L(ard[2]), v.L(ard[3]), cls='vis2', fill='#ffffff')
    sh.rect(X(ard[0] + 18), Y(ard[1] - 12), v.L(105), v.L(55), cls='fill-pcb')
    sdp = (1000, -175, 29, 18)
    sh.rect(X(sdp[0] - 6), Y(sdp[1] + 5), v.L(41), v.L(28), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(sdp[0]), Y(sdp[1]), v.L(sdp[2]), v.L(sdp[3]), cls='vis2', fill='#e8eaee')
    sh.path(f'M{f(X(-21))},{f(Y(-178))} C{f(X(-21))},{f(Y(-240))} {f(X(400))},{f(Y(-250))} {f(X(600))},{f(Y(-235))}', cls='cable')
    sh.path(f'M{f(X(1014))},{f(Y(-193))} C{f(X(1000))},{f(Y(-240))} {f(X(850))},{f(Y(-240))} {f(X(750))},{f(Y(-235))}', cls='cable')
    sh.path(f'M{f(X(XM))},{f(Y(-45))} C{f(X(XM))},{f(Y(-260))} {f(X(900))},{f(Y(-262))} {f(X(750))},{f(Y(-250))}', cls='cable')
    sh.path(f'M{f(X(675))},{f(Y(-265))} L{f(X(675))},{f(Y(-292))}', cls='cable')
    sh.text(X(675) + 6, Y(-292) + 4, 'USB → LAPTOP', cls='sm', anchor='start')
    sh.path(f'M{f(X(XS_TAP))},{f(Y(-HALF - T - 12))} C{f(X(XS_TAP))},{f(Y(-170))} {f(X(960))},{f(Y(-150))} {f(X(1004))},{f(Y(-175))}', cls='tube')
    sh.path(f'M{f(X(XE))},{f(Y(-h - 24))} C{f(X(XE))},{f(Y(-130))} {f(X(1040))},{f(Y(-130))} {f(X(1024))},{f(Y(-175))}', cls='tube')

    # callouts, far side
    R1, R2 = 78, 128
    B(sh, 8, X(-10), Y(80), 60, R2)
    B(sh, 1, X(150), Y(P['fan_W'] / 2), 175, R1)
    B(sh, 10, X(SOCK0 + 10), Y(RS + P['sock_wall']), 300, R2)
    B(sh, 11, X(D0 + 110), Y(r_in(D0 + 110) + T), 430, R1)
    B(sh, 20, X(620), Y(HALF + T), 600, R2)
    B(sh, 24, X(XMIST), Y(10), 760, R1)
    B(sh, 23, X(XS_TAP), Y(HALF + T + 12), 860, R2)
    B(sh, 30, X(C0 + 150), Y(r_in(C0 + 150) + T), 1010, R1)
    B(sh, 42, X(C1 + 120), Y(30), 1150, R1)
    B(sh, 60, X(XM) + 4, Y(4), 1230, R2)
    B(sh, 45, X(C1 + 229), Y(h + 6) - 3, 1380, R2, suffix=' (4 per panel shown)')

    # callouts, near side
    Q1, Q2 = 618, 660
    B(sh, 89, X(-21), Y(-178), 60, Q1)
    B(sh, 2, X(150), Y(-202), 200, Q2)
    B(sh, 92, X(400), Y(-245), 350, Q1)
    B(sh, 91, X(ard[0]), Y(-230), 520, Q1)
    B(sh, 90, X(ard[0] + 60), Y(ard[1] - 50), 640, Q2)
    B(sh, 93, X(675) + 1, Y(-285), 780, Q2)
    B(sh, 83, X(950), Y(-158), 900, Q1)
    B(sh, 87, X(1014), Y(-193), 1020, Q2)
    B(sh, 88, X(1035), Y(-178), 1150, Q1)
    B(sh, 48, X(XE), Y(-h - 24), 1290, Q2, name='Wall pressure-tap\nstation E')
    B(sh, 71, X(XM + 45), Y(-30), 1440, Q1)
    B(sh, 49, X(XM), Y(-h - 24), 1440, Q2, name='Wall pressure-tap\nstation M')
    sh.vtitle(X(650), 716, 'PLAN — TOP VIEW', 'Top window shown clear; sphere, shield and load-cell box seen through it')

    # joint schedule
    jx, jy = 40, 762
    sh.text(jx, jy, 'JOINT SCHEDULE — HOW EACH SECTION CONNECTS TO THE NEXT', cls='kh')
    cols = [0, 40, 270, 520, 760, 920]
    for c, hd in zip(cols, ['JOINT', 'BETWEEN', 'CONNECTION', 'FASTENERS AND SEAL', 'ALIGNMENT', 'DETAIL']):
        sh.text(jx + c, jy + 22, hd, cls='tblh')
    sh.line(jx, jy + 28, jx + 1000, jy + 28, cls='thin')
    rows = [('J1', 'Fan collar 3 → inlet ring 10', 'Slide fit; fan on its own stand', 'Neoprene wrap 4; duct tape 5', 'Snug fit (coupon C7)', 'Sh 3'),
            ('J2', 'Screen joints (5)', 'Flanges clamp frame 13 (12a–12e)', 'M3 × 16 into inserts 96; tape 46', 'Bolts', 'Sh 4, 5, 10'),
            ('J3', 'Chamber 20 → contraction 30', 'J250, 12 bolts', 'M3 × 12; tape 46', 'Bolts; straightedge', 'Sh 5, 6'),
            ('J4', 'Contraction ring → one-piece part (x = 82)', 'J220, 12 bolts', 'M3 × 12; tape 46', 'Bolts', 'Sh 6, 10'),
            ('J5', 'Contraction 30 → test section 40', 'J100, 8 bolts; step down only', 'M3 × 12; tape 46', '2 pins 98', 'Sh 6, 7'),
            ('J6', 'Front body → extension (x = 245)', 'J100, 8 bolts', 'M3 × 12; tape 46', 'Bolts', 'Sh 7'),
            ('J7', 'Top panel 42 / image panel 55 → body 40', 'Lift-off', 'Magnets 45; tape 46', 'Lips 47', 'Sh 7, 8'),
            ('J8', 'Load-cell box 71 → floor 41; door', 'Bolted, sealed (D-028)', '4 M3; tape; door magnets', 'Bosses', 'Sh 8'),
            ('J9', 'Joints → bench', 'Cradles 99 (not bolted)', 'Bumper pads 100', 'Lips', 'Sh 10'),
            ('J10', 'Test section → room', 'Open exit 52 (D-007)', '—', '—', 'Sh 7')]
    for i, row in enumerate(rows):
        yy = jy + 44 + i * 18.6
        for c, cell in zip(cols, row):
            sh.text(jx + c, yy, cell, cls='tblc', weight=700 if c == 0 else None)
        sh.line(jx, yy + 6, jx + 1000, yy + 6, cls='thin', extra='stroke-opacity="0.22"')

    # exit end view (looking upstream)
    ve = View(1345, 805, 0.62)
    Xe, Ye = ve.X, ve.Y
    rr = HALF + T + P['fl_w']
    sh.rect(Xe(-rr), Ye(rr), ve.L(2 * rr), ve.L(2 * rr), cls='vis2')
    sh.rect(Xe(-HALF), Ye(HALF), ve.L(2 * HALF), ve.L(2 * HALF), cls='hid')
    sh.rect(Xe(-h - 12), Ye(h + 12), ve.L(2 * h + 24), ve.L(2 * h + 24), cls='vis', fill='#ffffff')
    sh.rect(Xe(-h), Ye(h), ve.L(2 * h), ve.L(2 * h), cls='vis2', fill='#ffffff')
    sh.rect(Xe(-h - 6), Ye(h + 12), ve.L(2 * h + 12), ve.L(12 - P['acr_t']), cls='vis2', fill='url(#hPLA)')
    sh.circ(Xe(0), Ye(0), ve.L(P['ball34'] / 2), cls='vis2', fill='#f4f4f2')
    sh.rect(Xe(-3.75), Ye(-P['ball34'] / 2 - 5), ve.L(7.5), ve.L(50 - P['ball34'] / 2 - 5), cls='vis2', fill='#ffffff')
    sh.rect(Xe(-45), Ye(-h - 6), ve.L(90), ve.L(145 - h - 6), cls='vis2')
    for fx in (-60, 40):
        sh.rect(Xe(fx), Ye(-h - 12), ve.L(20), ve.L(170 - h - 12), cls='hid')
    sh.line(Xe(-rr - 20), Ye(-175), Xe(rr + 20), Ye(-175), cls='vis2')
    sh.centre(Xe(-rr - 15), Ye(0), Xe(rr + 15), Ye(0))
    sh.centre(Xe(0), Ye(rr + 15), Xe(0), Ye(-180))
    sh.hdim(Xe(-h), Xe(h), Ye(h + 12) - 4, Ye(h + 12) - 4, Ye(rr) - 14, '100', st='F')
    sh.vdim(Ye(h), Ye(-h), Xe(-h), Xe(-h), Xe(-rr) - 14, '100', st='F', side='l')
    sh.vdim(Ye(HALF), Ye(-HALF), Xe(HALF), Xe(HALF), Xe(rr) + 16, '250', st='F', side='r')
    sh.flow(1240, 936, d='d', label='FLOW: AWAY FROM VIEWER')
    sh.vtitle(1345, 960, 'VIEW A — EXIT END', 'Looking upstream')
    return sh
