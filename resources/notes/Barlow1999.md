# Barlow1999: Low-Speed Wind Tunnel Testing, 3rd ed. (selected chapters)

- Citation: J. B. Barlow, W. H. Rae Jr., A. Pope, *Low-Speed Wind Tunnel Testing*, 3rd ed., Wiley, New York, 1999.
  ISBN 0-471-55774-9.
- Copy: `Barlow1999_low-speed-wind-tunnel-testing-3rd-ed.pdf`, **local only, not in Git** (57 MiB, a commercial
  textbook; see the resources index). 724 PDF pages; a scanned book with an OCR text layer.
  - **PDF page = printed page + 11** throughout the chapters read (for example printed p. 234 is PDF page 245).
  - The text layer garbles most equations and some numbers. Equations quoted below were read from the page images
    unless marked "text layer".
  - The PDF has no bookmarks. Chapter starts (printed page / PDF page): 4 Pressure, flow and shear stress p. 136 / 147;
    6 Calibration of the test section p. 218 / 229; 7 Balances p. 234 / 245; 9 Boundary corrections I p. 328 / 339;
    10 Boundary corrections II p. 367 / 378; 12 Additional considerations (12.2 uncertainty) p. 444 / 455;
    17 Small wind tunnels p. 665 / 676.
- Reviewed: 2026-11-22 by Claude Code (Opus 5.5), at the owner's request ("go through these 5 papers thoroughly").
  What was read is listed at the head of each chapter section below. Chapters 1–3, 5, 8, 11 and 13–18 were not read.
- **Owner check pending** (checklist at the end).

Notation used in these notes: printed page first, then the PDF page, for example "p. 241 (PDF 252)".

## Summary for this project (2026-11-22; details and page references in each chapter section)

1. **The sting's drag must be measured with the ball in place**, not by running the sting alone (ch. 7). An image
   (mirror) sting from the ceiling, with a stub on top of the ball, measures tare plus interference in two runs.
2. **Seal the load-cell box** so no air flows through the gap around the sting (ch. 7).
3. **Calibration practice** (ch. 7): exercise the cell first, load up and down, repeat, check small loads, plot residuals,
   use the same electronics, use local g, take wind-off zeros before and after every run, and hang a check weight each
   session.
4. **The planned S − E airspeed method is the standard one** (ch. 6, Eq. 6.6). Calibrate it with the sting shield in
   place, at every speed, and keep the lines undisturbed and leak-tested (ch. 6; Bradshaw1964 adds that in tunnels this
   small the factor can vary with speed).
5. **The home-made total-pressure probe** starts to read low beyond about 8° of misalignment, not ±10° as the buy list
   assumed; chamfer the tip and align it carefully (ch. 4).
6. **Sphere corrections** (ch. 10): wake blockage (5/4)(S/C)C_Du plus solid blockage about a quarter of that; total
   about +4 % in q for the 3/4 in ball and about +7.6 % for the 1 in ball; subtract horizontal buoyancy from a measured
   pressure gradient (chs. 9–10). Testing two sizes at the same Re is the book's own check of the corrections (ch. 9).
7. **Uncertainty** (ch. 12): combine random and systematic parts, propagate through C_D = F/(qA), use block means
   because samples of an unsteady wake are correlated, and randomize the order of speeds.

---

## Chapter 7: Forces and moments from balance measurements (pp. 234–300, PDF 245–311)

Read: the whole chapter from the text layer, §7.1 reference frames briefly. Equation (7.13) and the numbers around it
were checked on the page image.

### What it says

**Alignment is critical, even for small angles** (§7.2, p. 241, PDF 252). In a worked example with lift ten times the
drag, skewing two balance members by 0.002 rad (about 0.1°) makes the drag read 2 % low (Eq. 7.12): "This is a 2 %
error in the drag reading! … Alignments of multicomponent balances is very critical. And even after the best efforts,
the result must be evaluated by calibration."

**Gravity is not 9.81 everywhere** (p. 241–242, PDF 252–253).

- Standard value 9.80665 m/s². Measured values range from 9.82618 m/s² (Hammerfest, Norway) to 9.79004 m/s² (Miami).
- Moritz's model with latitude λ, **Eq. (7.13): g = 978.0327 [1 + 0.0053024 (sin λ)² − 0.0000058 (sin 2λ)²]**
  (page image). The units are not printed; the numbers are in cm/s² (978.0327 cm/s² = 9.780327 m/s² at the equator;
  our reading).
- g also varies with altitude and local geology (not quantified). Dead-weight standards need a buoyancy correction for
  the density difference between the weight and the test article.
- "If a load cell is checked against a 'standard' weight, the result will, of course, be dependent on the local
  gravitational field strength."

**Calibration curves and residual plots** (p. 242, PDF 253; Figs. 7.5–7.6). Plot the difference between the
calibration data and a linear fit, and between the data and a second-order fit. "With the available computational
power today, there is little reason not to use whatever curve form is needed to reduce the residuals to have a mean of
zero with random distribution." Commercial transducers are often calibrated on site, and "it is often possible to
obtain better performance than the manufacturer quotes as nominal."

**Requirements** (§7.3, pp. 244–248, PDF 255–259).

- A warning to the inexperienced: "A wind tunnel balance is an immensely complicated apparatus … Buy the balance, then,
  if it is at all possible" (p. 244).
- Resolution example: one drag count (C_D = 0.0001) on a large airliner model needs 0.008 lb against a 600 lb range,
  75,000 : 1, so 17 bits. Averaging several passes helps, but "the minimum detectable value is still" one ADC step
  (p. 245).
- "Small tunnels intended for student use can have the tolerances relaxed" (p. 247).
- Table 7.3 (p. 248): permissible error in C_D of ±0.0001 or 0.1 % at low angle of attack, ±0.0020 or 0.25 % at high
  angle (aircraft).
- Do not run through test points faster than the forces settle: "The temptation to run through operating states too
  fast to get repeatable data must be resisted." Show the achieved precision next to the mean values as the test
  proceeds (p. 248).

**Deflections and pivots** (pp. 253–255, PDF 264–266). The mounting strut is the largest source of deflection; it must
be long and thin, which conflicts with stiffness, so use a high-modulus material. Ball and roller bearings make poor
pivots for very small rotations (flat spots, friction); flexures are essentially frictionless and free of hysteresis.

**What the force-measuring unit must do** (p. 256, PDF 267):

1. Keep a constant slope. A slope that drifts ("slips calibration") is hard to detect; DC amplifiers drift. "It is
   desirable to make end-to-end checks by the use of check weights at regular scheduled intervals."
2. Return to zero when the load is removed. "In most tunnels it is a standard policy to check the 'balance zero' for
   shift at the end of each run or run series. If the zero shift is too large, the runs are repeated. Care must be
   taken with the end of run zero to make sure that the tunnel velocity is also zero."
3. Show no hysteresis. When it appears, it is usually something loose and slipping, or "some slight contact or
   fouling that has not been found."
4. Connect to the data system.

**Strain gauges** (p. 258, PDF 269): almost always in a bridge; two or four active gauges to reduce temperature
effects, four also raising sensitivity. Typical resolution about 1 part in 20,000.

**Calibrating a balance** (pp. 258–263, PDF 269–274):

- A calibration covers loading each element, measuring deflections, combined loads, the natural frequency (to avoid
  resonance), and fluctuating loads, "so that it can be determined that the time average of balance output provides
  an accurate mean value" (p. 259).
- Loads are applied by cables over pulleys "about 8 in. minimum" radius, aligned with a plumb bob and level (p. 259).
- "It is common for new or repaired balances to require two or three full-load loading cycles before they settle in
  and give good repeatability" (p. 260).
- Load each component from zero to full scale and back to zero; plotting the error against load shows zero shifts and
  hysteresis (Fig. 7.18, where the permissible error line is 0.01 % of applied load). Repeat loadings to check
  repeatability, and apply very small loads to check sensitivity (p. 261).
- "In many cases the limitation on the accuracy of external balance measurements is actually the precision and
  accuracy with which calibration loads can be applied" (p. 262).
- The purposes of a calibration, as listed for internal balances (p. 296, PDF 307): proof load; coefficients;
  deflection against load; repeatability over short times; stability over long times; "sensitivity or minimum load for
  response"; hysteresis. Hysteresis "requires repeated loading sequences in which the loads are increasing and
  decreasing" (p. 299).

**Where interactions come from** (§7.6, pp. 293–296, PDF 304–307). A misalignment β between a sensor's measuring axis
and the load axis puts a fraction β of the cross load into the reading. Manufacturing misalignment gives linear
(first-degree) terms; elastic deflection under load gives second-degree terms, so "the raw data values depend on both
the applied load and the initial load" (Fig. 7.51). The interactions depend on the elastic modulus, which depends on
temperature.

**Temperature and electronics** (p. 299, PDF 310). Zero shift comes from temperature gradients across the balance and
from its average temperature. Reduce it with compensated gauges, four-arm bridges, and "insulating, heating, or cooling
the balance to minimize both temperature excursions and gradients." If the readout does not have infinite impedance,
"the data system used during test work must have the same impedance as the calibration data system."

**Tare and interference of the model support** (§7.5, pp. 264–279, PDF 275–290). The most important part of the
chapter for this project.

- A support adds three things to the reading: the direct air force on the exposed strut (**tare**), the strut's effect
  on the flow around the model, and the model's effect on the flow around the strut (together, **interference**). Their
  existence "should make clear the impossibility of evaluating the total tare by the simple expedient of measuring the
  drag of the struts with the model out" (p. 264). Again on p. 271: "The student invariably suggests removing the model
  to measure the forces on the model supports"; that exposes parts not normally in the flow and misses both
  interference effects.
- Struts of circular section have a drag that changes with Reynolds number (Fig. 7.19, cylinders and spheres); fixing
  transition reduces the variation (p. 264).
- Shield most of the strut with a fairing not attached to the balance. But "it is not advisable to try to decrease the
  tare drag … by continuing the windshields up close to the model because a fairing close to the model can increase the
  interference effects more than it decreases the tare." With an adjustable sleeve, the best sleeve position is the one
  that gives the lowest total measured drag (p. 265).
- **Seal the gap.** A pressure difference between the balance chamber and the test section drives flow up between
  the strut and its shield; "the flow can be eliminated by a light diaphragm seal" (p. 265). Bleed through the shields
  can induce flow along the model and even stall it: "It is therefore frequently advantageous to terminate the
  windshields well below the model and let the test be subjected to added but well-defined tare drag and to provide
  seals to stop the bleed flow" (p. 278, Fig. 7.32).
- **Measuring tare plus interference with an image (mirror) system** (pp. 271–274, Figs. 7.20, 7.24). The combined
  three-run method (p. 273): (1) model upright on its supports; (2) model inverted; (3) model inverted with dummy
  supports added on the other side, where "the exposed length of the support strut is attached to the model, and the
  clearance is in the dummy supports." Run (3) minus run (2) gives tare plus interference. The image geometry,
  including the gap between strut and fairing, must copy the real one exactly (p. 275). Without an image system, extra
  dummy supports can be added and assumed to act like the real ones, with a risk of mutual interference (p. 274).
- Size: "their combined effect often represents from 10 to 50 % of the minimum drag of the whole airplane" (p. 274).
  Wires taped to a strut need their own tare runs (p. 275).
- A strut behind a body, parallel to the flow, acts like a splitter plate and can suppress vortex shedding (p. 278).

**Flow angle and drift of the tunnel calibration** (pp. 265–270, PDF 276–281). Most tunnels have some upflow and cross
flow; for lifting models the misalignment correction comes from upright and inverted runs (Eqs. 7.17–7.21). Screens
get dirty, which changes the dynamic-pressure calibration and the upflow; check them periodically (p. 269).

### Limitations and caveats

- Written for large aircraft and automotive tunnels with multi-component balances. Nothing in the chapter treats a
  single-component, gram-scale balance or a commercial load cell like the TAL221.
- The tare and interference examples are for aircraft on struts; none is for a sphere on a sting.

### What it suggests for this project [Proposed; our reasoning, not decided]

1. **A sphere makes alignment easy.** It has no mean lift, so the 2 % effect above has nothing to act on. A tilt β of
   the load cell's sensitive axis loses only (1 − cos β) of the drag (about 0.0002 % at 0.1°) and adds β × the weight
   of the parts above the cell. That weight is constant, so the wind-off zero removes it.
2. **Second-degree effect between calibration and use (worth one check).** In the tunnel the cell carries the
   sting, ball and mount along its length while measuring drag across it; laid on its side for calibration, it does
   not. By the principle of Fig. 7.51 the sensitivity could differ slightly. A check in the upright position would show
   it. One way that needs no pulley: tilt the whole upright balance module by a measured angle θ, which applies
   W sin θ across the cell, where W is the weight of everything above it (weighed on the school balance). For example
   a 3° tilt gives 0.052 W. Our idea, not from the book.
3. **Zeros and check weights.** Take a wind-off zero before and after every run, with the air fully stopped. Set a
   limit on the zero shift from the calibration's repeatability, and repeat the run if it is exceeded. Hang one weighed
   check piece at the start of each session to confirm that the slope has not drifted (p. 256).
4. **Calibration procedure** (pp. 259–262, 296–299): first exercise the cell two or three times to a load above the
   working range (keeping masses plus preload under 100 g); then load in steps from zero up and back down, and repeat
   the whole sequence. That gives repeatability and hysteresis. Use the 2 g pieces for sensitivity at the drag range;
   plot residuals against a linear fit; keep a second-order fit only if the residuals show curvature; record the
   temperature. Calibrate with the same HX711 board, wiring and channel used in the tunnel (p. 299).
5. **The sting's tare and interference must be measured, not estimated, and not by running the sting without the
   ball** (pp. 264, 271). Our earlier estimate is 0.1–0.2 gf with about 5 mm exposed, which is 8–16 % of the 3/4 in
   ball's drag at 13 m/s. An adaptation of the image method suits a sphere, because a sphere needs no inversion: hang
   a dummy shield from a spare top panel, mirroring the floor shield, and attach a stub of sting of the same exposed
   length to the top of the ball, clear of the dummy shield. The difference between runs with and without the image is
   the tare plus interference of one sting and shield. Our adaptation, to be designed and checked.
6. **Seal the load-cell box.** The gap around the sting connects the test section to the box. Any leak from the box to
   the room, for example at the cable entry, lets air flow through that gap and push on the sting and the ball's
   underside (pp. 265, 278). Keep the box airtight apart from that gap.
7. **Temperature.** Keep the cell enclosed and away from the fan motor, and let the tunnel reach a steady temperature
   before runs: gradients across the cell shift its zero (p. 299). This agrees with the
   [TAL221 notes](TAL221.md).
8. **Local gravity.** Convert calibration masses with g from Eq. (7.13) at the owner's latitude, which is not
   recorded in the docs. Using 9.81 m/s² instead is within about 0.2 % at latitudes 25–60° (9.7896 at 25°,
   9.8062 at 45°, 9.8192 at 60°; our arithmetic), far below the other errors, so it is acceptable. The difference from 9.80665 m/s² is at most about 0.27 % (equator 9.7803, poles 9.8322
   m/s²; our arithmetic). Buoyancy on the weights is about 0.015 % for steel (1.2 / 8000; our arithmetic), negligible.
9. **Take data slowly** and show the standard deviation next to each mean while running (p. 248). The sphere's wake
   is unsteady, so the drag must be averaged; the calibration should include a tap test for the natural frequency of
   the sting and ball on the cell (p. 259).

---

## Chapter 12, §§12.1–12.3: Experiments, uncertainty, design of experiments (pp. 444–461, PDF 455–472)

Read: §§12.1–12.3 in full from the text layer. Table 12.1 and Eqs. (12.5)–(12.6), (12.11)–(12.13), (12.15) and
(12.18)–(12.20) checked on the page images. §§12.4–12.6 (model construction, planning, use of facilities) not read.

### What it says

**Two kinds of uncertainty** (pp. 445–447, PDF 456–458). Random (precision) components scatter about the true value
on repetition; systematic (bias) components repeat the same offset. Bias is "the most difficult to deal with in a
wholly satisfactory way"; it is usually all that is not random, and it must be estimated by judgment because it cannot
be sampled (for example, the effect of as-built model geometry would need many identical models).

**Distributions** (pp. 448–450, PDF 459–461). Normal, uniform, chi-square and Student t. For a uniform distribution of
half-range a, **σ = a/√3** (Eq. 12.6). The t distribution is "essentially indistinguishable from the normal
distribution for k > 100" degrees of freedom.

**Confidence interval on a mean** (pp. 451–453, PDF 462–464).

- Sample mean x̄ = (1/n) Σ xᵢ and sample standard deviation s = √[Σ(xᵢ − x̄)²/(n − 1)] (Eq. 12.11).
- Probability{x̄ − k₃s < μ < x̄ + k₃s} = β_cp (Eq. 12.12); the half-width is Δx = k₃s (Eq. 12.13), with k₃ from the t
  distribution with n − 1 degrees of freedom.
- **Table 12.1, k₃ = Δx/s at 95 % confidence** (selected rows): n = 2: 8.9846; 3: 2.4841; 5: 1.2417; 8: 0.8360;
  10: 0.7154; 12: 0.6354; 20 (not tabulated; between 19: 0.4820 and 21: 0.4552); 33: 0.3546; 105: 0.1935;
  201: 0.1391; 1033: 0.0611. (Our check: these equal t(0.975, n − 1)/√n, for example 2.262/√10 = 0.7154.)
- Example data (Fig. 12.5): 1000 drag readings at 8 samples per second from an external balance, for three objects.
  "Our sense is that taking less than eight observations in these types of situation is not often a good choice."
- Example 12.1 (p. 453): to get ±0.02 lb at 95 % with standard deviations of 0.03, 0.14 and 0.56 lb takes 12, about
  200, and "several thousand" samples respectively.
- **Periodic shedding:** "For objects that exhibit periodic shedding at frequencies that can drive the balance, the
  histogram will differ considerably from a normal form. In such cases, a dynamic analysis needs to be conducted and
  any sinusoidal time series removed from the data" (p. 453). Balances are "dynamic systems with their own transfer
  functions."

**Systematic components** (pp. 455–456, PDF 466–467). Estimate the maximum effect ±a of each identified source, assume
a distribution within ±a ("Assuming a uniform distribution is more conservative or pessimistic"), and treat it like a
random variable. Sources are usually taken as independent, but some are correlated.

**Combining** (pp. 456–458, PDF 467–469). For one variable, **U = √(U_s² + U_r²)** (Eq. 12.15). For a derived result
y = f(x), propagate with the first-order Taylor series: ỹ = [∂f/∂x] x̃ (Eq. 12.18), and ⟨ỹỹᵀ⟩ = J ⟨x̃x̃ᵀ⟩ Jᵀ
(Eq. 12.19), where J is the Jacobian at the mean. Random and systematic parts are assumed independent; correlated
systematic parts add off-diagonal terms that "may increase or decrease the variances" (Eq. 12.20). AGARD AR-304 (and
the essentially identical AIAA standard) works a full example for a force test (p. 458).

**Design of experiments** (§12.3, pp. 458–461, PDF 469–472).

- Three principles (after Montgomery): **replication** (repeat to measure variability directly), **randomization**
  (vary the order so that uncontrolled drifts average out; "the order in which conditions are set can have an effect on
  the resulting data"), and **blocking** (measure increments with the rest of the setup left in place, which gives more
  precise increments than removing and reinstalling the whole model).
- Guidelines (pp. 460–461): state the problem and the accuracy needed before starting; identify the outcomes and the
  ranges of parameters; identify the corrections (boundary, tare, interference) and their effect on accuracy; prepare
  run schedules with replication, randomization and blocking in mind; monitor achieved precision during the run; and
  report the achieved accuracy with the data. "Statistical significance and practical significance … are entirely
  different issues." "Usually, a series of experiments that build on each other rather than one all-encompassing
  experiment is a more effective use of resources."

### Limitations and caveats

- The confidence interval assumes independent, normally distributed samples. Samples taken quickly from an unsteady
  wake are correlated in time, so n consecutive samples carry less information than n independent ones. The book
  mentions periodic shedding and balance dynamics but does not give a method for correlated samples (our observation).
- The full worked uncertainty example is in AGARD AR-304, which is not in this folder.

### What it suggests for this project [Proposed]

1. **Uncertainty budget for C_D.** With C_D = F/(qA), and independent errors, the first-order propagation
   (Eq. 12.19) reduces to (δC_D/C_D)² = (δF/F)² + (δq/q)² + (δA/A)² (our algebra). Each term gets a random part from
   repeated readings and a systematic part from calibration, estimated as ±a with σ = a/√3 when only a bound is known.
   The blockage and tare corrections add their own systematic terms. This is the structure for the TODO uncertainty
   task; NIST TN 1297 (resources "Wanted" item 10) covers the same ground.
2. **Correlated errors matter here.** The same SDP810 measures q in every run, and the same calibration sets F; these
   systematic errors are shared by all runs, so averaging runs does not reduce them. Comparing the 3/4 in and 1 in balls
   at the same Re shares the q error, which partly cancels in their ratio (our reasoning).
3. **Number of samples.** Use Table 12.1 with the measured standard deviation: the 95 % half-width is k₃s. Because
   HX711 samples of an unsteady wake are correlated, compute s from block means (for example 1 s blocks) rather than
   from raw samples, and use the number of blocks as n (our proposal).
4. **Run order.** Randomize the order of speeds in a sphere run, or at least run speeds up and then down, so that slow
   drift (temperature, zero) shows up instead of masquerading as a Reynolds-number trend (§12.3). Repeat whole runs on
   different days for replication.
5. **Blocking for the sting tare.** Measure the image-sting increment (Chapter 7 notes, item 5) with the ball left in
   place, adding and removing only the image parts.

---

## Chapter 4: Pressure, flow and shear-stress measurements (pp. 136–187, PDF 147–198)

Read: §§4.1–4.3 in full (pressure-sensitive paint, hot wires and laser methods skimmed); §§4.4–4.5 skimmed for
anything about pitot tubes, taps and tubing. Eq. (4.1), the gravity formula, Eq. (4.12) and Figs. 4.5, 4.7 and 4.8
checked on the page images.

### What it says

**The airstream is defined by mean values** (p. 136, PDF 147): pressure and dynamic pressure are "the mean values …
averaged over a time interval chosen according to the required precision of the mean." Humidity changes the gas
constant in the equation of state.

**Manometers** (§4.1, pp. 137–142, PDF 148–153).

- **Eq. (4.1): p₂ − p₁ = Δh sin β g_l (ρ_f − ρ_a)**, where Δh is the liquid-column length difference along the tubes, β
  the angle of the tubes above horizontal, ρ_f the liquid density and ρ_a the air density. A smaller β gives more
  sensitivity.
- Local g is needed. The International Association of Geodesy formula (1980) is printed on p. 138 as
  g = 978.0327[1.0 + 0.053024 (sin φ)² − 0.0000058 (sin 2φ)²] dyn/g. **Misprint:** the second coefficient should be
  0.0053024, as in Eq. (7.13) on p. 242; only that value gives the book's own "variation from the equator to the north
  or south pole is about 0.5 %" (our check). The unit, dyn/g, is cm/s².
- Weighing the manometer liquid in air to get its density needs a buoyancy correction (p. 138).
- "Manometers are used frequently for calibrating and checking other devices, as it is difficult to obtain a more
  accurate or precise result in the range of differential pressures commonly of interest in subsonic aerodynamic
  testing" (p. 138). Accuracy is limited by reading the heights, by the liquid's density, and by surface tension
  (p. 139). Water with a little dye, or silicone oil, are the usual liquids (p. 140).
- A precise manometer drifts if the observer's body heat reaches it; it needs a stable thermal environment
  (pp. 140–141).
- Of the remaining uses of manometers, "the most important is the use of a manometer as a calibration standard for the
  transducers" (p. 152).

**Pressure transducers** (pp. 141–145, PDF 152–156).

- Two classes: those that monitor the tunnel condition, which must be accurate and stable (kept in thermally
  controlled enclosures), and cheap ones for model pressures.
- Silicon strain-gauge units "are remarkable for their economy, although they must be calibrated frequently against
  more stable standard units" (p. 142). They are "more susceptible to drift" (p. 143).
- Calibrate as mounted: clamping a transducer shifted its calibration slightly, and "the pressure transducer should be
  calibrated mounted" (p. 144).
- An end-to-end calibration through the same signal conditioning, digitizer and curve fit as the test is the ideal
  (p. 143). Transducers are usually linear, but third-order fits are often used (p. 144).
- Diaphragm transducers respond at a few hundred hertz; "the connecting pressure tubing will have a major dynamic effect
  on time-varying pressure measurements" (p. 144).
- With many lines, check each for plugs (a very slow response to a pressure change) and leaks (the reading changes
  while a held pressure is applied) (p. 152). A "lack of data visibility" lets a slipped calibration or a leaking line
  go unnoticed; show the readings live (p. 152).

**Temperature** (§4.2, pp. 153–154, PDF 164–165). At low speed the recovery factor is close to 1, so a flush
wall-mounted probe in the test section gives the stream temperature. A probe in the settling chamber needs a correction
to test-section conditions. Temperature is needed for density, velocity and Reynolds number.

**Total-pressure tubes and pitot-static tubes** (§4.3, pp. 154–159, PDF 165–170).

- **Sensitivity to flow angle** (p. 154, Fig. 4.5): "Pitots with hemispherical noses begin to show errors in total
  pressure at very low angles of flow inclination. Pitot tubes with a sharp square nose begin to show errors near 8°
  flow inclination. This can be improved by chamfering the nose." A Kiel tube reads correctly beyond 30°. A
  hemispherical tip reads total head accurately "as long as the yaw is less than 3°" (p. 155).
- A pitot-static tube can give q within about 0.1 % "if due allowance is made for these errors" (p. 155).
- **Low Reynolds number** (p. 156, Fig. 4.7): both tip shapes read high when Re on the probe diameter is low. In
  creeping flow, Barker: C_p(stag) = (p_stag − p)/q = 1 + 6/Re_d (Eq. 4.12).
- **Near a wall** (Fig. 4.8): a circular pitot tube needs a velocity correction ΔV/V that grows as the gap Z to the
  wall shrinks, plotted for Z/D from 0.5 to 1.9.
- **Static holes on a probe** read wrong for two reasons: low pressure behind the nose (reads low) and high pressure
  ahead of the stem (reads high) (pp. 156–157, Fig. 4.9). Example 4.1 (p. 158): holes 3.2 D behind the tip read
  0.5 % q low, and 8 D ahead of the stem 1.13 % q high, net 0.63 % q high. The Prandtl design places the holes where
  the two cancel (Fig. 4.10); a "standard" tube does not, and its readings are corrected with Fig. 4.9.
- A pitot-static tube near a model reads the model's pressure field, "which is why tunnel dynamic pressure calibrations
  are made without a model in the test section" (p. 159).
- Yawheads, claws and cone probes measure flow angle and must be calibrated, ideally upright and inverted (pp. 159–163).

**Wake surveys** (§4.5, pp. 176–179, PDF 187–190). Use the free-stream q from the outer tubes of the wake rake, "not
from the tunnel q at the model location, because the longitudinal velocity gradient in the tunnel invalidates q
calibrations made upstream" (p. 178). A round total-head tube in a pressure gradient across its face does not read the
centreline value; flattened tips are recommended (p. 179).

### Limitations and caveats

- The book does not quantify how much tubing a thermal (flow-through) sensor such as the SDP810 tolerates; its tubing
  remarks concern the response time of diaphragm sensors.
- Figs. 4.5, 4.7 and 4.8 are small plots; values read from them need the owner check at the end.

### What it suggests for this project [Proposed]

1. **The home-made total-pressure probe (a square-cut 1/8 in brass tube).** The buy list says "within about 1 % of q
   for misalignment up to about ±10°; confirm in Barlow1999 ch. 4." **Partly confirmed, partly corrected:** Barlow says
   a square nose starts to show error near 8°, and chamfering the nose improves this. So aim the probe within a few
   degrees of the flow, chamfer the outside of the tip, and do not rely on ±10°. The size of the error at 10° is to be
   read from Fig. 4.5 (owner check).
2. **Reynolds number of the probe.** For a 3.18 mm tube in air (ν ≈ 1.5 × 10⁻⁵ m²/s), Re_d is about 1400 at 6.5 m/s
   and 2800 at 13 m/s (our arithmetic). Figure 4.7's curves have flattened by then (owner check), so no
   low-Reynolds-number correction is expected. Eq. (4.12) applies only to creeping flow and is not for use here.
3. **Distance from the walls when mapping the flow.** Keep the probe tip more than about two outside diameters
   (about 7 mm) from any wall, or apply Fig. 4.8's correction; the boundary layer itself is a separate effect.
4. **Wall taps instead of probe static holes** avoid the tip and stem errors of Fig. 4.9 entirely, and they are what
   the project plans already. Two checks follow from the book:
   - the probe's own stem raises the pressure ahead of it, so read the M taps with the probe in and with it removed
     (empty tunnel, same fan setting); they should agree. If not, lengthen the probe's horizontal leg so its tip sits
     farther ahead of the stem (our proposal);
   - the q calibration must be done without the sphere in the test section (p. 159), which is the plan.
5. **Calibrate the SDP810 against a water manometer, mounted and with its real tubing**, because a manometer is the
   standard for this pressure range (pp. 138, 152) and a transducer is best calibrated as mounted (p. 144). At
   15–100 Pa a vertical water column is only 1.5–10 mm, so incline the tube: at 1 in 10 (sin β = 0.1) the reading
   becomes 15–100 mm along the tube (our arithmetic with Eq. 4.1). Measure the slope and the water temperature; use
   local g; keep hands and breath away from the tube while reading. This matches the buy list's §9 plan.
6. **Check each tap line for leaks and plugs** before trusting it (p. 152): apply a small held pressure and watch for a
   falling reading (leak) or a slow response (plug).
7. **Show readings live** during runs (Serial Plotter, then a laptop script), so a leaking line or a slipped zero is
   noticed at once (p. 152). This is already in the firmware plan.
8. **The q reference is calibrated in the empty tunnel and then used with the sphere in place**, so any longitudinal
   pressure gradient between the reference station and the sphere matters (p. 178). This links to the empty-tunnel
   gradient (Chapter 6 notes) and to the horizontal-buoyancy correction (Chapter 10 notes).

---

## Chapter 6: Calibration of the test section (pp. 218–233, PDF 229–244)

Read: the whole chapter from the text layer (§6.3 acoustics skimmed). Eqs. (6.1)–(6.6) checked on the page images.

### What it says

**Setting the speed from two wall pressures** (§6.1, pp. 218–221, PDF 229–232).

- A probe cannot sit in the test section with the model, because the model changes the flow ("induced flow"). So the
  speed is set from a pressure in the settling chamber (station L), "downstream of" any honeycomb or screens, and a
  static pressure just ahead of the test section (station S).
- Eq. (6.1): P_L + q_L = P_S + q_S − K₁q_S, with K₁q_S "an allowance for the small loss in total pressure." Continuity
  (6.2)–(6.3) gives q_L = (A_S/A_L)² q_S = K₂q_S. So **P_L − P_S = q_S (1 − K₁ − K₂)** (6.4). If S is not at the
  test-section area, q_S = (A_J/A_S)² q_J = K₃q_J (6.5) and **P_L − P_S = (1 − K₁ − K₂) K₃ q_J** (6.6).
  (Sign as printed: with this form a total-pressure loss makes K₁ negative; our check. The calibration measures the
  whole factor, so the sign does not matter in practice.)
- "The actual calibration of the tunnel is accomplished by running the tunnel at various values of P_L − P_S while
  measuring the dynamic pressure in the test section with a calibrated pitot-static tube. This evaluates
  (1 − K₁ − K₂)K₃" (p. 220).
- Survey at least the plane of the model, better the whole volume the model occupies; with large variations, use a
  weighted average q (p. 220).
- **Calibrate each test-section configuration separately**: "If the tunnel has an external balance, calibrations are
  often made with and without the balance struts and their fairings" (p. 220).
- The pressure sources should be a ring around the station, or taps on opposite walls, manifolded to an average; a
  sealed perforated tube flush with the surface also works. A large model or a model mounted far upstream can affect
  the S station; check this (pp. 220–221).
- **Leaks:** "Extreme care must be taken to make sure that there are no leaks in the tunnel dynamic pressure system …
  It is highly desirable and strongly suggested that the system should not be disturbed once it has been leak
  checked." Record each station's pressure relative to the room separately, from additional taps, as a check
  (p. 221). Check periodically for leaks, for example with a calibration model run at several q (p. 221).

**Longitudinal pressure gradient** (pp. 221–222, PDF 232–233). It "must be known in order to make necessary buoyancy
corrections." Measure it with a static probe moved along the centreline, or with a long static tube (a tube through the
test section with rings of manifolded static holes). Wall pressures are "a good adjunct", but "small variations in wall
geometry associated with joints, mounting holes, and the like cause local variations in the static pressure that are
typically too large to ignore … it is not a good idea to rely on wall pressure measurements for the baseline
characterization."

**Uniformity targets** (pp. 222–224, PDF 233–235).

- "The variation of q in the working range of the jet should be less than 0.50 % from the mean, which corresponds to a
  0.25 % variation in velocity." Fig. 6.2 shows a real section with 1.5–2 % variations; "the survey should have been
  carried to the walls."
- Uneven velocity can be fixed with local repairs, or with screens in the largest section whose mesh is denser where the
  jet is fast (Fig. 6.3).
- Flow angle: desirably within ±0.10°, at most ±0.20° (p. 224).

**Turbulence and spheres** (pp. 224–227, PDF 235–238).

- The Reynolds number at which a sphere's drag drops sharply (the critical Reynolds number) falls as tunnel turbulence
  rises; surface roughness also matters strongly. Free-air critical Re for a smooth sphere: **3.85 × 10⁵** (p. 224).
- A **turbulence sphere** finds the tunnel's critical Re: either where C_D = 0.30 on the drag curve (Fig. 6.5), or where
  ΔP/q = 1.220 from the nose pressure minus the mean of four rear pressures (Fig. 6.6). Turbulence factor
  TF = 385,000 / Re_critical; effective Re = TF × test Re (Eq. 6.9). It gives an average measure only, but is quick and
  useful for spotting changes. Fig. 6.7 relates TF to hot-wire turbulence intensity (Dryden et al., NACA Report 581).
- "The need for low test-section turbulence is not as severe for small student tunnels" (p. 227).

**Tunnel boundary layers and separation** (§6.2, pp. 227–229). Tunnel boundary layers are almost always turbulent.
Low-frequency unsteadiness suggests separated flow somewhere; look for it with a tuft wand or tufts taped to the
walls.

**Data systems** (§6.4, pp. 230–232, PDF 241–243). Store the test, run and configuration with every reading, and a
time stamp. Filters "must be used carefully" so that the signal is improved and not damaged. Data systems sample far
faster than the flow changes; aerodynamic "noise" is often slow, which "simply extends the time over which a particular
condition must be held and data averaged."

### Limitations and caveats

- Written for large closed-circuit tunnels; no specific guidance for an open-circuit blower tunnel with an open exit.
- The turbulence-sphere method needs Re of order 10⁵, far above this tunnel's range.

### What it suggests for this project [Proposed]

1. **The planned S − E airspeed method is the book's standard method** (Eq. 6.6). With the E ring at the
   test-section area, K₃ = 1 and K₂ = 1/6.25², so the ideal factor is 0.974, as in the buy list; the real factor is
   measured against the probe, exactly as on p. 220. **This answers the buy list's "Still to confirm in Barlow1999
   ch. 4 and 6": confirmed.** Two details from the book: the S ring must sit downstream of the last screen (p. 219),
   and the calibration should be made with the sting shield and floor insert in place but no ball, because the support
   fairing changes the calibration (p. 220).
2. **Leak-tightness of the S and E lines** (p. 221). The swap procedure disturbs the tubing on every calibration day,
   which the book advises against. Keep the S and E lines connected for force runs and swap only on calibration days;
   after any swap, check the wind-off zero (already planned) and do a held-pressure leak test. Two small 3-way valves
   (the buy list's upgrade) would disturb the lines less than pulling tubes.
3. **Do not rely on wall taps alone for the baseline** (p. 221). Wall taps at M stand in for the probe's static
   holes. Place every tap away from panel joints, screw holes and the floor-insert edges; read the four taps of a
   station one by one and require them to agree (already planned); and consider a simple long static tube, or a
   static probe, as an independent check of the M station. Our suggestion.
4. **Measure the empty-tunnel pressure gradient along the test section.** It is needed for the horizontal-buoyancy
   correction (Chapter 10 notes). The probe can be moved along the centreline for the total pressure, but the static
   pressure needs a static probe or the long static tube (p. 221).
5. **Uniformity target.** q within ±0.5 % of the mean over the region the sphere occupies is the professional target
   (p. 222). Report the flow map's spread against it; screens with denser mesh where the jet is fast are the book's fix.
6. **Turbulence.** A turbulence-sphere measurement is out of reach (this tunnel's Re is 1–2.5 × 10⁴, against a
   critical Re of order 10⁵), and the validation sphere runs well below its critical Re. Free-stream turbulence can
   still shift subcritical sphere drag slightly; that is a reason the ±10 % reference band is appropriate, not a
   correction we can apply (our reasoning).
7. **Look for separation** in the diffuser and contraction with a tuft wand or wall tufts when the tunnel first runs
   (§6.2), especially if the S − E reading shows slow wandering.

---

## Chapter 9: Boundary corrections I, basics and two-dimensional cases (pp. 328–366, PDF 339–377)

Read: §9.1, §9.2 (method of images and panel methods skimmed, measured-variable methods read), §9.3 skimmed, §9.4
(buoyancy, solid blockage, wake blockage) read; streamline-curvature algebra for airfoils skimmed. The equations quoted
were read from the page images (pp. 352, 354–357).

### What it says

**The effects of finite walls, defined** (pp. 328–330, PDF 339–341):

- **Horizontal buoyancy:** the static pressure varies along the empty test section, which pushes on a model like
  hydrostatic buoyancy. Not to be confused with the pressure variation the model itself causes.
- **Solid blockage:** the model's frontal area is a finite fraction of the section, "usually chosen in the range of
  0.01–0.10 with 0.05 being typical." In a closed section it raises the surface stresses, represented as an effective
  increase in speed or dynamic pressure. The first-order treatment assumes the pressure distribution's shape is
  unchanged, which "is obviously not valid for 'large' values of the blockage."
- **Wake blockage:** the wake's finite size; in a closed section it increases the measured drag. Often neglected for
  an open jet.
- Streamline curvature, downwash changes and propeller effects concern lifting models.
- Corrections are applied "in a linear manner … a superposition of the individual effects" (p. 330). Flow
  nonuniformity, tare and interference must be removed first: "It is necessary that the influence of those effects has
  been removed insofar as possible or practical before wall effects are considered" (p. 330).

**Size of the effect** (pp. 333–335, Fig. 9.9): an idealized 2-D cylinder plus wake at a large blockage gives a
centreline velocity increment of about 5.5 % (11 % in q). It scales with blockage, so "a blockage of 5 %, which will be
more typical, will produce velocity and dynamic pressure increments of about 1.3 and 2.6 %." The increment varies
through the test section, and the wake's share is larger in proportion to its size than the body's, so wakes need
careful treatment where flow separates (p. 335).

**Methods based on measured quantities** (§9.2, pp. 342–346, PDF 353–357). Maskell's method uses the measured drag
coefficient. The Hackett–Wilsden "wall signature" method uses a row of wall pressures to build a simple source model of
the body and wake; its report "also shows good correlation on sphere drag above and below the critical Reynolds number"
(p. 344). The Ashill–Keating two-variable method uses about 100–200 wall pressures and needs no model of the body
(p. 346).

**Buoyancy, two-dimensional** (§9.4, pp. 350–353, PDF 361–364).

- "Almost all wind tunnels with closed throats have a variation in static pressure along the axis of the test section
  resulting from the thickening of the boundary layer … Some tunnels have slightly expanding test sections to minimize
  this effect." The pressure falls towards the exit, so the model is "drawn" downstream (p. 350).
- Glauert's gradient factor k "has been observed in the range 0.016–0.040 for a closed square jet … but should be
  experimentally measured for a given tunnel." A long static tube is the ideal tool (p. 350).
- Horizontal buoyancy is small for wings but important for bodies; for large torpedo-like bodies "it can be of the order
  of the minimum drag" (p. 350).
- For a constant gradient, **D_B = p′ ∫S(x) dx = p′ × Vol** (Eq. 9.17, printed without a sign; p′ is the slope of the
  static pressure, and a falling pressure gives a positive drag). Adding the "squeezing" of the streamlines, Glauert's
  two-dimensional result is D_B = (π/2) λ₂ t² p′ per unit span, with t the thickness and λ₂ a body shape factor
  (Fig. 9.16) (p. 352).

**Solid blockage, two-dimensional** (pp. 353–355, PDF 364–366).

- The velocity increment at the model is "about one-fourth" of what the plain area reduction would suggest, because the
  streamlines far from the model are displaced most (p. 354).
- **Circular cylinder of radius a between walls h apart: ε_sb = (π²/3)(a²/h²)** (p. 354, by summing images). A 2 ft
  cylinder in a 10 ft tunnel acts as if the speed were 3.3 % higher.
- Glauert, for any 2-D body of thickness t: ε_sb = (π²/3)(λ₂/4)(t²/h²) = 0.822 λ₂ t²/h² (Eq. 9.20); −0.411 for an
  open jet. Allen and Vincenti: ε_sb = Λσ (Eq. 9.21).
- Thom: **ε_sb = K₁ (model volume)/C^{3/2}** (Eq. 9.22), with K₁ = 0.74 for a wing spanning the tunnel breadth and 0.52
  for one spanning the height (7 × 10 ft-type tunnels).
- **C, the test-section area, is better taken as the geometric area less the boundary-layer displacement thickness
  around the perimeter.** For a turbulent boundary layer the displacement thickness is about one-sixth of the boundary
  layer thickness (one-third if laminar), but it "will have to be measured" (p. 355).

**Wake blockage, two-dimensional** (pp. 356–357, PDF 367–368).

- A source at the body represents the wake; image sinks give ε_wb = ΔV/V_u = τ c_du with τ = (c/h)/4 (Thom gives the
  same).
- **Maskell: ε_wb = (c/h)/2 × c_du** (Eq. 9.23), twice the image value, because the faster flow outside the wake also
  lowers the pressure on the rear of the body. This uses the measured (uncorrected) drag coefficient c_du.
- For open jets the sign reverses, and the jet length can matter (Mercker and Wiedemann).

**Applying the corrections, two-dimensional** (§9.4, pp. 360–362, PDF 371–373; text layer, equations partly garbled):
q = q_u(1 + 2ε) (Eq. 9.29), Re = Re_u(1 + ε) (Eq. 9.30), and **c_d0 = c_d0u(1 − 3ε_sb − 2ε_wb)** (Eq. 9.34), "from the
dynamic pressure effect plus the wake gradient term." With ε_sb = (π²/12)(d/h)² and ε_wb = (d/h) c_du/4 for a cylinder
this is exactly Anthoine2004's Eq. (4) for Allen and Vincenti's correction (our check).

**Verification by model size** (p. 362, Figs. 9.20–9.21): "By testing models of several sizes at the same Reynolds
number, data were obtained that have yielded an excellent check on the wall corrections presented."

### Limitations and caveats

- This chapter is two-dimensional (bodies spanning the tunnel). The sphere is a three-dimensional problem (Chapter 10).
- The constants are for airfoils and for tunnels of the 7 × 10 ft type; λ₂ for shapes other than airfoils comes from
  Fig. 9.16, which was not read in detail.

### What it suggests for this project [Proposed]

1. **Order of corrections:** remove the sting's tare and interference and any flow nonuniformity first, then apply the
   wall corrections, each estimated separately and added (p. 330).
2. **Use the effective test-section area.** With a 100 mm section, a displacement thickness of about 1 mm on each wall
   reduces C by about 4 % (our arithmetic for illustration; the real thickness is unknown and must be measured with the
   probe near the walls during the flow map). That raises the blockage ratio and its correction by the same 4 %.
3. **A slightly expanding test section** cancels the falling static pressure (p. 350). Measure the gradient in the
   first printed test section; if it is significant, flaring the walls slightly in a reprint is the book's remedy (our
   suggestion).
4. **For a later cylinder test** (if a full-span rod is ever tested; see the 2026-11-10 session log): solid blockage
   (π²/3)(a/h)², and Maskell's wake blockage (d/h)/2 × c_du, are the starting formulas. Anthoine2004 reviews these
   corrections for cylinders specifically.
5. **The matched-Reynolds-number test of two ball sizes is the book's own verification method** (p. 362), which
   supports the plan to run the 3/4 in ball at 13 m/s against the 1 in ball at 9.75 m/s
   ([experimental setup](../../docs/experimental_setup.md), validation sphere row).
6. **Correct the Reynolds number too**: Re_c = Re_u(1 + ε) (Eq. 9.30; Eq. 10.63 gives the same for velocity). For the
   3/4 in ball, ε_T ≈ 2 % raises Re by about 2 %, which moves the Brown2003 reference C_D by only about 0.2 % (using
   d ln C_D / d ln Re ≈ 0.10 from the 2026-11-19 session; our arithmetic). Small, but free to apply.

---

## Chapter 10: Boundary corrections II, three-dimensional flow (pp. 367–427, PDF 378–438)

Read: §§10.1–10.3 (buoyancy, solid blockage, wake blockage) in full, with every equation and Figs. 10.1–10.3 checked
on the page images; §10.9 (summary of the closed-test-section data reduction) read, Eqs. (10.61)–(10.63) checked on the
image; §10.10 (open jet) read. §§10.4–10.8 (streamline curvature, downwash, flow behind the wing) skimmed: they concern
lift, and a sphere has none.

### What it says

**Buoyancy, three-dimensional** (§10.1, pp. 367–368, PDF 378–379). Including the "squeezing" of the streamlines,
Glauert's total correction is **ΔD_B = −(π/4) λ₃ t³ (dp/dl)** (Eq. 10.1), where t is the body's maximum thickness and
λ₃ a body shape factor from Fig. 10.1 (λ₃ against fineness ratio l/t for a Rankine ovoid, a spheroid and a streamline
body, l/t from 0 to 10). Example 10.1: a body with l/t = 3.98, λ₃ = 2.2 (estimated), t = 2.26 ft, gradient
−0.026 lb/ft² per ft: ΔD_B = 0.519 lb. "Approximating the integral too grossly may change the buoyancy drag as much as
20 %, but this in turn would be about 1 % of the total model drag for models of ordinary dimensions."

**Solid blockage** (§10.2, pp. 368–370, PDF 379–381).

- Wing: ε_sb,W = K₁τ₁(wing volume)/C^{3/2} (Eq. 10.2).
- **Body of revolution: ε_sb,B = K₃τ₁(body volume)/C^{3/2}** (Eq. 10.3). K₃ comes from Fig. 10.2, which covers
  streamline bodies with d/l from 0.04 to 0.24 only. τ₁ comes from Fig. 10.3, using span ratio 0 for bodies of
  revolution; it has curves for circular sections and for rectangular sections with B/H = 1.00, 1.43, 1.50, 1.75 and
  2.0.
- **Thom's short form: ε_sb = K(model volume)/C^{3/2}** (Eq. 10.4), with K = 0.90 for a three-dimensional wing and
  **0.96 for a body of revolution.** A streamline body of revolution has a volume of about 0.45 l d².
- In a round closed tunnel, the velocity increment at the wall is about 2.2 times that on the centreline for bodies of
  revolution (p. 370).
- For open jets, take one-fourth of the closed-section value, "normally … negligible" (p. 370).

**Wake blockage** (§10.3, pp. 370–375, PDF 381–386).

- Streamlined flow (wake as a source): **ε_wb = (S/4C) C_Du** (Eq. 10.5), or q_wb/q_u = 1 + (S/2C) C_Du (Eq. 10.6),
  where S is the model reference area and C_Du the uncorrected drag coefficient. The wake also puts the body in a
  pressure gradient (Eqs. 10.7–10.8), usually negligible.
- **Maskell, separated flow:** **ε_wb,t = (S/4C) C_D0 + (5S/4C)(C_Du − C_Di − C_D0)** (Eq. 10.9), so
  q_c/q_u = 1 + (S/2C) C_D0 + (5S/2C)(C_Du − C_Di − C_D0) (Eq. 10.10). C_D0 is the part of the drag from unseparated
  flow and C_Di the induced (lift-dependent) drag; the last bracket is the separated drag C_Ds, set to zero if data
  scatter makes it negative (p. 374).
- Maskell's three points (p. 370): wake blockage acts like testing at a higher speed; wakes tend to axial symmetry, so
  one correction serves almost all three-dimensional models; and the wake induces a streamwise pressure gradient.
- **"Maskell should be consulted for bluff models that have a substantial separated wake at α = 0, for a correction
  based on base pressure then becomes necessary"** (p. 372).
- Fig. 10.5: the blockage "constant" falls from over 2.5 for high-aspect-ratio plates to about 1.0 for two-dimensional
  ones. "There also is some controversy about the 5/4 factor": Maskell found it from flat plates normal to the flow,
  which separate across the whole span, so it may be too large for wings (p. 374).
- **Combining:** ε_t = ε_sb + ε_wb,t (Eq. 10.21). "When all is lost," for an unusual shape, ε_t = ¼ × model frontal
  area / test-section area (Eq. 10.22).
- **Blockage applies to everything in the test section** (p. 375): if the image system is used to find tare and
  interference, the blockage of the supports and shields is included automatically and removed with T + I. Without an
  image system, ε_t = ε_model+struts + ε_windshields, or "make a pitot-static survey with the windshields in, and use its
  values for 'free stream,' allowing for model blockage only in the work-up."
- **"A maximum ratio of model frontal area to test-section cross-sectional area of 7.5 % should probably be used unless
  errors of several percent can be accepted"** (p. 375).
- Measured-variable methods (Hensel 1957, Maskell 1965, Hackett–Wilsden, Ashill–Keating) are most useful "when
  significant and difficult-to-predict wake effects are present" (p. 375).

**Data-reduction order in a closed test section** (§10.9, pp. 412–418, PDF 423–429). Raw loads → balance calibration →
angle and deflection corrections → indicated q corrected by the tunnel's q calibration (q_A) → blockage:
**ε_T = ε_sb + ε_wb (10.61), q_c = q_A (1 + ε_T)² (10.62), V_c = V_A (1 + ε_T) (10.63)** → subtract support tares and
interference, then weight tares → coefficients with q_c → lift-related wall corrections. Do one reduction by hand
("once through by hand for any wind tunnel engineer is highly recommended"), and check the final numbers independently
of the program: "It is amazing how many constants can have numbers transposed or entered in the wrong field" (p. 418).

**Open jet** (§10.10, p. 425): blockage is small but not zero, and of opposite sign.

### Limitations and caveats

- **No chart covers a sphere.** Fig. 10.2 stops at d/l = 0.24, and a sphere has d/l = 1. Thom's K = 0.96 is for bodies
  of revolution generally, not spheres. Fig. 10.1 does extend down to l/t of about 1 for λ₃.
- The 5/4 factor in Maskell's wake term is from flat plates; for a sphere, Maskell1963 gives a factor a little above
  5/2 on q for axisymmetric bodies ([Maskell1963 notes](Maskell1963.md)), which is the same 5/4 on ε.

### What it suggests for this project [Proposed; arithmetic ours]

Inputs: 100 mm square test section, C = 0.0100 m²; balls of 19.05 mm (3/4 in) and 25.4 mm (1 in), S/C = 2.85 % and
5.07 %; C_Du taken as 0.44 for illustration (Brown2003 Eq. 19 is about 0.42–0.445 at our Re).

1. **Wake blockage dominates.** A sphere's drag is almost all separated-flow drag, so with C_Di = 0 and C_D0 ≈ 0,
   Eq. (10.9) gives ε_wb ≈ (5/4)(S/C) C_Du: 0.0157 for the 3/4 in ball and 0.0279 for the 1 in ball, that is +3.1 % and
   +5.6 % in q. This is the same as Maskell's θ = 2.5 used in the [Cooper1998 notes](Cooper1998.md).
2. **Solid blockage is about a quarter of that.** V/C^{3/2} is 0.00362 (3/4 in) and 0.00858 (1 in). With Thom's
   K = 0.96, ε_sb = 0.35 % and 0.82 %. A sphere's effective volume is about 1.5 V (Cooper1998, p. 6-27), which with
   τ₁ ≈ 0.8 for a square section gives 0.43 % and 1.03 % instead. Use the spread, about ±0.1–0.2 % in ε, as a
   systematic uncertainty. Note that τ₁ for a square section is to be read from Fig. 10.3 (owner check).
3. **Total q correction:** q_c = q_A(1 + ε_sb + ε_wb)²: about +3.9 to +4.0 % for the 3/4 in ball and +7.4 to +7.8 % for
   the 1 in ball (computed with a short Python calculation, 2026-11-22). C_D falls by the same factor. Both balls are under Barlow's 7.5 % frontal-area limit (2.85 %, 5.07 %),
   but the 1 in ball's correction is twice as large and rests more on the theory, which is a further reason to treat
   the matched-Re comparison of the two balls as the check on the correction itself (as planned).
4. **Correct the q reference for the sting shield** (p. 375): calibrate S − E against the probe with the floor insert
   and sting shield in place but no ball, so the shield's own blockage is in the "free stream" q. Or, if the image
   method is used for the sting tare, the shield's blockage is removed with the tare.
5. **Horizontal buoyancy.** In coefficient form, Eq. (10.1) for a sphere gives ΔC_D,B = −λ₃ t (dp/dx)/q (our algebra,
   with S = πt²/4). For a sphere, potential-flow theory gives λ₃ = 1 (the 1.5 V effective volume; our derivation),
   to be compared with Fig. 10.1 at l/t = 1 (owner check). With an illustrative gradient of 1 % of q per 100 mm, the
   3/4 in ball would read about 0.0019 too high in C_D, about 0.4 % (our arithmetic). Measure the gradient in the empty
   tunnel and subtract ΔC_D,B.
6. **Order of the data reduction** (§10.9): raw counts → load-cell calibration → minus wind-off zero → minus sting tare
   and interference → C_D with q_c from the S − E calibration and blockage → minus buoyancy. Work one run through by hand
   and check it against the analysis script.
7. **The wall taps at the model station feel the sphere.** The velocity increment at the wall is larger than on the
   centreline (about 2.2 times in a round tunnel), so M taps must not be used for q while the ball is in; force runs
   use S − E, with E at least 1.5√C upstream (the plan already).

---

## References worth following up

- AGARD AR-304, *Quality Assessment for Wind Tunnel Testing*, 1994, and the essentially identical AIAA standard
  (ch. 12, p. 458): a fully worked uncertainty analysis for a force test.
- NIST Technical Note 1297 (resources "Wanted" item 10): the same uncertainty method in a short free document.
- E. C. Maskell, ARC R&M 3400 (already in this folder as Maskell1963): the base-pressure version of the wake correction
  for bluff bodies at zero incidence, which Barlow recommends for such bodies (p. 372).
- H. J. Allen, W. G. Vincenti, NACA Report 782, 1944: two-dimensional corrections (ch. 9; also Anthoine2004).
- Hackett, Wilsden and Lilley (ch. 9 ref. 14): the wall-signature method, reported to correlate sphere drag above and
  below the critical Reynolds number (p. 344).

## Owner check (values read from the PDF)

Printed page, then PDF page (PDF = printed + 11). Figure items are blind: read the value yourself and send it; the
notes above deliberately do not give my reading.

1. p. 241 (PDF 252): the 2 % drag error example (0.002 rad, "A = −0.9800X").
2. **Most important.** p. 242 (PDF 253), Eq. (7.13): the three numbers 978.0327, 0.0053024 and 0.0000058. Then
   p. 138 (PDF 149): is the second coefficient printed there as 0.053024 (the misprint noted above)?
3. p. 256 (PDF 267): points 1–3 on slope drift, the end-of-run zero and hysteresis.
4. **Most important.** p. 264 (PDF 275) and p. 271 (PDF 282): the two sentences saying the support tare cannot be found
   by removing the model; p. 273 (PDF 284): the three-run image method; p. 274 (PDF 285): "10 to 50 %."
5. p. 453 (PDF 464), Table 12.1, 0.95 column: the values for n = 10, 33 and 105.
6. p. 154 (PDF 165), the "near 8°" sentence; then Fig. 4.5 (blind; both axes linear): for the plain square-ended tube,
   at about what angle does the curve first rise above zero, and roughly what is C_pa at 10°?
7. p. 156 (PDF 167), Fig. 4.7 (blind; the Reynolds-number axis is logarithmic, labelled 20, 50, 100, 200, 500, 2000):
   at what Re does the square-tip curve reach 1.00? Fig. 4.8 (blind; the y-axis is in units of 10⁻³): ΔV/V at
   Z/D = 1.0, and the Z/D where it reaches zero.
8. p. 220 (PDF 231): Eq. (6.6) and the sentence "The actual calibration of the tunnel is accomplished by running the
   tunnel at various values of P_L − P_S …"; p. 221 (PDF 232): the caution against relying on wall pressures.
9. p. 222 (PDF 233): "less than 0.50 % from the mean."
10. p. 368 (PDF 379), Fig. 10.1 (blind; both axes linear, 0–10): λ₃ for the spheroid at fineness ratio 1.
    p. 369 (PDF 380), Fig. 10.3 (blind): τ₁ for B/H = 1.00 at 2b/B = 0.
11. p. 370 (PDF 381): Thom's K = 0.96 for a body of revolution; p. 372 (PDF 383), Eq. (10.9): the 5S/4C term.
12. p. 375 (PDF 386): the 7.5 % frontal-area limit and the "pitot-static survey with the windshields in" sentence;
    p. 414 (PDF 425): Eqs. (10.61)–(10.63).
13. p. 355 (PDF 366): Thom's K₁ values (0.74, 0.52) and the displacement thickness "one-sixth of the boundary layer
    thickness."
