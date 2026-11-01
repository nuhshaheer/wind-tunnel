# 2026-10-31: Blockage review and tunnel concepts

- **Session ID:** 27e877ae-fe62-4bfe-9a84-8d8aecd9ff14 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

## 1. Starting state and objective

**Starting state** (from `/catchup`, 2026-10-31):

- Sync state `UP_TO_DATE` at `7db221f`. The owner had pushed the previous session's commit with the commands its
  `/wrap` gave (same 24 files and message). Clean working tree.
- `check_docs.py`: 0 failures, 0 warnings. Tests: 20/20 passed.
- Discrepancies found (fixed at this wrap):
  - PROJECT_STATUS, TODO, SESSION_LOG and the reference-library log still said that session was "not committed
    yet".
  - PROJECT_STATUS §13 did not list `7db221f`.
- Project: planning / pre-build, nothing built. The owner's sizing inputs and kit list are still missing.

**Objectives (owner requests, in order):**

1. Start the recommended first task: review Maskell1963 and Cooper1998. Before starting, the owner asked whether the
   agent can read scans without a text layer.
2. "What is our current plan for use of the electronics? Tell it to me."
3. The owner's questions and ideas:
   - "All of the ones I see online are purely for seeing the streamlines … how can we integrate the streamlines of
     water vapor with the fan still attached? Is that possible, is that worth it?"
   - A circuit "with a dial to control the angle of attack" for a wing ("nothing final").
4. "If I have a fan behind the water vapor, how will the water vapor flow be laminar before approaching the object?
   Also, how do we plan on measuring?"
5. "Would it be better to change the project so that it pulls the air instead of pushes it?" The owner thought a
   suction tunnel "won't be like a real wind tunnel" and that "we won't get any measurements", and concluded: "I
   guess I can worry about the vapor till the end then … just me adding some sort of hole to feed the air mist into."
6. Run `/wrap`.

## 2. Work completed

**Scan reading.** The agent confirmed it can read image-only scans:
- PyMuPDF renders each page to PNG and the agent reads the images.
- High-zoom crops are used for equations.
- For Cooper1998, the full AGARD volume's (Ewald1998) text layer was used as a cross-check for prose.

**Maskell1963 reviewed** ([notes](../../resources/notes/Maskell1963.md)), all 27 page images:
- The correction: Δq/q = ε C_D S/C, with ε = 1/(k_c² − 1) and k² = 1 − C_pb.
- ε = 5/2 for 3-D flow (2.75 better for axisymmetric wakes) and 0.96 for 2-D.
- The square-plate evidence (Tables 1–5).
- The composite stalled-wing formula, eq. 18.
- **Caveat recorded:** §2.6 says well-rounded bodies (like the circular cylinder) may have to be excluded, because
  their separation point can move. A sphere is such a body.

**Cooper1998 reviewed** ([notes](../../resources/notes/Cooper1998.md)):
- Text from Ewald1998's text layer. Every closed-section equation and Figs. 6.1–6.7 checked against the page images.
- Covers:
  - Maskell's eqs. 6.1–6.6;
  - Cowdrey;
  - Hackett's two-step version (6.13–6.15b);
  - wake buoyancy (6.16–6.18), which Cooper calls unsettled;
  - model-position rules: reference taps at least 1.5√C upstream of the model; model base at least 2√S_b,
    preferably 4√S_b, from the test-section end;
  - parachute θ = 1.85;
  - the 2-D cylinder evidence (Farell et al.).
- The open-jet sections were read as text only.

**Estimates and checks** (our arithmetic; formulas and assumptions are restated in the Cooper1998 notes):
- Correction sizes against θ.
- Maskell against Hackett for a sphere at 3 % and 5 % blockage.
- Solid-blockage order of magnitude.
- Position distances for square sections of 150, 200 and 250 mm.
- Eq. (6.15b) checked algebraically and numerically against (6.15a).

**Index:** [resources/README.md](../../resources/README.md) rows for Maskell1963 and Cooper1998 set to "Reviewed
2026-10-31", with links to the notes.

**Electronics plan explained to the owner** (no doc change needed; it is the existing PROJECT_STATUS §3 and TODO P1
content):
- pitot → differential pressure sensor;
- sphere on a sting → load cell → HX711;
- BME280 candidate for p and T;
- Arduino-class board → USB → CSV → Python;
- the op-amps have no defined job yet.

**Owner's questions answered** (recorded as proposals, not decisions):

- **Visualization vs measurement tunnels.** Both have the same skeleton and both run a fan. A measurement tunnel is
  faster and carries instruments.
- **Mist with the fan running.** Possible:
  - inject after the last screen, before the contraction;
  - push it in a blower tunnel; it is drawn in by itself in a suction tunnel;
  - match the jet speed to the air;
  - clean streaks only at low speed; never during measurements.
  - The agent judged it worth having as a late add-on, not a design driver. Cheap ways to keep the option open: a
    capped port and a test-section window. Tufts suggested for stall.
- **Laminar streaks.** The flow conditioning (honeycomb, screens, contraction), not the fan position, makes the
  stream smooth. The mist only marks the air.
- **Measurement plan explained:**
  - C_D = F/(q·A), with q from the pitot-static tube, so ρ does not enter C_D and is needed only for V and Re;
  - sting through a floor slot to an upright load cell;
  - calibration in the drag direction (pulley);
  - wind-off tare → wind-on average → wind-off zero; mount-drag subtraction; blockage correction; comparison with
    the Re-matched reference.
- **Blower vs suction.**
  - The agent corrected the owner's assumption: a suction tunnel is a real measurement tunnel.
  - The agent's lean is still blower with an open exit. Its test section sits near room pressure, so print seams and
    the sting slot barely leak; in a suction tunnel they leak inward next to the sphere unless sealed.
  - The owner deferred the mist to the end, with a port to feed it in.
- **Angle-of-attack dial** (owner's idea). Proposed form: potentiometer → Arduino → servo, with the angle logged.
  Caveats: commanded vs actual angle, servo jitter on the balance, wires crossing onto the balance.

**Documentation updated at this wrap:** see §3.

## 3. Files and equipment affected

**Created:**
- `resources/notes/Maskell1963.md`
- `resources/notes/Cooper1998.md`
- this log

**Modified:**

- `resources/README.md`: two index rows set to Reviewed, with notes links.
- `PROJECT_BACKGROUND.md`:
  - new "Blockage correction [Proposed]" subsection;
  - measurement approach (density, pitot placement, calibration direction);
  - Maskell1963 and Cooper1998 moved to "Reviewed";
  - new lesson on OCR text layers.
- `PROJECT_STATUS.md`:
  - last commit `7db221f`; stage; tunnel-type lean; test-section proposals; servo idea; mist deferred;
  - open questions 2, 7 and 8 updated, and new question 10 (airspeed reference placement);
  - findings; next steps; repository.
- `TODO.md`:
  - P0 commit task now points to this session;
  - P1 review task reduced to Morrison2013 and Roos1971;
  - sizing inputs, Barlow chapters and the blockage-method task updated;
  - P2 mist task updated; P2 validation run gains a two-sphere-size check; P3 dial idea added;
  - two Done entries.
- `docs/experimental_setup.md`: ambient-sensor rows corrected from "Not planned yet"; change-history row added.
- `docs/sessions/SESSION_LOG.md`: `7db221f` backfilled; this session's row added.
- `docs/sessions/2026-10-31-reference-library-and-electronics.md`: commit field backfilled to `7db221f` (the only
  edit to that log).

**Not changed:** DECISIONS.md (no decision made; the owner said "nothing final"), docs/data_catalog.md (no data),
README.md and CLAUDE.md (still accurate).

**Equipment:** none.

**Scratch files** (outside the repo, in the session scratchpad):
- `scripts/render.py`: PyMuPDF page renderer with an optional clip rectangle.
- `scripts/blockage_estimates.py`: the estimates in §6.
- Page renders.
- `txt/cooper_ch6.txt`: Ewald1998 pages 332–364 as text.

## 4. Experimental procedures performed

None. No physical work this session; no hardware exists yet.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                 # /catchup and /wrap: UP_TO_DATE at 7db221f
git status --short; git log --oneline -15; git show --stat 7db221f; git diff
python scripts/check_docs.py
python -m unittest discover -s tests [-v]
python -c "import pymupdf; print(pymupdf.__version__)"   # 1.28.2; pdftotext at /mingw64/bin/pdftotext
python -I <scratch>/scripts/render.py resources/Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf <scratch>/maskell 1.6 all
python -I <scratch>/scripts/render.py resources/Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf <scratch>/maskell_zoom 3.5 11 0.1 0.36 0.9 0.5
pdftotext -f 332 -l 364 -layout resources/Ewald1998_wind-tunnel-wall-correction-AGARD-AG-336.pdf <scratch>/txt/cooper_ch6.txt
python -I <scratch>/scripts/render.py resources/Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf <scratch>/cooper 1.6 7-17
python -I <scratch>/scripts/render.py resources/Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf <scratch>/cooper_zoom 4 10 0.25 0.5 0.95 0.56
python -I <scratch>/scripts/render.py resources/Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf <scratch>/cooper_zoom 4 12 0.12 0.4 0.95 0.6
python -I <scratch>/scripts/render.py resources/Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf <scratch>/cooper 1.6 32-33
python -I <scratch>/scripts/blockage_estimates.py
```

`render.py` arguments: `<pdf> <outdir> <zoom> <pages> [x0 y0 x1 y1]`, with the clip given as fractions of the page.

## 6. Measurements and results

No measurements. Calculated estimates only. Status: estimate, not a result. Assumptions: C_D = 0.47, square closed
test sections.

**Δq/q = θ C_D S/C:**

| S/C | θ = 1.85 | θ = 2.5 | θ = 2.77 |
|---|---|---|---|
| 3 % | 2.61 % | 3.52 % | 3.91 % |
| 5 % | 4.35 % | 5.88 % | 6.51 % |

- The spread is about ±0.65 % of C_D at 3 % blockage and ±1.1 % at 5 %.
- Keeping Δq ≤ 0.1 q (Maskell p. 13) needs S/C ≤ 8.5 % at θ = 2.5.

**Maskell vs Hackett** (θ = 2.5): if the true C_D is 0.47, the measured C_Du would be 0.4872 at S/C = 3 % and 0.4993
at 5 %.
- Maskell returns 0.4700 for both.
- Hackett returns 0.4700 and 0.4701 (ΔC_DM = −0.0006 and −0.0015).
- The methods agree within 0.1 %.

**Solid blockage** (eq. 6.16 form, ε_s = T V/C^{3/2}, T = 0.72): ε_s = 0.28 % at 3 % blockage (0.56 % in q) and 0.61 %
at 5 % (1.21 % in q), whatever the section size. These rise by half with a sphere's effective volume of 1.5 V.

**Positions:**

| h | 1.5√C | Sphere d (3 % / 5 %) | 4√S (3 % / 5 %) |
|---|---|---|---|
| 150 mm | 225 mm | 29.3 / 37.8 mm | 104 / 134 mm |
| 200 mm | 300 mm | 39.1 / 50.5 mm | 139 / 179 mm |
| 250 mm | 375 mm | 48.9 / 63.1 mm | 173 / 224 mm |

- Test-section length for h = 200 mm with Mehta's 0.5 D settling distance added: about 2.7–2.9 h.

**Upstream decay check, eq. 6.21:** ε_u/ε = 0.0848 at x = √C, 0.0505 at 1.1√C, 0.0039 at 1.5√C. This
contradicts Cooper's text ("√C … five percent"); see §8.

**Wake-induced increment, eq. 6.18:** −0.35 % of C_D at 3 % blockage and −0.6 % at 5 %.

**Other figures given to the owner in chat:**
- the drag of a 50 mm sphere at 10 m/s (about 5.7 gf, q ≈ 60 Pa), from the existing PROJECT_BACKGROUND table;
- the suction-tunnel test-section pressure below room pressure: about 75 Pa at 10 m/s and 300 Pa at 20 m/s, taking
  q plus about 0.2 q of screen and friction losses (our estimate, from the Mehta1979 loss values in
  PROJECT_BACKGROUND).

## 7. Tests, calibration checks and validation

| Check | Outcome |
|---|---|
| `python scripts/check_docs.py` (at `/catchup`) | 0 failures, 0 warnings |
| `python -m unittest discover -s tests` (at `/catchup`) | 20 tests, all passed |
| Equation transcriptions | Maskell eqs. 16–17 and Cooper eqs. 6.6 and 6.13–6.15b read from zoomed page images; eq. 6.15b verified algebraically and by the script's assertion against the quadratic root |
| Reference years | Cooper's reference list read from page images (pp. 6-32 and 6-33) to correct OCR errors in years and report numbers |
| `/wrap`: `python -m unittest discover -s tests -v` | 20 tests, all passed (no code changed) |
| `/wrap`: `python scripts/check_docs.py` (final, after this log) | 0 failures, 0 warnings: 4 session logs each indexed once, 176 links and anchors resolve, 46 committable files, none over 25 MiB, no secrets. `git status --short`: 10 paths (7 modified, 3 new), matching the §13 `git add` list |
| Not checked | Maskell Figs. 9–11 (stalled wings); Cooper §6.2.6 (Mercker) and the open-jet sections beyond the text layer; the solid-blockage formula against Barlow1999 |
| Calibration or equipment checks | **None performed.** No hardware exists |

## 8. Errors, failed approaches and troubleshooting

- **The OCR text layer misreads numbers.** Ewald1998's text layer gives Cooper's eq. (6.6) as 0.98 + …; the page shows
  0.96. It also garbles θ into "8" or "6", and its reference list misreads years ("Nov. 1985" for Maskell's 1965).
  Equations and numbers were taken from page images. Recorded as a lesson in PROJECT_BACKGROUND.md.
- **Inconsistencies in Cooper1998 itself:**
  - The text says a model at √C from the reference taps keeps their error "at five percent", but eq. (6.21) as
    printed gives 8.5 % there (5 % at about 1.1√C). The 1.5√C → 0.5 % rule agrees with the equation.
  - "(5.15a)" is a misprint for (6.15a).
  - Reference [32] is numbered SAND89-1485 but dated December 1985.
- **Agent slip, caught and fixed:** the first draft of the Cooper1998 notes gave Macha and Buffington as "1989" before
  the reference page was checked.
- **Failed edit approach:** a Python heredoc replacing the two `resources/README.md` index rows stopped at its
  exact-match assertion and wrote nothing. The cause was not diagnosed. The rows were edited with the Edit tool
  instead.

## 9. Decisions and reasoning

No DECISIONS.md entry: nothing was decided, and the owner said "nothing final". Recorded as proposals or leans:

- **Blockage correction** [Proposed]: Maskell, θ = 2.5, plus solid blockage, checked with two sphere sizes
  ([PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#blockage-correction-proposed)). Becomes a D-entry once the
  test section and sphere are chosen.
- **Closed test section** [Proposed]: closed-section corrections are better developed (Cooper1998 §6.1.2).
- **Tunnel type: lean toward a blower with an open exit** (agent, not decided).
  - Reason: low leakage at seams and at the sting slot. Suction is still acceptable with a sealed balance box.
  - Decide with the fan.
  - An exit diffuser would put a blower's test section below room pressure too (open question 7).
- **Mist deferred to the end** (owner). Only a capped port after the last screen and a test-section window are
  planned now.
- **Angle-of-attack dial** (owner's idea): recorded in TODO P3 with the agent's proposed form and caveats.

## 10. Open questions and blockers

- **Owner inputs needed for sizing:** bench length, target top speed, any fan in mind (unchanged).
- **ECE kit contents** (unchanged).
- D-003, D-004 and D-006 are still Tentative.
- **Blockage:**
  - solid-blockage formula (Barlow1999 ch. 9–10);
  - whether Maskell's theory holds for a sphere;
  - θ for a sphere.
- **New open question 10:** where the airspeed reference is read during force runs.
- **C_D reference** at the test Re: Morrison2013 and Roos1971 not yet reviewed.

## 11. Remaining tasks

See TODO.md:

- **P0 (owner):** commit and push this session; sizing inputs; kit list; confirm D-003, D-004 and D-006.
- **P1:**
  - review Morrison2013 and Roos1971;
  - size the contraction and test section, with this session's inputs;
  - Barlow1999 ch. 6 and 9–10;
  - the remaining hardware choices.
- **P2 and P3:** unchanged in substance. The validation run now includes a two-sphere-size check; the mist is
  deferred; the dial idea is under P3.

## 12. Recommended first task for the next agent

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed this session's commit; the next `/wrap` backfills its
hash here and in the index.

- **If the owner has given the sizing inputs,** start build step 1 with the new inputs in TODO P1.
- **Otherwise,** review **Morrison2013 and Roos1971** and write a notes file for each.
  - Extract the C_D value(s) at Re of about 10⁴–10⁵, with the figure or table each comes from.
  - Morrison2013 is a correlation: check it against Roos1971's measurements.
  - Read the numbers from page images, not text layers.

## 13. Manual Git commands (as given to the owner)

State at this wrap: `UP_TO_DATE` at `7db221f`. Nothing is staged or committed.

Run in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add PROJECT_BACKGROUND.md PROJECT_STATUS.md TODO.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-10-31-reference-library-and-electronics.md docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md
git add resources/README.md resources/notes/Maskell1963.md resources/notes/Cooper1998.md
git status
git diff --cached --stat
git diff --cached
git commit -m "Review blockage-correction papers and record tunnel concepts" -m "Adds reading notes for Maskell (1963) and Cooper (AGARD-AG-336 ch. 6), read from page images, and proposes the sphere blockage correction (Maskell, theta 2.5, plus solid blockage, checked with two sphere sizes) and test-section position rules. Records the owner's questions on mist visualization and blower vs suction, the angle-of-attack dial idea, and backfills 7db221f."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** after the `git add` lines, `git status` should show 10 files staged: 7 modified and 3 new (two notes
  files and this log). Nothing should remain unstaged.
- **After `git diff --cached`**, press `q` to leave the pager.
- **Pushing:** `git push origin HEAD`. The last command should end with `STATE: UP_TO_DATE`.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"), GitHub has commits you do not. Do not
  force-push. Run `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then
  `git push origin HEAD`.
