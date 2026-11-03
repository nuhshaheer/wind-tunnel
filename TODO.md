# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: give the target top airspeed.** The test section (100 mm, D-008) and length (about 1 m target, more
  allowed) are settled. The top speed sets the pressure-sensor range (±125 Pa covers about 14 m/s) and confirms the
  fan. 10–13 m/s is enough for the sphere validation. Outcome: recorded under "Requirements and constraints" in
  PROJECT_BACKGROUND.md. Verify: the sensor-range and fan tasks (P1) can be finished without guessing it.
- [ ] **Owner: choose the fan** from the candidates in [PROJECT_STATUS.md](PROJECT_STATUS.md) §3.
  - Agent's pick: a 6-inch mixed-flow EC inline fan. Either the VIVOSUN AeroZesh S6 (from about $63; first find its
    static pressure in the manual or from VIVOSUN) or the AC Infinity Cloudline S6 ($90–120, about 500 Pa listed).
  - Alternative if menu control of the fan matters from day one: two Delta PFR1212UHE-SP00 12 V PWM server fans
    (very loud; need about 5.4 A at 12 V from the bench supply; buy from a real distributor because fakes are common).
  - Check the listing for a 6-inch outlet, a maximum static pressure figure, an included speed controller and a
    return policy.
  - Outcome: model recorded in PROJECT_STATUS §3 and docs/experimental_setup.md with its datasheet or listed specs.
    Verify: its listed maximum static pressure is at least about 300 Pa and its free-air flow about 400 CFM (or the
    pair's combined), which covers 15 m/s with margin by the estimate in
    [PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#tunnel-length-budget).
- [ ] **Owner: finish the parts-on-hand list.** The ECE kit, a multimeter, a soldering station, a bench power supply
  and a workbench are recorded (2026-11-01). Still needed:
  - the bench supply's maximum voltage and current (on its label or front panel);
  - any other electronics the owner has (a photo works);
  - the magnets' type and size;
  - minor: whether the Mega board is printed "R3" (the main chip already reads ATMEGA2560);
  - whether to file the ECE kit's packing list (`PartsListECE2010.pdf`, in the owner's Downloads folder) in the repo
    as evidence for the kit inventory (asked 2026-11-01, not answered).

  Outcome: each item recorded as "On hand" in PROJECT_STATUS.md §3 and docs/experimental_setup.md, citing the owner
  and date. Verify: open question 9 closed.
- [ ] **Owner: confirm or change the tentative decisions** D-003 (private visibility), D-004 (data and LFS policy),
  D-006 (reference PDFs over 25 MB kept local only) and D-007's open exit (no exit diffuser) in
  [DECISIONS.md](DECISIONS.md). Verify: status changed to Accepted (or replaced by a new decision).

## P1: Design and choose hardware (build step 1)

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
    4. Why does the reference C_D depend on the Reynolds number, and why is ours about 0.42–0.445 rather than 0.47
       (D-009)?
    5. Why do the walls change the measured drag?
  - Verify: the owner can discuss those questions when making the sizing decisions.
- [ ] **Size the contraction and test section.** Fix the test-section length, contraction ratio, contraction wall
  shape and length, the settling chamber and the fan-to-chamber diffuser, and the target airspeed range.
  - **Decided 2026-11-01 (owner):** an open-circuit blower with the fan at the front (D-007) and a 100 mm × 100 mm
    test section (D-008). Proposed, from the
    [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget): contraction ratio 6.25 (250 mm settling chamber),
    contraction about 250 mm long, test section 270–290 mm, open exit; about 1.15–1.3 m including a 6-inch fan.
    The wide-angle diffuser from the round fan outlet (152 mm) to the 250 mm square chamber has an area ratio of
    about 3.4: check it against Mehta1977 and Mehta1979 Fig. 3.
  - **Added 2026-11-02 [Proposed], from Mehta1977, Scheiman1981 and Wieghardt1953:**
    - Fan-to-chamber diffuser: A = 3.44, K_sum ≥ 2.1. Two screens (K ≈ 1.1–1.5 each), one at the inlet angle change
      and one at the exit, give about 150–200 mm (Fig. 5 minimum about 115 mm).
      - Curved walls or radiused corners; filleted corners.
      - No honeycomb or straightener at the fan outlet.
      - Details in the [Mehta1977 notes](resources/notes/Mehta1977.md#what-it-suggests-for-this-project-proposed).
    - Settling chamber: a honeycomb (L/D 7–10, about 2–3 mm cells), then one or two screens at least 58 % open, then
      50 mm to the contraction.
      - Choose between Mehta1979's 0.2 D spacing (chamber about 150–200 mm) and full-decay spacing: 500 wire
        diameters between screens and about 50 cell diameters after the honeycomb (about 230–300 mm). See
        PROJECT_STATUS open question 13.
    - Fan pressure: use the low-speed screen K at about 2 m/s (about 1.1–1.8, extrapolated from Wieghardt's
      formula), not the high-speed value.
    - Then recompute the [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget). The diffuser comes out shorter
      and the chamber possibly longer, so the net change is roughly zero.
  - Inputs [Proposed]: contraction ratio 6–9, square section, 5th-order-polynomial wall, length about 1.0 × inlet
    height, sphere at least 0.5 D downstream of the contraction, segmented print (D-005). See the notes in
    [resources/README.md](resources/README.md).
  - Added 2026-11-01 [Proposed], the balance box:
    - only the load cell and HX711 in the closed box under the floor (the owner's sketched "electronics house"); the
      display, knob and Arduino in a separate box on a cable;
    - a sting about 80–90 mm long, as short and stiff as the layout allows;
    - optional (2026-11-02): room for a second, vertical load cell for airfoil lift or the owner's model-car idea
      (P3; PROJECT_STATUS open question 14);
    - **load-cell protection for model swaps**: a sting lock (a clamp or pin that holds the sting while swapping,
      removed before running), overload stops that let the sting move only slightly past full scale, and a low-twist
      model attachment (for example a push fit with a set screw). Small bar cells are typically rated for only about
      120 % of capacity; check the chosen cell's datasheet.
  - Added 2026-10-31 [Proposed]:
    - a **closed** test section with a clear window;
    - the test-section length set by the position rules: reference pressure at least 1.5√C upstream of the sphere,
      sphere at least 4√S from the end ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed));
    - choose where the airspeed reference is read (PROJECT_STATUS open question 10);
    - a capped mist port after the last screen, so optional visualization needs no later cutting;
    - lean toward a blower with an open exit, because seams and the sting slot then barely leak (PROJECT_STATUS §2).
      Decided 2026-11-01: blower (D-007).
  - Added 2026-11-01 [Proposed]: **model access through removable clear acrylic panels held by magnets** (owner's
    idea, preferred over a sliding panel). Owner's concept: one test chamber whose top and/or side panel comes off to
    swap the model; the top gives the best reach to the sting tip. Design points:
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
- [ ] **Review the remaining papers when their topic comes up.** Mehta1977 and Scheiman1981 were done 2026-11-02.
  Remaining:
  - Morel1975 (contraction);
  - Anthoine2004 (blockage on cylinders);
  - Bradshaw1964;
  - Barlow1999 chapters 4, 6, 7, 9–10 and 12.2: instrumentation; test-section calibration and data systems; balances;
    boundary corrections, needed to confirm the solid-blockage formula; uncertainty.

  Outcome: a notes file per paper. Verify: each index row in [resources/README.md](resources/README.md) says
  "Reviewed". Give the owner a checklist of values read from the PDFs to confirm (session log 2026-11-02).
- [ ] **Choose the screens and honeycomb** (new 2026-11-02).
  - Screens: metal square-mesh, at least 58 % open; for example 20–30 wires/in with 0.19–0.23 mm wire (Scheiman1981
    Table 1). Two go in the diffuser and one or two in the settling chamber.
  - Honeycomb: bought thin-walled (paper or aluminium) or drinking straws rather than printed, unless a printed one
    is shown to work. Cells about 2–3 mm, L/D 7–10.
  - Outcome: mesh, wire diameter, open area and supplier recorded in docs/experimental_setup.md, with K estimated at
    the settling-chamber speed.
  - Verify: open area at least 0.58 from (1 − d/ℓ)², where d is the wire diameter and ℓ the mesh pitch. Diffuser
    K_sum at least 2.1. If the fan's pressure margin is tight, measure one screen's pressure drop at about 2 m/s.
- [ ] **Size and choose the fan or blower.** The owner picks from the candidates (P0); this task checks the choice.
  - Proposed type (2026-11-01): an inline mixed-flow duct fan with a speed controller. Computer fans and box fans
    cannot push enough air through the honeycomb and screens; a centrifugal blower works but is loud and bulky,
    often with only 2–3 speeds. High-pressure 12 V server fans (Delta PFR1212UHE-SP00, 300 Pa) are the exception:
    two side by side should reach about 12 m/s (estimate), with PWM control from the Arduino, but they are loud.
  - Look for:
    - a **published fan curve** (flow against static pressure), or at least a listed maximum static pressure; a fan
      rated only by free-air CFM cannot be sized;
    - smooth or many-step speed control (the pitot measures the actual speed, so Arduino control is not needed);
    - an EC (brushless DC) motor if affordable, for smoother running;
    - a documented low-voltage speed input (PWM or 0–10 V) if the owner's menu is to set the fan speed.
  - Need for the 100 mm section (estimate): about 400 CFM rated, 300–500 Pa maximum static pressure. A 6-inch fan
    (listed about 402 CFM and 500 Pa maximum, $90–120) gives about 13 m/s
    ([length budget](PROJECT_BACKGROUND.md#tunnel-length-budget)).
  - Mount the fan on its own stand with a flexible coupling to the tunnel, so its vibration does not reach the
    balance. A printed round-to-square widening section joins it to the settling chamber.
  - Not suitable: the 120 mm Qirssyn fan from Aki's video (about 95 CFM, at most about 4.5 m/s through a 100 mm
    section even with nothing in the way), and 6-inch "booster" duct fans (axial, no pressure figure).
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
- [ ] **Choose sphere diameter(s) and material.** Proposed for the 100 mm section (2026-11-01): about 20 mm (3.1 %
  blockage) and about 25 mm (4.9 %) for the two-size check. Outcome: diameter, tolerance, surface finish and mounting
  method recorded (a low-twist attachment to the sting, see the sizing task). Verify: test Re sits inside the
  subcritical plateau (well below ~2×10⁵; a 20 mm sphere at 10 m/s is about 1.3×10⁴); diameter measured with calipers
  once bought. Plan the two-size check at **matched Re** (D-009). For example, 20 mm at 12.5 m/s matches 25 mm at
  10 m/s (our arithmetic).
- [ ] **Confirm the microcontroller / DAQ.** Candidate (2026-11-01): the owner's Elegoo Mega 2560 (5 V logic,
  I²C on pins 20/21). Weakly2024 used an Uno with one HX711 per load cell; the Mega does everything the Uno does,
  with more pins. The board works: a modified Blink uploaded on 2026-11-02 (PROJECT_STATUS §3). Outcome: board recorded as chosen (D-entry). Verify: it reads the
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
  cannot enter the uncertainty budget. Expected sphere drag in the 100 mm section: about 0.9 gf at 10 m/s and 2.0 gf
  at 15 m/s (estimate), plus the sting's drag. Outcome: capacity recorded. Verify: expected drag plus mount drag is a
  usable fraction of full scale; HX711 noise in grams computed from the chosen cell's rated output
  ([HX711 notes](resources/notes/HX711.md)); safe-overload rating noted and the sting lock and overload stops (sizing
  task) designed around it.
- [ ] **Choose the ambient pressure and temperature sensor** for air density (candidate: Bosch BME280 on a 5 V-compatible
  breakout; a BMP280 also serves for density). Outcome: sensor recorded in docs/experimental_setup.md. Verify: its
  stated accuracy gives a density uncertainty that is small next to the q and force uncertainties.
- [ ] **Decide the role of the op-amp circuit** (LM741/LM348/LMC6484, LM317, LM7805).
  - Proposed 2026-11-01: no op-amps in the measurement chain (the sensors are digital). The kit's regulators and
    potentiometers serve the interface board instead (P2).
  - Outcome: a short circuit description. Verify: supply rails compatible with each part (LM741 is not rail-to-rail
    and expects split supplies). Depends on the pressure-sensor choice and on the parts on hand (P0).
- [ ] **Owner: buy hardware** once the above are chosen. No fixed budget (owner, 2026-11-01). Rough total for the
  electronics plus a 6-inch fan: about $120–200 (PROJECT_STATUS §3). Outcome: parts on hand. Verify: part numbers and datasheets recorded in
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
    - headers for the display (I²C) and the rotary encoder (two interrupt pins plus the push switch) of the menu
      task below;
    - optionally a PWM output and speed-sense input for a 12 V fan, if one with a low-voltage control input is
      chosen.

    The servo-power and angle-dial inputs proposed earlier are no longer needed now that the owner has chosen preset
    angles (2026-11-01).

    Route I²C to the SDA/SCL pins next to AREF so the board also fits an Uno. Design in KiCad (free).
  - A breadboard is fine for testing the digital wiring. **Solder the load-cell leads directly to the HX711**, with no
    breadboard in the bridge wiring (Weakly2024 lesson).
  - Outcome: schematic and PCB files in the repo (folder to be chosen when the first file exists), and an assembled
    board.
  - Verify: an I²C scan finds the pressure sensor and the BME280 through the board, and the HX711 gives a stable
    zero with the wind off.
- [ ] **Firmware with an on-tunnel display and knob menu** (owner's idea, 2026-11-01: "like the menu for an Ender 3
  with a knob"; choose what to see, such as drag force, and change the fan speed).
  - Proposed hardware: a 20×4 character LCD with an I²C adapter (shares pins 20/21 with the pressure sensor) and a
    push-button rotary encoder on interrupt pins 2/3 or 18/19 (pins 20/21 are I²C). Start on the breadboard. Upgrade
    option: a 128×64 graphic LCD like the Ender 3's, for live graphs.
  - Proposed menu: live readout (V, q, F, C_D), tare (wind-off zero), calibrate with a known mass, model setup (sphere
    diameter), fan speed (only if the fan has a documented low-voltage input; otherwise the fan's own dial), logging
    on/off.
  - The laptop log over USB stays the data record; the screen is for watching live. Refresh the screen only 2–5 times
    a second so drawing does not slow the sensor readings.
  - Put the display, knob and Arduino in a box separate from the load-cell box.
  - Outcome: firmware in the repo (folder `firmware/`, documented in data/README.md when the first file exists).
    Verify: the menu works on the bench, and logging rate and timing with the screen running match those without it.
- [ ] **Build the load cell and its conditioning circuit.** Solder the load-cell leads directly to the HX711, with no
  breadboard in the bridge wiring (lesson from Weakly2024). Verify: stable zero over several minutes with wind off;
  noise recorded.
- [ ] **Calibrate the load cell against known weights.** Outcome: calibration dataset and fit (counts → N). Verify:
  residuals and linearity reported; calibration file referenced from the data catalog.
- [ ] **Sphere Cd validation run.** Outcome: C_D with uncertainty at several Re, compared with the reference.
  - **Reference (D-009, 2026-11-02):** Brown and Lawler Eq. (19) at each run's Re, with a band of about ±10 %. The
    analysis script computes it per run; see the [Brown2003 notes](resources/notes/Brown2003.md).
  - Verify:
    - mount drag subtracted and blockage corrected;
    - repeated runs agree within the stated uncertainty;
    - the analysis is reproducible from raw data;
    - corrected C_D lies inside the ±10 % band;
    - C_D rises with Re across about 5–15 m/s, as Eq. (19) predicts (about 12 %).
  - Proposed 2026-10-31: use at least two sphere sizes (different S/C) at **matched Re**, and check that the
    blockage-corrected C_D values agree. This tests the correction itself, which has no sphere data behind it
    ([PROJECT_BACKGROUND.md](PROJECT_BACKGROUND.md#blockage-correction-proposed)).

## P3: After validation (build step 7)

- [ ] **Airfoil tests at preset angles of attack.** Defined after the validation result.
  - **Owner, 2026-11-01:** preset angles, because a pivoting airfoil would ruin the force measurement (note on the
    [sketch](docs/sketches/README.md)). This replaces the earlier dial-and-servo idea below.
  - Proposed form: an indexed hub on the same sting, with a pin that drops into holes at set angles (for example 0°,
    2°, 4° …), so one airfoil covers many angles. Stop the tunnel and take a wind-off zero between angles.
  - Lift matters as much as drag for an airfoil, and measuring it needs a second load cell (Weakly2024 used two).
    Decide whether to measure lift before designing the hub.
  - Earlier idea (owner, 2026-10-31, "nothing final"; superseded 2026-11-01): a dial → microcontroller → servo, with
    the commanded angle logged in the CSV. Its points to plan for were: commanded ≠ actual angle; servo jitter
    vibrating the balance; servo wires crossing onto the balance.
  - Consider tufts (yarn taped to the wing) to see stall at full speed; Maskell1963 (p. 16) advises visual
    observation of stall onset.
  - Outcome and verify: defined after validation.
- [ ] **Idea (owner, 2026-11-02, "just an idea"): model-car downforce with a second load cell.** Not planned yet.
  Points from the discussion [Proposed]:
  - **Same hardware as airfoil lift.** Downforce and lift are the same vertical force, so a second, vertical load
    cell, rigidly coupled at right angles to the drag cell as in Weakly2024, would serve both. Leave room for it in
    the balance box (P1 sizing task).
  - **Hold the car on a short post from the balance, wheels just clear of a fixed floor** (about 0.5–1 mm). Do not
    use a weighing platform under the car: the low pressure under the car also pulls the platform up, so the
    platform cancels much of the downforce.
  - **"Blown away":** lift-off is unlikely, since the forces are a few gf against a car weighing tens of grams. Free
    wheels would roll, though, and the post fixes that.
  - **Size:** the floor acts as a mirror, so keep the frontal area to about 25 mm wide × 20 mm tall in the 100 mm
    section (about 5 % effective blockage). A 1:64 die-cast car is borderline; 1:43 is too big.
  - **Forces** at 13 m/s: drag about 1.5 gf, lift or downforce a few gf (estimate). Most road-car shapes make lift,
    not downforce.
  - **Limits:** a fixed floor is not a moving road. The floor boundary layer (about 2 mm, estimate) is comparable to
    a model's ground clearance, and Re is about 150 times below a real car's. So results compare shapes in this
    tunnel; they do not predict a real car.
  - A standard reference shape exists: the Ahmed body (Ahmed et al. 1984, SAE 840300; citation from the agent's
    memory, not checked, not in `resources/`).
  - Outcome and verify: defined if the owner takes it up after validation.

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
- [x] 2026-11-01: Owner committed and pushed the parts review as `748dae9`; `/wrap` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md)).
- [x] 2026-11-01: Sizing inputs, part 1: the owner chose a blower with the fan at the front (D-007) and a 100 mm test
  section (D-008), with a length target of about 1 m (more allowed). The top speed is still open (P0)
  ([session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md)).
- [x] 2026-11-01: The owner's first sketch filed in [docs/sketches/](docs/sketches/README.md), and the multimeter,
  soldering station, bench power supply and workbench recorded as on hand
  ([session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md)).
- [x] 2026-11-01: Owner committed and pushed part 2 of that session as `8fda08f`, with the sketch PDF uncompressed;
  `/catchup` confirmed `UP_TO_DATE` on 2026-11-02 ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md)).
- [x] 2026-11-02: Reviewed the C_D-reference papers Morrison2013 and Roos1971, then Brown2003 (added by the owner).
  Picked the Re-matched sphere C_D reference: Brown and Lawler Eq. (19), ±10 %, plus a trend check
  ([D-009](DECISIONS.md), Accepted by the owner)
  ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md)).
- [x] 2026-11-02: Reviewed Mehta1977 and Scheiman1981 for the 100 mm layout, and Wieghardt1953 (added by the owner)
  for screen K. The owner checked the key values against the PDFs
  ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md)).
- [x] 2026-11-02: Owner committed and pushed the session as `c04de1b`; `sync_status.py --fetch` confirmed
  `UP_TO_DATE`. The owner then renamed the GitHub account to `nuhshaheer`
  ([session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md)).
- [x] 2026-11-02: Owner pointed `origin` at https://github.com/nuhshaheer/wind-tunnel.git and committed and pushed the
  follow-up as `b22a45b`; `/catchup` confirmed `UP_TO_DATE` with the new remote
  ([session log](docs/sessions/2026-11-03-mega-2560-board-test.md)).
- [x] 2026-11-02: Owner set up the Elegoo Mega 2560: the main chip reads ATMEGA2560, Windows lists it on COM3
  (USB ID 2341:0042), and Blink with the delays changed from 1000 to 200 ms uploaded from Arduino IDE 2.3.10 and made
  the "L" LED blink faster. Verified (PROJECT_STATUS §3;
  [session log](docs/sessions/2026-11-03-mega-2560-board-test.md)).
