# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: commit and push this session's changes** (reference library and electronics references: docs, two
  notes files and 12 PDFs). Outcome: GitHub holds them. Verify: `python scripts/sync_status.py --fetch` reports
  `UP_TO_DATE`. Commands: [session log](docs/sessions/2026-10-31-reference-library-and-electronics.md#13-manual-git-commands-as-given-to-the-owner).
- [ ] **Owner: provide the sizing inputs:** available floor or bench length for the tunnel, target top airspeed, and
  any fan or blower already in mind. Outcome: recorded under "Requirements and constraints" in PROJECT_BACKGROUND.md.
  Verify: the first P1 sizing task can start without guessing these.
- [ ] **Owner: list what else is in the ECE kit** (a photo works): passives, breadboard, multimeter, bench or split
  power supply, any microcontroller board. Outcome: each item recorded as "On hand" in PROJECT_STATUS.md §3 and
  docs/experimental_setup.md, citing the owner and date. Verify: open question 9 closed; the microcontroller and
  op-amp tasks below can use it.
- [ ] **Owner: confirm or change the tentative decisions** D-003 (private visibility), D-004 (data and LFS policy) and
  D-006 (reference PDFs over 25 MB kept local only) in [DECISIONS.md](DECISIONS.md).
  Verify: status changed to Accepted (or replaced by a new decision).

## P1: Design and choose hardware (build step 1)

- [ ] **Review the blockage and C_D-reference papers now in `resources/`:** Maskell1963 and Cooper1998 (AGARD-AG-336
  chapter 6), then Morrison2013 and Roos1971. Both scans (Maskell1963, Cooper1998) have no text layer; read the page
  images, or the full AGARD volume's text on this machine. Outcome: a notes file per paper. Verify: each index row in
  [resources/README.md](resources/README.md) says "Reviewed". Feeds the blockage, C_D-reference and sizing tasks below.
- [ ] **Size the contraction and test section.** Choose tunnel type (open-circuit blower vs suck-down), test-section
  cross-section and length, contraction ratio, contraction wall shape and length, whether to fit an exit diffuser,
  and target airspeed range. Needs the owner's sizing inputs (P0).
  - Inputs [Proposed]: contraction ratio 6–9, square section, 5th-order-polynomial wall, length about 1.0 × inlet
    height, sphere at least 0.5 D downstream of the contraction, segmented print (D-005). See the notes in
    [resources/README.md](resources/README.md).
  - Outcome: a design note in `docs/experimental_setup.md` with dimensions and the reasoning, and a DECISIONS.md entry.
  - Verify: Reynolds number, blockage ratio, expected drag and fan duty recomputed for the chosen numbers (see
    [estimates](PROJECT_BACKGROUND.md#order-of-magnitude-estimates)); sphere blockage stays at a few percent or below.
- [ ] **Owner: download the electronics datasheets** on the resources "Wanted" list, items 1–4: pressure-sensor
  candidates (Sensirion SDP31/SDP32, Honeywell TruStability HSC ±1 inH₂O), load-cell candidates (TAL220, TAL221),
  TI LM741 / LM348 / LM317, Bosch BME280. Outcome: PDFs in `resources/`; an agent files them and writes notes.
  Verify: each has an index row marked "Reviewed".
- [ ] **Review the remaining papers when their topic comes up:** Mehta1977 (fan and wide-angle diffuser), Scheiman1981
  (screens and honeycomb), Morel1975 (contraction), Anthoine2004 (blockage on cylinders), Bradshaw1964, and Barlow1999
  chapters 4, 6.4, 7 and 12.2 (instrumentation, data systems, balances, uncertainty). Outcome and verify as above.
- [ ] **Size and choose the fan or blower.** Outcome: model recorded, with its performance curve. Verify: at the
  chosen test-section size and top speed, the required flow rate and static pressure (Mehta1979 power-factor method,
  recomputed for the real screens and contraction ratio) sit near the maker's maximum-efficiency point, with power
  margin.
- [ ] **Choose the blockage-correction method** for the sphere (Maskell1963 or the Cooper1998 methods). Outcome:
  method and formula recorded in PROJECT_BACKGROUND.md. Verify: the correction for the chosen sphere and test section
  is computed and stated with its uncertainty.
- [ ] **Choose sphere diameter(s) and material.** Outcome: diameter, tolerance, surface finish and mounting method recorded.
  Verify: test Re sits inside the subcritical plateau (well below ~2×10⁵); diameter measured with calipers once bought.
- [ ] **Choose the microcontroller / DAQ.** Baseline: Arduino Uno with one HX711 per load cell
  ([Weakly2024 notes](resources/notes/Weakly2024.md)). Outcome: board chosen and recorded (D-entry). Verify: it can
  read the HX711 and the chosen pressure sensor at the planned sample rate (interface and logic voltage checked), and
  log raw counts to a PC as CSV.
- [ ] **Choose the differential pressure sensor range.** Outcome: model and range recorded. Verify: full-scale range covers
  the maximum q (about 240 Pa at 20 m/s, estimate) without leaving most of the span unused; offset and noise specs written down.
- [ ] **Choose the load-cell capacity.** Outcome: capacity recorded. Verify: expected drag plus mount drag (grams-force
  range, estimate) is a usable fraction of full scale; HX711 noise in grams computed from the chosen cell's rated
  output ([HX711 notes](resources/notes/HX711.md)); overload margin for handling noted.
- [ ] **Choose the ambient pressure and temperature sensor** for air density (candidate: Bosch BME280). Outcome:
  sensor recorded in docs/experimental_setup.md. Verify: its stated accuracy gives a density uncertainty that is
  small next to the q and force uncertainties.
- [ ] **Decide the role of the op-amp circuit** (LM741/LM348, LM317). Outcome: a short circuit description. Verify:
  supply rails compatible with the op-amp (LM741 is not rail-to-rail and expects split supplies). Depends on the
  pressure-sensor choice (a digital sensor needs no analog conditioning) and on the kit inventory (P0).
- [ ] **Pick a Re-matched reference for sphere Cd.** Outcome: citation with figure/table and the Cd value at the test Re,
  added to PROJECT_BACKGROUND.md as reviewed. Verify: the source covers the planned Re range. Note: Achenbach (1972)
  covers only Re ≥ 5×10⁴, but the planned Re is roughly 10⁴–10⁵. Candidates now in `resources/`: Morrison2013
  (correlation) backed by Roos1971 (measurements).
- [ ] **Owner: buy hardware** once the above are chosen. Outcome: parts on hand. Verify: part numbers and datasheets
  recorded in `docs/experimental_setup.md`.

## P2: Build and validate (build steps 2–6)

- [ ] **Build flow conditioning** (honeycomb + screens). Verify: dimensions recorded; photos in docs.
- [ ] **Map flow uniformity** across the test section with the pitot tube. Outcome: velocity map dataset (EXP entry in the
  data catalog). Verify: raw data in `data/raw/`, uniformity (e.g. % deviation from mean) computed by a script.
- [ ] **Optional: flow visualization with a water-mist generator** (owner's idea, 2026-10-30; see the Aki videos in
  [resources/README.md](resources/README.md#videos-and-web-pages)). Qualitative only; it is not part of the measurement
  chain. Uses: spotting swirl or separation in the contraction during the uniformity map, seeing the sphere's wake, and
  photos of the work. Design points [Proposed]:
  - In a blower tunnel (fan at the inlet) the inside is at or above atmospheric pressure, so the tunnel will not suck
    mist in as Aki's suction tunnel does. Mist released at the fan inlet also passes through the fan, honeycomb and
    screens and becomes general fog rather than visible lines. Push the mist with a small fan on the generator's air
    intake, and release it through a thin tube (or a row of tubes) downstream of the last screen or just upstream of
    the model. This also bears on the blower-vs-suction choice in build step 1.
  - Mist fades at high speed, so run visualization at low speed.
  - Never run mist during force or pressure measurements. Water in the pitot lines or on the load cell corrupts
    readings, and humidity changes air density. Let the tunnel dry afterwards.
  - Use distilled water, and empty and dry the generator after each use. Ultrasonic foggers put whatever is in the
    water (minerals, microbes from standing water) into the air. Keep the mains supply dry.

  Outcome: a printed generator plus injection tube. Verify: visible streaklines in the test section at a stated speed
  (photo or video referenced in the data catalog).
- [ ] **Build the load cell and its conditioning circuit.** Solder the load-cell leads directly to the HX711, with no
  breadboard in the bridge wiring (lesson from Weakly2024). Verify: stable zero over several minutes with wind off;
  noise recorded.
- [ ] **Calibrate the load cell against known weights.** Outcome: calibration dataset and fit (counts → N). Verify:
  residuals and linearity reported; calibration file referenced from the data catalog.
- [ ] **Sphere Cd validation run.** Outcome: C_D with uncertainty at one or more Re, compared with the reference.
  Verify: mount drag subtracted, blockage corrected, repeated runs agree within the stated uncertainty, analysis
  reproducible from raw data.

## P3: After validation (build step 7)

- [ ] **Airfoil pitch attachment** (servo). Defined after the validation result.

## Done

- [x] 2026-10-25: Project plan (original README).
- [x] 2026-10-29: Repository, documentation and `/catchup` / `/wrap` workflow implemented; `/catchup` verified with
  a fresh agent ([session log](docs/sessions/2026-10-29-github-setup-and-agent-handoff.md)).
- [x] 2026-10-29: Owner committed and pushed the initial setup as `cc51fff`. `/catchup` confirmed `UP_TO_DATE` on
  2026-10-30 ([session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)).
- [x] 2026-10-30: Created `resources/` (index, naming rules, notes template) and reviewed Abdelhamed2014, Bell1988 and
  Mehta1979. Recorded D-005 (segmented printing on the P1S), estimates of printable sizes and fan requirements, and a
  checked list of further documents ([session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)).
- [x] 2026-10-31: Owner committed and pushed the literature review as `5bc60f0`, after fixing a network fault (the
  PC had no IPv4 address). The push used the commands `/wrap` gave, which completes the independent `/wrap`
  verification ([session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md)).
- [x] 2026-10-31: Owner committed and pushed the second `/wrap`'s doc update as `b710093`; `/catchup` confirmed
  `UP_TO_DATE` ([session log](docs/sessions/2026-10-31-reference-library-and-electronics.md)).
- [x] 2026-10-31: Owner downloaded every document on the 2026-10-30 "Wanted" list (and the full AGARD-AG-336 volume);
  the agent filed them, reviewed the HX711 datasheet and Weakly2024, and wrote a new electronics "Wanted" list
  ([session log](docs/sessions/2026-10-31-reference-library-and-electronics.md)).
