"""Sheets 3-6: fan and joint, diffuser, settling chamber, contraction."""
from wtsheets import *


def wall_section(sh, v, xa, xb, top=True, fill='url(#hPLA)', n=60):
    sh.pl(wall_poly(v, xa, xb, top, n=n), cls='vis2', close=True, fill=fill)


def flange_pair(sh, v, xj, r_left, r_right, both=True, frame=False, fill='url(#hPLA)', gasket=True):
    """Bolted flange joint seen in side section (top and bottom). Optional screen frame between flanges."""
    ft, fw = P['fl_t'], P['fl_w']
    rr = max(r_left, r_right) + T + fw
    gap = 0
    if frame:
        gap = 4
    for s_ in (1, -1):
        # left flange
        y1, y2 = s_ * (r_left + T), s_ * rr
        sh.rect(v.X(xj - ft - gap / 2), v.Y(max(y1, y2)), v.L(ft), v.L(abs(y2 - y1)), cls='vis2', fill=fill)
        if both:
            y1, y2 = s_ * (r_right + T), s_ * rr
            sh.rect(v.X(xj + gap / 2), v.Y(max(y1, y2)), v.L(ft), v.L(abs(y2 - y1)), cls='vis2', fill=fill)
        if frame:
            ri = min(r_left, r_right)
            y1, y2 = s_ * ri, s_ * (rr - 2)
            sh.rect(v.X(xj - gap / 2), v.Y(max(y1, y2)), v.L(gap), v.L(abs(y2 - y1)), cls='vis2', fill='url(#hPETG)')
        # bolt (hidden) through the flanges
        yb = s_ * (rr - fw / 2)
        sh.line(v.X(xj - ft - gap / 2 - 1), v.Y(yb), v.X(xj + gap / 2 + (ft if both else 0) + 1), v.Y(yb), cls='hid')
    if frame:
        ri = min(r_left, r_right)
        sh.line(v.X(xj), v.Y(ri), v.X(xj), v.Y(-ri), cls='scr')


# =====================================================================================
def sheet_fan():
    sh = Sheet(3, 'WT-01', 'FAN, STAND AND FAN-TO-TUNNEL JOINT', '', 'NTS',
               ['The fan never touches the print: every contact at the joint is neoprene on plastic (buy list §1).',
                'Fan model open (D-011). Body drawn as the S6 envelope; all fan dimensions TBD until it is chosen.',
                'Measure the outlet collar on arrival (paper strip ÷ π) before printing the socket; print a 10 mm test ring first.',
                'The stand carries the fan; the tunnel does not hold it. Leaks here blow outwards, upstream of all conditioning.',
                'Turn the controller down before switching on: it restarts at its last speed. Mains never goes to the Arduino.',
                'Screen 12a, frame 13 and flange 95 at joint J2 are detailed on sheets 4 and 10.'])
    v = View(150, 432, 1.45)
    X, Y = v.X, v.Y
    cr = P['collar_D'] / 2
    # fan
    sh.rect(X(0), Y(cr), v.L(P['collar_L']), v.L(2 * cr), cls='vis2')
    sh.rect(X(P['collar_L']), Y(P['fan_H'] / 2), v.L(P['fan_L'] - 2 * P['collar_L']), v.L(P['fan_H']), cls='vis', rx=18)
    sh.rect(X(P['fan_L'] - P['collar_L']), Y(cr), v.L(P['collar_L'] - P['sock_depth']), v.L(2 * cr), cls='vis2')
    sh.rect(X(SOCK0), Y(cr), v.L(P['sock_depth'] - 2), v.L(2 * cr), cls='hid')
    for xx in (110, 210):
        sh.line(X(xx), Y(P['fan_H'] / 2), X(xx), Y(-P['fan_H'] / 2), cls='thin')
    sh.text(X(160), Y(8), 'FAN BODY', cls='sm', anchor='middle')
    sh.text(X(160), Y(-8), 'MODEL TBD (D-011)', cls='sm', anchor='middle', color=TBD)
    # guard
    sh.rect(X(-14), Y(cr + 6), v.L(8), v.L(2 * cr + 12), cls='vis2')
    for k in range(-5, 6):
        sh.line(X(-14), Y(k * 13), X(-6), Y(k * 13), cls='thin')
    # stand and feet
    sh.rect(X(70), Y(-P['fan_H'] / 2 + 6), v.L(180), v.L(150 - P['fan_H'] / 2 + 6), cls='vis2')
    sh.path(f'M{f(X(70))},{f(Y(-P["fan_H"]/2+6))} L{f(X(250))},{f(Y(-P["fan_H"]/2+6))}', cls='vis2')
    for fx in (80, 218):
        sh.rect(X(fx), Y(-150), v.L(22), v.L(25), cls='fill-neo')
    # socket section with neoprene, and the start of the diffuser
    for s_ in (1, -1):
        yt = s_ * (RS + P['sock_wall']) if s_ > 0 else -RS
        sh.rect(X(SOCK0), Y(yt), v.L(P['sock_depth']), v.L(P['sock_wall']), cls='vis2', fill='url(#hPLA)')
        yo = cr + P['wrap_t'] if s_ > 0 else -cr
        sh.rect(X(SOCK0 - 2), Y(yo), v.L(P['sock_depth']), v.L(P['wrap_t']), cls='fill-neo')
    for top in (True, False):
        sh.pl(wall_poly(v, D0, D0 + 45, top, n=20), cls='vis2', close=True, fill='url(#hPLA)')
    flange_pair(sh, v, D0, RS, r_in(D0 + 0.1), frame=True)
    sh.breakline(X(D0 + 45), Y(r_in(D0 + 45) + T + 4), Y(-r_in(D0 + 45) - T - 4))
    # controller
    cx0, cy0 = 300, -140
    sh.rect(X(cx0), Y(cy0), v.L(60), v.L(35), cls='vis2', fill='#eef0f3')
    sh.circ(X(cx0 + 30), Y(cy0 - 17), v.L(8), cls='thin')
    sh.path(f'M{f(X(230))},{f(Y(-P["fan_H"]/2))} C{f(X(240))},{f(Y(-125))} {f(X(290))},{f(Y(-122))} {f(X(cx0))},{f(Y(cy0-10))}', cls='thin')
    # bench and centre line
    sh.line(X(-40), Y(-175), X(D0 + 70), Y(-175), cls='vis2')
    xx = X(-40)
    while xx < X(D0 + 70) - 8:
        sh.line(xx, Y(-175), xx + 8, Y(-175) + 8, cls='thin')
        xx += 16
    sh.centre(X(-40), Y(0), X(D0 + 70), Y(0))
    sh.flow(X(60), Y(40), 60)
    # dimensions
    sh.vdim(Y(cr), Y(-cr), X(0), X(0), X(-40), 'Ø TBD\n(measure)', st='T', side='l')
    sh.hdim(X(SOCK0), X(D0), Y(RS + P['sock_wall']) - 4, Y(RS + P['sock_wall']) - 4, Y(132), '25–30', st='P', tx=X(D0) + 26, ty=Y(132) - 6)
    sh.hdim(X(P['fan_L'] - P['collar_L']), X(SOCK0), Y(cr) - 4, Y(RS + P['sock_wall']) - 4, Y(116), 'gap TBD (> 0)', st='T', tx=X(232), ty=Y(116) - 6)
    sh.hdim(X(0), X(P['fan_L']), Y(-175) + 4, Y(-175) + 4, Y(-175) + 46, 'TBD  (S6: 320 overall)', st='T')
    sh.vdim(Y(0), Y(-175), X(D0 + 20), X(D0 + 20), X(D0 + 60), 'TBD', st='T', side='r')
    sh.vdim(Y(-150), Y(-175), X(80), X(80), X(55), '≈20–25', st='P', side='l')
    sh.detail_circle(X(D0 - 12), Y(RS + 2), 44, 'B')
    sh.vtitle(X(150), Y(-175) + 92, 'VIEW A — SIDE ELEVATION', 'Socket and diffuser start in section · fan, stand, controller outside view')
    # callouts view A
    B(sh, 8, X(-10), Y(60), 70, 150)
    B(sh, 1, X(150), Y(P['fan_H'] / 2), 210, 105)
    B(sh, 3, X(P['fan_L'] - P['collar_L'] + 3), Y(cr), 330, 150)
    B(sh, 6, X(160), Y(-140), 70, 720)
    B(sh, 7, X(91), Y(-160), 70, 770)
    B(sh, 2, X(cx0 + 40), Y(cy0), X(cx0 + 40) + 40, 720)
    B(sh, 11, X(D0 + 30), Y(r_in(D0 + 30) + T), 640, 105)

    # ---------- detail B, collar joint, 8:1 ----------
    s8 = 8.0
    vb = View(820 - s8 * (SOCK0 - 14), 520 + s8 * 70, s8)
    Xb, Yb = vb.X, vb.Y
    x_a, x_b = SOCK0 - 14, D0 + 14
    # collar wall (thickness unknown, drawn 1 mm)
    sh.rect(Xb(x_a), Yb(cr), vb.L(D0 - 2 - x_a), vb.L(1), cls='vis2', fill='#c9ccd2')
    # neoprene
    sh.rect(Xb(SOCK0 - 2), Yb(cr + P['wrap_t']), vb.L(P['sock_depth']), vb.L(P['wrap_t']), cls='fill-neo')
    # socket wall
    sh.rect(Xb(SOCK0), Yb(RS + P['sock_wall']), vb.L(P['sock_depth']), vb.L(P['sock_wall']), cls='vis2', fill='url(#hPLA)')
    # flanges and frame at J2
    ft, fw = P['fl_t'], P['fl_w']
    top_r = RS + T + fw
    sh.rect(Xb(D0 - ft - 2), Yb(top_r), vb.L(ft), vb.L(top_r - RS - P['sock_wall']), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xb(D0 - 2), Yb(top_r - 2), vb.L(4), vb.L(top_r - 2 - RS), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xb(D0 + 2), Yb(top_r), vb.L(ft), vb.L(top_r - RS), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xb(D0 + 2 + ft), Yb(RS + T), vb.L(x_b - D0 - 2 - ft), vb.L(T), cls='vis2', fill='url(#hPLA)')
    sh.line(Xb(D0), Yb(RS), Xb(D0), Yb(RS - 6), cls='scr')
    # duct tape: over the collar, the socket face and along the socket outside
    tp = f'M{f(Xb(x_a+2))},{f(Yb(cr+0.35))} L{f(Xb(SOCK0-3))},{f(Yb(cr+0.35))} L{f(Xb(SOCK0-0.4))},{f(Yb(RS+P["sock_wall"]+0.4))} L{f(Xb(SOCK0+14))},{f(Yb(RS+P["sock_wall"]+0.4))}'
    sh.path(tp, cls='vis', extra='style="stroke:#555b66;stroke-width:3.2"')
    # break lines
    sh.breakline(Xb(x_a), Yb(cr + 4), Yb(cr - 4))
    sh.centre(Xb(x_a), Yb(RS - 4.5), Xb(x_b), Yb(RS - 4.5))
    sh.text(Xb(x_b) + 4, Yb(RS - 4.5) + 4, '(toward centre line)', cls='sm', anchor='start', size=11)
    # dims
    sh.hdim(Xb(SOCK0), Xb(D0 - 2), Yb(top_r) - 4, Yb(top_r) - 4, Yb(top_r) - 30, '25–30', st='P')
    sh.vdim(Yb(cr + P['wrap_t']), Yb(cr), Xb(SOCK0 - 2), Xb(SOCK0 - 2), Xb(SOCK0 - 14), '1.6', st='F', side='l', ty=Yb(cr) - 2)
    sh.lnote(Xb(SOCK0 + 18), Yb(RS) + 1, Xb(SOCK0 + 4), Yb(RS) + 46, 'clearance ≈0.25 per side', st='P')
    sh.vdim(Yb(RS + P['sock_wall']), Yb(RS), Xb(SOCK0 + 20), Xb(SOCK0 + 20), Xb(SOCK0 + 20) + 0.1, '', st='T', ext=False)
    sh.bgtext(Xb(SOCK0 + 21) + 4, Yb(RS + 2) + 4, 't TBD', st='T', anchor='start')
    sh.lnote(Xb(D0 - 2.5), Yb(cr + 0.5), Xb(D0 - 9), Yb(cr - 6), 'end gap TBD', st='T', anchor='end')
    sh.vtitle(Xb((x_a + x_b) / 2), Yb(cr - 10) + 16, 'DETAIL B — COLLAR IN SOCKET (8:1)', 'Upper wall only, section on centre line')
    B(sh, 4, Xb(SOCK0 + 8), Yb(cr + 0.8), Xb(SOCK0 + 2), Yb(top_r) - 66)
    B(sh, 5, Xb(SOCK0 - 6), Yb(cr + 0.4), Xb(x_a) - 6, Yb(top_r) - 66, side='r')
    B(sh, 10, Xb(SOCK0 + 12), Yb(RS + 2), Xb(SOCK0 + 16), Yb(top_r) - 66)
    B(sh, 95, Xb(D0 - 5), Yb(top_r - 4), Xb(D0 + 2) + 40, Yb(top_r) - 66, name='Bolted flange (J2)')
    B(sh, 13, Xb(D0), Yb(top_r - 6), Xb(x_b) + 20, Yb(top_r - 4), name='Screen frame')
    B(sh, 12, Xb(D0), Yb(RS - 3), Xb(x_b) + 20, Yb(RS - 3) + 14, name='Screen 12a (diffuser inlet)')
    B(sh, 3, Xb(x_a + 10), Yb(cr - 0.5), Xb(x_a + 4), Yb(cr - 10) - 20, side='r', name='Fan outlet collar (wall t unknown)')

    # ---------- socket sizing box ----------
    bx, by = 820, 640
    sh.rect(bx, by, 740, 104, cls='thin')
    sh.text(bx + 12, by + 22, 'SOCKET INSIDE DIAMETER (ITEM 10) — owner’s design, 2026-11-08', cls='kh')
    sh.text(bx + 12, by + 46, 'ID  =  D_collar  +  2 × 1.6 (neoprene)  +  ≈0.5 (print clearance)', cls='dim p', size=14)
    sh.text(bx + 12, by + 68, 'Example: D_collar = 150 → ID ≈ 153.7 mm (6.05 in). Owner’s first figure: 6.25 in (158.75 mm).', cls='lbl')
    sh.text(bx + 12, by + 88, 'Depth 25–30. Step loss at 13 m/s: < 0.1 Pa at 153.7, ≈0.4 Pa at 158.75 (buy list §1; our arithmetic).', cls='lbl')

    # ---------- fan candidates table ----------
    tx, ty = 820, 770
    sh.text(tx, ty, 'FAN CANDIDATES (D-011, owner to choose) — published figures, not measured', cls='kh')
    cols = [0, 170, 450]
    for c, hd in zip(cols, ['', 'AC INFINITY CLOUDLINE S6 (AI-CLS6)', 'VEVOR VV-GDFJ-AC6']):
        sh.text(tx + c, ty + 20, hd, cls='tblh')
    rows = [('Price seen', '$99.00 (maker, 2026-11-08)', '$53.90 (owner, 2026-11-09)'),
            ('Flow / max static pressure', '425 CFM / 503 Pa (maker)', '400 CFM / 300 Pa (seller)'),
            ('Motor and control', 'EC, PWM; 10 speed levels', 'AC, 60 W; variable controller'),
            ('Size', '7.87 × 12.60 × 8.35 in (200 × 320 × 212)', '306 × 255 × 212 (axis order not stated)'),
            ('Mounting', 'holes 80 × 60 mm, Ø6', 'not published'),
            ('Est. top speed (5 screens)', '≈13.0–13.4 m/s', '≈11.3 m/s'),
            ('Collar diameter', 'not published — measure', 'not published — measure')]
    for i, row in enumerate(rows):
        yy = ty + 38 + i * 18.5
        for c, cell in zip(cols, row):
            sh.text(tx + c, yy, cell, cls='tblc', weight=700 if c == 0 else None)
        sh.line(tx, yy + 6, tx + 740, yy + 6, cls='thin', extra='stroke-opacity="0.22"')
    return sh


# =====================================================================================
def sheet_diffuser():
    sh = Sheet(4, 'WT-02', 'WIDE-ANGLE DIFFUSER (FAN OUTLET → SETTLING CHAMBER)', '', 'NTS',
               ['Mehta1977 Fig. 5: area ratio 3.44 needs screens with K_sum ≥ 2.1. Two screens allow about 115 mm minimum.',
                'Wall form TBD: curved (bell) walls, or straight walls with radiused ends, since 2θ exceeds 24° below about 220 mm.',
                'Fillet the four corners (radius TBD): across the diagonal the expansion is about twice as steep as across the flats.',
                'No honeycomb or flow straightener at the fan outlet: the fan’s swirl helps keep the diffuser flow attached.',
                'Screen 12b only if the delivered wire is 0.010 in (K_sum 1.90 with two). Its joint position is TBD.',
                'Consider moving 12a slightly into the diffuser: at 1.5 × the outlet area its loss roughly halves (TBD).'])
    s = 1.75
    v = View(160 - s * (SOCK0 - 6), 440, s)
    X, Y = v.X, v.Y
    xr = D1 + 26
    # socket
    for s_ in (1, -1):
        yt = s_ * (RS + P['sock_wall']) if s_ > 0 else -RS
        sh.rect(X(SOCK0), Y(yt), v.L(P['sock_depth'] - P['fl_t'] - 2), v.L(P['sock_wall']), cls='vis2', fill='url(#hPLA)')
    flange_pair(sh, v, D0, RS, RS, frame=True)
    for top in (True, False):
        wall_section(sh, v, D0 + 2 + P['fl_t'], D1 - 2 - P['fl_t'])
        wall_section(sh, v, D0 + 2 + P['fl_t'], D1 - 2 - P['fl_t'], top=False)
        break
    flange_pair(sh, v, D1, HALF, HALF, frame=True)
    # chamber start
    for s_ in (1, -1):
        yt = s_ * (HALF + T) if s_ > 0 else -HALF
        sh.rect(X(D1 + 2 + P['fl_t']), Y(yt), v.L(xr - D1 - 2 - P['fl_t']), v.L(T), cls='vis2', fill='url(#hPLA)')
    sh.breakline(X(xr), Y(HALF + T + 6), Y(-HALF - T - 6))
    # optional 12b
    xmid = (D0 + D1) / 2
    sh.line(X(xmid), Y(r_in(xmid)), X(xmid), Y(-r_in(xmid)), cls='hid')
    # corner line (diagonal) shown hidden
    sh.centre(X(SOCK0 - 4), Y(0), X(xr + 6), Y(0))
    sh.flow(X(D0 + 50), Y(-30), 62)
    # dims
    yt_ = Y(HALF + T + P['fl_w'])
    sh.hdim(X(D0), X(D1), yt_ - 4, yt_ - 4, yt_ - 44, '150–200', st='P')
    sh.hdim(X(SOCK0), X(D0), Y(RS + P['sock_wall']) - 4, Y(RS + P['sock_wall']) - 4, yt_ - 44, '25–30', st='P', tx=X(SOCK0) - 30)
    sh.hdim(X(D0), X(xmid), Y(-r_in(xmid)) + 6, Y(-r_in(xmid)) + 6, Y(-HALF - T - P['fl_w']) + 40, 'TBD (mid-length)', st='T')
    sh.vdim(Y(HALF), Y(-HALF), X(D1), X(D1), X(xr) + 40, '250', st='P', side='r')
    sh.vdim(Y(RS), Y(-RS), X(SOCK0), X(SOCK0), X(SOCK0) - 44, 'Ø ID\n(sheet 3)', st='P', side='l')
    sh.lnote(X(D0 + 60), Y(r_in(D0 + 60) + T / 2), X(D0 + 55), Y(HALF + 30), 'wall t TBD · form TBD', st='T', anchor='middle')
    sh.lnote(X(D1 - 3), Y(HALF + T + P['fl_w'] - 4), X(D1 + 60), Y(HALF + T + P['fl_w']) - 16, 'flange TBD', st='T', anchor='start')
    sh.vtitle(X((D0 + D1) / 2), Y(-HALF - T - P['fl_w']) + 96, 'SECTION A–A — ON CENTRE LINE', 'Flow left to right; screens dashed grey, optional 12b dashed black')
    # callouts
    B(sh, 10, X(SOCK0 + 8), Y(RS + P['sock_wall']), 130, 110)
    B(sh, 12, X(D0), Y(40), 150, 160, name='Screen 12a (diffuser inlet)')
    B(sh, 95, X(D0 - 4), Y(RS + T + P['fl_w']), 300, 110)
    B(sh, 11, X(D0 + 110), Y(r_in(D0 + 110) + T), 470, 110)
    B(sh, 12, X(xmid), Y(r_in(xmid) - 20), 395, 160, name='Screen 12b (optional)')
    B(sh, 12, X(D1), Y(70), 560, 160, name='Screen 12c (diffuser exit)')
    B(sh, 13, X(D1 - 2), Y(-HALF - 6), 220, 770, name='Screen frame (each screen)')
    B(sh, 20, X(xr - 8), Y(-HALF - T), 470, 770, name='Settling-chamber shell (start)')
    B(sh, 98, X(D1 + 4), Y(-HALF - T - 8), 330, 815, name='Alignment pin and hole (sheet 10)')

    # ---------- view B, end view looking downstream from the fan ----------
    vb = View(1235, 410, 1.05)
    Xb, Yb = vb.X, vb.Y
    rr = HALF + T + P['fl_w']
    sh.rect(Xb(-rr), Yb(rr), vb.L(2 * rr), vb.L(2 * rr), cls='vis2')
    sh.rect(Xb(-HALF), Yb(HALF), vb.L(2 * HALF), vb.L(2 * HALF), cls='hid', rx=vb.L(12))
    sh.circ(Xb(0), Yb(0), vb.L(RS + P['sock_wall']), cls='vis', fill='#ffffff')
    sh.circ(Xb(0), Yb(0), vb.L(RS), cls='vis2', fill='url(#hScr)')
    for a in (45, 135, 225, 315):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        sh.line(Xb((RS + P['sock_wall']) * ca), Yb((RS + P['sock_wall']) * sa), Xb((HALF - 4) * math.copysign(1, ca)), Yb((HALF - 4) * math.copysign(1, sa)), cls='hid')
    sh.centre(Xb(-rr - 14), Yb(0), Xb(rr + 14), Yb(0))
    sh.centre(Xb(0), Yb(rr + 14), Xb(0), Yb(-rr - 14))
    sh.vdim(Yb(HALF), Yb(-HALF), Xb(HALF), Xb(HALF), Xb(rr) + 22, '250', st='P', side='r')
    sh.hdim(Xb(-rr), Xb(rr), Yb(rr) - 4, Yb(rr) - 4, Yb(rr) - 26, 'flange TBD', st='T')
    sh.lnote(Xb(-HALF + 3), Yb(HALF - 3), Xb(-rr) - 10, Yb(rr) - 40, 'corner fillet R TBD', st='T', anchor='end')
    sh.lnote(Xb(-RS * 0.7), Yb(-RS * 0.7), Xb(-rr) - 10, Yb(-rr) + 30, 'Ø socket ID\n(sheet 3)', st='P', anchor='end')
    sh.flow(Xb(rr) + 28, Yb(-rr) + 18, d='d', label='FLOW: AWAY')
    sh.vtitle(1235, Yb(-rr) + 68, 'VIEW B — FROM THE FAN SIDE', 'Looking downstream; screen 12a shaded in the socket')
    B(sh, 12, Xb(RS * 0.45), Yb(RS * 0.3), Xb(rr) + 26, Yb(rr) + 40, name='Screen 12a')

    # ---------- screen table ----------
    tx, ty = 820, 790
    sh.text(tx, ty, 'DIFFUSER SCREENS AT 13 m/s (buy list §3; Wieghardt formula, our arithmetic)', cls='kh')
    cols = [0, 95, 255, 395, 530]
    for c, hd in zip(cols, ['SCREEN', 'POSITION', 'LOCAL SPEED', 'K (0.010–0.011 in)', 'LOSS']):
        sh.text(tx + c, ty + 20, hd, cls='tblh')
    rows = [('12a', 'Diffuser inlet', '≈7.4 m/s', '0.75–0.85', '24–28 Pa'),
            ('12b', 'Middle (optional)', '≈3.7 m/s', '≈0.95', '≈8 Pa'),
            ('12c', 'Diffuser exit', '≈2.1 m/s', '1.15–1.30', '3.0–3.4 Pa'),
            ('Σ', 'Two screens (12a + 12c)', '', '1.90–2.15 (need ≥ 2.1)', '')]
    for i, row in enumerate(rows):
        yy = ty + 38 + i * 18.5
        for c, cell in zip(cols, row):
            sh.text(tx + c, yy, cell, cls='tblc', weight=700 if c == 0 else None)
        sh.line(tx, yy + 6, tx + 720, yy + 6, cls='thin', extra='stroke-opacity="0.22"')
    return sh


# =====================================================================================
def sheet_chamber():
    sh = Sheet(5, 'WT-03', 'SETTLING CHAMBER, HONEYCOMB AND SCREENS', '', 'NTS',
               ['Order in the flow: honeycomb first, then screens (Mehta1979). The last screen must be more than 57 % open.',
                'Station spacings are TBD; the two options are compared in the table. Drawn at layout values only.',
                'Joints sit at the honeycomb frame and at each screen so the frames come out for cleaning (layout only).',
                'S taps and the mist port: positions TBD, both after the last screen. Side-wall taps are seen in the far wall.',
                'The 250 mm section plus walls exceeds the 256 mm P1S bed: how each segment is split is TBD (D-005).',
                'Upgrade if the flow map shows a problem: 5 mm drinking straws, 40 mm long, in the same frame.'])
    s = 1.45
    x0 = D1 - 18
    v = View(110 - s * x0, 420, s)
    X, Y = v.X, v.Y
    xr = C0 + 26
    # walls between joints
    segs = [(D1, HC0), (HC0, SC1), (SC1, SC2), (SC2, C0)]
    for xa, xb in segs:
        for s_ in (1, -1):
            yt = s_ * (HALF + T) if s_ > 0 else -HALF
            sh.rect(X(xa + 2 + P['fl_t']), Y(yt), v.L(xb - xa - 4 - 2 * P['fl_t']), v.L(T), cls='vis2', fill='url(#hPLA)')
    # diffuser end on the left
    for s_ in (1, -1):
        yt = s_ * (HALF + T) if s_ > 0 else -HALF
        sh.rect(X(x0), Y(yt), v.L(D1 - 2 - P['fl_t'] - x0), v.L(T), cls='vis2', fill='url(#hPLA)')
    sh.breakline(X(x0), Y(HALF + T + 6), Y(-HALF - T - 6))
    flange_pair(sh, v, D1, HALF, HALF, frame=True)
    flange_pair(sh, v, HC0, HALF, HALF, frame=False)
    flange_pair(sh, v, SC1, HALF, HALF, frame=True)
    flange_pair(sh, v, SC2, HALF, HALF, frame=True)
    flange_pair(sh, v, C0, HALF, HALF, frame=False)
    # contraction start
    for top in (True, False):
        sh.pl(wall_poly(v, C0 + 2 + P['fl_t'], xr, top, n=10), cls='vis2', close=True, fill='url(#hPLAk)')
    sh.breakline(X(xr), Y(HALF + T + 6), Y(-HALF - T - 6))
    # honeycomb and its frame
    sh.rect(X(HC0 + 2), Y(HALF), v.L(P['hc_L']), v.L(2 * HALF), cls='vis2', fill='#ffffff')
    k = -HALF + 5.2
    while k < HALF:
        sh.line(X(HC0 + 2), Y(k), X(HC0 + 2 + P['hc_L']), Y(k), cls='thin')
        k += 5.2
    for s_ in (1, -1):
        sh.rect(X(HC0 + 2), Y(s_ * HALF) if s_ > 0 else Y(-HALF + 4), v.L(P['hc_L']), v.L(4), cls='vis2', fill='url(#hPETG)')
    # S taps and mist port
    for s_ in (1, -1):
        yt = HALF + T + 12 if s_ > 0 else -HALF
        sh.rect(X(XS_TAP) - 2.3, Y(yt), 4.6, v.L(12 + T), cls='vis2', fill='url(#hBr)')
    sh.circ(X(XS_TAP), Y(0), 3.5, cls='vis2', fill='url(#hBr)')
    sh.rect(X(XMIST - 8), Y(HALF + T + 20), v.L(16), v.L(20), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(XMIST - 10), Y(HALF + T + 26), v.L(20), v.L(6), cls='vis2', fill='#ffffff')
    sh.centre(X(x0 - 6), Y(0), X(xr + 8), Y(0))
    sh.flow(X(HC1 + 30), Y(-40), 62)
    sh.cutline(X(HC0 + 2 + P['hc_L'] / 2), Y(HALF + T + P['fl_w']) - 16, Y(-HALF - T - P['fl_w']) + 16, 'B')
    # dimension chain, below
    yb = Y(-HALF - T - P['fl_w'])
    yd = yb + 40
    chain = [(D1, HC0 + 2, 'TBD', 'T'), (HC0 + 2, HC1 + 2, '48–50', 'P'), (HC1 + 2, SC1, 'TBD', 'T'), (SC1, SC2, 'TBD', 'T'), (SC2, C0, '50', 'P')]
    for xa, xb, lab, st in chain:
        sh.hdim(X(xa), X(xb), yb + 4, yb + 4, yd, lab, st=st)
    sh.hdim(X(D1), X(C0), yd + 6, yd + 6, yd + 40, 'TBD (see table)', st='T')
    sh.vdim(Y(HALF), Y(-HALF), X(C0), X(C0), X(xr) + 34, '250', st='P', side='r')
    yt_ = Y(HALF + T + P['fl_w'])
    sh.hdim(X(XS_TAP), X(C0), yt_ - 4, yt_ - 4, yt_ - 40, 'TBD', st='T', tx=X(C0) + 24)
    sh.vtitle(X((D1 + C0) / 2), yd + 84, 'SECTION A–A — ON CENTRE LINE', 'Flow left to right')
    # callouts
    R1, R2 = 110, 160
    B(sh, 12, X(D1), Y(80), 120, R2, name='Screen 12c')
    B(sh, 22, X(HC0 + 20), Y(HALF - 2), 230, R1)
    B(sh, 21, X(HC0 + 30), Y(60), 250, R2)
    B(sh, 20, X(HC1 + 60), Y(HALF + T), 390, R1)
    B(sh, 95, X(SC1 - 4), Y(HALF + T + P['fl_w']), 400, R2, name='Bolted flange (joint J4)')
    B(sh, 12, X(SC1), Y(60), 570, R1, name='Screen 12d')
    B(sh, 13, X(SC2), Y(HALF + T + 4), 650, R2, name='Screen frame')
    B(sh, 12, X(SC2), Y(30), 690, R1, name='Screen 12e')
    B(sh, 24, X(XMIST), Y(HALF + T + 26), 770, R2 + 40, side='r')
    B(sh, 23, X(XS_TAP) + 3, Y(0), 850, Y(-60), name='Wall pressure-tap station S\n(4 taps; side tap in far wall)')
    B(sh, 30, X(xr - 6), Y(r_in(xr - 6) + T), 860, R1 + 10, name='Contraction shell (start)')

    # ---------- section B-B, through the honeycomb ----------
    vb = View(1235, 395, 1.05)
    Xb, Yb = vb.X, vb.Y
    rr = HALF + T + P['fl_w']
    sh.rect(Xb(-HALF - T), Yb(HALF + T), vb.L(2 * HALF + 2 * T), vb.L(2 * HALF + 2 * T), cls='vis', fill='url(#hPLA)')
    sh.rect(Xb(-HALF), Yb(HALF), vb.L(2 * HALF), vb.L(2 * HALF), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xb(-HALF + 4), Yb(HALF - 4), vb.L(2 * HALF - 8), vb.L(2 * HALF - 8), cls='vis2', fill='#ffffff')
    # hex cells in the upper-right quadrant (6 mm across flats, true scale)
    a = 6 / math.sqrt(3)  # side length for 6 mm across flats
    cells = []
    row = 0
    yc = 3.0
    while yc < HALF - 4 - 3:
        xc = 3.0 + (0 if row % 2 == 0 else 1.5 * a)
        while xc < HALF - 4 - a:
            pts = [(Xb(xc + a * math.cos(math.radians(60 * k))), Yb(yc + a * math.sin(math.radians(60 * k)))) for k in range(6)]
            cells.append(' '.join(f'{f(px)},{f(py)}' for px, py in pts))
            xc += 3 * a
        yc += 3.0
        row += 1
    for c in cells:
        sh.a(f'<polygon points="{c}" class="thin" style="stroke-width:0.45"/>')
    sh.line(Xb(0), Yb(0), Xb(0), Yb(HALF - 4), cls='thin')
    sh.line(Xb(0), Yb(0), Xb(HALF - 4), Yb(0), cls='thin')
    sh.text(Xb(-HALF / 2), Yb(HALF / 2) + 4, 'HONEYCOMB CONTINUES', cls='sm', anchor='middle')
    sh.text(Xb(-HALF / 2), Yb(HALF / 2) + 20, '(cells shown in one quadrant)', cls='sm', anchor='middle')
    sh.centre(Xb(-rr), Yb(0), Xb(rr), Yb(0))
    sh.centre(Xb(0), Yb(rr), Xb(0), Yb(-rr))
    sh.hdim(Xb(-HALF + 4), Xb(HALF - 4), Yb(HALF + T) - 4, Yb(HALF + T) - 4, Yb(HALF + T) - 26, '≈250 (P1S bed: one piece)', st='P')
    sh.vdim(Yb(HALF), Yb(-HALF), Xb(HALF + T), Xb(HALF + T), Xb(HALF + T) + 22, '250', st='P', side='r')
    sh.flow(Xb(HALF + T) + 20, Yb(-HALF) + 34, d='d', label='FLOW: AWAY')
    sh.detail_circle(Xb(HALF - 22), Yb(HALF - 22), 22, 'C')
    sh.vtitle(1235, Yb(-HALF - T) + 40, 'SECTION B–B — THROUGH THE HONEYCOMB', 'Looking downstream')
    B(sh, 22, Xb(-HALF + 2), Yb(-HALF / 2), Xb(-HALF - T) - 40, Yb(-HALF / 2) + 30, side='l')

    # ---------- detail C, cells 8:1 ----------
    vc = View(1000, 760, 8)
    Xc, Yc = vc.X, vc.Y
    for (xc, yc) in ((0, 0), (1.5 * a, 3), (3 * a, 0), (1.5 * a, -3)):
        pts = [(Xc(xc + a * math.cos(math.radians(60 * k))), Yc(yc + a * math.sin(math.radians(60 * k)))) for k in range(6)]
        pin = [(Xc(xc + (a - 0.46) * math.cos(math.radians(60 * k))), Yc(yc + (a - 0.46) * math.sin(math.radians(60 * k)))) for k in range(6)]
        sh.pl(pts, cls='vis2', close=True, fill='#c9ccd2')
        sh.pl(pin, cls='vis2', close=True, fill='#ffffff')
    sh.vdim(Yc(3), Yc(-3), Xc(0), Xc(0), Xc(-a) - 18, '6', st='P', side='l')
    sh.lnote(Xc(3 * a + a * 0.5 - 0.1), Yc(a * 0.87 - 0.2), Xc(3 * a) + 70, Yc(5), 'wall 0.4', st='P', anchor='start')
    sh.text(Xc(1.5 * a), Yc(-6.5) + 8, 'DETAIL C — CELLS (8:1)', cls='vt', anchor='middle', size=14)
    sh.text(Xc(1.5 * a), Yc(-6.5) + 26, 'hexagons 6 across flats, about 48–50 long (L/D ≈ 8); ≈87 % open', cls='vs', anchor='middle')

    # ---------- spacing options ----------
    tx, ty = 1110, 690
    sh.text(tx, ty, 'STATION SPACING — OPTIONS (decide at sizing)', cls='kh')
    rows = [('', 'A: 0.2 D (Mehta1979)', 'B: full decay'),
            ('Diffuser exit → honeycomb', 'TBD', 'TBD'),
            ('Honeycomb → 12d', '50', '≥150 (buy list);'),
            ('', '', '50 cells = 300'),
            ('12d → 12e', '50', '≥500 wire Ø = 127–140*'),
            ('12e → contraction', '50', '50'),
            ('Chamber length', '≈200 + frames', '≈380–400 + frames')]
    for i, (a_, b_, c_) in enumerate(rows):
        yy = ty + 20 + i * 18
        sh.text(tx, yy, a_, cls='tblh' if i == 0 else 'tblc', weight=700 if i else None)
        sh.text(tx + 165, yy, b_, cls='tblh' if i == 0 else 'tblc')
        sh.text(tx + 300, yy, c_, cls='tblh' if i == 0 else 'tblc')
    sh.text(tx, ty + 20 + 7 * 18 + 4, '* our arithmetic with the chosen 0.010–0.011 in screen wire; the docs’ 230–300', cls='sm')
    sh.text(tx, ty + 20 + 7 * 18 + 20, '  mm range assumed 0.15–0.25 mm wire and 2–3 mm cells.', cls='sm')
    return sh


# =====================================================================================
def sheet_contraction():
    sh = Sheet(6, 'WT-04', 'CONTRACTION (250 × 250 → 100 × 100, CR 6.25)', '', 'NTS',
               ['Wall shape: 5th-order polynomial (Bell1988), zero slope and curvature at both ends, inflection at mid-length.',
                'Each of the four walls follows the same half-width curve: a square section, outside Bell1988’s tested range.',
                'Length 250 = 1.0 × inlet (Bell1988 minimum 0.89 at c = 7.7). Contraction ratio 6.25 (Mehta1979: 6–9).',
                'Print in black PLA; sand the inside 220–600 grit. Keep internal segment joints away from the exit (D-005).',
                'Segment split TBD: the 250 inlet plus walls exceeds the 256 mm bed. Inside faces must meet with no step.',
                'Optional small 45° corner fillets (Mehta1979) must not end abruptly in the test section: TBD.'])
    s = 1.7
    x0 = C0 - 24
    v = View(110 - s * x0, 445, s)
    X, Y = v.X, v.Y
    xr = C1 + 30
    # chamber end
    for s_ in (1, -1):
        yt = s_ * (HALF + T) if s_ > 0 else -HALF
        sh.rect(X(x0), Y(yt), v.L(C0 - 2 - P['fl_t'] - x0), v.L(T), cls='vis2', fill='url(#hPLA)')
    sh.breakline(X(x0), Y(HALF + T + 6), Y(-HALF - T - 6))
    flange_pair(sh, v, C0, HALF, HALF)
    for top in (True, False):
        sh.pl(wall_poly(v, C0 + 2 + P['fl_t'], C1 - 2 - P['fl_t'], top, n=80), cls='vis2', close=True, fill='url(#hPLAk)')
    flange_pair(sh, v, C1, P['ts'] / 2, P['ts'] / 2)
    for s_ in (1, -1):
        yt = s_ * (P['ts'] / 2 + T) if s_ > 0 else -P['ts'] / 2
        sh.rect(X(C1 + 2 + P['fl_t']), Y(yt), v.L(xr - C1 - 2 - P['fl_t']), v.L(T), cls='vis2', fill='url(#hPLAk)')
    sh.breakline(X(xr), Y(P['ts'] / 2 + T + 6), Y(-P['ts'] / 2 - T - 6))
    # true profile (inner surface) and ordinates
    pts = [v.P(C0 + P['con_L'] * i / 100, contraction_half(i / 100)) for i in range(101)]
    sh.pl(pts, cls='vis')
    for i in range(11):
        xi = i / 10
        xx = C0 + P['con_L'] * xi
        sh.line(X(xx), Y(0), X(xx), Y(contraction_half(xi)), cls='thin', extra='stroke-dasharray="2 2"')
        sh.text(X(xx), Y(0) + 15, str(i), cls='sm', anchor='middle', size=11)
    sh.circ(X(C0 + 125), Y(contraction_half(0.5)), 4, cls='vis2', fill='#ffffff')
    sh.lnote(X(C0 + 125) + 2, Y(contraction_half(0.5)) + 3, X(C0 + 133), Y(28), 'inflection at x = 125 (0.5 L)', st='P', anchor='start')
    sh.centre(X(x0 - 6), Y(0), X(xr + 8), Y(0))
    sh.flow(X(C0 + 30), Y(-70), 64)
    # dims
    yt_ = Y(HALF + T + P['fl_w'])
    yb_ = Y(-HALF - T - P['fl_w'])
    sh.hdim(X(C0), X(C1), yb_ + 4, Y(-P['ts'] / 2 - T - P['fl_w']) + 4, yb_ + 40, '250', st='P')
    sh.vdim(Y(HALF), Y(-HALF), X(C0), X(C0), X(x0) - 30, '250', st='P', side='l')
    sh.vdim(Y(50), Y(-50), X(C1), X(C1), X(xr) + 30, '100', st='F', side='r')
    sh.lnote(X(C0 + 200), Y(-contraction_half(0.8) - T / 2), X(C0 + 210), Y(-HALF + 6), 'wall t TBD', st='T', anchor='start')
    sh.lnote(X(C1 + 3), Y(-P['ts'] / 2 - T - P['fl_w'] + 3), X(C1 + 40), Y(-HALF - 18), 'flange TBD', st='T', anchor='start')
    sh.vtitle(X((C0 + C1) / 2), Y(-HALF - T - P['fl_w']) + 88, 'SECTION A–A — ON CENTRE LINE', 'Dotted lines: ordinate stations 0–10 (table below)')
    # callouts
    B(sh, 20, X(x0 + 6), Y(HALF + T), 90, 80, name='Settling-chamber shell (end)')
    B(sh, 95, X(C0 - 4), Y(HALF + T + P['fl_w']), 300, 80, name='Bolted flange (joint J5)')
    B(sh, 30, X(C0 + 70), Y(contraction_half(0.28) + T), 470, 130)
    B(sh, 98, X(C1 + 4), Y(P['ts'] / 2 + T + P['fl_w'] - 3), 650, 80, name='Alignment pin and hole (J6)')
    B(sh, 40, X(xr - 8), Y(P['ts'] / 2 + T), 820, 130, name='Test-section frame (start)')

    # ordinate table
    tx, ty = 70, 840
    sh.text(tx, ty, 'WALL ORDINATES — y = 125 − 75 · (6ξ⁵ − 15ξ⁴ + 10ξ³), ξ = x / 250   (proposed; Bell1988)', cls='kh')
    sh.text(tx, ty + 24, 'Station', cls='tblh')
    sh.text(tx, ty + 44, 'x (mm)', cls='tblh')
    sh.text(tx, ty + 64, 'half-width y', cls='tblh')
    sh.text(tx, ty + 84, 'inside width 2y', cls='tblh')
    for i in range(11):
        cx = tx + 120 + i * 62
        yv = contraction_half(i / 10)
        sh.text(cx, ty + 24, str(i), cls='tblm', anchor='middle')
        sh.text(cx, ty + 44, f'{25 * i}', cls='tblm', anchor='middle')
        sh.text(cx, ty + 64, f'{yv:.2f}', cls='tblm', anchor='middle')
        sh.text(cx, ty + 84, f'{2 * yv:.1f}', cls='tblm', anchor='middle')
    for k in range(4):
        sh.line(tx, ty + 30 + 20 * k, tx + 120 + 10 * 62 + 30, ty + 30 + 20 * k, cls='thin', extra='stroke-opacity="0.22"')

    # end views
    rr = HALF + T + P['fl_w']
    ve = View(1290, 300, 0.78)
    Xe, Ye = ve.X, ve.Y
    sh.rect(Xe(-rr), Ye(rr), ve.L(2 * rr), ve.L(2 * rr), cls='vis2')
    sh.rect(Xe(-HALF), Ye(HALF), ve.L(2 * HALF), ve.L(2 * HALF), cls='vis')
    sh.rect(Xe(-50), Ye(50), ve.L(100), ve.L(100), cls='vis2')
    for sx, sy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        sh.line(Xe(sx * HALF), Ye(sy * HALF), Xe(sx * 50), Ye(sy * 50), cls='vis2')
    sh.centre(Xe(-rr - 12), Ye(0), Xe(rr + 12), Ye(0))
    sh.centre(Xe(0), Ye(rr + 12), Xe(0), Ye(-rr - 12))
    sh.vdim(Ye(HALF), Ye(-HALF), Xe(HALF), Xe(HALF), Xe(rr) + 20, '250', st='P', side='r')
    sh.hdim(Xe(-50), Xe(50), Ye(50) - 4, Ye(50) - 4, Ye(HALF) + 22, '100', st='F')
    sh.flow(Xe(-rr) - 4, Ye(-rr) - 2 + 30, d='d', label=None)
    sh.vtitle(1290, Ye(-rr) + 38, 'VIEW B — INLET END', 'Looking downstream, into the contraction')
    ve2 = View(1290, 690, 0.78)
    X2, Y2 = ve2.X, ve2.Y
    r2 = P['ts'] / 2 + T + P['fl_w']
    sh.rect(X2(-r2), Y2(r2), ve2.L(2 * r2), ve2.L(2 * r2), cls='vis2', fill='#ffffff')
    sh.rect(X2(-50), Y2(50), ve2.L(100), ve2.L(100), cls='vis')
    sh.centre(X2(-HALF - 12), Y2(0), X2(HALF + 12), Y2(0))
    sh.centre(X2(0), Y2(HALF + 12), X2(0), Y2(-HALF - 12))
    sh.vdim(Y2(50), Y2(-50), X2(50), X2(50), X2(r2) + 20, '100', st='F', side='r')
    sh.hdim(X2(-r2), X2(r2), Y2(-r2) + 4, Y2(-r2) + 4, Y2(-r2) + 26, 'flange TBD', st='T')
    sh.vtitle(1290, Y2(-HALF) + 38, 'VIEW C — EXIT END', 'Looking upstream, into the contraction exit')
    sh.flow(X2(-HALF) - 4, Y2(-HALF) + 4, d='o', label=None)
    return sh
