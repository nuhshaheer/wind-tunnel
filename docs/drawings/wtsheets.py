"""Sheet definitions. Each function returns a wtlib.Sheet."""
import math
from wtlib import *
from wtdata import P, ITEM, contraction_half

USED = {}


def B(sh, n, tx, ty, cx, cy, side='r', name=None, suffix='', **kw):
    """Balloon using the master parts-list name, and record where each item appears."""
    key = int(str(n).rstrip('abcde'))
    USED.setdefault(key, set()).add(sh.no)
    nm = name if name is not None else ITEM[key]['name'] + suffix
    sh.balloon(n, tx, ty, cx, cy, nm, side=side, **kw)


def BM(sh, n, targets, cx, cy, side='r', name=None, suffix=''):
    key = int(str(n).rstrip('abcde'))
    USED.setdefault(key, set()).add(sh.no)
    nm = name if name is not None else ITEM[key]['name'] + suffix
    sh.balloon_multi(n, targets, cx, cy, nm, side=side)


# ---------- tunnel stations (mm, x from the fan inlet face) ----------
SOCK0 = P['fan_L'] - P['sock_depth']            # socket face
D0 = P['fan_L']                                  # diffuser start (socket bottom)
D1 = D0 + P['diff_L']                            # diffuser exit / chamber start
HC0 = D1 + P['ch_gap0']
HC1 = HC0 + P['hc_L']
SC1 = HC1 + P['hc_s1']
SC2 = SC1 + P['s1_s2']
C0 = SC2 + P['s2_c']                             # contraction inlet
C1 = C0 + P['con_L']                             # contraction exit / test section inlet
T1 = C1 + P['ts_L']                              # exit
XE = C1 + P['xE']
XS_TAP = SC2 + 15                                # layout only (position TBD)
XMIST = SC2 + 35                                 # layout only (position TBD)
XM = C1 + P['xM']
RS = (P['collar_D'] + 2 * P['wrap_t'] + P['clear']) / 2   # socket inner radius (layout)
HALF = P['ch'] / 2
T = P['t']


def smooth(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3 - 2 * u)


def r_in(x):
    """Inner half-height of the duct at station x (layout)."""
    if x < D0:
        return RS
    if x <= D1:
        return RS + (HALF - RS) * smooth((x - D0) / (D1 - D0))
    if x <= C0:
        return HALF
    if x <= C1:
        return contraction_half((x - C0) / (C1 - C0))
    return P['ts'] / 2


def wall_poly(v, xa, xb, top=True, n=60, t=T):
    s = 1 if top else -1
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    inner = [v.P(x, s * r_in(x)) for x in xs]
    outer = [v.P(x, s * (r_in(x) + t)) for x in reversed(xs)]
    return inner + outer




# ---------- floor insert (owner's sketch, 2026-11-09). Sizes are layout only: TBD ----------
INS_HL, INS_HW, INS_LEDGE = 40, 30, 4


def floor_run(sh, X, Y, x0, x1, e0, e1, top, t, hole=None, fix='url(#hPLAk)', ins='url(#hPLAr)', cls='vis2'):
    """Floor cut from x0 to x1 with a drop-in insert e0..e1 whose lip sits on a ledge of the fixed floor.
    Works along or across the flow. hole=(h0, h1) is a cut through the insert (sting hole)."""
    mid, bot, L = top - t / 2, top - t, INS_LEDGE

    def pp(pts):
        return [(X(a), Y(b)) for a, b in pts]
    sh.pl(pp([(x0, top), (e0, top), (e0, mid), (e0 + L, mid), (e0 + L, bot), (x0, bot)]), cls=cls, close=True, fill=fix)
    sh.pl(pp([(e1, top), (x1, top), (x1, bot), (e1 - L, bot), (e1 - L, mid), (e1, mid)]), cls=cls, close=True, fill=fix)
    if hole:
        h0, h1 = hole
        sh.pl(pp([(e0, top), (h0, top), (h0, bot), (e0 + L, bot), (e0 + L, mid), (e0, mid)]), cls=cls, close=True, fill=ins)
        sh.pl(pp([(h1, top), (e1, top), (e1, mid), (e1 - L, mid), (e1 - L, bot), (h1, bot)]), cls=cls, close=True, fill=ins)
    else:
        sh.pl(pp([(e0, top), (e1, top), (e1, mid), (e1 - L, mid), (e1 - L, bot), (e0 + L, bot), (e0 + L, mid), (e0, mid)]),
              cls=cls, close=True, fill=ins)
