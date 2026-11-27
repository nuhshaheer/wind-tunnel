# TODO

Actionable tasks by priority. Keep this consistent with [PROJECT_STATUS.md](PROJECT_STATUS.md): when a task is done,
move it to **Done** with the date and a link to the session log. Each task states its expected outcome and how to verify it.

Priority: **P0** = do next, **P1** = needed before building, **P2** = build and validation, **P3** = after validation.
Owner tasks are physical or account actions that an agent cannot do.

## P0: Now

- [ ] **Owner: CAD from the sizing sheets, test coupons first** ([D-017](DECISIONS.md); sheets of 2026-11-26).
  - First draw and print coupons C1–C5 ([cad/sizing/coupons.md](cad/sizing/coupons.md)) with the real print settings,
    and report the sizes that work. C1 needs the T18 insert tip (to buy).
  - Then the parts, in the order of [cad/sizing/README.md](cad/sizing/README.md): the contraction (inlet ring and
    one-piece part), the test section (front body, extension, top panel, image panel, floor inserts), the settling
    chamber, the diffuser, the balance (box, door, module, mount, shield), the supports. The fan's inlet ring waits on
    the S6's collar (coupon C7).
  - **In progress (started 2026-11-26,
    [log](docs/sessions/2026-11-26-pdfs-decisions-register-and-cad-start.md)).** The owner is drawing the parts
    first and will print the coupons before any big part. **Exported as 3MF to `cad/main cad files/` and checked by the
    agent (2026-11-26, [log](docs/sessions/2026-11-26-first-cad-exports-checked.md)):**
    - the honeycomb (249.4 outside, 247 inside the rim, 50 tall, 6 mm cells, 0.4 walls);
    - settling chamber C1, whole (one body, chamfer under the insert flange, corner blocks at x = 17–25);
    - the diffuser, whole: 189 overall, the 175 curve plus its end flanges (owner kept it);
    - the fan inlet ring: a straight Ø156.1 socket 27 deep (owner kept it), on the 6 in collar placeholder.

    Drawn, not exported: screen 12a's frame. Next:
    - chambers C2 and C3 (flanges as on C1, chamfer under the insert flange, no corner blocks);
    - the diffuser cut at the middle of its curve: 87.5 from the curve's start, 95.5 from the round flange's face.
      Flanges go around the wall there with no straight length added; D2's insert flange gets the chamfer, D1's screw
      flange doesn't. Then D2 into four corner pieces;
    - the chambers into corner pieces with pin holes;
    - the 50 mm corner spacers and screen frames 12b–12e, after the spacer choice below.
  - **Owner, before drawing the spacers and 12d's frame:** choose what the spacers push on. Proposed: four small corner
    tabs on the upstream layer of 12d's frame, spacers 50 long
    ([settling_chamber.md](cad/sizing/settling_chamber.md#found-while-preparing-the-cad-2026-11-26)).
  - **Owner, each part:** export it as 3MF to `cad/main cad files/` for the agent to check. Check chamfers are Chamfer,
    not Fillet, and that each part is one body.
  - **Owner, before drawing C3:** choose the mist port's place
    ([options](cad/sizing/settling_chamber.md#found-while-preparing-the-cad-2026-11-26); it lands on a glued seam).
  - **Owner, also:**
    - say whether the S6 is being bought now ("im buying the s6", 2026-11-26) or last, as D-025 says;
    - once it arrives, measure its collar and update `collar_d`, so the ring's socket follows.
  - Estimate 12–25 h (owner's own estimate about 10 h).
  - Outcome: STEP or STL exports in `cad/` (D-004's size rule). Verify: the agent checks each export (fits the 256 mm
    bed, key dimensions match the sheets, bolt holes line up between mating parts), and the coupons fit.
- [ ] **Owner: buy the build tools** (2026-11-26; [shopping list](docs/shopping_list.md), "Tools for the build"): a
  T18 heat-set insert tip set with an M3 size, the AstroAI 6000-count multimeter, flush cutters, a heat gun (optional
  for the tunnel). Outcome: each marked "Got it". Verify: the insert tip used on coupon C1.
- [ ] **Owner: close the 2026-11-23 bring-up** (new 2026-11-23; [session log](docs/sessions/2026-11-23-sensor-bring-up.md) §10).
  **Answered 2026-11-26:** the penny was 2.5 g (2.43 g at the EXP-002 sensitivity); the old C1 was marked 1 µF and is
  replaced by the 0.1 µF film; R1 and R2 are removed. Still to send the agent:
  - the HX711's excitation voltage: USB in, DC volts, red probe on the RED pad, black on BLK (walk-through step 3 item 5);
  - the Adafruit BME280 Library version (Library Manager);
  - which wire was moving when the BME280 reset at about 63 s, if remembered;
  - that the two +5 V wires that fed R1 and R2 are out (implied on 2026-11-26, not stated).

  And at the bench: mark the SDP810's High barb (asked 2026-11-26; not confirmed); firm up the BME280's connection (a
  6-pin male header strip pressed into the breadboard, and the hanging jumper bundle taped down). Outcome: each value
  recorded in [docs/experimental_setup.md](docs/experimental_setup.md#breadboard-as-built). Verify: the 2026-11-23 log's
  §10 items closed.
- [ ] **Agent, with the owner at the bench: the combined logging sketch** (walk-through step 4; new 2026-11-23). One CSV
  line per sample with time, HX711 counts, SDP810 dp (raw and × 96600 / p_amb), BME280 p, T and RH, and a flag column
  for BME280 resets and failed reads, following [D-019](DECISIONS.md). Details in P2 "Data-logging firmware". Since
  2026-11-26 the output can be recorded with `scripts/serial_capture.ps1` ([D-021](DECISIONS.md)). Outcome:
  `firmware/logger/` (name to confirm). Verify: a 10-minute run with a steady sample rate and every value responding to
  a change the owner causes, recorded in docs/experimental_setup.md.
- [ ] **Owner: report what is on hand and send the part details the sizing needs** (new 2026-11-10; every ordered part
  arrived by 2026-11-17, see Done). Send the agent:
  - ~~the heat-set inserts' length and outside diameter~~ **answered 2026-11-26: Kadrick M3 × 5, Ø4.5 top, Ø3.9
    bottom** (seller's table; one caliper check is still worthwhile); the hole is settled on coupon C1;
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
- [ ] **Owner: say whether to republish the drawings' private claude.ai copy** (added 2026-11-10). It still shows
  revision B (with the 5/32 in sleeve); the repo copy is revision F (sized, 2026-11-26)
  ([docs/drawings/README.md](docs/drawings/README.md)). Agents republish only on the owner's go-ahead. Outcome: the
  published copy matches `docs/drawings/wind-tunnel-drawings.html`, or a note that only the repo copy is kept. Verify:
  the drawings README no longer says the published copy shows revision B.

## P1: Design and choose hardware (build step 1)

- [ ] **Owner (recommended, optional): read the two key references.** The owner has not read the references yet
  (2026-11-01).
  - Read in full: [Mehta1979](resources/notes/Mehta1979.md) (rules for every
    part of a small blower tunnel) and
    [Weakly2024](resources/notes/Weakly2024.md) (a student balance with an
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
  Proposed, from the notes' "What it suggests" sections. **2026-11-26:** #1 (image sting, D-029) and #2
  (sealed box, D-028) adopted; #6 built into D-024 (E at 56) and D-027 (last screen 100 before the contraction); #7
  (screen lands) and #8 (coarse grid clamped at the 12e joint on test days, no extra joint) are Proposed in the sizing
  sheets; #5's chamfered, aligned probe tip is in the supports sheet. **Still to decide: #3, #4, #9 and #10**
  (procedures; no CAD impact):
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
- [ ] **Confirm the microcontroller / DAQ.** **The board is decided:** the Mega 2560 is part of
  [D-018](DECISIONS.md) (Accepted 2026-11-26), so that entry is the D-entry this task asked for. **Mostly met (2026-11-26 catch-up):** all three sensors read on the Mega
  (2026-11-23) and HX711 counts were logged to CSV (EXP-002); only the combined logging at the planned rate is left, which
  is the P0 logging-sketch task. Candidate (2026-11-01): the owner's Elegoo Mega 2560 (5 V logic,
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
    ([D-018](DECISIONS.md), Tentative then; Accepted 2026-11-26), explained in [docs/electronics_walkthrough.md](docs/electronics_walkthrough.md).
    The sensors stay on cables in their own places; the shield carries only three 4-pin connectors (J1–J3), C2 and empty
    pads for pull-ups R1 and R2, because the BME280 board already has pull-ups. This supersedes the socket list below.
    **2026-11-18: the breadboard is started.** The Mega, power rails, C2 and signal rows are wired and the power passed
    ([as built](docs/experimental_setup.md#breadboard-as-built)); no sensor is connected. **2026-11-23: the breadboard is complete and every sensor reads**
    ([as built](docs/experimental_setup.md#breadboard-as-built)). Next:
    1. ~~the breadboard, one sensor at a time~~ (done 2026-11-23); the combined logging test (walk-through step 4,
       P0) remains;
    2. ~~the owner chooses the PCB program and draws sheet 12 in it~~ **done 2026-11-23: KiCad 10**, the shield drawn
       by the owner and checked by the agent ([D-020](DECISIONS.md), [session log](docs/sessions/2026-11-23-sensor-shield-pcb.md));
    3. ~~the shield PCB and the J1–J3 connector type~~ **designed 2026-11-23:** 2.54 mm pin headers for jumper wires,
       each in its part's pin order; Gerbers in `PCB/arduino_shield/gerbers/`. ~~The capacitor measurements and the
       order~~ **ordered 2026-11-26** (JLCPCB Y6-12005915A, 5 boards, OSP finish; arrival about 6–8 December,
       estimate). The breadboard already matches the shield and passes (2026-11-26). **Next, when the boards arrive:**
       keep them sealed until soldering (OSP), hold them by the edges; solder the headers (the 40 strips on hand should
       supply the 99 pins; count the male ones), C1 (the 0.1 µF film, legs bent to 5 mm) and C2 (+ leg to +5V); leave
       R1 and R2 empty; with plain male pins, check the shield clears the Mega's USB socket and tape the socket's top if
       it touches; then run the checks below. The optional SDP810 carrier board was not drawn.
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
  - Outcome: schematic and PCB files in the repo (`PCB/arduino_shield/`, since 2026-11-23), and an assembled
    board.
  - Verify: an I²C scan finds the pressure sensor and the BME280 through the board, and the HX711 gives a stable
    zero with the wind off.
- [ ] **Replace the walk-through's sheet 12 snapshot** (`docs/images/2026-11-17_sheet12-schematic-revD.png`) with
  revision E (new 2026-11-23). Sheet 12 now shows the delivered HX711 pad names and the shield's pin orders, but Edge's
  headless screenshots stopped working during the 2026-11-23 wrap, so no new snapshot was made. Verify: `python
  docs/drawings/preview.py 12` writes a PNG that shows "J1 … SCL" at pin 1, and the walk-through links it.
- [ ] **Agent: bring the drawing package to the owner's CAD (revision G)** (new 2026-11-26). Revision F puts the
  diffuser's flanges inside its 175 mm (the CAD has them outside: 189 overall), the socket 28 deep (CAD 27), and the TBD
  register's collar row at 150/153.7 (now 152.4/156.1). Do it once more parts are drawn
  ([drawings README](docs/drawings/README.md)). Verify: `python docs/drawings/page.py` rebuilds with
  `parts never drawn: []`, the changed sheets previewed, and the README's "Known differences" list cleared.
- [ ] **Optional, agent: keep the 3MF export checker in the repo** (new 2026-11-26). This session's section-cutting
  scripts (a standard-library 3MF reader, a plane-section and ray tool) were scratch work. A kept script in `cad/`
  would make each export check rerunnable. Outcome: a script with its command in `cad/sizing/README.md`. Verify: it
  reproduces this session's numbers on the four exports.
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
  - Live view: the Arduino IDE's Serial Plotter first; a laptop script later if needed. Recording to a file:
    `scripts/serial_capture.ps1` ([D-021](DECISIONS.md), 2026-11-26; the IDE must be closed while it runs).
  - Outcome: firmware in the repo (folder `firmware/`, documented in [firmware/README.md](firmware/README.md)).
    Verify: each sensor's reading follows a change the owner causes (a known mass on the load cell, blowing on a
    pressure port, a finger on the BME280), and the logged sample rate is steady over 10 minutes.
- [ ] **Arrival checks for each new part** (owner; new 2026-11-08). **Every part arrived by 2026-11-17. Done so far (2026-11-17/18): the
  SDP810's label and the BME280 cable's resistances; the HX711 board's labels are read. **Done 2026-11-23**
  ([as built](docs/experimental_setup.md#breadboard-as-built)): the soldered TAL221's resistances at its free wire ends ("about" 1090 and 1000 Ω, exact values
  not given; cross pairs and body not measured); the BME280's 4.81 V on SDA and SCL and chip ID 0x60; the SDP810's zero
  (−0.022 Pa with the ports looped); the HX711's rate (10 SPS, from timing). **Done 2026-11-26:** a several-minute
  no-load zero on a firm mount (the printed bench scale, [EXP-002](docs/data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale));
  the calipers work (used for the capacitor leads). Still open below: the spare TAL221, the HX711's excitation voltage,
  the Mega's own pull-ups, the screen and the 2026-11-10 items. Everything below not marked done
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
  mount (the balance module, or a clamp). **2026-11-24:** a printable bench scale for the TAL221 is filed in
  `cad/third-party/tal221-scale-bwilless/`. **2026-11-26: done on the bench scale**
  ([EXP-002](docs/data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale)): reading noise sd 40 counts
  (0.003 g), 10 s means sd 0.0045 g after 3 min, about 5× the taped cell's scatter on 2026-11-23 (cause not tested).
  Remains: the same checks on the balance module once built.
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
  **2026-11-26, bench practice ([EXP-002](docs/data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale),
  Preliminary):** on the printed scale the cell gives 13,727.5 counts/g, straight within 0.025 g from 2 to 79 g (the
  0–11 g slope within 0.14 % of the 0–79 g slope), so the 2–50 g pieces can set the slope for the 0.3–2.3 g drag range.
  Lessons for the real calibration: record with `scripts/serial_capture.ps1`; take a zero before and after each load
  (the zero lags 0.01–0.02 g after larger loads, and hysteresis and drift could not be separated with zeros only at the
  ends); go up and down; place each mass at one marked spot; lift weights straight off (tweezer bumps); log the BME280's
  temperature alongside; and keep heavy loads off the cell for a while before drag runs.
  Outcome: calibration dataset and fit (counts → N). Verify:
  residuals and linearity reported; calibration file referenced from the data catalog.
- [ ] **Optional bench follow-ups to EXP-002** (new 2026-11-26; on the printed scale, any time before the balance
  module). Each a short recording with `scripts/serial_capture.ps1`:
  - noise source: the 10 s zero with a box over the scale against without, and on the laptop's battery against on its
    charger (the reading noise is about 5× the 2026-11-23 taped-cell figure);
  - hysteresis against drift: one load cycle with an empty-pan zero between every load;
  - temperature: the BME280 logged beside the HX711 for an hour of empty pan.

  Outcome: each result in the data catalog (EXP-003 onward). Verify: the cause of the extra noise named, or ruled out.
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
  Tentative then; Accepted 2026-11-26); the 4-core cable optional; header strips tin-plated. Tracker: [docs/shopping_list.md](docs/shopping_list.md)
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
  (Tentative then; Accepted 2026-11-26), which also answers P1 "Decide the role of the op-amp circuit" (none); the Waveshare BME280 schematic
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
  `bme280_read`, with [firmware/README.md](firmware/README.md) and [D-019](DECISIONS.md) (Tentative then; Accepted 2026-11-26)
  ([session log](docs/sessions/2026-11-23-sensor-bring-up.md)).
- [x] 2026-11-23: PCB program chosen: KiCad 10 (owner; PROJECT_STATUS open question 18) ([session log](docs/sessions/2026-11-23-sensor-shield-pcb.md)).
- [x] 2026-11-23: Shield PCB designed (owner, agent checking): `PCB/arduino_shield/`, final ERC no errors, DRC 0
  unconnected items and 0 parity issues, Gerbers and drill files checked; not ordered ([D-020](DECISIONS.md);
  [session log](docs/sessions/2026-11-23-sensor-shield-pcb.md)).
- [x] 2026-11-24: Shield PCB session committed and pushed as `f10f315` (owner) ([session log](docs/sessions/2026-11-23-sensor-shield-pcb.md)).
- [x] 2026-11-24: A printable TAL221 bench-scale design found (owner) and checked against the TAL221 notes (agent);
  filed in `cad/third-party/tal221-scale-bwilless/` ([session log](docs/sessions/2026-11-23-sensor-shield-pcb.md)).
- [x] 2026-11-23: Sheet 12 redrawn as revision E (agent, at the wrap): connectors in each part's pin order, five-pin J3,
  C1 on the shield, the HX711's delivered pad names (replaces the 2026-11-18 task "Update sheet 12 with the delivered
  HX711 pad names") ([drawings README](docs/drawings/README.md); [session log](docs/sessions/2026-11-23-sensor-shield-pcb.md)).
- [x] 2026-11-24: The bench-scale continuation committed and pushed as `397c671` (owner); `/catchup` confirmed
  `UP_TO_DATE` on 2026-11-25 ([session log](docs/sessions/2026-11-26-shield-order-and-load-cell-bench-test.md)).
- [x] 2026-11-26: The shield's capacitors measured (owner): C2's lead spacing matches; C1 (0.1 µF film, 108.9 nF) has
  legs 6.5–6.7 mm apart, bent to the 5.0 mm holes; the agent checked the room on the board. No footprint change
  ([D-020](DECISIONS.md); [session log](docs/sessions/2026-11-26-shield-order-and-load-cell-bench-test.md)).
- [x] 2026-11-26: The breadboard brought to the shield's configuration (owner): C1 the 0.1 µF film (the old one was
  1 µF), R1 and R2 removed; scan, SDP810 zero and sign pass ([as built](docs/experimental_setup.md#breadboard-as-built)).
- [x] 2026-11-26: **Shield PCB ordered** (owner): JLCPCB Y6-12005915A, 5 boards, OSP, from the zip of `gerbers/` as
  committed in `397c671`; schematic title block filled in, revision 1
  ([shield PCB](docs/experimental_setup.md#shield-pcb-ordered-not-received)).
- [x] 2026-11-26: TAL221 bench scale printed and the cell mounted (owner); **EXP-002** recorded and analysed:
  13,727.5 counts/g, straight within 0.025 g to 79 g, zero wander and lag 0.005–0.025 g (Preliminary;
  [data catalog](docs/data_catalog.md#exp-002-load-cell-on-the-printed-bench-scale)). Replaces the P0 task "print the
  TAL221 bench scale and run a several-minute zero on it".
- [x] 2026-11-26: `scripts/serial_capture.ps1` written and used ([D-021](DECISIONS.md)); `analysis/exp002_bench_scale.py`
  written, the project's first analysis script ([session log](docs/sessions/2026-11-26-shield-order-and-load-cell-bench-test.md)).
- [x] 2026-11-26: `ac895a3` (shield order and EXP-002) committed and pushed by the owner; `/catchup` found it `UP_TO_DATE`
  ([session log](docs/sessions/2026-11-26-build-step-1-sizing.md)).
- [x] 2026-11-26: **Build step 1, the sizing.** Every tunnel part sized with the owner (D-022 to D-030): dimension
  sheets and Fusion points files in [cad/sizing/](cad/sizing/README.md), drawing package revision F. Replaces the P0
  "Start the sizing for the CAD" and the P1 "Size the contraction and test section" tasks
  ([session log](docs/sessions/2026-11-26-build-step-1-sizing.md)).
- [x] 2026-11-26: Fan chosen: the AC Infinity CLOUDLINE S6 ([D-025](DECISIONS.md), supersedes D-011). Replaces the P0
  "choose the fan" and P1 "Size and choose the fan or blower" tasks; the fan is still bought last.
- [x] 2026-11-26: Screens and honeycomb settled: three diffuser screens (D-026) and a compact 275 mm chamber with the
  printed honeycomb (D-027). Replaces "Choose the screens and honeycomb".
- [x] 2026-11-26: The owner confirmed D-004, D-006, D-007's open exit, D-016, D-018, D-019 (with `AVERAGE_OVER = 1`) and
  D-021; D-003's private visibility superseded by D-031 (the repository is public). Replaces "Owner: confirm or change
  the tentative decisions".
- [x] 2026-11-26: The 2026-11-15 P1 task "Owner: CAD every printed part from the dimension sheets" moved to P0 as "CAD
  from the sizing sheets, test coupons first", now that the sheets exist.
- [x] 2026-11-26: **Copyrighted PDFs out of the public repository's current files** (owner chose option (a); note on
  [D-031](DECISIONS.md)). 13 PDFs untracked with `git rm --cached` and listed in `.gitignore`; the local copies are
  unchanged (all 23 PDFs byte-identical by SHA-256 before and after). [resources/README.md](resources/README.md) links
  each one online, and the notes no longer link the files. Verified: `git ls-files resources` lists 8 PDFs, all
  NASA, AGARD or vendor datasheets. Not done: the copies in the Git history (option (b), not chosen). Replaces the P0
  "decide on the copyrighted PDFs" task ([session log](docs/sessions/2026-11-26-pdfs-decisions-register-and-cad-start.md)).
- [x] 2026-11-26: **Decisions register** in [PROJECT_STATUS.md](PROJECT_STATUS.md#decisions-what-is-decided-and-what-is-not):
  - what is decided, what the owner chose outside DECISIONS.md, and what is not decided yet;
  - every Status line in DECISIONS.md now starts with its current status;
  - the rule is in CLAUDE.md and `/wrap`.

  Verified by reading every Status line against the register
  ([session log](docs/sessions/2026-11-26-pdfs-decisions-register-and-cad-start.md)).
- [x] 2026-11-26: **The contraction and diffuser curves drawn without importing points.** They are exact control point
  splines (degree 5 and degree 3). `contraction.py` and `profiles.py` print the control points and check them against
  the equations (2.2 × 10⁻¹³ mm and below). Sheets: [cad/sizing/README.md](cad/sizing/README.md),
  [contraction.md](cad/sizing/contraction.md) and [diffuser.md](cad/sizing/diffuser.md)
  ([session log](docs/sessions/2026-11-26-pdfs-decisions-register-and-cad-start.md)).
- [x] 2026-11-26: Owner committed and pushed the PDFs-and-register session as `83d6fad`; `/catchup` confirmed
  `UP_TO_DATE` ([session log](docs/sessions/2026-11-26-first-cad-exports-checked.md)).
- [x] 2026-11-26: **First four CAD exports checked** (honeycomb, settling chamber C1, the whole diffuser, the fan inlet
  ring; 3MF in `cad/main cad files/`). Verified by cutting sections through each mesh against the sheets. Found and
  fixed by the owner in two rounds: C1 in six bodies, the missing chamfers (then fillets instead of chamfers) and a
  tapered socket. Owner's decisions: the diffuser 189 overall and the socket 27 deep (notes on D-026 and D-027); the
  tunnel is about 1.40 m long ([session log](docs/sessions/2026-11-26-first-cad-exports-checked.md)).
