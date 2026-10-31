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
- [Confirmed] Why it matters to the owner: of their three current projects, this is the one that shows mechanical
  engineering work in fluids, the kind of work aerospace companies hire MEs into.
- [Confirmed] After validation: an airfoil pitch attachment (servo-driven) for further testing.

Source: the original README, written 2026-10-25 and kept in [README.md](README.md).

## Requirements and constraints

- [Confirmed] Instrumentation is the owner's own: flow conditioning, pitot tube for airspeed, load cell for drag,
  signal conditioning built from an ECE kit (LM741/LM348 op-amps, LM317 regulator).
- [Confirmed] Build order: (1) size the contraction and test section, (2) flow conditioning (honeycomb and screens),
  (3) map flow uniformity with the pitot tube, (4) load cell and conditioning circuit, (5) calibrate against known
  weights, (6) sphere Cd validation run, (7) airfoil pitch attachment.
- [Confirmed] The owner has access to a Bambu Lab P1S 3D printer (stated 2026-10-30). Build volume 256 × 256 × 256 mm
  (manufacturer's published spec, not measured). Filament and material choice: unknown.
- Unknown: budget, available space, power supply, tunnel type (open-circuit suck-down vs blower), target airspeed.

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
subcritical plateau, and the reference value should come from a source that covers that Re. Choosing that
source is an open item in [TODO.md](TODO.md).

### Corrections to expect [Standard]

- **Support (sting) drag:** the load cell measures the sphere plus its mount. Measure the mount alone and subtract it.
- **Blockage:** a model in a closed test section speeds up the local flow and inflates measured drag. Keep frontal
  area small relative to the test-section area (a few percent) or apply a blockage correction.
- **Zero drift and temperature:** HX711 and load-cell zero drift. Tare immediately before each run, and record a
  wind-off zero after it.
- **Flow non-uniformity and turbulence:** the reason for honeycomb, screens and contraction. Build step 3 (uniformity map) quantifies it.

## Order-of-magnitude estimates

**[Assumption] values, not measurements:** ρ = 1.20 kg/m³, μ = 1.81×10⁻⁵ Pa·s, C_D = 0.47, and a 300 mm × 300 mm
test section used only to illustrate blockage. Computed 2026-10-29 with a short Python calculation (formulas above).

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
  D-005, 2026-10-30). The test-section size is not yet chosen.
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

## Measurement and analysis approach [Proposed]

1. Measure ambient p and T each session to compute ρ (instrument not chosen).
2. Map test-section velocity uniformity with the pitot tube before force testing (build step 3).
3. Calibrate the load cell with known masses across the expected force range (build step 5). Fit counts → newtons
   and record residuals.
4. For each speed: wind-off tare → wind-on average → wind-off zero; repeat runs; subtract mount drag; compute C_D with uncertainty.
5. Keep raw logs untouched in `data/raw/`; do all conversions in scripts (see [data/README.md](data/README.md)).

## Known sources of uncertainty

Pressure-sensor offset and drift; load-cell creep and temperature drift; mount (sting) drag and interference; blockage;
flow non-uniformity and turbulence intensity; sphere diameter and surface finish; ρ from ambient conditions; vibration
from the fan coupling into the balance. None has been quantified yet.

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

### Not yet reviewed

These are standard sources suggested as starting points. Move each to "Reviewed" (with the relevant page or figure,
and notes in `resources/`) when it is actually used. More candidates are listed under "Wanted" in
[resources/README.md](resources/README.md).

- J. B. Barlow, W. H. Rae, A. Pope, *Low-Speed Wind Tunnel Testing*, 3rd ed., Wiley, 1999. Tunnel design, corrections, blockage.
- E. Achenbach, "Experiments on the flow past spheres at very high Reynolds numbers," *Journal of Fluid Mechanics*
  54, 1972, pp. 565–575. Sphere drag and the drag crisis. Its abstract (checked online 2026-10-30) gives the range
  5×10⁴ ≤ Re ≤ 6×10⁶. That covers only the top of this project's planned Re (roughly 10⁴–10⁵ in the estimates
  above), so it cannot be the only C_D reference. Candidates covering 10⁴–10⁵ are listed under "Wanted" in
  [resources/README.md](resources/README.md).
- F. M. White, *Fluid Mechanics* (any recent edition). Sphere C_D vs Re chart and pitot-static theory.

## Lessons learned

None recorded yet. Add lasting lessons here (with a link to the session log where they were learned).
