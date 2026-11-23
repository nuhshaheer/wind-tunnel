# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: close the 2026-11-23 bring-up** (new 2026-11-23; [session log](docs/sessions/2026-11-23-sensor-bring-up.md) §10). Send the agent:
  - the penny's year (1983 or later is 2.5 g, 1982 or earlier probably 3.11 g), or better, its mass from the school
    balance, to settle the counts-per-gram estimate (about 13,300 or 10,700 counts/g);
  - the HX711's excitation voltage: USB in, DC volts, red probe on the RED pad, black on BLK (walk-through step 3 item 5);
  - the Adafruit BME280 Library version (Library Manager);
  - which wire was moving when the BME280 reset at about 63 s, if remembered.

  And at the bench: mark the SDP810's High barb; firm up the BME280's connection (a 6-pin male header strip pressed
  into the breadboard, and the hanging jumper bundle taped down); remove R1 and R2 to match sheet 12, or say to keep
  them (the photos suggest they are still fitted; harmless). Outcome: each value recorded in
  [docs/experimental_setup.md](docs/experimental_setup.md#breadboard-as-built). Verify: the 2026-11-23 log's §10 items closed.
- [ ] **Agent, with the owner at the bench: the combined logging sketch** (walk-through step 4; new 2026-11-23). One CSV
  line per sample with time, HX711 counts, SDP810 dp (raw and × 96600 / p_amb), BME280 p, T and RH, and a flag column
  for BME280 resets and failed reads, following [D-019](DECISIONS.md). Details in P2 "Data-logging firmware". Outcome:
  `firmware/logger/` (name to confirm). Verify: a 10-minute run with a steady sample rate and every value responding to
  a change the owner causes, recorded in docs/experimental_setup.md.
- [ ] **Owner: choose the fan, the S6 or the VEVOR** (D-011, Tentative since 2026-11-09; "ill consult my budget
  and choose later"). Not ordered yet. **The agent recommends the S6** (2026-11-09): about 2 m/s faster whatever the
  tunnel's true loss factor, makers' figures rather than a seller's, and an EC motor that is likely steadier at low
  speed; the VEVOR still validates if the $45 matters ([buy list](docs/buy_list.md) §1).
  - AC Infinity CLOUDLINE S6, model AI-CLS6: $99; 425 CFM and 503 Pa (maker); EC motor, 10 speed levels; about
    13.0–13.4 m/s with five window screens (straight-line estimate).
  - VEVOR VV-GDFJ-AC6: $53.90; 400 CFM and 300 Pa (seller's figures); AC motor with a speed controller; about
    11.3 m/s, about 73 % of the S6's force at top speed. Both validate.
  - Comparison and the fan-to-tunnel joint: [docs/buy_list.md](docs/buy_list.md) §1.
  - **Timing (owner, 2026-11-10):** buy the fan later, when the prints are ready, so its 30-day return window covers
    the real test. Agent's advice: buy it once the airspeed readout works (SDP810, probe and firmware), then measure the
    top speed and the load-cell noise with the fan running inside the window; check the seller's return terms. Still
    choose the model before the fan stand is designed (the two fans differ in size).
  - Outcome: a new decision superseding D-011; the model recorded in PROJECT_STATUS §3 and docs/experimental_setup.md.
    Verify: if the VEVOR is chosen, D-010's target is restated as "what the fan reaches, about 11 m/s".
- [ ] **Owner: report what is on hand and send the part details the sizing needs** (new 2026-11-10; every ordered part
  arrived by 2026-11-17, see Done). Send the agent:
  - the **heat-set inserts' length and outside diameter** (the printed holes are sized to them);
  - ~~which acrylic sheets were bought~~ **answered 2026-11-10: four 8 × 12 in sheets** (owner); each gives one window
    up to about 305 mm long;
  - ~~the SDP810 part number on the Mouser order~~ **answered 2026-11-10: Mouser 403-SDP810-125PA, maker's part
    SDP810-125PA** (owner), the ±125 Pa part;
  - **filament on hand:** PLA (4 kg black arrived by 2026-11-17; the tunnel needs roughly 3–4 kg in all) and PETG-CF (the loaded
    parts need roughly 0.5–1 kg; buy plain PETG only if less is left);
  - which **"check house" items** are at home: power strip, sealant, super glue and epoxy, heat-shrink, solder, steel
    rule, files, hacksaw, tin snips;
  - ~~what the school lab balance reads to~~ **answered 2026-11-19: 0.01 g** (CGOLDENWALL HZ50002B, 5000 g; owner);
  - ~~which CAD program you use~~ **answered 2026-11-17: Fusion 360** (owner; note on D-017);
  - optional: **hours a week and any deadline** (added 2026-11-15), to narrow the schedule estimate (about 70–155 h to
    the validation; [session log](docs/sessions/2026-11-17-time-estimates-and-cad.md#6-measurements-and-results)).

  **Every ordered part arrived by 2026-11-17** (owner); [docs/shopping_list.md](docs/shopping_list.md) is marked "Got
  it". Now do each arrival check (P2). Outcome: each part On hand in the buy list, PROJECT_STATUS §3 and docs/experimental_setup.md, with part numbers.
  Verify: no "Ordered" row left once the parcels are in, and the sizing inputs above recorded.
- [ ] **Owner: check the values the agent read from four documents** (2026-11-08 and 2026-11-17): the checklists at
  the end of [resources/notes/SDP8xx.md](resources/notes/SDP8xx.md), [Sensirion2024.md](resources/notes/Sensirion2024.md),
  [TAL221.md](resources/notes/TAL221.md) and [WaveshareBME280.md](resources/notes/WaveshareBME280.md) (added 2026-11-17). Verify: each notes file's "owner check pending" removed, or the error
  corrected.
- [ ] **Owner: finish the parts-on-hand list.** Recorded: the ECE kit, a multimeter, a soldering station, a bench
  power supply and a workbench (2026-11-01). Also recorded, 2026-11-08/09:
  - 6 in calipers (battery to replace), a hand drill, a spirit level;
  - 43 magnets of 8 × 2 mm;
  - PLA, PETG-CF and a hardened-steel nozzle;
  - school lab balance access (a CGOLDENWALL HZ50002B, d = 0.01 g, 2026-11-19);
  - a calibration weight set (50–2 g and a hanging rod; owner, 2026-11-19).

  Still needed:
  - the bench supply's maximum voltage and current (on its label or front panel);
  - any other electronics the owner has (a photo works);
  - ~~whether the Mega board is printed "R3"~~ **answered by the 2026-11-18 photos: R3 layout, with SDA1 and SCL1 beside
    AREF**;
  - whether to file the ECE kit's packing list (`PartsListECE2010.pdf`, in the owner's Downloads folder) in the repo
    as evidence for the kit inventory (asked 2026-11-01, not answered).

  Outcome: each item recorded as "On hand" in PROJECT_STATUS.md §3 and docs/experimental_setup.md, citing the owner
  and date. Verify: open question 9 closed.
- [ ] **Owner: confirm or change the tentative decisions** D-003 (private visibility), D-004 (data and LFS policy),
  D-006 (reference PDFs over 25 MB kept local only), D-007's open exit (no exit diffuser), D-011 (the fan, above),
  D-016 (one full-length sting per ball, no sleeve; "confirm at sizing") D-018 (the sensor circuit, agent's design,
  2026-11-17; the breadboard test passed on 2026-11-23) and D-019 (bring-up firmware conventions, agent's choice,
  2026-11-23) in [DECISIONS.md](DECISIONS.md). Verify:
  status changed to Accepted (or replaced by a new decision).
- [ ] **Owner: say whether to republish the drawings' private claude.ai copy** (added 2026-11-10). It still shows
  revision B (with the 5/32 in sleeve); the repo copy is revision D, with the electrical sheets 11 and 12
  ([docs/drawings/README.md](docs/drawings/README.md)). Agents republish only on the owner's go-ahead. Outcome: the
  published copy matches `docs/drawings/wind-tunnel-drawings.html`, or a note that only the repo copy is kept. Verify:
  the drawings README no longer says the published copy shows revision B.

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
    - lean toward a blower with an open exit, because seams and the sting hole then barely leak (PROJECT_STATUS §2).
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
      (aluminium, brass or carbon fibre). (2026-11-09: stainless screws are fine near it; the 8 × 2 mm magnets pull on
      even a plain steel M3 screw at 60 mm with only about 1 µN, so the brass screw set is dropped; buy list §4.) A
      magnet right next to a steel sting could add a few grams-force, the same size as the drag;
    - holding force: test-section panels see little pressure in a blower with an open exit. A removable 500 mm
      settling-chamber panel would see about 15 N at 10 m/s and 60 N at 20 m/s (estimate), so it needs latches or
      many strong magnets;
    - acrylic 3–5 mm thick, cast rather than extruded (clearer);
    - mark the magnet poles; one flipped magnet repels.
  - **Added 2026-11-08/09 [Proposed], from the buy-list session** ([docs/buy_list.md](docs/buy_list.md)):
    - Fan-to-tunnel joint: a printed inlet sized from the measured fan collar (plus one neoprene layer and about
      0.5 mm), about 25–30 mm deep; test-print a 10 mm ring first. **2026-11-10:** make the inlet a separate ring that
      bolts to the diffuser, so the diffuser can be printed before the fan arrives (the owner will buy the fan last).
    - Screens: aluminium window screen, with two or three in the diffuser. Consider placing the first slightly into
      the diffuser: at the fan outlet it costs about 24–28 Pa at 13 m/s. Use the §3 table for the fan pressure.
    - Honeycomb: printed (owner), for example 6 mm hexagons, 0.4 mm walls, about 50 mm long.
    - Wall-tap stations S (settling chamber), E (test-section entrance, at least 150 mm ahead of the sphere) and M
      (model station), four taps each: 0.8–1.0 mm holes drilled after printing, with printed bosses holding 1/8 in
      brass stubs. Plus a probe guide across the section. **Idea (agent, 2026-11-09; weigh at sizing):** a straight
      probe entering through the open exit, facing upstream, on a printed stand outside the tunnel, needs no bend and
      no wall hole, and comes out easily before force runs. **2026-11-09 (owner asked whether to print the holes):**
      the file gets the stub socket, stopping about 1.5–2 mm short of the inside face, and a pilot dimple at the tap
      position; the sensing hole itself is drilled with the pin vise, then the inside edge is flattened with 400–600
      wet/dry on a flat block (no burr, no rounding). A 0.8–1.0 mm hole is only about two nozzle widths, so a
      printed one comes out undersized, out of round or strung shut. The M taps matter most: their error goes
      straight into q at the model (probe − M), while constant S and E errors are calibrated out. Practise on a
      printed test coupon first.
    - The balance as a removable module that can lay on its side for calibration. The load cell stands upright under
      the ball, clamped only at its top end ([owner's sketch](docs/sketches/README.md)).
    - A sting shield about 7.5 mm wide (5 mm bore), streamlined, fixed to the sphere floor insert (D-014), up to about
      5 mm below the ball; ~~a 5/32 in sleeve at the sting top for the balls' 1/8 in stems~~ **(2026-11-09,
      [D-016](DECISIONS.md), Tentative): no sleeve; each ball, and the calibration hook, gets its own full-length 1/8 in brass sting, all cut
      to the same length within about 0.5 mm. The drawings show this since revision C (2026-11-10).**
    - Panels: 1/8 in acrylic in printed frames with 8 × 2 mm magnet pockets (about 8.2–8.3 mm across, 2.2 mm deep).
    - Bolted flanges, M3 screws into brass heat-set inserts, foam tape, screens clamped between the flanges in printed
      frames (decided 2026-11-09, [D-013](DECISIONS.md)); printed feet under each section, no plywood base (owner).
    - Filament: PLA shells (black for the contraction and test section), PETG-CF for loaded parts.
  - **Added 2026-11-09:** settle the seven findings from the drawing package (PROJECT_STATUS open question 15),
    starting with the settling-chamber spacing and how the 250 mm sections split in cross-section. Then update the
    drawings: the numbers in `docs/drawings/wtdata.py`, `python docs/drawings/page.py`, and `preview.py` to check that
    no label overlaps ([docs/drawings/README.md](docs/drawings/README.md)).
  - **Added 2026-11-15 ([D-017](DECISIONS.md)):** the owner draws the CAD, so the sizing ends in one dimension sheet
    per printed part (flanges, bolt pattern, walls, holes, clearances) and the contraction wall as a points file to
    import as a spline in Fusion 360 (the owner's CAD program, 2026-11-17).
  - **Added 2026-11-19:** a small open, vented holder for the BME280 board, for room air near the fan inlet: slots on
    every side with the sensor chip facing one, screws or a snap-in slot for the board (check whether it has mounting
    holes), a zip-tie point for the cable, about 10 cm from the fan's motor body and out of lamp light or sunlight.
    Not inside the tunnel and not in the Arduino box. The owner measures the board (outline, holes, connector side)
    for its dimension sheet ([session log](docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md)).
  - Outcome: a design note in `docs/experimental_setup.md` with dimensions and the reasoning, a DECISIONS.md entry, and
    the dimension sheets and points file.
  - Verify: Reynolds number, blockage ratio, expected drag and fan duty recomputed for the chosen numbers (see
    [estimates](PROJECT_BACKGROUND.md#order-of-magnitude-estimates)); sphere blockage stays at a few percent or below.
- [ ] **Owner: CAD every printed part from the dimension sheets** (new 2026-11-15, [D-017](DECISIONS.md)). Estimate
  12–25 h (owner's own estimate about 10 h). Draw the flange and screen frame once and reuse them; print test coupons
  (heat-set insert holes, magnet pockets, the sting hole, a 10 mm fan-ring test) before the large parts. Depends on
  the sizing above. Outcome: STEP or STL files in `cad/` (D-004's size rule). Verify: the agent checks each export
  (fits the 256 mm bed, key dimensions match the sizing, bolt holes line up between mating parts), and the coupons
  fit.
- [ ] **Owner: download the remaining electronics datasheets** on the resources "Wanted" list: Bosch BME280, TI
  LM741 / LM348 / LMC6484 / LM317 / LM7805, and the chosen fan's manual. **Done 2026-11-08 by the agent:** SDP8xx,
  TAL221 and Sensirion's signal-compensation note, filed with notes. No longer needed: SDP31/SDP32, Honeywell HSC,
  TAL220 (parts chosen). Outcome: PDFs in `resources/`; an agent files them and writes notes. Verify: each has an index
  row marked "Reviewed".
- [ ] **Owner: check the 2026-11-22 paper notes against the PDFs** (new 2026-11-22). Each notes file ends with a
  checklist, printed and PDF pages given; figure items are blind (read the value yourself):
  [Barlow1999](resources/notes/Barlow1999.md) (13 items), [Morel1975](resources/notes/Morel1975.md) (6),
  [Anthoine2004](resources/notes/Anthoine2004.md) (6), [Bradshaw1964](resources/notes/Bradshaw1964.md) (8). Barlow1999
  is local only (not on GitHub). Outcome: each notes file records "Checked by the owner against the PDF, <date>",
  with any disagreements.
- [ ] **Decide which proposals from the 2026-11-22 reading to adopt** (owner, with the agent; new 2026-11-22). All are
  Proposed, from the notes' "What it suggests" sections; none is decided:
  1. Measure the sting's tare and interference with an image sting (a dummy shield hung from a spare top panel, plus a
     stub on top of the ball), not by running the sting alone (Barlow1999 ch. 7). Needs parts in the sizing and CAD.
  2. Seal the load-cell box, including the cable entry, so no air flows through the gap around the sting (Barlow1999
     ch. 7).
  3. Calibration procedure details: exercise the cell first, load up and down, repeat, small-load check, residual plot,
     same HX711 and wiring as in the tunnel, g = 9.81 m/s² (within about 0.2 % of the true value at latitudes 25–60°;
     the exact local value from Eq. 7.13 if the owner gives a rough latitude), a check weight each session, and a
     zero-shift limit for repeating runs (Barlow1999 ch. 7).
  4. Calibrate S − E with the floor insert and sting shield in place, at every fan setting, and fit any trend with speed
     (Barlow1999 ch. 6; Bradshaw1964 p. 15). Leave the S and E lines connected during force runs.
  5. Chamfer the total-pressure probe's tip and align it within a few degrees (Barlow1999 ch. 4: errors from about 8°).
     Nothing new to buy (2026-11-22): the tube cutter, pin vise, drill bits and 220–600 sandpaper are on hand; needle
     files are optional. Alignment comes from a printed guide in the CAD, then a check: turn the probe slightly each way
     and set it in the middle of the range where the reading stays highest.
  6. Put the E ring at least about 56 mm downstream of the contraction exit and the last screen about 60 mm before the
     contraction (Morel1975).
  7. Give each diffuser screen a short parallel land on both sides of its flange so it meets the walls square
     (Bradshaw1964).
  8. Add a coarse-grid repeat of one sphere run to the validation plan, to show whether free-stream turbulence matters
     (Bradshaw1964). Proposed form (2026-11-22): a piece of 1/4 in galvanized hardware cloth (to buy, a few dollars;
     open area well above 57 %), cut and clamped at a spare settling-chamber joint after the honeycomb like a screen;
     the sizing leaves that joint. Recalibrate S − E with the grid in, run the same ball at the same Re three times with
     and three times without it, alternating, and compare the change in C_D with the run-to-run scatter. Timing (owner,
     2026-11-22): at the end, after the main validation runs; only the spare joint is needed at sizing, and the mesh is
     bought later. Also a diagnostic if C_D falls outside the band.
  9. Measure the empty tunnel's static-pressure gradient along the test section (a static probe or a long static tube)
     for the horizontal-buoyancy correction (Barlow1999 chs. 6, 9–10).
  10. Uncertainty method: block means for correlated samples, randomized or up-and-down speed order, and the C_D
      budget structure in the Barlow1999 ch. 12 notes.

  Outcome: each item accepted, changed or rejected; accepted ones move into the sizing task, the calibration and
  validation tasks, or a DECISIONS entry. Verify: no item above is left undecided.
- [ ] **Choose the screens and honeycomb** (new 2026-11-02). **Mostly done 2026-11-09** ([buy list](docs/buy_list.md)
  §3): aluminium window insect screen ("bright aluminum", 18 × 16 mesh, 66–69 % open, about $10 a roll), two or three
  in the diffuser and two in the settling chamber; a **printed honeycomb** (owner), with straws as the upgrade.
  **2026-11-09: screen ordered** (Saint-Gobain ADFORS FCS9222-M, Bright; maker's spec 18 × 16, 0.011 in wire, 66 %
  open). With 0.011 in wire two diffuser screens just meet K_sum 2.1 (2.15), so three are planned for margin.
  Remaining: on arrival, count its wires per inch and check one wire (about 0.28 mm; 0.36 mm or more would drop it
  below 58 % open), then confirm three diffuser screens at sizing.
  - Screens: metal square-mesh, at least 58 % open; for example 20–30 wires/in with 0.19–0.23 mm wire (Scheiman1981
    Table 1). Two go in the diffuser and one or two in the settling chamber (2026-11-09: three in the diffuser and
    two in the chamber, above).
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
  - **2026-11-22 (Barlow1999 ch. 10, [notes](resources/notes/Barlow1999.md)):** wake blockage (5/4)(S/C)C_Du (Maskell,
    Eq. 10.9) plus solid blockage K(V/C^{3/2}), with Thom's K = 0.96 for bodies of revolution or about 1.5τ₁ for a
    sphere's effective volume; no chart covers a sphere. Total +3.9 to +4.0 % in q for the 3/4 in ball and +7.4 to
    +7.8 % for the 1 in ball (our arithmetic). The test section (100 mm) and balls are chosen, so the method can now be
    proposed for decision; subtract horizontal buoyancy separately once the pressure gradient is measured.
  - Outcome: method and formula marked as chosen (D-entry).
  - Verify: the correction for the chosen sphere and test section is computed and stated with its uncertainty
    (θ spread 1.85–2.8). The plan includes a two-sphere-size check (P2 validation run).
- [ ] **Confirm the microcontroller / DAQ.** Candidate (2026-11-01): the owner's Elegoo Mega 2560 (5 V logic,
  I²C on pins 20/21). Weakly2024 used an Uno with one HX711 per load cell; the Mega does everything the Uno does,
  with more pins. The board works: a modified Blink uploaded on 2026-11-02 (PROJECT_STATUS §3). The wiring is drawn (2026-11-17, sheet 12,
  [D-018](DECISIONS.md)). Outcome: board recorded as chosen (D-entry). Verify: it reads the
  HX711 and the chosen pressure sensor at the planned sample rate (interface and logic voltage checked), and logs raw
  counts to a PC as CSV.

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
  - **Lighting (owner, 2026-11-09; to be designed at the end, with the mist):** a light outside the test section,
    shining down through the clear top panel onto the model against the dark (black PLA) far wall and floor. The owner's
    reference was a photo of a display case lit by an LED strip along its top front edge. The light is only for mist,
    so it is off during force and pressure runs (the load cell's zero moves about 0.01 g/°C, and the drag signal is
    tens of µV). It needs no second clear side panel. The agent's first idea, a backlight behind the far side window,
    suits silhouettes, not mist: it shines toward the camera and washes the streaks out.
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
- [ ] **Owner (recommended): learn the circuit basics before wiring** (new 2026-11-17; the owner is new to
  electronics). Read [docs/electronics_walkthrough.md](docs/electronics_walkthrough.md) §2–5 and the "before wiring"
  tutorials in its §9 (about 3–5 h, estimate), then each step's tutorials just before that step. Outcome: the owner can
  answer the six questions in its §8. Verify: the owner explains them in their own words before the breadboard, or asks
  about the ones that are unclear.
- [ ] **Design and build the sensor interface board** (owner's plan, 2026-11-01: design the circuit, possibly test it
  on a breadboard, then turn it into a PCB). **Owner, 2026-11-09:** when the parts arrive, build it on the breadboard,
  test it, then order the PCB; no soldered prototyping shield in between.
  - **2026-11-17: the circuit is drawn** (agent, at the owner's request): drawing package sheets 11 and 12
    ([D-018](DECISIONS.md), Tentative), explained in [docs/electronics_walkthrough.md](docs/electronics_walkthrough.md).
    The sensors stay on cables in their own places; the shield carries only three 4-pin connectors (J1–J3), C2 and empty
    pads for pull-ups R1 and R2, because the BME280 board already has pull-ups. This supersedes the socket list below.
    **2026-11-18: the breadboard is started.** The Mega, power rails, C2 and signal rows are wired and the power passed
    ([as built](docs/experimental_setup.md#breadboard-as-built)); no sensor is connected. **2026-11-23: the breadboard is complete and every sensor reads**
    ([as built](docs/experimental_setup.md#breadboard-as-built)). Next:
    1. ~~the breadboard, one sensor at a time~~ (done 2026-11-23); the combined logging test (walk-through step 4,
       P0) remains;
    2. the owner chooses the PCB program, **KiCad (recommended) or EasyEDA**, and draws sheet 12 in it; the agent
       checks the exported net list against sheet 12;
    3. the shield PCB and the J1–J3 connector type (locking Grove/JST-style plugs likely; owner, 2026-11-17: order
       them when needed); optionally a small carrier board for the SDP810 in the same order.
  - Proposed contents (2026-11-01/09; partly superseded on 2026-11-17, above): a shield for the Mega 2560 holding:
    - **female header sockets** for the HX711 module and the BME280, and a connector for the SDP810's cable (its pins
      are at 2 mm pitch), so modules plug in and can be swapped (owner's socket idea, 2026-11-09); DIP sockets for any
      chips;
    - I²C pull-ups and decoupling capacitors;
    - optionally a PWM output and speed-sense input for a fan with a low-voltage control input.

    No display or encoder headers (D-012, 2026-11-08). The servo-power and angle-dial inputs proposed earlier are no
    longer needed now that the owner has chosen preset angles (2026-11-01).

    Route I²C to the SDA/SCL pins next to AREF so the board also fits an Uno (if the Mega is an R3). PCB program: the
    owner's choice (2026-11-17; PROJECT_STATUS open question 18).
  - A breadboard is fine for testing the digital wiring. **Solder the load-cell leads directly to the HX711**, with no
    breadboard in the bridge wiring (Weakly2024 lesson).
  - Outcome: schematic and PCB files in the repo (folder to be chosen when the first file exists), and an assembled
    board.
  - Verify: an I²C scan finds the pressure sensor and the BME280 through the board, and the HX711 gives a stable
    zero with the wind off.
- [ ] **Update sheet 12 with the delivered HX711 pad names** (new 2026-11-18; waits for the owner's go-ahead): RED, BLK,
  WHT, GRN and YLW instead of E+, E−, A−, A+; check whether the walk-through's snapshot needs replacing. Verify: `python
  docs/drawings/page.py` rebuilds and `preview.py` shows no overlaps.
- [ ] **Data-logging firmware** (replaces the 2026-11-01 "firmware with an on-tunnel display and knob menu", dropped by
  [D-012](DECISIONS.md) on 2026-11-08: all output goes to the laptop).
  - **First, bring-up sketches** (agent, proposed 2026-11-17): an I²C scanner, then one commented sketch per sensor,
    matching walk-through §6 steps 1–3, so each part is tested alone. Pins: SDA 20, SCL 21, HX711 DAT 2 and CLK 3
    (D-018). Outcome: sketches in `firmware/`. Verify: the owner's bench results for each step, recorded in
    docs/experimental_setup.md. **Done 2026-11-23:** `i2c_scan`, `hx711_raw_counts`, `sdp810_read`, `bme280_read`
    ([firmware/README.md](firmware/README.md), [D-019](DECISIONS.md)), all passing on the bench. Lessons for the logger:
    flag BME280 resets (check its mode bits) and failed reads in a column, and stop the SDP810 before starting it.
  - Read the HX711 (raw counts), the SDP810 (DP temperature compensation with "average till read", command 0x3615;
    240 counts/Pa; [SDP8xx notes](resources/notes/SDP8xx.md)) and the BME280; send CSV lines with a timestamp and a
    run flag over USB.
  - Log raw values only. Calibration, the ×966 mbar / p_amb correction and C_D belong in the analysis scripts
    (CLAUDE.md conventions).
  - Live view: the Arduino IDE's Serial Plotter first; a laptop script later if needed.
  - Outcome: firmware in the repo (folder `firmware/`, documented in [firmware/README.md](firmware/README.md)).
    Verify: each sensor's reading follows a change the owner causes (a known mass on the load cell, blowing on a
    pressure port, a finger on the BME280), and the logged sample rate is steady over 10 minutes.
- [ ] **Arrival checks for each new part** (owner; new 2026-11-08). **Every part arrived by 2026-11-17. Done so far (2026-11-17/18): the
  SDP810's label and the BME280 cable's resistances; the HX711 board's labels are read. **Done 2026-11-23**
  ([as built](docs/experimental_setup.md#breadboard-as-built)): the soldered TAL221's resistances at its free wire ends ("about" 1090 and 1000 Ω, exact values
  not given; cross pairs and body not measured); the BME280's 4.81 V on SDA and SCL and chip ID 0x60; the SDP810's zero
  (−0.022 Pa with the ports looped); the HX711's rate (10 SPS, from timing). Still open below: the spare TAL221, a
  longer no-load zero on a firm mount, the HX711's excitation voltage, the Mega's own pull-ups, the calipers, the screen
  and the 2026-11-10 items. Everything below not marked done
  is still open.** Record each result with the date:
  - TAL221s: wire resistances (red–black about 1090 Ω, green–white about 1000 Ω, cross pairs, body open) and the
    no-load zero, as baselines for spotting damage later. Measure the resistances at the free wire ends **before**
    soldering to the HX711; afterwards the board's own parts are in the circuit and change the reading (2026-11-22);
  - BME280 (Waveshare, ordered 2026-11-09): first, with only VCC (5 V) and GND connected, SDA and SCL read about 5 V
    on the multimeter (level translator working; about 3.3 V means no shifting, so do not wire it to the Mega); then
    chip ID 0x60, not a BMP280's 0x58 (Waveshare's schematic predicts 5 V: SDA and SCL are pulled up to VCC through
    4.7 kΩ);
  - SDP810: zero with both ports capped, within about 0.1 Pa;
  - calipers: new battery, return to 0.00, a known object measured;
  - window screen (ordered 2026-11-09): 18 and 16 wires per inch against the steel rule, one wire about 0.28 mm
    (0.011 in), "Bright" bare aluminium; store it flat or loosely rolled, since creases do not come out;
  - added 2026-11-10: barbed connectors, at least 10 tees and 2 straight couplers; brass rod, a true 1/8 in (3.18 mm),
    not 3 mm, and straight when rolled on a table; brass tube, 1/8 in OD (the 1/8 in silicone tubing should seal on
    it); acrylic, 1/8 in and acrylic rather than styrene; neoprene, 1/16 in and soft; the SDP810's label reads
    125 Pa; the drill set has 0.8–1.0 mm and 3.0 mm bits.

  - added 2026-11-17, updated 2026-11-18: the HX711's RATE jumper, and its excitation voltage (RED to BLK pads, powered)
    once wired; the Mega's pin-20-to-5V resistance, unpowered and with R1 out (about 10 kΩ if it has its own pull-ups).
    Answered from photos: the HX711 pad labels, the BME280's cable, the Mega's R3 layout.

  Details: [docs/buy_list.md](docs/buy_list.md) §5, §6, §7 and §10. Verify: values written into
  docs/experimental_setup.md.
- [ ] **Calibrate the pressure sensor against a home-made inclined water manometer** (new 2026-11-08). A water U-tube
  lying on a ramp at about 1 in 10 (100 Pa moves the menisci about 102 mm apart), teed onto the same taps as the
  SDP810 with the tunnel running at 80–100 Pa. It corrects the sensor's 3 % gain error, with the real tubing in place
  ([docs/buy_list.md](docs/buy_list.md) §9). Outcome: a calibration dataset and a gain factor with uncertainty. Verify:
  readings at several pressures agree after correction within the manometer's estimated ±1 %.
- [ ] **Build the load cell and its conditioning circuit.** Solder the load-cell leads directly to the HX711, with no
  breadboard in the bridge wiring (lesson from Weakly2024). Verify: stable zero over several minutes with wind off;
  noise recorded. **2026-11-23:** one TAL221 soldered straight to the HX711's pads (owner); 1.4 s of zero gave a
  standard deviation of 26 counts (about 0.002 g, estimate) on a taped mount. The several-minute zero waits for a firm
  mount (the balance module, or a clamp).
- [ ] **Calibrate the load cell against known weights.** Method proposed 2026-11-08 ([buy list](docs/buy_list.md)
  §9): lay the balance module on its side so gravity acts in the drag direction (no pulley friction), and hang masses
  at the ball's position from a budget 10 mg–100 g set (in a light pan hung from a printed attachment on the sting's
  end, with a hook at the ball's centre; owner's idea, 2026-11-09). Weigh every piece once on the school lab balance first, and
  record those masses as raw data. Set the slope with the 2–20 g pieces; check 0.2–3 g, where the drag is.
  **2026-11-19: the masses are weighed** ([EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing)): the set bought is 50, 2 × 20, 6 × 10, 2 × 5 and 3 × 2 g
  plus a 10 g hanging rod, each now known to about ±0.01 g; use these measured masses, not the stamped ones (up to
  2.5 % off). It has nothing under 2 g; the drag range lies between the wind-off zero and the 2 g pieces, so no smaller
  masses are needed (solder cut by length if a low-end check is ever wanted; buy list §9). Keep masses plus preload
  under 100 g: the whole set is 165.5 g, 175.3 g with the rod. The hanging rod (9.80 g) may replace the pan.
  Outcome: calibration dataset and fit (counts → N). Verify:
  residuals and linearity reported; calibration file referenced from the data catalog.
- [ ] **Check the fan's heating of the tunnel air with the BME280** (new 2026-11-19; after the fan arrives). Run the fan
  at top speed for a few minutes, hold the BME280 on its cable in the jet a hand's width past the open exit, and compare
  its temperature with the room reading at the fan inlet. Expected under about 0.4 °C (estimate). Outcome: the
  difference recorded as a correction or an uncertainty. Verify: both readings and the difference written into
  docs/experimental_setup.md; if it exceeds about 1 °C, revisit where the BME280 sits.
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
  5. vortex-shedding tone of a 1/8 in rod (about 410–820 Hz at 6.5–13 m/s), recorded by phone or laptop;
  6. **added 2026-11-10 (owner asked about buying plastic cylinders from McMaster):** cylinder drag on the balance, a
     rod standing from a floor insert to just under the lid. At 13 m/s, with C_D 1.0–1.2 assumed (textbook, agent's
     memory, not checked): the 1/8 in brass rod already ordered about 3.2–3.9 gf at 3.2 % blockage; a 1/4 in Delrin rod
     about 6.4–7.7 gf at 6.3 %; 3/8 in blocks 9.5 %, too much. The 3/4 in ball gives about 1.3 gf. Needs its own
     holder, a floor-insert hole and a gap under the lid, and a cylinder-drag source reviewed in `resources/`; end gaps
     and 2-D blockage make it a weaker reference than the sphere. Agent's advice: do not buy now; a 1/4 in acetal rod
     costs about $1.80–2.60 a foot (Aircraft Spruce, Zoro, 2026-11-10; McMaster's price not seen). **Owner to say
     whether sizing should leave room for it** (no cost now).

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
  (5.07 %), ±0.001 in, two of each; press-fit on brass stems, drilled with a printed jig (2026-11-09/10: a pack of 10 of each ordered;
  each ball on its own full-length sting, D-016). The Re-matched pair: the
  3/4 in ball at 13 m/s against the 1 in ball at 9.75 m/s ([buy list](docs/buy_list.md) §6).
- [x] 2026-11-08: **Pressure sensor chosen:** one Sensirion SDP810-125Pa (owner chose one over two). Datasheet
  reviewed: 0.08 Pa + 3 % of reading, I²C 0x25, solder pins at 2 mm pitch. Ambient-pressure correction ×966 mbar /
  p_amb required ([SDP8xx notes](resources/notes/SDP8xx.md), [Sensirion2024 notes](resources/notes/Sensirion2024.md)).
  Probe made in-house: brass total-pressure tube and wall taps ([buy list](docs/buy_list.md) §5).
- [x] 2026-11-08: **Load-cell capacity chosen:** TAL221 100 g, two of them, with a SparkFun HX711. Datasheet reviewed
  ([TAL221 notes](resources/notes/TAL221.md)).
- [x] 2026-11-08: **Ambient sensor chosen:** Adafruit BME280 (2652), with level shifting for 5 V
  ([buy list](docs/buy_list.md) §7). Replaced on 2026-11-09 by the Waveshare BME280, which the owner ordered (below).
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
- [x] 2026-11-09: Owner committed and pushed the fan-advice and screen-order session as `c768e2c`; `/catchup` confirmed
  `UP_TO_DATE` ([session log](docs/sessions/2026-11-10-parts-ordering.md)).
- [x] 2026-11-09/10: **Parts ordered: everything on the buy list except the fan** (owner), which is bought last so its
  return window covers the real test. Changes on the way: Waveshare BME280 instead of the Adafruit; stainless screws
  instead of a brass set; one full-length sting per ball instead of the 5/32 in sleeve ([D-016](DECISIONS.md),
  Tentative); the 4-core cable optional; header strips tin-plated. Tracker: [docs/shopping_list.md](docs/shopping_list.md)
  ([session log](docs/sessions/2026-11-10-parts-ordering.md)).
- [x] 2026-11-10: Owner committed and pushed the parts-ordering session as `f4fa904` (`UP_TO_DATE`); the README was
  then updated to the current state ([session log](docs/sessions/2026-11-10-parts-ordering.md)).
- [x] 2026-11-10: Owner committed and pushed the README follow-up as `f5616a3`; `/catchup` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-10-order-details-and-cylinders.md)).
- [x] 2026-11-10: **Two sizing inputs recorded** (owner): the acrylic is four 8 × 12 in sheets, and the SDP810 order is
  Mouser 403-SDP810-125PA (maker's part SDP810-125PA), the ±125 Pa part. The BME280 is now named as the Waveshare in
  every live doc and the drawings' parts list ([session log](docs/sessions/2026-11-10-order-details-and-cylinders.md)).
- [x] 2026-11-10: Owner committed and pushed the order-details session as `2ac0809`; `/catchup` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-10-consistency-audit.md)).
- [x] 2026-11-10: **Consistency audit of every folder** (owner's request): the live docs and the drawings brought up to
  the latest decisions: the replaceable sphere floor insert with the sting shield attached (D-014), one sting per ball
  with no sleeve or separate stems (D-016), stainless screws at the balance, and the order statuses. Drawings revised
  to C. Documentation only ([session log](docs/sessions/2026-11-10-consistency-audit.md)).
- [x] 2026-11-11: Owner committed and pushed the consistency audit as `5cb8b7a`; `/catchup` confirmed `UP_TO_DATE` on
  2026-11-15 ([session log](docs/sessions/2026-11-17-time-estimates-and-cad.md)).
- [x] 2026-11-15: **Who does the CAD decided** (owner): the owner draws every part; the agent supplies dimension sheets,
  the contraction points file and STL checks ([D-017](DECISIONS.md)). Time estimates for the CAD and the whole project
  recorded ([session log](docs/sessions/2026-11-17-time-estimates-and-cad.md)).
- [x] 2026-11-17: Owner committed and pushed the time-estimates session as `ce69a57`; `/catchup` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-17-sensor-circuit-design.md)).
- [x] 2026-11-17: **Every part ordered on 2026-11-09/10 arrived** (owner); the fan is still to buy (P0). Shopping list
  marked "Got it"; arrival checks still to do (P2). Was P1 "Owner: buy hardware".
- [x] 2026-11-17: **CAD program recorded:** Fusion 360 (owner; note on [D-017](DECISIONS.md)).
- [x] 2026-11-17: **Sensor circuit drawn and explained** (agent, at the owner's request; documentation only): drawing
  package revision D, sheets 11 (block diagram) and 12 (schematic, parts and net lists); [D-018](DECISIONS.md)
  (Tentative), which also answers P1 "Decide the role of the op-amp circuit" (none); the Waveshare BME280 schematic
  filed with notes; [docs/electronics_walkthrough.md](docs/electronics_walkthrough.md) for a beginner
  ([session log](docs/sessions/2026-11-17-sensor-circuit-design.md)).
- [x] 2026-11-17: Owner committed and pushed the sensor-circuit session as `8904785`; `/catchup` confirmed `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-18-breadboard-power-and-part-checks.md)).
- [x] 2026-11-18: **Breadboard power wiring checked** (owner): continuity passed and the rails and C2 read 4.962 V; no
  sensor connected ([as built](docs/experimental_setup.md#breadboard-as-built)).
- [x] 2026-11-18: **Delivered electronics read from photos and the walk-through corrected:** HX711 pad names, the SDP810's
  pin view, the BME280 cable and first checks ([session log](docs/sessions/2026-11-18-breadboard-power-and-part-checks.md)).
- [x] 2026-11-18: Owner committed and pushed the breadboard session as `ff2ac6e` and moved the original photos out of
  the repo; `/catchup` confirmed `UP_TO_DATE` on 2026-11-19 ([session log](docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md)).
- [x] 2026-11-19: **Calibration weights weighed** (owner, at school): each piece three times on a CGOLDENWALL HZ50002B
  (d = 0.01 g), re-zeroed before every reading; −2.5 % to +1.1 % off nominal ([EXP-001](docs/data_catalog.md#exp-001-calibration-mass-weighing); weighing form in
  [docs/forms/](docs/forms/calibration-mass-weighing.xlsx)). Answers PROJECT_STATUS open question 16.
- [x] 2026-11-19: Owner committed and pushed the weighing session as `fd20afe`; `sync_status.py` confirmed
  `UP_TO_DATE` on 2026-11-22 ([session log](docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md)).
- [x] 2026-11-19: **SDP810 cable fitted** (owner): the ready-made PH 2.0 cable is a stiff fit and is pushed on; not
  powered. The before-power checks and the colour-to-pin map stay open (P2, SDP810 connection item).
- [x] 2026-11-22: **Remaining papers reviewed** (agent, at the owner's request): Barlow1999 chapters 4, 6, 7, 9, 10 and
  §§12.1–12.3; Morel1975; Anthoine2004; Bradshaw1964. Notes with owner checklists:
  [Barlow1999](resources/notes/Barlow1999.md), [Morel1975](resources/notes/Morel1975.md),
  [Anthoine2004](resources/notes/Anthoine2004.md), [Bradshaw1964](resources/notes/Bradshaw1964.md); index rows marked
  Reviewed ([session log](docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md), the 2026-11-19 session
  continued).
- [x] 2026-11-23: The SDP810's connection chosen and proven: the ready-made PH 2.0 cable (pushed on 2026-11-19), its
  wires spliced to jumpers and wired by pin number from the moulded "1"; the I²C scan found 0x25 and the sensor zeroes
  and reads the right sign ([session log](docs/sessions/2026-11-23-sensor-bring-up.md)).
- [x] 2026-11-23: BME280 step 1 and the whole breadboard bring-up (owner at the bench; agent's sketches): rails 4.947 V,
  SDA/SCL 4.81 V, scan 0x25 + 0x77 with chip ID 0x60; HX711 at 10 SPS with a penny step of about 33,300 counts; SDP810
  scale 240, zero −0.022 Pa, correct sign; BME280 99.6 kPa, 23.3 °C, 44.5 %, responding to breath and touch, one reset
  under handling detected and recovered ([as built](docs/experimental_setup.md#breadboard-as-built); [session log](docs/sessions/2026-11-23-sensor-bring-up.md)).
- [x] 2026-11-23: Bring-up sketches written (agent): `firmware/i2c_scan`, `hx711_raw_counts`, `sdp810_read`,
  `bme280_read`, with [firmware/README.md](firmware/README.md) and [D-019](DECISIONS.md) (Tentative)
  ([session log](docs/sessions/2026-11-23-sensor-bring-up.md)).
