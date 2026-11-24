"""Sheets 11-12, electrical (revision D, 2026-11-17; sheet 12 revised E, 2026-11-23): the system block diagram and the
interface schematic.

Sources: resources/notes/SDP8xx.md (U1 pins, address, supply), HX711.md and TAL221.md (bridge, wire colours),
docs/buy_list.md §5-8, and Waveshare's "BME280 Environmental Sensor" schematic, read 2026-11-17 (header H1 pin order
1 VCC, 2 GND, 3 SDA, 4 SCL, 5 ADDR, 6 CS; 4.7 kΩ pull-ups to VCC on SDA, SCL, ADDR and CS; RT9193-33 regulator;
NDC7002N level translator). The SparkFun HX711 header and pad names are as on the delivered board (owner's photo,
2026-11-17). Revision E (2026-11-23): J1-J3 follow each part's own pin order so every cable runs pin 1 to pin 1, J3 has
five pins (VDD and VCC both on +5V), and C1 sits on the shield beside J1, as in the KiCad shield PCB/arduino_shield
(D-020).
"""
import wtsheets
from wtlib import *

DIG, PWR, TUBEC, MECH = '#6b4f8f', '#c62828', '#4f6f8f', '#59606b'
DATE = '2026-11-17'      # sheet 11 (revision D)
DATE_E = '2026-11-23'    # sheet 12 (revision E)
STATUS = 'BREADBOARD TESTED · SHIELD PCB NOT YET MADE'
BASIS = 'docs + datasheet notes + Waveshare schematic · Claude Code (agent)'
WARN = []   # text that may not fit its box; printed by check_fit()


def _mk(id_, color, size):
    return (f'<marker id="{id_}" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="{size}" markerHeight="{size}" '
            f'markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,1.5 L10,5 L0,8.5 z" fill="{color}"/></marker>')


EDEFS = ('<defs>' + _mk('eD', DIG, 13) + _mk('eA', INK, 11) + _mk('eP', PWR, 12) + _mk('eT', TUBEC, 15)
         + _mk('eF', FLOW, 16) + _mk('eK', MECH, 18) + _mk('eU', INK, 17) + '</defs>')


def used(sh, *items):
    """Record that these parts-list items appear on this sheet (the parts list's Sheets column)."""
    for n in items:
        wtsheets.USED.setdefault(n, set()).add(sh.no)


def fit(text, size, width, where, mono=False):
    if tw(text, size, mono) > width:
        WARN.append(f'{where}: "{text}" ≈{tw(text, size, mono):.0f} px > {width:.0f} px')


def path_d(pts):
    return 'M' + ' L'.join(f'{f(x)},{f(y)}' for x, y in pts)


def arrow(sh, pts, cls, mk, both=False):
    ex = f'marker-end="url(#{mk})"' + (f' marker-start="url(#{mk})"' if both else '')
    sh.path(path_d(pts), cls=cls, extra=ex)


def mech(sh, pts):
    """Mechanical load path: a double line with an arrowhead."""
    sh.path(path_d(pts), cls='smo', extra='marker-end="url(#eK)"')
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    L = math.hypot(x2 - x1, y2 - y1) or 1
    inner = pts[:-1] + [(x2 - (x2 - x1) / L * 16, y2 - (y2 - y1) / L * 16)]
    sh.path(path_d(inner), cls='smi')


def blk(sh, x, y, w, h, title, lines=(), cls='eb', tsize=14, lsize=12, lh=15, pad=10):
    """A block: bold title and plain lines; a line given as (text, 'P' or 'T') is coloured by status."""
    sh.rect(x, y, w, h, cls=cls)
    fit(title, tsize, w - 2 * pad, title)
    sh.text(x + pad, y + pad + tsize - 2, title, cls='bt', size=tsize)
    yy = y + pad + tsize - 2 + lh + 2
    for ln in lines:
        st = None
        if isinstance(ln, tuple):
            ln, st = ln
        fit(ln, lsize, w - 2 * pad, title)
        sh.text(x + pad, yy, ln, cls='bl', color=STC[st] if st else None, size=lsize)
        yy += lh
    if yy - lh + 6 > y + h:
        WARN.append(f'{title}: lines run past the bottom of the box')


def region(sh, x, y, w, h, label, inner=False, bottom=False):
    sh.rect(x, y, w, h, cls='rgi' if inner else 'rg', rx=6)
    sh.text(x + 12, y + h - 10 if bottom else y + 18, label, cls='rgl')
    fit(label, 11, w - 24, 'region ' + label)


# ---------- schematic symbols ----------
def wire(sh, pts):
    sh.path(path_d(pts), cls='w')


def dot(sh, x, y):
    sh.circ(x, y, 3.2, cls='jd')


def pwr(sh, x, y, d='u', label='+5V'):
    """+5V supply symbol: a short stem from (x, y) ending in a bar."""
    if d == 'u':
        wire(sh, [(x, y), (x, y - 12)])
        sh.line(x - 9, y - 12, x + 9, y - 12, cls='w', extra='style="stroke-width:2"')
        sh.text(x, y - 18, label, cls='pnam', anchor='middle', weight=700)
    else:
        wire(sh, [(x, y), (x - 12, y)])
        sh.line(x - 12, y - 9, x - 12, y + 9, cls='w', extra='style="stroke-width:2"')
        sh.text(x - 17, y + 4, label, cls='pnam', anchor='end', weight=700)


def gnd(sh, x, y, d='d'):
    """Ground symbol: stem, then three shrinking bars."""
    if d == 'd':
        wire(sh, [(x, y), (x, y + 10)])
        for i, hw in enumerate((10, 6.5, 3)):
            sh.line(x - hw, y + 10 + 4 * i, x + hw, y + 10 + 4 * i, cls='w')
    else:
        wire(sh, [(x, y), (x - 10, y)])
        for i, hw in enumerate((10, 6.5, 3)):
            sh.line(x - 10 - 4 * i, y - hw, x - 10 - 4 * i, y + hw, cls='w')


def tag(sh, x, y, name, d='r'):
    """Net label: a flag whose point touches the wire end at (x, y)."""
    w = tw(name, 11.5, mono=True) + 10
    s = 1 if d == 'r' else -1
    pts = [(x, y), (x + s * 7, y - 8), (x + s * (7 + w), y - 8), (x + s * (7 + w), y + 8), (x + s * 7, y + 8)]
    sh.pl(pts, cls='tag', close=True)
    sh.text(x + s * (7 + w / 2), y + 4, name, cls='tagt', anchor='middle')


def res_v(sh, x, y1, y2):
    """Zigzag resistor, vertical, 36 px body centred between y1 and y2."""
    m = (y1 + y2) / 2
    b0 = m - 18
    zz = [(x, b0)] + [(x + (6 if i % 2 == 0 else -6), b0 + 3 + 6 * i) for i in range(6)] + [(x, b0 + 36)]
    wire(sh, [(x, y1), (x, b0)])
    sh.pl(zz, cls='w')
    wire(sh, [(x, b0 + 36), (x, y2)])


def cap_v(sh, x, y1, y2, polar=False):
    """Capacitor, vertical, plates 8 px apart; polar = electrolytic (curved lower plate, + at the top)."""
    m = (y1 + y2) / 2
    wire(sh, [(x, y1), (x, m - 4)])
    sh.line(x - 10, m - 4, x + 10, m - 4, cls='w', extra='style="stroke-width:2.4"')
    if polar:
        sh.path(f'M{f(x - 10)},{f(m + 8)} Q{f(x)},{f(m + 1)} {f(x + 10)},{f(m + 8)}', cls='w', extra='style="stroke-width:2.4"')
        sh.text(x - 15, m - 7, '+', cls='pnam', anchor='middle', weight=700)
        wire(sh, [(x, m + 4.5), (x, y2)])
    else:
        sh.line(x - 10, m + 4, x + 10, m + 4, cls='w', extra='style="stroke-width:2.4"')
        wire(sh, [(x, m + 4), (x, y2)])


def nc(sh, x, y):
    sh.line(x - 5, y - 5, x + 5, y + 5, cls='w')
    sh.line(x - 5, y + 5, x + 5, y - 5, cls='w')


def part(sh, x, w, pins_l=(), pins_r=(), pad=18, stub=26, body=None):
    """A part drawn as a box. pins_* are (y, name, number or '', status or None); body=(top, bottom) overrides the
    box height. Returns (top, bottom)."""
    ys = [p[0] for p in list(pins_l) + list(pins_r)]
    top, bot = body or (min(ys) - pad, max(ys) + pad)
    sh.rect(x, top, w, bot - top, cls='sym')
    for (y, name, num, st) in pins_l:
        wire(sh, [(x - stub, y), (x, y)])
        sh.text(x + 7, y + 4, name, cls='pnam', color=STC[st] if st else None)
        if num:
            sh.text(x - stub / 2, y - 5, num, cls='pnum', anchor='middle')
    for (y, name, num, st) in pins_r:
        wire(sh, [(x + w, y), (x + w + stub, y)])
        sh.text(x + w - 7, y + 4, name, cls='pnam', anchor='end', color=STC[st] if st else None)
        if num:
            sh.text(x + w + stub / 2, y - 5, num, cls='pnum', anchor='middle')
    return top, bot


def conn(sh, x, ys, ref):
    """A 4-pin connector: body with pin numbers, board-side stubs on the left, the cable leaving on the right."""
    top, bot = ys[0] - 14, ys[-1] + 14
    sh.rect(x, top, 22, bot - top, cls='sym')
    for i, y in enumerate(ys):
        sh.text(x + 11, y + 4, str(i + 1), cls='pnum', anchor='middle')
        wire(sh, [(x - 26, y), (x, y)])
    sh.text(x + 11, top - 8, ref, cls='ref', anchor='middle', size=14)


def cable(sh, x, ys, ref, note):
    cy = (ys[0] + ys[-1]) / 2
    ry = (ys[-1] - ys[0]) / 2 + 10
    sh.a(f'<ellipse cx="{f(x)}" cy="{f(cy)}" rx="8" ry="{f(ry)}" class="thin"/>')
    sh.text(x, ys[0] - 28, ref, cls='ref', anchor='middle', size=13)
    sh.text(x, ys[0] - 14, note, cls='ll', anchor='middle', color=TBD)


def table(sh, x0, y0, title, cols, rows, size=11.5, step=16, colour=None):
    """Simple ruled table. cols = [(header, width)], rows = tuples of strings; colour(row, col) -> colour or None."""
    sh.text(x0, y0, title, cls='kh')
    hy = y0 + 20
    x = x0
    for (hd, wd) in cols:
        sh.text(x + 4, hy, hd, cls='tblh')
        x += wd
    sh.line(x0, hy + 6, x, hy + 6, cls='vis2')
    yy = hy + 22
    for r in rows:
        x = x0
        for j, ((hd, wd), cell) in enumerate(zip(cols, r)):
            fit(cell, size, wd - 8, f'table {title}')
            c = colour(r, j) if colour else None
            sh.text(x + 4, yy, cell, cls='tblc', size=size, color=c, weight=700 if j == 0 else None)
            x += wd
        sh.line(x0, yy + 5, x, yy + 5, cls='thin', extra='style="stroke:#d5d9de"')
        yy += step
    return yy


# =====================================================================================================
def sheet_block():
    sh = Sheet(11, 'WT-E01', 'ELECTRICAL: SYSTEM BLOCK DIAGRAM', '', 'NTS',
               ['Left to right: what is measured → sensor → conditioning + ADC → microcontroller → laptop. Power runs right to left.',
                'U1 and A3 are digital sensors (conditioning and ADC inside), so only the load cell needs its own board, A2.',
                'U1 and A3 share one I²C bus, two wires; A1 calls each by its address (0x25, 0x77). A2 has its own two wires.',
                'The firmware logs raw values only; calibrations, the ×966 mbar / p_amb correction and C_D are done in analysis/.',
                'Pins, parts and values: sheet 12 (WT-E02). Pressure taps and tubing: sheet 9 (WT-07).',
                'Ranges for q, force and current are our estimates, not measurements. Nothing on this sheet is built or tested yet.'],
               kind='elec', date=DATE, status=STATUS, basis=BASIS, units='SI',
               key2=[('text', 'Line styles:'), ('text', 'see the LINES box')])
    sh.a(EDEFS)
    used(sh, 66, 72, 87, 89, 90, 93)

    # ---------- source and legend ----------
    blk(sh, 50, 90, 210, 98, 'Air source (not measured)',
        ['6 in inline fan, with its own', 'speed controller, on mains', ('model open (D-011)', 'T'), 'no wire to A1 (D-012)'])
    sh.rect(330, 90, 1230, 98, cls='ebd')
    sh.text(342, 108, 'LINES', cls='kh')
    items = [((342, 136), 'air', 'Airflow'), ((640, 136), 'tube', 'Pressure in a tube'), ((940, 136), 'mech', 'Force (mechanical)'),
             ((1240, 136), 'ana', 'Analog signal (µV–mV)'), ((342, 168), 'dig', 'Digital: I²C or 2-wire serial'),
             ((640, 168), 'usb', 'USB: data and 5 V'), ((940, 168), 'pwr', '+5 V supply'), ((1240, 168), 'box', 'Dashed box: one board or device')]
    for (x, y), k, label in items:
        if k == 'air':
            arrow(sh, [(x, y), (x + 56, y)], 'sair', 'eF')
        elif k == 'tube':
            arrow(sh, [(x, y), (x + 56, y)], 'stb', 'eT')
        elif k == 'mech':
            mech(sh, [(x, y), (x + 56, y)])
        elif k == 'ana':
            arrow(sh, [(x, y), (x + 56, y)], 'sana', 'eA')
        elif k == 'dig':
            arrow(sh, [(x, y), (x + 56, y)], 'sdig', 'eD', both=True)
        elif k == 'usb':
            arrow(sh, [(x, y), (x + 56, y)], 'susb', 'eU')
        elif k == 'pwr':
            arrow(sh, [(x + 56, y), (x, y)], 'spwr', 'eP')
        elif k == 'box':
            sh.rect(x, y - 9, 56, 18, cls='ebd')
        sh.text(x + 68, y + 4, label, cls='lbl', size=12.5)

    # ---------- column headers ----------
    for cx, h in ((155, 'WHAT IS MEASURED'), (445, 'SENSOR'), (745, 'CONDITIONING AND ADC'), (1040, 'MICROCONTROLLER'), (1390, 'LAPTOP')):
        sh.text(cx, 236, h, cls='kh', anchor='middle')
    sh.line(40, 246, 1560, 246, cls='thin')

    # ---------- airflow trunk ----------
    arrow(sh, [(75, 188), (75, 290)], 'sair', 'eF')
    sh.text(86, 272, 'AIRFLOW', cls='flt')
    arrow(sh, [(75, 380), (75, 610)], 'sair', 'eF')
    sh.text(86, 600, 'ON THE BALL', cls='flt')

    # ---------- row A: airspeed ----------
    blk(sh, 50, 290, 210, 90, 'Air at the model', ['dynamic pressure q', ('≈ 25–101 Pa at 6.5–13 m/s', 'P'), '(our estimate)'])
    arrow(sh, [(260, 335), (330, 335)], 'stb', 'eT')
    sh.text(295, 325, 'taps, tubes', cls='llt', anchor='middle')
    sh.text(295, 354, '(sheet 9)', cls='ll', anchor='middle')
    blk(sh, 330, 290, 230, 90, 'U1 · SDP810-125Pa', ['thermal flow-through sensor', '±125 Pa, 16-bit, 0.08 Pa + 3 %', 'I²C address 0x25'])
    sh.text(745, 322, 'conditioning + ADC are inside U1', cls='ll', anchor='middle')

    # ---------- row B: room air ----------
    blk(sh, 100, 450, 160, 90, 'Room air', ['pressure ≈ 1 atm,', 'temperature,', 'humidity'])
    arrow(sh, [(260, 495), (330, 495)], 'sair', 'eF')
    blk(sh, 330, 450, 230, 90, 'A3 · BME280 board', ['pressure, temperature, humidity', '3.3 V chip + level translator', 'I²C address 0x77'])
    sh.text(745, 482, 'conditioning + ADC are inside the BME280', cls='ll', anchor='middle')

    # shared I²C bus into A1
    arrow(sh, [(900, 335), (560, 335)], 'sdig', 'eD')
    arrow(sh, [(900, 495), (560, 495)], 'sdig', 'eD')
    sh.path(path_d([(900, 335), (900, 495)]), cls='sdig')
    arrow(sh, [(900, 415), (940, 415)], 'sdig', 'eD')
    sh.circ(900, 415, 4.5, cls='jd', fill=DIG)
    sh.text(888, 410, 'I²C bus (shared)', cls='lld', anchor='end')
    sh.text(888, 426, 'SDA 20, SCL 21, 100 kHz', cls='ll', anchor='end')

    # ---------- row C: force ----------
    blk(sh, 50, 610, 210, 90, 'Drag on the ball', [('≈ 0.3–2.3 gf (3–23 mN)', 'P'), 'at 6.5–13 m/s', '(our estimate)'])
    mech(sh, [(260, 655), (330, 655)])
    sh.text(295, 642, 'sting, mount', cls='ll', anchor='middle')
    blk(sh, 330, 610, 230, 110, 'LC1 · TAL221 100 g', ['strain-gauge bridge, 0.6 mV/V', ('≈ 9–70 µV at 5 V excitation', 'P'),
                                                      '(our arithmetic)', 'four wires, soldered to A2'])
    sh.rect(588, 596, 282, 150, cls='ebd')
    sh.text(600, 614, 'A2 · SparkFun HX711 board', cls='bt', size=13)
    arrow(sh, [(560, 668), (610, 668)], 'sana', 'eA')
    sh.text(585, 660, 'µV', cls='ll', anchor='middle')
    sh.pl([(610, 638), (610, 698), (680, 668)], cls='sym', close=True)
    sh.text(633, 672, '×128', cls='bt', size=12, anchor='middle')
    sh.text(645, 716, 'amplifier', cls='ll', anchor='middle')
    arrow(sh, [(680, 668), (710, 668)], 'sana', 'eA')
    sh.pl([(710, 643), (830, 643), (850, 668), (830, 693), (710, 693)], cls='sym', close=True)
    sh.text(770, 665, '24-bit ADC', cls='bt', size=13, anchor='middle')
    sh.text(770, 681, '10 or 80 SPS', cls='bl', size=11.5, anchor='middle')
    sh.text(780, 716, 'converter', cls='ll', anchor='middle')
    arrow(sh, [(850, 668), (940, 668)], 'sdig', 'eD', both=True)
    sh.text(895, 658, 'DAT, CLK', cls='lld', anchor='middle')
    sh.text(895, 686, 'pins 2, 3', cls='ll', anchor='middle', color=PROP)

    # ---------- microcontroller ----------
    blk(sh, 940, 290, 200, 460, 'A1 · Arduino Mega 2560',
        ['Elegoo, ATmega2560, 5 V', '', 'Firmware (TODO P2):', '• reads U1, A3 and A2', '• adds a time stamp', '• sends one CSV line',
         '  per sample to the laptop', '• raw values only, no', '  corrections or units', '', 'No display or knob (D-012)'])
    arrow(sh, [(1140, 430), (1240, 430)], 'susb', 'eU')
    sh.path(path_d([(1180, 430), (1180, 332)]), cls='susb')
    arrow(sh, [(1180, 332), (1240, 332)], 'susb', 'eU')
    dot(sh, 1180, 430)
    sh.circ(1180, 430, 5, cls='jd')
    sh.text(1150, 455, 'USB', cls='bt', size=12)
    sh.text(1150, 470, 'CSV lines', cls='ll')

    # ---------- laptop ----------
    sh.rect(1210, 280, 355, 470, cls='ebd')
    sh.text(1222, 298, 'SOFTWARE', cls='rgl')
    blk(sh, 1240, 305, 300, 55, 'Serial Plotter', ['live view while running (D-012)'])
    blk(sh, 1240, 400, 300, 60, 'Logger → data/raw/', ['raw values + time, never edited'])
    blk(sh, 1240, 500, 300, 120, 'Analysis scripts (analysis/)',
        ['calibrations: load cell, SDP810 gain', '× 966 mbar / p_amb on every q', 'ρ = p / (R T), then V, Re and C_D',
         'mount drag and blockage corrections'])
    blk(sh, 1240, 660, 300, 75, 'Result vs reference', ['Brown and Lawler Eq. (19), ±10 %,', 'C_D rising with Re (D-009)'])
    arrow(sh, [(1390, 460), (1390, 500)], 'sana', 'eA')
    arrow(sh, [(1390, 620), (1390, 660)], 'sana', 'eA')

    # ---------- power ----------
    sh.text(50, 828, 'POWER', cls='kh')
    blk(sh, 50, 840, 210, 62, 'Fan: own mains supply', ['never through A1 (D-012)'], cls='ebg', tsize=13)
    blk(sh, 330, 840, 530, 62, '+5 V to U1, A3 and A2 (through J1–J3)',
        [('≈ 100 mA in all, including the Mega itself (our estimate)', 'P')], tsize=13)
    blk(sh, 940, 840, 200, 62, 'A1 5 V rail', ['fed from USB'], tsize=13)
    blk(sh, 1240, 840, 300, 62, 'Laptop USB port', ['5 V, up to 500 mA (USB 2.0 standard)'], tsize=13)
    arrow(sh, [(1240, 871), (1140, 871)], 'spwr', 'eP')
    arrow(sh, [(940, 871), (860, 871)], 'spwr', 'eP')
    return sh


# =====================================================================================================
def sheet_schematic():
    sh = Sheet(12, 'WT-E02', 'ELECTRICAL: INTERFACE SCHEMATIC', '', 'NTS',
               ['Same label = same wire (SDA, SCL, HX_DAT, HX_CLK). All +5V symbols are one rail; all ground symbols one ground.',
                'Pin numbers are each part’s own: U1 from the SDP8xx datasheet p. 4; A3 from Waveshare’s schematic (header H1).',
                'J1–J3 follow each part’s own pin order, so each cable runs pin 1 to pin 1 (D-020). A2 is drawn as its board is labelled.',
                'R1, R2 not fitted (DNP): A3 already has 4.7 kΩ pull-ups to 5 V. Fit them only to run U1 without A3 on the bus.',
                'LC1’s wires are soldered straight to A2, never through the breadboard (Weakly2024). No mains on this sheet (D-012).',
                'Breadboard built and every sensor read, 2026-11-23. Shield PCB designed in KiCad (PCB/arduino_shield, D-020), not made.'],
               kind='elec', date=DATE_E, status=STATUS, basis=BASIS, units='SI', key2=['wire', 'dot', 'tag', 'nc'])
    sh.a(EDEFS)
    used(sh, 66, 71, 72, 87, 88, 89, 90, 91, 92, 93)

    # ---------- regions ----------
    region(sh, 150, 50, 610, 702, 'ARDUINO BOX (ITEM 91) · MIDDLE OF THE TUNNEL')
    region(sh, 490, 84, 255, 656, 'INTERFACE · BREADBOARD → PCB', inner=True, bottom=True)
    region(sh, 880, 50, 685, 200, 'BY THE TEST SECTION · ON THE SENSOR BRACKET (ITEM 88)')
    region(sh, 880, 265, 685, 240, 'ROOM AIR NEAR THE FAN INLET · AWAY FROM HEAT')
    region(sh, 880, 520, 685, 232, 'BALANCE BOX (LOAD-CELL BOX, ITEM 71)')

    # ---------- laptop and A1 ----------
    sh.rect(30, 360, 98, 70, cls='eb')
    sh.text(79, 386, 'LAPTOP', cls='bt', size=13, anchor='middle')
    sh.text(79, 402, 'log and', cls='bl', size=11.5, anchor='middle')
    sh.text(79, 416, 'live view', cls='bl', size=11.5, anchor='middle')
    sh.text(79, 450, 'W4 · USB A–B', cls='ll', anchor='middle')
    sh.text(79, 465, 'item 93', cls='ll', anchor='middle')

    part(sh, 200, 180, pins_l=[(400, 'USB', '', None)],
         pins_r=[(230, '5V', '', None), (270, 'GND', '', None), (350, 'SDA 20', '', None), (390, 'SCL 21', '', None),
                 (470, 'D2', '', 'P'), (510, 'D3', '', 'P')], body=(110, 570))
    sh.text(212, 134, 'A1', cls='ref', size=16)
    sh.text(212, 154, 'Arduino Mega 2560', cls='bt', size=13)
    sh.text(212, 170, 'Elegoo · item 90', cls='bl', size=11.5)
    sh.text(212, 186, 'ATmega2560, 5 V logic', cls='bl', size=11.5)
    sh.text(212, 552, 'other pins unused', cls='bl', size=11.5)
    wire(sh, [(174, 400), (128, 400)])

    wire(sh, [(406, 230), (440, 230)])
    pwr(sh, 440, 230)
    wire(sh, [(406, 270), (440, 270)])
    gnd(sh, 440, 270)
    tag(sh, 406, 350, 'SDA')
    tag(sh, 406, 390, 'SCL')
    tag(sh, 406, 470, 'HX_DAT')
    tag(sh, 406, 510, 'HX_CLK')

    # ---------- interface parts ----------
    pwr(sh, 520, 150)
    cap_v(sh, 520, 150, 200, polar=True)
    gnd(sh, 520, 200)
    sh.text(536, 172, 'C2', cls='ref', size=13)
    sh.text(536, 187, '10 µF 50 V', cls='bl', size=11.5)
    sh.text(536, 201, 'at the 5 V entry', cls='bl', size=11)

    for x, name, ref in ((530, 'SDA', 'R1'), (630, 'SCL', 'R2')):
        pwr(sh, x, 452)
        res_v(sh, x, 452, 516)
        wire(sh, [(x, 516), (x + 12, 516)])
        tag(sh, x + 12, 516, name)
        sh.text(x + 12, 474, ref, cls='ref', size=13)
        sh.text(x + 12, 488, '5.1 kΩ', cls='bl', size=11.5)
        sh.text(x + 12, 502, 'DNP', cls='bl', size=11.5, color=PROP, weight=700)

    # Revision E: each connector follows its part's own pin order, so every cable runs pin 1 to pin 1 (D-020).
    J1, J2, J3 = [130, 160, 190, 220], [310, 340, 370, 400], [565, 595, 625, 655, 685]
    for ys, ref, nets in ((J1, 'J1', ('SCL', '+5V', 'GND', 'SDA')), (J2, 'J2', ('+5V', 'GND', 'SDA', 'SCL')),
                          (J3, 'J3', ('+5V', '+5V', 'HX_DAT', 'HX_CLK', 'GND'))):
        conn(sh, 690, ys, ref)
        for y, net in zip(ys, nets):
            if net == '+5V':
                pwr(sh, 664, y, d='l')
            elif net == 'GND':
                gnd(sh, 664, y, d='l')
            else:
                tag(sh, 664, y, net, d='l')
        for y in ys:
            wire(sh, [(712, y), (1014, y)])
    cable(sh, 820, J1, 'W1', '4 wires, length TBD')
    cable(sh, 820, J2, 'W2', '4 of its 6 wires')
    cable(sh, 820, J3, 'W3', '5 wires, length TBD')

    # C1 moved onto the shield, beside J1 (revision E; on the breadboard it sat at the cable's board end).
    pwr(sh, 560, 250)
    cap_v(sh, 560, 250, 300)
    gnd(sh, 560, 300)
    sh.text(576, 268, 'C1', cls='ref', size=13)
    sh.text(576, 283, '0.1 µF', cls='bl', size=11.5)
    sh.text(576, 297, 'next to J1', cls='bl', size=11)

    # ---------- U1, SDP810 ----------
    part(sh, 1040, 150, pins_l=[(130, 'SCL', '1', None), (160, 'VDD', '2', None), (190, 'GND', '3', None), (220, 'SDA', '4', None)],
         pins_r=[(155, 'H', '', None), (195, 'L', '', None)])
    for y in (155, 195):
        sh.circ(1220, y, 4, cls='sym')
    sh.text(1232, 159, 'H port ← S or P', cls='llt')
    sh.text(1232, 199, 'L port ← E or M', cls='llt')
    sh.text(1232, 176, 'tubes, sheet 9', cls='ll')
    tx = 1355
    sh.text(tx, 92, 'U1', cls='ref', size=16)
    sh.text(tx, 110, 'Sensirion SDP810-125Pa', cls='bt', size=13)
    sh.text(tx, 126, 'item 87 · I²C 0x25', cls='bl', size=11.5)
    sh.text(tx, 142, '2.7–5.5 V, ≤ 5.5 mA', cls='bl', size=11.5)
    sh.text(tx, 166, 'Pins on the part, in order:', cls='bl', size=11.5, weight=700)
    sh.text(tx, 182, '1 SCL · 2 VDD · 3 GND · 4 SDA', cls='pnam', size=11.5)
    sh.text(tx, 198, '2 mm pitch; find pin 1 on p. 12', cls='bl', size=11)
    sh.text(tx, 214, 'C1 is on the shield, next to J1', cls='bl', size=11)

    # ---------- A3, BME280 ----------
    part(sh, 1040, 150, pins_l=[(310, 'VCC', '1', None), (340, 'GND', '2', None), (370, 'SDA', '3', None), (400, 'SCL', '4', None),
                                (430, 'ADDR', '5', None), (460, 'CS', '6', None)])
    nc(sh, 1014, 430)
    nc(sh, 1014, 460)
    tx = 1210
    sh.text(tx, 302, 'A3', cls='ref', size=16)
    sh.text(tx, 320, 'Waveshare BME280 Environmental Sensor', cls='bt', size=13)
    sh.text(tx, 336, 'item 89 · I²C 0x77 (ADDR left open)', cls='bl', size=11.5)
    sh.text(tx, 358, 'On the board (Waveshare schematic):', cls='bl', size=11.5, weight=700)
    sh.text(tx, 374, '• 3.3 V regulator (RT9193-33) for the chip', cls='bl', size=11.5)
    sh.text(tx, 390, '• level translator (2 × NDC7002N)', cls='bl', size=11.5)
    sh.text(tx, 406, '• 4.7 kΩ pull-ups to VCC on SDA, SCL, ADDR, CS', cls='bl', size=11.5)
    sh.text(tx, 426, 'ADDR and CS open: pulled high, so I²C mode, 0x77', cls='bl', size=11.5)
    sh.text(tx, 446, 'Its cable: 6-pin plug to six Dupont sockets', cls='bl', size=11.5)

    # ---------- A2, HX711, and LC1 ----------
    top, bot = part(sh, 1040, 140, pins_l=[(565, 'VDD', '', None), (595, 'VCC', '', None), (625, 'DAT', '', None),
                                           (655, 'CLK', '', None), (685, 'GND', '', None)],
                    pins_r=[(580, 'RED', '', None), (610, 'BLK', '', None), (640, 'WHT', '', None), (670, 'GRN', '', None)])
    sh.text(1110, 700, 'B+, B− unused', cls='bl', size=10.5, anchor='middle')
    sh.text(1040, bot + 17, 'A2 · SparkFun HX711 breakout (SEN-13879) · item 72', cls='bt', size=12.5)
    sh.text(1040, bot + 32, 'header and pads as labelled on the board; RATE 10 samples/s', cls='bl', size=11.5)
    for y, colour in ((580, 'red · E+'), (610, 'black · E−'), (640, 'white · A−'), (670, 'green · A+')):
        wire(sh, [(1206, y), (1294, y)])
        sh.text(1250, y - 5, colour, cls='ll', anchor='middle')
    sh.text(1250, 692, 'soldered direct,', cls='ll', anchor='middle')
    sh.text(1250, 705, 'no breadboard', cls='ll', anchor='middle')
    part(sh, 1320, 100, pins_l=[(580, 'EXC+', '', None), (610, 'EXC−', '', None), (640, 'SIG−', '', None), (670, 'SIG+', '', None)])
    cx, cy, r = 1394, 625, 20
    sh.pl([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], cls='thin', close=True)
    for px, py in ((cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)):
        sh.circ(px, py, 2, cls='jd')
    tx = 1435
    sh.text(tx, 580, 'LC1', cls='ref', size=16)
    sh.text(tx, 597, 'TAL221 100 g', cls='bt', size=13)
    sh.text(tx, 613, 'load cell, item 66', cls='bl', size=11.5)
    sh.text(tx, 629, '0.6 mV/V, ≤ 6 V', cls='bl', size=11.5)
    sh.text(tx, 645, 'bridge: 4 gauges', cls='bl', size=11.5)
    sh.text(tx, 661, '2nd cell: spare', cls='bl', size=11.5)

    # ---------- tables ----------
    def bom_colour(r, j):
        if j == 4 and 'TBD' in r[4]:
            return TBD
        if j == 4 and r[4].startswith('DNP'):
            return PROP
        return None
    table(sh, 30, 774, 'ELECTRICAL PARTS',
          [('REF', 56), ('PART', 150), ('VALUE / PART NUMBER', 262), ('WHERE', 134), ('STATUS', 112), ('ITEM', 46)],
          [('A1', 'Microcontroller', 'Elegoo Mega 2560', 'Arduino box', 'On hand, works', '90'),
           ('A2', 'Load-cell amplifier', 'SparkFun HX711 breakout, SEN-13879', 'Balance box', 'On hand', '72'),
           ('A3', 'Ambient sensor board', 'Waveshare BME280 Environmental Sensor', 'Room air, fan inlet', 'On hand', '89'),
           ('U1', 'Differential pressure', 'Sensirion SDP810-125Pa', 'Sensor bracket', 'On hand', '87'),
           ('LC1', 'Load cell', 'TAL221 100 g (the second is a spare)', 'Balance box', 'On hand', '66'),
           ('C1', 'Capacitor', '0.1 µF film, ECE kit', 'Shield, by J1', 'On hand', '—'),
           ('C2', 'Capacitor', '10 µF 50 V electrolytic, ECE kit', 'Interface, 5 V in', 'On hand', '—'),
           ('R1, R2', 'I²C pull-up', '5.1 kΩ ¼ W, ECE kit', 'Interface', 'DNP (note 4)', '—'),
           ('J1–J3', 'Pin header, 2.54 mm', 'J1, J2 4-pin; J3 5-pin; for jumpers', 'Shield', 'TBD: on hand?', '—'),
           ('W1–W4', 'Cables', 'W1–W3: wires with Dupont ends; W4: USB A–B', 'Between boxes', 'Lengths TBD', '92, 93')],
          colour=bom_colour)
    end = table(sh, 810, 774, 'CONNECTIONS (NET LIST)', [('NET', 70), ('JOINS', 515), ('NOTES', 175)],
                [('+5V', 'A1 5V · C1 · C2+ · J1-2 · J2-1 · J3-1, 2 · (R1, R2) → U1-2 VDD · A3-1 VCC · A2 VDD, VCC', 'USB 5 V, ≈100 mA (est.)'),
                 ('GND', 'A1 GND · C1 · C2− · J1-3 · J2-2 · J3-5 → U1-3 · A3-2 · A2 GND', 'one common ground'),
                 ('SDA', 'A1 pin 20 · J1-4 · J2-3 · (R1) → U1-4 · A3-3', 'I²C data, 100 kHz'),
                 ('SCL', 'A1 pin 21 · J1-1 · J2-4 · (R2) → U1-1 · A3-4', 'I²C clock, from A1'),
                 ('HX_DAT', 'A1 pin 2 · J3-3 → A2 DAT', 'data out of the HX711'),
                 ('HX_CLK', 'A1 pin 3 · J3-4 → A2 CLK', 'clock from A1'),
                 ('Bridge', 'A2 RED, BLK, WHT, GRN (E+, E−, A−, A+) → LC1 wires of the same colours', 'soldered, balance box only'),
                 ('Open', 'A3-5 ADDR, A3-6 CS; A2 B+, B− (channel B)', 'not connected')])
    sh.text(810, end + 6, 'J1-3 means connector J1, pin 3; U1-4 means part U1, pin 4. Arrows read “board side → remote part”.', cls='ll')
    return sh


def check_fit():
    for w in WARN:
        print('fit:', w)
