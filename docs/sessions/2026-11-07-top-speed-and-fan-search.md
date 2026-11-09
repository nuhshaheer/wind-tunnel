# 2026-11-07: Top speed and fan search

- **Session ID:** 8a067f65-0dff-4cff-a63a-4591e2854a53 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** `d7f5cdf`

The session began on 2026-11-05 with `/catchup`. The `/wrap` ran on 2026-11-07, which gives the file its date.
Documentation only: nothing was bought, built or tested.

## 1. Starting state and objective

**Starting state** (from `/catchup`, 2026-11-05):

- Sync state `UP_TO_DATE` at `36f39eb`. The previous session's commit had been pushed. No local changes, stashes or
  other branches; the only ignored files were the two D-006 local-only PDFs and `__pycache__`.
- `check_docs.py`: 0 failures, 0 warnings. Tests: 20/20 passed in 11.3 s.
- Discrepancies found, all because the owner committed and pushed after the previous `/wrap`:
  - the PROJECT_STATUS.md header still gave `b22a45b` as the last commit and said the board test was not committed;
  - PROJECT_STATUS §12 still listed "commit and push", and §4 and §13 lacked `b22a45b` and/or `36f39eb`;
  - SESSION_LOG.md and the 2026-11-03 log's header still said "not committed yet";
  - TODO.md had no Done entry for that push.

**Objectives (owner, in order):**

1. `/catchup`.
2. "What do you think our top speed should be?"
3. "am i looking for 500 Pa?"
4. Pasted the spec table of a VEVOR 6-inch inline fan and asked "does this wokr?"
5. "im trying to find somethign more affordbale"
6. `/wrap` (2026-11-07).

## 2. Work completed

- **Catch-up** (2026-11-05): handoff summary; proposed build step 1 (sizing) as the first task. No files changed.
- **Top-speed recommendation: 13 m/s, with validation runs from about 6.5 m/s.** Estimates, not confirmed by the
  owner. The table and reasons are now in
  [PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#top-speed-trade-off-proposed). In short:
  - the trend check gains little above 13 m/s: Eq. (19) rises 8.7 % to 13 m/s, 9.8 % to 15 m/s;
  - one 6-inch fan listing about 500 Pa should just reach it, whereas 15 m/s needs a bigger fan and 1.5× the power;
  - q = 101 Pa fits a ±125 Pa sensor (full scale at 14.4 m/s);
  - the cost is force: 15 m/s would give about 35 % more;
  - if the real fan reaches only 11–12 m/s, the validation still works.
- **Fan pressure explained.**
  - A fan's listed maximum static pressure is at zero flow, and free-air CFM is at zero pressure; the tunnel runs in
    between, at about 275 CFM against 127–152 Pa for 13 m/s.
  - Gave the minimum listed pressure for each free-air flow (about 410–490 Pa at 400 CFM), the inH₂O and mmH₂O
    conversions, and the fan-curve test: at least 275 CFM at 150 Pa (0.6 inH₂O).
  - Pointed out that the 500 Pa fan figure is unrelated to the ±500 Pa sensor; the proposed sensor is ±125 Pa.
- **Docs error found and corrected.**
  - TODO P0 said that 400 CFM and 300 Pa "covers 15 m/s with margin", and PROJECT_STATUS §3, PROJECT_BACKGROUND and
    TODO P1 gave the requirement as "300–500 Pa".
  - By the docs' own straight-line estimate, 400 CFM and 300 Pa give only about 11.5–12 m/s.
- **VEVOR 6-inch fan assessed:** unsuitable as listed (§6).
- **Search for a cheaper fan:** none with a published pressure figure meets 13 m/s for less than the Cloudline S6's
  $99 (§6, §8).
  - Agent's advice: first ask VIVOSUN for the AeroZesh S6's maximum static pressure or fan curve (the agent offered
    to draft the message). Buy it if the figure is about 450 Pa or more; otherwise buy the Cloudline S6.
  - A used or open-box S6 is fine if its bearings run quiet.
- **Documentation updated** at `/wrap` (§3), including the stale lines from `/catchup`.

## 3. Files and equipment affected

Files (six modified, one new):

- `PROJECT_STATUS.md`:
  - header: last commit `36f39eb`, this session uncommitted;
  - stage: proposed top speed;
  - §3 fan row: corrected requirement, candidates with 2026-11-05 prices, the unsuitable fans; §3 pressure-sensor row;
  - §4: `/catchup` and `/wrap` evidence;
  - §6: the `36f39eb` push and this session;
  - §8: estimates pointer; §9: blockers, test-time watch;
  - §10 questions 3 and 4; §12 next steps; §13 commit list.
- `TODO.md`: P0 top-speed and fan tasks (the proposal, advice, corrected Verify line); P1 fan and pressure-sensor
  tasks; Done entry for `36f39eb`.
- `PROJECT_BACKGROUND.md`: budget and unknowns lines; the corrected fan-requirement sentence; new subsection
  "Top-speed trade-off [Proposed]".
- `docs/experimental_setup.md`: configuration date; fan, airspeed-range and airspeed-sensor rows; change-history row.
- `docs/sessions/SESSION_LOG.md`: the 2026-11-03 row's commit filled in (`36f39eb`); this session's row.
- `docs/sessions/2026-11-03-mega-2560-board-test.md`: header's commit field backfilled with `36f39eb` (the only
  permitted edit to an old log).
- `docs/sessions/2026-11-07-top-speed-and-fan-search.md`: this log (new).

Equipment: none.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch            # UP_TO_DATE at 36f39eb (catchup 2026-11-05 and wrap 2026-11-07)
git status --short; git log --oneline -15; git remote -v; git stash list; git branch -a
git status --short --ignored                     # only the D-006 PDFs and __pycache__
git show --stat 36f39eb                          # 7 files, matching the 2026-11-03 log's §13 list
git log --format=%h -1 -- docs/sessions/2026-11-03-mega-2560-board-test.md   # 36f39eb, for the backfill
python scripts/check_docs.py
python -m unittest discover -s tests             # catchup; -v at wrap
```

Web searches (2026-11-05, Claude Code's WebSearch; results came back as summaries, and no page was opened):

1. "VEVOR 6 inch inline duct fan 400 CFM static pressure" (standard)
2. "VIVOSUN AeroZesh S6 static pressure inH2O Pa specifications" (extended)
3. "affordable 6 inch EC inline duct fan under $70 static pressure rating Pa inH2O 400 CFM" (extended)
4. "AC Infinity Cloudline S6 price static pressure 2025" (standard)

Estimate script. It was first run in pieces on 2026-11-05, then rerun on 2026-11-07 as this one file from the session
scratchpad; the output matched every figure given to the owner. Run with `python topspeed.py`:

```python
# Top-speed and fan-pressure estimates, 100 mm square section. rho=1.20 kg/m^3, mu=1.81e-5 Pa s;
# C_D from Brown & Lawler Eq. (19) (D-009); open-exit fan pressure 1.25-1.5 q; straight-line fan curve.
rho, mu, A, g, CFM = 1.20, 1.81e-5, 0.01, 9.80665, 2118.88   # CFM per m^3/s
cd = lambda Re: (24/Re)*(1 + 0.150*Re**0.681) + 0.407/(1 + 8710/Re)
def drag_gf(V, d):
    Re = rho*V*d/mu
    return 0.5*rho*V**2*cd(Re)*3.14159265*d**2/4/g*1000
for V in (5, 6.5, 10, 11, 12, 13, 15, 20):
    q = 0.5*rho*V**2
    print(f"V={V:4} q={q:4.0f} Pa  drag 20/25 mm {drag_gf(V,.020):.2f}/{drag_gf(V,.025):.2f} gf  "
          f"needs {A*V*CFM:.0f} CFM at {1.25*q:.0f}-{1.5*q:.0f} Pa  power x{(V/13)**3:.2f} of 13 m/s")
for span in (125, 249, 500):
    print(f"sensor span {span} Pa -> q full scale at {(2*span/rho)**0.5:.1f} m/s")
def top(Qf, Pm, k):   # top speed for a straight-line fan curve (Qf CFM free air, Pm Pa at zero flow)
    lo, hi = 1, 40
    for _ in range(60):
        m = (lo+hi)/2
        lo, hi = (m, hi) if Qf*(1 - k*0.5*rho*m*m/Pm) > A*m*CFM else (lo, m)
    return lo
for Qf, Pm in ((402, 503), (400, 500), (400, 400), (400, 300)):
    print(f"fan {Qf} CFM / {Pm} Pa -> top {top(Qf,Pm,1.5):.1f}-{top(Qf,Pm,1.25):.1f} m/s")
q13 = 0.5*rho*13**2; Q13 = A*13*CFM
for Qf in (350, 400, 450, 500):
    print(f"13 m/s with {Qf} CFM free air needs max static {1.25*q13/(1-Q13/Qf):.0f}-{1.5*q13/(1-Q13/Qf):.0f} Pa")
for vlo, vhi in ((6.5, 11), (6.5, 13), (6.5, 15), (5, 15)):
    r1, r2 = rho*vlo*.020/mu, rho*vhi*.025/mu
    print(f"trend 20 mm@{vlo} -> 25 mm@{vhi}: Re {r1:.0f}-{r2:.0f}, C_D {cd(r1):.3f}-{cd(r2):.3f}, rise {100*(cd(r2)/cd(r1)-1):.1f} %")
```

## 6. Measurements and results

**None measured.** Everything below is either an estimate from assumed values or a figure read from a retail listing.

**Estimates** (the script in §5; full tables in
[PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#top-speed-trade-off-proposed)):

- At 13 m/s: q = 101 Pa; sphere drag 1.40 gf (20 mm) and 2.23 gf (25 mm); the fan must deliver about 275 CFM
  against 127–152 Pa.
- The 402 CFM / 503 Pa Cloudline S6 gives 13.1–13.7 m/s on a straight-line curve. A 400 CFM fan listed at 300 Pa
  gives 11.5–12.0 m/s.
- Uncertainty is not quantified. The straight-line fan curve is optimistic, because real curves sag, and the duct
  loss factors are Mehta1979's typical values, not this tunnel's.

**Fan listings** (2026-11-05, from web-search summaries; no page was opened, and prices change):

| Fan | Listed | Source |
|---|---|---|
| AC Infinity Cloudline S6 | 402 CFM (425 in some listings), 503 Pa, EC; $99 on AC Infinity's site, $119–175 elsewhere. One garden-supply listing shows 300 Pa and 351 CFM, possibly another configuration | AC Infinity comparison page; Hydrobuilder and other retailers |
| VIVOSUN AeroZesh S6 | 405 CFM, 3100 rpm, 45 dBA, 35 W, PWM-controlled EC, mixed flow, "high static pressure" with no number | VIVOSUN product page; AVAGROW listing |
| VEVOR 6-inch 400 CFM, AC (owner's paste) | 120 V, 60 W, 34 dB, 2600 rpm, 400 CFM; no pressure; $84.49 on eBay | Owner's paste; VEVOR page; eBay |
| Fan probably the same as the VEVOR | 400 CFM, 2600 rpm, 300 Pa. The search summary says the rpm and the 12 × 10 × 8.4 in dimensions match a VEVOR listing; the match is not confirmed | Lowe's listing |
| Skyshalo 6-inch | 400 CFM, AC, $53.89; no pressure. Same listing wording as the VEVOR (probably the same fan; our inference) | Home Depot |
| HFS 6-inch | 400 CFM, 120 W, 65 dB, $62.49; no pressure | HFS shop |

Source URLs:
- [AC Infinity comparison page](https://acinfinity.com/compare/254/369)
- [Hydrobuilder Cloudline PRO S6](https://hydrobuilder.com/products/ac-infinity-6-cloudline-pro-s6-quiet-inline-fan-with-speed-controller-402-cfm)
- [VIVOSUN AeroZesh S6](https://vivosun.com/vivosun-aerozesh-6-inch-inline-fan-hvac-blower-for-ventilation-p90271565918111669-v90271565918111650)
- [AVAGROW](https://avagrow.co.uk/shop/hydroponic-environmental-control-systems/fans/vivosun/vivosun-6-s6-aerozesh-inline-ec-fan/)
- [VEVOR](https://vevor.com/inline-duct-fan-c_11974/vevor-6-inch-inline-duct-fan-hvac-exhaust-blower-kit-ac-variable-speed-control-p_010143880081)
- [eBay](https://www.ebay.com/itm/326808506778)
- [Lowe's](https://www.lowes.com/pd/-/5014737253)
- [Home Depot](https://www.homedepot.com/p/SKYSHALO-6-in-Inline-Duct-Fan-400-CFM-Quiet-AC-Motor-Ventilation-Exhaust-Fan-for-Cooling-Booster-Grow-Tents-Hydroponics-XLGDFJYCHSAC6J5DVV1-1204/333857652)
- [HFS](https://shophfs.com/products/inline-6-exhaust-ventilation-fan-includes-mounting-brackets-400cfm)

**Interpretation** (agent's, not a result):

- The VEVOR fan would probably run the tunnel, but at about 11–12 m/s at best, with AC speed control that is
  usually less smooth at low speed than an EC motor's. That behaviour is not checked for this controller.
- Its "34 dB" is unlikely for a fan moving 400 CFM.

## 7. Tests, calibration checks and validation

- `python scripts/check_docs.py`: 0 failures and 0 warnings at `/catchup` (2026-11-05). At `/wrap`: see the last
  line of this section.
- `python -m unittest discover -s tests`: 20 tests OK in 11.3 s at `/catchup`. With `-v` at `/wrap`: 20 tests OK in
  7.9 s.
- The estimate script (§5) was rerun at `/wrap`; its output matched every figure given to the owner on 2026-11-05.
  That includes the 11 m/s figures (0.99 gf and a 7.2 % rise), first given from hand arithmetic as "about 1.0 gf" and
  "about 7 %".
- Not performed: any physical check (none was possible; no fan or sensor is on hand).
- `python scripts/check_docs.py` after the wrap edits: 0 failures, 0 warnings.

## 8. Errors, failed approaches and troubleshooting

- **Docs error (found 2026-11-05):** the fan requirement "300–500 Pa", and TODO's "300 Pa … covers 15 m/s with
  margin", contradicted the straight-line estimate in the same docs. That estimate gives 11.5–12 m/s for 400 CFM at
  300 Pa. Corrected in PROJECT_STATUS §3, TODO P0 and P1, PROJECT_BACKGROUND and docs/experimental_setup.md, each with
  a dated note. Both phrases were introduced in `8fda08f` (2026-11-01, part 2 of that session), found with
  `git log -S "300–500 Pa"` and `git log -S "covers 15 m/s"`.
- **Dead end:** the search for a 6-inch fan under about $70 with a published static pressure that meets 13 m/s found
  none (searches 2 and 3 in §5).
- **VIVOSUN still publishes no static pressure for the AeroZesh S6**, on its own pages or on retailers' (search 2).
- **Limits of the search:** every spec and price came from search-result summaries, not from opening the pages. The
  VEVOR's 300 Pa comes from a Lowe's listing matched to it by rpm and dimensions, not confirmed. Treat these as
  leads, and check the page or the manual before buying.

## 9. Decisions and reasoning

None by the owner. The 13 m/s top speed is the agent's recommendation. The owner asked follow-up questions about the
fan but did not confirm the speed, so no DECISIONS.md entry was made; record it as D-010 once confirmed. The fan
requirement change is a correction of an error, not a decision.

## 10. Open questions and blockers

The main blocker is unchanged: buying hardware waits on the top speed and the fan. Open:

- confirm or change the proposed 13 m/s top speed (open question 3);
- the fan choice: the AeroZesh S6's static pressure (ask VIVOSUN), or the Cloudline S6 at $99;
- the settling-chamber spacing (open question 13), asked 2026-11-02, still not answered;
- the bench-supply rating, the magnets, other electronics, whether the board is printed "R3", and whether to file
  `PartsListECE2010.pdf`;
- D-003, D-004, D-006 and D-007's open exit, still Tentative.

## 11. Remaining tasks

See TODO.md:

- **P0 (owner):** commit and push this session; confirm the top speed; choose the fan; finish the parts list; confirm
  the tentative decisions.
- **P1:** build step 1 sizing, screens and honeycomb, the fan check, remaining papers, datasheets and parts.

## 12. Recommended first task for the next agent

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed this session, and backfill this log's commit hash.

- **If the owner has confirmed the top speed,** record it as D-010 and under "Requirements and constraints" in
  PROJECT_BACKGROUND.md.
- **If the owner wants to ask VIVOSUN,** draft the message: ask for the AeroZesh S6's maximum static pressure (Pa or
  inH₂O) and its fan curve (airflow against static pressure).
- **If the owner has chosen a fan,** record it in PROJECT_STATUS §3 and docs/experimental_setup.md, with its listed
  specs or datasheet.
- **Then start build step 1** (TODO P1 "Size the contraction and test section") with 13 m/s as the design speed,
  unless the owner chose another.

## 13. Manual Git commands (as given to the owner)

State at this wrap: `UP_TO_DATE` at `36f39eb`. Nothing staged or committed. Seven files: six modified, one new (this
log).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add PROJECT_STATUS.md PROJECT_BACKGROUND.md TODO.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-03-mega-2560-board-test.md docs/sessions/2026-11-07-top-speed-and-fan-search.md
git status
git diff --cached --stat
git commit -m "Propose 13 m/s top speed and correct the fan pressure need" -m "Records the agent's 13 m/s top-speed recommendation (not yet confirmed by the owner) with its trade-off table, corrects the fan requirement (400 CFM at 300 Pa gives only about 11.5-12 m/s, so about 500 Pa is needed), and records the fan search: the owner's VEVOR AC fan is unsuitable as listed and nothing cheaper than the Cloudline S6 has a published pressure that meets 13 m/s. Backfills 36f39eb."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 7 files under "Changes to be committed" and nothing else.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** `gh auth status` or `gh auth login`, or sign in through Git Credential Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- The last command should end with `STATE: UP_TO_DATE`.
