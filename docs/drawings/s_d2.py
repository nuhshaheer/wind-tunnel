"""Shared test-section and balance helpers (used by s_d2b.py). The superseded drafts of sheets 7-8 were removed 2026-11-10."""
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
