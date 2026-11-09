# Project Background

Long-term context that changes slowly. Current state lives in [PROJECT_STATUS.md](PROJECT_STATUS.md).
Every statement is tagged: **[Confirmed]** = stated by the project owner or verified in this repo;
**[Standard]** = textbook physics; **[Assumption]** = a value chosen only to make an estimate;
**[Proposed]** = an approach not yet decided.

## Motivation and intended outcome

- [Confirmed] Goal: measure drag, and prove the tunnel reads true.
- [Confirmed] Approach: before trusting any other result, validate the tunnel on something with a known answer,
  the drag coefficient of a sphere (about 0.47). The owner compares this to "the 100 MΩ resistor on the STM": checking
  an instrument against a known reference before trusting it.
- [Confirmed] Deliverable: the measured Cd of a sphere compared against the published value of about 0.47.
  - Refined 2026-11-02 ([D-009](DECISIONS.md), Accepted by the owner): the published value depends on Re. At the
    planned Re it is about 0.42–0.445.
  - The comparison is with Brown and Lawler (2003) Eq. (19) at each run's Re, with a band of about ±10 %, plus a check
    that C_D rises with Re as predicted ([below](#why-reynolds-number-matters-for-the-validation-standard)).
- [Confirmed] Why it matters to the owner: of their three current projects, this is the one that shows mechanical
  engineering work in fluids, the kind of work aerospace companies hire MEs into.
- [Confirmed] After validation: an airfoil pitch attachment (servo-driven, in the original README) for further
  testing. On 2026-11-01 the owner switched to **preset angles of attack**: their sketch notes that a pivoting airfoil
  would ruin the force measurement.

Source: the original README, written 2026-10-25 and kept in [README.md](README.md).

## Requirements and constraints

- [Confirmed] Instrumentation is the owner's own: flow conditioning, pitot tube for airspeed, load cell for drag,
  signal conditioning built from an ECE kit (LM741/LM348 op-amps, LM317 regulator). The whole kit (WPI ECE2010
  Lab 2) is listed from its packing list in [docs/experimental_setup.md](docs/experimental_setup.md#parts-on-hand)
  (2026-11-01).
- [Confirmed] The owner wants to design the sensor interface circuit: design it, maybe test it on a breadboard, then
  turn it into a PCB (2026-11-01).
- [Confirmed] Microcontroller on hand: an Elegoo board the owner identifies as a Mega 2560 R3 by its appearance
  (2026-11-01). Its main chip reads ATMEGA2560, and a Blink upload worked on 2026-11-02
  ([PROJECT_STATUS.md](PROJECT_STATUS.md) §3).
- [Confirmed] Build order: (1) size the contraction and test section, (2) flow conditioning (honeycomb and screens),
  (3) map flow uniformity with the pitot tube, (4) load cell and conditioning circuit, (5) calibrate against known
  weights, (6) sphere Cd validation run, (7) airfoil pitch attachment.
- [Confirmed] The owner has access to a Bambu Lab P1S 3D printer (stated 2026-10-30). Build volume 256 × 256 × 256 mm
  (manufacturer's published spec, not measured). Filament: PLA and PETG-CF on hand, amounts unknown, with a
  hardened-steel nozzle (owner, 2026-11-09). Proposed: PLA shells, PETG-CF for clamped or loaded parts
  ([docs/buy_list.md](docs/buy_list.md) §2).
- [Confirmed] Tunnel type: open-circuit **blower**, fan at the front (owner, 2026-11-01; [D-007](DECISIONS.md)).
- [Confirmed] Test section **100 mm × 100 mm** (owner, 2026-11-01; [D-008](DECISIONS.md)). Length: the owner first
  wanted about 1 m in total including the fan, then allowed more. Estimated 1.15–1.3 m with a 6-inch fan
  ([Tunnel length budget](#tunnel-length-budget)).
- [Confirmed] Model access: one test chamber. The top and/or side acrylic panel comes off to swap the model; the
  owner proposed magnets to hold the panels (2026-11-01).
- [Confirmed] Controls: a display with a knob and a menu like the Ender 3 3D printer's, to choose what to show (drag
  force and so on) and to change the fan speed (owner, 2026-11-01). **Superseded 2026-11-08 by
  [D-012](DECISIONS.md):** no display or knob; all output goes to the laptop ("this isnt a device").
- [Confirmed] Top speed: **13 m/s target, validation runs from about 6.5 m/s** (owner, 2026-11-08;
  [D-010](DECISIONS.md)). Not a must-have: 11–12 m/s still validates, with less force.
- [Confirmed] The full parts list, with what each part does and its price, is [docs/buy_list.md](docs/buy_list.md)
  (2026-11-08/09). The owner builds the circuit on a breadboard first, then orders a PCB with sockets (2026-11-09).
- [Confirmed] Tools on hand: a multimeter, a soldering station, a bench power supply (maximum voltage and current
  unknown) and access to a workbench (owner, 2026-11-01).
- [Confirmed] Budget: "I don't really have a budget" (owner, 2026-11-01). The owner compared this project with typical
  projects under $50, which have no load cell. The agent's first estimate (2026-11-01) was about $120–200, mostly the
  fan and the pressure sensor. The full buy list (2026-11-08/09) comes to about $315–505 before tax and shipping
  ([docs/buy_list.md](docs/buy_list.md); still to buy: [docs/shopping_list.md](docs/shopping_list.md)). On the fan, the owner is price-conscious: after the AC Infinity Cloudline S6
  ($99) was recommended, "im trying to find somethign more affordbale" (2026-11-05).
- Unknown: the fan model (open between the AC Infinity S6 and the VEVOR VV-GDFJ-AC6, [D-011](DECISIONS.md)), the
  bench supply's rating, the room's free length around the tunnel.

## Governing equations [Standard]

| Quantity | Equation | Notes |
|---|---|---|
| Air density | ρ = p / (R·T), R = 287.05 J/(kg·K) | Use measured ambient pressure p and temperature T. Humidity lowers ρ slightly. |
| Airspeed from pitot-static | V = √(2·Δp / ρ) | Δp = total − static pressure. A plain pitot gives total pressure only; static pressure must come from a static port. |
| Dynamic pressure | q = ½·ρ·V² | |
| Drag coefficient | C_D = F_D / (q·A) | A = πd²/4 for a sphere (frontal area). |
| Reynolds number | Re = ρ·V·d / μ | μ of air ≈ 1.8×10⁻⁵ Pa·s near room temperature. |
| Cd uncertainty (independent errors) | (δC_D/C_D)² ≈ (δF/F)² + (δq/q)² + (2·δd/d)² | Diameter error counts double because A ∝ d². |

### Why Reynolds number matters for the validation [Standard]

A smooth sphere's C_D is roughly constant (about 0.4–0.5) over a wide subcritical range, roughly 10³ < Re < 2×10⁵.
Near Re ≈ 2–3×10⁵ the "drag crisis" drops it sharply (to roughly 0.1–0.2). Free-stream turbulence and surface roughness
move the crisis to lower Re. So the comparison with "0.47" is only meaningful if the test Re sits well inside the
subcritical plateau, and the reference value should come from a source that covers that Re.

**Reference chosen 2026-11-02 ([D-009](DECISIONS.md), Accepted).** Within the "plateau", C_D still varies:

- It has a shallow minimum of about 0.39–0.40 near Re ≈ 5×10³. It then rises to about 0.47 near 10⁵ (Brown and
  Lawler's Eq. (19) gives 0.466 there).
- At the planned Re (1.3–2.5×10⁴), **Eq. (19) gives 0.42–0.445**, rising about 12 % from Re = 6.6×10³ to 2.5×10⁴.
- The published data at this Re scatter about ±8 % and sit about 7 % above Eq. (19), by our measurement of their
  Fig. 3. So the reference band is about ±10 %.
- Each run is compared with Eq. (19) at its own Re, and runs at several speeds must show the predicted rise.
- Sources and the comparison with Morrison2013 (7–11 % low here) and Roos1971 (points excluded for vibration):
  [Brown2003 notes](resources/notes/Brown2003.md), [Morrison2013 notes](resources/notes/Morrison2013.md),
  [Roos1971 notes](resources/notes/Roos1971.md).

[Assumption] The reference data come from spheres falling or towed through still fluid, with no sting and no
free-stream turbulence. The tunnel's sting, blockage and turbulence are this project's corrections or uncertainties.

### Corrections to expect [Standard]

- **Support (sting) drag:** the load cell measures the sphere plus its mount. Measure the mount alone and subtract it.
- **Blockage:** a model in a closed test section speeds up the local flow and inflates measured drag. Keep frontal
  area small relative to the test-section area (a few percent) or apply a blockage correction.
- **Zero drift and temperature:** HX711 and load-cell zero drift. Tare immediately before each run, and record a
  wind-off zero after it.
- **Flow non-uniformity and turbulence:** the reason for honeycomb, screens and contraction. Build step 3 (uniformity map) quantifies it.

### Blockage correction [Proposed]

Not decided. From [Maskell1963](resources/notes/Maskell1963.md) and [Cooper1998](resources/notes/Cooper1998.md)
(reviewed 2026-10-31). The test section is now 100 mm × 100 mm (D-008), but the sphere is not chosen, so the
correction has not been computed for the real geometry (TODO P1). Percentages below are our arithmetic for
C_D = 0.47.

- **Wake blockage (Maskell, closed test section):** q_c/q_u = C_Du/C_Dc = 1 + θ·C_Du·S/C.
  - θ = 2.5; C_Du is the measured, uncorrected drag coefficient; S is the sphere's frontal area; C is the
    test-section area.
  - The support's own drag takes the classical ½·(S/C)·C_Dr term, not θ.
  - Hackett's two-step version gives the same corrected drag within 0.1 % at S/C ≤ 5 %, so the value of θ matters
    more than the choice of method.
- **θ is uncertain for a sphere.** It was derived on flat plates (2.5–2.8); a fit for parachutes gave 1.85. Maskell
  warns that well-rounded bodies may fall outside the theory, and neither source has sphere data. The spread is about
  ±0.65 % of C_D at S/C = 3 % and ±1.1 % at 5 %.
- **Solid blockage** (the sphere's own volume) is a separate term. Using Cooper's eq. (6.16) form it is about 0.6 %
  in q at S/C = 3 % and 1.2 % at 5 %, and up to half as much again with a sphere's effective volume of 1.5 V. Confirm
  the formula in Barlow1999 ch. 9–10 before using it.
- **Check the correction experimentally:** measure two or more sphere sizes (different S/C) and confirm that the
  corrected C_D values agree.
- **Limits:** keep Δq ≤ 0.1 q (S/C ≤ about 8.5 %), preferably about 3 %. Use a closed test section; open-jet
  corrections are less developed.
- **Positions:**
  - the reference pressure reading at least 1.5√C upstream of the sphere;
  - the sphere's base at least 2√S_b, preferably 4√S_b, from the end of the test section (S_b = separated base area,
    at most S);
  - the sphere at least about 0.5 D after the contraction exit (Mehta1979).

## Order-of-magnitude estimates

**[Assumption] values, not measurements:** ρ = 1.20 kg/m³, μ = 1.81×10⁻⁵ Pa·s, C_D = 0.47, and a 300 mm × 300 mm
test section used only to illustrate blockage. Computed 2026-10-29 with a short Python calculation (formulas above).
Note added 2026-11-02: at the planned Re the reference C_D is about 0.42–0.445 (D-009). So the drag values in these
estimates, which assume 0.47, are about 5–10 % high for Re of 1–3×10⁴. That makes no difference at their precision.

| V (m/s) | q (Pa) | Sphere d (mm) | Drag (N) | Drag (gf) | Re | Blockage in 300×300 mm |
|---|---|---|---|---|---|---|
| 5 | 15 | 50 | 0.014 | 1.4 | 1.7×10⁴ | 2.2 % |
| 10 | 60 | 40 | 0.035 | 3.6 | 2.7×10⁴ | 1.4 % |
| 10 | 60 | 50 | 0.055 | 5.7 | 3.3×10⁴ | 2.2 % |
| 10 | 60 | 75 | 0.125 | 12.7 | 5.0×10⁴ | 4.9 % |
| 15 | 135 | 50 | 0.125 | 12.7 | 5.0×10⁴ | 2.2 % |
| 20 | 240 | 50 | 0.221 | 22.6 | 6.6×10⁴ | 2.2 % |
| 20 | 240 | 75 | 0.498 | 50.8 | 9.9×10⁴ | 4.9 % |

What this implies (to be confirmed during build step 1):

- Drag forces are **grams-force**. A low-capacity load cell, a stiff low-drag mount and careful zeroing matter more than resolution on paper.
- Dynamic pressure is **tens to a few hundred pascals**. At 10 m/s, a ±1 Pa pressure error is about ±0.8 % in V; at
  5 m/s a ±5 Pa error is about ±17 %. Pressure-sensor range and offset stability drive airspeed accuracy.
- All rows sit in the subcritical Re range, which is where the ~0.47 plateau applies.

### Printable contraction sizes

**[Assumption] values, not measurements.** Square sections; contraction ratio 6.25 and length = inlet width, following
[Abdelhamed2014](resources/notes/Abdelhamed2014.md); the sphere is sized for 3 % or 5 % blockage; ρ, μ and C_D as
above. Computed 2026-10-30 with a short Python calculation.

| Test section (mm) | Contraction inlet = length (mm) | Sphere d at 3 % blockage | Drag at 10 / 20 m/s (gf) | Re at 20 m/s | Sphere d at 5 % blockage | Drag at 10 / 20 m/s (gf) |
|---|---|---|---|---|---|---|
| 100 | 250 | 19.5 mm | 0.86 / 3.45 | 2.6×10⁴ | 25.2 mm | 1.44 / 5.75 |
| 120 | 300 | 23.5 mm | 1.24 / 4.97 | 3.1×10⁴ | 30.3 mm | 2.07 / 8.28 |
| 150 | 375 | 29.3 mm | 1.94 / 7.76 | 3.9×10⁴ | 37.8 mm | 3.24 / 12.94 |
| 200 | 500 | 39.1 mm | 3.45 / 13.80 | 5.2×10⁴ | 50.5 mm | 5.75 / 23.00 |

What this implies (to be confirmed during build step 1):

- With the P1S's 256 mm build volume, only the 100 mm row could be printed as a one-piece contraction, and only barely:
  a 250 mm inlet leaves about 3 mm per side for the walls and no room for a flange. Any larger section means printing
  the contraction in segments and joining them. **The owner chose a larger tunnel printed in segments** (DECISIONS.md
  D-005, 2026-10-30). The owner later chose the 100 mm section anyway (D-008, 2026-11-01). It is still printed in
  segments, because the 250 mm inlet leaves no room for walls and flanges.
- Drag scales with the square of the test-section size at fixed blockage. A 100 mm section gives about 1 gf at
  10 m/s, which makes the load cell, its mount and zero drift the hardest part of the measurement. The choice is
  between a small one-piece print with tiny forces and a segmented print with larger, easier-to-measure forces.

### Fan requirement estimates

**[Assumption] values, not measurements.** Method and loss terms from [Mehta1979](resources/notes/Mehta1979.md)
(p. 449). The paper's typical values are used: skin friction 0.07, plus screens and honeycomb 0.18 (four K = 1.5
screens and a K = 0.5 honeycomb at contraction ratio 9; our layout will differ). Blower efficiency 0.8, ρ = 1.20 kg/m³.

- **Open exit** (no exit diffuser): the exit kinetic-energy loss is the full q₀, so the fan static pressure is about
  1.25 q₀ and the power factor λ ≈ 1.56.
- **Exit diffuser** with area ratio 2.5: the fan static pressure is about 0.66 q₀ and λ ≈ 0.83.

Computed 2026-10-30 with a short Python calculation.

| Square test section (mm) | U (m/s) | q₀ (Pa) | Flow (m³/h) | Fan static pressure (Pa), open / diffuser | Shaft power (W), open / diffuser |
|---|---|---|---|---|---|
| 100 | 10 | 60 | 360 | 75 / 40 | 9 / 5 |
| 100 | 20 | 240 | 720 | 300 / 158 | 75 / 40 |
| 150 | 10 | 60 | 810 | 75 / 40 | 21 / 11 |
| 150 | 20 | 240 | 1620 | 300 / 158 | 169 / 89 |
| 200 | 10 | 60 | 1440 | 75 / 40 | 38 / 20 |
| 200 | 20 | 240 | 2880 | 300 / 158 | 300 / 158 |
| 250 | 10 | 60 | 2250 | 75 / 40 | 59 / 31 |
| 250 | 20 | 240 | 4500 | 300 / 158 | 469 / 248 |

What this implies (to be confirmed when the layout is chosen):

- Flow rate scales with the test-section area and the speed; power scales with the area and the speed cubed. The top
  speed drives the fan choice much more than the size does.
- An exit diffuser roughly halves the fan pressure and power, but adds length and printing.
- Recompute with the actual screen count, K values and contraction ratio once they are chosen. Add a power margin,
  as Mehta1979 advises.

### Tunnel length budget

**[Assumption] values, not measurements.** Blower layout with an open exit (D-007) and contraction ratio 6.25, so the
settling chamber is 2.5 h square. Computed 2026-11-01 with short Python calculations (session scratch scripts, not
kept; the rules below reproduce them).

Section rules:

| Section | Rule | Source |
|---|---|---|
| Wide-angle diffuser (fan outlet → settling chamber) | Equivalent cone opening at 30–45° (included angle). Assumed on 2026-11-01. **Superseded 2026-11-02 by Mehta1977 Fig. 5**: at h = 100 mm (A = 3.44), the minimum length is about 115 mm with two screens and 195 mm with one, so about 150–200 mm with two screens is proposed | [Mehta1977](resources/notes/Mehta1977.md) |
| Settling chamber | 0.6–0.8 × its width: honeycomb, screens 0.2 widths apart, the last 0.2 widths before the contraction. **Added 2026-11-02:** for full turbulence decay, at least 500 wire diameters between screens and about 50 cell diameters from the honeycomb to the first screen. That is about 230–300 mm at h = 100 mm instead of 150–200 mm | [Mehta1979](resources/notes/Mehta1979.md), [Mehta1977](resources/notes/Mehta1977.md), [Scheiman1981](resources/notes/Scheiman1981.md) |
| Contraction | 1.0 × its inlet width | [Bell1988](resources/notes/Bell1988.md), [Abdelhamed2014](resources/notes/Abdelhamed2014.md) |
| Test section | 2.7–2.9 h: 0.5 h for the flow to settle, the reference reading 1.5√C before the sphere, 4√S behind it at 3–5 % blockage | [Mehta1979](resources/notes/Mehta1979.md), [Cooper1998](resources/notes/Cooper1998.md) |
| Exit diffuser (not planned) | Area ratio 2.5 at a 5° included angle: about 7.5 h | [Mehta1979](resources/notes/Mehta1979.md) |

The table below was computed on 2026-11-01 with the original two rules. For h = 100 mm, the 2026-11-02 changes roughly
cancel: the diffuser is shorter and the chamber possibly longer. Recompute at the sizing task.

Fan outlets assumed: 6-inch (152 mm) for h ≤ 120 mm, 8-inch for 150 mm, 10-inch for 200 mm. The 6-inch fan's body
is about 320 mm long (listings for the AC Infinity Cloudline S6 give 12.6 in); the larger fans' lengths are not
known. Sphere d = 0.2 h (3.1 % blockage), C_D = 0.47, ρ = 1.20 kg/m³.

| Test section h (mm) | Settling chamber (mm) | Fan outlet to exit (mm) | Total with fan | Sphere d (mm) | Drag at 10 / 15 m/s (gf) |
|---|---|---|---|---|---|
| 80 | 200 | 625–729 | 0.95–1.05 m | 16 | 0.58 / 1.31 |
| **100 (chosen, D-008)** | 250 | 827–983 | **1.15–1.30 m** | 20 | 0.90 / 2.03 |
| 120 | 300 | 1029–1236 | 1.35–1.56 m | 24 | 1.30 / 2.93 |
| 150 | 375 | 1271–1521 | about 1.6–1.9 m (fan length guessed) | 30 | 2.03 / 4.58 |
| 200 | 500 | 1714–2059 | about 2.0–2.5 m (fan length guessed) | 40 | 3.6 / 8.1 |

What this implies:

- Most of the length is flow conditioning and the contraction, not the test section.
- With the same fan, a bigger section gives *less* force at top speed: the speed falls faster than the sphere's area
  grows. A bigger tunnel only gives more force with a bigger fan. Doubling the size gives four times the force for four
  times the fan power; doubling the speed gives four times the force for eight times the power.
- The sting should be as short as the layout allows: a cantilever's deflection grows with length cubed. For h =
  100 mm it is about 80–90 mm long (sphere centre 50 mm above the floor, plus 30–40 mm through the floor to the load
  cell). A 20 mm sphere sheds vortices at about 0.2 V/d, i.e. about 100 Hz at 10 m/s and 150 Hz at 15 m/s. Check the
  sting-plus-load-cell natural frequency against that once both are chosen.

Fan requirement for h = 100 mm (open exit, fan pressure 1.25–1.5 q): about 210 CFM delivered against 75–90 Pa at
10 m/s, and about 320 CFM against 170–200 Pa at 15 m/s. So look for a fan **rated about 400 CFM free air with a
listed maximum static pressure of about 500 Pa**. (Corrected 2026-11-05: this said 300–500 Pa, but by the
straight-line estimate used here, 400 CFM and 300 Pa give only about 11.5–12 m/s; see
[Top-speed trade-off](#top-speed-trade-off-proposed).) Crude top-speed estimates, assuming a straight-line fan curve
between the listed maximum pressure and the free-air flow (real curves sag, so real speeds are lower):

| Fan (listed specs) | Estimated top speed at h = 100 mm |
|---|---|
| AC Infinity Cloudline S6: 402 CFM, about 500 Pa maximum (retailer listings) | 13.1–13.7 m/s |
| Delta PFR1212UHE-SP00 120 mm 12 V server fan: 228.6 CFM, 300 Pa (DigiKey) | one fan 8.5–8.7 m/s; two side by side 12.1–12.8 m/s |

### Top-speed trade-off [Proposed]

**[Assumption] values, not measurements.** 100 mm square section, ρ = 1.20 kg/m³, μ = 1.81×10⁻⁵ Pa·s, C_D from Brown
and Lawler Eq. (19) (D-009), fan pressure 1.25–1.5 q (open exit), straight-line fan curve. Computed 2026-11-05 and
rerun 2026-11-07 with a short Python script, kept in the
[session log](docs/sessions/2026-11-07-top-speed-and-fan-search.md#5-commands-and-scripts-executed).

| Top speed | q | Sphere drag, 20 / 25 mm | Fan must deliver | Pressure sensor (full scale) | Fan power vs 13 m/s |
|---|---|---|---|---|---|
| 11 m/s | 73 Pa | 0.99 / 1.58 gf | 233 CFM at 91–109 Pa | ±125 Pa (14.4 m/s) | 0.61× |
| 12 m/s | 86 Pa | 1.19 / 1.89 gf | 254 CFM at 108–130 Pa | ±125 Pa | 0.79× |
| **13 m/s** | **101 Pa** | **1.40 / 2.23 gf** | **275 CFM at 127–152 Pa** | **±125 Pa** | **1×** |
| 15 m/s | 135 Pa | 1.89 / 3.01 gf | 318 CFM at 169–202 Pa | ±249 Pa (20.4 m/s) or ±500 Pa | 1.54× |
| 20 m/s | 240 Pa | 3.44 / 5.44 gf | 424 CFM at 300–360 Pa | ±249 Pa (barely) or ±500 Pa | 3.64× |

At the slow end: 6.5 m/s gives q = 25 Pa and 0.33 / 0.52 gf; 5 m/s gives 15 Pa and 0.19 / 0.30 gf.

Trend check (D-009), from the 20 mm sphere at 6.5 m/s (Re 8.6×10³, C_D 0.405) to the 25 mm sphere at the top speed:

| Top speed | Re at the top | Eq. (19) C_D at the top | Predicted rise |
|---|---|---|---|
| 11 m/s | 1.8×10⁴ | 0.434 | 7.2 % |
| 13 m/s | 2.2×10⁴ | 0.440 | 8.7 % |
| 15 m/s | 2.5×10⁴ | 0.445 | 9.8 % (12.1 % if the slow end is 5 m/s) |

What a fan must list to reach 13 m/s. A fan's listed maximum static pressure is at **zero flow**, with the outlet
blocked; the tunnel runs at about 150 Pa. Real curves sag below the straight line, so aim above these figures.

| Listed free-air flow | Minimum listed maximum static pressure |
|---|---|
| 350 CFM | 595–714 Pa (2.4–2.9 inH₂O) |
| 400 CFM | 407–488 Pa (1.6–2.0 inH₂O) |
| 450 CFM | 327–392 Pa (1.3–1.6 inH₂O) |
| 500 CFM | 282–339 Pa (1.1–1.4 inH₂O) |

A 400 CFM fan listed at 300 Pa gives about 11.5–12.0 m/s, at 400 Pa 12.4–12.9 m/s, and at 500 Pa 13.1–13.6 m/s. A
published fan curve is a better test: it should show at least 275 CFM at 150 Pa (0.6 inH₂O). Unit conversions:
1 inH₂O = 249.09 Pa, 1 mmH₂O = 9.807 Pa.

What this implies [Proposed by the agent, 2026-11-05; not confirmed by the owner]:

- **A top speed of 13 m/s, with validation runs from about 6.5 m/s.**
  - The trend check gains little above 13 m/s.
  - One 6-inch fan listing about 500 Pa should just reach it.
  - q fits a ±125 Pa sensor, whose smaller span should mean a smaller zero error in pascals. That matters most at the
    slow end; confirm it in the datasheets.
- **The cost is force.** Drag grows with V², so 15 m/s would give about 35 % more signal on the hardest measurement,
  for 1.5× the fan power and an 8-inch fan or two fans. The HX711's electrical noise is not the limit (about 0.002 g
  per sample with a 100 g cell, [HX711 notes](resources/notes/HX711.md)). Load-cell creep, zero drift and sting drag
  are, and they cannot be quantified until a cell is chosen.
- **If the real fan reaches only 11–12 m/s, the validation still works**, with about 30 % less force at the top and
  a smaller predicted rise.
- **Below about 6.5 m/s,** the 20 mm sphere's drag is only 0.2–0.3 gf, so fixed zero errors dominate.
- **A bigger fan can be fitted later** if the airfoil or car tests need more speed. The fan has its own stand and a
  flexible coupling; a bigger one would need a new diffuser and a wider-range pressure sensor.
- **Accepted 2026-11-08 as the target ([D-010](DECISIONS.md)).** Update 2026-11-08/09 (our arithmetic,
  [docs/buy_list.md](docs/buy_list.md) §1 and §3):
  - The real screens lose more than the 0.18 q₀ assumed above. Four or five window screens lose about 33–48 Pa at
    13 m/s, mostly the one at the fan outlet. The fan then needs about 1.55 q₀ (about 157 Pa).
  - With that, the CLOUDLINE S6 (425 CFM, 503 Pa per the maker) gives about 13.0–13.4 m/s on a straight-line curve
    (12.3–12.7 at 90 % of it). The VEVOR VV-GDFJ-AC6 (400 CFM, 300 Pa, seller's figures) gives about 11.3 m/s (10.8).
  - With the 3/4 in and 1 in balls, the trend check's predicted rise from the 3/4 in ball at 6.5 m/s to the 1 in
    ball at the top speed is 9.2 % at 13 m/s, 8.5 % at 12 m/s and 7.8 % at 11 m/s.

## Measurement and analysis approach [Proposed]

1. Measure ambient p and T each session to compute ρ (an Adafruit BME280, chosen 2026-11-08).
   - The pitot-static tube measures q directly, and C_D = F/(q·A), so ρ does not enter C_D itself.
   - ρ is needed for the airspeed V = √(2q/ρ) and for Re, which picks the reference C_D.
   - **The SDP810's reading must be corrected for ambient pressure:** q = reading × 966 mbar / p_amb (about ×0.95 near
     sea level), because Sensirion's thermal flow-through sensors are calibrated at 966 mbar
     ([Sensirion2024 notes](resources/notes/Sensirion2024.md)). So p_amb does enter C_D through q, at about 5 %.
   - The airspeed reference (2026-11-08, proposed): the contraction's pressure drop S − E, calibrated against a
     home-made total-pressure probe and wall taps at the model station ([docs/buy_list.md](docs/buy_list.md) §5).
2. Map test-section velocity uniformity with the pitot tube before force testing (build step 3).
   - During force runs, take the reference reading where its wake cannot reach the sphere: a probe off the
     centreline, or wall static taps calibrated against a pitot at the model position in the empty tunnel.
   - Place it at least 1.5√C upstream of the sphere ([Blockage correction](#blockage-correction-proposed)).
3. Mount the model on a sting that passes through a floor slot to an upright straight-bar load cell outside the
   tunnel, as Weakly2024 did. Drag bends the cell. Use a non-magnetic sting and fasteners if magnets hold panels
   nearby (2026-11-01).
   - Put only the load cell and HX711 in the closed box under the floor (the "electronics house" in the owner's
     sketch). The Arduino goes in a separate box on a cable, so handling it does not bump the balance and its heat
     does not drift the load cell (2026-11-01). No display or knob since D-012 (2026-11-08).
   - Protect the load cell when swapping models. Small bar cells are typically rated for only about 120 % of
     capacity before damage (check the chosen cell's datasheet), and screwing a model onto the sting twists and
     pushes it. Plan a sting lock (a clamp or pin that holds the sting while swapping, removed before running),
     overload stops, and a low-twist model attachment (for example a push fit with a set screw). Re-zero with the wind
     off after every swap.
4. Calibrate the load cell with known masses across the expected force range (build step 5). Apply the load in the
   drag direction at the sphere's position. Proposed 2026-11-08/09: lay the removable balance module on its side so
   gravity acts in the drag direction, and hang the masses in a pan from a printed attachment on the sting's end
   (owner's idea), with no pulley, whose friction is unknown ([docs/buy_list.md](docs/buy_list.md) §9). Fit counts →
   newtons and record residuals.
5. For each speed: wind-off tare → wind-on average → wind-off zero; repeat runs; subtract mount drag; compute C_D with uncertainty.
6. Keep raw logs untouched in `data/raw/`; do all conversions in scripts (see [data/README.md](data/README.md)).

## Known sources of uncertainty

Pressure-sensor offset and drift; load-cell creep and temperature drift; mount (sting) drag and interference; blockage;
flow non-uniformity and turbulence intensity; sphere diameter and surface finish; ρ from ambient conditions; vibration
from the fan coupling into the balance; magnetic pull between panel magnets and any ferrous part on the measured side of
the balance (added 2026-11-01). None has been quantified yet.

## References

PDFs and reading notes live in [resources/](resources/README.md).

### Reviewed

- A. S. Abdelhamed, Y. El-S. Yassen, M. M. ElSakka, "Design optimization of three dimensional geometry of wind tunnel
  contraction," *Ain Shams Engineering Journal*, 2014, doi:10.1016/j.asej.2014.09.008. Reviewed 2026-10-30. Contraction
  ratio, length and wall profile. Notes: [resources/notes/Abdelhamed2014.md](resources/notes/Abdelhamed2014.md).
- J. H. Bell, R. D. Mehta, *Contraction Design for Small Low-Speed Wind Tunnels*, NASA CR-177488, Stanford University,
  August 1988. Reviewed 2026-10-30. 5th-order-polynomial wall shape, length limits and separation for small tunnels.
  Notes: [resources/notes/Bell1988.md](resources/notes/Bell1988.md).
- R. D. Mehta, P. Bradshaw, "Design rules for small low speed wind tunnels," *The Aeronautical Journal* 83(827),
  November 1979, pp. 443–449. Reviewed 2026-10-30. Rules for every component of a small blower tunnel, plus the
  power-factor estimate. Notes: [resources/notes/Mehta1979.md](resources/notes/Mehta1979.md).
- J. Weakly, S. Ho, E. Feehery, B. D. Kothmann, C. Sung, "A Low-Cost, Adaptable System for Lift and Drag Measurement
  in an Educational Wind Tunnel," ASEE Annual Conference, 2024. Reviewed 2026-10-31. TAL220 + HX711 + Arduino balance
  with a sphere-drag check. Notes: [resources/notes/Weakly2024.md](resources/notes/Weakly2024.md).
- Avia Semiconductor, HX711 datasheet, rev. V2.0. Reviewed 2026-10-31. Notes:
  [resources/notes/HX711.md](resources/notes/HX711.md).
- E. C. Maskell, "A Theory of the Blockage Effects on Bluff Bodies and Stalled Wings in a Closed Wind Tunnel," ARC
  R&M 3400, November 1963. Reviewed 2026-10-31. The bluff-body wake-blockage correction Δq/q = ε·C_D·S/C, with ε
  about 5/2 in 3-D. Notes: [resources/notes/Maskell1963.md](resources/notes/Maskell1963.md).
- K. R. Cooper, "Bluff-Body Blockage Corrections in Closed- and Open-Test-Section Wind Tunnels," AGARD-AG-336
  chapter 6, 1998. Reviewed 2026-10-31. Maskell, Hackett's two-step version and the rules for model position along
  the test section. Notes: [resources/notes/Cooper1998.md](resources/notes/Cooper1998.md).
- F. A. Morrison, "Data Correlation for Drag Coefficient for Sphere," Michigan Technological University, 2013.
  Reviewed 2026-11-02. A single C_D(Re) fit. It is 7–11 % below Brown2003 at this project's Re, and the exam-sheet
  version has a typo. Notes: [resources/notes/Morrison2013.md](resources/notes/Morrison2013.md).
- F. W. Roos, W. W. Willmarth, "Some experimental results on sphere and disk drag," *AIAA Journal* 9(2), 1971,
  pp. 285–291. Reviewed 2026-11-02. Towing-tank sphere drag. Its points above Re = 5,500 read high (vibration).
  Notes: [resources/notes/Roos1971.md](resources/notes/Roos1971.md).
- P. P. Brown, D. F. Lawler, "Sphere Drag and Settling Velocity Revisited," *Journal of Environmental Engineering*
  129(3), 2003, pp. 222–231. Reviewed 2026-11-02. 480 curated sphere-drag points and the Eq. (19) correlation, the
  validation reference (D-009). Notes: [resources/notes/Brown2003.md](resources/notes/Brown2003.md).
- R. D. Mehta, "The aerodynamic design of blower tunnels with wide-angle diffusers," *Prog. Aerospace Sci.* 18, 1977,
  pp. 59–120. Reviewed 2026-11-02. Wide-angle diffuser charts, screens, honeycombs and settling chambers. Notes:
  [resources/notes/Mehta1977.md](resources/notes/Mehta1977.md).
- J. Scheiman, *Comparison of Experimental and Theoretical Turbulence Reduction Characteristics for Screens,
  Honeycomb, and Honeycomb-Screen Combinations*, NASA TP-1958, 1981. Reviewed 2026-11-02. Notes:
  [resources/notes/Scheiman1981.md](resources/notes/Scheiman1981.md).
- K. E. G. Wieghardt, "On the Resistance of Screens," *The Aeronautical Quarterly* 4, 1953, pp. 186–192. Reviewed
  2026-11-02. The screen pressure-drop formula. Notes: [resources/notes/Wieghardt1953.md](resources/notes/Wieghardt1953.md).
- Sensirion AG, *Datasheet SDP8xx-Digital*, Version 1.1, April 2019. Reviewed 2026-11-08. The chosen airspeed sensor
  (SDP810-125Pa). Notes: [resources/notes/SDP8xx.md](resources/notes/SDP8xx.md).
- Sensirion AG, *SDP Signal Compensation*, application note, Version 1.0, June 2024. Reviewed 2026-11-08. The
  ×966 mbar / p_amb correction. Notes: [resources/notes/Sensirion2024.md](resources/notes/Sensirion2024.md).
- HT Sensor (HTC), *TAL221 Miniature Load Cell*, datasheet. Reviewed 2026-11-08. The chosen load cell (100 g). Notes:
  [resources/notes/TAL221.md](resources/notes/TAL221.md).

### Not yet reviewed

These are standard sources suggested as starting points. Move each to "Reviewed" (with the relevant page or figure,
and notes in `resources/`) when it is actually used. More papers are in `resources/` but not yet reviewed
(Anthoine2004, Morel1975, Bradshaw1964 and the full AGARD-AG-336), and further candidates are under "Wanted"; both
are in [resources/README.md](resources/README.md).

- J. B. Barlow, W. H. Rae, A. Pope, *Low-Speed Wind Tunnel Testing*, 3rd ed., Wiley, 1999. Tunnel design, corrections,
  blockage. A local-only copy is in `resources/` (not in Git; see the index).
- E. Achenbach, "Experiments on the flow past spheres at very high Reynolds numbers," *Journal of Fluid Mechanics*
  54, 1972, pp. 565–575. Sphere drag and the drag crisis. Its abstract (checked online 2026-10-30) gives the range
  5×10⁴ ≤ Re ≤ 6×10⁶. That covers only the top of this project's planned Re (roughly 10⁴–10⁵ in the estimates
  above), so it cannot be the only C_D reference. The reference chosen for 10⁴–10⁵ is Brown2003 (D-009; Reviewed
  above). Brown and Lawler left Achenbach's data out because they were published only as graphs.
- F. M. White, *Fluid Mechanics* (any recent edition). Sphere C_D vs Re chart and pitot-static theory.

## Lessons learned

Add lasting lessons here (with a link to the session log where they were learned).

- **"Could not resolve host: github.com" can be a missing IPv4 address, not a DNS or sandbox problem** (2026-10-31,
  [session log](docs/sessions/2026-10-31-literature-review-and-design-inputs.md#8-errors-failed-approaches-and-troubleshooting)).
  - What happened: the PC's Wi-Fi had only a self-assigned IPv4 address (169.254.x.x), so only sites with IPv6
    addresses worked. Google and Microsoft loaded. GitHub, amzn.to and Stack Overflow failed in every browser and in
    Git. `nslookup` still printed GitHub's IPv4 address, which made DNS look fine.
  - Check: run `ipconfig`. If the Wi-Fi's IPv4 address starts with 169.254, the PC has no working IPv4 connection.
  - Things to try: turn the Wi-Fi off and on, restart the router, or forget and rejoin the network. Which step fixed
    it on 2026-10-31 was not recorded; `ipconfig /renew` alone had not helped.
  - The agent's fetch failed and recovered at the same times as the owner's. So when an agent reports
    `FETCH_FAILED` with "Could not resolve host", check the PC's network before blaming the agent's sandbox.
- **Take equations and numbers from page images, not from a PDF's OCR text layer** (2026-10-31,
  [session log](docs/sessions/2026-10-31-blockage-review-and-tunnel-concepts.md#8-errors-failed-approaches-and-troubleshooting)).
  - The full AGARD-AG-336 volume's text layer reads Cooper's eq. (6.6) as θ = 0.98 + …; the page shows 0.96.
  - The same layer garbles θ into "8" or "6" and renders most equations unreadably.
  - Use the text layer to find pages and read prose. Read equations, tables and numbers from page renders (PyMuPDF),
    zooming into equations.
- **`git commit` commits only staged files** (2026-11-01,
  [session log](docs/sessions/2026-11-01-parts-review-and-kit-inventory.md#8-errors-failed-approaches-and-troubleshooting)).
  The owner's `git commit` committed nothing; `git status` showed that no files had been staged with `git add`. Run the
  `git add` lines that `/wrap` gives first, then check `git status` before committing. New files are untracked, so
  `git commit -a` would miss them.
- **Amazon product pages are too large for an agent's web fetch** (2026-11-01, same session log). The page for the
  owner's fan link was 1.29 million characters, and the first part read held only the title. Take specs from the
  maker's page or other retailers' listings, or ask the owner for a screenshot of the spec section. Before trusting a
  hobby part's headline spec (CFM, "high accuracy"), check its range and pressure against this project's numbers.
- **Have the owner check values read from PDFs, and settle figure readings by measurement** (2026-11-02,
  [session log](docs/sessions/2026-11-02-cd-reference-and-flow-conditioning.md#8-errors-failed-approaches-and-troubleshooting)).
  - The owner asked to check everything read from PDFs. Give a checklist with printed and PDF page numbers. Leave
    figure readings blind, so the owner reads the figure without seeing the agent's number.
  - Common traps:
    - **log axes** read as linear (the owner twice read about 0.6 where the value was about 0.4–0.5);
    - the **raised-dot decimal** in old British papers ("5·5" = 5.5, not 5 × 5);
    - **typos in the source** (Mehta1977's reversed "60 > … > 600"; Morrison's exam-sheet "236,000");
    - PDF page numbers that differ from printed page numbers.
  - Measure figures from pixels against the figure's own tick marks. **Check the calibration on a known feature**
    (for example the Stokes line in Brown2003 Fig. 3) before trusting a reading.
- **An equipment test must show a change you caused** (2026-11-02,
  [session log](docs/sessions/2026-11-03-mega-2560-board-test.md#4-experimental-procedures-performed)). A new Mega 2560
  may already run Blink, so a blinking LED proves nothing about an upload. Changing the delay to 200 ms and seeing the
  LED speed up did. Plan later checks (sensor readings, calibrations) the same way: change something known and see
  the reading follow.
- **A datasheet's footnote conditions can hide a large correction** (2026-11-08,
  [session log](docs/sessions/2026-11-09-buy-list.md#8-errors-failed-approaches-and-troubleshooting)). The SDP8xx
  datasheet's specs hold "at absolute pressure = 966 mbar", and it points elsewhere for compensation. Sensirion's
  application note then requires ×966 / p_amb for direct differential-pressure readings, about 5 % near sea level,
  more than the sensor's whole span error. Read a sensor's application notes, not just its datasheet.
- **"Mesh" is not enough to choose a tunnel screen** (2026-11-09, same log). Check the wire diameter and the open
  area: the screen must be woven wire cloth, about 20–30 mesh, at least 58 % open.
  - Industrial "filter mesh" (McMaster's 30 × 30 has 0.012–0.013 in wire, 37–41 % open) would cost about 1.7 m/s of
    top speed and make the flow patchy.
  - A perforated sheet, even at 58 % open, makes hole-sized jets.
  - Ordinary aluminium window insect screen (18 × 16, about 66 % open, about $10 a roll) is the cheap, suitable
    choice.
- **Reading web PDFs** (2026-11-08, same log). The web-fetch agent cannot parse a binary PDF, but the harness saves it
  locally. Claude Code's Read cannot render PDF pages here (no `pdftoppm`). Extract the text and render pages with
  PyMuPDF (`python -I`, file path as an argument), then check tables and drawings on the page images. Some shop pages
  (McMaster, Zoro, TWP prices) need a browser; ask the owner to paste the table.
- **"Not committed yet" in the docs after the owner pushed is expected, not lost work** (2026-11-09,
  [session log](docs/sessions/2026-11-09-shopping-list.md#8-errors-failed-approaches-and-troubleshooting)).
  `/wrap` writes the docs before the owner commits, so a commit can never contain its own hash; the next `/wrap`
  backfills it. When `/catchup` finds this, say first that the repository is fine (local `HEAD` = `origin/main`, clean
  tree) and that only the doc text lags. The 2026-11-09 catch-up's wording ("your push isn't recorded anywhere") made
  the owner think a commit had gone missing.
- **A correlation's overall accuracy can hide a local offset** (2026-11-02, same log). Brown and Lawler's "81 % of
  points within ±5 %" is over all Re, yet at this project's Re their own data sit about 7 % above the curve. Check
  the data near the Re that matters, not just the headline fit statistic.
