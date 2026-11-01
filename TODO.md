# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: commit and push this session's changes** (parts review and kit inventory: one new session log and doc
  updates). Outcome: GitHub holds them. Verify: `python scripts/sync_status.py --fetch` reports `UP_TO_DATE`.
  Commands: [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#13-manual-git-commands-as-given-to-the-owner).
- [ ] **Owner: provide the sizing inputs:** available floor or bench length for the tunnel, target top airspeed, and
  any fan or blower already in mind. These now also decide the fan size (6-inch or 8-inch inline fan) and the
  pressure-sensor range. Outcome: recorded under "Requirements and constraints" in PROJECT_BACKGROUND.md.
  Verify: the first P1 sizing task can start without guessing these.
- [ ] **Owner: set up the Elegoo Mega 2560 R3** once the USB A-to-B cable arrives (UGREEN 5 ft, ordered 2026-11-01).
  - Confirm the board: it should read MEGA2560 R3, and the large chip ATMEGA2560.
  - Install the Arduino IDE, select **Tools → Board → Arduino Mega or Mega 2560** and the port, and upload
    **File → Examples → Basics → Blink**.
  - Outcome: the board recorded as working in PROJECT_STATUS §3 and docs/experimental_setup.md.
  - Verify: a new COM port appears in Device Manager under "Ports (COM & LPT)" when it is plugged in, and the
    onboard LED blinks. The power LED alone proves nothing, because it also lights on a charge-only cable. If
    Windows shows "Unknown device", a driver is needed; report the name it shows.
- [ ] **Owner: finish the parts-on-hand list.** The ECE kit is recorded from its packing list (2026-11-01). Still
  needed:
  - whether a multimeter, soldering iron and bench or split power supply are on hand;
  - any other electronics the owner has (a photo works);
  - the magnets' type and size.

  Outcome: each item recorded as "On hand" in PROJECT_STATUS.md §3 and docs/experimental_setup.md, citing the owner
  and date. Verify: open question 9 closed.
- [ ] **Owner: confirm or change the tentative decisions** D-003 (private visibility), D-004 (data and LFS policy) and
  D-006 (reference PDFs over 25 MB kept local only) in [DECISIONS.md](DECISIONS.md).
  Verify: status changed to Accepted (or replaced by a new decision).

## P1: Design and choose hardware (build step 1)

- [ ] **Review the C_D-reference papers: Morrison2013 and Roos1971** (Maskell1963 and Cooper1998 were done
  2026-10-31). Outcome: a notes file per paper, with the C_D value(s) at Re of about 10⁴–10⁵ and the figure or table
  they come from. Verify: each index row in [resources/README.md](resources/README.md) says "Reviewed". Read numbers
  from page images, not text layers (Lessons learned in PROJECT_BACKGROUND.md). Feeds the C_D-reference task below.
- [ ] **Owner (recommended, optional): read the two key references.** The owner has not read the references yet
  (2026-11-01).
  - Read in full: [Mehta1979](resources/Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf) (rules for every
    part of a small blower tunnel) and
    [Weakly2024](resources/Weakly2024_low-cost-lift-drag-balance-educational-tunnel.pdf) (a student balance with an
    Arduino, HX711 and a sphere, and what went wrong).
  - Notes only: Bell1988, Maskell1963, Cooper1998 and HX711 in [resources/notes/](resources/notes/). The agent reads
    the rest when their topic comes up.
  - Outcome: the owner can answer five questions:
    1. What does each part of the tunnel do?
    2. What sets the test-section and fan size?
    3. How is a force of a few grams measured accurately?
    4. Why is 0.47 only right over a range of Reynolds numbers?
    5. Why do the walls change the measured drag?
  - Verify: the owner can discuss those questions when making the sizing decisions.
- [ ] **Size the contraction and test section.** Choose tunnel type (open-circuit blower vs suck-down), test-section
  cross-section and length, contraction ratio, contraction wall shape and length, whether to fit an exit diffuser,
  and target airspeed range. Needs the owner's sizing inputs (P0).
  - Inputs [Proposed]: contraction ratio 6–9, square section, 5th-order-polynomial wall, length about 1.0 × inlet
    height, sphere at least 0.5 D downstream of the contraction, segmented print (D-005). See the notes in
    [resources/README.md](resources/README.md).
  - Added 2026-10-31 [Proposed]:
    - a **closed** test section with a clear window;
    - the test-section length set by the position rules: reference pressure at least 1.5√C upstream of the sphere,
      sphere at least 4√S from the end ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed));
    - choose where the airspeed reference is read (PROJECT_STATUS open question 10);
    - a capped mist port after the last screen, so optional visualization needs no later cutting;
    - lean toward a blower with an open exit, because seams and the sting slot then barely leak (PROJECT_STATUS §2).
      Decide together with the fan.
  - Added 2026-11-01 [Proposed]: **model access through removable clear acrylic panels held by magnets** (owner's
    idea, preferred over a sliding panel). Design points:
    - magnets clamp; pins or lips locate each panel so it lands in the same place every time, especially at the
      contraction-to-test-section joint (a 1 mm step in the wall disturbs the flow just before the sphere);
    - the panel's inner face flush with the wall (acrylic set into a printed frame that holds the magnets; magnets
      can be embedded by pausing the print);
    - a thin foam gasket under each panel to seal it and stop it buzzing;
    - the floor (sting slot and balance) stays fixed; the pitot goes through a fixed wall;
    - **keep magnets away from ferrous parts on the measured side of the balance**, and use a non-magnetic sting
      (aluminium, brass or carbon fibre) and non-magnetic fasteners near it. A magnet pulling on a steel sting could
      add a few grams-force, the same size as the drag;
    - holding force: test-section panels see little pressure in a blower with an open exit. A removable 500 mm
      settling-chamber panel would see about 15 N at 10 m/s and 60 N at 20 m/s (estimate), so it needs latches or
      many strong magnets;
    - acrylic 3–5 mm thick, cast rather than extruded (clearer);
    - mark the magnet poles; one flipped magnet repels.
  - Outcome: a design note in `docs/experimental_setup.md` with dimensions and the reasoning, and a DECISIONS.md entry.
  - Verify: Reynolds number, blockage ratio, expected drag and fan duty recomputed for the chosen numbers (see
    [estimates](PROJECT_BACKGROUND.md#order-of-magnitude-estimates)); sphere blockage stays at a few percent or below.
- [ ] **Owner: download the electronics datasheets** on the resources "Wanted" list, items 1–4: pressure-sensor
  candidates (Sensirion SDP810 and SDP31/SDP32, Honeywell TruStability HSC ±1 inH₂O), load-cell candidates (TAL220,
  TAL221), TI LM741 / LM348 / LMC6484 / LM317 / LM7805, Bosch BME280. Outcome: PDFs in `resources/`; an agent files
  them and writes notes. Verify: each has an index row marked "Reviewed".
- [ ] **Review the remaining papers when their topic comes up:** Mehta1977 (fan and wide-angle diffuser), Scheiman1981
  (screens and honeycomb), Morel1975 (contraction), Anthoine2004 (blockage on cylinders), Bradshaw1964, and Barlow1999
  chapters 4, 6, 7, 9–10 and 12.2 (instrumentation; test-section calibration and data systems; balances; boundary
  corrections, needed to confirm the solid-blockage formula; uncertainty). Outcome and verify as above.
- [ ] **Size and choose the fan or blower.**
  - Proposed type (2026-11-01): an inline mixed-flow duct fan with a speed controller. Computer fans and box fans
    cannot push enough air through the honeycomb and screens; a centrifugal blower works but is loud and bulky,
    often with only 2–3 speeds.
  - Look for:
    - a **published fan curve** (flow against static pressure); a fan rated only by free-air CFM cannot be sized;
    - smooth or many-step speed control (the pitot measures the actual speed, so Arduino control is not needed);
    - an EC (brushless DC) motor if affordable, for smoother running.
  - Rough size: a 6-inch fan (listed about 402 CFM and 500 Pa maximum, $90–120) gives roughly 9–13 m/s in a
    120–100 mm section (estimate, session log 2026-11-01). Larger sections or 20 m/s need 8 inches or more.
  - Mount the fan on its own stand with a flexible coupling to the tunnel, so its vibration does not reach the
    balance. A printed round-to-square widening section joins it to the settling chamber.
  - Not suitable: the 120 mm Qirssyn fan from Aki's video (about 95 CFM, at most about 4.5 m/s through a 100 mm
    section even with nothing in the way).
  - Outcome: model recorded, with its performance curve. Verify: at the chosen test-section size and top speed, the
    required flow rate and static pressure (Mehta1979 power-factor method, recomputed for the real screens and
    contraction ratio) sit near the maker's maximum-efficiency point, with power margin.
- [ ] **Choose the blockage-correction method** for the sphere.
  - Proposed 2026-10-31: Maskell with θ = 2.5 plus a solid-blockage term, recorded in
    [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed).
  - Still to do: confirm the solid-blockage formula in Barlow1999 ch. 9–10, then fix the method once the test section
    and sphere are chosen.
  - Outcome: method and formula marked as chosen (D-entry).
  - Verify: the correction for the chosen sphere and test section is computed and stated with its uncertainty
    (θ spread 1.85–2.8). The plan includes a two-sphere-size check (P2 validation run).
- [ ] **Choose sphere diameter(s) and material.** Outcome: diameter, tolerance, surface finish and mounting method recorded.
  Verify: test Re sits inside the subcritical plateau (well below ~2×10⁵); diameter measured with calipers once bought.
- [ ] **Confirm the microcontroller / DAQ.** Candidate (2026-11-01): the owner's Elegoo Mega 2560 R3 (5 V logic,
  I²C on pins 20/21). Weakly2024 used an Uno with one HX711 per load cell; the Mega does everything the Uno does,
  with more pins. Needs the P0 Blink test first. Outcome: board recorded as chosen (D-entry). Verify: it reads the
  HX711 and the chosen pressure sensor at the planned sample rate (interface and logic voltage checked), and logs raw
  counts to a PC as CSV.
- [ ] **Choose the differential pressure sensor range.**
  - Look for:
    - a full-scale range just above the top speed's q: ±125 Pa covers about 14 m/s, ±500 Pa about 29 m/s;
    - digital I²C that runs at 5 V;
    - a small zero-point error;
    - **accuracy stated as % of reading**, because the q error goes straight into C_D.
  - Candidates: Sensirion SDP810-125Pa or -500Pa (3–5.5 V and I²C per distributor listings; about $25–45; one
    reseller lists the 125 Pa part at 3 % of reading and 0.08 Pa zero accuracy, to be confirmed in the datasheet).
    Also the SDP31/SDP32 (3.3 V surface-mount) and Honeywell HSC ±1 inH₂O.
  - Buy the pitot-static probe separately (a drone probe is about $5–20). Drone airspeed kits built on the MS4525DO
    (±1 psi) do not suit these pressures.
  - Outcome: model and range recorded. Verify: full-scale range covers the maximum q (about 240 Pa at 20 m/s,
    estimate) without leaving most of the span unused; offset and noise specs written down.
- [ ] **Choose the load-cell capacity.** Buy a straight-bar cell that has a datasheet; a no-name cell without one
  cannot enter the uncertainty budget. Outcome: capacity recorded. Verify: expected drag plus mount drag
  (grams-force range, estimate) is a usable fraction of full scale; HX711 noise in grams computed from the chosen
  cell's rated output ([HX711 notes](resources/notes/HX711.md)); overload margin for handling noted.
- [ ] **Choose the ambient pressure and temperature sensor** for air density (candidate: Bosch BME280 on a 5 V-compatible
  breakout; a BMP280 also serves for density). Outcome: sensor recorded in docs/experimental_setup.md. Verify: its
  stated accuracy gives a density uncertainty that is small next to the q and force uncertainties.
- [ ] **Decide the role of the op-amp circuit** (LM741/LM348/LMC6484, LM317, LM7805).
  - Proposed 2026-11-01: no op-amps in the measurement chain (the sensors are digital). The kit's regulators and
    potentiometers serve the interface board instead (P2).
  - Outcome: a short circuit description. Verify: supply rails compatible with each part (LM741 is not rail-to-rail
    and expects split supplies). Depends on the pressure-sensor choice and on the parts on hand (P0).
- [ ] **Pick a Re-matched reference for sphere Cd.** Outcome: citation with figure/table and the Cd value at the test Re,
  added to PROJECT_BACKGROUND.md as reviewed. Verify: the source covers the planned Re range. Note: Achenbach (1972)
  covers only Re ≥ 5×10⁴, but the planned Re is roughly 10⁴–10⁵. Candidates now in `resources/`: Morrison2013
  (correlation) backed by Roos1971 (measurements).
- [ ] **Owner: buy hardware** once the above are chosen. Rough total for the electronics plus a 6-inch fan: about
  $200 (PROJECT_STATUS §3). Outcome: parts on hand. Verify: part numbers and datasheets recorded in
  `docs/experimental_setup.md`.

## P2: Build and validate (build steps 2–6)

- [ ] **Build flow conditioning** (honeycomb + screens). Verify: dimensions recorded; photos in docs.
- [ ] **Map flow uniformity** across the test section with the pitot tube. Outcome: velocity map dataset (EXP entry in the
  data catalog). Verify: raw data in `data/raw/`, uniformity (e.g. % deviation from mean) computed by a script.
- [ ] **Optional: flow visualization with a water-mist generator** (owner's idea, 2026-10-30; see the Aki videos in
  [resources/README.md](resources/README.md#videos-and-web-pages)). Qualitative only; it is not part of the measurement
  chain. Uses: spotting swirl or separation in the contraction during the uniformity map, seeing the sphere's wake, and
  photos of the work. **The owner deferred it to the end of the project (2026-10-31)**; only the capped port and
  the window are planned now (sizing task, P1). Design points [Proposed]:
  - In a blower tunnel (fan at the inlet) the inside is at or above atmospheric pressure, so the tunnel will not suck
    mist in as Aki's suction tunnel does.
  - Mist released at the fan inlet passes through the fan, honeycomb and screens and becomes general fog rather than
    visible lines.
  - Instead, push the mist with a small fan on the generator's air intake, through a thin tube (or a row of tubes)
    into the **settling chamber after the last screen, before the contraction**. The flow is already smooth there,
    and the contraction stretches the streaks.
  - Point the tube outlets downstream and match the mist's exit speed to the local air speed. A mismatched jet makes
    its own turbulence. The air there is slow (test-section speed ÷ contraction ratio), so only a gentle push is needed.
  - The fan's position does not decide whether the streaks are smooth; the flow conditioning does.
  - Mist suits the tunnel type only weakly and should not decide blower vs suction.
  - Mist fades at high speed, so run visualization at low speed.
  - Never run mist during force or pressure measurements. Water in the pitot lines or on the load cell corrupts
    readings, and humidity changes air density. Let the tunnel dry afterwards.
  - Use distilled water, and empty and dry the generator after each use. Ultrasonic foggers put whatever is in the
    water (minerals, microbes from standing water) into the air. Keep the mains supply dry.
  - Generator options, compared 2026-11-01 after the owner asked for one that makes thick smoke:
    - **ultrasonic mist maker** (Aki's approach): water, cool, no residue, cheap; fades at high speed. The agent's
      first choice;
    - **glycol fog machine**: the thickest smoke, but warm, leaves an oily film (bad for the pitot holes and the
      surfaces near the balance) and sets off smoke alarms;
    - **smoke wire**: a thin oil-coated wire heated by a short current pulse; the classic lab method for sharp
      streaklines at low speed. Its pulse circuit could be an owner circuit project.

  Outcome: a printed generator plus injection tube. Verify: visible streaklines in the test section at a stated speed
  (photo or video referenced in the data catalog).
- [ ] **Design and build the sensor interface board** (owner's plan, 2026-11-01: design the circuit, possibly test it
  on a breadboard, then turn it into a PCB).
  - Proposed contents: a shield for the Mega 2560 holding:
    - connectors for the HX711 module, the pressure sensor and the BME280;
    - I²C pull-ups and decoupling capacitors;
    - servo power from the kit's LM7805 (kept off the Arduino's own regulator);
    - an input for the angle dial (the kit's 10 kΩ potentiometer).

    Route I²C to the SDA/SCL pins next to AREF so the board also fits an Uno. Design in KiCad (free).
  - A breadboard is fine for testing the digital wiring. **Solder the load-cell leads directly to the HX711**, with no
    breadboard in the bridge wiring (Weakly2024 lesson).
  - Outcome: schematic and PCB files in the repo (folder to be chosen when the first file exists), and an assembled
    board.
  - Verify: an I²C scan finds the pressure sensor and the BME280 through the board, and the HX711 gives a stable
    zero with the wind off.
- [ ] **Build the load cell and its conditioning circuit.** Solder the load-cell leads directly to the HX711, with no
  breadboard in the bridge wiring (lesson from Weakly2024). Verify: stable zero over several minutes with wind off;
  noise recorded.
- [ ] **Calibrate the load cell against known weights.** Outcome: calibration dataset and fit (counts → N). Verify:
  residuals and linearity reported; calibration file referenced from the data catalog.
- [ ] **Sphere Cd validation run.** Outcome: C_D with uncertainty at one or more Re, compared with the reference.
  Verify: mount drag subtracted, blockage corrected, repeated runs agree within the stated uncertainty, analysis
  reproducible from raw data. Proposed 2026-10-31: use at least two sphere sizes (different S/C), if possible at
  matched Re, and check that the blockage-corrected C_D values agree. This tests the correction itself, which has
  no sphere data behind it ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed)).

## P3: After validation (build step 7)

- [ ] **Airfoil pitch attachment** (servo). Defined after the validation result.
  - Owner's idea (2026-10-31, "nothing final"): a dial (potentiometer) to set the angle of attack.
  - Proposed form: dial → microcontroller → servo, with the commanded angle logged in the same CSV as the forces. A
    hardware-only servo-tester circuit (555 timer + potentiometer) would work but could not log the angle.
  - Plan for:
    - commanded ≠ actual angle (servo slop, air load): calibrate against a protractor or measure the pivot angle
      directly;
    - servo jitter vibrating the balance: cut the signal once set, or use a self-locking worm gear;
    - servo wires crossing onto the balance: keep them light and slack.
  - Consider tufts (yarn taped to the wing) to see stall at full speed; Maskell1963 (p. 16) advises visual
    observation of stall onset.
  - Outcome and verify: defined after validation.

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
- [x] 2026-10-31: Owner committed and pushed the reference library as `7db221f`; `/catchup` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md)).
- [x] 2026-10-31: Reviewed Maskell1963 and Cooper1998 (notes files; index rows "Reviewed") and proposed the
  blockage correction and test-section position rules ([session log](docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md)).
- [x] 2026-11-01: Owner committed and pushed the blockage review as `9b42a07` (10 files, as listed in that session's
  commands); `/wrap` confirmed `UP_TO_DATE` ([session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md)).
- [x] 2026-11-01: ECE kit recorded from its packing list, the Elegoo Mega 2560 R3 recorded, and the owner's candidate
  pitot kit and fan assessed ([session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md)).
