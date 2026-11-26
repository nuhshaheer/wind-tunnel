# Bradshaw1964: The design of low-speed wind tunnels

- Citation: P. Bradshaw, R. C. Pankhurst, "The design of low-speed wind tunnels," *Progress in Aerospace Sciences* 5,
  1964, p. 1 (journal details from the earlier citation check; this copy states "Crown copyright. Reprinted from NPL Aero
  Report 1039").
- Copy in this folder: `Bradshaw1964_design-of-low-speed-wind-tunnels.pdf` (local only, not in Git since 2026-11-26: D-031)
  (was `bradshaw1964.pdf`). 69 PDF pages; **printed page = PDF page.** Scanned with a usable text layer; several
  formulas and all the figures are garbled in the text layer.
- Reviewed: 2026-11-22 by Claude Code (Opus 5.5). Read in full from the text layer: §§1–5 and 7–16. §6 (axial-fan
  design) skimmed, since this tunnel uses a bought duct fan; §15 (case studies of about thirty tunnels) read for its
  lessons; the drawings (Figs. 9–36) and Table 1 were not studied. The screen and contraction reduction factors were
  checked against our own arithmetic (below).
- Largely summarized by [Mehta1979](Mehta1979.md), which was written as its update; this file records what Bradshaw adds
  or puts differently.
- **Owner check pending** (checklist at the end).

## What it is

A review of low-speed tunnel design practice at the UK National Physical Laboratory in the early 1960s, component by
component (drive, fan, diffusers, corners, screens and honeycombs, contractions, working section, construction,
testing), with critical comments on existing tunnels and a "stereotype" design in the conclusions. "Wind tunnel
design lies somewhere between an art and a science, with occasional excursions into propitiatory magic" (p. 2).

## Key points and numbers (printed page)

**Tunnel types** (§3.2, pp. 7–8):

- Most tunnels with working sections under about 2 ft are open circuit.
- Open-circuit tunnels "are sensitive to draughts and obstructions in the tunnel room"; leave plenty of space between
  the tunnel and the room's walls, floor and ceiling (p. 7).
- **Blower tunnels** (fan upstream of the settling chamber and working section) suit work in which the flow leaving the
  working section is greatly disturbed. "Usually a diffuser is omitted: this enables liberties to be taken with the
  working-section arrangements at the cost of a power factor necessarily greater than unity" (p. 8).
- Open-jet working sections lose momentum to entrainment (an effective friction coefficient of 0.020) and suffer axial
  pressure gradients from flow into the collector (p. 8).

**Steady, uniform flow** (§4, pp. 9–13):

- "Unsteadiness is normally a symptom of flow separation or intermittent separation, for instance in a diffuser with
  too large an expansion angle, or in an excessively short contraction" (p. 9).
- Acceptable mean-velocity variation in a high-performance tunnel: ±0.2 % and ±0.1° (p. 10).
- Sphere critical Reynolds numbers as a turbulence measure depend on the sphere's diameter, so converting them to a
  percentage turbulence "is illogical" (p. 11).
- **"A useful indication of whether turbulence is low enough for a given test is to repeat it with a slightly higher
  turbulence level by inserting a coarse grid in the settling chamber."** Design the structure so extra screens, and a
  honeycomb, can be added later (p. 12).
- Reduction factors (pp. 12–13), as tabulated:
  - Screen, u-component mean velocity: (2 − K)/(2 + K), or (1 + α − αK)/(1 + α + K) with α ≈ 1.1/√(1 + K);
    for K = 1, 2, 3, 4: 0.33, 0, −0.2, −0.33 and 0.36, 0.1, −0.022, −0.086. v-component mean: α = 0.78, 0.64, 0.55,
    0.49.
  - Screen, r.m.s. intensity (experimental): u 0.45, 0.36, 0.31, 0.28; v 0.66, 0.54, 0.45, 0.40 (for K = 1–4).
  - Contraction of area ratio c, as fractions of the percentage variation: U mean 1/c², V mean 1/√c,
    u r.m.s. √[3(ln 4c³ − 1)]/(2c²), v r.m.s. √(3c)/(2c); for c = 12, 0.007, 0.29, 0.02 and 0.25 (our check reproduces
    all four).
  - "The reduction of the lateral component by a screen or a contraction is much less than that of the longitudinal
    component, and so it is the desired reduction in the former which decides the screen arrangement and contraction
    ratio" (p. 13).

**Speed setting** (§5, p. 15): the usual control signal is the pressure difference between a hole in the widest part of
the settling chamber and one near the narrow end of the contraction, "far enough upstream to be uninfluenced by the
presence of a model." **"In all but the smallest tunnels (i.e., whenever the contraction boundary-layer displacement
thickness is reasonably small compared with the working section size) this pressure difference is a constant fraction
of the empty working section dynamic pressure."** Use four holes, one on each wall, manifolded together.

**Fans** (§6, pp. 15–26): swirl must be removed by pre-rotation or straightener vanes unless it decays before the
working section; straighteners are "normally fitted as a precaution." Keep the working-section-to-fan area ratio about
2–3. A fan tends to even out circumferential velocity variations (p. 26).

**Diffusers** (§7, pp. 26–29):

- Usual rule: an equivalent cone of 5° total angle, and avoid thick entry boundary layers (p. 26).
- Wide-angle diffuser before the settling chamber: "A 45° equivalent cone with about three screens fitted at intervals
  has been found to maintain satisfactory flow with an area ratio of 4 : 1." "It would be an advantage for the screens
  to intersect the walls at right angles so that the refraction of the flow by the screens does not itself tend to
  produce separations, but this presents constructional difficulties" (pp. 26–27).
- "Adequate space should be allowed between the wide-angle diffuser and the honeycomb so that the outer cells of the
  latter run full" (p. 27).
- Screens in small-angle diffusers are not recommended except as an extreme remedy (p. 28). Leaks into a diffuser make
  jets normal to the wall (p. 27).
- Diffuser efficiency about 0.9 for 5–10° and usual area ratios (pp. 28–29).

**Screens and honeycombs** (§9, pp. 30–32):

- **Screens less than about 0.57 open** suffer a flow instability: the jets from the pores coalesce in random steady
  patterns, giving spanwise variations of boundary-layer thickness and wall shear of the order of 10 % (p. 30).
- Wire wakes become turbulent if U d/(βν) exceeds about 80 (150 for an isolated cylinder); that turbulence is small in
  scale and likely to decay (p. 30).
- Pressure-drop correlation: β²K/(1 − β) ≈ 9 Re^(−0.4) for 50 < Re < 200; Wieghardt's 6.5 Re^(−1/3) for 60 < Re < 600
  (p. 31). Example: 16-mesh, 28 s.w.g. (0.0148 in) wire, β = 0.58, K ≈ 1.25 at 30 ft/s, 1.6 at 12 ft/s.
- About four or five screens of K = 1.6 in the settling chamber for a low-turbulence general-purpose tunnel; spacing
  about **500 wire diameters** so each screen's wire wakes decay before the next (p. 31).
- **Honeycomb:** cell length at least 6–8 cell widths; flow incidence not over about 10°; about 50 cells across the
  settling chamber for a closed-circuit tunnel with screens, much finer for an open-circuit tunnel without screens;
  resistance coefficient about 0.5 (pp. 31–32). Screens are not effective at removing swirl; a honeycomb is.

**Contractions** (§10, pp. 32–35):

- "There is no wholly satisfactory method of contraction design." Any finite contraction has adverse gradients at both
  ends (proof by the hodograph, p. 35).
- In rectangular sections, surface streamlines cross the corners, giving severe secondary flow; corner boundary layers
  are more liable to separate. Octagonal sections are the usual compromise (p. 32).
- Designing by eye: make the wall radii of curvature smaller at the narrow end than at the wide end; "the temptation to
  draw an antisymmetrical S-shaped wall should be resisted, unless particularly mild velocity gradients are required at
  the high-speed end"; the wide-end radii must be large enough that the flow through the last screen is nearly axial.
  An "infinite-length" design can be cut off at the last screen (p. 34).
- The boundary layer usually becomes turbulent near the wide end (adverse gradient, concave wall), "in all but the
  smallest tunnels" (p. 34).
- Test a model contraction with a deliberately non-uniform inlet (part of the bellmouth obstructed) (p. 35).

**Working section** (§11, p. 35): a rectangle of about √2 : 1 with corner fillets; "Any increase in cross-sectional
area to compensate for boundary-layer growth is usually accomplished by tapering the fillets." Weigh-beam balances
reach 1 part in 10,000 of full load; "resistance strain gauges are notoriously sensitive to temperature" (p. 36).

**Smoke tunnels** (§12.1, pp. 36–37): speeds above 50 ft/s (15 m/s) rarely achieved; low turbulence needed (spread angle
about 2.5 u′/U radians); forced ventilation of the room is advisable, but natural ventilation "tends to produce
unsteadiness of the tunnel flow."

**Construction** (§13, pp. 38–45):

- Keep panel resonant frequencies above the fan blade frequency at maximum speed (avoid drumming); design for deflection,
  because "large deflections cause leaks to appear on repeated loading" (p. 39).
- Screens: the simplest mounting in small tunnels clamps the gauze between two frames that form part of the structure;
  small screens can be pre-tensioned flat, and must be taut enough to show no wrinkles when running (p. 42).
- Joints must be leak-proof (rubber gaskets, or sealing tape for sections not dismantled); leak-test after assembly
  (p. 42).

**Testing a new tunnel** (§14, pp. 45–46):

- Failure to reach design speed points almost certainly to the first diffuser or the fan.
- Detect separations with a surface pitot (Preston tube) or tufts; detect asymmetry with two pitots on opposite sides.
- **If turbulence is higher than expected, measure its frequency spectrum:** a peak at the fan shaft frequency means
  imbalance; at the blade frequency, an asymmetric velocity profile into the fan; low frequencies, unsteadiness
  (separation) in the circuit or contraction; broadband high frequencies, ineffective screens or honeycomb (p. 46).
- "The contraction ratios of 6 to 12 commonly used in modern tunnels should be sufficient to provide a very uniform mean
  flow in the working section unless the last screen is of poor quality" (p. 46).

**Lessons from case studies** (§15):

- NBS 4.5 ft tunnel: its "moderate contraction ratio of 7 : 1 is too small to make the effect of screen inhomogeneity
  negligible"; axial vorticity shed by the last screen produced spanwise variation of a flat plate's boundary layer
  (p. 47).
- RAE 4 ft × 3 ft tunnel, "one of the best tunnels ever built": its flaw was "an insufficient distance between the rapid
  expansion and the contraction resulting in a tendency to separation downstream of the screens" (p. 52); turbulence was
  traced to separations in the wide-angle diffuser and contraction, "too close together" (p. 46).
- RMTC tunnel: small disturbances were fed back round a low-resistance circuit; "large differences in performance …
  exist between almost identical tunnels" (p. 57).

**Conclusions: the stereotype** (§16, p. 65): a 1.5 : 1 working section no more than three equivalent diameters long;
5° diffusers; a rapid expansion of about 2 : 1 with at least two screens; a honeycomb of length/width at least 6–8
"mounted well downstream of the rapid expansion"; about four screens of K ≈ 1.6; a 12 : 1 contraction tested as a
model. "We hope that tunnel designers will either try the experiment of departing from this stereotype or, at least,
calibrate their tunnels properly and publish the results, good or bad."

## Limitations and caveats

- 1964 practice for large, mostly closed-circuit tunnels of wood; numbers in feet. Mehta1977 and Mehta1979 update it
  for small blower tunnels and are the project's main sources.
- The contraction guidance is "by eye"; it predates the computed designs of Morel1975 and Bell1988.
- The fan section assumes a custom axial fan with vanes, not a bought mixed-flow duct fan.

## What it suggests for this project [Proposed; arithmetic ours]

1. **The S − E factor may change with speed in a tunnel this small** (p. 15). Bradshaw's constant-fraction statement
   holds only when the contraction's boundary-layer displacement thickness is small next to the working section, and a
   100 mm section is at the "smallest" end. The calibration plan already measures the factor at every fan setting;
   expect a small trend with speed and fit it (for example against Re), rather than using one average.
2. **Turbulence sensitivity test for the sphere** (p. 12): repeat one sphere run with a coarse grid added in the
   settling chamber. If C_D barely changes, free-stream turbulence is not a significant error; if it changes, report
   the turbulence level with the result. A cheap and convincing check to add to the validation plan. The D-013 flange
   joints already allow an extra screen or grid to be clamped in.
3. **The last screen's quality matters at a contraction ratio of 6.25** (pp. 46–47: even 7 : 1 was too small to hide
   screen flaws). Choose the flattest, most even piece of the window screen for the last position, tension it evenly,
   and keep it free of creases.
4. **Screen open area:** the window screen's 66–69 % is above the 57 % limit (p. 30). Its wire Reynolds number in the
   settling chamber is about 59 at 13 m/s test speed (2.1 m/s through a 0.28 mm wire, β = 0.66), below the ~80 at which
   wire wakes turn turbulent.
5. **Honeycomb:** the printed one (6 mm cells, about 50 mm long, so L/D ≈ 8) meets the 6–8 rule. Across 250 mm it has
   about 42 cells, close to Bradshaw's 50 for tunnels with screens. Put it "well downstream" of the wide-angle diffuser,
   with enough space that its outer cells run full (p. 27); this is the same spacing issue as open question 15. A
   honeycomb is what removes the duct fan's swirl, since screens cannot (p. 31).
6. **Screens in the wide-angle diffuser should meet the walls at right angles** (pp. 26–27). Where a diffuser screen is
   clamped at a flange joint, give the walls a short parallel land on each side of the flange so the screen meets them
   square. Our suggestion, to fold into the diffuser CAD.
7. **Test-section length:** the planned 270–290 mm is 2.4–2.6 equivalent diameters (113 mm), within Bradshaw's limit of
   three. Tapering the corner fillets slightly along the test section is his way to offset boundary-layer growth
   (p. 35), the same aim as Barlow's slightly expanding walls; consider it if the measured pressure gradient is
   significant.
8. **The room:** keep the fan inlet clear of walls, doors and air vents, and leave free space in front of the open exit
   so the jet does not recirculate to the inlet (p. 7). For mist visualization, avoid draughts but ventilate (p. 37).
9. **Diagnosing problems when it first runs** (pp. 45–46): if it falls short of the expected speed, look at the
   wide-angle diffuser and fan first; use tufts to find separation; and log the S − E pressure fast enough to see its
   spectrum (fan shaft frequency means imbalance, blade frequency an uneven inflow, slow wandering means separation).
10. **Panels and joints:** keep printed and acrylic panels stiff enough not to drum at the fan's blade frequency, seal
    every joint (the neoprene gaskets), and leak-test once assembled (pp. 39, 42).

## References worth following up

- R. D. Mehta, P. Bradshaw (1979), already reviewed: [Mehta1979 notes](Mehta1979.md).
- G. B. Schubauer, W. G. Spangenberg, P. S. Klebanoff, "Aerodynamic characteristics of damping screens," NACA TN 2001,
  1950 (their ref. 21; free from NASA NTRS).
- G. B. Schubauer, W. G. Spangenberg, "Effect of screens in wide angle diffusers," NACA Report 949, 1949 (their ref. 14).

## Owner check (values read from the PDF)

Printed page = PDF page.

1. p. 8: the sentence on blower tunnels and the omitted diffuser.
2. p. 12: the sentence about repeating a test with a coarse grid in the settling chamber.
3. **Most important.** p. 15: the sentence beginning "In all but the smallest tunnels", and "four holes (one on each
   wall) manifolded together."
4. p. 13: the table of reduction factors for K = 1–4, and the four values for c = 12 (0.007, 0.29, 0.02, 0.25).
5. p. 30: the open-area limit "less than about 0.57" and the wire Reynolds number "about 80."
6. p. 31: "500 wire diameters"; honeycomb "cell length at least six or eight times the cell diameter."
7. pp. 26–27: the 45° wide-angle diffuser with about three screens at 4 : 1, and the screens meeting the walls at right
   angles.
8. p. 65: the list of stereotype features (a)–(k).
