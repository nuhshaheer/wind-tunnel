# Abdelhamed2014: Design optimization of three dimensional geometry of wind tunnel contraction

- Citation: A. S. Abdelhamed, Y. El-S. Yassen, M. M. ElSakka (Port-Said University, Egypt), "Design optimization of
  three dimensional geometry of wind tunnel contraction," *Ain Shams Engineering Journal*, 2014.
  doi:10.1016/j.asej.2014.09.008
- Copy in this folder: [Abdelhamed2014_wind-tunnel-contraction-optimization.pdf](../Abdelhamed2014_wind-tunnel-contraction-optimization.pdf),
  8 pages, "article in press" version (no volume or page numbers). The owner added it on 2026-10-30 as
  `Design_optimization_of_three_dimensional_geometry_-1.pdf`. Page numbers below refer to this PDF.
- Reviewed: 2026-10-30 by Claude Code: full text, and Figures 1, 3, 4, 5, 6, 10 and 11, viewed by extracting the PDF's
  embedded images. The table layout was scrambled in text extraction. Table values were assigned to columns by
  position and then cross-checked (see "Key numbers"). Figures 2, 7, 8 and 9 were not viewed.

## What they did

They redesigned the contraction of an existing open-jet blower tunnel. They used CFD with an automated
design-of-experiments optimizer, built the winning design at full scale, and compared it with a pitot-static traverse.

- **Tunnel** (p. 3, Fig. 1, dimensions in cm): two 5.5 kW centrifugal blowers. Each feeds its own leg through a
  flexible joint, then two wide-angle diffusers in series:
  - first diffuser: 36 × 50 → 50 × 100 cm over 125 cm (max angle 22.6°, area ratio 2.78);
  - second diffuser: 50 × 100 → 74 × 150 cm over 100 cm (max angle 28°, area ratio 2.22).

  A screen of porosity 0.43 sits between the diffusers and one of porosity 0.5 at the exit of the second. The legs
  merge in a 30 cm settling chamber, followed by the 150 cm contraction and a 50 cm exit section, 60 × 60 cm.
- **Old contraction:** square, 150 × 150 → 80 × 80 cm, contraction ratio (CR) 3.5. They call this lower than the
  recommended 6–9 (p. 3, citing refs 13 and 14).
- **New contraction:** square, 150 × 150 → 60 × 60 cm, CR 6.25, length L = 150 cm. That gives L / (inlet hydraulic
  diameter) = 1, "the recommended ratio" (p. 3, citing ref 14, Mehta & Bradshaw 1979).
- **Wall-profile parameterization** (p. 4, Fig. 4): the wall is plotted as y/h against x/L, where h is the inlet
  half-height. It runs from y/h = 1 at the inlet to 0.4 at the exit (= 60/150). A straight line joins the two end
  points, and three parameters describe the wall relative to it:
  - **a**: height of the concave (upstream) part above the line, as a fraction of h. Drawn at x/L = 0.2 in Fig. 4.
  - **b**: depth of the convex (downstream) part below the line, as a fraction of h. Drawn at x/L = 0.7.
  - **c**: x/L of the inflection point, where the wall crosses the line.

  In Fig. 4 the wall is flat (zero slope) at both ends. The text does not say what kind of curve joins the points or
  whether the a and b stations are fixed at 0.2 and 0.7. The method is cited to ref 15 (Con & Rick, AIAA 2005).
- **Objective:** maximize exit-plane uniformity, Uni_ex = U_mean / U_max (Eq. 1, p. 4). Absence of separation was
  judged by a positive minimum wall shear τ_min on the contraction.
- **CFD** (pp. 4–5): ANSYS Fluent 14, pressure-based segregated solver, QUICK discretization, SST k-ω turbulence model.
  One quarter of the tunnel was modeled using two symmetry planes, on a hexahedral mesh of 254,259 cells. Inlet
  12 m/s; outlet at atmospheric static pressure. Screens were porous-jump boundaries with C2 = 218.875 and 142 m⁻¹,
  from the screen loss coefficient k = 0.71 (1 − β) / β² (β = porosity; refs 16, 17). The authors say the mesh is not
  fine enough near the wall to resolve the boundary layer.
- **Optimization** (pp. 6–7): enhanced rotatable central composite design, 29 sample points at 5 levels.
  Non-parametric regression response surface. "Screening" of 10,000 samples to find the best candidates, then CFD
  re-runs of the top three to verify them.
- **Experiment** (p. 3): 6 mm pitot-static tube on a slide traverse at the contraction exit. 30 points at 1 cm
  spacing, plus three near-wall points at 2 mm spacing, the nearest 4 mm from the wall. Re = 4.8×10⁵. Mean-velocity
  uncertainty ±4.8 % at 95 % confidence (root-sum-square).

## Key numbers

Table 1 (p. 6), optimization candidates. "Pred." is the response-surface prediction; "CFD" is the verification run.
τ_min in Pa (the nomenclature gives N/m²).

| Candidate | a | b | c | Uni_ex pred. | Uni_ex CFD | τ_min pred. | τ_min CFD |
|---|---|---|---|---|---|---|---|
| A | 0.088835 | 0.036637 | 0.325706 | 0.979834 | 0.981661 | 0.003984 | 0.005793 |
| B | 0.087155 | 0.034527 | 0.34500 | 0.979716 | 0.981292 | 0.004430 | 0.006586 |
| **C (chosen)** | **0.066435** | **0.035758** | **0.414229** | 0.980373 | 0.980839 | 0.010024 | 0.009724 |

Table 2 (p. 7), boundary layer at the exit of the test section:

| Quantity | Old design (CFD) | New design (CFD) | New design (experiment) |
|---|---|---|---|
| Half hydraulic diameter Dh/2 (m) | 0.4 | 0.3 | 0.3 |
| Maximum velocity (m/s) | 6.82286 | 12.1956 | 12.11892 |
| 2δ/Dh | 0.181188 | 0.148143 | 0.11128 |
| Boundary-layer thickness δ (m) | 0.072475 | 0.044443 | 0.033384 |
| Displacement thickness δ* (m) | 0.009713 | 0.007492 | 0.002911 |
| Momentum thickness θ (m) | 0.004984 | 0.003567 | 0.002339 |
| Re_θ | 2168.8 | 2774.5 | 1807.6 |

Reported findings:

- The CFD shows no separation (positive τ_min everywhere; Fig. 11 scale minimum 9.9×10⁻³ Pa). The authors also say
  there are no Görtler vortices (pp. 6–7).
- Uniformity peaks with the inflection at 42 % of the length, against a recommended 40 % (Fig. 8(4), p. 7).
  Conclusion: the best result comes "when the point of inflection was located as far downstream as possible" (p. 8).
- Predicted and measured exit profiles agree within about ±2 % (Fig. 10, p. 7).
- The new design cuts boundary-layer thickness by 38.68 % and momentum thickness by 28.43 % compared with the old one
  (CFD, p. 7).
- The whole study took less than a week (p. 8).

Cross-checks of the transcription (our arithmetic):

- 1 − 0.044443/0.072475 = 38.68 % and 1 − 0.003567/0.004984 = 28.43 %. These match the text, which confirms the Table 2
  columns.
- Candidate C's c = 0.414 matches the "42 %" in the text, and its verified τ_min of 0.0097 Pa matches the 9.9×10⁻³ Pa
  minimum in Fig. 11.
- Re = 12 m/s × 0.6 m / (1.5×10⁻⁵ m²/s) = 4.8×10⁵, so the reported Re is consistent with 12 m/s and the 0.6 m
  section width. The paper does not state the length scale.
- k / C2 = 10.0 mm for both screens. The porous-jump thickness was therefore probably 10 mm; the paper does not state it.

Read from the figures (approximate):

- In Fig. 10, measured and CFD U/U_max at the exit mid-plane stay within about 1 % of 1.0 for y/h > 0.15. The nearest
  measured point is about 0.85.
- The 30 × 1 cm traverse spans 30 cm, which is one half-width, so the traverse probably ran from the wall to the
  centreline (our reading).

## Limitations and caveats

- One tunnel, one speed (12 m/s), one optimization objective. "Optimal" here means the most uniform exit profile among
  shapes of this three-parameter family, at this contraction ratio.
- The authors say the near-wall mesh does not resolve the boundary layer, and the CFD boundary layer is thicker than
  the measured one (δ 44 mm vs 33 mm).
- The "no Görtler vortices" claim rests on RANS CFD. The paper's own introduction (p. 2) says CFD at this level is
  "typically insufficient" to detect longitudinal vortices.
- The measurements are a single mid-plane traverse of mean velocity. No turbulence intensity was reported, although
  controlling turbulence is one of the stated aims.
- The uniformity metric (U_mean / U_max over the exit plane) is coarse: all three candidates score about 0.98.
- The exact wall equation is not given, so the profile cannot be reproduced exactly from this paper alone.
- The tunnel is much larger than ours (60 cm section, 11 kW). The ratios are non-dimensional, but the Reynolds number
  will be lower in a small tunnel, so the boundary layers will be relatively thicker. Their boundary-layer numbers
  should not be scaled down directly.

## What it suggests for this project [Proposed]

Nothing here is decided. These are inputs to build step 1 (sizing the contraction and test section).

1. **Contraction ratio 6–9.** CR 6.25 has a practical advantage: for a square section the exit is at y/h = 1/√6.25 =
   0.4, exactly the paper's case, so candidate C's a, b and c can be reused without change. At a different CR the exit
   y/h changes, and their optimum may not carry over.
2. **Length about equal to the inlet width** (L / inlet hydraulic diameter ≈ 1).
3. **Wall shape:** flat at both ends, concave then convex, inflection near x/L ≈ 0.41 (a = 0.066, b = 0.036,
   c = 0.414). A smooth curve (for example a spline) through these points would need its own check. Our
   flow-uniformity map (build step 3) is what will show whether it works. [Bell1988](Bell1988.md) offers a
   closed-form alternative (5th-order polynomial, inflection at 0.5 L); the two are compared there.
4. **A square cross-section is acceptable.** The paper (p. 2, citing ref 5) says corner secondary flows stay local when
   there is no separation. Square is also easier to 3D-print and to mount a model in.
5. **Template for the uniformity map (build step 3):** pitot-static traverse with coarse spacing in the core and fine
   spacing near the wall, reporting U/U_max and boundary-layer thickness. Probe size and spacing must be scaled down
   for a small section.
6. **Screen losses:** k = 0.71 (1 − β) / β² gives the pressure drop of each screen. This is needed to size the fan.
7. **3D printing (Bambu Lab P1S):** with CR 6.25 and L ≈ inlet width, the 256 mm build volume limits a one-piece
   contraction to about a 100 mm test section. A larger section means printing the contraction in segments.
   Estimates are in [PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#printable-contraction-sizes).

## References worth following up

- Bell & Mehta 1988, NASA CR-177488 (refs 6, 10): contraction design specifically for small low-speed tunnels.
  Now in this folder: [Bell1988](Bell1988.md). The "JIAA report TR-64" in this paper's reference list should be TR-84.
- Mehta & Bradshaw 1979 (ref 14): cited as the source of the CR 6–9 and L/D ≈ 1 rules. Now in this folder:
  [Mehta1979](Mehta1979.md). It gives CR 6–9 (p. 448) but has no explicit L/D ≈ 1 rule, although this paper
  attributes that rule to it. [Bell1988](Bell1988.md) (L/H_i ≈ 0.89–1.2) is the better source for the length.
- Con & Rick 2005, AIAA (ref 15): the profile parameterization (exact curve definition).
- Laws 1971 (ref 16); Eckert & Pfluger 1941, NACA TM 1003 (ref 17): screen pressure-drop relation.
