# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: choose the fan, the S6 or the VEVOR** (D-011, Tentative since 2026-11-09; "ill consult my budget
  and choose later"). Not ordered yet. **The agent recommends the S6** (2026-11-09): about 2 m/s faster whatever the
  tunnel's true loss factor, makers' figures rather than a seller's, and an EC motor that is likely steadier at low
  speed; the VEVOR still validates if the $45 matters ([buy list](docs/buy_list.md) §1).
  - AC Infinity CLOUDLINE S6, model AI-CLS6: $99; 425 CFM and 503 Pa (maker); EC motor, 10 speed levels; about
    13.0–13.4 m/s with five window screens (straight-line estimate).
  - VEVOR VV-GDFJ-AC6: $53.90; 400 CFM and 300 Pa (seller's figures); AC motor with a speed controller; about
    11.3 m/s, about 73 % of the S6's force at top speed. Both validate.
  - Comparison and the fan-to-tunnel joint: [docs/buy_list.md](docs/buy_list.md) §1.
  - Outcome: a new decision superseding D-011; the model recorded in PROJECT_STATUS §3 and docs/experimental_setup.md.
    Verify: if the VEVOR is chosen, D-010's target is restated as "what the fan reaches, about 11 m/s".
- [ ] **Owner: report what is on hand, then order the parts** in [docs/buy_list.md](docs/buy_list.md). Track them in
  the owner's tracker, [docs/shopping_list.md](docs/shopping_list.md) (2026-11-09): change each row's status To buy →
  Ordered → Got it, and give the agent the part numbers when they arrive. **PLA:** the owner may need more rolls
  (2026-11-09). Weigh the spools; the tunnel needs roughly 3–4 kg in all (estimate, firmed up at sizing).
  - **Ordered so far:** the aluminium window screen (2026-11-09; Saint-Gobain ADFORS FCS9222-M, Bright).
  - **PETG-CF:** the loaded parts need roughly 0.5–1 kg (estimate); weigh that spool too, and buy plain PETG only if
    less is left.
  - The owner will report on 2026-11-10: filament amounts (PLA, PETG-CF); super glue, epoxy, silicone, sandpaper, M3/M4
    screws, rubber feet, duct tape, an acrylic scoring knife, a switched power strip, tin snips, files, a hacksaw.
  - The electronics (one SDP810-125Pa, two TAL221 100 g, a SparkFun HX711, an Adafruit BME280) and most small parts do
    not depend on the fan or on the sizing and can be ordered now.
  - Outcome: each part On hand in the buy list, PROJECT_STATUS §3 and docs/experimental_setup.md, with part numbers.
    Verify: the buy list's "To buy" items are all marked bought or deliberately dropped.
- [ ] **Owner: check the values the agent read from the three new datasheets** (2026-11-08): the checklists at the end
  of [resources/notes/SDP8xx.md](resources/notes/SDP8xx.md), [Sensirion2024.md](resources/notes/Sensirion2024.md)
  and [TAL221.md](resources/notes/TAL221.md). Verify: each notes file's "owner check pending" removed, or the error
  corrected.
- [ ] **Owner: finish the parts-on-hand list.** Recorded: the ECE kit, a multimeter, a soldering station, a bench
  power supply and a workbench (2026-11-01). Also recorded, 2026-11-08/09:
  - 6 in calipers (battery to replace), a hand drill, a spirit level;
  - 43 magnets of 8 × 2 mm;
  - PLA, PETG-CF and a hardened-steel nozzle;
  - school lab balance access.

  Still needed:
  - the bench supply's maximum voltage and current (on its label or front panel);
  - any other electronics the owner has (a photo works);
  - minor: whether the Mega board is printed "R3" (the main chip already reads ATMEGA2560);
  - whether to file the ECE kit's packing list (`PartsListECE2010.pdf`, in the owner's Downloads folder) in the repo
    as evidence for the kit inventory (asked 2026-11-01, not answered).

  Outcome: each item recorded as "On hand" in PROJECT_STATUS.md §3 and docs/experimental_setup.md, citing the owner
  and date. Verify: open question 9 closed.
- [ ] **Owner: confirm or change the tentative decisions** D-003 (private visibility), D-004 (data and LFS policy),
  D-006 (reference PDFs over 25 MB kept local only), D-007's open exit (no exit diffuser) and D-011 (the fan, above)
  in [DECISIONS.md](DECISIONS.md). Verify: status changed to Accepted (or replaced by a new decision).

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
        PROJECT_STATUS open question 13. (2026-11-09: with the chosen screen and 6 mm cells, full decay gives about
        380–390 mm plus frames; open question 15.)
    - Fan pressure: use the low-speed screen K at about 2 m/s (about 1.1–1.8, extrapolated from Wieghardt's
      formula), not the high-speed value.
    - Then recompute the [length budget](PROJECT_BACKGROUND.md#tunnel-length-budget). The diffuser comes out shorter
      and the chamber possibly longer, so the net change is roughly zero.
  - Inputs [Proposed]: contraction ratio 6–9, square section, 5th-order-polynomial wall, length about 1.0 × inlet
    height, sphere at least 0.5 D downstream of the contraction, segmented print (D-005). See the notes in
    [resources/README.md](resources/README.md).
  - Added 2026-11-01 [Proposed], the balance box:
    - only the load cell and HX711 in the closed box under the floor (the owner's sketched "electronics house"); the
      Arduino in a separate box on a cable (no display or knob since D-012);
    - a sting about 80–90 mm long, as short and stiff as the layout allows;
    - optional (2026-11-02): room for a second, vertical load cell for airfoil lift or the owner's model-car idea
      (P3; PROJECT_STATUS open question 14);
    - **load-cell protection for model swaps**: originally a sting lock (a clamp or pin that holds the sting while
      swapping, removed before running), overload stops that let the sting move only slightly past full scale, and a
      low-twist model attachment. **Decided 2026-11-09 ([D-015](DECISIONS.md), owner):** a printed sting mount on the
      cell's top end, the owner's thumb-screw sting lock clamping the sting in it, balls changed with the sting lifted
      out, overload stops at about 120 g (the TAL221's safe overload is 150 g), and no separate hold-still pin. Size
      the hole fit and depth, the screw and the stop gap; hold the mount while turning the screw.
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
    swap the model; the top gives the best reach to the sting tip. **Decided 2026-11-09 ([D-014](DECISIONS.md),
    owner): the top panel lifts off, held by magnets (design later); a removable side panel is still open; the floor
    under the model is a replaceable insert** (a sphere insert with the shield, and a plain insert for cars). Design
    points:
    - magnets clamp; pins or lips locate each panel so it lands in the same place every time, especially at the
      contraction-to-test-section joint (a 1 mm step in the wall disturbs the flow just before the sphere);
    - the panel's inner face flush with the wall (acrylic set into a printed frame that holds the magnets; magnets
      can be embedded by pausing the print);
    - a thin foam gasket under each panel to seal it and stop it buzzing;
    - ~~the floor (sting slot and balance) stays fixed~~ (superseded by D-014: the floor inserts drop in from above,
      sit flush, land on pins and seal at their edges); the pitot goes through a fixed wall;
    - **keep magnets away from ferrous parts on the measured side of the balance**, and use a non-magnetic sting
      (aluminium, brass or carbon fibre) and non-magnetic fasteners near it. A magnet pulling on a steel sting could
      add a few grams-force, the same size as the drag;
    - holding force: test-section panels see little pressure in a blower with an open exit. A removable 500 mm
      settling-chamber panel would see about 15 N at 10 m/s and 60 N at 20 m/s (estimate), so it needs latches or
      many strong magnets;
    - acrylic 3–5 mm thick, cast rather than extruded (clearer);
    - mark the magnet poles; one flipped magnet repels.
  - **Added 2026-11-08/09 [Proposed], from the buy-list session** ([docs/buy_list.md](docs/buy_list.md)):
    - Fan-to-tunnel joint: a printed inlet sized from the measured fan collar (plus one neoprene layer and about
      0.5 mm), about 25–30 mm deep; test-print a 10 mm ring first.
    - Screens: aluminium window screen, with two or three in the diffuser. Consider placing the first slightly into
      the diffuser: at the fan outlet it costs about 24–28 Pa at 13 m/s. Use the §3 table for the fan pressure.
    - Honeycomb: printed (owner), for example 6 mm hexagons, 0.4 mm walls, about 50 mm long.
    - Wall-tap stations S (settling chamber), E (test-section entrance, at least 150 mm ahead of the sphere) and M
      (model station), four taps each: 0.8–1.0 mm holes drilled after printing, with printed bosses holding 1/8 in
      brass stubs. Plus a probe guide across the section.
    - The balance as a removable module that can lay on its side for calibration. The load cell stands upright under
      the ball, clamped only at its top end ([owner's sketch](docs/sketches/README.md)).
    - A sting shield about 7.5 mm wide (5 mm bore), streamlined, fixed to the sphere floor insert (D-014), up to about
      5 mm below the ball; a 5/32 in sleeve at the sting top for the balls' 1/8 in stems.
    - Panels: 1/8 in acrylic in printed frames with 8 × 2 mm magnet pockets (about 8.2–8.3 mm across, 2.2 mm deep).
    - Bolted flanges, M3 screws into brass heat-set inserts, foam tape, screens clamped between the flanges in printed
      frames (decided 2026-11-09, [D-013](DECISIONS.md)); printed feet under each section, no plywood base (owner).
    - Filament: PLA shells (black for the contraction and test section), PETG-CF for loaded parts.
  - **Added 2026-11-09:** settle the seven findings from the drawing package (PROJECT_STATUS open question 15),
    starting with the settling-chamber spacing and how the 250 mm sections split in cross-section. Then update the
    drawings: the numbers in `docs/drawings/wtdata.py`, `python docs/drawings/page.py`, and `preview.py` to check that
    no label overlaps ([docs/drawings/README.md](docs/drawings/README.md)).
  - Outcome: a design note in `docs/experimental_setup.md` with dimensions and the reasoning, and a DECISIONS.md entry.
  - Verify: Reynolds number, blockage ratio, expected drag and fan duty recomputed for the chosen numbers (see
    [estimates](PROJECT_BACKGROUND.md#order-of-magnitude-estimates)); sphere blockage stays at a few percent or below.
- [ ] **Owner: download the remaining electronics datasheets** on the resources "Wanted" list: Bosch BME280, TI
  LM741 / LM348 / LMC6484 / LM317 / LM7805, and the chosen fan's manual. **Done 2026-11-08 by the agent:** SDP8xx,
  TAL221 and Sensirion's signal-compensation note, filed with notes. No longer needed: SDP31/SDP32, Honeywell HSC,
  TAL220 (parts chosen). Outcome: PDFs in `resources/`; an agent files them and writes notes. Verify: each has an index
  row marked "Reviewed".
- [ ] **Review the remaining papers when their topic comes up.** Mehta1977 and Scheiman1981 were done 2026-11-02.
  Remaining:
  - Morel1975 (contraction);
  - Anthoine2004 (blockage on cylinders);
  - Bradshaw1964;
  - Barlow1999 chapters 4, 6, 7, 9–10 and 12.2: instrumentation; test-section calibration and data systems; balances;
    boundary corrections, needed to confirm the solid-blockage formula; uncertainty.

  Outcome: a notes file per paper. Verify: each index row in [resources/README.md](resources/README.md) says
  "Reviewed". Give the owner a checklist of values read from the PDFs to confirm (session log 2026-11-02).
- [ ] **Choose the screens and honeycomb** (new 2026-11-02). **Mostly done 2026-11-09** ([buy list](docs/buy_list.md)
  §3): aluminium window insect screen ("bright aluminum", 18 × 16 mesh, 66–69 % open, about $10 a roll), two or three
  in the diffuser and two in the settling chamber; a **printed honeycomb** (owner), with straws as the upgrade.
  **2026-11-09: screen ordered** (Saint-Gobain ADFORS FCS9222-M, Bright; maker's spec 18 × 16, 0.011 in wire, 66 %
  open). With 0.011 in wire two diffuser screens just meet K_sum 2.1 (2.15), so three are planned for margin.
  Remaining: on arrival, count its wires per inch and check one wire (about 0.28 mm; 0.36 mm or more would drop it
  below 58 % open), then confirm three diffuser screens at sizing.
  - Screens: metal square-mesh, at least 58 % open; for example 20–30 wires/in with 0.19–0.23 mm wire (Scheiman1981
    Table 1). Two go in the diffuser and one or two in the settling chamber.
  - Honeycomb: bought thin-walled (paper or aluminium) or drinking straws rather than printed, unless a printed one
    is shown to work. Cells about 2–3 mm, L/D 7–10. (Superseded 2026-11-09 by the owner's choice of a printed one; the
    flow map, build step 3, is the test.)
  - Outcome: mesh, wire diameter, open area and supplier recorded in docs/experimental_setup.md, with K estimated at
    the settling-chamber speed.
  - Verify: open area at least 0.58 from (1 − d/ℓ)², where d is the wire diameter and ℓ the mesh pitch. Diffuser
    K_sum at least 2.1. If the fan's pressure margin is tight, measure one screen's pressure drop at about 2 m/s.
- [ ] **Size and choose the fan or blower.** The owner picks from the candidates (P0: the S6 or the VEVOR); this task
  checks the choice against the sized tunnel's pressure loss, including the screen losses in the
  [buy list](docs/buy_list.md) §3.
  - Proposed type (2026-11-01): an inline mixed-flow duct fan with a speed controller. Computer fans and box fans
    cannot push enough air through the honeycomb and screens; a centrifugal blower works but is loud and bulky,
    often with only 2–3 speeds. High-pressure 12 V server fans (Delta PFR1212UHE-SP00, 300 Pa) are the exception:
    two side by side should reach about 12 m/s (estimate), with PWM control from the Arduino, but they are loud.
  - Look for:
    - a **published fan curve** (flow against static pressure), or at least a listed maximum static pressure; a fan
      rated only by free-air CFM cannot be sized;
    - smooth or many-step speed control (the pitot measures the actual speed, so Arduino control is not needed);
    - an EC (brushless DC) motor if affordable, for smoother running;
    - a documented low-voltage speed input (PWM or 0–10 V) if the owner's menu is to set the fan speed. No longer
      needed: there is no menu (D-012, 2026-11-08).
  - Need for the 100 mm section at 13 m/s (estimate): about 400 CFM rated and about 500 Pa maximum static pressure
    (corrected 2026-11-05 from "300–500 Pa"). A 6-inch fan listed at 402 CFM and 503 Pa (the Cloudline S6, $99 on
    AC Infinity's site, 2026-11-05) gives about 13 m/s
    ([top-speed trade-off](PROJECT_BACKGROUND.md#top-speed-trade-off-proposed)).
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
- [ ] **Confirm the microcontroller / DAQ.** Candidate (2026-11-01): the owner's Elegoo Mega 2560 (5 V logic,
  I²C on pins 20/21). Weakly2024 used an Uno with one HX711 per load cell; the Mega does everything the Uno does,
  with more pins. The board works: a modified Blink uploaded on 2026-11-02 (PROJECT_STATUS §3). Outcome: board recorded as chosen (D-entry). Verify: it reads the
  HX711 and the chosen pressure sensor at the planned sample rate (interface and logic voltage checked), and logs raw
  counts to a PC as CSV.
- [ ] **Decide the role of the op-amp circuit** (LM741/LM348/LMC6484, LM317, LM7805).
  - Proposed 2026-11-01: no op-amps in the measurement chain (the sensors are digital). The kit's regulators and
    potentiometers serve the interface board instead (P2).
  - Owner, 2026-11-09: the PCB gets DIP sockets for any chips such as op-amps, so they can be swapped.
  - Outcome: a short circuit description. Verify: supply rails compatible with each part (LM741 is not rail-to-rail
    and expects split supplies). Depends on the parts on hand (P0).
- [ ] **Owner: buy hardware** per [docs/buy_list.md](docs/buy_list.md) (see P0). No fixed budget (owner,
  2026-11-01), but price-conscious; the list totals about $315–505. Outcome: parts on hand. Verify: part numbers and
  datasheets recorded in `docs/experimental_setup.md`.

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
  on a breadboard, then turn it into a PCB). **Owner, 2026-11-09:** when the parts arrive, build it on the breadboard,
  test it, then order the PCB; no soldered prototyping shield in between.
  - Proposed contents: a shield for the Mega 2560 holding:
    - **female header sockets** for the HX711 module and the BME280, and a connector for the SDP810's cable (its pins
      are at 2 mm pitch), so modules plug in and can be swapped (owner's socket idea, 2026-11-09); DIP sockets for any
      chips;
    - I²C pull-ups and decoupling capacitors;
    - optionally a PWM output and speed-sense input for a fan with a low-voltage control input.

    No display or encoder headers (D-012, 2026-11-08). The servo-power and angle-dial inputs proposed earlier are no
    longer needed now that the owner has chosen preset angles (2026-11-01).

    Route I²C to the SDA/SCL pins next to AREF so the board also fits an Uno. Design in KiCad (free).
  - A breadboard is fine for testing the digital wiring. **Solder the load-cell leads directly to the HX711**, with no
    breadboard in the bridge wiring (Weakly2024 lesson).
  - Outcome: schematic and PCB files in the repo (folder to be chosen when the first file exists), and an assembled
    board.
  - Verify: an I²C scan finds the pressure sensor and the BME280 through the board, and the HX711 gives a stable
    zero with the wind off.
- [ ] **Data-logging firmware** (replaces the 2026-11-01 "firmware with an on-tunnel display and knob menu", dropped by
  [D-012](DECISIONS.md) on 2026-11-08: all output goes to the laptop).
  - Read the HX711 (raw counts), the SDP810 (DP temperature compensation with "average till read", command 0x3615;
    240 counts/Pa; [SDP8xx notes](resources/notes/SDP8xx.md)) and the BME280; send CSV lines with a timestamp and a
    run flag over USB.
  - Log raw values only. Calibration, the ×966 mbar / p_amb correction and C_D belong in the analysis scripts
    (CLAUDE.md conventions).
  - Live view: the Arduino IDE's Serial Plotter first; a laptop script later if needed.
  - Outcome: firmware in the repo (folder `firmware/`, documented in data/README.md when the first file exists).
    Verify: each sensor's reading follows a change the owner causes (a known mass on the load cell, blowing on a
    pressure port, a finger on the BME280), and the logged sample rate is steady over 10 minutes.
- [ ] **Arrival checks for each new part** (owner; new 2026-11-08). Record each result with the date:
  - TAL221s: wire resistances (red–black about 1090 Ω, green–white about 1000 Ω, cross pairs, body open) and the
    no-load zero, as baselines for spotting damage later;
  - BME280: chip ID 0x60, not a BMP280's 0x58;
  - SDP810: zero with both ports capped, within about 0.1 Pa;
  - calipers: new battery, return to 0.00, a known object measured;
  - window screen (ordered 2026-11-09): 18 and 16 wires per inch against the steel rule, one wire about 0.28 mm
    (0.011 in), "Bright" bare aluminium; store it flat or loosely rolled, since creases do not come out.

  Details: [docs/buy_list.md](docs/buy_list.md) §6, §7 and §10. Verify: values written into
  docs/experimental_setup.md.
- [ ] **Calibrate the pressure sensor against a home-made inclined water manometer** (new 2026-11-08). A water U-tube
  lying on a ramp at about 1 in 10 (100 Pa moves the menisci about 102 mm apart), teed onto the same taps as the
  SDP810 with the tunnel running at 80–100 Pa. It corrects the sensor's 3 % gain error, with the real tubing in place
  ([docs/buy_list.md](docs/buy_list.md) §9). Outcome: a calibration dataset and a gain factor with uncertainty. Verify:
  readings at several pressures agree after correction within the manometer's estimated ±1 %.
- [ ] **Build the load cell and its conditioning circuit.** Solder the load-cell leads directly to the HX711, with no
  breadboard in the bridge wiring (lesson from Weakly2024). Verify: stable zero over several minutes with wind off;
  noise recorded.
- [ ] **Calibrate the load cell against known weights.** Method proposed 2026-11-08 ([buy list](docs/buy_list.md)
  §9): lay the balance module on its side so gravity acts in the drag direction (no pulley friction), and hang masses
  at the ball's position from a budget 10 mg–100 g set (in a light pan hung from a printed attachment on the sting's
  end, with a hook at the ball's centre; owner's idea, 2026-11-09). Weigh every piece once on the school lab balance first, and
  record those masses as raw data. Set the slope with the 2–20 g pieces; check 0.2–3 g, where the drag is.
  Outcome: calibration dataset and fit (counts → N). Verify:
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
  **Owner, 2026-11-09:** lift may never be measured. If not, swap in the plain floor insert (D-014; it replaces the
  printed plug planned earlier the same day), set a model car on it and study it with mist only (a visual study, no
  force). The spare TAL221 stays available for a vertical
  cell. Points from the discussion [Proposed]:
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

- [ ] **Ideas for later experiments (agent, 2026-11-09; the owner has not chosen any).** Details and numbers in the
  [session log](docs/sessions/2026-11-09-fan-advice-and-screen-order.md#2-work-completed). All after the sphere
  validation (D-001), except that (1) characterises the rig:
  1. measure the fan's real curve: printed exit plates with different holes; flow from the test-section speed,
     pressure from a tap after the fan (a water U-tube above 125 Pa). Tests the straight-line fan estimates;
  2. pressure around a cylinder: a 3/8 in brass tube across the section with one tap, turned in 10° steps, at
     10 m/s or below (±125 Pa sensor); about 9.5 % blockage, so it needs a correction;
  3. a pitot traverse of the free jet leaving the open exit;
  4. a drag lineup of 19 mm printed shapes (disc, cups both ways, cone, teardrop) on the balance;
  5. vortex-shedding tone of a 1/8 in rod (about 410–820 Hz at 6.5–13 m/s), recorded by phone or laptop.

  Not possible here: the drag crisis (top Re about 2×10⁴), turbulence measurements (need a hot-wire), models wider
  than about 22 × 22 mm. Outcome and verify: defined if the owner takes one up.

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
- [x] 2026-11-03: Owner committed and pushed the board-test session as `36f39eb`; `/catchup` confirmed `UP_TO_DATE`
  on 2026-11-05 ([session log](docs/sessions/2026-11-07-top-speed-and-fan-search.md)).
- [x] 2026-11-07: Owner committed and pushed the top-speed and fan-search session as `d7f5cdf`; `/catchup` confirmed
  `UP_TO_DATE` on 2026-11-08 ([session log](docs/sessions/2026-11-09-buy-list.md)).
- [x] 2026-11-08: **Target top airspeed confirmed:** 13 m/s, validation from about 6.5 m/s ([D-010](DECISIONS.md),
  owner). Not a must-have: 11–12 m/s still validates ([session log](docs/sessions/2026-11-09-buy-list.md)).
- [x] 2026-11-08: **Sphere diameters and material chosen:** Delrin (acetal) balls, 3/4 in (2.85 % blockage) and 1 in
  (5.07 %), ±0.001 in, two of each; press-fit on brass stems, drilled with a printed jig. The Re-matched pair: the
  3/4 in ball at 13 m/s against the 1 in ball at 9.75 m/s ([buy list](docs/buy_list.md) §6).
- [x] 2026-11-08: **Pressure sensor chosen:** one Sensirion SDP810-125Pa (owner chose one over two). Datasheet
  reviewed: 0.08 Pa + 3 % of reading, I²C 0x25, solder pins at 2 mm pitch. Ambient-pressure correction ×966 mbar /
  p_amb required ([SDP8xx notes](resources/notes/SDP8xx.md), [Sensirion2024 notes](resources/notes/Sensirion2024.md)).
  Probe made in-house: brass total-pressure tube and wall taps ([buy list](docs/buy_list.md) §5).
- [x] 2026-11-08: **Load-cell capacity chosen:** TAL221 100 g, two of them, with a SparkFun HX711. Datasheet reviewed
  ([TAL221 notes](resources/notes/TAL221.md)).
- [x] 2026-11-08: **Ambient sensor chosen:** Adafruit BME280 (2652), with level shifting for 5 V
  ([buy list](docs/buy_list.md) §7).
- [x] 2026-11-08/09: **Full buy list written with the owner**, [docs/buy_list.md](docs/buy_list.md): 11 sections, about
  $315–505. Also recorded D-011 (fan; reopened 2026-11-09) and D-012 (no display or knob), and filed the owner's
  load-cell sketch ([session log](docs/sessions/2026-11-09-buy-list.md)).
- [x] 2026-11-09: Owner committed and pushed the buy-list session as `0351407`; `/catchup` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-09-shopping-list.md)).
- [x] 2026-11-09: **Owner's shopping tracker** written, [docs/shopping_list.md](docs/shopping_list.md): what is still
  to buy, with qty, price, link and status, grouped by store; about $255–360 plus the fan
  ([session log](docs/sessions/2026-11-09-shopping-list.md)). Owner committed and pushed it as `b08a151`.
- [x] 2026-11-09: Owner committed and pushed the shopping-list follow-up (how the calibration masses hang) as
  `0558370`; `/catchup` confirmed `UP_TO_DATE` ([session log](docs/sessions/2026-11-09-drawing-package.md)).
- [x] 2026-11-09: **Preliminary drawing package** of the whole tunnel, [docs/drawings/](docs/drawings/README.md):
  10 sheets, a 70-item parts list, a TBD register and seven findings (pre-sizing, not for manufacture). The owner's
  flange, load-cell and test-chamber sketch filed and compressed; D-013 (bolted flange joints), D-014 (top panel on
  magnets, floor inserts) and D-015 (sting mount and thumb-screw sting lock) recorded
  ([session log](docs/sessions/2026-11-09-drawing-package.md)).
- [x] 2026-11-09: Owner committed and pushed the drawing-package session as `507f71c`; `/catchup` confirmed
  `UP_TO_DATE` ([session log](docs/sessions/2026-11-09-fan-advice-and-screen-order.md)).
- [x] 2026-11-09: **Screen chosen and ordered** (owner): Saint-Gobain ADFORS FCS9222-M, Bright, 36 × 84 in roll from
  Home Depot; 18 × 16, 0.011 in wire per the maker's spec, 66 % open. The first part ordered
  ([session log](docs/sessions/2026-11-09-fan-advice-and-screen-order.md)).
