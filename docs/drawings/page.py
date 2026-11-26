"""Assemble the published HTML page: sheets, parts list, TBD register, findings."""
import io, os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wtlib
from wtdata import ITEMS, ITEM
import wtsheets
from build import all_sheets

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))

sheets = all_sheets()
N = len(sheets)
used = wtsheets.USED

# ---------- consistency checks ----------
missing_in_list = sorted(k for k in used if k not in ITEM)
not_drawn = sorted(n for n in ITEM if n not in used)
assert not missing_in_list, f'callouts without a parts-list row: {missing_in_list}'
print('parts never drawn:', not_drawn)

STATUS_CLS = {'To buy': 'buy', 'Ordered': 'ord', 'On hand': 'have', 'Printed': 'print', 'Printed (later)': 'print', 'Choice open': 'open',
              'Feature': 'feat', 'Check house': 'house', 'Printed + brass': 'print', 'To buy (tool)': 'buy', 'To buy / Printed': 'buy'}

TBD_ROWS = [
    ('Fan collar diameter and inlet-ring socket ID', 'collar 150, socket ≈153.7', 'Measure the S6’s collar on arrival (paper strip ÷ π); socket = collar + 3.2 + ≈0.5; coupon C7', '3, 4'),
    ('Diffuser inlet diameter against the collar’s inside', 'Ø152', 'Match the loft’s inlet circle to the collar’s inside diameter on arrival', '4'),
    ('Hole sizes: inserts, screw clearance, magnet pockets, tap-stub sockets', 'Ø4.0, Ø3.4, Ø8.3, Ø3.3', 'Test coupons C1–C4 (cad/sizing/coupons.md), printed with the real settings', '7, 9, 10'),
    ('Sting fit in the mount', 'Ø3.3', 'Coupon C6 on the delivered rod', '8'),
    ('Fan-stand height', 'axis 175', 'The S6’s outlet axis height above its base, measured on arrival', '1, 3'),
    ('Load-cell mounting holes', 'as drawn', 'Read off the cell: which end is tapped M3 and which has Ø3.2 clearance (TAL221 notes)', '8'),
    ('Balance-module rails and door size', '≈80 × 70 door', 'Draw the box around the real module', '8'),
    ('BME280 holder', 'schematic', 'Measure the board (outline, holes, connector side)', '2'),
    ('Cable lengths W1–W3 and wire colours', 'length TBD', 'Box positions are now set (cad/sizing/supports.md); one colour per signal at assembly', '12'),
]

FINDINGS = [
    ('Settling-chamber length grows with the chosen parts. Resolved:',
     'compact spacing, 275 in all (D-027). Full-decay spacing would have been about 465.'),
    ('Taps “one per wall” meet the lift-off panels. Resolved:',
     'E sits in a printed entrance band closed on all four sides; M uses one tap in each side wall, 12 above the floor; no tap is in the lift-off panel (D-024).'),
    ('The M-station floor tap cannot sit at the floor centre. Resolved:',
     'the floor tap is dropped; M has two side-wall taps (D-024).'),
    ('250 mm sections need splitting in cross-section. Resolved:',
     'each prints as four identical corner pieces glued at mid-wall seams (D-023); the contraction splits at x = 82, so its exit is one seamless piece.'),
    ('The balance box sets the tunnel’s height. Resolved:',
     'with the mount stacked on the cell the box reaches 145 below the axis, the chamber’s flanges 140; the axis stands 175 above the bench, so the box clears by 30 (cad/sizing/supports.md).'),
    ('I²C length limits where the Arduino box can go. Placed:',
     'on the bench beside the contraction, with the SDP810 on the black wall near the test-section entrance and the BME280 on the fan stand (Proposed).'),
    ('Turning the sting-lock knob twists the load cell. Still a caution:',
     'the screw stays along the wind, so any twist that gets through bends the cell in its stiff direction; hold the mount while turning (D-015).'),
]


NAV = {1: 'General arrangement: side elevation', 2: 'General arrangement: plan, exit view, joints',
       3: 'Fan, stand and fan-to-tunnel joint', 4: 'Wide-angle diffuser', 5: 'Settling chamber, honeycomb and screens',
       6: 'Contraction, 250 to 100 mm', 7: 'Test section, windows and model station', 8: 'Force balance and model mount',
       9: 'Pressure taps, probe, sensor and wiring', 10: 'Flanged joints, alignment and feet',
       11: 'Electrical: system block diagram', 12: 'Electrical: interface schematic'}


def fmt_sheets(n):
    return ', '.join(str(s) for s in sorted(used.get(n, [])))


def build():
    svgs = [s.svg(N, wtlib.DEFS) for s in sheets]
    nav = ''.join(f'<li><a href="#sheet-{s.no}"><span class="no">{s.no:02d}</span><span class="code">{E(s.code)}</span>'
                  f'<span class="t">{E(NAV[s.no])}</span></a></li>' for s in sheets)
    figs = ''.join(f'<section class="sheetwrap" id="sheet-{s.no}" aria-label="Sheet {s.no}"><div class="sheethead"><span class="no">SHEET {s.no} OF {N}</span>'
                   f'<h2>{E(s.title)}</h2><span class="code">{E(s.code)}</span></div><div class="scroll">{svg}</div></section>'
                   for s, svg in zip(sheets, svgs))
    rows = []
    for (n, nm, does, spec, qty, cost, st, src) in ITEMS:
        sc = STATUS_CLS.get(st, 'feat')
        rows.append(f'<tr><td class="num"><span class="bal">{n}</span></td><td class="nm">{E(nm)}</td><td>{E(does)}</td><td class="spec">{E(spec)}</td>'
                    f'<td class="q">{E(qty)}</td><td class="c">{E(cost)}</td><td><span class="st {sc}">{E(st)}</span></td>'
                    f'<td class="q">{fmt_sheets(n)}</td><td class="src">{E(src)}</td></tr>')
    tbd = ''.join(f'<tr><td>{E(a)}</td><td class="mono">{E(b)}</td><td>{E(c)}</td><td class="q">{E(d)}</td></tr>' for a, b, c, d in TBD_ROWS)
    finds = ''.join(f'<li><strong>{E(a)}</strong> {E(b)}</li>' for a, b in FINDINGS)
    n_items = len(ITEMS)

    page = f'''<title>Wind Tunnel Drawing Package</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@400;600;700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>
/* Layout: a drawing-office binder. One column of full-width A-series sheets, then the parts list and the open-items register. */
:root {{
  --paper: #ffffff; --desk: #eef0f2; --ink: #15181d; --muted: #59606b; --rule: #d5d9de;
  --fix: {wtlib.FIX}; --prop: {wtlib.PROP}; --tbd: {wtlib.TBD}; --flow: {wtlib.FLOW};
  --f-head: "IBM Plex Sans Condensed", "Arial Narrow", "Segoe UI", Arial, sans-serif;
  --f-body: "IBM Plex Sans", "Segoe UI", Arial, sans-serif;
  --f-mono: "IBM Plex Mono", Consolas, monospace;
  color-scheme: light;
}}
body {{ background: var(--desk); color: var(--ink); font-family: var(--f-body); font-size: 15px; line-height: 1.5; }}
.wrap {{ max-width: 1640px; margin: 0 auto; padding-block: 28px 64px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); display: grid; gap: 28px; }}
header.top {{ background: var(--paper); border: 1px solid var(--rule); padding: 28px 32px; display: grid; gap: 18px; }}
.eyebrow {{ font-family: var(--f-head); letter-spacing: .12em; text-transform: uppercase; font-size: 13px; color: var(--muted); }}
h1 {{ font-family: var(--f-head); font-weight: 700; font-size: clamp(28px, 4vw, 44px); line-height: 1.05; margin: 0; text-wrap: balance; }}
.lede {{ max-width: 78ch; margin: 0; color: #2a2f37; }}
.status {{ display: inline-flex; gap: 10px; align-items: center; font-family: var(--f-head); font-weight: 700; color: var(--tbd); border: 1.5px solid var(--tbd); padding: 4px 10px; letter-spacing: .06em; font-size: 14px; width: fit-content; }}
.keyrow {{ display: flex; flex-wrap: wrap; gap: 10px 26px; font-size: 14px; align-items: center; }}
.keyrow .k {{ font-family: var(--f-mono); font-weight: 600; }}
.k.f {{ color: var(--fix); }} .k.p {{ color: var(--prop); }} .k.t {{ color: var(--tbd); }}
.flowkey {{ display: inline-block; width: 34px; height: 6px; background: var(--flow); position: relative; vertical-align: middle; margin-right: 6px; }}
.flowkey::after {{ content: ""; position: absolute; right: -10px; top: -5px; border-left: 11px solid var(--flow); border-top: 8px solid transparent; border-bottom: 8px solid transparent; }}
nav.index ol {{ list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 6px 18px; }}
nav.index a {{ display: grid; grid-template-columns: 30px 78px 1fr; gap: 8px; align-items: baseline; color: var(--ink); text-decoration: none; padding: 6px 4px; border-bottom: 1px solid var(--rule); font-size: 14px; }}
nav.index a:hover, nav.index a:focus-visible {{ background: #f4f6f8; outline: none; }}
nav.index .no {{ font-family: var(--f-mono); color: var(--muted); }}
nav.index .code {{ font-family: var(--f-mono); font-size: 13px; }}
nav.index .t {{ font-family: var(--f-head); }}
.sheetwrap {{ background: var(--paper); border: 1px solid var(--rule); box-shadow: 0 1px 0 rgba(0,0,0,.04); scroll-margin-top: 16px; min-width: 0; }}
.sheethead {{ display: flex; flex-wrap: wrap; gap: 6px 16px; align-items: baseline; padding: 14px 20px 6px; border-bottom: 1px solid var(--rule); }}
.sheethead h2 {{ font-family: var(--f-head); font-size: 20px; margin: 0; font-weight: 700; }}
.sheethead .no, .sheethead .code {{ font-family: var(--f-mono); font-size: 13px; color: var(--muted); }}
.scroll {{ overflow-x: auto; -webkit-overflow-scrolling: touch; }}
.scroll svg.sheet {{ display: block; width: 100%; min-width: 1060px; height: auto; }}
{wtlib.CSS}
section.doc {{ background: var(--paper); border: 1px solid var(--rule); padding: 24px 28px; display: grid; gap: 14px; min-width: 0; }}
section.doc h2 {{ font-family: var(--f-head); font-size: 26px; margin: 0; }}
section.doc p {{ margin: 0; max-width: 90ch; }}
.tablewrap {{ overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; font-size: 13.5px; }}
th {{ font-family: var(--f-head); text-align: left; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; font-size: 12px; color: var(--muted); border-bottom: 1.5px solid var(--ink); padding: 8px 8px; position: sticky; top: 0; background: var(--paper); }}
td {{ border-bottom: 1px solid var(--rule); padding: 7px 8px; vertical-align: top; }}
td.num {{ width: 44px; }}
.bal {{ display: inline-grid; place-items: center; width: 28px; height: 28px; border: 1.3px solid var(--ink); border-radius: 50%; font-family: var(--f-head); font-weight: 700; font-size: 12.5px; font-variant-numeric: tabular-nums; }}
td.nm {{ font-family: var(--f-head); font-weight: 700; font-size: 14.5px; min-width: 150px; }}
td.spec {{ min-width: 260px; }}
td.q, td.c {{ white-space: nowrap; font-variant-numeric: tabular-nums; }}
td.src {{ color: var(--muted); font-size: 12.5px; white-space: nowrap; }}
td.mono {{ font-family: var(--f-mono); font-size: 12.5px; }}
.st {{ font-family: var(--f-head); font-weight: 600; font-size: 12.5px; padding: 2px 7px; border: 1px solid; white-space: nowrap; }}
.st.buy {{ color: #7a4a00; border-color: #c9a227; background: #fff8e1; }}
.st.have {{ color: #1f6b3a; border-color: #7bbf93; background: #eef8f1; }}
.st.print {{ color: #2d4f86; border-color: #9db5dc; background: #f0f5fc; }}
.st.open {{ color: var(--tbd); border-color: var(--tbd); background: #fff3ec; }}
.st.feat {{ color: var(--muted); border-color: var(--rule); background: #f6f7f8; }}
.st.house {{ color: #5b4a8a; border-color: #b7a9e0; background: #f5f2fd; }}
.st.ord {{ color: #0f5f66; border-color: #7fc0c4; background: #ecf7f8; }}
ol.findings {{ margin: 0; padding-left: 22px; display: grid; gap: 10px; max-width: 110ch; }}
footer.src {{ font-size: 13px; color: var(--muted); max-width: 110ch; }}
@media (max-width: 640px) {{ header.top, section.doc {{ padding: 18px; }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior: auto !important; }} }}
</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow">Wind tunnel · 100 × 100 mm open-circuit blower · owner N. Shaheer</div>
  <h1>Drawing package: assembly, sections and parts</h1>
  <p class="lede">Twelve sheets: the general arrangement, then each section from the fan to the open exit, the force balance, the airspeed instrumentation and the joints, and (since revision D) two electrical sheets, the system block diagram and the interface schematic. Every dimension comes from the project documents (at commit 0558370 for revision B, updated 2026-11-10 for revision C: buy list, status, decisions and paper notes) and the owner’s sketch of 2026-11-09 (floor inserts, sting mount and sting lock). Revision F (2026-11-26) carries the sizing of build step 1: decisions D-022 to D-031 and the dimension sheets in cad/sizing/, from which the owner draws the CAD. Black dimensions are decided, blue are proposals in those sheets, and orange TBD marks what still needs a measurement or a test print.</p>
  <span class="status">REVISION F · SIZED 2026-11-26 · CAD FROM cad/sizing</span>
  <p style="font-size:14px;margin:0;color:var(--muted)">Revision B, 2026-11-09: replaceable floor inserts (53, 54), the sting mount (65) and the thumb-screw sting lock (68) from the owner’s sketch (D-013 to D-015); general-arrangement leaders rerouted. Revision C, 2026-11-10: each ball press-fit on its own full-length sting (63), so the ball stem (61) and the 5/32 in sting sleeve (62) are removed (D-016); stainless short M3 screws (73) at the balance instead of brass; the sting shield (64) shown attached to the sphere insert (53), lifting out with it (D-014); screen 12b planned for margin; every parts-list status brought up to the orders of 2026-11-09/10 (Waveshare BME280, acrylic as four 8 × 12 in sheets). Revision D, 2026-11-17: electrical sheets 11 (system block diagram) and 12 (interface schematic, with its electrical parts list and net list); sheet 9’s wiring note and HX711 pins now point to sheet 12; parts-list statuses Ordered → On hand (the owner reported every ordered part arrived, 2026-11-17; arrival checks pending). Note, 2026-11-19: parts-list item 76 now describes the weight set actually bought. Revision F, 2026-11-26: sized from decisions D-022 to D-031 (250 mm chamber and 250 mm 5th-order contraction; four-corner-piece split; 310 mm test section in two prints with one window and a black wall; E and M taps; the S6 fan; three-screen 175 mm diffuser; compact 275 mm chamber; sealed load-cell box with a door; image sting, items 55–57; probe through the open exit); flanges 12 beyond the wall with M3 × 5 inserts. Generated by docs/drawings/ in the repo.</p>
  <div class="keyrow">
    <span><span class="k f">100</span>&nbsp; decided, datasheet or part spec</span>
    <span><span class="k p">150–200</span>&nbsp; proposed in the docs, not final</span>
    <span><span class="k t">TBD</span>&nbsp; to be decided</span>
    <span><span class="flowkey"></span>&nbsp; airflow</span>
    <span>All dimensions in mm. Do not scale the drawings.</span>
  </div>
  <nav class="index" aria-label="Sheets"><ol>{nav}<li><a href="#parts"><span class="no">—</span><span class="code">PARTS</span><span class="t">Parts list ({n_items} items)</span></a></li><li><a href="#tbd"><span class="no">—</span><span class="code">OPEN</span><span class="t">TBD register and findings</span></a></li></ol></nav>
</header>
{figs}
<section class="doc" id="parts" aria-label="Parts list">
  <h2>Parts list</h2>
  <p>Every numbered callout on the sheets, with what the part does, its specification, quantity, the price seen in the buy list (a guide, not a quote; tax and shipping excluded) and where it appears. Screens 12a–12e are one part in five positions.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>No.</th><th>Name</th><th>What it does</th><th>Specification / material</th><th>Qty</th><th>Cost seen</th><th>Status</th><th>Sheets</th><th>Source</th></tr></thead>
    <tbody>{''.join(rows)}</tbody></table></div>
</section>
<section class="doc" id="tbd" aria-label="TBD register">
  <h2>TBD register</h2>
  <p>What is still open after the sizing: mostly measurements of delivered parts and test prints. The value drawn only places it.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Open item</th><th>Drawn as (layout only)</th><th>Decided by</th><th>Sheets</th></tr></thead>
    <tbody>{tbd}</tbody></table></div>
  <h2 style="margin-top:10px">Findings from drawing it out</h2>
  <p>Gaps that showed up when the parts were first placed together (2026-11-09), and how the sizing of 2026-11-26 settled them.</p>
  <ol class="findings">{finds}</ol>
  <footer class="src">Sources: docs/buy_list.md §1–11, PROJECT_STATUS.md §2–3 and §10, DECISIONS.md D-005 to D-016, docs/shopping_list.md, PROJECT_BACKGROUND.md, and the notes for Bell1988, Mehta1977, Mehta1979, Cooper1998, TAL221, SDP8xx and Sensirion2024, and the owner’s sketch docs/sketches/2026-11-09_flange-load-cell-test-chamber-notes-1.pdf. Electrical sheets: the SDP8xx, HX711 and TAL221 notes, buy list §5–8, and Waveshare’s BME280 Environmental Sensor schematic (read 2026-11-17). Where a figure is our arithmetic it says so. Drawn by Claude Code (agent), 2026-11-09; revision C 2026-11-10; revision D 2026-11-17; sheet 12 revision E 2026-11-23 (connector pin orders and C1 as in the KiCad shield, D-020); revision F 2026-11-26 (sizing, D-022 to D-031; cad/sizing/).</footer>
</section>
</div>'''
    out = os.path.join(HERE, 'wind-tunnel-drawings.html')
    io.open(out, 'w', encoding='utf-8').write(page)
    print(out, round(len(page) / 1024), 'KB')
    return out


if __name__ == '__main__':
    build()
