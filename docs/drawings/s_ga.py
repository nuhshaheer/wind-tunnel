"""Sheets 1 and 2: general arrangement."""
from wtsheets import *


def draw_tunnel_side(sh, v, detail=True):
    """Side elevation, section on the centre line. Returns key positions."""
    X, Y = v.X, v.Y
    cr = P['collar_D'] / 2
    # fan (outside view)
    sh.rect(X(0), Y(cr), v.L(P['collar_L']), v.L(2 * cr), cls='vis2')
    sh.rect(X(P['collar_L']), Y(P['fan_H'] / 2), v.L(P['fan_L'] - 2 * P['collar_L']), v.L(P['fan_H']), cls='vis', rx=14)
    sh.rect(X(P['fan_L'] - P['collar_L']), Y(cr), v.L(P['collar_L'] - P['sock_depth']), v.L(2 * cr), cls='vis2')
    sh.line(X(110), Y(P['fan_H'] / 2), X(110), Y(-P['fan_H'] / 2), cls='thin')
    sh.line(X(210), Y(P['fan_H'] / 2), X(210), Y(-P['fan_H'] / 2), cls='thin')
    # inlet guard
    sh.rect(X(-14), Y(cr + 6), v.L(8), v.L(2 * cr + 12), cls='vis2')
    for k in range(-5, 6):
        sh.line(X(-14), Y(k * 13), X(-6), Y(k * 13), cls='thin')
    # stand and feet
    sh.rect(X(70), Y(-P['fan_H'] / 2 + 6), v.L(180), v.L(150 - P['fan_H'] / 2 + 6), cls='vis2')
    sh.text(X(160), Y(-131), 'CRADLE', cls='sm', anchor='middle')
    for fx in (80, 218):
        sh.rect(X(fx), Y(-150), v.L(22), v.L(25), cls='fill-neo')
    # socket (section) with collar and neoprene inside
    for s in (1, -1):
        y_top = s * (RS + P['sock_wall']) if s > 0 else -RS
        sh.rect(X(SOCK0), Y(y_top), v.L(P['sock_depth']), v.L(P['sock_wall']), fill='url(#hPLA)', cls='vis2')
        yo = cr + P['wrap_t'] if s > 0 else -cr
        sh.rect(X(SOCK0), Y(yo), v.L(P['sock_depth']), v.L(P['wrap_t']), cls='fill-neo')
        sh.line(X(SOCK0), Y(s * cr), X(D0), Y(s * cr), cls='vis2')
    # duct walls
    for xa, xb in ((D0, D1), (D1, C0), (C0, C1)):
        for top in (True, False):
            sh.pl(wall_poly(v, xa, xb, top), cls='fill-wall', close=True)
    # flanges / joints
    for xj in (D0, D1, HC0, SC1, SC2, C0, C1):
        r = r_in(xj - 0.01) if xj != D0 else RS
        r2 = r_in(xj + 0.01) if xj != C1 else P['ts'] / 2
        rr = max(r, r2) + T + P['fl_w']
        for s in (1, -1):
            for xa, xb, ri in ((xj - P['fl_t'], xj, r), (xj, xj + P['fl_t'], r2)):
                if xj == C1 and xa >= xj:
                    continue
                y1, y2 = s * (ri + T), s * rr
                sh.rect(X(xa), Y(max(y1, y2)), v.L(xb - xa), v.L(abs(y2 - y1)), cls='fill-wall')
    # screens
    for xs_, tag, opt in ((D0, '12a', False), ((D0 + D1) / 2, '12b', True), (D1, '12c', False), (SC1, '12d', False), (SC2, '12e', False)):
        r = r_in(xs_)
        sh.line(X(xs_), Y(r), X(xs_), Y(-r), cls='hid' if opt else 'scr')
        left = tag == '12c'
        sh.text(X(xs_) + (-4 if left else 4), Y(-r) - 6, tag, cls='sm', anchor='end' if left else 'start')
    # honeycomb
    sh.rect(X(HC0), Y(HALF), v.L(P['hc_L']), v.L(2 * HALF), cls='vis2', fill='#ffffff')
    k = -HALF + 6
    while k < HALF:
        sh.line(X(HC0), Y(k), X(HC1), Y(k), cls='thin')
        k += 6
    # S taps (top and bottom walls) and mist port
    xs_tap = XS_TAP
    for s in (1, -1):
        ytop = HALF + T + 12 if s > 0 else -HALF
        sh.rect(X(xs_tap) - 2, Y(ytop), 4, v.L(12 + T), cls='vis2', fill='url(#hBr)')
    xmist = XMIST
    sh.rect(X(xmist - 8), Y(HALF + T + 20), v.L(16), v.L(20), cls='vis2', fill='url(#hPLA)')
    sh.rect(X(xmist - 10), Y(HALF + T + 26), v.L(20), v.L(6), cls='vis2', fill='#ffffff')
    # test section
    h = P['ts'] / 2
    for xa in (C1, T1 - 12):
        sh.rect(X(xa), Y(h + 12), v.L(12), v.L(12), fill='url(#hPLAk)', cls='vis2')
    for xa in (C1 + 12, T1 - 26):
        sh.rect(X(xa), Y(h + 10), v.L(14), v.L(10), fill='url(#hPLA)', cls='vis2')
    sh.rect(X(C1 + 20), Y(h + P['acr_t']), v.L(P['ts_L'] - 40), v.L(P['acr_t']), cls='fill-acr')
    ft = P['floor_t']
    floor_run(sh, X, Y, C1, T1, XM - INS_HL, XM + INS_HL, -h, ft, hole=(XM - 2.5, XM + 2.5))
    for xt in (XE, XM - 30):
        sh.rect(X(xt) - 2, Y(-h - ft), 4, v.L(12), cls='vis2', fill='url(#hBr)')
    rb = P['ball34'] / 2
    sh.circ(X(XM), Y(0), v.L(P['ball1'] / 2), cls='hid')
    sh.circ(X(XM), Y(0), v.L(rb), cls='vis', fill='#f4f4f2')
    sh.line(X(XM), Y(-rb), X(XM), Y(-78), cls='vis2')
    st_ = -rb - P['shield_gap']
    sh.path(f'M{f(X(XM-7.5))},{f(Y(-h))} L{f(X(XM-7.5))},{f(Y(st_-3))} Q{f(X(XM-7.5))},{f(Y(st_))} {f(X(XM-4))},{f(Y(st_))} '
            f'L{f(X(XM+15))},{f(Y(st_))} L{f(X(XM+15))},{f(Y(-h))} Z', cls='vis2', fill='url(#hPLA)')
    bx0, bx1, by0, by1 = XM - 45, XM + 45, -h - ft, -158
    sh.rect(X(bx0), Y(by0), v.L(bx1 - bx0), v.L(by0 - by1), cls='vis2')
    sh.rect(X(bx0 + 3), Y(by0), v.L(bx1 - bx0 - 6), v.L(by0 - by1 - 3), cls='thin')
    sh.rect(X(bx0 + 4), Y(-149), v.L(bx1 - bx0 - 8), v.L(6), fill='url(#hPETG)', cls='vis2')
    sh.rect(X(XM - 3), Y(-85), v.L(6), v.L(47), fill='url(#hAl)', cls='vis2')
    sh.rect(X(XM - 7), Y(-73), v.L(14), v.L(19), fill='url(#hPETG)', cls='vis2')
    sh.rect(X(XM - 12), Y(-76.5), v.L(5), v.L(3), fill='#b9bec6', cls='vis2')
    sh.rect(X(XM - 17), Y(-75), v.L(5), v.L(6), fill='#ead9a4', cls='vis2')
    sh.rect(X(XM - 7), Y(-122), v.L(14), v.L(27), fill='url(#hPETG)', cls='vis2')
    sh.rect(X(XM + 16), Y(-140), v.L(24), v.L(3), cls='fill-pcb')
    for sx in (-11, 6):
        sh.rect(X(XM + sx), Y(-60), v.L(5), v.L(8), fill='url(#hPETG)', cls='vis2')
    # feet and pads
    feet = [(462, -(r_in(472) + T)), (590, -HALF - T), (712, -HALF - T), (830, -(r_in(840) + T)),
            (C1 + 17, -h - 12), (T1 - 37, -h - 12)]
    for fx, ytop in feet:
        sh.rect(X(fx), Y(ytop), v.L(20), v.L(ytop + 170), fill='url(#hPLA)', cls='vis2')
        sh.rect(X(fx), Y(-170), v.L(20), v.L(5), cls='fill-neo')
    sh.centre(X(-40), Y(0), X(T1 + 30), Y(0))
    return dict(xs_tap=xs_tap, xmist=xmist, feet=feet)


def bench_line(sh, v, x0, x1, yb=-175):
    X, Y = v.X, v.Y
    sh.line(X(x0), Y(yb), X(x1), Y(yb), cls='vis2')
    xx = X(x0)
    while xx < X(x1) - 8:
        sh.line(xx, Y(yb), xx + 8, Y(yb) + 8, cls='thin')
        xx += 16
    sh.text(X(x0), Y(yb) + 22, 'BENCH', cls='sm', anchor='start')


def sheet_ga1():
    sh = Sheet(1, 'WT-00-1', 'GENERAL ARRANGEMENT — SIDE ELEVATION', '', 'NTS',
               ['Section on the tunnel centre line; fan, stand and feet shown in outside view.',
                'Lengths marked TBD are drawn mid-range for layout only. Do not scale from the drawing.',
                'Fan model open (D-011): body drawn as the AC Infinity S6 envelope, 200 × 320 × 212.',
                'Screens 12a–12e: 12b, the third diffuser screen, is planned for margin; its position is TBD (drawn dashed).',
                'Joint positions inside the settling chamber and the test-section feet are layout only.',
                'Ball drawn 3/4 in (solid) with the 1 in ball dashed. Wall thickness t = TBD everywhere.'])
    v = View(88, 432, 0.95)
    X, Y = v.X, v.Y
    k = draw_tunnel_side(sh, v)
    bench_line(sh, v, -40, T1 + 30)
    h = P['ts'] / 2
    # flow arrows, one per section
    sh.flow(X(105), Y(-48), 58)
    sh.flow(X(D0 + 52), Y(-45), 50)
    sh.flow(X(HC1 + 14), Y(-62), 58)
    sh.flow(X(C0 + 34), Y(-70), 58)
    sh.flow(X(C1 + 24), Y(28), 56)

    # dimension chain
    yb = Y(-175)
    yd1, yd2 = yb + 104, yb + 150
    for xa, xb, lab, st, nm in ((0, P['fan_L'], 'TBD', 'T', 'FAN · D-011 OPEN'), (D0, D1, '150–200', 'P', 'DIFFUSER'),
                                (D1, C0, 'TBD', 'T', 'SETTLING CHAMBER'), (C0, C1, '250', 'P', 'CONTRACTION'),
                                (C1, T1, '270–290', 'P', 'TEST SECTION')):
        sh.hdim(X(xa), X(xb), yb + 4, yb + 4, yd1, lab, st=st)
        sh.text((X(xa) + X(xb)) / 2, yd1 + 17, nm, cls='sm', anchor='middle')
    sh.hdim(X(0), X(T1), yd1 + 6, yd1 + 6, yd2, 'TBD   (docs estimate 1150–1300 incl. fan)', st='T')
    sh.vtitle(X(T1 / 2), yd2 + 42, 'SIDE ELEVATION — SECTION ON TUNNEL CENTRE LINE',
              'Fan, stand, feet and balance box in outside view where not cut')

    # callouts, top rows
    R1, R2, R3 = 92, 148, 204
    B(sh, 1, X(150), Y(P['fan_H'] / 2), 190, R1)
    B(sh, 11, X(D0 + 120), Y(r_in(D0 + 120) + T), 430, R1)
    B(sh, 20, X(705), Y(HALF + T), 740, R1)
    B(sh, 23, X(k['xs_tap']), Y(HALF + T + 12), 930, R1)
    B(sh, 95, X(C1 - 3), Y(P['ts'] / 2 + T + P['fl_w']), 1150, R1)
    B(sh, 8, X(-10), Y(70), 66, R2)
    B(sh, 12, X(D1), Y(70), 512, R2, name='Screen (5 places, 12a–12e)')
    B(sh, 24, X(k['xmist']), Y(HALF + T + 26), 960, R2)
    B(sh, 10, X(SOCK0 + 8), Y(RS + P['sock_wall']), 300, R3)
    B(sh, 21, X(HC0 + 30), Y(118), 610, R3)
    B(sh, 30, X(C0 + 150), Y(r_in(C0 + 150) + T), 960, R3)

    # callouts, right column (test section and balance), ordered by target height
    cx = 1392
    col = [(40, X(T1 - 6), Y(h + 12), None), (42, X(C1 + 200), Y(h + P['acr_t']), 'Top window panel\n(removable)'),
           (52, X(T1), Y(32), None), (60, X(XM) + 6, Y(6), None), (64, X(XM + 12), Y(-30), None),
           (53, X(XM + 30), Y(-h - 3), None), (41, X(T1 - 30), Y(-h - 3), None),
           (66, X(XM + 3), Y(-100), None), (71, X(XM + 45), Y(-112), None), (72, X(XM + 30), Y(-139), 'HX711 amplifier\nboard'),
           (70, X(XM + 38), Y(-148), 'Balance module\nplate')]
    yy = 270
    for n, tx, ty, nm in col:
        B(sh, n, tx, ty, cx, yy, name=nm)
        yy += 37 if (nm and '\n' in nm) else 32

    # callouts, bottom row
    Rb = yb + 48
    B(sh, 7, X(91), Y(-160), 100, Rb)
    B(sh, 6, X(160), Y(-135), 250, Rb)
    B(sh, 99, X(472), Y(-150), 440, Rb)
    B(sh, 100, X(600), Y(-172), 640, Rb)
    B(sh, 13, X(SC1 + 3), Y(-HALF - T - P['fl_w']), 740, Rb)
    B(sh, 48, X(XE), Y(-h - 16), 1126, Rb, side='d', name='Tap station E')
    B(sh, 49, X(XM - 30), Y(-h - 16), 1250, Rb, side='d', name='Tap station M')

    # section index
    tx0, ty0 = 88, 838
    sh.text(tx0, ty0, 'WHERE EACH SECTION IS DETAILED', cls='kh')
    rows = [('Fan, stand, collar joint', 'items 1–10', 'Sheet 3 · WT-01'), ('Wide-angle diffuser', '10–13', 'Sheet 4 · WT-02'),
            ('Settling chamber', '12–13, 20–24', 'Sheet 5 · WT-03'), ('Contraction', '30', 'Sheet 6 · WT-04'),
            ('Test section and windows', '40–54', 'Sheet 7 · WT-05'), ('Force balance', '60–76', 'Sheet 8 · WT-06'),
            ('Pressure taps and airspeed', '80–93', 'Sheet 9 · WT-07'), ('Flanges, joints and feet', '95–100', 'Sheet 10 · WT-08'),
            ('Plan, end view, electronics layout', 'all', 'Sheet 2 · WT-00-2')]
    for i, (a, b, c) in enumerate(rows):
        col_ = i // 5
        rr = i % 5
        x0 = tx0 + col_ * 520
        y0 = ty0 + 24 + rr * 24
        sh.text(x0, y0, a, cls='tblc')
        sh.text(x0 + 255, y0, b, cls='tblm')
        sh.text(x0 + 360, y0, c, cls='tblc', weight=700)
        sh.line(x0, y0 + 7, x0 + 500, y0 + 7, cls='thin', extra='stroke-opacity="0.25"')
    return sh
