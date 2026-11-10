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

STATUS_CLS = {'To buy': 'buy', 'On hand': 'have', 'Printed': 'print', 'Printed (later)': 'print', 'Choice open': 'open',
              'Feature': 'feat', 'Check house': 'house', 'Printed + brass': 'print', 'To buy (tool)': 'buy', 'To buy / Printed': 'buy'}

TBD_ROWS = [
    ('Fan model and every fan dimension', 'S6 envelope 200 × 320 × 212', 'Owner’s budget choice (D-011); then measure the outlet collar', '1–3'),
    ('Outlet collar Ø and socket ID', 'collar 150, socket ≈153.7', 'Measure the collar (paper strip ÷ π); socket = collar + 3.2 + ≈0.5; 10 mm test ring', '3, 4'),
    ('Wall thickness, all printed shells', '3', 'Sizing (2–3 mm was only a filament estimate)', 'all'),
    ('Flange width, thickness, bolt count and pitch; insert length; pin size', '14 × 6, 12 bolts', 'Sizing (build step 1)', '10'),
    ('Diffuser length and wall form; corner fillet radius', '175, curved', 'Sizing within 150–200 (Mehta1977 Fig. 5)', '4'),
    ('Screen 12b (third diffuser screen) and the position of 12a', 'both drawn', 'Measure the delivered screen wire: 0.010 in → three screens', '4'),
    ('Settling-chamber stations and length', '25 / 50 / 100 / 75 / 50', 'Choose spacing option A or B (sheet 5 table)', '5'),
    ('How 250 mm sections are split to fit the 256 mm bed', '—', 'Sizing: lengthwise halves or flat panels', '5, 6'),
    ('S taps, mist port: axial positions', 'after 12e', 'Sizing (both after the last screen)', '5'),
    ('Test-section length', '280', '270–290 from the station rules; the 1 in ball sets 4√S = 90', '7'),
    ('Side panel removable or fixed; panel size; taps in the removable top panel', 'top off, side TBD', 'Top comes off on magnets (owner, D-014); the side panel and the taps at sizing; see finding 2', '7'),
    ('M-station floor-tap offset; probe-guide position', 'offset 30', 'Sizing; the sting hole occupies the floor centre', '7'),
    ('Panel-frame, lip, gasket-ledge and magnet-skin sizes', 'concept only', 'Sizing; test-print the magnet pockets (8.2–8.3 × 2.2)', '7'),
    ('Sleeve and stem lengths; mount hole fit and depth; thumb-screw length; stop gap; base form', 'layout', 'Sizing; test-print the hole on the delivered rod; stops set with a known mass at ≈120 g', '8'),
    ('Floor-insert size, ledge, hold-down and seal', '80 × 60, ledge 4', 'Sizing: fits inside the balance box, sits flush, lifts out through the top opening', '7, 8'),
    ('Load-cell box, balance plate and HX711 board sizes', 'layout', 'Sizing; board dimensions from the delivered part', '8'),
    ('Feet heights and size; fan-stand height', 'bench at −175', 'Balance-box clearance sets the tunnel centre-line height (finding 5)', '1, 3, 10'),
    ('Arduino box, BME280 and SDP810 bracket positions', 'schematic', 'I²C runs under ≈1 m (finding 6)', '2, 9'),
    ('Overall length', '≈1325 drawn', 'Sum of the above; docs estimate 1150–1300 including the fan', '1'),
]

FINDINGS = [
    ('Settling-chamber length grows with the chosen parts.',
     'The docs’ 230–300 mm “full decay” length assumed 0.15–0.25 mm wire and 2–3 mm cells. With the chosen window screen (0.010–0.011 in wire: 500 d = 127–140 mm) and 6 mm printed cells (≥150 mm after the honeycomb), the same rules give about 380–390 mm plus frames. Mehta1979’s 0.2 D spacing gives about 200 mm. Our arithmetic; decide at sizing.'),
    ('Taps “one per wall” meet the lift-off panels.',
     'The top panel (and possibly a side panel) covers the E and M stations, so taps there would have to be unplugged at every model swap. Options: taps only in fixed walls, or panels that stop short of the stations.'),
    ('The M-station floor tap cannot sit at the floor centre.',
     'The sting hole and shield are there. The floor tap needs an offset (drawn 30 mm upstream, TBD) or the station uses three taps. It now sits in the sphere insert (53), so its tube is unplugged whenever the insert comes out.'),
    ('250 mm sections need splitting in cross-section, not only along the flow.',
     'A 250 mm square duct plus walls and flanges is wider than the 256 mm P1S bed, so each chamber and contraction-inlet segment must be printed in halves or as flat panels (D-005 covers segments along the flow only).'),
    ('The balance box sets the tunnel’s height.',
     'At layout values the box hangs to about 158 mm below the centre line, lower than the chamber’s flanges (142 mm). The test-section feet are therefore the tallest, and the fan stand must match the resulting centre-line height.'),
    ('I²C length limits where the Arduino box can go.',
     'With the BME280 near the fan inlet and the SDP810 near the test section, each run under about 1 m puts the Arduino box near the middle of the tunnel.'),
    ('Turning the sting-lock knob twists the load cell.',
     'The twist from the thumb screw (68) goes through the mount into the 100 g cell unless the mount is held. The screw is drawn along the wind, so any twist that gets through bends the cell in its stiff sideways direction (if the sensitive axis is as assumed on sheet 8). Hold the mount through the insert opening while turning. Our reasoning; not quantified.'),
]


NAV = {1: 'General arrangement: side elevation', 2: 'General arrangement: plan, exit view, joints',
       3: 'Fan, stand and fan-to-tunnel joint', 4: 'Wide-angle diffuser', 5: 'Settling chamber, honeycomb and screens',
       6: 'Contraction, 250 to 100 mm', 7: 'Test section, windows and model station', 8: 'Force balance and model mount',
       9: 'Pressure taps, probe, sensor and wiring', 10: 'Flanged joints, alignment and feet'}


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
ol.findings {{ margin: 0; padding-left: 22px; display: grid; gap: 10px; max-width: 110ch; }}
footer.src {{ font-size: 13px; color: var(--muted); max-width: 110ch; }}
@media (max-width: 640px) {{ header.top, section.doc {{ padding: 18px; }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior: auto !important; }} }}
</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow">Wind tunnel · 100 × 100 mm open-circuit blower · owner N. Shaheer</div>
  <h1>Drawing package: assembly, sections and parts</h1>
  <p class="lede">Ten sheets: the general arrangement, then each section from the fan to the open exit, the force balance, the airspeed instrumentation and the joints. Every dimension comes from the project documents at commit 0558370 (buy list, status, decisions and paper notes) and the owner’s sketch of 2026-11-09 (floor inserts, sting mount and sting lock). The sizing step (build step 1) has not been done, so most lengths are proposals and many are still to be decided. Undecided dimensions are marked TBD and drawn at layout values only.</p>
  <span class="status">PRELIMINARY · PRE-SIZING · NOT FOR MANUFACTURE</span>
  <p style="font-size:14px;margin:0;color:var(--muted)">Revision B, 2026-11-09: replaceable floor inserts (53, 54), the sting mount (65) and the thumb-screw sting lock (68) from the owner’s sketch (D-013 to D-015); general-arrangement leaders rerouted. Parts list, 2026-11-10: the Waveshare BME280 (89) and the acrylic as four 8 × 12 in sheets (42, 43), as ordered; the other rows’ statuses are still those of 2026-11-09, before the orders, and are updated at sizing. Generated by docs/drawings/ in the repo.</p>
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
  <p>What is still open on these drawings, the value drawn only to place it, and what decides it. Most close in build step 1 (sizing); the fan closes on the owner’s choice.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Open item</th><th>Drawn as (layout only)</th><th>Decided by</th><th>Sheets</th></tr></thead>
    <tbody>{tbd}</tbody></table></div>
  <h2 style="margin-top:10px">Findings from drawing it out</h2>
  <p>Gaps that only showed up when the parts were placed together. Recorded in PROJECT_STATUS.md §11 (2026-11-09); none is resolved yet.</p>
  <ol class="findings">{finds}</ol>
  <footer class="src">Sources: docs/buy_list.md §1–11, PROJECT_STATUS.md §2–3 and §10, DECISIONS.md D-005 to D-012, PROJECT_BACKGROUND.md, and the notes for Bell1988, Mehta1977, Mehta1979, Cooper1998, TAL221, SDP8xx and Sensirion2024, and the owner’s sketch docs/sketches/2026-11-09_flange-load-cell-test-chamber-notes-1.pdf. Where a figure is our arithmetic it says so. Drawn by Claude Code (agent), 2026-11-09.</footer>
</section>
</div>'''
    out = os.path.join(HERE, 'wind-tunnel-drawings.html')
    io.open(out, 'w', encoding='utf-8').write(page)
    print(out, round(len(page) / 1024), 'KB')
    return out


if __name__ == '__main__':
    build()
