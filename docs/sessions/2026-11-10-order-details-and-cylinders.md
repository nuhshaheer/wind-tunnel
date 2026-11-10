# 2026-11-10: Order details and cylinders

- **Session ID:** 3fc38569-3ca2-4f1d-909d-a2424715134b (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

A short session: buying advice and documentation only. Nothing arrived, was built or was tested.

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `f5616a3` (the owner had committed and pushed the README follow-up to the parts-ordering
  session). Working tree clean. `check_docs.py` 0 failures, 0 warnings; 20 tests OK in 14.8 s.
- Discrepancies found at catch-up:
  1. PROJECT_STATUS (header, §6, §12), SESSION_LOG, the parts-ordering log and TODO still called the README follow-up
     "not committed yet". This is the expected lag after a push; backfilled in this wrap.
  2. `docs/experimental_setup.md` gave the full-decay settling chamber as 230–300 mm (about 380–390 mm plus frames with
     the chosen parts, open question 15). The previous log said this was fixed; it was not.
  3. `docs/experimental_setup.md` still said two diffuser screens (three are planned).
  4. PROJECT_BACKGROUND named "an Adafruit BME280" (the Waveshare was ordered).
  5. PROJECT_BACKGROUND said "the sphere is not chosen" (chosen 2026-11-08).
  6. The drawings still show the 5/32 in sleeve and the Adafruit BME280 (deliberate, left for sizing).
- No objective set at the start. The owner asked about cylinders, then sent order details.

## 2. Work completed

**Cylinder advice (owner: "should i buy some cylindars too?").**
- First reading, as the cylinder experiments in TODO P3: not now. The spare 1/8 in brass rod already covers the
  vortex-tone idea. A 3/8 in brass tube (K&S 8135, about $3.69–3.99 at hardware stores, $8.87 at Walmart) is needed
  only if the pressure-around-a-cylinder experiment is chosen. A cylinder is not a better validation than the sphere
  (9.5 % blockage for 3/8 in, end gaps). A third floor insert (D-014) could hold an upright cylinder, so no wall holes
  are needed.
- **The owner clarified:** plastic cylinders from McMaster, like the Delrin balls. Advice: not now.
  - Upside: force. A full-span 1/4 in rod gives about 6.4–7.7 gf at 13 m/s against about 1.3 gf for the 3/4 in ball
    (estimates, §6).
  - Downsides: it needs its own holder, a floor-insert hole and a gap under the lid; there is no cylinder-drag
    source in `resources/`; end gaps and 2-D blockage make it a weaker reference than the sphere; and it would be a
    separate McMaster order for a $2–3 part.
  - The 1/8 in brass rod is already a precise cylinder, and printed ones would do, because surface finish matters only
    near the drag crisis.
  - If wanted later, a 1/4 in Delrin rod is the size to buy.
  - The agent asked whether sizing should leave room for a cylinder test. **Not answered**; recorded in TODO P3 idea 6.

**Order details recorded (owner, 2026-11-10):**
- Acrylic: **four 8 × 12 in sheets** of the 1/8 in cast acrylic. Each sheet (203 × 305 mm) gives one window panel of
  about 300 × 120 mm plus a strip about 83 mm wide; the test section is 270–290 mm long, so it fits.
- SDP810: the Mouser order shows **403-SDP810-125PA, MFG part SDP810-125PA**: the ±125 Pa part, as chosen.

**BME280 named as the Waveshare** (owner asked, "change it to waveshare BME280 as well"): PROJECT_BACKGROUND
(measurement approach, step 1), TODO's 2026-11-08 Done entry (a note that it was replaced), and the drawings' parts
list (item 89).

**Drawings:** parts-list rows 42 and 43 (acrylic) and 89 (BME280) updated in `docs/drawings/wtdata.py`, with status
"Ordered". A note was added to the revision line in `page.py` saying that the other rows' statuses are still those of
2026-11-09, before the orders, and are updated at sizing. The page was rebuilt. The sheets themselves did not change.

**At the wrap:** discrepancies 1–5 fixed (the commit backfilled; the settling-chamber, diffuser-screen and sphere
entries updated, keeping the dated history).

## 3. Files and equipment affected

- `PROJECT_STATUS.md`: header (last commit `f5616a3`, not-committed note), §3 SDP810 and acrylic rows, §4 `/catchup`
  and `/wrap` records, §6 work completed, §12 next steps (cylinder question; inputs answered), §13 commit list.
- `TODO.md`: P0 reporting task (acrylic and SDP810 answered), P3 idea 6 (cylinder on the balance), Done entries
  (`f5616a3`, the order details), a note on the 2026-11-08 Adafruit entry.
- `PROJECT_BACKGROUND.md`: Waveshare BME280 (measurement approach); spheres chosen (blockage section); settling-chamber
  row in the length budget (380–390 mm note).
- `docs/experimental_setup.md`: current configuration (acrylic), settling-chamber and diffuser rows, model access
  (acrylic sheets), airspeed sensor row (Mouser part number), change history.
- `docs/buy_list.md`, `docs/shopping_list.md`: acrylic and SDP810 rows.
- `docs/drawings/wtdata.py`, `docs/drawings/page.py`, `docs/drawings/wind-tunnel-drawings.html` (rebuilt).
- `docs/sessions/SESSION_LOG.md` (new row; commit backfilled), `docs/sessions/2026-11-10-parts-ordering.md` (commit
  field backfilled: `f5616a3`), this log.
- Not updated: `README.md` (checked: still accurate); `DECISIONS.md` (no decision made); the owner's private
  published copy of the drawings on claude.ai (now out of date).
- Equipment: none changed; nothing has arrived.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch          # catch-up and wrap: STATE: UP_TO_DATE at f5616a3
python scripts/check_docs.py                   # see §7
python -m unittest discover -s tests -v        # see §7
python docs/drawings/page.py                   # before editing (no diff), then after the parts-list edits
```

Force estimate for full-span cylinders and the balls (run once, 2026-11-10; ρ 1.20 kg/m³, μ 1.81×10⁻⁵ Pa·s, wetted span
98 mm assumed, C_D 1.0–1.2 for the cylinders and 0.44 for the balls, both assumed):

```bash
python -c "
q13=0.5*1.20*13**2; q65=0.5*1.20*6.5**2; mu=1.81e-5
for name,d in (('1/8 in brass rod (have)',3.175e-3),('1/4 in rod',6.35e-3),('3/8 in rod',9.525e-3)):
  L=0.098
  for cd in (1.0,1.2):
    F13=cd*q13*d*L/9.80665e-3; F65=cd*q65*d*L/9.80665e-3
    print(f'{name:24s} Cd {cd}: {F65:5.2f}-{F13:5.2f} gf at 6.5-13 m/s, blockage {d/0.1*100:4.1f} %, Re {1.2*6.5*d/mu:6.0f}-{1.2*13*d/mu:6.0f}')
import math
for nm,d in (('3/4 in ball',19.05e-3),('1 in ball',25.4e-3)):
  A=math.pi*d*d/4; print(nm, round(0.44*q13*A/9.80665e-3,2),'gf at 13 m/s (Cd 0.44)')
"
```

Web searches (standard mode): "K&S 3/8 inch brass tube 12 inch price" and "acetal Delrin rod 1/4 inch diameter 1 ft
price McMaster-Carr". Sources are in the conversation answers; none was filed in `resources/`.

## 6. Measurements and results

No measurements. Estimates and prices seen (not results, not quotes):

| Quantity | Value | Basis |
|---|---|---|
| Full-span 1/8 in rod (3.175 mm) | 0.80–0.97 gf at 6.5 m/s, 3.2–3.9 gf at 13 m/s; 3.2 % blockage; Re 1,370–2,740 | §5 script |
| Full-span 1/4 in rod (6.35 mm) | 1.6–1.9 gf at 6.5 m/s, 6.4–7.7 gf at 13 m/s; 6.35 % blockage; Re 2,740–5,470 | §5 script |
| Full-span 3/8 in rod (9.525 mm) | 2.4–2.9 gf at 6.5 m/s, 9.7–11.6 gf at 13 m/s; 9.5 % blockage; Re 4,100–8,200 | §5 script |
| 3/4 in and 1 in balls at 13 m/s | 1.30 and 2.31 gf | §5 script, C_D 0.44 |
| Long-cylinder C_D at these Re | about 1.0–1.2 | textbook value from the agent's memory, not checked against a source |
| Panel from one 8 × 12 in sheet | 203 × 305 mm sheet: one 300 × 120 mm panel plus a strip about 83 mm wide | our arithmetic |
| K&S 3/8 in brass tube, 12 in | $3.69 (Super Arbor), $3.99 (Paul B Hardware, Hemlock Hardware), $8.87 (Walmart) | search snapshots, 2026-11-10 |
| 1/4 in acetal rod | $2.59 for 1 ft (Zoro), $1.77 a foot (Aircraft Spruce); McMaster's price not visible to the search | search snapshots, 2026-11-10 |

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests -v`: 20 tests OK in 14.8 s (catch-up) and 21.9 s (wrap), Python 3.11.0.
- `python scripts/check_docs.py`: 0 failures, 0 warnings at catch-up and after the mid-session edits. At the wrap,
  before this log existed: 7 failures, all links to this log (expected). After writing it: 0 failures, 0 warnings.
- `python docs/drawings/page.py`: before editing, the rebuild left `git status` clean (the generator is deterministic).
  After editing: "parts never drawn: []"; the page contains no "Adafruit"; its diff is only the three parts rows and
  the revision note. `preview.py` was not run: no sheet geometry changed.
- Not performed: any physical check. No part has arrived.

## 8. Errors, failed approaches and troubleshooting

- **The first cylinder question was misread.** The agent answered for the brass cylinders in the TODO P3 ideas; the
  owner meant precise plastic cylinders bought from McMaster, like the Delrin balls. Both answers came to the same
  advice (not now). When "should I buy X too" is ambiguous, ask what it is for and where from before answering.
- Rows set to "Ordered" in the drawings' parts list have no entry in `page.py`'s `STATUS_CLS` map, so they render in
  the neutral grey "feat" style. Acceptable; add a class when all statuses are updated at sizing.
- `check_docs.py` failed on 7 links while this log was still unwritten (order of work, not a fault).

## 9. Decisions and reasoning

- No DECISIONS.md entry. Owner's facts recorded: four 8 × 12 in acrylic sheets; SDP810 order Mouser 403-SDP810-125PA.
- Agent's advice, not a decision: no cylinders for now; a 1/4 in Delrin rod if a cylinder test is wanted later.

## 10. Open questions and blockers

- Heat-set inserts' length and outside diameter (needed for the flange and frame holes).
- Filament on hand, the "check house" items, and what the school lab balance reads to (open question 16).
- The fan model (D-011, Tentative), needed before the fan stand is designed.
- Whether sizing should leave room for a cylinder test (TODO P3 idea 6).
- The drawings' other parts statuses, the 5/32 in sleeve and the published claude.ai copy are out of date until the
  sizing update.

## 11. Remaining tasks

- Owner: commit and push (§13); send the inserts' size; report filament, check-house items and the balance's
  readability; answer the cylinder question; choose the fan; mark parts "Got it" and do each arrival check.
- Agent: build step 1 (sizing), with the drawings updated afterwards (sleeve, statuses, and the republished copy if
  the owner wants it).

## 12. Recommended first task for the next agent

Start build step 1 (sizing) with the settling-chamber spacing: Mehta1979's 0.2 D (about 200 mm) against full-decay
spacing (about 380–390 mm plus frames with the chosen screen and 6 mm cells), then how the 250 mm sections split for
the 256 mm bed (PROJECT_STATUS open questions 13 and 15). Neither needs the owner's inputs. Ask the owner for the
heat-set insert size (the flanges and frames depend on it) and whether to leave room for a cylinder test. If the owner
reports parts arriving, record each arrival check in `docs/experimental_setup.md` first.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `f5616a3`; nothing staged; 11 files modified and 1 new (this log).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add PROJECT_STATUS.md TODO.md PROJECT_BACKGROUND.md docs/experimental_setup.md docs/buy_list.md docs/shopping_list.md
git add docs/drawings/wtdata.py docs/drawings/page.py docs/drawings/wind-tunnel-drawings.html
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-10-parts-ordering.md docs/sessions/2026-11-10-order-details-and-cylinders.md
git status
git diff --cached --stat
git commit -m "Record acrylic sheets, SDP810 order and Waveshare BME280" -m "The owner reported four 8 x 12 in acrylic sheets and confirmed the Mouser order as 403-SDP810-125PA. Names the Waveshare BME280 in PROJECT_BACKGROUND and the drawings' parts list (rebuilt), fixes stale settling-chamber, diffuser-screen and sphere entries, and records advice against buying cylinders for now. Backfills f5616a3."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 12 paths under "Changes to be committed". Nothing else should be left.
- **Harmless warnings:** "LF will be replaced by CRLF" (or the reverse) can be ignored.
- **If the push asks for credentials:** `gh auth status` or `gh auth login`, or sign in through Git Credential Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- The last command should end with `STATE: UP_TO_DATE`.
