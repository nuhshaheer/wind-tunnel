"""Sheets 7-8: test section, force balance."""
from wtsheets import *

h = P['ts'] / 2
RB = P['ball34'] / 2
RB1 = P['ball1'] / 2
SH_TOP = -RB - P['shield_gap']         # shield top (ball centre = 0)
CELL_TOP = -h - P['below_floor']       # -85
CELL_BOT = CELL_TOP - P['cell_L']      # -132


def shield_side(sh, v, x0, fill='url(#hPLA)'):
    """Sting shield in side view: rounded nose upstream, from the floor to SH_TOP."""
    X, Y = v.X, v.Y
    n0, t0 = x0 - 7.5, x0 + 15
    sh.path(f'M{f(X(n0))},{f(Y(-h))} L{f(X(n0))},{f(Y(SH_TOP - 2.5))} Q{f(X(n0))},{f(Y(SH_TOP))} {f(X(n0 + 2.5))},{f(Y(SH_TOP))} '
            f'L{f(X(t0))},{f(Y(SH_TOP))} L{f(X(t0))},{f(Y(-h))} Z', cls='vis2', fill=fill)


def teardrop(x0, y0, L=22.5, w=7.5, nose=7.5, n=40):
    """Teardrop outline in plan (x along flow), nose upstream of (x0,y0) by `nose`."""
    pts = []
    r = w / 2
    xn = x0 - nose
    for i in range(n + 1):
        a = math.pi / 2 + math.pi * i / n
        pts.append((xn + r + r * math.cos(a), y0 + r * math.sin(a)))
    pts.append((xn + L, y0))
    return pts


# =====================================================================================
def sheet_test_section():
    sh = Sheet(7, 'WT-05', 'TEST SECTION, WINDOWS AND MODEL STATION', '', 'NTS',
               ['Inside 100 × 100 (D-008). Station rules: E taps ≥ 0.5 h after the contraction; sphere ≥ 1.5√C = 150 after E; ≥ 4√S before the exit.',
                'Panels: acrylic set in a printed frame, inside face flush with the walls, foam gasket under, magnets clamp, lips locate (concept; sizes TBD).',
                'Which panels come off is TBD (“top and/or side”). Taps in a removable panel would need unplugging at each swap: open question.',
                'The M-station floor tap is offset from the sting hole (offset TBD). The probe is used only in the empty tunnel (sphere removed).',
                'No magnets near ferrous parts on the measured side of the balance; the sting is brass and screws near it are brass.',
                'Balance under the floor: sheet 8. Contraction joint J6 and flanges: sheets 6 and 10.'])
    s = 2.2
    v = View(80 - s * (C1 - 20), 330, s)
    X, Y = v.X, v.Y
    # contraction end and flange
    for s_ in (1, -1):
        yt = s_ * (h + T) if s_ > 0 else -h
        sh.rect(X(C1 - 20), Y(yt), v.L(14), v.L(T), cls='vis2', fill='url(#hPLAk)')
        y1, y2 = s_ * (h + T), s_ * (h + T + P['fl_w'])
        sh.rect(X(C1 - 6), Y(max(y1, y2)), v.L(6), v.L(P['fl_w']), cls='vis2', fill='url(#hPLAk)')
    sh.breakline(X(C1 - 20), Y(h + T + 4), Y(-h - T - 4))
    # end rings
    for xa in (C1, T1 - 12):
        sh.rect(X(xa), Y(h + 12), v.L(12), v.L(12), cls='vis2', fill='url(#hPLAk)')
    # panel frame ends and acrylic
    for xa in (C1 + 12, T1 - 26):
        sh.rect(X(xa), Y(h + 10), v.L(14), v.L(10), cls='vis2', fill='url(#hPLA)')
    for xa in (C1 + 12, T1 - 12):
        sh.rect(X(xa) - 2, Y(h + 10), 4, v.L(10), cls='vis2', fill='url(#hFoam)')
    sh.rect(X(C1 + 20), Y(h + P['acr_t']), v.L(P['ts_L'] - 40), v.L(P['acr_t']), cls='fill-acr')
    # floor with sting hole
    ft = P['floor_t']
    sh.rect(X(C1), Y(-h), v.L(XM - 2.5 - C1), v.L(ft), cls='vis2', fill='url(#hPLAk)')
    sh.rect(X(XM + 2.5), Y(-h), v.L(T1 - XM - 2.5), v.L(ft), cls='vis2', fill='url(#hPLAk)')
    # taps: floor E and M (M offset), top E and M in the panel (TBD) dashed
    for xt in (XE, XM - 30):
        sh.rect(X(xt) - 3.5, Y(-h - ft), 7, v.L(14), cls='vis2', fill='url(#hBr)')
    for xt in (XE, XM):
        sh.rect(X(xt) - 3.5, Y(h + P['acr_t'] + 14), 7, v.L(14), cls='hid')
        sh.circ(X(xt), Y(0) - 40, 4, cls='vis2', fill='url(#hBr)')
    # sphere, sting, shield
    sh.circ(X(XM), Y(0), v.L(RB1), cls='hid')
    sh.circ(X(XM), Y(0), v.L(RB), cls='vis', fill='#f4f4f2')
    shield_side(sh, v, XM)
    sh.line(X(XM) - v.L(P['sting_d'] / 2), Y(-RB - 2), X(XM) - v.L(P['sting_d'] / 2), Y(-h - ft - 12), cls='hid')
    sh.line(X(XM) + v.L(P['sting_d'] / 2), Y(-RB - 2), X(XM) + v.L(P['sting_d'] / 2), Y(-h - ft - 12), cls='hid')
    # probe (empty tunnel only), phantom
    sh.line(X(XM), Y(30), X(XM + 26), Y(30), cls='hid', extra='style="stroke:#5a6270;stroke-width:1.6"')
    sh.circ(X(XM + 28), Y(30), v.L(2.2), cls='hid')
    sh.circ(X(XM + 28), Y(30), v.L(5), cls='thin')
    sh.text(X(XM + 36), Y(30) + 4, 'probe: empty tunnel only', cls='sm', anchor='start')
    # balance box (phantom, broken)
    sh.pl([v.P(XM - 45, -h - ft), v.P(XM - 45, -h - 28)], cls='hid')
    sh.pl([v.P(XM + 45, -h - ft), v.P(XM + 45, -h - 28)], cls='hid')
    sh.text(X(XM), Y(-h - 26) + 4, 'BALANCE — SHEET 8', cls='sm', anchor='middle')
    sh.centre(X(C1 - 24), Y(0), X(T1 + 18), Y(0))
    sh.flow(X(C1 + 18), Y(26), 60)
    # dims, above
    ytop = Y(h + 12)
    yd1, yd2 = ytop - 36, ytop - 74
    for xa, xb, lab in ((C1, XE, '≥ 50'), (XE, XM, '≥ 150'), (XM, T1, '≥ 68 / 90')):
        sh.hdim(X(xa), X(xb), ytop - 4, ytop - 4, yd1, lab, st='P')
    sh.hdim(X(C1), X(T1), yd1 - 6, yd1 - 6, yd2, '270–290', st='P')
    sh.vdim(Y(h), Y(-h), X(T1), X(T1), X(T1 + 15) + 26, '100', st='F', side='r')
    sh.vdim(Y(0), Y(-h), X(XM + 40), X(XM + 40), X(XM + 58), '50', st='P', side='r')
    sh.lnote(X(C1 + 60), Y(h + P['acr_t'] / 2), X(C1 + 34), Y(h + 26), '3.2 acrylic', st='F', anchor='start')
    sh.text(X(C1 - 8), yd1 + 4, 'E', cls='sm', anchor='end')
    # callouts below
    R1, R2 = 560, 602
    B(sh, 30, X(C1 - 16), Y(-h - T), 90, R1, name='Contraction (end)')
    B(sh, 95, X(C1 - 3), Y(-h - T - P['fl_w'] + 2), 120, R2, name='Bolted flange (J6)')
    B(sh, 40, X(C1 + 6), Y(h + 12), 60, 160, side='r')
    B(sh, 41, X(C1 + 60), Y(-h - 3), 310, R1)
    B(sh, 48, X(XE), Y(-h - ft - 14), 330, R2, name='Tap station E')
    B(sh, 49, X(XM - 30), Y(-h - ft - 14), 520, R2, name='Tap station M (floor tap offset TBD)')
    B(sh, 64, X(XM + 12), Y(-35), 520, R1)
    B(sh, 60, X(XM) + 8, Y(-4), 670, R1 - 70 + 70, name='Validation sphere')
    B(sh, 52, X(T1), Y(-25), 790, R1 - 110, side='r')
    B(sh, 44, X(T1 - 20), Y(h + 10), 640, 110)
    B(sh, 42, X(C1 + 140), Y(h + P['acr_t']), 420, 110, name='Top window panel')
    B(sh, 46, X(T1 - 12), Y(h + 6), 790, 160)
    B(sh, 50, X(XM + 28) + 11, Y(30) - 3, 790, 300, name='Probe guide (position TBD)')
    sh.vtitle(X((C1 + T1) / 2) + 40, 650, 'SECTION A–A — ON CENTRE LINE', 'Flow left to right · E and M taps in the top panel drawn dashed (TBD)')

    # ---------- view B, plan ----------
    sb = 1.15
    vb = View(905 - sb * (C1 - 6), 250, sb)
    Xb, Yb = vb.X, vb.Y
    sh.rect(Xb(C1), Yb(h + 12), vb.L(P['ts_L']), vb.L(2 * h + 24), cls='vis')
    sh.rect(Xb(C1 + 12), Yb(h + 10), vb.L(P['ts_L'] - 24), vb.L(2 * h + 20), cls='vis2')
    sh.rect(Xb(C1 + 20), Yb(h + 3), vb.L(P['ts_L'] - 40), vb.L(2 * h + 6), cls='fill-acr')
    sh.rect(Xb(C1 - 6), Yb(h + T + P['fl_w']), vb.L(6), vb.L(2 * (h + T + P['fl_w'])), cls='vis2')
    sh.circ(Xb(XM), Yb(0), vb.L(RB), cls='vis2', fill='#f4f4f2')
    sh.pl([(Xb(px), Yb(py)) for px, py in teardrop(XM, 0)], cls='hid', close=True)
    for mx, my in ((C1 + 19, h + 6), (T1 - 19, h + 6), (C1 + 19, -h - 6), (T1 - 19, -h - 6)):
        sh.circ(Xb(mx), Yb(my), vb.L(4), cls='vis2', fill='#3a3f47')
    for xt in (XE, XM):
        for s_ in (1, -1):
            y0, y1 = s_ * (h + 12), s_ * (h + 24)
            sh.rect(Xb(xt) - 1.8, Yb(max(y0, y1)), 3.6, vb.L(12), cls='vis2', fill='url(#hBr)')
    sh.rect(Xb(XM + 22), Yb(h + 26), vb.L(12), vb.L(14), cls='vis2', fill='url(#hPLA)')
    sh.centre(Xb(C1 - 10), Yb(0), Xb(T1 + 10), Yb(0))
    sh.flow(Xb(C1 + 30), Yb(-30), 50, label=None)
    sh.hdim(Xb(C1 + 12), Xb(T1 - 12), Yb(-h - 10) + 4, Yb(-h - 10) + 4, Yb(-h - 12) + 30, 'panel ≈300 × 120 (TBD)', st='T')
    sh.text(Xb((C1 + T1) / 2), 100, 'VIEW B — PLAN (TOP)', cls='vt', anchor='middle')
    sh.text(Xb((C1 + T1) / 2), 118, 'Far side up; acrylic shown clear', cls='vs', anchor='middle')
    B(sh, 45, Xb(T1 - 19) + 4, Yb(h + 6) - 3, 1330, 150, name='Magnet (8 × 2), 4 shown')
    B(sh, 50, Xb(XM + 28), Yb(h + 26), 1330, 196, name='Probe guide')
    B(sh, 48, Xb(XE), Yb(-h - 24), 1330, 300, name='Tap station E (side taps)')
    B(sh, 49, Xb(XM), Yb(-h - 24), 1330, 344, name='Tap station M (side taps)')

    # ---------- section C-C at the model station (looking downstream) ----------
    sc = 2.4
    vc = View(1095, 660, sc)
    Xc, Yc = vc.X, vc.Y
    # floor
    sh.rect(Xc(-70), Yc(-h), vc.L(140), vc.L(ft), cls='vis2', fill='url(#hPLAk)')
    sh.rect(Xc(-2.5), Yc(-h), vc.L(5), vc.L(ft), cls='vis2', fill='#ffffff')
    # far wall (left, fixed) with rail and lip
    sh.pl([(Xc(-58), Yc(-h)), (Xc(-58), Yc(40)), (Xc(-66), Yc(40)), (Xc(-66), Yc(46.8)), (Xc(-53), Yc(46.8)), (Xc(-53), Yc(50)),
           (Xc(-50), Yc(50)), (Xc(-50), Yc(-h))], cls='vis2', close=True, fill='url(#hPLAk)')
    # near side: acrylic window between top rail and floor rail
    sh.pl([(Xc(66), Yc(40)), (Xc(66), Yc(46.8)), (Xc(53), Yc(46.8)), (Xc(53), Yc(50)), (Xc(50), Yc(50)), (Xc(50), Yc(40))],
          cls='vis2', close=True, fill='url(#hPLAk)')
    sh.rect(Xc(50), Yc(40), vc.L(P['acr_t']), vc.L(40 + h), cls='fill-acr')
    sh.rect(Xc(53.2), Yc(40), vc.L(4.8), vc.L(40 + h), cls='vis2', fill='url(#hPLA)')
    # top panel: frame members, gasket, magnets, acrylic
    for s_ in (1, -1):
        sh.pl([(Xc(s_ * 53), Yc(50)), (Xc(s_ * 53), Yc(60)), (Xc(s_ * 68), Yc(60)), (Xc(s_ * 68), Yc(50)), (Xc(s_ * 57), Yc(50)),
               (Xc(s_ * 57), Yc(53.2)), (Xc(s_ * 53), Yc(53.2))], cls='vis2', close=True, fill='url(#hPLA)')
        sh.rect(Xc(min(s_ * 56, s_ * 65)), Yc(50), vc.L(9), vc.L(3.2), cls='vis2', fill='url(#hFoam)')
        sh.rect(Xc(min(s_ * 57, s_ * 65)), Yc(53.6 + 2), vc.L(8), vc.L(2), cls='fill-neo')
        sh.rect(Xc(min(s_ * 57, s_ * 65)), Yc(46.0 - 0.8), vc.L(8), vc.L(2), cls='fill-neo')
    sh.rect(Xc(-57), Yc(50 + P['acr_t']), vc.L(114), vc.L(P['acr_t']), cls='fill-acr')
    # sphere, sting, shield
    sh.circ(Xc(0), Yc(0), vc.L(RB1), cls='hid')
    sh.circ(Xc(0), Yc(0), vc.L(RB), cls='vis', fill='#f4f4f2')
    sh.rect(Xc(-3.75), Yc(SH_TOP), vc.L(7.5), vc.L(SH_TOP + h), cls='vis2', fill='url(#hPLA)')
    sh.rect(Xc(-2.5), Yc(SH_TOP), vc.L(5), vc.L(SH_TOP + h), cls='vis2', fill='#ffffff')
    sh.rect(Xc(-P['sting_d'] / 2), Yc(-RB + 1), vc.L(P['sting_d']), vc.L(-RB + 1 + h + ft + 10), cls='vis2', fill='url(#hBr)')
    # M taps: far wall stub, floor tap offset (not in this section), top and near TBD (dashed)
    sh.rect(Xc(-70), Yc(1.6), vc.L(12), vc.L(3.2), cls='vis2', fill='url(#hBr)')
    sh.rect(Xc(58), Yc(1.6), vc.L(12), vc.L(3.2), cls='hid')
    sh.rect(Xc(-1.6), Yc(72), vc.L(3.2), vc.L(12), cls='hid')
    sh.pl([(Xc(-45), Yc(-h - ft)), (Xc(-45), Yc(-h - 20))], cls='hid')
    sh.pl([(Xc(45), Yc(-h - ft)), (Xc(45), Yc(-h - 20))], cls='hid')
    sh.centre(Xc(-78), Yc(0), Xc(78), Yc(0))
    sh.centre(Xc(0), Yc(80), Xc(0), Yc(-h - 22))
    sh.flow(Xc(-30), Yc(-30), d='d', label=None)
    sh.hdim(Xc(-50), Xc(50), Yc(-h - ft) + 4, Yc(-h - ft) + 4, Yc(-h - ft) + 34, '100', st='F')
    sh.vdim(Yc(h), Yc(-h), Xc(-58), Xc(-58), Xc(-70) - 34, '100', st='F', side='l')
    sh.hdim(Xc(-3.75), Xc(3.75), Yc(-30), Yc(-30), Yc(-38), '7.5', st='P', tx=Xc(3.75) + 22)
    sh.vdim(Yc(-RB), Yc(SH_TOP), Xc(3.75), Xc(3.75), Xc(14), '5', st='P', side='r')
    sh.lnote(Xc(RB * 0.7), Yc(RB * 0.7), Xc(26), Yc(28), 'Ø19.05 (3/4 in) · Ø25.4 dashed', st='F', anchor='start')
    sh.detail_circle(Xc(60), Yc(52), 17, 'F')
    sh.text(1095, 905, 'SECTION C–C — AT THE MODEL STATION', cls='vt', anchor='middle')
    sh.line(1095 - 150, 909, 1095 + 150, 909, cls='vtu')
    sh.text(1095, 926, 'Looking downstream; far wall left, near window right (fixed or removable TBD)', cls='vs', anchor='middle')
    B(sh, 43, Xc(51.6), Yc(-10), 1330, 640, name='Side window panel')
    B(sh, 41, Xc(40), Yc(-h - 3), 1330, 760)
    B(sh, 64, Xc(3.75), Yc(-35), 1330, 700)
    B(sh, 63, Xc(0), Yc(-h - ft - 6), 1330, 812)
    B(sh, 49, Xc(-66), Yc(0), 900, 590, side='l', name='Tap station M')
    B(sh, 40, Xc(-62), Yc(43), 900, 520, side='l', name='Test-section frame')
    B(sh, 47, Xc(-51.5), Yc(48.5), 900, 470, side='l', name='Locating lip')

    # ---------- detail F, panel edge 10:1 ----------
    sf = 10
    vf = View(150 - sf * 46, 965 - sf * 40, sf)
    Xf, Yf = vf.X, vf.Y
    sh.pl([(Xf(46), Yf(40)), (Xf(66), Yf(40)), (Xf(66), Yf(46.8)), (Xf(53), Yf(46.8)), (Xf(53), Yf(50)), (Xf(50), Yf(50)),
           (Xf(50), Yf(40))], cls='vis2', close=True, fill='url(#hPLAk)')
    sh.rect(Xf(46), Yf(40), vf.L(4), vf.L(0.01), cls='thin')
    sh.pl([(Xf(53), Yf(50)), (Xf(53), Yf(60)), (Xf(68), Yf(60)), (Xf(68), Yf(50)), (Xf(57), Yf(50)), (Xf(57), Yf(53.2)), (Xf(53), Yf(53.2))],
          cls='vis2', close=True, fill='url(#hPLA)')
    sh.rect(Xf(56), Yf(50), vf.L(9), vf.L(3.2), cls='vis2', fill='url(#hFoam)')
    sh.rect(Xf(57), Yf(55.6), vf.L(8), vf.L(2), cls='fill-neo')
    sh.rect(Xf(57), Yf(46.0 - 0.8), vf.L(8), vf.L(2), cls='fill-neo')
    sh.rect(Xf(46), Yf(50 + P['acr_t']), vf.L(11), vf.L(P['acr_t']), cls='fill-acr')
    sh.breakline(Xf(46), Yf(54), Yf(49.5))
    sh.line(Xf(44), Yf(50), Xf(70), Yf(50), cls='ctr')
    sh.text(Xf(44) - 4, Yf(50) + 4, 'inside face', cls='sm', anchor='end')
    sh.vdim(Yf(50 + P['acr_t']), Yf(50), Xf(48), Xf(48), Xf(48), '', st='F', ext=False)
    sh.bgtext(Xf(47), Yf(51.6) + 4, '3.2', st='F', anchor='end')
    sh.vdim(Yf(53.2), Yf(50), Xf(65), Xf(65), Xf(70), '3.2 gasket', st='P', side='r')
    sh.hdim(Xf(57), Xf(65), Yf(57.6) - 3, Yf(57.6) - 3, Yf(60) - 14, '8', st='F', tx=Xf(61), ty=Yf(60) - 19)
    sh.lnote(Xf(64), Yf(56.6), Xf(70), Yf(58.5), 'magnet 8 × 2; pocket Ø8.2–8.3 × 2.2', st='F', anchor='start')
    sh.lnote(Xf(64), Yf(45.6), Xf(70), Yf(43), 'skin over magnet: TBD', st='T', anchor='start')
    sh.lnote(Xf(52), Yf(50.05), Xf(54), Yf(38.5), 'flush: no step', st='P', anchor='start')
    sh.text(Xf(57), 690, 'DETAIL F — PANEL EDGE (10:1, CONCEPT)', cls='vt', anchor='middle')
    sh.line(Xf(57) - 150, 694, Xf(57) + 150, 694, cls='vtu')
    sh.text(Xf(57), 711, 'Features from the docs; all section sizes TBD at sizing', cls='vs', anchor='middle')
    B(sh, 42, Xf(48), Yf(52.4), 110, 760, side='r', name='Top window panel')
    B(sh, 44, Xf(66), Yf(59), 560, 740)
    B(sh, 45, Xf(61), Yf(46.4), 560, 960, name='Magnet (pair)')
    B(sh, 46, Xf(58), Yf(51.6), 700, 960, name='Foam gasket tape')
    B(sh, 47, Xf(51.5), Yf(48.5), 110, 960, side='r', name='Locating lip')
    return sh


# =====================================================================================
def sheet_balance():
    sh = Sheet(8, 'WT-06', 'FORCE BALANCE: SPHERE, STING, SHIELD AND LOAD CELL', '', 'NTS',
               ['The cell stands upright under the ball; the sting is clamped only to its top end, the bottom end to the base; screws along the wind.',
                'Nothing touches the bar between its end blocks. Hold and clamp the cell only by its end blocks; short screws.',
                'Lock the sting (68) before touching the ball, sting or shield; stops (69) catch it at ≈120 g, below the 150 g safe limit.',
                'The shield is fixed to the floor and never touches the sting: tap it with the wind off; the reading must not change.',
                'Balls are press-fit on their stems (acetal cannot be glued): Ø3.0–3.1 hole drilled to the centre with a printed jig.',
                'Sensitive axis assumed across the 12 mm face (TAL221 notes): confirm on the delivered cell with a known mass.'])
    s = 3.4
    v = View(380 - s * XM, 210, s)
    X, Y = v.X, v.Y
    ft = P['floor_t']
    # floor
    sh.rect(X(XM - 62), Y(-h), v.L(62 - 4), v.L(ft), cls='vis2', fill='url(#hPLAk)')
    sh.rect(X(XM + 4), Y(-h), v.L(58), v.L(ft), cls='vis2', fill='url(#hPLAk)')
    sh.breakline(X(XM - 62), Y(-h + 3), Y(-h - ft - 3))
    sh.breakline(X(XM + 62), Y(-h + 3), Y(-h - ft - 3))
    # shield (cut) with bore
    sh_x0 = XM
    sh.path(f'M{f(X(XM-7.5))},{f(Y(-h))} L{f(X(XM-7.5))},{f(Y(SH_TOP-2.5))} Q{f(X(XM-7.5))},{f(Y(SH_TOP))} {f(X(XM-5))},{f(Y(SH_TOP))} '
            f'L{f(X(XM-2.5))},{f(Y(SH_TOP))} L{f(X(XM-2.5))},{f(Y(-h))} Z', cls='vis2', fill='url(#hPLA)')
    sh.path(f'M{f(X(XM+2.5))},{f(Y(-h))} L{f(X(XM+2.5))},{f(Y(SH_TOP))} L{f(X(XM+15))},{f(Y(SH_TOP))} L{f(X(XM+15))},{f(Y(-h))} Z', cls='vis2', fill='url(#hPLA)')
    # ball (cut) with drilled hole and stem
    sh.circ(X(XM), Y(0), v.L(RB1), cls='hid')
    sh.a(f'<circle cx="{f(X(XM))}" cy="{f(Y(0))}" r="{f(v.L(RB))}" class="vis" style="fill:url(#hPETG)"/>')
    sh.rect(X(XM - 1.55), Y(0), v.L(3.1), v.L(RB), cls='vis2', fill='#ffffff')
    stem_bot = -26
    sh.rect(X(XM - P['sting_d'] / 2), Y(0), v.L(P['sting_d']), v.L(-stem_bot), cls='vis2', fill='url(#hBr)')
    # sleeve
    sl_top, sl_bot = -12, -30
    sh.rect(X(XM - P['sleeve_d'] / 2), Y(sl_top), v.L(P['sleeve_d']), v.L(sl_top - sl_bot), cls='vis2', fill='url(#hBr)')
    sh.rect(X(XM - P['sting_d'] / 2), Y(sl_top), v.L(P['sting_d']), v.L(sl_top - stem_bot), cls='vis2', fill='url(#hBr)')
    # sting
    sh.rect(X(XM - P['sting_d'] / 2), Y(sl_bot + 4), v.L(P['sting_d']), v.L(sl_bot + 4 - (CELL_TOP + 4)), cls='vis2', fill='url(#hBr)')
    # under floor: stops, lock
    for xs_, w in ((XM - 9, 6), (XM + 3, 6)):
        sh.rect(X(xs_), Y(-h - ft - 2), v.L(w), v.L(7), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 16), Y(-h - ft - 13), v.L(14.4), v.L(6), cls='vis2', fill='url(#hPETG)')
    sh.line(X(XM - 22), Y(-h - ft - 16), X(XM - 2.5), Y(-h - ft - 16), cls='vis2')
    sh.circ(X(XM - 22), Y(-h - ft - 16), 4, cls='vis2', fill='#ffffff')
    # clamp, cell, base, plate, box
    sh.rect(X(XM - 7), Y(CELL_TOP + 7), v.L(14), v.L(14), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 3), Y(CELL_TOP), v.L(6), v.L(P['cell_L']), cls='vis', fill='url(#hAl)')
    sh.rect(X(XM - 2.2), Y(CELL_TOP - 12), v.L(4.4), v.L(P['cell_L'] - 24), cls='hid')
    yb0 = CELL_BOT + 10
    sh.rect(X(XM - 7), Y(yb0), v.L(14), v.L(yb0 - (-144)), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 42), Y(-144), v.L(84), v.L(6), cls='vis2', fill='url(#hPETG)')
    sh.rect(X(XM - 45), Y(-h - ft), v.L(90), v.L(-h - ft + 158), cls='vis2')
    sh.rect(X(XM - 42), Y(-h - ft), v.L(84), v.L(-h - ft + 155), cls='thin')
    sh.rect(X(XM + 16), Y(-141), v.L(24), v.L(3), cls='fill-pcb')
    for yy in (CELL_TOP - 3.5, CELL_TOP - 3.5 - P['cell_hole']):
        sh.line(X(XM - 7), Y(yy), X(XM + 9), Y(yy), cls='hid')
        sh.rect(X(XM + 7), Y(yy + 2.5), v.L(2), v.L(5), cls='vis2', fill='url(#hBr)')
    sh.path(f'M{f(X(XM+3))},{f(Y(CELL_TOP-20))} C{f(X(XM+14))},{f(Y(CELL_TOP-26))} {f(X(XM+20))},{f(Y(-120))} {f(X(XM+24))},{f(Y(-138))}', cls='thin',
            extra='style="stroke:#a33;stroke-width:1.2;fill:none"')
    sh.centre(X(XM), Y(RB1 + 8), X(XM), Y(-162))
    sh.centre(X(XM - 20), Y(0), X(XM + 20), Y(0))
    sh.flow(X(XM - 60), Y(14), 60)
    # dims (left side)
    xl = X(XM - 62)
    sh.vdim(Y(0), Y(-h), X(XM - 10), X(XM - 62), xl - 30, '50', st='P', side='l')
    sh.vdim(Y(-h), Y(CELL_TOP), X(XM - 62), X(XM - 7), xl - 30, '30–40', st='P', side='l')
    sh.vdim(Y(0), Y(CELL_TOP), X(XM - 10), X(XM - 7), xl - 80, '80–90\n(sting)', st='P', side='l')
    sh.vdim(Y(CELL_TOP), Y(CELL_BOT), X(XM - 3), X(XM - 7), xl - 30, '47', st='F', side='l')
    sh.vdim(Y(CELL_TOP - 3.5), Y(CELL_TOP - 3.5 - P['cell_hole']), X(XM + 9), X(XM + 9), X(XM + 30), '40', st='F', side='r')
    sh.hdim(X(XM - 3), X(XM + 3), Y(CELL_BOT) + 4, Y(CELL_BOT) + 4, Y(CELL_BOT) + 26, '6', st='F', tx=X(XM + 3) + 18)
    # dims (right side, top)
    sh.vdim(Y(-RB), Y(SH_TOP), X(XM + 15), X(XM + 15), X(XM + 26), '5', st='P', side='r')
    sh.vdim(Y(SH_TOP), Y(-h), X(XM + 15), X(XM + 15), X(XM + 26), '≈35', st='P', side='r')
    sh.hdim(X(XM - 7.5), X(XM + 15), Y(SH_TOP) - 4, Y(SH_TOP) - 4, Y(SH_TOP) - 1, '', st='P', ext=False)
    sh.lnote(X(XM + 1), Y(-RB / 2), X(XM + 20), Y(10), 'Ø3.0–3.1 × 9.5 deep (12.7 for 1 in)', st='P', anchor='start')
    sh.lnote(X(XM + RB * 0.7), Y(RB * 0.7), X(XM + 20), Y(20), 'Ø19.05 · Ø25.4 dashed', st='F', anchor='start')
    sh.lnote(X(XM + 6), Y(-h - ft - 1), X(XM + 24), Y(-h - ft - 4) + 0, 'stop gap TBD (set at ≈120 g)', st='T', anchor='start')
    sh.lnote(X(XM + 45), Y(-152), X(XM + 50), Y(-163), 'box TBD', st='T', anchor='start')
    sh.vtitle(X(XM), Y(-158) + 50, 'VIEW A — SIDE SECTION ON CENTRE LINE', 'Wind left to right · 3/4 in ball shown, 1 in dashed')
    # callouts (left column)
    cl = 70
    B(sh, 60, X(XM - RB * 0.7), Y(RB * 0.7), cl, Y(14) - 10)
    B(sh, 61, X(XM - 1.4), Y(-6), cl, Y(-2) + 18)
    B(sh, 62, X(XM - 2), Y(-20), cl, Y(-20) + 10)
    B(sh, 64, X(XM - 6), Y(-38), cl, Y(-36) + 4)
    B(sh, 41, X(XM - 40), Y(-h - 3), cl, Y(-h) + 8)
    B(sh, 69, X(XM - 7), Y(-h - ft - 5), cl, Y(-h - ft - 5) + 26)
    B(sh, 68, X(XM - 12), Y(-h - ft - 13), cl, Y(-h - ft - 13) + 44)
    B(sh, 63, X(XM - 1.6), Y(-75), cl, Y(-75) + 40)
    B(sh, 65, X(XM - 7), Y(CELL_TOP + 2), cl, Y(CELL_TOP) + 54)
    B(sh, 66, X(XM - 3), Y(CELL_TOP - 25), cl, Y(CELL_TOP - 25) + 56)
    # callouts (right)
    cr_ = 640
    B(sh, 73, X(XM + 8), Y(CELL_TOP - 3.5), cr_, Y(CELL_TOP - 3.5) - 18, name='Brass M3 screw (2 per end)')
    B(sh, 72, X(XM + 30), Y(-139), cr_, Y(-139) - 40, name='HX711 amplifier board')
    B(sh, 67, X(XM + 7), Y(-130), cr_, Y(-130) - 34)
    B(sh, 70, X(XM + 40), Y(-144), cr_, Y(-144) + 10)
    B(sh, 71, X(XM + 45), Y(-100), cr_, Y(-100) - 30)

    # ---------- view B, front (looking downstream) ----------
    vb = View(1000, 210, s)
    Xb, Yb = vb.X, vb.Y
    sh.rect(Xb(-40), Yb(-h), vb.L(80), vb.L(ft), cls='vis2')
    sh.breakline(Xb(-40), Yb(-h + 3), Yb(-h - ft - 3))
    sh.breakline(Xb(40), Yb(-h + 3), Yb(-h - ft - 3))
    sh.rect(Xb(-3.75), Yb(SH_TOP), vb.L(7.5), vb.L(SH_TOP + h), cls='vis2')
    sh.circ(Xb(0), Yb(0), vb.L(RB1), cls='hid')
    sh.circ(Xb(0), Yb(0), vb.L(RB), cls='vis', fill='#f4f4f2')
    sh.line(Xb(-P['sting_d'] / 2), Yb(-RB), Xb(-P['sting_d'] / 2), Yb(SH_TOP), cls='vis2')
    sh.line(Xb(P['sting_d'] / 2), Yb(-RB), Xb(P['sting_d'] / 2), Yb(SH_TOP), cls='vis2')
    sh.rect(Xb(-P['sting_d'] / 2), Yb(-h - ft), vb.L(P['sting_d']), vb.L(CELL_TOP + 7 - (-h - ft)) * -1 if False else vb.L((-h - ft) - (CELL_TOP + 7)), cls='vis2', fill='url(#hBr)')
    sh.rect(Xb(-9), Yb(CELL_TOP + 7), vb.L(18), vb.L(14), cls='vis2')
    sh.rect(Xb(-6), Yb(CELL_TOP), vb.L(12), vb.L(P['cell_L']), cls='vis', fill='#e6ebef')
    for yy in (CELL_TOP - 3.5, CELL_TOP - 3.5 - P['cell_hole']):
        for xx in (-3, 3):
            sh.circ(Xb(xx), Yb(yy), vb.L(1.6), cls='vis2', fill='#ffffff')
    sh.rect(Xb(-9), Yb(yb0), vb.L(18), vb.L(yb0 + 144), cls='vis2')
    sh.rect(Xb(-42), Yb(-144), vb.L(84), vb.L(6), cls='vis2')
    sh.rect(Xb(-45), Yb(-h - ft), vb.L(90), vb.L(-h - ft + 158), cls='vis2')
    sh.centre(Xb(0), Yb(RB1 + 8), Xb(0), Yb(-162))
    sh.flow(Xb(-30), Yb(14), d='d', label=None)
    sh.hdim(Xb(-6), Xb(6), Yb(CELL_BOT) + 4, Yb(CELL_BOT) + 4, Yb(CELL_BOT) + 26, '12', st='F', tx=Xb(6) + 24)
    sh.hdim(Xb(-3), Xb(3), Yb(CELL_TOP - 3.5) - 4, Yb(CELL_TOP - 3.5) - 4, Yb(CELL_TOP) - 30, '6', st='F', tx=Xb(3) + 18, ty=Yb(CELL_TOP) - 34)
    sh.hdim(Xb(-3.75), Xb(3.75), Yb(-h) - 4, Yb(-h) - 4, Yb(-30), '7.5', st='P', tx=Xb(3.75) + 26)
    sh.vtitle(1000, Yb(-158) + 50, 'VIEW B — FRONT', 'Looking downstream')
    B(sh, 66, Xb(-6), Yb(CELL_TOP - 30), 820, Yb(CELL_TOP - 30) + 30, side='r', name='Load cell (12 mm face)')
    B(sh, 80, Xb(-3), Yb(CELL_TOP - 3.5), 820, Yb(CELL_TOP) - 40, side='r', name='') if False else None

    # ---------- section D-D through the shield ----------
    vd = View(1290, 300, 9)
    Xd, Yd = vd.X, vd.Y
    sh.pl([(Xd(px), Yd(py)) for px, py in teardrop(0, 0)], cls='vis2', close=True, fill='url(#hPLA)')
    sh.circ(Xd(0), Yd(0), vd.L(2.5), cls='vis2', fill='#ffffff')
    sh.circ(Xd(0), Yd(0), vd.L(P['sting_d'] / 2), cls='vis2', fill='url(#hBr)')
    sh.centre(Xd(-12), Yd(0), Xd(19), Yd(0))
    sh.hdim(Xd(-7.5), Xd(15), Yd(3.75) - 4, Yd(0) - 4, Yd(3.75) - 30, '20–25', st='P')
    sh.vdim(Yd(3.75), Yd(-3.75), Xd(-3.75), Xd(-3.75), Xd(-7.5) - 22, '7.5', st='P', side='l')
    sh.lnote(Xd(1.8), Yd(-1.8), Xd(6), Yd(-8), 'bore Ø5 · sting Ø3.175 · ≈0.9 all round', st='P', anchor='start')
    sh.flow(Xd(-7.5) - 10, Yd(-6) + 30, 70)
    sh.text(1300, 420, 'SECTION D–D — THROUGH THE SHIELD (9:1)', cls='vt', anchor='middle')
    sh.line(1300 - 160, 424, 1300 + 160, 424, cls='vtu')
    sh.text(1300, 441, 'Teardrop or airfoil; rounded nose into the wind', cls='vs', anchor='middle')

    # ---------- view E, calibration set-up (schematic) ----------
    ve = View(1110, 640, 2.2)
    Xe, Ye = ve.X, ve.Y
    sh.rect(Xe(-6), Ye(30), ve.L(6), ve.L(60), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xe(0), Ye(3), ve.L(P['cell_L']), ve.L(6), cls='vis', fill='#e6ebef')
    sh.rect(Xe(-2), Ye(9), ve.L(10), ve.L(12), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xe(P['cell_L'] - 7), Ye(9), ve.L(14), ve.L(12), cls='vis2', fill='url(#hPETG)')
    sh.rect(Xe(P['cell_L'] + 7), Ye(1.6), ve.L(80), ve.L(3.2), cls='vis2', fill='url(#hBr)')
    sh.rect(Xe(P['cell_L'] + 87), Ye(6), ve.L(14), ve.L(12), cls='vis2', fill='url(#hPLA)')
    hook_x = P['cell_L'] + 92
    sh.line(Xe(hook_x), Ye(-6), Xe(hook_x), Ye(-40), cls='thin')
    sh.path(f'M{f(Xe(hook_x-12))},{f(Ye(-40))} L{f(Xe(hook_x+12))},{f(Ye(-40))} L{f(Xe(hook_x+9))},{f(Ye(-52))} L{f(Xe(hook_x-9))},{f(Ye(-52))} Z', cls='vis2', fill='#ffffff')
    sh.rect(Xe(hook_x - 4), Ye(-44), ve.L(8), ve.L(8), cls='vis2', fill='#b9bec6')
    sh.line(Xe(-14), Ye(-60), Xe(170), Ye(-60), cls='vis2')
    sh.line(Xe(-6), Ye(-60), Xe(-6), Ye(30), cls='thin')
    sh.a(f'<line x1="{f(Xe(hook_x)+40)}" y1="{f(Ye(0))}" x2="{f(Xe(hook_x)+40)}" y2="{f(Ye(-30))}" class="ldr" marker-end="url(#aL)"/>')
    sh.text(Xe(hook_x) + 46, Ye(-12), 'g = drag direction', cls='sm', anchor='start')
    sh.text(1290, 790, 'VIEW E — CALIBRATION SET-UP (SCHEMATIC, NTS)', cls='vt', anchor='middle')
    sh.line(1290 - 190, 794, 1290 + 190, 794, cls='vtu')
    sh.text(1290, 811, 'Balance module on its side; masses hang at the ball-centre height (buy list §9)', cls='vs', anchor='middle')
    sh.text(1060, 836, 'Lock the sting while hanging the pan; unlock to read. Slope from the 2–20 g pieces, check 0.2–3 g.', cls='sm', anchor='start')
    sh.text(1060, 852, 'Preload of sting, sleeve, attachment and pan ≈10–15 g (estimate), zeroed out. Leave the 100 g piece out.', cls='sm', anchor='start')
    B(sh, 74, Xe(P['cell_L'] + 94), Ye(6), 1180, 520, side='r')
    B(sh, 75, Xe(hook_x + 9), Ye(-46), 1430, 700, side='u')
    B(sh, 76, Xe(hook_x), Ye(-40), 1460, 600, side='r')
    return sh
