# Mehta1977: The aerodynamic design of blower tunnels with wide-angle diffusers

- Citation: R. D. Mehta, "The aerodynamic design of blower tunnels with wide-angle diffusers," *Progress in Aerospace
  Sciences* 18, 1977, pp. 59–120 (Pergamon Press). Department of Aeronautics, Imperial College, London.
- Copy in this folder: [Mehta1977_blower-tunnels-wide-angle-diffusers.pdf](../Mehta1977_blower-tunnels-wide-angle-diffusers.pdf)
  (was `mehta1979.pdf`). Scanned journal pages with an OCR text layer, 62 PDF pages.
  **PDF page = journal page − 58** (PDF p. 1 = p. 59).
- Reviewed: 2026-11-02 by Claude Code. Read in full:
  - §1 (introduction) and §2 (wide-angle diffusers), pp. 61–78;
  - §3.2 (honeycombs), p. 99, and the screen-instability and screen-K passages of §3.1, pp. 92–93;
  - §5.2 (settling chambers), pp. 115–116;
  - §6 (conclusions), pp. 117–118.

  Checked on page images: Fig. 5 (p. 69, read with calibrated grid lines drawn over it), Fig. 7 (p. 71) and all of
  §6.
- **Checked by the owner against the PDF, 2026-11-02:**
  - Fig. 5 at A = 3.4, read independently: 17°, 28.5°, 46° and 53.5° for 0–3 screens. This agrees with our reading
    within 0.5°.
  - The wording of §6.1.1(ii), §6.1.2(iii) and §6.6(ii).
  - The reversed inequality in eq. (9)'s range (see Screens below). Skimmed only: the rest of §3.1 (screen theory and experiments), §4 (centrifugal blowers), §5.1 and §5.3
  (contractions, working sections) and Tables 1–9.

## What it is

The detailed review behind Mehta1979, written for open-circuit tunnels driven by a centrifugal blower. The blower
feeds a **wide-angle diffuser** (one that expands so fast that it needs boundary-layer control, usually screens) into
the settling chamber.
- The diffuser rules come from about a hundred published diffusers, successful and unsuccessful (Table 1, Figs. 5–7).
- New experiments cover screens in boundary layers and the exit flow of three centrifugal blowers.

## Key numbers

**Definitions** (p. 68, Fig. 4):

- **Diffuser angle 2θ:** the angle between straight lines joining the inlet edge to the outlet edge. If plan and
  elevation differ, use the larger.
- **Area ratio A:** outlet area / inlet area.
- **K:** the screen pressure drop / q. K_sum is the sum over all the screens in the diffuser.

**Design rules for wide-angle diffusers** (§6.1, p. 117; Figs. 5 and 7):

1. **Fig. 5 (p. 69): the limit on 2θ for a given A and number of screens.**
   - Keep to the left of the curve for that number of screens (0, 1, 2 or 3). Small separations "acceptable for tunnel
     purposes" may still occur.
   - A safe upper limit from the data is 2θ = 55° (p. 74).
   - The curves level off at large 2θ: about A = 1.1 (0 screens), 1.9 (1), 2.7 (2) and 3.1 (3) (our reading).
2. **Fig. 7 (p. 71) and §6.1.1(ii): A < 1.14·K_sum + 1.** Successful diffusers lie on the high-K side of this line.
3. **Further suggestions:**
   - Use screens if A < about 5 and 2θ < about 50°.
   - A rectangular section **with filleted corners** is fine unless pressure recovery matters.
   - **Use curved walls if 2θ > 10·(A − 1) degrees.**
   - Use curved screens.
   - Avoid sharp corners at inlet and outlet; use fairings, even "a bent piece of plywood" (p. 77).
4. **Screen positions** (pp. 75–76, eqs. 2–4).
   - Put a screen wherever the wall angle changes (p. 75): that is where separation starts.
   - For smooth walls, use a moment rule. M₁ = Σ K_r·(x_r/L) / K_sum should be about 0.5 (screens spread evenly).
     M₂ = Σ K_r·(x_r/L − ½)² / K_sum should be about 0.17 with a sharp inlet, or about 0.04 with a radiused inlet.
   - A failure example (configuration 44, p. 75): the screens were placed halfway along each section instead of at
     the angle changes, and a honeycomb straightened the flow just before the diffuser.
5. Use several screens of K between about 1 and 2 rather than one strong screen (pp. 66–67). More than about 4–5
   screens in a diffuser is undesirable (p. 73).

**Fig. 5 read at A = 3.44, this project's diffuser** (our reading of the page image, ±1°):

| Screens in the diffuser | Largest 2θ allowed |
|---|---|
| 0 | about 17° |
| 1 | about 28° |
| 2 | about 46° |
| 3 | about 53° |

**Screens** (§3.1, §6.2):

- Use metal wire gauze with square meshes (p. 117).
- **Estimating K** (p. 117; eq. (9), p. 93):
  - For U < 10 m/s, use Wieghardt's (1953) formula, K = 6.5·[(1 − β)/β²]·(Ud/βν)^(−1/3) (eq. (9), as given in the
    Mehta1979 notes).
    - Its range is printed as "60 > Ud/βν > 600 … 1.2 > U > 12 m/s", with both inequalities reversed (owner checked
      the page).
    - Our arithmetic (d = 0.4 mm, β = 0.5, ν = 1.5×10⁻⁵ m²/s): Ud/βν = 60 at 1.1 m/s and 600 at 11 m/s, so the range
      meant is 60 < Ud/βν < 600.
    - **Confirmed in the source** (2026-11-02): Wieghardt writes "for u₁d/(βν) between 60 and 600" (p. 190). His
      eq. (11) is c = 6.5·(u₁d/βν)^(−1/3) with k = c(1 − β)/β², which matches the form above
      ([Wieghardt1953 notes](Wieghardt1953.md)).
  - For U > 10 m/s, use Collar's (1939) K = C(1 − β)/β², with C = 0.9 (lower speeds) or 1.0 (higher speeds).
- **Choosing K:**
  - Several screens of lower K are better than one of the same total pressure drop.
  - K below about 1.5 gives the least variation of surface shear stress.
  - About 2.4 gives the least longitudinal velocity variation; the optimum is K ≈ 2.0 (§6.2(iii), p. 117).
- **Open-area ratio β below about 0.57** (K above about 1.6 at Re ≈ 100) gives unstable flow behind the screen. The
  pore jets coalesce into weak streamwise vortices that vary skin friction by about ±10 % (Bradshaw 1965; p. 92).
- Gauzes must be uniformly woven and free of wrinkles. Nylon or polyester mesh may be strong enough for small blower
  tunnels (p. 66).

**Honeycombs** (§3.2, p. 99; §6.3):

- They remove swirl and lateral velocity variation, provided yaw stays below about 10°; larger angles "stall" the
  cells.
- **Cell length / diameter: at least 6–8 to straighten the flow; about 7–10 is the optimum** (Loehrke and Nagib 1976:
  not more than about 10 for turbulence reduction).
- Use small cells, smaller than the smallest lateral wavelength of the velocity variation. About 150 cells per
  settling-chamber diameter is enough. Typical resistance K ≈ 0.5.
- Impregnated paper honeycomb is adequate for small tunnels; cells must be straight and uniform.

**Settling chamber** (§5.2, pp. 115–116; §6.6):

- Honeycomb first, then screens. If swirl above about 10° is expected, put one screen ahead of the honeycomb. A K = 1.5
  screen reduces yaw or swirl angles by a factor of about 0.7.
- Two or three settling-chamber screens (K ≈ 1.5) are normally enough when the wide-angle diffuser also has screens.
- **Spacing between successive screens: not less than about 500 wire diameters**, so that each screen's wire wakes
  decay before the next (p. 115; "optimum … about 500 wire diameters", p. 118).
  - Mehta1979 instead gives about 0.2 settling-chamber diameters as a spacing that "performs successfully"
    ([notes](Mehta1979.md)).
  - In a small tunnel the two rules can differ; use the larger.
- About **0.2 cross-section diameters** between the last screen and the contraction entry (Morel 1975; Laine and
  Harjumäki 1975). Shorter distorts the flow through the last screen; longer only grows boundary layers.
- Small tunnels: tack the screens to frames and clamp the diffuser, frames and contraction together with drawbolts
  on a table, so that frames can be withdrawn for cleaning (pp. 115–116).

**Blowers and their swirl** (§4, pp. 99–110, skimmed; §6.4):

- Single-inlet centrifugal blowers with backward-facing aerofoil blades are adequate. Their exit flow carries a
  vortex.
- In Mehta's tests (pp. 105–109, Figs. 17a–b):
  - swirl fed into a wide-angle diffuser (A = 2.25, 2θ = 15°) kept the wall flow attached but reversed the flow in
    the centre;
  - a paper honeycomb (9.5 mm cells) at the blower outlet removed the swirl, but the diffuser then separated
    completely on one wall;
  - two K ≈ 1.5 screens in the diffuser gave the best result.

  So "a swirling component in the blower exit flow may … be a property to be sought rather than avoided" (p. 109),
  provided screens follow. **Do not straighten the flow before a wide-angle diffuser.**
- Connect the blower to the tunnel with a flexible coupling (§6.4(v), p. 118).

**Contractions and working sections** (§6.5, §6.7):

- Contraction ratio about 6–9. An "eye-designed" or copied wall shape is adequate, and a cubic wall contour seems to
  work well.
- A rectangular working section of about √2:1 unless there is a special purpose. Use an exit diffuser only if the
  power factor matters more than flexibility of the working section.

## Limitations and caveats

- The design charts are empirical boundaries drawn around published diffusers that their designers judged successful
  (p. 69). They are "not inflexible" (p. 74), and the review is biased toward the Schubauer and Spangenberg (1948)
  rules that many designers followed (p. 68).
- The diffusers in Table 1 are mostly far larger than this project's. A 152 mm round fan outlet feeding a 250 mm
  square chamber is a round-to-square transition, which the definition of 2θ does not cover exactly.
- The data are for centrifugal blowers. An inline mixed-flow duct fan (this project's proposed fan) is not discussed.
  Its exit swirl may differ (our note).
- Wieghardt's K formula is stated for Ud/βν of 60–600. Screens in this project's settling chamber run below that (see
  below), so their real K is uncertain and probably higher than either formula gives (our inference).
- Skimmed sections (screen theory, blower data, contraction tables) may hold details not recorded here.

## What it suggests for this project [Proposed]

Our arithmetic, 2026-11-02 (short Python calculation). Assumptions: a 152 mm (6-inch) round fan outlet, a 250 mm
square settling chamber, 13 m/s in the 100 mm test section and ν = 1.5×10⁻⁵ m²/s.

1. **Fan-to-chamber diffuser:**
   - Area ratio **A = 3.44** (182 cm² → 625 cm²). It needs **K_sum ≥ 2.1** (A < 1.14·K_sum + 1).
   - **Length** (taking 2θ across the flats; the half-width grows by 49 mm). Fig. 5 allows:

     | Screens | Shortest diffuser (2θ) |
     |---|---|
     | 0 | about 335 mm (17°) |
     | 1 | about 195 mm (28°) |
     | 2 | about 115 mm (46°) |
     | 3 | about 100 mm (53°) |
   - Proposed: **two screens of K ≈ 1.1–1.5 each** (K_sum 2.2–3.0). One goes at the inlet, where the wall angle
     changes; one at the exit, or curved and normal to the walls. With them the diffuser can be about 150–200 mm
     long (2θ = 36–28°).
   - Below about 220 mm the rule "curved walls if 2θ > 10·(A − 1) = 24°" applies. So use curved (bell-shaped) walls,
     or straight walls with radiused inlet and outlet corners.
   - Fillet the four corners. Across the diagonal the expansion is about twice as steep as across the flats: 54° at
     200 mm (our arithmetic).
   - This replaces the length budget's assumed "30–45° equivalent cone" rule
     ([PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#tunnel-length-budget)) with a chart-based one. The result
     is similar: about 0.15–0.2 m with two screens.
2. **Don't put a honeycomb or flow straightener at the fan outlet.** The fan's swirl helps keep the diffuser attached
   (pp. 105–109), and the honeycomb belongs in the settling chamber. If swirl at the chamber is above about 10°, put
   one screen ahead of the honeycomb. The two diffuser screens already do that.
3. **Settling chamber:**
   - honeycomb (cell L/D about 7–10, about 150 cells across 250 mm, so cells of about 1.7 mm);
   - two or three screens with β > 0.57 (at least the last one);
   - **screen spacing of at least 500 wire diameters**: 75–100 mm for 0.15–0.2 mm wire, which is larger than
     0.2 × 250 mm = 50 mm;
   - 50 mm (0.2 D) from the last screen to the contraction.

   Check the length budget's 150–200 mm chamber against this once the screens are chosen. It may grow by roughly
   50–100 mm.
4. **Screen K at our speeds:** the settling chamber flow is only about 2.1 m/s at 13 m/s in the test section. For
   0.1–0.25 mm wire and β = 0.6, Ud/βν is about 23–58, below Wieghardt's range, so screen K is uncertain there.
   Measure the pressure drop across a sample screen if fan pressure becomes tight.
5. **Flexible coupling** between fan and diffuser (already planned), and drawbolt-clamped, removable screen frames.
   Both fit the segmented print (D-005).

## References worth following up

- K. E. G. Wieghardt, "On the resistance of screens," *Aeronautical Quarterly* 4, 1953, p. 186 (as listed in this
  paper's references): the source of eq. (9) and its valid range.
- G. B. Schubauer, W. G. Spangenberg, "Effect of screens in wide-angle diffusers," NACA-TN-1610, 1948 (as listed in
  this paper's references). The original screened-diffuser rules (eq. (5)).
- R. I. Loehrke, H. M. Nagib, "Control of free-stream turbulence by means of honeycombs: a balance between suppression
  and generation," *ASME J. Fluids Engng* 98I, 1976, p. 342 (honeycomb length).
- P. Bradshaw, "The effect of wind tunnel screens on nominally two-dimensional boundary layers," *J. Fluid Mech.* 22,
  1965, p. 679 (the β < 0.57 instability).
- R. D. Mehta, "The design of wide-angle diffusers," Imperial College Aero Report 76-03, 1976 (fuller version of §2).
- Scheiman1981 (in `resources/`): screen and honeycomb turbulence reduction.
