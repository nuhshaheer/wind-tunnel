# 2026-11-10: Consistency audit

- **Session ID:** 90885266-4724-4915-ad78-adb18be8a46b (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

Documentation and drawings only. Nothing arrived, was built or was tested. The work ran on the evening of 2026-11-10
(local time); the conversation was summarized once to free context, and `/wrap` ran on 2026-11-11.

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `2ac0809` (the owner had committed and pushed the order-details session). Working tree
  clean. `check_docs.py` 0 failures, 0 warnings; 20 tests OK in 13.8 s.
- Discrepancies found at catch-up:
  1. The commit records were one push behind: the PROJECT_STATUS header, §4 and §13, the SESSION_LOG row and the
     order-details log still said "not committed yet" or stopped at `f5616a3`, and TODO had no Done entry for the
     push. This is the expected lag after a push. Fixed this session.
  2. `docs/experimental_setup.md` said the sphere was "Chosen; to buy", but the balls are ordered. Fixed.
  3. PROJECT_STATUS §12 put "(answered 2026-11-10: the acrylic…)" right after the heat-set insert request, so the
     inserts looked answered. They are still open. Fixed.
  4. PROJECT_STATUS is long (598 lines, 64 KB at catch-up) for a "concise snapshot". Not changed: the owner's call (§10).
  5. The drawings still showed the 5/32 in sleeve and the part statuses from before the orders (left for sizing at
     the time), and the owner's published claude.ai copy was out of date. Fixed in the repo (revision C). The
     published copy still shows revision B.
- Objective (owner): "can you go thorugh each folder, and make sure that everythign is updated to the lastest of waht
  we have. likfe for example, we arn't using a 5/32 brash rod anymore, and we are doing a removable floor with the
  sting shield attached to the floor".

## 2. Work completed

**Method.** The agent read every live doc and index, then searched them for superseded terms. The files read were
README, CLAUDE.md, PROJECT_STATUS, TODO, PROJECT_BACKGROUND, DECISIONS, docs/experimental_setup.md, the buy list, the
shopping list, the data catalog, data/README, docs/sketches/README, resources/README, and the docs/drawings/ README
and scripts. The search terms were: sleeve, 5/32, stem, slot, plug, fixed shield, brass M3 / brass screws, set screw,
20 mm / 25 mm sphere, Uno, "To buy" and "not committed". Each hit was compared with:
- the latest decisions, D-012 to D-016;
- the owner's tracker, [docs/shopping_list.md](../shopping_list.md), the source for every "ordered" status;
- the 2026-11-09/10 session logs.

Dated history was left as written:
- old session logs;
- the bodies of DECISIONS entries;
- entries already marked dropped or struck through;
- the reading notes in `resources/notes/`.

**The owner's two examples:**
- **No 5/32 in sleeve ([D-016](../../DECISIONS.md)).** The remaining sleeve and ball-stem wording was replaced in:
  - PROJECT_BACKGROUND: measurement approach step 3 and the calibration step;
  - the buy list: the §6 subtotal, ball fixing and the spin check, the drill size, the §9 calibration load and the
    thread loop;
  - docs/sketches/README.md and TODO.

  The drawings were revised (below).
- **Removable floor with the shield attached ([D-014](../../DECISIONS.md)).** Two docs still described the old mount:
  - docs/experimental_setup.md, sphere row: "a fixed, streamlined printed shield and a floor slot";
  - PROJECT_BACKGROUND, step 3: "a floor slot".

  Both now describe the replaceable sphere floor insert. It carries the sting hole, the shield is attached to it, and
  both lift out together once the sting is out. The buy list's shield note says the same, and the README gained one
  sentence on how the model is held. The drawings already drew the shield on insert 53; their text now says
  "attached".

**Other stale entries fixed:**
- **Brass screws at the balance** (dropped 2026-11-09 for stainless):
  - the drawings: items 65, 68, 69 and 73 and the sheet notes;
  - PROJECT_BACKGROUND;
  - PROJECT_STATUS open question 12;
  - the buy list: the §2 brass-set row struck through.
- **Order statuses,** all taken from the shopping list:
  - the buy list's summary table (§1, 2, 4, 5, 6, 9 and 10);
  - the setup doc: balls, sting rods, HX711, LR44;
  - about 30 rows of the drawings' parts list.
- **Screens.** The setup row and drawing sheets 1 and 4 now give the ordered roll (0.011 in wire per the maker), with
  three diffuser screens planned for margin. They had said "three only if the wire is 0.010 in".
- **Buy list wording:** "stainless screen mesh" corrected to aluminium window screen (tin snips row); the BME280
  placement note no longer mentions a display (D-012).
- **docs/sketches/README.md:**
  - the knob menu marked dropped (D-012);
  - the exit diffuser noted as now an open exit (D-007, Tentative);
  - the 10.2 MiB PDF's "compress before committing" replaced by "committed uncompressed in `8fda08f`";
  - each ball's own sting noted (D-016).
- **resources/README.md, "Wanted" list:**
  - the parts were chosen on 2026-11-08;
  - the SDP3x and HSC datasheets are no longer needed;
  - the LM7805 was proposed for a servo that is no longer planned;
  - the BME280 datasheet is still wanted.
- **PROJECT_BACKGROUND, top-speed section:** a note that 20 and 25 mm were the proposed sizes, with the chosen balls'
  forces copied from the buy list §6.
- **Data indexes:** data/README.md and docs/data_catalog.md now say "no data (as of 2026-11-10)" instead of
  2026-10-29.
- **Commit records:** `2ac0809` backfilled in PROJECT_STATUS, SESSION_LOG, the order-details log and TODO.
- **DECISIONS.md** (append-only):
  - a dated note under D-015: stems and sleeve dropped by D-016, and stainless screws are fine at the balance;
  - at the wrap, a dated note under D-016 that the drawings no longer show the sleeve.

**Drawings, revision C** ([docs/drawings/](../drawings/README.md); generated, never hand-edited):
- **Unused draft code deleted first.** The superseded draft sheet functions in `s_d1.py`, `s_d2.py` and `s_d3.py`
  (1,072 lines, some still drawing the sleeve) were deleted. The page rebuilt byte-identical to the copy saved before
  (`cmp`, §7), so the deletion changed nothing visible.
- **`wtdata.py`:**
  - `sleeve_d` removed, and items 61 (ball stem) and 62 (sting sleeve) removed; their numbers are not reused;
  - item 63 (sting): one per ball, quantity "3 + spares", Ordered;
  - 64 (shield): attached to the sphere insert 53 and lifting out with it;
  - 53 updated to match; 54 is the plain insert, with no shield, and replaces the floor plug;
  - 60 (balls): one of each in use, from packs of 10;
  - 73 renamed "Short M3 screw" (stainless, from the assortment); 65, 68 and 69 changed from brass to stainless;
  - 74: the calibration attachment on its own sting;
  - 12: the screen as ordered, quantity 5, with 12b planned for margin;
  - 92: the TUOFENG wire; 96: measure on arrival; 100: pads from the 20-pack of feet;
  - status "Ordered" for items 4, 5, 7, 12, 46, 51, 60, 63, 66, 72, 73, 76, 80, 82–87, 92, 96, 97 and 100.
- **Sheets 7 and 8 (`s_d2b.py`):**
  - one sting drawn from the ball's centre down to the mount, in place of the sleeve and stem;
  - balloons 61 and 62 removed, and the press-fit leader note revised;
  - sheet 8 notes 4 and 5 (shield on the insert; one sting per ball) and sheet 7 note 6 (stainless screws)
    rewritten.
- **Sheets 1, 2, 4 and 10** (`s_ga.py`, `s_ga2.py`, `s_d1b.py`, `s_d3b.py`): the screen 12b note; joint J8's fastener
  changed to "Short M3 73"; the sheet 10 note and table rows 73 and 100.
- **`page.py`:**
  - an "Ordered" status style (`.st.ord`);
  - the TBD register: the 12b row, and "sting length (all cut equal)" in place of the sleeve and stem row;
  - the lede, the revision C note and the footer.
- **`wtlib.py`:** the title-block date and basis.
- **README:** revision C described; it notes that the published claude.ai copy still shows revision B.

## 3. Files and equipment affected

- `PROJECT_STATUS.md`:
  - header: last commit `2ac0809`, the not-committed note;
  - the stage paragraph: the drawing package line (revision C);
  - §4: the drawing row (revision C, published copy not republished) and the `/wrap` commit list;
  - §6: `2ac0809`, and this session's entry;
  - §9: test timings;
  - §10: open question 12 (stainless);
  - §12: next steps, including the republish and file-length questions;
  - §13: commit list.
- `TODO.md`: sting hole; the drawings note; the screen note; a note on the 2026-11-08 balls entry; D-016 added to the
  tentative-decision task; a new P0 task to decide on republishing the drawings; Done entries for the `2ac0809` push
  and this audit.
- `PROJECT_BACKGROUND.md`: measurement step 3 (floor and shield, stainless screws, one sting per ball), the
  calibration step, the chosen balls' forces.
- `DECISIONS.md`: dated notes under D-015 and D-016 (nothing else changed).
- `README.md`: one sentence on the model mount.
- `docs/experimental_setup.md`: current configuration, the CAD, screens, HX711, sphere and calipers rows, change
  history.
- `docs/buy_list.md`: last updated, the summary table, §2, §6, §7, §9, §10.
- `docs/drawings/`:
  - `README.md`, `page.py`, `wtdata.py`, `wtlib.py`;
  - `s_d1.py`, `s_d2.py`, `s_d3.py` (drafts deleted);
  - `s_d1b.py`, `s_d2b.py`, `s_d3b.py`, `s_ga.py`, `s_ga2.py`;
  - `wind-tunnel-drawings.html` (rebuilt).
- `docs/sketches/README.md`, `resources/README.md`, `data/README.md`, `docs/data_catalog.md`.
- `docs/sessions/SESSION_LOG.md` (`2ac0809` backfilled; new row), `docs/sessions/2026-11-10-order-details-and-cylinders.md`
  (commit field backfilled: `2ac0809`), this log.
- Checked and not changed:
  - `CLAUDE.md` (still accurate);
  - `docs/shopping_list.md` (already current);
  - `resources/notes/` (dated reading notes);
  - older session logs.

  There is no `data/raw/`.
- Not published: the owner's private claude.ai copy of the drawings (still revision B).
- Equipment: none changed; nothing has arrived.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch          # catch-up and wrap: STATE: UP_TO_DATE at 2ac0809
python scripts/check_docs.py                   # see §7
python -m unittest discover -s tests -v        # see §7
python docs/drawings/page.py                   # rebuild after each drawing edit
python docs/drawings/preview.py 7 8            # before editing: the sheets that drew the sleeve
python docs/drawings/preview.py 1 2 4 7 8 10   # after editing (PNGs in docs/drawings/png/, gitignored)
```

Byte-identical check of the draft deletion (scratchpad path shortened to `$SP`):

```bash
cd docs/drawings
cp wind-tunnel-drawings.html "$SP/drawings-before.html"
# one-off Python: keep only the imported helpers in s_d1.py (lines 1-34 and 416-end), s_d2.py (1-31), s_d3.py (1-11)
python page.py && cmp wind-tunnel-drawings.html "$SP/drawings-before.html" && echo "IDENTICAL OUTPUT"
```

Text edits were made with a scratchpad helper, `replace_exact.py <file> <pairs.py>`. It applies `(old, new)` string
pairs only if every old string occurs exactly once, otherwise it writes nothing, and it keeps the file's line endings.
The helper and its pairs files lived in the session scratchpad and are not kept. The diff is the record.

Stale-term searches were run with `grep -n -i` over the live docs, using the terms in §2. Title-block crops of the
preview PNGs were made with PyMuPDF to check the notes by eye. The crop file was deleted afterwards.

## 6. Measurements and results

No measurements and no new estimates. One figure was copied into PROJECT_BACKGROUND rather than computed: the chosen
balls' drag. It is 0.30–1.27 gf (3/4 in) and 0.54–2.31 gf (1 in) at 6.5–13 m/s, an estimate from 2026-11-08 in
[docs/buy_list.md](../buy_list.md) §6.

## 7. Tests, calibration checks and validation

- **Draft deletion:** `cmp` of the rebuilt page against the copy saved before printed "IDENTICAL OUTPUT" (433 KB),
  with "parts never drawn: []".
- **After the content edits:**
  - `python docs/drawings/page.py`: "parts never drawn: []";
  - the only "sleeve" left in the page is the revision C note and "No sleeve" in the sting's spec;
  - sheets 1, 2, 4, 7, 8 and 10 were rendered and checked by eye; no overlapping text was found.
- **`python -m unittest discover -s tests -v`:** 20 tests OK, Python 3.11.0:
  - 13.8 s at catch-up;
  - 15.6 s after the edits;
  - 11.1 s at the wrap.
- **`python scripts/check_docs.py`:**
  - 0 failures, 0 warnings at catch-up;
  - 0 failures, 0 warnings after the edits (621 links);
  - 0 failures, 0 warnings at the wrap, after this log was written (637 links; 15 session logs, each indexed once;
    PROJECT_STATUS last updated 2026-11-11).
- **Drawings at the wrap:** `python docs/drawings/page.py` rebuilt the page to the same SHA-256 as the working copy
  (deterministic; nothing changed since the edits).
- **Not performed:** any physical check, since no part has arrived. The drawings are not checked against anything
  built.

## 8. Errors, failed approaches and troubleshooting

- **A bash heredoc failed.** A Python script inside an inline bash heredoc failed on a quote ("unexpected EOF while
  looking for matching `''"). Fixed by writing scripts to scratchpad files and running them.
- **Two replacement pairs did not match,** so nothing was written on those runs:
  - `wtdata.py` item 66: its quantity is on the same line as its spec;
  - `s_d3b.py` row 100: the last tuple ends in `)]`.

  Both pairs were corrected and rerun.
- **The first PyMuPDF crop came out wrong.** The page units differ from pixels; the crop box was rescaled.
- **The "fixed shield and a floor slot" wording survived D-014** (2026-11-09) and two later sessions that edited the
  same table row. Lesson: when a decision is recorded, search every live doc for the superseded words, not only the
  rows being edited.

## 9. Decisions and reasoning

- No new decision. D-014 and D-016 were applied consistently. Dated notes were appended to D-015 and D-016, since
  DECISIONS.md is append-only.
- Agent's choices, not owner decisions:
  - drawing items 61 and 62 are retired rather than renumbered, so older references stay unambiguous;
  - "Ordered" gets its own status style in the parts list;
  - dated history was left as written (see §2).

## 10. Open questions and blockers

- **Republish the drawings?** Whether to republish the owner's private claude.ai copy as revision C (TODO P0).
- **Shorten PROJECT_STATUS?** About 600 lines, against CLAUDE.md's "concise snapshot". Moving the dated history into
  the session logs would help (catch-up point 4; owner's call).
- **D-016 is still Tentative** (confirm at sizing).
- **From before:**
  - the heat-set inserts' length and outside diameter;
  - whether sizing should leave room for a cylinder test;
  - the fan (D-011);
  - the filament amounts and the "check house" items;
  - what the school balance reads to (open question 16);
  - the datasheet checklists.

## 11. Remaining tasks

- **Owner:**
  - commit and push (§13);
  - answer the republish and PROJECT_STATUS-length questions;
  - send the insert size;
  - report the filament, the check-house items and the balance's readability;
  - answer the cylinder question;
  - choose the fan;
  - mark parts "Got it" and do each arrival check.
- **Agent:** build step 1 (sizing), then update `wtdata.py` with the sized numbers and rebuild the drawings.

## 12. Recommended first task for the next agent

Start build step 1 (sizing) with the settling-chamber spacing: Mehta1979's 0.2 D (about 200 mm) against full-decay
spacing (about 380–390 mm plus frames with the chosen screen and 6 mm cells). Then work out how the 250 mm sections
split for the 256 mm bed (PROJECT_STATUS open questions 13 and 15). Neither needs the owner's inputs. Ask the owner
for the heat-set insert size, which the flanges and frames depend on. If the owner reports parts arriving, record
each arrival check in `docs/experimental_setup.md` first.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `2ac0809`; nothing staged. 26 files are modified and 1 is new (this log).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md README.md TODO.md data/README.md
git add docs/buy_list.md docs/data_catalog.md docs/experimental_setup.md docs/sketches/README.md resources/README.md
git add docs/drawings/README.md docs/drawings/page.py docs/drawings/wtdata.py docs/drawings/wtlib.py docs/drawings/wind-tunnel-drawings.html
git add docs/drawings/s_d1.py docs/drawings/s_d1b.py docs/drawings/s_d2.py docs/drawings/s_d2b.py docs/drawings/s_d3.py docs/drawings/s_d3b.py docs/drawings/s_ga.py docs/drawings/s_ga2.py
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-10-order-details-and-cylinders.md docs/sessions/2026-11-10-consistency-audit.md
git status
git diff --cached --stat
git commit -m "Bring docs and drawings up to the latest decisions" -m "At the owner's request every folder was checked against D-012 to D-016 and the orders. The sphere mount is now described through the replaceable floor insert with the shield attached (D-014); the 5/32 in sleeve and separate ball stems are gone from every live doc and the drawings (D-016, revision C); stainless screws at the balance; order statuses follow the shopping list. Unused draft sheet code deleted (page rebuilt byte-identical). Backfills 2ac0809."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 27 paths under "Changes to be committed", with nothing left over.
- **Harmless warnings:** "LF will be replaced by CRLF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
