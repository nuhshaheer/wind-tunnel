# 2026-11-17: Time estimates and CAD approach

- **Session ID:** 4dddb536-73db-480a-9aaf-1f52bf9a6275 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

Planning conversation only. Nothing arrived, was built, drawn or tested, and no repository file changed before the
wrap. Started 2026-11-15 with `/catchup`; `/wrap` ran on 2026-11-17.

## 1. Starting state and objective

- `/catchup` (2026-11-15): `UP_TO_DATE` at `5cb8b7a`, so the owner had committed and pushed the consistency audit
  (2026-11-11). Working tree clean. `check_docs.py` 0 failures, 0 warnings (637 links); 20 tests OK in 13.9 s.
- Discrepancies found at catch-up:
  1. The commit records were one push behind: the PROJECT_STATUS header, §4, §12 and §13, the SESSION_LOG row and the
     audit log's commit line still said "not committed yet" or stopped at `2ac0809`, and TODO had no Done entry for the
     push. `5cb8b7a` holds exactly the 27 files the audit log listed. The expected lag; backfilled in this wrap.
  2. PROJECT_STATUS is 611 lines (66 KB) against CLAUDE.md's "concise snapshot". Not changed: still the owner's call.
  3. The owner's private claude.ai copy of the drawings still shows revision B (TODO P0, unchanged).
- No data, analysis, results or firmware folders exist, which matches the data catalog.
- Objective (owner): "how long do you estimate it will take us to cad. additianollly, with all the parts, a resoable
  time estiamete to do the proejct. keep in mind i have school and other commitments". Then: whether an agent could do
  the CAD faster, and whether the agent could control the owner's desktop.

## 2. Work completed

1. **Time estimates** for the CAD and for the whole project up to the sphere validation, built part by part from the
   drawings' parts list and the build steps (§6). All are the agent's estimates, not measurements.
2. **CAD time revised after the owner's pushback.** The owner said CAD should take about 10 h. The agent's first figure
   (25–50 h) assumed average CAD speed and some design decisions made inside CAD. A part-by-part fast pass gives about
   10–17 h, plus 3–8 h of fixes after test prints, so 12–25 h, with 10 h as the best case. Three ways to reach the low
   end: finish the sizing first, draw the flange and screen frame once and reuse them, print test coupons before the
   big parts.
3. **Agent-drawn CAD discussed (not chosen).** Asked what a Fable agent at max effort, or "ultracode", would change:
   - an agent would write Python CAD scripts (CadQuery or build123d) exporting STEP and STL, with automatic checks
     (fits the 256 mm bed, bolt holes line up, wall thickness) and rendered views. Owner time about 3–6 h of review;
     the whole project about 60–135 h (estimate);
   - the model and effort level change how carefully the scripts are reasoned, not the physical loop (test prints,
     printing, assembly, calibration);
   - no "ultracode" mode is known to the agent; the closest, `/code-review ultra`, reviews code and builds nothing;
   - costs: a large new dependency (the project's scripts are standard-library only), STEP files without an editable
     feature history, and the owner not doing the CAD.
4. **Desktop control discussed (not available, not advised).** Computer use is not available in this VS Code
   extension session. It works through the Claude desktop app with Computer use turned on (Settings → This computer →
   Computer use; off by default), or on claude.ai through Devices in the + menu where offered. The agent advised that it
   would not improve CAD for a proficient user: it works screenshot by screenshot, and CAD needs picking edges and faces
   in a 3D view, dragging sketch geometry and filling constraint dialogs.
5. **The owner will do the CAD** ("no its fine ill do the CAD myself", 2026-11-15; the owner is "already proficient in
   CAD"). Recorded as [D-017](../../DECISIONS.md). The agent's side: one dimension sheet per part after sizing, the
   contraction wall as an importable points file, and checks of exported STLs on request.
6. **Wrap:** commit records backfilled (`5cb8b7a`), D-017 added, the estimates and the owner's time constraint recorded
   in PROJECT_STATUS and PROJECT_BACKGROUND, TODO updated.

## 3. Files and equipment affected

- `DECISIONS.md`: D-017 added.
- `PROJECT_STATUS.md`: header and last commit; current stage (D-017, the schedule estimate); §4 `/catchup` and `/wrap`
  rows; §6 the audit's commit and this session; §8 a pointer to the estimates; §12 next steps; §13 remote commits.
- `PROJECT_BACKGROUND.md`: two constraints added (the owner's time; the owner does the CAD).
- `TODO.md`: P0 owner details (CAD program, weekly hours, any deadline); P1 sizing deliverables and a new owner CAD
  task; Done entries for the `5cb8b7a` push and D-017.
- `docs/sessions/SESSION_LOG.md`: the audit row backfilled; this session's row added.
- `docs/sessions/2026-11-10-consistency-audit.md`: commit line backfilled to `5cb8b7a` (the only edit).
- `docs/sessions/2026-11-17-time-estimates-and-cad.md`: this log (new).
- Outside the repo: the agent's memory file `owner-does-cad-themselves.md` (Claude Code's per-project memory).
- Equipment: none.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch            # 2026-11-15: STATE: UP_TO_DATE at 5cb8b7a
cat PROJECT_STATUS.md && cat TODO.md             # output too large (113.7 KB); read in parts instead
wc -lc PROJECT_STATUS.md TODO.md                 # 611 and 564 lines
git status --short                               # empty
git log --format="%h %ad %s" --date=short -15
git show --stat 5cb8b7a                          # 27 files, matching the audit log's §13 list
git remote -v                                    # https://github.com/nuhshaheer/wind-tunnel.git
python scripts/check_docs.py                     # 0 failures, 0 warnings
python -m unittest discover -s tests             # 20 tests OK, 13.865 s
ls data data/raw data/processed results analysis firmware   # only data/README.md exists
grep -rn "not committed yet" --include=*.md .    # stale commit records (§1)
grep -n -i "print" docs/drawings/wtdata.py       # printed parts, for the CAD estimate
# wrap, 2026-11-17:
python scripts/sync_status.py --fetch            # STATE: UP_TO_DATE at 5cb8b7a; 0 uncommitted paths
git log --format=%h -1 -- docs/sessions/2026-11-10-consistency-audit.md   # 5cb8b7a
python -m unittest discover -s tests -v
python scripts/check_docs.py
```

No calculation scripts: the estimates in §6 are hand arithmetic on the figures shown.

## 6. Measurements and results

No measurements. **Planning estimates only (agent's judgement, not results):**

- **CAD, owner's hours.** First estimate at average CAD speed, including fixes: contraction 4–8, diffuser and fan ring
  3–6, settling chamber with honeycomb and screen frames 3–5, test section 5–10, floor inserts and sting shield 1–3,
  balance module 4–8, about 10 small parts 3–6, fit check and slicing 2–4; **total 25–50 h**. Revised for a fluent
  user: a first pass of about 10–17 h (contraction 1.5–3, test section 2–4, balance 1.5–3, diffuser 1–2, settling
  chamber 1–2, small parts 2.5–3), plus 3–8 h of fixes: **12–25 h**. Owner's own estimate: about 10 h.
- **Whole project to the sphere validation, owner's hours:** reviewing the sizing 2–4, CAD (as above), printing work
  (slicing, plate swaps, sanding, heat-set inserts) 10–20, electronics bring-up 10–20, assembly 8–15, calibrations and
  flow map 10–20, sphere runs 10–20, troubleshooting 10–30. **85–180 h** with the first CAD figure, **about 70–155 h**
  with 12–25 h of CAD.
- **Printer time:** about 80–200 h for 3.5–5 kg (PLA 3–4 kg and PETG-CF 0.5–1 kg, TODO P0) at an assumed 25–45 g/h,
  more with reprints. The rate is a guess for the P1S, not measured; the slicer will give the real figure. Mostly
  unattended and overlapping the CAD.
- **Calendar** (the owner's weekly hours were not stated, so these are assumed, from 2026-11-15):
  - with 85–180 h: 4–5 h a week gives 4–10 months (March–September 2027), 6–8 h gives 2.5–7 months (late January–June
    2027), 10 h gives 2–4 months (mid-January–March 2027);
  - with 70–155 h at 6–8 h a week: about mid-January to mid-May 2027.
- **Agent-drawn CAD (not chosen):** owner review about 3–6 h; whole project about 60–135 h, early January to late April
  2027 at 6–8 h a week.
- **What could make it run long (estimates):** a balance or shield redesign, +10–20 h and 2–4 weeks; each reprint of a
  large section, 10–20 h of printer time; a PCB before the validation, +10–20 h of design and typically 1–3 weeks'
  shipping (general knowledge, not checked); learning CAD, +50–100 % (does not apply: the owner is proficient).

## 7. Tests, calibration checks and validation

- **At catch-up (2026-11-15):** `check_docs.py` 0 failures, 0 warnings (637 links); 20 tests OK in 13.9 s.
- **At the wrap (2026-11-17), after the doc edits:**
  - `python -m unittest discover -s tests -v`: 20 tests OK in 20.2 s (Python 3.11.0);
  - `python scripts/check_docs.py`: 0 failures, 0 warnings (654 links; 16 session logs, each indexed once;
    PROJECT_STATUS last updated 2026-11-17).
- **Not performed:** any physical check; no part was reported as arrived. The time estimates are not checked against
  anything.

## 8. Errors, failed approaches and troubleshooting

- Reading PROJECT_STATUS and TODO in one `cat` exceeded the tool's output limit (113.7 KB); they were read in parts.
- Desktop control: no computer-use tools exist in this VS Code session, so it could not be offered here.
- Two statements in the conversation came from the agent's general knowledge and were not checked: that Fusion ships an
  import-spline-from-CSV sample script, and the 1–3 week PCB shipping time.

## 9. Decisions and reasoning

- [D-017](../../DECISIONS.md) (Accepted, owner, 2026-11-15): the owner draws all the CAD; the agent supplies dimension
  sheets, the contraction points file and STL checks. Reasoning in the entry: the owner is fluent; script CAD adds a
  large dependency and loses the feature history; desktop control is slower than the owner in a 3D view.
- Agent's choice: the session log is named for the wrap date (2026-11-17), as most earlier logs are.

## 10. Open questions and blockers

- **Asked this session, not answered:**
  - which CAD program the owner uses (sets the points file's format);
  - how many hours a week the owner can give, and any deadline (school or a fair); they would narrow the schedule;
  - whether any parcels have arrived (ordered 2026-11-09/10);
  - whether to start the sizing now.
- **From before:** the heat-set insert length and outside diameter; the fan (D-011); filament amounts and the "check
  house" items; what the school balance reads to (open question 16); the datasheet checklists; whether to republish the
  drawings and to shorten PROJECT_STATUS; room for a cylinder test; D-016 and the other tentative decisions.

## 11. Remaining tasks

- **Owner:** commit and push (§13); answer the questions in §10; mark parts "Got it" and do each arrival check.
- **Agent:** build step 1 (sizing), delivering a dimension sheet per part and the contraction points file (D-017); then
  update `wtdata.py` and rebuild the drawings; check the owner's STLs when they exist.

## 12. Recommended first task for the next agent

Unchanged from the audit: start the sizing with the settling-chamber spacing (Mehta1979's 0.2 D, about 200 mm, against
full-decay spacing, about 380–390 mm plus frames), then how the 250 mm sections split for the 256 mm bed (PROJECT_STATUS
open questions 13 and 15). Write the results as dimension sheets the owner can draw from (D-017). If the owner reports
parts arriving, record each arrival check in `docs/experimental_setup.md` first. Ask for the CAD program before writing
the contraction points file.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `5cb8b7a`; nothing staged. 6 files modified and 1 new (this log).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md TODO.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-10-consistency-audit.md docs/sessions/2026-11-17-time-estimates-and-cad.md
git status
git diff --cached --stat
git commit -m "Record time estimates and owner-drawn CAD (D-017)" -m "The owner asked how long the CAD and the whole project would take around school; the estimates are recorded with their assumptions. The owner will draw every part (D-017), so sizing delivers dimension sheets and a contraction points file. Backfills 5cb8b7a."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 7 paths under "Changes to be committed", with nothing left over.
- **Harmless warnings:** "LF will be replaced by CRLF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
