"""Sheet 6 (contraction) and two helpers shared with s_d1b.py. The superseded drafts of sheets 3-5 were removed 2026-11-10."""
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
