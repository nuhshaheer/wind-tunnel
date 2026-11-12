# Drawings

A **preliminary** engineering drawing package for the whole tunnel: 10 sheets, a parts list matching every numbered
callout, a TBD register and the findings from drawing it. Revision C, 2026-11-10 (revision B, 2026-11-09). **Pre-sizing,
not for manufacture:**
build step 1 (sizing) has not been done, so most dimensions are proposals and many are TBD.

- Open [wind-tunnel-drawings.html](wind-tunnel-drawings.html) in a browser. The owner also has a private published copy
  at https://claude.ai/artifact/D8V6LeDybj3N6xJeeqzTzd (only the owner's account can open it); it still shows
  revision B until it is republished.
- Sources: the project docs at commit `0558370` (revision B) and as of 2026-11-10 (revision C), the owner's
  [2026-11-09 sketch](../sketches/README.md) and decisions D-013 to D-016 ([DECISIONS.md](../../DECISIONS.md)).
- Revision C (2026-11-10): each ball sits on its own full-length sting (D-016), so the ball stem (61) and the 5/32 in
  sting sleeve (62) are gone and their numbers are not reused; stainless short M3 screws (73) at the balance instead of
  brass; the sting shield (64) is attached to the sphere floor insert (53) and lifts out with it (D-014); screen 12b is
  planned for margin; every parts-list status follows the orders of 2026-11-09/10. The superseded draft sheet
  functions were deleted from `s_d1.py`, `s_d2.py` and `s_d3.py` (the rebuilt page was byte-identical before and after).
- Sessions: [2026-11-09 drawing package](../sessions/2026-11-09-drawing-package.md) (revision B);
  [2026-11-10 consistency audit](../sessions/2026-11-10-consistency-audit.md) (revision C).

## Reading the sheets

- Dimensions are in mm and coloured by status: **black** = decided, or from a datasheet or part spec; **blue** =
  proposed in the docs, not final; **orange-red TBD** = not decided. Undecided parts are drawn at layout values only,
  which are never printed as dimensions. Do not scale the drawings.
- Callout numbers are the same on every sheet and in the parts list: 1–8 fan; 10–13 diffuser and screens; 20–24
  settling chamber; 30 contraction; 40–54 test section and floor inserts; 60–76 balance, model mount and calibration;
  80–93 airspeed taps, sensors and electronics; 95–100 joints and feet.

| Sheet | Code | Contents |
|---|---|---|
| 1 | WT-00-1 | General arrangement: side elevation, section on the centre line |
| 2 | WT-00-2 | Plan, exit end view, electronics layout, joint schedule |
| 3 | WT-01 | Fan, stand and the fan-to-tunnel collar joint |
| 4 | WT-02 | Wide-angle diffuser |
| 5 | WT-03 | Settling chamber, honeycomb and screens |
| 6 | WT-04 | Contraction, with the wall-ordinate table |
| 7 | WT-05 | Test section, windows, floor inserts and model station |
| 8 | WT-06 | Force balance, sting mount and lock, floor inserts in plan, calibration set-up |
| 9 | WT-07 | Pressure taps, probe, SDP810 and wiring |
| 10 | WT-08 | Flanged joints, alignment and feet |

## Regenerating

Python 3 standard library only. Never hand-edit the HTML; change the scripts and rebuild.

```bash
python docs/drawings/page.py            # rebuilds wind-tunnel-drawings.html; prints "parts never drawn: []"
python docs/drawings/preview.py 1 7 8   # optional: PNGs of chosen sheets in docs/drawings/png/ (ignored by Git)
```

`preview.py` needs Microsoft Edge at its standard Windows path. `page.py` stops if a callout has no parts-list row,
and prints any parts-list item that no sheet shows.

| File | What it holds |
|---|---|
| `wtdata.py` | Every dimension with its source, and the parts list (`ITEMS`). After sizing, change the numbers here first |
| `wtlib.py` | Drawing primitives: lines, hatches, dimensions, callout balloons, airflow arrows, sheet frame and title block, styles |
| `wtsheets.py` | Stations along the tunnel, the balloon helper that records where each part appears, and the floor-insert helper |
| `s_ga.py`, `s_ga2.py` | Sheets 1 and 2 |
| `s_d1b.py` | Sheets 3–5 |
| `s_d1.py` | Sheet 6 and the wall and flange helpers used by `s_d1b.py` |
| `s_d2b.py` | Sheets 7 and 8 (`s_d2.py`: the shared shield and balance helpers) |
| `s_d3b.py` | Sheets 9 and 10 (`s_d3.py`: one shared helper) |
| `build.py` | Sheet order |
| `page.py` | The HTML page: sheets, parts list, TBD register and findings |

Callout positions are hand-placed in sheet pixels. After changing dimensions, render the affected sheets with
`preview.py` and check that no label, leader or dimension overlaps another.
