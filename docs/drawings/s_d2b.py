"""Sheets 7-8, second layout."""
from wtsheets import *
from s_d2 import h, RB, RB1, SH_TOP, CELL_TOP, CELL_BOT, shield_side, teardrop
from s_d1 import flange_pair


def sheet_test_section():
    sh = Sheet(7, 'WT-05', 'TEST SECTION, WINDOWS AND MODEL STATION', '', 'NTS',
               ['Inside 100.3 × 100.3 (D-008; 0.15 per side bigger than the contraction exit). 310 long: front body 245 + extension 65 (D-024).',
                'E taps at 56 in all four walls of the printed entrance band (0–80); ball at 206; ≈90 behind the 1 in ball to the open exit.',
                'Top panel 80–235 lifts off on magnets (D-014); one fixed window on the camera side, black printed wall opposite (D-024).',
                'M taps: one in each side wall at the ball, 12 above the floor. Windows sit flush in pockets cut from the inside, against a 5 lip.',
                'Floor inserts 60 × 70 (D-014): 1 in and 3/4 in sphere inserts and a plain one; they seal on foam tape on the ledge (D-028).',
                'Probe: straight, through the open exit, on a stand (D-030), calibration days only. Balance and image sting: sheet 8.'])
    s = 2.2
    v = View(80 - s * (C1 - 20), 330, s)
    X, Y = v.X, v.Y
    ft = P['floor_t']
    for s_ in (1, -1):
        yt = s_ * (h + T) if s_ > 0 else -h
        sh.rect(X(C1 - 20), Y(yt), v.L(14), v.L(T), cls='vis2', fill='url(#hPLAk)')
        y1, y2 = s_ * (h + T), s_ * (h + T + P['fl_w'])
        sh.rect(X(C1 - 6), Y(max(y1, y2)), v.L(6), v.L(P['fl_w']), cls='vis2', fill='url(#hPLAk)')
    sh.breakline(X(C1 - 20), Y(h + T + 4), Y(-h - T - 4))
    for xa, xb in ((C1, C1 + 80), (C1 + 235, XTJ - 2 - P['fl_t']), (XTJ + 2 + P['fl_t'], T1)):
        sh.rect(X(xa), Y(h + T), v.L(xb - xa), v.L(T), cls='vis2', fill='url(#hPLAk)')
    for xa in (C1 + 80, C1 + 229):
        sh.rect(X(xa), Y(h + 10), v.L(6), v.L(10 - P['acr_t']), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(C1 + 80), Y(h + P['acr_t']), v.L(155), v.L(P['acr_t']), cls='fill-acr')
    flange_pair(sh, v, XTJ, h, h, fill='url(#hPLAk)')
    floor_run(sh, X, Y, C1, T1, XM - INS_HL, XM + INS_HL, -h, ft, hole=(XM - 2.5, XM + 2.5))
    sh.rect(X(XE) - 3.5, Y(-h - ft), 7, v.L(14), cls='vis2', fill='url(#hBr)')
    sh.rect(X(XE) - 3.5, Y(h + T + 14), 7, v.L(14), cls='vis2', fill='url(#hBr)')
    sh.circ(X(XM), Y(-h + 12), v.L(2.2), cls='vis2', fill='url(#hBr)')
    sh.circ(X(XM), Y(0), v.L(RB1), cls='hid')
    sh.circ(X(XM), Y(0), v.L(RB), cls='vis', fill='#f4f4f2')
    shield_side(sh, v, XM)
    for sx in (-1, 1):
        sh.line(X(XM) + sx * v.L(P['sting_d'] / 2), Y(-RB - 2), X(XM) + sx * v.L(P['sting_d'] / 2), Y(-h - ft - 12), cls='hid')
    sh.line(X(XM), Y(15), X(T1 + 14), Y(15), cls='hid', extra='style="stroke:#5a6270;stroke-width:1.6"')
    sh.text(X(XM + 22), Y(15) + 14, 'probe (calibration only): straight, through the open exit', cls='sm', anchor='start')
    sh.centre(X(C1 - 24), Y(0), X(T1 + 18), Y(0))
    sh.flow(X(C1 + 16), Y(-22), 60)
    # dims: station chain inside the duct, total below
    yin = Y(h) + 4
    yd1 = Y(41)
    for xa, xb, lab in ((C1, XE, '56'), (XE, XM, '150'), (XM, T1, '104')):
        sh.hdim(X(xa), X(xb), yin, yin, yd1, lab, st='F')
    sh.hdim(X(C1), X(T1), yin, yin, Y(28), '310', st='F')
    yfl = Y(-h - ft) + 34
    sh.hdim(X(C1), X(XTJ), Y(-h - ft) + 4, Y(-h - ft) + 4, yfl, '245 front body (one print)', st='F')
    sh.hdim(X(XTJ), X(T1), Y(-h - ft) + 4, Y(-h - ft) + 4, yfl, '65', st='F')
    sh.vdim(Y(h), Y(-h), X(T1), X(T1), X(T1 + 15) + 26, '100', st='F', side='r')
    sh.vdim(Y(0), Y(-h), X(XM + 40), X(XM + 40), X(XM + 58), '50', st='P', side='r')
    # callouts above
    R1, R2, R3 = 58, 104, 150
    B(sh, 30, X(C1 - 16), Y(h + T), 70, R1, name='Contraction (end)')
    B(sh, 42, X(C1 + 150), Y(h + P['acr_t']), 380, R1, name='Top window panel (80–235)')
    B(sh, 40, X(C1 + 40), Y(h + T), 800, R1, name='Test-section body (black PLA)')
    B(sh, 48, X(XE), Y(h + T + 14), 230, R2, name='Tap station E (4 walls)')
    B(sh, 44, X(C1 + 232), Y(h + 6), 640, R2, name='Panel frame')
    B(sh, 95, X(C1 - 3), Y(h + T + P['fl_w'] - 2), 230, R3, name='Bolted flange (J100)')
    B(sh, 95, X(XTJ - 3), Y(h + T + P['fl_w'] - 2), 560, R3, name='Joint to the extension (x = 245)')
    B(sh, 50, X(T1 + 10), Y(15), 860, R3, name='Probe stand (D-030)')
    # callouts below
    Q1, Q2 = 548, 590
    B(sh, 41, X(C1 + 70), Y(-h - 3), 330, Q1)
    B(sh, 49, X(XM) - 4, Y(-h + 12), 560, Q2, name='Tap station M (side walls, 12 up)')
    B(sh, 64, X(XM + 12), Y(-35), 620, Q1)
    B(sh, 53, X(XM + 25), Y(-h - 1.5), 760, Q1)
    B(sh, 60, X(XM + RB * 0.75), Y(-RB * 0.6), 840, 400, name='Validation sphere')
    B(sh, 52, X(T1), Y(-26), 840, 445, name='Open exit')
    sh.vtitle(X((C1 + T1) / 2), 638, 'SECTION A–A — ON CENTRE LINE', 'Flow left to right · M tap seen in the far (black) wall · sting continues to the balance (sheet 8)')

    # ---------- view B, plan ----------
    sb = 1.15
    vb = View(915 - sb * (C1 - 6), 255, sb)
    Xb, Yb = vb.X, vb.Y
    sh.rect(Xb(C1), Yb(h + 12), vb.L(P['ts_L']), vb.L(2 * h + 24), cls='vis')
    sh.rect(Xb(C1 + 12), Yb(h + 10), vb.L(P['ts_L'] - 24), vb.L(2 * h + 20), cls='vis2')
    sh.rect(Xb(C1 + 80), Yb(h + 3), vb.L(155), vb.L(2 * h + 6), cls='fill-acr')
    sh.line(Xb(XTJ), Yb(h + 12), Xb(XTJ), Yb(-h - 12), cls='vis2')
    sh.rect(Xb(C1 - 6), Yb(h + T + P['fl_w']), vb.L(6), vb.L(2 * (h + T + P['fl_w'])), cls='vis2')
    sh.circ(Xb(XM), Yb(0), vb.L(RB), cls='vis2', fill='#f4f4f2')
    sh.pl([(Xb(px), Yb(py)) for px, py in teardrop(XM, 0)], cls='hid', close=True)
    for mx, my in ((C1 + 86, h + 6), (C1 + 229, h + 6), (C1 + 86, -h - 6), (C1 + 229, -h - 6)):
        sh.circ(Xb(mx), Yb(my), vb.L(4), cls='vis2', fill='#3a3f47')
    for xt in (XE, XM):
        for s_ in (1, -1):
            y0, y1 = s_ * (h + 12), s_ * (h + 24)
            sh.rect(Xb(xt) - 1.8, Yb(max(y0, y1)), 3.6, vb.L(12), cls='vis2', fill='url(#hBr)')
    sh.rect(Xb(XM - INS_HL), Yb(INS_HW), vb.L(2 * INS_HL), vb.L(2 * INS_HW), cls='thin')
    for px_, py_ in ((XM - INS_HL + 2, INS_HW - 2), (XM + INS_HL - 2, -INS_HW + 2)):
        sh.circ(Xb(px_), Yb(py_), 2.2, cls='vis2', fill='#3a3f47')
    sh.centre(Xb(C1 - 10), Yb(0), Xb(T1 + 10), Yb(0))
    sh.flow(Xb(C1 + 30), Yb(-30), 50, label=None)
    sh.hdim(Xb(C1 + 80), Xb(C1 + 235), Yb(-h - 10) + 4, Yb(-h - 10) + 4, Yb(-h - 12) + 52, 'top opening 155 × 100.3', st='F')
    sh.text(Xb((C1 + T1) / 2), 96, 'VIEW B — PLAN (TOP)', cls='vt', anchor='middle')
    sh.text(Xb((C1 + T1) / 2), 114, 'Far (black) wall up; top panel shown clear', cls='vs', anchor='middle')
    B(sh, 45, Xb(C1 + 229) + 4, Yb(h + 6) - 3, 1330, 150, name='Magnet (8 × 2), 4 shown')
    B(sh, 53, Xb(XM + INS_HL), Yb(18), 1330, 250)
    B(sh, 48, Xb(XE), Yb(-h - 24), 1330, 305, name='Tap station E (side taps)')
    B(sh, 49, Xb(XM), Yb(-h - 24), 1330, 349, name='Tap station M (side walls)')

    # ---------- section C-C ----------
    sc = 2.4
    vc = View(1100, 665, sc)
    Xc, Yc = vc.X, vc.Y
    floor_run(sh, Xc, Yc, -70, 70, -INS_HW, INS_HW, -h, ft, hole=(-2.5, 2.5))
    sh.pl([(Xc(-58), Yc(-h)), (Xc(-58), Yc(40)), (Xc(-66), Yc(40)), (Xc(-66), Yc(46.8)), (Xc(-53), Yc(46.8)), (Xc(-53), Yc(50)),
           (Xc(-50), Yc(50)), (Xc(-50), Yc(-h))], cls='vis2', close=True, fill='url(#hPLAk)')
    sh.pl([(Xc(66), Yc(40)), (Xc(66), Yc(46.8)), (Xc(53), Yc(46.8)), (Xc(53), Yc(50)), (Xc(50), Yc(50)), (Xc(50), Yc(40))],
          cls='vis2', close=True, fill='url(#hPLAk)')
    sh.rect(Xc(50), Yc(40), vc.L(P['acr_t']), vc.L(70), cls='fill-acr')
    sh.rect(Xc(53.2), Yc(40), vc.L(4.8), vc.L(70), cls='vis2', fill='url(#hPLAk)')
    sh.rect(Xc(50), Yc(-30), vc.L(8), vc.L(20), cls='vis2', fill='url(#hPLAk)')
    for s_ in (1, -1):
        sh.pl([(Xc(s_ * 53), Yc(50)), (Xc(s_ * 53), Yc(60)), (Xc(s_ * 68), Yc(60)), (Xc(s_ * 68), Yc(50)), (Xc(s_ * 57), Yc(50)),
               (Xc(s_ * 57), Yc(53.2)), (Xc(s_ * 53), Yc(53.2))], cls='vis2', close=True, fill='url(#hPLA)')
        sh.rect(Xc(min(s_ * 56, s_ * 65)), Yc(50), vc.L(9), vc.L(3.2), cls='vis2', fill='url(#hFoam)')
        sh.rect(Xc(min(s_ * 57, s_ * 65)), Yc(55.6), vc.L(8), vc.L(2), cls='fill-neo')
        sh.rect(Xc(min(s_ * 57, s_ * 65)), Yc(45.2), vc.L(8), vc.L(2), cls='fill-neo')
    sh.rect(Xc(-57), Yc(50 + P['acr_t']), vc.L(114), vc.L(P['acr_t']), cls='fill-acr')
    sh.circ(Xc(0), Yc(0), vc.L(RB1), cls='hid')
    sh.circ(Xc(0), Yc(0), vc.L(RB), cls='vis', fill='#f4f4f2')
    sh.rect(Xc(-3.75), Yc(SH_TOP), vc.L(7.5), vc.L(SH_TOP + h), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xc(-2.5), Yc(SH_TOP), vc.L(5), vc.L(SH_TOP + h), cls='vis2', fill='#ffffff')
    sh.rect(Xc(-P['sting_d'] / 2), Yc(-RB + 1), vc.L(P['sting_d']), vc.L(-RB + 1 + h + ft + 10), cls='vis2', fill='url(#hBr)')
    sh.rect(Xc(-70), Yc(-36.4), vc.L(12), vc.L(3.2), cls='vis2', fill='url(#hBr)')
    sh.rect(Xc(58), Yc(-36.4), vc.L(12), vc.L(3.2), cls='vis2', fill='url(#hBr)')
    sh.centre(Xc(-78), Yc(0), Xc(78), Yc(0))
    sh.centre(Xc(0), Yc(80), Xc(0), Yc(-h - 20))
    sh.flow(Xc(-32), Yc(-32), d='d', label=None)
    sh.hdim(Xc(-50), Xc(50), Yc(-h - ft) + 4, Yc(-h - ft) + 4, Yc(-h - ft) + 30, '100', st='F')
    sh.vdim(Yc(h), Yc(-h), Xc(-58), Xc(-58), Xc(-70) - 34, '100', st='F', side='l')
    sh.hdim(Xc(-3.75), Xc(3.75), Yc(-26), Yc(-26), Yc(-34), '7.5', st='P', tx=Xc(3.75) + 26, ty=Yc(-34) + 4)
    sh.vdim(Yc(-RB), Yc(SH_TOP), Xc(3.75), Xc(3.75), Xc(14), '5', st='P', side='r')
    sh.lnote(Xc(-RB * 0.7), Yc(RB * 0.7), Xc(-46), Yc(30), 'Ø19.05 · Ø25.4 dashed', st='F', anchor='start')
    sh.detail_circle(Xc(60), Yc(52), 17, 'F')
    sh.text(1100, 905, 'SECTION C–C — AT THE MODEL STATION', cls='vt', anchor='middle')
    sh.line(1100 - 150, 909, 1100 + 150, 909, cls='vtu')
    sh.text(1100, 926, 'Looking downstream; black printed wall left, fixed window right (D-024); M taps 12 above the floor', cls='vs', anchor='middle')
    B(sh, 43, Xc(51.6), Yc(-10), 1340, 640, name='Side window panel')
    B(sh, 64, Xc(3.75), Yc(-35), 1340, 700)
    B(sh, 53, Xc(15), Yc(-h - 1.5), 1340, 730)
    B(sh, 41, Xc(40), Yc(-h - 3), 1340, 760)
    B(sh, 63, Xc(0), Yc(-h - ft - 6), 1340, 812)
    B(sh, 47, Xc(-51.5), Yc(48.5), 905, 470, side='l', name='Locating lip')
    B(sh, 40, Xc(-54), Yc(10), 905, 520, side='l', name='Black printed wall')
    B(sh, 49, Xc(-66), Yc(-34.8), 905, 590, side='l', name='Tap station M')

    # ---------- detail F, panel edge 10:1 ----------
    sf = 10
    vf = View(150 - sf * 46, 720 + sf * 62, sf)
    Xf, Yf = vf.X, vf.Y
    sh.pl([(Xf(46), Yf(40)), (Xf(66), Yf(40)), (Xf(66), Yf(46.8)), (Xf(53), Yf(46.8)), (Xf(53), Yf(50)), (Xf(50), Yf(50)),
           (Xf(50), Yf(40))], cls='vis2', close=True, fill='url(#hPLAk)')
    sh.pl([(Xf(53), Yf(50)), (Xf(53), Yf(60)), (Xf(68), Yf(60)), (Xf(68), Yf(50)), (Xf(57), Yf(50)), (Xf(57), Yf(53.2)), (Xf(53), Yf(53.2))],
          cls='vis2', close=True, fill='url(#hPLA)')
    sh.rect(Xf(56), Yf(50), vf.L(9), vf.L(3.2), cls='vis2', fill='url(#hFoam)')
    sh.rect(Xf(57), Yf(55.6), vf.L(8), vf.L(2), cls='fill-neo')
    sh.rect(Xf(57), Yf(45.2), vf.L(8), vf.L(2), cls='fill-neo')
    sh.rect(Xf(46), Yf(50 + P['acr_t']), vf.L(11), vf.L(P['acr_t']), cls='fill-acr')
    sh.breakline(Xf(46), Yf(53.6), Yf(39.6))
    sh.breakline(Xf(66), Yf(47.2), Yf(39.6))
    sh.line(Xf(43), Yf(50), Xf(71), Yf(50), cls='ctr')
    sh.text(Xf(71) + 4, Yf(50) + 4, 'inside face', cls='sm', anchor='start')
    sh.vdim(Yf(50 + P['acr_t']), Yf(50), Xf(46), Xf(46), Xf(44), '3.2', st='F', side='l')
    sh.vdim(Yf(53.2), Yf(50), Xf(65), Xf(65), Xf(69.5), '3.2', st='P', side='r', ty=Yf(53.2) - 4)
    sh.lnote(Xf(60), Yf(45.4), Xf(66) + 10, 935, 'pocket Ø8.2–8.4 × 2.2 (coupon C3)', st='P', anchor='start')
    sh.text(Xf(57), 696, 'DETAIL F — PANEL EDGE (10:1, CONCEPT)', cls='vt', anchor='middle')
    sh.line(Xf(57) - 150, 700, Xf(57) + 150, 700, cls='vtu')
    sh.text(Xf(57), 717, 'Acrylic flush with the inside face; pocket and lip sizes in cad/sizing/test_section.md', cls='vs', anchor='middle')
    B(sh, 42, Xf(47.5), Yf(52), 90, 742, side='r', name='Top window panel')
    B(sh, 47, Xf(51.5), Yf(48.5), 90, 932, side='r', name='Locating lip')
    B(sh, 44, Xf(67), Yf(59), 560, 760)
    B(sh, 46, Xf(64.5), Yf(51.6), 560, 820, name='Foam gasket tape')
    B(sh, 45, Xf(64.5), Yf(46.2), 560, 890, name='Magnet (8 × 2), pair')
    return sh


# =====================================================================================
def sheet_balance():
    sh = Sheet(8, 'WT-06', 'FORCE BALANCE AND MODEL MOUNT', '', 'NTS',
               ['The cell stands upright under the ball; the sting (85) is clamped only to its top end, the bottom end to the base; screws along the wind.',
                'Sealed box (D-028): airtight except the gap round the sting; foam tape at its joints and the insert ledge; door on the camera side.',
                'Sting lock 68 (D-015): a thumb screw clamps the sting in the mount’s blind hole, no glue. Hold the mount while turning the screw.',
                'Shield 64 (NACA section 22.5 × 7.5, bore Ø5) on the sphere insert 53, ending 5 below the ball; never touching the sting.',
                'Each ball press-fit on its own full-length sting (D-016). Image sting (D-029): view H; ball alone = Run 1 − (Run 2 − Run 1).',
                'Box bottom 145 below the axis, 30 above the bench (cad/sizing/supports.md). Sizes in cad/sizing/balance.md.'])
    s = 3.4
    v = View(430 - s * XM, 200, s)
    X, Y = v.X, v.Y
    ft = P['floor_t']
    floor_run(sh, X, Y, XM - 62, XM + 62, XM - INS_HL, XM + INS_HL, -h, ft, hole=(XM - 2.5, XM + 2.5))
    sh.breakline(X(XM - 62), Y(-h + 3), Y(-h - ft - 3))
    sh.breakline(X(XM + 62), Y(-h + 3), Y(-h - ft - 3))
    sh.path(f'M{f(X(XM-7.5))},{f(Y(-h))} L{f(X(XM-7.5))},{f(Y(SH_TOP-2.5))} Q{f(X(XM-7.5))},{f(Y(SH_TOP))} {f(X(XM-5))},{f(Y(SH_TOP))} '
            f'L{f(X(XM-2.5))},{f(Y(SH_TOP))} L{f(X(XM-2.5))},{f(Y(-h))} Z', cls='vis2', fill='url(#hPLA)')
    sh.path(f'M{f(X(XM+2.5))},{f(Y(-h))} L{f(X(XM+2.5))},{f(Y(SH_TOP))} L{f(X(XM+15))},{f(Y(SH_TOP))} L{f(X(XM+15))},{f(Y(-h))} Z', cls='vis2', fill='url(#hPLA)')
    sh.circ(X(XM), Y(0), v.L(RB1), cls='hid')
    sh.a(f'<circle cx="{f(X(XM))}" cy="{f(Y(0))}" r="{f(v.L(RB))}" class="vis" style="fill:url(#hPETG)"/>')
    sh.rect(X(XM - 1.55), Y(0), v.L(3.1), v.L(RB), cls='vis2', fill='#ffffff')
    # one full-length sting from the ball's centre down to the mount: no sleeve, no separate stem (D-016)
    sh.rect(X(XM - P['sting_d'] / 2), Y(0), v.L(P['sting_d']), v.L(-(CELL_TOP + 12)), cls='vis2', fill='url(#hBr)')
    for xs_ in (XM - 9, XM + 3):
        sh.rect(X(xs_), Y(-h - ft - 2), v.L(6), v.L(7), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 7), Y(CELL_TOP + 12), v.L(14), v.L(19), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - P['sting_d'] / 2), Y(CELL_TOP + 12), v.L(P['sting_d']), v.L(10), cls='vis2', fill='url(#hBr)')
    yk = CELL_TOP + 7                                   # thumb-screw axis (layout)
    sh.rect(X(XM - 7), Y(yk + 2.5), v.L(4.4), v.L(5), cls='vis2', fill='url(#hBr)')
    sh.rect(X(XM - 12), Y(yk + 1.5), v.L(12 - P['sting_d'] / 2), v.L(3), cls='vis2', fill='#b9bec6')
    sh.rect(X(XM - 17), Y(yk + 3), v.L(5), v.L(6), cls='vis2', fill='#ead9a4')
    for i_ in range(1, 5):
        sh.line(X(XM - 17 + i_), Y(yk + 3), X(XM - 17 + i_), Y(yk - 3), cls='thin')
    sh.rect(X(XM - 3), Y(CELL_TOP), v.L(6), v.L(P['cell_L']), cls='vis', fill='url(#hAl)')
    sh.rect(X(XM - 2.2), Y(CELL_TOP - 12), v.L(4.4), v.L(P['cell_L'] - 24), cls='hid')
    yb0 = CELL_BOT + 10
    sh.rect(X(XM - 7), Y(yb0), v.L(14), v.L(yb0 + 136), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 47), Y(-136), v.L(94), v.L(6), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 50), Y(-h - ft), v.L(100), v.L(-h - ft + 145), cls='vis2')
    sh.rect(X(XM - 47), Y(-h - ft), v.L(94), v.L(-h - ft + 142), cls='thin')
    sh.rect(X(XM + 16), Y(-131), v.L(24), v.L(3), cls='fill-pcb')
    for yy in (CELL_TOP - 3.5, CELL_TOP - 3.5 - P['cell_hole']):
        sh.line(X(XM - 7), Y(yy), X(XM + 9), Y(yy), cls='hid')
        sh.rect(X(XM + 7), Y(yy + 2.5), v.L(2), v.L(5), cls='vis2', fill='url(#hBr)')
    sh.path(f'M{f(X(XM+3))},{f(Y(CELL_TOP-20))} C{f(X(XM+14))},{f(Y(CELL_TOP-26))} {f(X(XM+20))},{f(Y(-120))} {f(X(XM+24))},{f(Y(-138))}',
            cls='thin', extra='style="stroke:#a33;stroke-width:1.2;fill:none"')
    sh.centre(X(XM), Y(RB1 + 8), X(XM), Y(-150))
    sh.centre(X(XM - 20), Y(0), X(XM + 20), Y(0))
    sh.flow(X(XM - 34), Y(22), 58)
    # dims: three columns on the right
    c1, c2, c3 = X(XM + 30), X(XM + 62) + 14, X(XM + 62) + 74
    sh.vdim(Y(-RB), Y(SH_TOP), X(XM + 15), X(XM + 15), c1, '5', st='P', side='r')
    sh.vdim(Y(SH_TOP), Y(-h), X(XM + 15), X(XM + 15), c1, '35.5', st='P', side='r')
    sh.vdim(Y(CELL_TOP - 3.5), Y(CELL_TOP - 3.5 - P['cell_hole']), X(XM + 9), X(XM + 9), c1, '40', st='F', side='r')
    sh.vdim(Y(0), Y(-h), X(XM + 15), X(XM + 62), c2, '50', st='P', side='r')
    sh.vdim(Y(-h), Y(CELL_TOP), X(XM + 62), X(XM + 7), c2, '37', st='P', side='r')
    sh.vdim(Y(CELL_TOP), Y(CELL_BOT), X(XM + 7), X(XM + 7), c2, '47', st='F', side='r')
    sh.vdim(Y(0), Y(CELL_TOP), X(XM + 62), X(XM + 62), c3, '85\n(sting)', st='P', side='r')
    sh.hdim(X(XM - 3), X(XM + 3), Y(CELL_BOT) + 4, Y(CELL_BOT) + 4, Y(CELL_BOT) + 22, '6', st='F', tx=X(XM - 3) - 14)
    sh.lnote(X(XM + RB * 0.7), Y(RB * 0.7), X(XM + 26), Y(26), 'Ø19.05 · Ø25.4 dashed', st='F', anchor='start')
    sh.lnote(X(XM + 1), Y(-RB / 2), X(XM + 26), Y(12), 'press-fit hole Ø3.0–3.1 × 9.5 deep (12.7 for 1 in)', st='P', anchor='start')
    sh.vtitle(X(XM), 812, 'VIEW A — SIDE SECTION ON CENTRE LINE', 'Wind left to right · 3/4 in ball shown, 1 in dashed')
    cl = 252
    B(sh, 60, X(XM - RB * 0.7), Y(RB * 0.7), cl, Y(14), side='l')
    B(sh, 64, X(XM - 6), Y(-38), cl, 302, side='l')
    B(sh, 53, X(XM - 25), Y(-h - 2.5), cl, 329, side='l')
    B(sh, 41, X(XM - 52), Y(-h - 3), cl - 40, 356, side='l')
    B(sh, 69, X(XM - 7), Y(-h - ft - 5), cl, Y(-h - ft - 5) + 14, side='l', name='Overload stops\n(set at 120 g)')
    B(sh, 63, X(XM - 1.6), Y(-68), cl, 448, side='l')
    B(sh, 68, X(XM - 14.5), Y(CELL_TOP + 7), cl, 474, side='l')
    B(sh, 96, X(XM - 4.5), Y(CELL_TOP + 4.9), cl, 528, side='l', name='Heat-set insert (M3)')
    B(sh, 65, X(XM - 7), Y(CELL_TOP - 3), cl, 554, side='l')
    B(sh, 66, X(XM - 3), Y(CELL_TOP - 25), cl, Y(CELL_TOP - 25) + 34, side='l')
    B(sh, 67, X(XM - 7), Y(-130), cl, Y(-130) + 16, side='l')
    Rb = 768
    B(sh, 73, X(XM + 8), Y(CELL_TOP - 3.5 - P['cell_hole']), 330, Rb, name='Short M3 screw')
    B(sh, 70, X(XM - 30), Y(-136), 175, Rb, name='Balance module plate')
    B(sh, 72, X(XM + 30), Y(-129), 470, Rb, name='HX711 amplifier board')
    B(sh, 71, X(XM + 50), Y(-140), 640, Rb, name='Sealed load-cell box (D-028)')

    # ---------- view B, front ----------
    vb = View(1100, 200, s)
    Xb, Yb = vb.X, vb.Y
    floor_run(sh, Xb, Yb, -40, 40, -INS_HW, INS_HW, -h, ft, fix=None, ins=None)
    sh.breakline(Xb(-40), Yb(-h + 3), Yb(-h - ft - 3))
    sh.breakline(Xb(40), Yb(-h + 3), Yb(-h - ft - 3))
    sh.rect(Xb(-3.75), Yb(SH_TOP), vb.L(7.5), vb.L(SH_TOP + h), cls='vis2')
    sh.circ(Xb(0), Yb(0), vb.L(RB1), cls='hid')
    sh.circ(Xb(0), Yb(0), vb.L(RB), cls='vis', fill='#f4f4f2')
    for sx in (-1, 1):
        sh.line(Xb(sx * P['sting_d'] / 2), Yb(-RB), Xb(sx * P['sting_d'] / 2), Yb(SH_TOP), cls='vis2')
    sh.rect(Xb(-P['sting_d'] / 2), Yb(-h - ft), vb.L(P['sting_d']), vb.L((-h - ft) - (CELL_TOP + 12)), cls='vis2', fill='url(#hBr)')
    sh.rect(Xb(-9), Yb(CELL_TOP + 12), vb.L(18), vb.L(19), cls='vis2')
    sh.circ(Xb(0), Yb(CELL_TOP + 7), vb.L(3), cls='vis2', fill='#ead9a4')
    sh.circ(Xb(0), Yb(CELL_TOP + 7), vb.L(1.6), cls='thin')
    sh.rect(Xb(-6), Yb(CELL_TOP), vb.L(12), vb.L(P['cell_L']), cls='vis', fill='#e6ebef')
    for yy in (CELL_TOP - 3.5, CELL_TOP - 3.5 - P['cell_hole']):
        for xx in (-3, 3):
            sh.circ(Xb(xx), Yb(yy), vb.L(1.6), cls='vis2', fill='#ffffff')
    sh.rect(Xb(-9), Yb(yb0), vb.L(18), vb.L(yb0 + 136), cls='vis2')
    sh.rect(Xb(-42), Yb(-136), vb.L(84), vb.L(6), cls='vis2')
    sh.rect(Xb(-45), Yb(-h - ft), vb.L(90), vb.L(-h - ft + 145), cls='vis2')
    sh.rect(Xb(45), Yb(-h - ft - 8), vb.L(3), vb.L(70), cls='vis2', fill='url(#hPLA)')
    sh.text(Xb(48) + 6, Yb(-h - ft - 40), 'door (D-028)', cls='sm', anchor='start')
    sh.centre(Xb(0), Yb(RB1 + 8), Xb(0), Yb(-150))
    sh.flow(Xb(-32), Yb(16), d='d', label=None)
    sh.hdim(Xb(-6), Xb(6), Yb(CELL_BOT) + 4, Yb(CELL_BOT) + 4, Yb(CELL_BOT) + 22, '12', st='F', tx=Xb(6) + 24, ty=Yb(CELL_BOT) + 26)
    sh.hdim(Xb(-3), Xb(3), Yb(CELL_TOP - 3.5) - 6, Yb(CELL_TOP - 3.5) - 6, Yb(CELL_TOP - 3.5) - 12, '6', st='F', tx=Xb(3) + 22, ty=Yb(CELL_TOP - 3.5) - 8, ext=False)
    sh.hdim(Xb(-3.75), Xb(3.75), Yb(-30), Yb(-30), Yb(-30), '7.5', st='P', tx=Xb(3.75) + 26, ty=Yb(-30) + 4, ext=False)
    sh.vtitle(1100, 812, 'VIEW B — FRONT', 'Looking downstream; door on the camera side (right)')

    # ---------- section D-D ----------
    vd = View(1415, 290, 9)
    Xd, Yd = vd.X, vd.Y
    sh.pl([(Xd(px), Yd(py)) for px, py in teardrop(0, 0)], cls='vis2', close=True, fill='url(#hPLA)')
    sh.circ(Xd(0), Yd(0), vd.L(2.5), cls='vis2', fill='#ffffff')
    sh.circ(Xd(0), Yd(0), vd.L(P['sting_d'] / 2), cls='vis2', fill='url(#hBr)')
    sh.centre(Xd(-11), Yd(0), Xd(18), Yd(0))
    sh.hdim(Xd(-7.5), Xd(15), Yd(3.75) - 4, Yd(0) - 4, Yd(3.75) - 30, '22.5', st='P')
    sh.vdim(Yd(3.75), Yd(-3.75), Xd(-3.75), Xd(-3.75), Xd(-7.5) - 18, '7.5', st='P', side='l')
    sh.lnote(Xd(1.6), Yd(-1.9), Xd(-9), Yd(-9), 'bore Ø5 · sting Ø3.175\n≈0.9 clearance all round', st='P', anchor='start')
    sh.flow(Xd(-7.5) - 10, Yd(6) - 4, 70, label=None)
    sh.text(1415, 440, 'SECTION D–D — SHIELD (9:1)', cls='vt', anchor='middle')
    sh.line(1415 - 120, 444, 1415 + 120, 444, cls='vtu')
    sh.text(1415, 461, 'NACA 4-digit, t/c 1/3, bore at 30 % chord', cls='vs', anchor='middle')

    # ---------- view E, calibration set-up ----------
    se = 1.55
    ve = View(1290 + 14 * se, 560 + 30 * se, se)
    Xe, Ye = ve.X, ve.Y
    sh.rect(Xe(-6), Ye(30), ve.L(6), ve.L(60), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xe(0), Ye(3), ve.L(P['cell_L']), ve.L(6), cls='vis', fill='#e6ebef')
    sh.rect(Xe(-2), Ye(9), ve.L(10), ve.L(12), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xe(P['cell_L'] - 7), Ye(9), ve.L(14), ve.L(12), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xe(P['cell_L'] + 7), Ye(1.6), ve.L(80), ve.L(3.2), cls='vis2', fill='url(#hBr)')
    sh.rect(Xe(P['cell_L'] + 87), Ye(6), ve.L(14), ve.L(12), cls='vis2', fill='url(#hPLA)')
    hook_x = P['cell_L'] + 92
    sh.line(Xe(hook_x), Ye(-6), Xe(hook_x), Ye(-40), cls='thin')
    sh.path(f'M{f(Xe(hook_x-12))},{f(Ye(-40))} L{f(Xe(hook_x+12))},{f(Ye(-40))} L{f(Xe(hook_x+9))},{f(Ye(-52))} L{f(Xe(hook_x-9))},{f(Ye(-52))} Z',
            cls='vis2', fill='#ffffff')
    sh.rect(Xe(hook_x - 4), Ye(-44), ve.L(8), ve.L(8), cls='vis2', fill='#b9bec6')
    sh.line(Xe(-14), Ye(-60), Xe(170), Ye(-60), cls='vis2')
    sh.line(Xe(-6), Ye(-60), Xe(-6), Ye(30), cls='thin')
    gx = Xe(30)
    sh.a(f'<line x1="{f(gx)}" y1="{f(Ye(-14))}" x2="{f(gx)}" y2="{f(Ye(-44))}" class="ldr" marker-end="url(#aL)"/>')
    sh.text(gx + 6, Ye(-28), 'gravity = drag direction', cls='sm', anchor='start')
    sh.text(1415, 766, 'VIEW E — CALIBRATION SET-UP', cls='vt', anchor='middle')
    sh.line(1415 - 130, 770, 1415 + 130, 770, cls='vtu')
    sh.text(1415, 787, 'Schematic, NTS · module on its side (buy list §9)', cls='vs', anchor='middle')
    for i, t_ in enumerate(['Masses hang at the ball-centre height. Hang the pan', 'gently: the stops (69) catch an overload. Slope from the',
                            '2–20 g pieces; check 0.2–3 g. Preload ≈10–15 g (estimate),', 'zeroed out. Leave the 100 g piece out.']):
        sh.text(1262, 812 + i * 16, t_, cls='sm', anchor='start')
    B(sh, 74, Xe(P['cell_L'] + 94), Ye(12), 1500, 505, side='l')
    B(sh, 76, Xe(hook_x - 4), Ye(-42), 1300, 728, side='r')
    B(sh, 75, Xe(hook_x + 10), Ye(-47), 1452, 728, side='r', name='Calibration pan\nand thread')

    # ---------- view G, the two floor inserts in plan (owner's sketch, 2026-11-09) ----------
    def insert_plan(cxg, plain):
        vg = View(cxg, 884, 1.45)
        Xg, Yg = vg.X, vg.Y
        sh.rect(Xg(-INS_HL), Yg(INS_HW), vg.L(2 * INS_HL), vg.L(2 * INS_HW), cls='vis', fill='#ffffff')
        sh.rect(Xg(-INS_HL + INS_LEDGE), Yg(INS_HW - INS_LEDGE), vg.L(2 * (INS_HL - INS_LEDGE)), vg.L(2 * (INS_HW - INS_LEDGE)), cls='hid')
        for px_, py_ in ((-INS_HL + 2, INS_HW - 2), (INS_HL - 2, -INS_HW + 2)):
            sh.circ(Xg(px_), Yg(py_), 2.4, cls='vis2', fill='#3a3f47')
        sh.centre(Xg(-INS_HL - 6), Yg(0), Xg(INS_HL + 6), Yg(0))
        if plain:
            sh.text(Xg(0), Yg(0) + 16, 'no holes', cls='sm', anchor='middle')
        else:
            sh.pl([(Xg(px), Yg(py)) for px, py in teardrop(0, 0)], cls='vis2', close=True, fill='#ffffff')
            sh.circ(Xg(0), Yg(0), vg.L(2.5), cls='vis2', fill='#ffffff')
            sh.circ(Xg(0), Yg(0), vg.L(P['sting_d'] / 2), cls='vis2', fill='url(#hBr)')
        return Xg, Yg
    Xg1, Yg1 = insert_plan(380, False)
    Xg2, Yg2 = insert_plan(900, True)
    sh.flow(458, 872, 46, label=None)
    B(sh, 53, Xg1(-32), Yg1(18), 230, 850, side='l')
    B(sh, 64, Xg1(6), Yg1(-1), 230, 910, side='l')
    B(sh, 47, Xg1(INS_HL - 2), Yg1(-INS_HW + 2), 530, 912, name='Locating pin (2 per insert)')
    B(sh, 54, Xg2(32), Yg2(18), 1020, 856)
    sh.vtitle(640, 952, 'VIEW G — FLOOR INSERTS, PLAN', '60 × 70 · ledge dashed · a 1 in and a 3/4 in sphere insert (shield heights differ) and a plain one · seal on tape')

    # ---------- view H, image run (D-029), schematic ----------
    hx, hs = 855, 1.3
    hy0 = 330
    sh.rect(hx - 50, hy0, 100, 6, cls='vis2', fill='url(#hPLAk)')
    sh.rect(hx - 6, hy0 + 6, 12, 32.3 * hs, cls='vis2', fill='url(#hPLA)')
    sh.rect(hx - 2.5, hy0 + 6 + 32.3 * hs, 5, 5 * hs + 1, cls='vis2', fill='url(#hBr)')
    yb_c = hy0 + 6 + (32.3 + 5 + 12.7) * hs
    sh.circ(hx, yb_c, 12.7 * hs, cls='vis', fill='#f4f4f2')
    sh.rect(hx - 2.5, yb_c + 12.7 * hs, 5, 5 * hs, cls='vis2', fill='url(#hBr)')
    sh.rect(hx - 6, yb_c + 17.7 * hs, 12, 32.3 * hs, cls='vis2', fill='url(#hPLA)')
    sh.rect(hx - 50, yb_c + 50 * hs, 100, 6, cls='vis2', fill='url(#hPLA)')
    sh.text(hx, yb_c + 50 * hs + 30, 'VIEW H — IMAGE RUN', cls='vt', anchor='middle')
    sh.text(hx, yb_c + 50 * hs + 47, 'Run 2: dummy shield', cls='vs', anchor='middle')
    sh.text(hx, yb_c + 50 * hs + 63, 'and stub added (D-029)', cls='vs', anchor='middle')
    B(sh, 55, hx + 40, hy0 + 3, 830, 250, side='l', name='Image panel')
    B(sh, 56, hx + 6, hy0 + 30, 930, 300, side='r', name='Dummy shield')
    B(sh, 57, hx + 2.5, hy0 + 6 + 34.8 * hs, 930, 350, side='r', name='Stub (5 showing)')
    return sh
