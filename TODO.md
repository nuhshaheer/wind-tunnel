# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: review and push the initial commit.**
  Outcome: the repo on GitHub contains the setup. Verify: `git status` shows a clean tree and `git log origin/main -1`
  matches local `main`. Commands: [2026-10-29 session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md#manual-git-commands).
- [ ] **Owner: confirm or change the tentative decisions** D-003 (private visibility) and D-004 (data and LFS policy) in [DECISIONS.md](DECISIONS.md).
  Verify: status changed to Accepted (or replaced by a new decision).

- [ ] **Verify `/wrap` independently.** At the end of the next real work session, run `/wrap` and check the result.
  Outcome: a correct session log, updated status and correct Git commands from an agent that did not write the skill.
  Verify: `python scripts/check_docs.py` passes, and the owner's push succeeds with the commands given.

## P1: Design and choose hardware (build step 1)

- [ ] **Size the contraction and test section.** Choose tunnel type (open-circuit blower vs suck-down), test-section
  cross-section and length, contraction ratio, and target airspeed range.
  Outcome: a design note in `docs/experimental_setup.md` with dimensions and the reasoning, and a DECISIONS.md entry.
  Verify: Reynolds number, blockage ratio and expected drag recomputed for the chosen numbers (see
  [estimates](PROJECT_BACKGROUND.md#order-of-magnitude-estimates)); blockage of the sphere stays at a few percent or below.
- [ ] **Choose sphere diameter(s) and material.** Outcome: diameter, tolerance, surface finish and mounting method recorded.
  Verify: test Re sits inside the subcritical plateau (well below ~2×10⁵); diameter measured with calipers once bought.
- [ ] **Choose the microcontroller / DAQ.** Outcome: board chosen and recorded (D-entry). Verify: it can read the HX711
  and the chosen pressure sensor at the planned sample rate, and log to a PC as CSV.
- [ ] **Choose the differential pressure sensor range.** Outcome: model and range recorded. Verify: full-scale range covers
  the maximum q (about 240 Pa at 20 m/s, estimate) without leaving most of the span unused; offset and noise specs written down.
- [ ] **Choose the load-cell capacity.** Outcome: capacity recorded. Verify: expected drag plus mount drag (grams-force
  range, estimate) is a usable fraction of full scale; overload margin for handling noted.
- [ ] **Decide the role of the op-amp circuit** (LM741/LM348, LM317). Outcome: a short circuit description. Verify:
  supply rails compatible with the op-amp (LM741 is not rail-to-rail and expects split supplies).
- [ ] **Pick a Re-matched reference for sphere Cd.** Outcome: citation with figure/table and the Cd value at the test Re,
  added to PROJECT_BACKGROUND.md as reviewed. Verify: the source covers the planned Re range.
- [ ] **Owner: buy hardware** once the above are chosen. Outcome: parts on hand. Verify: part numbers and datasheets
  recorded in `docs/experimental_setup.md`.

## P2: Build and validate (build steps 2–6)

- [ ] **Build flow conditioning** (honeycomb + screens). Verify: dimensions recorded; photos in docs.
- [ ] **Map flow uniformity** across the test section with the pitot tube. Outcome: velocity map dataset (EXP entry in the
  data catalog). Verify: raw data in `data/raw/`, uniformity (e.g. % deviation from mean) computed by a script.
- [ ] **Build the load cell and its conditioning circuit.** Verify: stable zero over several minutes with wind off; noise recorded.
- [ ] **Calibrate the load cell against known weights.** Outcome: calibration dataset and fit (counts → N). Verify:
  residuals and linearity reported; calibration file referenced from the data catalog.
- [ ] **Sphere Cd validation run.** Outcome: C_D with uncertainty at one or more Re, compared with the reference.
  Verify: mount drag subtracted, repeated runs agree within the stated uncertainty, analysis reproducible from raw data.

## P3: After validation (build step 7)

- [ ] **Airfoil pitch attachment** (servo). Defined after the validation result.

## Done

- [x] 2026-10-25: Project plan (original README).
- [x] 2026-10-29: Repository, documentation and `/catchup` / `/wrap` workflow implemented; `/catchup` verified with
  a fresh agent ([session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md)).
