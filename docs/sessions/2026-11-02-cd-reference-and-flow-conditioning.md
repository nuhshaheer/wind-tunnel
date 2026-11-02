# 2026-11-02: Sphere C_D reference and flow-conditioning review

- **Session ID:** aebc66ce-18f0-40b7-924b-7258bf51df1d (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** not committed yet

## 1. Starting state and objective

**Starting state** (from `/catchup`, 2026-11-02):

- Sync state `UP_TO_DATE` at `8fda08f`. No local changes, stashes or other branches.
- `check_docs.py`: 0 failures, 0 warnings. Tests: 20/20 passed.
- Discrepancies found:
  - `8fda08f` (the previous session's part 2, pushed) was still described as "not committed yet" in
    PROJECT_STATUS.md, SESSION_LOG.md and that session's log;
  - the sketch-PDF compression question was moot, because it was committed uncompressed;
  - two lines in PROJECT_BACKGROUND.md predated D-008;
  - the question of filing `PartsListECE2010.pdf` was still unanswered.

**Objectives (owner requests, in order):**

1. "Would it be a good idea … another loadcell for when i want to stick a model car into the machine … the downforce
   could be measured. my only concern would be the car being blown away by the wind. this is just an idea."
2. "Get started on the agent tasks": review Morrison2013 and Roos1971 for the Re-matched C_D reference, then Mehta1977
   (wide-angle diffuser) and Scheiman1981 (screens and honeycomb).
3. The owner offered: "anything you need me to review and look at and just tell you what it says … even if you are
   confident … let me review it." They then checked the values the agent listed.
4. The owner added Wieghardt (1953) and Brown and Lawler (2003). They asked: "isn't Brown and Lawler old? what makes it
   credible?"
5. "Is this a good decision to make?" (the validation reference). Then: "Ok, let's move forward with this."
6. `/wrap`.

## 2. Work completed

**Model-car downforce idea (discussion only; recorded as a P3 idea in TODO.md):**

- It needs the same second, vertical load cell as airfoil lift. Weakly2024 used two cells at right angles.
- Hold the car on a post with its wheels just clear of a fixed floor, not on a weighing platform: the platform would
  cancel much of the downforce.
- Lift-off is unlikely, but free wheels would roll. The post fixes that.
- Size about 25 × 20 mm frontal area in the 100 mm section. Forces are a few gf.
- The fixed floor and the low Re mean results only compare shapes.
- The Ahmed body is a reference shape (cited from memory, unverified).

**Reference reviews.** Each has a notes file and an index row marked "Reviewed 2026-11-02".

- **Morrison2013**: one C_D(Re) fit. Eq. (1) was read from page images.
  - The exam sheet prints a different last term and a typo: 236,000 for 263,000.
  - Eq. (1) gives about 0.393 at Re 1.3–2×10⁴. This was later found to be 7–11 % low; see Brown2003.
- **Roos1971**: towing-tank sphere drag.
  - Table 1 was checked against the page image.
  - The authors say their points for Re 5,500–100,000 read high because of vibration.
  - The band of earlier data in Fig. 3 was read with overlaid reference lines.
- **Mehta1977**: the wide-angle diffuser charts.
  - Fig. 5 was read with a pixel-calibrated overlay: at A = 3.44, the largest 2θ is about 17°, 28.5°, 46° and 53° for
    0, 1, 2 and 3 screens.
  - Fig. 7 gives A < 1.14 K_sum + 1.
  - Other content: screen positioning (moment rule), honeycomb L/D 7–10, settling-chamber screen spacing of at least
    500 wire diameters, and the blower swirl experiments.
- **Scheiman1981**: turbulence reduction by screens and honeycombs (Table 1, Figs. 5, 7 and 11).
  - Screens alone: u′ follows 1/(1 + K), v′ follows 1/√(1 + K).
  - A honeycomb followed by a screen is far better than screens alone.
  - Spacings: 80–100 mesh lengths between screens; 0.3 m from the honeycomb to the first screen.
- **Wieghardt1953** (added by the owner):
  - the screen-K formula, c = 6.5(u₁d/βν)^(−1/3) "between 60 and 600", with k = c(1 − β)/β²;
  - the critical u₁d/βν of 85 for eddy shedding.
- **Brown2003** (added by the owner):
  - 480 curated, wall-corrected points;
  - Roos's 44 high-Re points excluded for vibration;
  - Eq. (19) and Clift's correlation (Table 2), with fit statistics (Table 3);
  - a pixel measurement of Fig. 3 near this project's Re.
- The owner's PDF checks are recorded in each notes file as "Checked by the owner against the PDF, 2026-11-02".
- `resources/README.md`: index rows added or updated. The "Wanted" list gained a tabulated C_D reference and
  Wieghardt, both since answered; Clift's book is now optional.
- The owner's files `wieghardt1953.pdf` and `brown2003.pdf` were renamed under the naming rule.

**Decision:** D-009, the sphere-validation reference (§9). D-001's status points to it.

**Documentation updated at `/wrap`:**

- PROJECT_STATUS.md: header, objectives, configuration, flow conditioning, tooling, findings, open questions 6, 13
  and 14, next steps, backfill of `8fda08f`.
- TODO.md: P0 commit item, P1 reviews and reference task moved to Done, a new screens-and-honeycomb task, sizing
  inputs, P2 validation criteria, the P3 model-car idea.
- PROJECT_BACKGROUND.md: Reynolds-number section, length-budget rules, references, lessons learned, two stale lines.
- docs/experimental_setup.md: diffuser, settling chamber, flow conditioning, sphere row, change history.
- CLAUDE.md: validation sentence and Python note.
- README.md: status banner and Python note.
- SESSION_LOG.md and the 2026-11-01 log: `8fda08f` backfilled.

## 3. Files and equipment affected

Equipment: none. Nothing was built, bought or tested.

| File | Change |
|---|---|
| `resources/notes/Morrison2013.md`, `Roos1971.md`, `Mehta1977.md`, `Scheiman1981.md`, `Wieghardt1953.md`, `Brown2003.md` | New notes files |
| `resources/Wieghardt1953_resistance-of-screens.pdf`, `resources/Brown2003_sphere-drag-settling-velocity-revisited.pdf` | Added by the owner (as `wieghardt1953.pdf`, `brown2003.pdf`); renamed by the agent. 0.30 MB and 0.14 MB |
| `resources/README.md` | Index rows, "Wanted" list |
| `DECISIONS.md` | D-009 appended; D-001 status note |
| `PROJECT_STATUS.md`, `TODO.md`, `PROJECT_BACKGROUND.md`, `docs/experimental_setup.md`, `CLAUDE.md`, `README.md` | Updated (§2) |
| `docs/sessions/SESSION_LOG.md`, `docs/sessions/2026-11-01-parts-review-and-kit-inventory.md` | `8fda08f` backfilled; this session's row added |
| This log | New |

Outside the repository: the agent saved a Claude Code memory note for this project (`owner-verifies-pdf-readings`).
It says to give the owner a checklist of values read from PDFs, how to handle log axes and raised-dot decimals, and to
give printed and PDF page numbers. Scratch scripts and page renders stayed in the session scratchpad and were not
kept.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch            # UP_TO_DATE at 8fda08f (catchup and wrap)
python scripts/check_docs.py                     # several times; 0 failures each time
python -m unittest discover -s tests             # 20 tests OK
git status --short; git log --oneline -15; git diff --stat; git show --stat 8fda08f
git log --format=%h -1 -- docs/sessions/2026-11-01-parts-review-and-kit-inventory.md   # -> 8fda08f (backfill)
mv resources/wieghardt1953.pdf resources/Wieghardt1953_resistance-of-screens.pdf
mv resources/brown2003.pdf resources/Brown2003_sphere-drag-settling-velocity-revisited.pdf
python --version                                 # 3.11.0 in Git Bash and PowerShell; py -0p lists 3.14, 3.12, 3.11, 3.10
```

Scratch Python scripts (PyMuPDF 1.28.2, run with `python -I`, not kept):

- `render.py`: page or clip renders at a chosen zoom.
- `text.py`: text-layer dumps, using `sys.stdout.reconfigure(encoding="utf-8")`.
- `band.py`, `overlay.py`: Roos Fig. 3 grid and tick detection, with C_D and Re reference lines drawn over it.
- `m77fig5.py`, `m77fig5_overlay.py`: Mehta Fig. 5 tick detection and overlay.
  - Calibration: A = 3 at y = 803 px, 172 px per unit of A; 2θ = 0 at x = 24 px, 23.1 px per degree (zoom 4, clip
    55,315–470,610 pt).
- `cd_compare.py`, `cd_brown.py`: C_D from Morrison Eq. (1), Brown and Lawler Eqs. (17) and (19), Clift (Table 2),
  Turton and Levenspiel, and Haider and Levenspiel, at the planned Re. Binned statistics of Roos Table 1.
- `brown_fig3.py`, `brown_overlay.py`: Brown Fig. 3 tick detection.
  - Calibration: log Re = −3 + (x − 64)/158.6; log C_D = −(y − 858)/191.5 (zoom 4, clip 140,30–525,300 pt).
  - Dot statistics against Eq. (19), with a Stokes-region calibration check and an overlay of Eq. (19) and Clift.

All the formulas and constants are in the notes files, so every number can be recomputed. ρ = 1.20 kg/m³ and
μ = 1.81×10⁻⁵ Pa·s were assumed for the test Re (20 mm sphere at 10 m/s: Re = 1.33×10⁴).

One web search (standard mode) confirmed the Brown and Lawler citation and abstract before the owner obtained the PDF.

## 6. Measurements and results

No measurements. Every number below is a literature value or our arithmetic on one; none is a result of this project.

| Quantity | Value | Basis |
|---|---|---|
| Reference sphere C_D at Re 1.33–2.49×10⁴ | 0.422–0.445, Brown and Lawler Eq. (19); Clift 0.424–0.450 | Formula; constants owner-checked |
| Same, Morrison2013 Eq. (1) | 0.393–0.396, 7–11 % below Eq. (19) | Formula; constants owner-checked |
| Rise of Eq. (19) from Re 6.6×10³ to 2.49×10⁴ | 0.397 → 0.445, about 12 % | Formula |
| Brown Fig. 3 data ÷ Eq. (19), Re 10⁴–3×10⁴ | Median 1.07, 5th–95th percentile 1.00–1.20 | Pixel measurement. Calibration check: Stokes region median 1.011 against the paper's ±2.5 % |
| Roos Table 1 means against Morrison | +11 % to +28 % by Re bin | Table values; four owner-checked |
| Fan-to-chamber diffuser area ratio | 3.44 (181.5 cm² → 625 cm²) | Geometry |
| Minimum K_sum for that diffuser | 2.14 | Mehta1977 A < 1.14 K_sum + 1 |
| Shortest diffuser (2θ across the flats) | 0 screens 334 mm, 1 screen 193 mm, 2 screens 114 mm, 3 screens 98 mm | Fig. 5 readings 16.7°/28.5°/46.4°/53.1°; owner read 17/28.5/46/53.5 |
| Screen K at 2.08 m/s (28M: 0.19 mm wire, β = 0.62) | 1.56–1.84 (eqs. 12, 13, 11); Collar's high-Re value 0.89 | Wieghardt, extrapolated (u₁d/βν = 42, below 60) |
| Settling-chamber speed at 13 m/s in the test section | 2.08 m/s; fan outlet 7.2 m/s | Continuity |

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests`: 20 tests, OK (Python 3.11.0). It ran in 15.9 s at `/catchup` and 12.9 s
  mid-session, but **1,662.7 s** at this `/wrap` (see §8).
- `python scripts/check_docs.py`: 0 failures, 0 warnings after the edits (final run at this `/wrap`: 6 session logs,
  326 links and anchors, 58 committable files).
- Figure-reading checks:
  - Mehta Fig. 5 calibration lines lay on the figure's own ticks (visual).
  - Brown Fig. 3 dots in the Stokes region read 1.011 × 24/Re (median), against the paper's statement that they lie
    within ±2.5 %.
  - Roos Fig. 3: its y-axis ticks were located at 0.2, 0.4, 0.6 and 0.8, to resolve the owner's differing reading.
- Owner checks against the PDFs (recorded in the notes files):
  - Morrison constants and typo: confirmed.
  - Roos Table 1 spot values and quote: confirmed. Roos Fig. 3 band: the owner could not read it.
  - Mehta Fig. 5 readings agree within 0.5°; three rule quotes confirmed; the reversed inequality confirmed as printed.
  - Scheiman Figs. 7 and 11 readings agree within 0.01.
  - Wieghardt eqs. (5), (11) and (15) confirmed. The owner first read eq. (12)'s "5·5" as 5 × 5; it is a raised-dot
    decimal.
  - Brown Eq. (19), Table 3 row, Clift segment and the Roos exclusion: confirmed. Fig. 3: "around 0.5", hard to read.
- Not performed: no physical checks, and no check of the board, sensors or fan.

## 8. Errors, failed approaches and troubleshooting

- **A wrong reference value was given and later corrected.**
  - From Morrison2013, the agent first told the owner the expected C_D was "about 0.39", with a ±10 % band from Roos.
  - Brown2003 showed Morrison to be 7–11 % low at this Re. The notes carry a dated "superseded" banner.
- **The agent first proposed ±5 % and Clift as a cross-check.**
  - Measuring Brown's Fig. 3 showed the local data about 7 % above Eq. (19). Clift turned out to be fitted to almost
    the same data.
  - The agent revised the proposal to ±10 % plus a trend check before the owner decided.
- **The owner's approval was ambiguous.** They answered "let's move forward with this" but pasted the old ±5 % wording.
  The agent asked, and the owner chose the revised version.
- **Automatic edge detection of Roos's hatched band failed.** It was contaminated by labels, arrows and the edges of the
  data dots, giving ranges like 0.25–0.56. Visual reading with overlaid reference lines replaced it.
- **The first eyeballed Mehta Fig. 5 coordinates were wrong**, taken by eye from a downscaled render. Pixel tick
  detection gave the calibration.
- **Brown Fig. 3 showed a uniform +7 %**, which looked like a calibration error at first. It was checked against the
  Stokes region (median 1.011), which showed the axes were right.
- **Text-layer garbling:**
  - all of Morrison's equations;
  - Roos's "less than 2%" (text layer "2!%");
  - Mehta's M₂ formula and screen-K range;
  - Scheiman's reduction formulas;
  - all of Wieghardt's equations.

  All were read from page images.
- **Source typos:**
  - Morrison's exam sheet: 236,000 for 263,000;
  - Morrison's handout: "transition region near Re=2x10⁶", probably 2×10⁵;
  - Mehta1977: "60 > Ud/βν > 600", confirmed as 60–600 in Wieghardt;
  - Roos: "Wieselberger" for Wieselsberger.
- **Owner reading traps:**
  - log axes read as linear: about 0.6 at Re 10⁴ for Roos Fig. 3, and 0.5/0.6/0.7 for Brown Fig. 3;
  - "5·5" read as 5 × 5;
  - the agent gave PDF page numbers while the owner used printed ones.

  These are now in Lessons learned and the agent's memory note.
- **`UnicodeEncodeError` (cp1252)** when printing PDF text in Git Bash. `PYTHONIOENCODING` is ignored under `python -I`,
  so the scripts call `sys.stdout.reconfigure(encoding="utf-8")`.
- **Environment:** `python` is 3.11.0, not the 3.13 recorded earlier. Noted in CLAUDE.md and PROJECT_STATUS §4. It is
  not known whether another machine has 3.13.
- After the Wieghardt rename the shell's working directory briefly moved into `resources/`; later commands used
  absolute paths. No effect on files.
- **Slow test run, cause unknown.** At this `/wrap` the 20 tests took 1,662.7 s instead of the usual 13–16 s; all
  passed.
  - The command ran past the 120 s tool limit and finished in the background.
  - Not investigated. Possible causes include a Git operation in the throwaway test repos waiting on something
    (credential helper, antivirus or OneDrive). Python 3.11's unittest has no per-test timing, so the slow test is not
    known.
  - If it recurs, run `python -m unittest discover -s tests -v` and watch which test stalls.

## 9. Decisions and reasoning

- **[D-009](../../DECISIONS.md) (Accepted by the owner):** the sphere-validation reference is Brown and Lawler (2003)
  Eq. (19) at each run's Re, with a band of about ±10 %. Runs at several speeds must show the predicted rise of C_D with
  Re.
  - Why: the best curated data, an explicit formula, and C_D varying about 12 % across the test range.
  - Why ±10 %: the local data scatter.
  - Rejected: 0.47; Morrison; ±5 % with a Clift cross-check; Roos Table 1.
  - D-001's "about 0.47" is superseded by it; validating with a sphere stands.
- **Proposed, not decided** (TODO P1 and open questions):
  - two diffuser screens and a 150–200 mm diffuser;
  - the settling-chamber spacing (open question 13);
  - room for a second load cell (open question 14);
  - running the two-sphere check at matched Re.

## 10. Open questions and blockers

- Unchanged owner inputs, still the main blocker:
  - target top speed;
  - fan choice;
  - Blink test once the cable arrives;
  - bench supply rating, magnets, other electronics;
  - D-003, D-004, D-006 and D-007's open exit;
  - whether to file `PartsListECE2010.pdf`.
- New:
  - open question 13: screens and honeycomb, bought or printed, mesh, settling-chamber length;
  - open question 14: plan now for a second, vertical load cell?
  - whether to pursue the model-car idea after validation.
- D-009's band could be tightened with the original data tables near Re = 10⁴ (likely Lunnon 1928 and Vlajinac and
  Covert 1972, not checked).
- Python version: 3.11 observed. Was 3.13 on another machine, or removed?

## 11. Remaining tasks

See TODO.md:
- **P0 (owner):** commit and push this session; the top speed; the fan; the board setup; the parts list; confirm the
  tentative decisions.
- **P1:**
  - the sizing task, now with the diffuser and settling-chamber inputs;
  - choose the screens and honeycomb (new);
  - the fan check, using the low-speed screen K;
  - the remaining papers (Morel1975, Anthoine2004, Bradshaw1964, Barlow1999 chapters);
  - datasheets and parts choices.
- **P2:** validation run criteria updated (D-009).
- **P3:** the model-car idea added.

## 12. Recommended first task for the next agent

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed this session; the next `/wrap` backfills the hash here
and in the index.

- **If the owner has given the top speed or chosen a fan,** record them, check the fan against the length budget and
  the low-speed screen K (TODO P1 fan task), and choose the pressure-sensor range.
- **Otherwise, start build step 1** (TODO P1 "Size the contraction and test section"). All its inputs are now
  reviewed. Lay out the section dimensions:
  - diffuser: about 150–200 mm with two screens;
  - settling-chamber stack: decide open question 13 with the owner;
  - contraction 250 mm;
  - test section 270–290 mm.

  Then recompute the length budget and the fan's pressure requirement with the actual screen K values. Write the
  design note in docs/experimental_setup.md.
- Whenever values are read from a PDF, give the owner a checklist to confirm (Lessons learned, 2026-11-02).

## 13. Manual Git commands (as given to the owner)

State at this wrap: `UP_TO_DATE` at `8fda08f`. Nothing is staged or committed. Nineteen files changed: 10 modified,
9 new (6 notes files, 2 PDFs, this log).

Run in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add CLAUDE.md README.md DECISIONS.md PROJECT_STATUS.md PROJECT_BACKGROUND.md TODO.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-01-parts-review-and-kit-inventory.md docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md
git add resources/README.md resources/notes/Morrison2013.md resources/notes/Roos1971.md resources/notes/Mehta1977.md resources/notes/Scheiman1981.md resources/notes/Wieghardt1953.md resources/notes/Brown2003.md
git add resources/Wieghardt1953_resistance-of-screens.pdf resources/Brown2003_sphere-drag-settling-velocity-revisited.pdf
git status
git diff --cached --stat
git commit -m "Choose Re-matched sphere C_D reference and review flow conditioning" -m "Reviews Morrison2013, Roos1971, Brown2003, Mehta1977, Scheiman1981 and Wieghardt1953, with values checked by the owner against the PDFs. Records D-009: compare the sphere C_D with Brown and Lawler Eq. (19) at each run's Re, with a +-10 % band and a trend check, replacing 'about 0.47'. Adds diffuser, settling-chamber, screen and honeycomb design inputs, the model-car downforce idea (P3), and backfills 8fda08f."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** after the `git add` lines, `git status` should show 19 files under "Changes to be committed" and nothing
  left unstaged or untracked.
- **Inspecting:** `git diff --cached` shows the full staged diff; press `q` to leave the pager. The two PDFs show only
  as binary files.
- **Pushing:** `git push origin HEAD`. The last command should end with `STATE: UP_TO_DATE`.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
