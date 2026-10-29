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

**Not yet reviewed by this project.** These are standard sources suggested as starting points. Mark each as reviewed
(with the relevant page or figure) when it is actually used.

- J. B. Barlow, W. H. Rae, A. Pope, *Low-Speed Wind Tunnel Testing*, 3rd ed., Wiley, 1999. Tunnel design, corrections, blockage.
- R. D. Mehta, P. Bradshaw, "Design rules for small low speed wind tunnels," *The Aeronautical Journal*, 1979. Contraction, honeycomb and screen guidance.
- E. Achenbach, "Experiments on the flow past spheres at very high Reynolds numbers," *Journal of Fluid Mechanics*, 1972. Sphere drag and the drag crisis.
- F. M. White, *Fluid Mechanics* (any recent edition). Sphere C_D vs Re chart and pitot-static theory.

## Lessons learned

None recorded yet. Add lasting lessons here (with a link to the session log where they were learned).
