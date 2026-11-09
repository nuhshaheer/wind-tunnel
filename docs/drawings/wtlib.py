"""SVG drawing helpers for the wind-tunnel drawing package (engineering-drawing style).

All geometry is passed in sheet pixels (viewBox 1600 x 1130). Views map millimetres to pixels with View.
Dimension status colours: FIX = decided / datasheet / part spec, PROP = proposed in the docs, TBD = not decided.
"""
import html, math

W, H = 1600, 1130
INK = '#15181d'
FIX = '#15181d'
PROP = '#1d5fae'
TBD = '#c0410d'
FLOW = '#0b7d8c'
STC = {'F': FIX, 'P': PROP, 'T': TBD}
STN = {'F': 'f', 'P': 'p', 'T': 't'}
CW = 0.50   # label face (IBM Plex Sans Condensed): average char width / size
CWM = 0.60  # dimension face (IBM Plex Mono)


def esc(s):
    return html.escape(str(s), quote=True)


def tw(text, size, mono=False):
    """Estimated text width in px."""
    return len(text) * size * (CWM if mono else CW)


class View:
    """Maps millimetres (x right, y up) to sheet pixels."""

    def __init__(self, ox, oy, s):
        self.ox, self.oy, self.s = ox, oy, s

    def X(self, x):
        return self.ox + self.s * x

    def Y(self, y):
        return self.oy - self.s * y

    def P(self, x, y):
        return (self.X(x), self.Y(y))

    def L(self, d):
        return self.s * d


def f(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


class Sheet:
    def __init__(self, no, code, title, subtitle, scale_note, notes):
        self.no, self.code, self.title, self.subtitle = no, code, title, subtitle
        self.scale_note, self.notes = scale_note, notes
        self.e = []

    def a(self, s):
        self.e.append(s)
        return self

    # ---------- primitives ----------
    def line(self, x1, y1, x2, y2, cls='vis', extra=''):
        return self.a(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" class="{cls}" {extra}/>')

    def pl(self, pts, cls='vis', close=False, fill=None, extra=''):
        d = ' '.join(f'{f(x)},{f(y)}' for x, y in pts)
        tag = 'polygon' if close else 'polyline'
        fl = f' style="fill:{fill}"' if fill else ''
        return self.a(f'<{tag} points="{d}" class="{cls}"{fl} {extra}/>')

    def path(self, d, cls='vis', fill=None, extra=''):
        fl = f' style="fill:{fill}"' if fill else ''
        return self.a(f'<path d="{d}" class="{cls}"{fl} {extra}/>')

    def rect(self, x, y, w, h, cls='vis', fill=None, rx=0, extra=''):
        if w < 0:
            x, w = x + w, -w
        if h < 0:
            y, h = y + h, -h
        fl = f' style="fill:{fill}"' if fill else ''
        r = f' rx="{f(rx)}"' if rx else ''
        return self.a(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" class="{cls}"{fl}{r} {extra}/>')

    def circ(self, cx, cy, r, cls='vis', fill=None, extra=''):
        fl = f' style="fill:{fill}"' if fill else ''
        return self.a(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" class="{cls}"{fl} {extra}/>')

    def text(self, x, y, s, cls='lbl', anchor='start', color=None, size=None, weight=None, extra=''):
        st = []
        if color:
            st.append(f'fill:{color}')
        if size:
            st.append(f'font-size:{size}px')
        if weight:
            st.append(f'font-weight:{weight}')
        sty = f' style="{";".join(st)}"' if st else ''
        lines = s.split('\n')
        if len(lines) == 1:
            return self.a(f'<text x="{f(x)}" y="{f(y)}" class="{cls}" text-anchor="{anchor}"{sty} {extra}>{esc(s)}</text>')
        lh = (size or 13) * 1.25
        spans = ''.join(f'<tspan x="{f(x)}" dy="{0 if i == 0 else f(lh)}">{esc(t)}</tspan>' for i, t in enumerate(lines))
        return self.a(f'<text x="{f(x)}" y="{f(y)}" class="{cls}" text-anchor="{anchor}"{sty} {extra}>{spans}</text>')

    def bgtext(self, x, y, s, st='F', anchor='middle', size=12.5, cls='dim'):
        """Dimension text with a white knock-out box."""
        lines = s.split('\n')
        wmax = max(tw(t, size, mono=True) for t in lines)
        lh = size * 1.22
        h = lh * len(lines)
        if anchor == 'middle':
            x0 = x - wmax / 2
        elif anchor == 'end':
            x0 = x - wmax
        else:
            x0 = x
        self.rect(x0 - 2, y - size + 1, wmax + 4, h + 1, cls='ko')
        return self.text(x, y, s, cls=f'{cls} {STN[st]}', anchor=anchor, size=size)

    # ---------- engineering symbols ----------
    def hdim(self, x1, x2, yf1, yf2, yd, label, st='F', tx=None, ty=None, size=12.5, ext=True):
        """Horizontal dimension between x1 and x2; features at yf1, yf2; dimension line at yd."""
        c = STN[st]
        if ext:
            for x, yf in ((x1, yf1), (x2, yf2)):
                if yf is None:
                    continue
                g = 3 if yd < yf else -3
                o = -6 if yd < yf else 6
                self.line(x, yf - g, x, yd + o, cls=f'dl {c}')
        self.line(x1, yd, x2, yd, cls=f'dl {c}', extra=f'marker-start="url(#a{c})" marker-end="url(#a{c})"')
        if tx is None:
            tx = (x1 + x2) / 2
        if ty is None:
            ty = yd - 5
        self.bgtext(tx, ty, label, st=st, size=size)

    def vdim(self, y1, y2, xf1, xf2, xd, label, st='F', side='l', tx=None, ty=None, size=12.5, ext=True):
        """Vertical dimension between y1 and y2; features at xf1, xf2; dimension line at xd; text horizontal."""
        c = STN[st]
        if ext:
            for y, xf in ((y1, xf1), (y2, xf2)):
                if xf is None:
                    continue
                g = 3 if xd < xf else -3
                o = -6 if xd < xf else 6
                self.line(xf - g, y, xd + o, y, cls=f'dl {c}')
        self.line(xd, y1, xd, y2, cls=f'dl {c}', extra=f'marker-start="url(#a{c})" marker-end="url(#a{c})"')
        if ty is None:
            ty = (y1 + y2) / 2 + 4
        if tx is None:
            tx = xd - 6 if side == 'l' else xd + 6
        self.bgtext(tx, ty, label, st=st, anchor='end' if side == 'l' else 'start', size=size)

    def adim(self, x1, y1, x2, y2, off, label, st='F', size=12.5):
        """Aligned dimension (for slanted features), offset perpendicular by off px."""
        c = STN[st]
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        nx, ny = -dy / L * off, dx / L * off
        self.line(x1, y1, x1 + nx * 1.1, y1 + ny * 1.1, cls=f'dl {c}')
        self.line(x2, y2, x2 + nx * 1.1, y2 + ny * 1.1, cls=f'dl {c}')
        self.line(x1 + nx, y1 + ny, x2 + nx, y2 + ny, cls=f'dl {c}', extra=f'marker-start="url(#a{c})" marker-end="url(#a{c})"')
        self.bgtext((x1 + x2) / 2 + nx * 1.6, (y1 + y2) / 2 + ny * 1.6 + 4, label, st=st, size=size)

    def lnote(self, tx, ty, lx, ly, label, st='F', anchor='start', size=12.5):
        """Leader note: arrow at (tx,ty), text at (lx,ly)."""
        c = STN[st]
        lines = label.split('\n')
        wmax = max(tw(t, size, mono=True) for t in lines)
        # leader attaches at the text's near edge, mid-height of first line
        if anchor == 'start':
            ax = lx - 3
        elif anchor == 'end':
            ax = lx + 3
        else:
            ax = lx
        ay = ly - size * 0.35
        self.line(ax, ay, tx, ty, cls=f'dl {c}', extra=f'marker-end="url(#a{c})"')
        self.bgtext(lx, ly, label, st=st, anchor=anchor, size=size)

    def balloon(self, n, tx, ty, cx, cy, name, side='r', r=12, size=13.5, dot=False):
        """Numbered callout circle at (cx,cy), leader with arrow to (tx,ty), full name beside it."""
        dx, dy = tx - cx, ty - cy
        L = math.hypot(dx, dy) or 1
        sx, sy = cx + dx / L * r, cy + dy / L * r
        mk = 'url(#dotL)' if dot else 'url(#aL)'
        self.line(sx, sy, tx, ty, cls='ldr', extra=f'marker-end="{mk}"')
        self.circ(cx, cy, r, cls='bal')
        ns = str(n)
        self.text(cx, cy + 4.2, ns, cls='bnum', anchor='middle', size=12 if len(ns) < 3 else 10)
        if name:
            lines = name.split('\n')
            if side == 'r':
                self.text(cx + r + 5, cy + 4.5 - (len(lines) - 1) * size * 0.62, name, cls='bname', anchor='start', size=size)
            elif side == 'l':
                self.text(cx - r - 5, cy + 4.5 - (len(lines) - 1) * size * 0.62, name, cls='bname', anchor='end', size=size)
            elif side == 'u':
                self.text(cx, cy - r - 6 - (len(lines) - 1) * size * 1.25, name, cls='bname', anchor='middle', size=size)
            elif side == 'd':
                self.text(cx, cy + r + 15, name, cls='bname', anchor='middle', size=size)

    def balloon_multi(self, n, targets, cx, cy, name, side='r', r=12, size=13.5):
        """One balloon, several leaders (same part in several places)."""
        for (tx, ty) in targets[1:]:
            dx, dy = tx - cx, ty - cy
            L = math.hypot(dx, dy) or 1
            self.line(cx + dx / L * r, cy + dy / L * r, tx, ty, cls='ldr', extra='marker-end="url(#aL)"')
        self.balloon(n, targets[0][0], targets[0][1], cx, cy, name, side=side, r=r, size=size)

    def flow(self, x, y, length=64, d='r', label='AIRFLOW'):
        """Prominent but small airflow arrow."""
        if d == 'r':
            x2 = x + length
            pts = [(x, y - 3), (x2 - 14, y - 3), (x2 - 14, y - 8), (x2, y), (x2 - 14, y + 8), (x2 - 14, y + 3), (x, y + 3)]
            self.pl(pts, cls='flw', close=True)
            if label:
                self.text(x + (length - 14) / 2, y - 11, label, cls='flt', anchor='middle')
        elif d == 'd':  # into the page (end views): circle with dot = toward viewer, cross = away
            self.circ(x, y, 9, cls='flwo')
            self.line(x - 6, y - 6, x + 6, y + 6, cls='flwx')
            self.line(x - 6, y + 6, x + 6, y - 6, cls='flwx')
            if label:
                self.text(x + 15, y + 4, label, cls='flt', anchor='start')
        elif d == 'o':  # out of the page, toward the viewer
            self.circ(x, y, 9, cls='flwo')
            self.circ(x, y, 3, cls='flw')
            if label:
                self.text(x + 15, y + 4, label, cls='flt', anchor='start')

    def centre(self, x1, y1, x2, y2):
        self.line(x1, y1, x2, y2, cls='ctr')

    def cutline(self, x, y1, y2, letter, dirn='r'):
        """Section cutting plane, vertical, arrows pointing in viewing direction."""
        self.line(x, y1, x, y2, cls='cut')
        for yy in (y1, y2):
            ax = x + (16 if dirn == 'r' else -16)
            self.line(x, yy, ax, yy, cls='cutb', extra='marker-end="url(#aCut)"')
            self.text(ax + (6 if dirn == 'r' else -6), yy + 5, letter, cls='cutl', anchor='start' if dirn == 'r' else 'end')

    def vtitle(self, x, y, title, sub=None):
        self.text(x, y, title, cls='vt', anchor='middle')
        w = tw(title, 15) * 0.98
        self.line(x - w / 2, y + 4, x + w / 2, y + 4, cls='vtu')
        if sub:
            self.text(x, y + 20, sub, cls='vs', anchor='middle')

    def breakline(self, x, y1, y2):
        """Zig-zag break line, vertical."""
        ym = (y1 + y2) / 2
        pts = [(x, y1), (x, ym - 8), (x - 6, ym - 3), (x + 6, ym + 3), (x, ym + 8), (x, y2)]
        self.pl(pts, cls='thin')

    def detail_circle(self, cx, cy, r, letter):
        self.circ(cx, cy, r, cls='detc')
        self.text(cx + r * 0.75 + 4, cy - r * 0.75 - 2, letter, cls='cutl', anchor='start')

    # ---------- sheet furniture ----------
    def frame(self, nsheets):
        out = []
        out.append(f'<rect x="12" y="12" width="{W-24}" height="{H-24}" class="brd"/>')
        out.append(f'<rect x="20" y="20" width="{W-40}" height="{H-40}" class="brd2"/>')
        # zone ticks
        for i in range(1, 8):
            x = 20 + i * (W - 40) / 8
            out.append(f'<line x1="{f(x)}" y1="12" x2="{f(x)}" y2="20" class="thin"/>')
            out.append(f'<line x1="{f(x)}" y1="{H-20}" x2="{f(x)}" y2="{H-12}" class="thin"/>')
        # bottom strip
        y0 = 985
        out.append(f'<line x1="20" y1="{y0}" x2="{W-20}" y2="{y0}" class="brd2"/>')
        # key
        kx = 30
        out.append(f'<text x="{kx}" y="{y0+20}" class="kh">KEY</text>')
        rows = [('F', '120', 'Decided, datasheet or part spec'), ('P', '150–200', 'Proposed in the docs, not final'),
                ('T', 'TBD', 'To be decided (build step 1)')]
        for i, (stc, sample, desc) in enumerate(rows):
            yy = y0 + 40 + i * 18
            out.append(f'<text x="{kx}" y="{yy}" class="dim {STN[stc]}" style="font-size:12px">{esc(sample)}</text>')
            out.append(f'<text x="{kx+64}" y="{yy}" class="kt">{esc(desc)}</text>')
        yy = y0 + 40 + 3 * 18
        out.append(f'<polygon points="{kx},{yy-6} {kx+30},{yy-6} {kx+30},{yy-10} {kx+44},{yy-4} {kx+30},{yy+2} {kx+30},{yy-2} {kx},{yy-2}" class="flw"/>')
        out.append(f'<text x="{kx+64}" y="{yy}" class="kt">Airflow direction</text>')
        # line types
        lx = 300
        out.append(f'<line x1="{lx}" y1="{y0+36}" x2="{lx+40}" y2="{y0+36}" class="vis"/><text x="{lx+48}" y="{y0+40}" class="kt">Visible</text>')
        out.append(f'<line x1="{lx}" y1="{y0+54}" x2="{lx+40}" y2="{y0+54}" class="hid"/><text x="{lx+48}" y="{y0+58}" class="kt">Hidden</text>')
        out.append(f'<line x1="{lx}" y1="{y0+72}" x2="{lx+40}" y2="{y0+72}" class="ctr"/><text x="{lx+48}" y="{y0+76}" class="kt">Centre line</text>')
        out.append(f'<rect x="{lx}" y="{y0+84}" width="40" height="12" style="fill:url(#hPLA)" class="thin"/><text x="{lx+48}" y="{y0+94}" class="kt">Printed (cut)</text>')
        # notes
        nx = 420
        out.append(f'<line x1="{nx-10}" y1="{y0}" x2="{nx-10}" y2="{H-20}" class="brd2"/>')
        out.append(f'<line x1="{290}" y1="{y0}" x2="{290}" y2="{H-20}" class="thin"/>')
        out.append(f'<text x="{nx}" y="{y0+20}" class="kh">NOTES</text>')
        yy = y0 + 38
        for i, n in enumerate(self.notes):
            out.append(f'<text x="{nx}" y="{yy}" class="nt"><tspan class="nn">{i+1}.</tspan> {esc(n)}</text>')
            yy += 16
        # title block
        tx = 1130
        out.append(f'<line x1="{tx}" y1="{y0}" x2="{tx}" y2="{H-20}" class="brd2"/>')
        tbh = H - 20 - y0
        out.append(f'<line x1="{tx}" y1="{y0+44}" x2="{W-20}" y2="{y0+44}" class="thin"/>')
        out.append(f'<line x1="{tx}" y1="{y0+80}" x2="{W-20}" y2="{y0+80}" class="thin"/>')
        out.append(f'<text x="{tx+10}" y="{y0+17}" class="tbs">WIND TUNNEL · 100 × 100 mm OPEN-CIRCUIT BLOWER · OWNER: N. SHAHEER</text>')
        out.append(f'<text x="{tx+10}" y="{y0+37}" class="tbt">{esc(self.title)}</text>')
        cells = [(tx, 'DWG NO', self.code), (tx + 105, 'SHEET', f'{self.no} OF {nsheets}'), (tx + 180, 'UNITS', 'mm'),
                 (tx + 230, 'SCALE', self.scale_note), (tx + 335, 'DATE', '2026-11-09')]
        for i, (cx, k, v) in enumerate(cells):
            if i:
                out.append(f'<line x1="{cx}" y1="{y0+44}" x2="{cx}" y2="{y0+80}" class="thin"/>')
            out.append(f'<text x="{cx+8}" y="{y0+57}" class="tbk">{k}</text><text x="{cx+8}" y="{y0+74}" class="tbv">{esc(v)}</text>')
        out.append(f'<text x="{tx+10}" y="{y0+97}" class="tbk">STATUS</text>')
        out.append(f'<text x="{tx+70}" y="{y0+97}" class="tbw">PRELIMINARY · PRE-SIZING · NOT FOR MANUFACTURE</text>')
        out.append(f'<text x="{tx+10}" y="{y0+114}" class="tbk">BASIS</text>')
        out.append(f'<text x="{tx+70}" y="{y0+114}" class="tbv2">docs at 0558370 + owner sketch 2026-11-09 · Claude Code (agent)</text>')
        return '\n'.join(out)

    def svg(self, nsheets, defs):
        body = '\n'.join(self.e)
        return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
                f'aria-label="{esc(self.code + " " + self.title)}" class="sheet">'
                f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>{defs}{body}{self.frame(nsheets)}</svg>')


DEFS = f'''<defs>
<marker id="af" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,1.6 L10,5 L0,8.4 z" fill="{FIX}"/></marker>
<marker id="ap" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,1.6 L10,5 L0,8.4 z" fill="{PROP}"/></marker>
<marker id="at" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,1.6 L10,5 L0,8.4 z" fill="{TBD}"/></marker>
<marker id="aL" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,1.5 L10,5 L0,8.5 z" fill="{INK}"/></marker>
<marker id="dotL" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" markerUnits="userSpaceOnUse"><circle cx="5" cy="5" r="4" fill="{INK}"/></marker>
<marker id="aCut" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,1 L10,5 L0,9 z" fill="{INK}"/></marker>
<pattern id="hPLA" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="7" stroke="{INK}" stroke-width="0.7"/></pattern>
<pattern id="hPLAk" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="7" height="7" fill="#e9eaec"/><line x1="0" y1="0" x2="0" y2="7" stroke="{INK}" stroke-width="0.7"/></pattern>
<pattern id="hPLAr" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="7" height="7" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="7" stroke="{INK}" stroke-width="0.7"/></pattern>
<pattern id="hPETG" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="5" height="5" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="5" stroke="{INK}" stroke-width="0.7"/></pattern>
<pattern id="hBr" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="4" fill="#f3e3b5"/><line x1="0" y1="0" x2="0" y2="4" stroke="#6b5413" stroke-width="0.8"/></pattern>
<pattern id="hAl" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#e6ebef"/><line x1="0" y1="0" x2="0" y2="6" stroke="#4b5560" stroke-width="0.7"/><line x1="3" y1="0" x2="3" y2="6" stroke="#4b5560" stroke-width="0.35"/></pattern>
<pattern id="hFoam" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fbf6e9"/><circle cx="1.5" cy="1.5" r="0.8" fill="#8a7a55"/><circle cx="4.5" cy="4.5" r="0.8" fill="#8a7a55"/></pattern>
<pattern id="hHex" width="10.392" height="6" patternUnits="userSpaceOnUse"><path d="M0,0 L1.732,1 L1.732,3 L0,4 M1.732,1 L3.464,0 M1.732,3 L3.464,4" stroke="{INK}" stroke-width="0.4" fill="none"/></pattern>
<pattern id="hScr" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="3" fill="#ffffff"/><path d="M0,0 L3,0 M0,0 L0,3" stroke="#6a737d" stroke-width="0.45"/></pattern>
</defs>'''

CSS = f'''
.sheet text{{font-family:"IBM Plex Sans Condensed","Arial Narrow","Segoe UI",Arial,sans-serif}}
.sheet .vis{{stroke:{INK};stroke-width:1.6;fill:none;stroke-linejoin:round}}
.sheet .vis2{{stroke:{INK};stroke-width:1.1;fill:none;stroke-linejoin:round}}
.sheet .thin{{stroke:{INK};stroke-width:0.7;fill:none}}
.sheet .hid{{stroke:{INK};stroke-width:0.8;fill:none;stroke-dasharray:6 3}}
.sheet .ctr{{stroke:#4a5260;stroke-width:0.6;fill:none;stroke-dasharray:22 4 3 4}}
.sheet .cut{{stroke:{INK};stroke-width:0.8;fill:none;stroke-dasharray:22 4 3 4}}
.sheet .cutb{{stroke:{INK};stroke-width:1.8;fill:none}}
.sheet .cutl{{font-size:17px;font-weight:700;fill:{INK}}}
.sheet .detc{{stroke:{INK};stroke-width:0.9;fill:none;stroke-dasharray:10 4}}
.sheet .dl{{stroke-width:0.7;fill:none}}
.sheet .dl.f{{stroke:{FIX}}} .sheet .dl.p{{stroke:{PROP}}} .sheet .dl.t{{stroke:{TBD}}}
.sheet text.dim{{font-size:12.5px;font-family:"IBM Plex Mono","Consolas",monospace}}
.sheet .dim.f{{fill:{FIX}}} .sheet .dim.p{{fill:{PROP}}} .sheet .dim.t{{fill:{TBD};font-weight:700}}
.sheet .ko{{fill:#ffffff;stroke:none}}
.sheet .ldr{{stroke:{INK};stroke-width:0.8;fill:none}}
.sheet .bal{{stroke:{INK};stroke-width:1.2;fill:#ffffff}}
.sheet .bnum{{font-size:11.5px;font-weight:700;fill:{INK}}}
.sheet .bname{{font-size:13.5px;fill:{INK}}}
.sheet .lbl{{font-size:13px;fill:{INK}}}
.sheet .sm{{font-size:12px;fill:#3b4350}}
.sheet .flw{{fill:{FLOW};stroke:none}}
.sheet .flwo{{fill:#ffffff;stroke:{FLOW};stroke-width:2}}
.sheet .flwx{{stroke:{FLOW};stroke-width:2}}
.sheet .flt{{font-size:10.5px;font-weight:700;letter-spacing:.08em;fill:{FLOW}}}
.sheet .vt{{font-size:16px;font-weight:700;letter-spacing:.04em;fill:{INK}}}
.sheet .vtu{{stroke:{INK};stroke-width:1}}
.sheet .vs{{font-size:12px;fill:#3b4350}}
.sheet .brd{{fill:none;stroke:{INK};stroke-width:2}}
.sheet .brd2{{fill:none;stroke:{INK};stroke-width:1.2}}
.sheet .kh{{font-size:12px;font-weight:700;letter-spacing:.1em;fill:{INK}}}
.sheet .kt{{font-size:12.2px;fill:{INK}}}
.sheet .nt{{font-size:12.4px;fill:{INK}}}
.sheet .nn{{font-weight:700}}
.sheet .tbs{{font-size:10.5px;letter-spacing:.06em;fill:#3b4350}}
.sheet .tbt{{font-size:18px;font-weight:700;fill:{INK}}}
.sheet .tbk{{font-size:9.5px;letter-spacing:.1em;fill:#5a6270}}
.sheet .tbv{{font-size:13px;font-weight:700;fill:{INK}}}
.sheet .tbv2{{font-size:11px;fill:{INK}}}
.sheet .tbw{{font-size:11.5px;font-weight:700;fill:{TBD}}}
.sheet .tblh{{font-size:11px;font-weight:700;fill:{INK}}}
.sheet .tblc{{font-size:12.5px;fill:{INK}}}
.sheet text.tblm{{font-size:12px;fill:{INK};font-family:"IBM Plex Mono","Consolas",monospace}}
.sheet .fill-acr{{fill:#d7ecf5;stroke:{INK};stroke-width:1.1}}
.sheet .fill-neo{{fill:#2a2d33;stroke:{INK};stroke-width:0.8}}
.sheet .fill-grey{{fill:#d9dce1;stroke:{INK};stroke-width:1.1}}
.sheet .fill-wall{{fill:#c9ccd2;stroke:{INK};stroke-width:0.9}}
.sheet .fill-pcb{{fill:#cfe3d2;stroke:{INK};stroke-width:1.1}}
.sheet .tube{{stroke:#4f6f8f;stroke-width:2.2;fill:none}}
.sheet .cable{{stroke:#6b4f8f;stroke-width:1.6;fill:none;stroke-dasharray:1 0}}
.sheet .scr{{stroke:#4b5560;stroke-width:1.2;stroke-dasharray:2 2;fill:none}}
'''
