"""Render chosen sheets to PNG with headless Edge, for checking layout. Usage: python preview.py 1 2 ..."""
import os, subprocess, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
import wtlib
from build import all_sheets

EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'png')
os.makedirs(OUT, exist_ok=True)
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap">'

sheets = all_sheets()
want = [int(a) for a in sys.argv[1:]] or [s.no for s in sheets]
for s in sheets:
    if s.no not in want:
        continue
    svg = s.svg(len(sheets), wtlib.DEFS)
    page = f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>body{{margin:0;background:#fff}}{wtlib.CSS}</style></head><body>{svg}</body></html>'
    fn = os.path.join(OUT, f'sheet{s.no}.html')
    open(fn, 'w', encoding='utf-8').write(page)
    png = os.path.join(OUT, f'sheet{s.no}.png')
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--screenshot={png}',
                    '--window-size=1600,1130', '--virtual-time-budget=4000', 'file:///' + fn.replace('\\', '/')],
                   check=False, capture_output=True, timeout=90)
    print(png, os.path.exists(png))
