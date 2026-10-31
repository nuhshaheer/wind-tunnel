# Mehta1979: Design rules for small low speed wind tunnels

- Citation: R. D. Mehta, P. Bradshaw, "Design rules for small low speed wind tunnels," *The Aeronautical Journal*
  83(827), November 1979, pp. 443–449 (Technical Note, Paper No. 718). doi:10.1017/S0001924000031985
- Copy in this folder: [Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf](../Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf).
  Scanned journal pages with an OCR text layer. The owner added it on 2026-10-30 as `10.1017S0001924000031985.pdf`
  (the DOI).
  - **PDF pages 1–7 are journal pp. 443–449, this paper.** PDF page = journal page − 442.
  - **PDF pages 8–11 are an unrelated technical note** (Thomas & Dokumaci, finite elements for pre-twisted blades)
    that came with the scan. Ignore them.
- Licence: every page carries a Cambridge Core download stamp (Monash University, 27 Dec 2016) and "subject to the
  Cambridge Core terms of use". Keep it out of a public repository (D-003).
- Reviewed: 2026-10-30 by Claude Code. Read the full text. Checked against page images: every formula and Figs. 1(b),
  3 and 4. Figs. 1(a) and 2 were only glanced at. The OCR garbles most formulas; use the page images.

## What it is

A short design guide for small open-circuit **blower** tunnels (fan at the inlet), covering every component: fan,
screens, diffusers, corner vanes, honeycomb, settling chamber, contraction, working section and power estimate. It
is based on data from more than a hundred successful designs and the authors' own experiments (details in Mehta 1977
and 1978). Fig. 1(b) (p. 444) shows the layout:

centrifugal blower → flexible coupling → wide-angle diffuser with screens → settling chamber (honeycomb + screens) →
contraction → working section → optional exit diffuser.

## Rules by component

**Tunnel type** (p. 443)

- An open-circuit blower tunnel can perform well while saving space and cost. It also suffers less from temperature
  drift, and the fan is not disturbed by the working-section flow.
- It needs free room around it: "an open-circuit tunnel in a room is really a closed-circuit tunnel with a
  poorly-designed return leg".
- A centrifugal blower is preferable to an axial fan because it copes with large changes in load. The only advantage
  of a suction tunnel is "dubious".
- Small blower tunnels often omit the exit diffuser, at the cost of a power factor above 1.

**Fans** (pp. 443–445)

- Commercial single-inlet centrifugal blowers with backward-facing impellers are adequate.
- Fit an inlet bellmouth and an inlet filter. Put large blowers on anti-vibration mounts, connected to the tunnel by a
  flexible coupling.
- Double-inlet blowers give a uniformly inclined flow, so design the wide-angle diffuser more conservatively with them.
- The ratio of tongue (splitter) height to casing height should be below 0.3.
- Choose the fan from the maker's charts so that it runs near maximum efficiency at the required flow rate and static
  pressure. Its outlet flow is least turbulent there.

**Screens** (p. 445)

- K is the pressure drop divided by the dynamic pressure; β is the open-area ratio.
- A screen with K ≈ 2 removes nearly all longitudinal mean-velocity variation.
- For a given β, a finer mesh is better at reducing existing turbulence.
- Screens with β < 0.57 produce instabilities: jets coalesce into longitudinal vortices that persist through the
  contraction. Uneven weave and wrinkles make this worse. Inspect and clean screens regularly.
- Wieghardt's formula: K = 6.5 [(1 − β)/β²] (U d / β ν)^(−1/3), where d is the wire diameter. K falls with speed up to
  U d / β ν ≈ 600 and is constant beyond that. Collar's K = 0.9 (1 − β)/β² usually overestimates K at high Re. Both are
  printed as "[1 − β/β²]"; the standard form, also used in Abdelhamed2014, is (1 − β)/β².
- Inclined screens: K_θ = K cos^m θ, with m = 1.0 for β ≈ 0.6 and m ≈ 1.4 for β ≈ 0.3.
- Flow deflection α (outlet angle / inlet angle) = A + B/√(1 + K), with A = 0.66 and B = 0.31. A larger-angle formula
  uses C = 0.68, D = 0.62, E = 1.0 and F = 1.5.
- Nylon or polyester screens are acceptable when wind loads are low. They tend to wrinkle when tensioned.

**Diffusers** (pp. 445–447)

- Exit diffuser: included angle 2θ ≤ 5° for steady flow (best pressure recovery is near 10°), and area ratio ≤ about
  2.5. Unsteady pressure recovery makes the tunnel speed fluctuate.
- The wide-angle diffuser between blower and settling chamber needs boundary-layer control, usually screens. Several
  screens of K below about 1.5 work better than one strong one. Its job is to save length; its net pressure rise is
  slightly negative.
  - Design chart Fig. 3 (p. 446): area ratio A against 2θ, with boundaries for 0–3 screens. Each extra screen allows
    a wider angle. Read values from the figure itself.
  - Fig. 4: the screens' total K must satisfy A < 1.14 K_sum + 1.0. Our arithmetic: K_sum ≥ 2.6 for A = 4 and ≥ 4.4
    for A = 6.
  - Put screens where the wall angle changes suddenly, especially a fairly strong one at the diffuser entry.
    Curved screens that meet the walls at right angles help. Fillet the corners in small tunnels.

**Honeycomb** (p. 447)

- Removes swirl and lateral velocity variation if the flow yaw is below about 10°; above that the cells stall.
- Cell length should be 6–8 cell diameters.
- Cells should be smaller than the smallest lateral wavelength of the velocity variation. About 150 cells across the
  settling chamber (≈ 25,000 in total) is adequate.
- Cell flow is usually laminar; then a shorter honeycomb gives a larger net turbulence reduction. Paper honeycomb is
  adequate for small tunnels. Remove burrs from the cells.

**Settling chamber** (pp. 447–448)

- Honeycomb first, then screens. The reverse order is not recommended.
- If strong swirl is expected, put one screen before the honeycomb. A K = 1.5 screen reduces yaw or swirl angles of
  about 40° by a factor of about 0.7.
- Place the honeycomb some distance downstream of the wide-angle diffuser exit.
- The most downstream screen must have β > 0.57.
- Space screens about 0.2 settling-chamber diameters apart, and leave about 0.2 diameters between the last screen and
  the contraction entry. Closer distorts the flow through the last screen; farther adds boundary-layer growth.
- For small tunnels, rest the diffuser, screen frames and contraction on a table, clamped with drawbolts, with the
  screens in removable frames.

**Contraction** (p. 448)

- Contraction ratio 6–9 for smaller tunnels. Screen losses scale as 1/c², but large ratios cost more and risk noise
  and separation.
- Batchelor (1970) reduction factors for c ≫ 1 are the same as in Bell1988. The paper adds: "the factor of reduction
  of percentage velocity variation is given by multiplying the above expressions by 100/c". This confirms the ÷ c
  reading used in the Bell1988 notes.
- Target: exit non-uniformity typically **±½ %** outside the boundary layers. Design so that separation is just
  avoided.
- A well-designed **square** contraction is fine. Small 45° corner fillets reduce boundary-layer migration where the
  section's aspect ratio changes, but must not end abruptly in the working section.
- 2-D contractions need about 25 % more length than axisymmetric ones for the same pressure uniformity.
- Wall shape: there is no wholly satisfactory theoretical design method. "The actual form of a contraction contour is
  not very important except near the ends, and smoothness in contour shape is much more important than exact
  dimensions." Wall radii of curvature should be smaller at the narrow end, and the first and second derivatives
  should be zero, or very small, at both ends.

**Working section** (pp. 448–449)

- Flow leaving a contraction needs about 0.5 diameters to become acceptably uniform; a turbulence grid needs 10–15 mesh
  lengths. These often set the minimum working-section length.
- Tapered fillets control the streamwise pressure gradient. Removable side panels on pinned hinges help with access.
- Drag ∝ U², so a fractional velocity error doubles in the drag.

**Power factor** (p. 449)

λ = H / (½ ρ₀ U₀³ A₀), where H is the shaft power and subscript 0 means the working section. Each component's loss is
written ηΔλ (η = blower efficiency, typically 0.8), and λ = Σ ηΔλ / η.

| Loss | Formula | Paper's typical value |
|---|---|---|
| (i) Skin friction | (A₀/A)² ∫ C_f S/A dx ≈ C_f S L / A in the working section (S = perimeter, L = length) | 0.07 (C_f ≈ 0.003) |
| (ii) Screens, honeycomb, vanes | K (A₀/A)² each | 0.18: four screens with K = 1.5 (for 5–10 m/s), two of them in the wide-angle diffuser at A/A₀ = 4 and 6, plus a K = 0.5 honeycomb, c = 9. The A/A₀ = 4 screen alone is 0.094 |
| (iii) Exit-diffuser inefficiency | (1 − η_D)[1 − (A₀/A_out)²] | 0.25 for η_D = 0.7, A = 2.5 |
| (iv) Kinetic energy lost at the exit | (A₀/A_out)²; **= 1 for a blower tunnel with no exit diffuser** | 0.16 for A = 2.5 |
| Total | λ = Σ ηΔλ / η | 0.825 with an exit diffuser |

- In term (iii) the square on (A₀/A_out) is not visible in the scan, but the stated 0.25 needs it:
  0.3 × (1 − 0.16) = 0.25 (our check).
- The fan's dynamic-pressure rise is usually ignored and acts as a safety margin. Install extra power for working
  sections that are not known in advance.

## Cross-checks with the other papers (our synthesis)

- **Contraction ratio:** 6–9 here; Abdelhamed2014 cites this paper for 6–9; Bell1988 gives 6–10.
- **Square section:** all three papers say it is acceptable.
- **Wall shape:** this paper requires zero first and second derivatives at the ends. Bell1988's 5th-order polynomial
  meets that exactly. Abdelhamed2014's Fig. 4 shows zero slope at the ends; its end curvature is not stated.
- **Settling distance downstream of the contraction:** about 0.5 diameters here; Bell1988 gives 0.37 H_e for a 10 %
  residual.
- **Uniformity target:** ±½ % here; under 1 % in Bell1988.
- **Screens:** Abdelhamed2014's tunnel used screens with β = 0.43 and 0.5, both below the 0.57 limit here, and
  mentions no honeycomb. This is an observation for our design, not a criticism of their result.

## What it suggests for this project [Proposed]

Not decided. These are inputs to build step 1 and to choosing the fan.

1. **Layout:** an open-circuit blower tunnel as in Fig. 1(b), driven by a single-inlet, backward-curved centrifugal
   blower, with free room around the tunnel. The tunnel type is still Unknown in PROJECT_BACKGROUND.md.
2. **Fan sizing:** estimates from this method are in
   [PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#fan-requirement-estimates).
   - Without an exit diffuser, the fan static pressure is about 1.25 q₀ and λ ≈ 1.6.
   - With a 2.5:1 exit diffuser, the fan static pressure is about 0.66 q₀ and λ ≈ 0.8.
   - The diffuser roughly halves fan power but adds length and printing.
3. **Vibration:** anti-vibration mounts and a flexible coupling between blower and tunnel. This matters for a load
   cell measuring grams-force.
4. **Settling chamber:**
   - honeycomb with cell length 6–8 diameters and about 150 cells across (to buy or print; not decided);
   - screens about 0.2 D apart, with the last screen β > 0.57 and about 0.2 D before the contraction;
   - screens in removable frames.
5. **Contraction:** c = 6–9, with a smooth contour whose first and second derivatives are zero at both ends; Bell1988's
   5th-order polynomial fits. "Smoothness … much more important than exact dimensions" supports careful seam finishing
   on the segmented print (D-005). Consider small 45° corner fillets.
6. **Test section:** place the sphere at least about 0.5 D downstream of the contraction exit, and provide a removable
   panel for mounting the model.

## References worth following up

- R. D. Mehta, "The aerodynamic design of blower tunnels with wide-angle diffusers," *Prog. Aerospace Sci.* 18, 1977,
  p. 59. The detailed data behind these rules.
- P. Bradshaw, R. C. Pankhurst, "The design of low-speed wind tunnels," *Prog. Aerospace Sci.* 5, 1964, p. 1. Fan
  design and general tunnel design.
- D. J. Cockrell, E. Markland, "Diffuser behaviour — a review of past experimental work — relevant today," *Aircr.
  Engng* 46, 1974, p. 16. Exit-diffuser design.
- R. I. Loehrke, H. M. Nagib, "Control of free-stream turbulence by means of honeycombs," *ASME J. Fluids Engng* 98,
  1976, p. 342. Honeycomb length.
