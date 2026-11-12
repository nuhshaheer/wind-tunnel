"""A shared helper used by s_d3b.py. The superseded drafts of sheets 9-10 were removed 2026-11-10."""
from wtsheets import *


def box(sh, x, y, w, hgt, title, sub=None, fill='#f4f5f7'):
    sh.rect(x, y, w, hgt, cls='vis2', fill=fill)
    sh.text(x + w / 2, y + hgt / 2 + (0 if sub else 5), title, cls='lbl', anchor='middle', weight=700)
    if sub:
        sh.text(x + w / 2, y + hgt / 2 + 17, sub, cls='sm', anchor='middle')
