"""Sheets 3-5, second layout (replaces the first drafts in s_d1)."""
from wtsheets import *
from s_d1 import wall_section, flange_pair


# =====================================================================================
def sheet_fan():
    sh = Sheet(3, 'WT-01', 'FAN, STAND AND FAN-TO-TUNNEL JOINT', '', 'NTS',
               ['The fan never touches the print: every contact at the joint is neoprene on plastic (buy list §1).',
                'Fan: AC Infinity CLOUDLINE S6, model AI-CLS6 (D-025); body 200 × 320 × 212 (maker). Bought last, once the airspeed readout works.',
                'Measure the outlet collar on arrival (paper strip ÷ π) before printing the socket; print a 10 mm test ring first.',
                'The stand carries the fan; the tunnel does not hold it. Stand feet: soft bumpers about 20–25 mm (buy list §1).',
                'Turn the controller down before switching on: it restarts at its last speed. Mains never goes to the Arduino.',
                'The inlet ring (10) is its own print, bolted to the diffuser with screen 12a between (cad/sizing/diffuser.md). Socket depth 28.'])
    v = View(150, 432, 1.45)
    X, Y = v.X, v.Y
    cr = P['collar_D'] / 2
    cend = D0 - 4          # collar end, short of the screen frame (gap TBD)
    sh.rect(X(0), Y(cr), v.L(P['collar_L']), v.L(2 * cr), cls='vis2')
    sh.rect(X(P['collar_L']), Y(P['fan_H'] / 2), v.L(P['fan_L'] - 2 * P['collar_L']), v.L(P['fan_H']), cls='vis', rx=18)
    sh.rect(X(P['fan_L'] - P['collar_L']), Y(cr), v.L(SOCK0 - P['fan_L'] + P['collar_L']), v.L(2 * cr), cls='vis2')
    sh.rect(X(SOCK0), Y(cr), v.L(cend - SOCK0), v.L(2 * cr), cls='hid')
    for xx in (110, 210):
        sh.line(X(xx), Y(P['fan_H'] / 2), X(xx), Y(-P['fan_H'] / 2), cls='thin')
    sh.text(X(160), Y(8), 'FAN BODY', cls='sm', anchor='middle')
    sh.text(X(160), Y(-8), 'AC INFINITY S6 (D-025)', cls='sm', anchor='middle', color=FIX)
    sh.rect(X(-14), Y(cr + 6), v.L(8), v.L(2 * cr + 12), cls='vis2')
    for k in range(-5, 6):
        sh.line(X(-14), Y(k * 13), X(-6), Y(k * 13), cls='thin')
    sh.rect(X(70), Y(-P['fan_H'] / 2 + 6), v.L(180), v.L(150 - P['fan_H'] / 2 + 6), cls='vis2')
    for fx in (80, 218):
        sh.rect(X(fx), Y(-150), v.L(22), v.L(25), cls='fill-neo')
    for s_ in (1, -1):
        yt = s_ * (RS + P['sock_wall']) if s_ > 0 else -RS
        sh.rect(X(SOCK0), Y(yt), v.L(D0 - 2 - P['fl_t'] - SOCK0), v.L(P['sock_wall']), cls='vis2', fill='url(#hPLA)')
        yo = cr + P['wrap_t'] if s_ > 0 else -cr
        sh.rect(X(SOCK0 - 2), Y(yo), v.L(cend - SOCK0 + 2), v.L(P['wrap_t']), cls='fill-neo')
    for top in (True, False):
        sh.pl(wall_poly(v, D0 + 2 + P['fl_t'], D0 + 45, top, n=20), cls='vis2', close=True, fill='url(#hPLA)')
    flange_pair(sh, v, D0, RS, r_in(D0 + 0.1), frame=True)
    sh.breakline(X(D0 + 45), Y(r_in(D0 + 45) + T + 4), Y(-r_in(D0 + 45) - T - 4))
    cx0, cy0 = 300, -140
    sh.rect(X(cx0), Y(cy0), v.L(60), v.L(35), cls='vis2', fill='#eef0f3')
    sh.circ(X(cx0 + 30), Y(cy0 - 17), v.L(8), cls='thin')
    sh.path(f'M{f(X(230))},{f(Y(-P["fan_H"]/2))} C{f(X(240))},{f(Y(-125))} {f(X(290))},{f(Y(-122))} {f(X(cx0))},{f(Y(cy0-10))}', cls='thin')
    sh.line(X(-40), Y(-175), X(D0 + 70), Y(-175), cls='vis2')
    xx = X(-40)
    while xx < X(D0 + 70) - 8:
        sh.line(xx, Y(-175), xx + 8, Y(-175) + 8, cls='thin')
        xx += 16
    sh.centre(X(-40), Y(0), X(D0 + 70), Y(0))
    sh.flow(X(60), Y(40), 60)
    sh.vdim(Y(cr), Y(-cr), X(0), X(0), X(-40), 'Ø TBD\n(measure)', st='T', side='l')
    sh.lnote(X(286), Y(95), X(268), Y(70) + 4, 'gap TBD (> 0)', st='T', anchor='end')
    sh.hdim(X(0), X(P['fan_L']), Y(-175) + 4, Y(-175) + 4, Y(-175) + 46, '320 (S6, maker)', st='F')
    sh.vdim(Y(0), Y(-175), X(D0 + 20), X(D0 + 20), X(D0 + 60), '175', st='P', side='r')
    sh.detail_circle(X(D0 - 12), Y(RS + 2), 44, 'B')
    sh.vtitle(X(150), Y(-175) + 92, 'VIEW A — SIDE ELEVATION', 'Socket and diffuser start in section · fan, stand, controller outside view')
    B(sh, 8, X(-10), Y(60), 70, 150)
    B(sh, 1, X(150), Y(P['fan_H'] / 2), 210, 105)
    B(sh, 3, X(P['fan_L'] - P['collar_L'] + 3), Y(cr), 330, 160)
    B(sh, 11, X(D0 + 30), Y(r_in(D0 + 30) + T), 640, 105)
    B(sh, 6, X(110), Y(-130), 230, 610, side='l')
    B(sh, 7, X(84), Y(-160), 230, 665, side='l')
    B(sh, 2, X(cx0 + 40), Y(cy0), X(cx0 + 40) + 40, 720)

    # ---------- detail B, collar joint, 10:1 ----------
    s10 = 10.0
    xa, xb = SOCK0 - 12, D0 + 12
    vb = View(850 - s10 * xa, 190 + s10 * 96, s10)
    Xb, Yb = vb.X, vb.Y
    ft, fw = P['fl_t'], P['fl_w']
    top_r = RS + T + fw
    sh.rect(Xb(xa), Yb(cr), vb.L(cend - xa), vb.L(1), cls='vis2', fill='#c9ccd2')                       # collar wall
    sh.rect(Xb(SOCK0 - 2), Yb(cr + P['wrap_t']), vb.L(cend - SOCK0 + 2), vb.L(P['wrap_t']), cls='fill-neo')  # neoprene
    sh.rect(Xb(SOCK0), Yb(RS + P['sock_wall']), vb.L(D0 - 2 - ft - SOCK0), vb.L(P['sock_wall']), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xb(D0 - ft - 2), Yb(top_r), vb.L(ft), vb.L(top_r - RS), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xb(D0 - 2), Yb(top_r - 2), vb.L(4), vb.L(top_r - 2 - RS), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xb(D0 + 2), Yb(top_r), vb.L(ft), vb.L(top_r - RS), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xb(D0 + 2 + ft), Yb(RS + T), vb.L(xb - D0 - 2 - ft), vb.L(T), cls='vis2', fill='url(#hPLA)')
    sh.line(Xb(D0), Yb(RS), Xb(D0), Yb(70), cls='scr')
    tp = (f'M{f(Xb(xa + 1.5))},{f(Yb(cr + 0.35))} L{f(Xb(SOCK0 - 3))},{f(Yb(cr + 0.35))} '
          f'L{f(Xb(SOCK0 - 0.4))},{f(Yb(RS + P["sock_wall"] + 0.4))} L{f(Xb(SOCK0 + 13))},{f(Yb(RS + P["sock_wall"] + 0.4))}')
    sh.path(tp, cls='vis', extra='style="stroke:#59606b;stroke-width:3.4;fill:none"')
    sh.breakline(Xb(xa), Yb(cr + 4), Yb(cr - 4))
    sh.breakline(Xb(xb), Yb(RS + T + 3), Yb(RS - 1))
    # dims and notes
    sh.vdim(Yb(cr + P['wrap_t']), Yb(cr), Xb(SOCK0 - 4), Xb(SOCK0 - 4), Xb(xa + 6), '1.6', st='F', side='l', ty=Yb(cr) - 5)
    sh.lnote(Xb(SOCK0 + 10), Yb(RS) + 1, Xb(SOCK0 - 6), Yb(71.5), 'clearance ≈0.25 per side', st='P', anchor='start')
    sh.lnote(Xb(SOCK0 + 16), Yb(RS + 2), 845, Yb(RS + 2) + 4, 't 3', st='P', anchor='end')
    sh.lnote(Xb(cend + 1), Yb(cr - 0.5), Xb(xb) + 10, Yb(cr - 0.5) + 4, 'end gap TBD', st='T', anchor='start')
    sh.text(Xb((xa + xb) / 2), 600, 'DETAIL B — COLLAR IN SOCKET (10:1)', cls='vt', anchor='middle')
    sh.line(Xb((xa + xb) / 2) - 150, 604, Xb((xa + xb) / 2) + 150, 604, cls='vtu')
    sh.text(Xb((xa + xb) / 2), 621, 'Upper wall, section on centre line · socket depth 28 (sheet 4)', cls='vs', anchor='middle')
    B(sh, 5, Xb(SOCK0 + 6), Yb(RS + P['sock_wall'] + 0.4), 1000, 140, side='l')
    B(sh, 10, Xb(SOCK0 + 9), Yb(RS + 1.5), 1090, 95)
    B(sh, 95, Xb(D0 - 5), Yb(top_r - 3), 1185, 140, name='Bolted flange')
    B(sh, 13, Xb(D0), Yb(top_r - 6), 1330, 95, name='Screen frame')
    B(sh, 3, Xb(xa + 5), Yb(cr - 0.5), 900, 545)
    B(sh, 4, Xb(SOCK0 + 8), Yb(cr + 0.8), 1010, 505)
    B(sh, 12, Xb(D0), Yb(71), 1330, 545, name='Screen 12a')

    bx, by = 820, 650
    sh.rect(bx, by, 740, 100, cls='thin')
    sh.text(bx + 12, by + 22, 'SOCKET INSIDE DIAMETER (ITEM 10) — owner’s design, 2026-11-08', cls='kh')
    sh.text(bx + 12, by + 46, 'ID  =  D_collar  +  2 × 1.6 (neoprene)  +  ≈0.5 (print clearance)', cls='dim p', size=14)
    sh.text(bx + 12, by + 68, 'Example: D_collar = 150 → ID ≈ 153.7 mm (6.05 in). Owner’s first figure: 6.25 in (158.75 mm).', cls='lbl')
    sh.text(bx + 12, by + 88, 'Step loss at 13 m/s: < 0.1 Pa at 153.7, ≈0.4 Pa at 158.75, against ≈150 Pa from the fan (buy list §1).', cls='lbl')
    tx, ty = 820, 785
    sh.text(tx, ty, 'FANS COMPARED — S6 CHOSEN (D-025) · published figures, not measured', cls='kh')
    cols = [0, 170, 450]
    for c, hd in zip(cols, ['', 'AC INFINITY CLOUDLINE S6 (AI-CLS6)', 'VEVOR VV-GDFJ-AC6']):
        sh.text(tx + c, ty + 20, hd, cls='tblh')
    rows = [('Price seen', '$99.00 (maker, 2026-11-08)', '$53.90 (owner, 2026-11-09)'),
            ('Flow / max static pressure', '425 CFM / 503 Pa (maker)', '400 CFM / 300 Pa (seller)'),
            ('Motor and control', 'EC, PWM; 10 speed levels', 'AC, 60 W; variable controller'),
            ('Size', '7.87 × 12.60 × 8.35 in (200 × 320 × 212)', '306 × 255 × 212 (axis order not stated)'),
            ('Mounting', 'holes 80 × 60 mm, Ø6', 'not published'),
            ('Est. top speed (5 screens)', '≈13.0–13.4 m/s', '≈11.3 m/s'),
            ('Collar diameter', 'not published: measure', 'not published: measure')]
    for i, row in enumerate(rows):
        yy = ty + 37 + i * 18
        for c, cell in zip(cols, row):
            sh.text(tx + c, yy, cell, cls='tblc', weight=700 if c == 0 else None)
        sh.line(tx, yy + 6, tx + 740, yy + 6, cls='thin', extra='stroke-opacity="0.22"')
    return sh


# =====================================================================================
def sheet_diffuser():
    sh = Sheet(4, 'WT-02', 'WIDE-ANGLE DIFFUSER', '', 'NTS',
               ['Area ratio 3.44 needs screens with K_sum ≥ 2.1 (Mehta1977); three screens give ≈3.2, 175 long (D-026).',
                'Walls: one smooth S-curve loft from Ø152 to the 250 square through two rails (cad/sizing/profiles.py); 2θ 45.6° at most across the flats.',
                'Sharp corners, matching the chamber: the diagonal expands about twice as steeply; 12b sits at the steepest point.',
                'No honeycomb or flow straightener at the fan outlet: the fan’s swirl helps keep the diffuser flow attached.',
                'Front half (to the mid joint) prints in one piece, 231 across; back half as four corner pieces glued at mid-wall seams (D-023).',
                'Screen frames: two 2 mm layers; M3 × 16 at screen joints; foam tape on the screw-flange side (cad/sizing/diffuser.md).'])
    s = 1.75
    v = View(170 - s * (SOCK0 - 6), 450, s)
    X, Y = v.X, v.Y
    xr = D1 + 26
    for s_ in (1, -1):
        yt = s_ * (RS + P['sock_wall']) if s_ > 0 else -RS
        sh.rect(X(SOCK0), Y(yt), v.L(D0 - 2 - P['fl_t'] - SOCK0), v.L(P['sock_wall']), cls='vis2', fill='url(#hPLA)')
    flange_pair(sh, v, D0, RS, RS, frame=True)
    for xa_, xb_ in ((D0 + 2 + P['fl_t'], XDM - 2 - P['fl_t']), (XDM + 2 + P['fl_t'], D1 - 2 - P['fl_t'])):
        wall_section(sh, v, xa_, xb_)
        wall_section(sh, v, xa_, xb_, top=False)
    flange_pair(sh, v, XDM, r_in(XDM), r_in(XDM), frame=True)
    flange_pair(sh, v, D1, HALF, HALF, frame=True)
    for s_ in (1, -1):
        yt = s_ * (HALF + T) if s_ > 0 else -HALF
        sh.rect(X(D1 + 2 + P['fl_t']), Y(yt), v.L(xr - D1 - 2 - P['fl_t']), v.L(T), cls='vis2', fill='url(#hPLA)')
    sh.breakline(X(xr), Y(HALF + T + 6), Y(-HALF - T - 6))
    xmid = (D0 + D1) / 2
    for xs_, tag in ((D0, '12a'), (xmid, '12b'), (D1, '12c')):
        sh.text(X(xs_) + 5, Y(-r_in(xs_)) - 8, tag, cls='sm', anchor='start')
    sh.centre(X(SOCK0 - 4), Y(0), X(xr + 6), Y(0))
    sh.flow(X(D0 + 50), Y(-30), 62)
    sh.lnote(X(D0 + 50), Y(-r_in(D0 + 50) - T / 2), X(D0 + 22), Y(-62), 'wall 3 · S-curve loft (rails file)', st='P', anchor='start')
    sh.lnote(X(D1 - 4), Y(HALF + T + P['fl_w'] - 3), X(xr) + 30, Y(HALF + 34), 'flange 12 beyond the wall', st='P', anchor='start')
    yb_ = Y(-HALF - T - P['fl_w'])
    sh.hdim(X(SOCK0), X(D0), Y(-RS - P['sock_wall']) + 4, Y(-RS - P['sock_wall']) + 4, yb_ + 34, '28', st='P', tx=X(SOCK0) - 30, ty=yb_ + 29)
    sh.hdim(X(D0), X(D1), yb_ + 4, yb_ + 4, yb_ + 34, '175', st='F')
    sh.hdim(X(D0), X(xmid), yb_ + 4, None, yb_ + 66, '87.5 to the 12b joint', st='F')
    sh.vdim(Y(HALF), Y(-HALF), X(D1), X(D1), X(xr) + 40, '250', st='F', side='r')
    sh.vdim(Y(RS), Y(-RS), X(SOCK0), X(SOCK0), X(SOCK0) - 44, 'Ø ID\n(sheet 3)', st='P', side='l')
    sh.vtitle(X((D0 + D1) / 2), yb_ + 112, 'SECTION A–A — ON CENTRE LINE', 'Flow left to right · three screens in frames at the inlet, mid and exit joints')
    R1, R2 = 78, 128
    B(sh, 10, X(SOCK0 + 8), Y(RS + P['sock_wall']), 130, R1)
    B(sh, 95, X(D0 - 4), Y(RS + T + P['fl_w']), 300, R1)
    B(sh, 11, X(D0 + 70), Y(r_in(D0 + 70) + T), 410, R1)
    B(sh, 12, X(D0), Y(40), 165, R2, name='Screen 12a')
    B(sh, 12, X(xmid), Y(r_in(xmid) - 25), 470, R2, name='Screen 12b')
    B(sh, 12, X(D1), Y(70), 600, R2, name='Screen 12c')
    B(sh, 13, X(D1 - 2), Y(-HALF - 8), 680, 610, name='Screen frame')
    B(sh, 20, X(xr - 8), Y(-HALF - T), 680, 655, name='Settling-chamber shell (start)')
    B(sh, 98, X(D1 + 4), Y(-HALF - T - P['fl_w'] + 2), 680, 700, name='Alignment pin and hole (sheet 10)')

    vb = View(1235, 410, 1.05)
    Xb, Yb = vb.X, vb.Y
    rr = HALF + T + P['fl_w']
    sh.rect(Xb(-rr), Yb(rr), vb.L(2 * rr), vb.L(2 * rr), cls='vis2')
    sh.rect(Xb(-HALF), Yb(HALF), vb.L(2 * HALF), vb.L(2 * HALF), cls='hid')
    sh.circ(Xb(0), Yb(0), vb.L(RS + P['sock_wall']), cls='vis', fill='#ffffff')
    sh.circ(Xb(0), Yb(0), vb.L(RS), cls='vis2', fill='url(#hScr)')
    for a in (45, 135, 225, 315):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        sh.line(Xb((RS + P['sock_wall']) * ca), Yb((RS + P['sock_wall']) * sa), Xb((HALF - 4) * math.copysign(1, ca)), Yb((HALF - 4) * math.copysign(1, sa)), cls='hid')
    sh.centre(Xb(-rr - 14), Yb(0), Xb(rr + 14), Yb(0))
    sh.centre(Xb(0), Yb(rr + 14), Xb(0), Yb(-rr - 14))
    sh.vdim(Yb(HALF), Yb(-HALF), Xb(HALF), Xb(HALF), Xb(rr) + 22, '250', st='P', side='r')
    sh.hdim(Xb(-rr), Xb(rr), Yb(rr) - 4, Yb(rr) - 4, Yb(rr) - 26, '280 (J250 flange)', st='P')
    sh.lnote(Xb(-HALF + 3), Yb(HALF - 3), Xb(-rr) - 10, Yb(rr) - 40, 'sharp corners', st='P', anchor='end')
    sh.lnote(Xb(-RS * 0.7), Yb(-RS * 0.7), Xb(-rr) - 10, Yb(-rr) + 30, 'Ø socket ID\n(sheet 3)', st='P', anchor='end')
    sh.flow(Xb(rr) + 28, Yb(-rr) + 18, d='d', label='FLOW: AWAY')
    sh.vtitle(1235, Yb(-rr) + 68, 'VIEW B — FROM THE FAN SIDE', 'Looking downstream; screen 12a shaded in the socket')
    B(sh, 12, Xb(RS * 0.45), Yb(RS * 0.3), Xb(rr) + 26, Yb(rr) + 40, name='Screen 12a')

    tx, ty = 820, 790
    sh.text(tx, ty, 'DIFFUSER SCREENS AT 13 m/s (buy list §3; Wieghardt formula, our arithmetic)', cls='kh')
    cols = [0, 95, 255, 395, 560]
    for c, hd in zip(cols, ['SCREEN', 'POSITION', 'LOCAL SPEED', 'K (0.010–0.011 in wire)', 'LOSS']):
        sh.text(tx + c, ty + 20, hd, cls='tblh')
    rows = [('12a', 'Diffuser inlet', '≈7.4 m/s', '0.75–0.85', '24–28 Pa'),
            ('12b', 'Mid joint (x = 87.5)', '≈3.7 m/s', '≈0.95', '≈8 Pa'),
            ('12c', 'Diffuser exit', '≈2.1 m/s', '1.15–1.30', '3.0–3.4 Pa'),
            ('Σ', 'Three screens (D-026)', '', '≈2.9–3.1 (need ≥ 2.1)', '≈35–40 Pa')]
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
                'Compact spacing, 275 in all (D-027): honeycomb 25 after 12c, 50 to 12d, 50 to 12e, 100 to the contraction.',
                'Joints at each screen, so the frames come out; the honeycomb slides out of C1 once C2 is off (corner stops and spacers).',
                'S taps 25 after 12e and 75 before the contraction, one per wall beside its seam (D-023); mist port at 65 after 12e.',
                'Each 250 section prints as four identical corner pieces glued at mid-wall seams (D-023); walls 3.',
                'Upgrade if the flow map shows a problem: 5 mm drinking straws in place of the printed honeycomb.'])
    s = 1.45
    x0 = D1 - 18
    v = View(110 - s * x0, 455, s)
    X, Y = v.X, v.Y
    xr = C0 + 26
    for xa, xb in ((D1, SC1), (SC1, SC2), (SC2, C0)):
        for s_ in (1, -1):
            yt = s_ * (HALF + T) if s_ > 0 else -HALF
            sh.rect(X(xa + 2 + P['fl_t']), Y(yt), v.L(xb - xa - 4 - 2 * P['fl_t']), v.L(T), cls='vis2', fill='url(#hPLA)')
    for s_ in (1, -1):
        yt = s_ * (HALF + T) if s_ > 0 else -HALF
        sh.rect(X(x0), Y(yt), v.L(D1 - 2 - P['fl_t'] - x0), v.L(T), cls='vis2', fill='url(#hPLA)')
    sh.breakline(X(x0), Y(HALF + T + 6), Y(-HALF - T - 6))
    flange_pair(sh, v, D1, HALF, HALF, frame=True)
    flange_pair(sh, v, SC1, HALF, HALF, frame=True)
    flange_pair(sh, v, SC2, HALF, HALF, frame=True)
    flange_pair(sh, v, C0, HALF, HALF)
    for top in (True, False):
        sh.pl(wall_poly(v, C0 + 2 + P['fl_t'], xr, top, n=10), cls='vis2', close=True, fill='url(#hPLAk)')
    sh.breakline(X(xr), Y(HALF + T + 6), Y(-HALF - T - 6))
    sh.rect(X(HC0 + 2), Y(HALF), v.L(P['hc_L']), v.L(2 * HALF), cls='vis2', fill='#ffffff')
    k = -HALF + 5.2
    while k < HALF:
        sh.line(X(HC0 + 2), Y(k), X(HC0 + 2 + P['hc_L']), Y(k), cls='thin')
        k += 5.2
    for s_ in (1, -1):
        sh.rect(X(HC0 + 2), Y(s_ * HALF) if s_ > 0 else Y(-HALF + 4), v.L(P['hc_L']), v.L(4), cls='vis2', fill='url(#hPETG)')
    for xs_, tag in ((D1, '12c'), (SC1, '12d'), (SC2, '12e')):
        sh.text(X(xs_) + 5, Y(-HALF) - 8, tag, cls='sm', anchor='start')
    for s_ in (1, -1):
        yt = HALF + T + 12 if s_ > 0 else -HALF
        sh.rect(X(XS_TAP) - 2.3, Y(yt), 4.6, v.L(12 + T), cls='vis2', fill='url(#hBr)')
    sh.circ(X(XS_TAP), Y(0), 3.5, cls='vis2', fill='url(#hBr)')
    sh.rect(X(XMIST - 8), Y(HALF + T + 20), v.L(16), v.L(20), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(XMIST - 10), Y(HALF + T + 26), v.L(20), v.L(6), cls='vis2', fill='#ffffff')
    sh.centre(X(x0 - 6), Y(0), X(xr + 8), Y(0))
    sh.flow(X(HC1 + 30), Y(-40), 62)
    sh.cutline(X(HC0 + 2 + P['hc_L'] / 2), Y(HALF + T + P['fl_w']) - 16, Y(-HALF - T - P['fl_w']) + 16, 'B')
    sh.hdim(X(XS_TAP), X(C0), Y(HALF) + 4, Y(HALF) + 4, Y(104), '75', st='P', tx=X(XS_TAP) - 22, ty=Y(104) + 4)
    yb = Y(-HALF - T - P['fl_w'])
    yd = yb + 40
    for xa, xb, lab, st in ((D1, HC0 + 2, '25', 'F'), (HC0 + 2, HC1 + 2, '50', 'F'), (HC1 + 2, SC1, '50', 'F'), (SC1, SC2, '50', 'F'), (SC2, C0, '100', 'F')):
        sh.hdim(X(xa), X(xb), yb + 4, yb + 4, yd, lab, st=st)
    sh.hdim(X(D1), X(C0), yd + 6, yd + 6, yd + 40, '275 (D-027)', st='F')
    sh.vdim(Y(HALF), Y(-HALF), X(x0), X(x0), X(x0) - 30, '250', st='F', side='l')
    sh.vtitle(X((D1 + C0) / 2), yd + 84, 'SECTION A–A — ON CENTRE LINE', 'Flow left to right')
    R1, R2 = 70, 122
    B(sh, 22, X(HC0 + 20), Y(HALF - 2), 150, R1, name='Honeycomb stops')
    B(sh, 21, X(HC0 + 32), Y(60), 216, R2)
    B(sh, 20, X(620), Y(HALF + T), 300, R1)
    B(sh, 95, X(SC1 - 4), Y(HALF + T + P['fl_w']), 384, R2, name='Bolted flange')
    B(sh, 13, X(SC2), Y(HALF + T + 10), 520, R1)
    cxr = 690
    B(sh, 24, X(XMIST), Y(HALF + T + 26), cxr, 200)
    B(sh, 23, X(XS_TAP) + 3, Y(0), cxr, Y(-18), name='Wall pressure-tap station S\n(4 taps; side tap in far wall)')
    B(sh, 12, X(SC2), Y(-55), cxr, Y(-55), name='Screen (12c, 12d, 12e)')
    B(sh, 30, X(xr - 6), Y(-r_in(xr - 6) - T + 1), cxr, Y(-r_in(xr - 6)) + 10, name='Contraction shell (start)')

    vb = View(1235, 395, 1.05)
    Xb, Yb = vb.X, vb.Y
    rr = HALF + T + P['fl_w']
    sh.rect(Xb(-HALF - T), Yb(HALF + T), vb.L(2 * HALF + 2 * T), vb.L(2 * HALF + 2 * T), cls='vis', fill='url(#hPLA)')
    sh.rect(Xb(-HALF), Yb(HALF), vb.L(2 * HALF), vb.L(2 * HALF), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xb(-HALF + 4), Yb(HALF - 4), vb.L(2 * HALF - 8), vb.L(2 * HALF - 8), cls='vis2', fill='#ffffff')
    a = 6 / math.sqrt(3)
    row, yc = 0, 3.0
    while yc < HALF - 4 - 3:
        xc = 3.0 + (0 if row % 2 == 0 else 1.5 * a)
        while xc < HALF - 4 - a:
            pts = ' '.join(f'{f(Xb(xc + a * math.cos(math.radians(60 * k))))},{f(Yb(yc + a * math.sin(math.radians(60 * k))))}' for k in range(6))
            sh.a(f'<polygon points="{pts}" class="thin" style="stroke-width:0.45"/>')
            xc += 3 * a
        yc += 3.0
        row += 1
    sh.text(Xb(-HALF / 2), Yb(-HALF / 2) - 18, 'Honeycomb fills the', cls='sm', anchor='middle')
    sh.text(Xb(-HALF / 2), Yb(-HALF / 2) - 3, 'whole frame; cells', cls='sm', anchor='middle')
    sh.text(Xb(-HALF / 2), Yb(-HALF / 2) + 12, 'drawn in one', cls='sm', anchor='middle')
    sh.text(Xb(-HALF / 2), Yb(-HALF / 2) + 27, 'quadrant only', cls='sm', anchor='middle')
    sh.centre(Xb(-rr), Yb(0), Xb(rr), Yb(0))
    sh.centre(Xb(0), Yb(rr), Xb(0), Yb(-rr))
    sh.hdim(Xb(-HALF + 4), Xb(HALF - 4), Yb(HALF + T) - 4, Yb(HALF + T) - 4, Yb(HALF + T) - 26, '249.4 honeycomb (fits the bed in one piece)', st='P')
    sh.vdim(Yb(HALF), Yb(-HALF), Xb(HALF + T), Xb(HALF + T), Xb(HALF + T) + 22, '250', st='F', side='r')
    for sx_, sy_ in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        sh.line(Xb(sx_ * HALF if sx_ else -3), Yb(sy_ * HALF if sy_ else -3), Xb(sx_ * (HALF + T) if sx_ else 3), Yb(sy_ * (HALF + T) if sy_ else 3), cls='vis', extra='style="stroke:#c0410d;stroke-width:2.2"')
    sh.flow(1448, Yb(HALF) + 6, d='d', label='FLOW: AWAY')
    sh.detail_circle(Xb(72), Yb(72), 18, 'C')
    sh.vtitle(1235, Yb(-HALF - T) + 40, 'SECTION B–B — THROUGH THE HONEYCOMB', 'Looking downstream')
    B(sh, 22, Xb(-HALF + 2), Yb(-HALF / 2 - 30), Xb(-HALF - T) - 40, Yb(-HALF / 2) + 50, side='l')
    B(sh, 21, Xb(40), Yb(40), Xb(HALF + T) + 40, Yb(-HALF / 2) + 50, side='r')

    vc = View(190, 905, 8)
    Xc, Yc = vc.X, vc.Y
    for (xc, yc) in ((0, 0), (1.5 * a, 3), (3 * a, 0), (1.5 * a, -3)):
        pts = [(Xc(xc + a * math.cos(math.radians(60 * k))), Yc(yc + a * math.sin(math.radians(60 * k)))) for k in range(6)]
        pin = [(Xc(xc + (a - 0.46) * math.cos(math.radians(60 * k))), Yc(yc + (a - 0.46) * math.sin(math.radians(60 * k)))) for k in range(6)]
        sh.pl(pts, cls='vis2', close=True, fill='#c9ccd2')
        sh.pl(pin, cls='vis2', close=True, fill='#ffffff')
    sh.vdim(Yc(3), Yc(-3), Xc(0), Xc(0), Xc(-a) - 18, '6', st='P', side='l')
    sh.lnote(Xc(3 * a + a * 0.5 - 0.1), Yc(a * 0.87 - 0.2), Xc(3 * a) + 60, Yc(6), 'wall 0.4', st='P', anchor='start')
    sh.text(Xc(3 * a) + 60, 900, 'DETAIL C — CELLS (8:1)', cls='vt', anchor='start')
    sh.text(Xc(3 * a) + 60, 920, 'Hexagons 6 across flats, about 48–50 long (L/D ≈ 8); about 87 % open.', cls='vs', anchor='start')
    sh.text(Xc(3 * a) + 60, 936, 'At 2.1 m/s the 0.4 mm wall wakes (Re ≈ 56) die out before the first screen (buy list §3).', cls='vs', anchor='start')

    tx, ty = 1060, 700
    sh.text(tx, ty, 'STATION SPACING — COMPACT CHOSEN (D-027)', cls='kh')
    rows = [('', 'Chosen: 0.2 D (Mehta1979)', 'Not chosen: full decay'),
            ('Diffuser exit → honeycomb', '25', '25'),
            ('Honeycomb → 12d', '50', '≥150 (6 mm cells)'),
            ('12d → 12e', '50', '500 wire Ø = 140 *'),
            ('12e → contraction', '100', '100'),
            ('Chamber length', '275', '≈465 *')]
    for i, (a_, b_, c_) in enumerate(rows):
        yy = ty + 22 + i * 19
        cl = 'tblh' if i == 0 else 'tblc'
        sh.text(tx, yy, a_, cls=cl, weight=700 if i else None)
        sh.text(tx + 170, yy, b_, cls=cl)
        sh.text(tx + 300, yy, c_, cls=cl)
        if i:
            sh.line(tx, yy + 6, tx + 500, yy + 6, cls='thin', extra='stroke-opacity="0.22"')
    sh.text(tx, ty + 22 + 6 * 19 + 2, '* Our arithmetic with the 0.011 in screen wire and 6 mm cells. S taps 25 after 12e.', cls='sm')
    sh.text(tx, ty + 22 + 6 * 19 + 18, '  Orange ticks in section B–B: the glued mid-wall seams of the corner pieces (D-023).', cls='sm')
    return sh
