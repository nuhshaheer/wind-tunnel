# Morel1975: Comprehensive design of axisymmetric wind tunnel contractions

- Citation: T. Morel, "Comprehensive Design of Axisymmetric Wind Tunnel Contractions," *ASME Journal of Fluids
  Engineering*, June 1975, pp. 225–233 (ASME Paper 75-FE-17). Author at General Motors Research Laboratories.
- Copy in this folder: `Morel1975_axisymmetric-contraction-design.pdf` (local only, not in Git since 2026-11-26: D-031)
  (was `morel1975.pdf`). Nine pages; printed page = PDF page + 224. The copy carries an ASME Digital Collection
  download stamp dated 08/06/2013; keep it out of a public repository.
  - **Text layer:** PDF page 1 holds two overlapping OCR copies of the same text (the "doubled characters" noted in the
    index); pages 2–9 have one copy, with garbled equations. Equations, Table 1 and Figs. 4–7 were read from page
    images.
- Reviewed: 2026-11-22 by Claude Code (Opus 5.5): full text; Eqs. (11)–(12), Table 1 and Figs. 4–7 checked on the page
  images.
- **Owner check pending** (checklist at the end).

## What they did

An inviscid, incompressible streamline-curvature calculation (General Motors' extension of Katsanis's program) of flow
through axisymmetric contractions with straight ducts 0.7 diameters long before and after (pp. 226–227). Wall shapes:
two matched power-law curves, each with its apex at one end, joined at a match point X = x_m/L (Fig. 3). Six orders
(N = 2, 2.5, 3, 3.5, 4, 5) were compared; the **cubic** was studied in detail: 124 configurations with CR = 2, 4, 9,
16 and 25; L/D₁ = 0.75, 0.85, 1.0 and 1.25; X = 0.2–0.8 (p. 228). D₁ is the inlet diameter, D₂ the exit diameter.

## Key ideas and numbers

**Why every finite contraction has two adverse pressure gradients** (p. 225). Streamline curvature makes the wall
velocity dip to a minimum just inside the inlet and peak to a maximum just inside the exit (Fig. 2). Both are followed
by a pressure rise, so the boundary layer can separate at either end; and the exit velocity profile is never quite
uniform. "In short nozzles this nonuniformity may reach 10 percent or more."

**Design parameters** (p. 227):

- Inlet: **C_pi = 1 − (V_i/U₁,∞)²**, the wall pressure rise from the inlet minimum (separation risk at the wide end).
- Exit: **C_pe = 1 − (U₂,∞/V_e)²**, from the exit maximum (exit nonuniformity).
- Exit nonuniformity: **ũ₂ = (V − U_c)₂/U₂,∞** (wall minus centreline velocity in the exit plane).
- The design reduces to choosing C_pi and C_pe; Figs. 4–6 then give L/D₁ and X for CR = 4, 9 and 16.

**Results for cubics** (pp. 228–229):

- Changing X trades C_pe against C_pi. C_p values change greatly between L/D₁ = 0.75 and 1.25, which "covers most of the
  nozzles that would be used for wind-tunnel purposes."
- Inlet pressure gradient dC_p/d(x/D₁) ≈ 0.4 C_pi/(s/D₁), where s is the distance between the points where C_p = 0.4 and
  0.8 C_pi (Fig. 7); at the exit, 0.4 C_pe D₂/s ≈ 4 C_pe (for C_pe ≤ 0.1).
- The pressure extrema lie at most about 0.25 D₁ inside the inlet and 0.25 D₂ inside the exit (Figs. 8–9).
- **ũ₂ ≈ (0.35–0.4) C_pe** for C_pe < 0.2. The nonuniformity decays in the test section to 0.45, 0.21, 0.1, 0.049 and
  0.025 of ũ₂ at x/D₂ = 0.1, 0.2, 0.3, 0.4 and 0.5, roughly as exp(−7.5 x/D₂) (theory far downstream:
  exp(−7.66 x/D₂)).
- **Surprising:** for fixed C_pi and C_pe the required L/D₁ *decreases* as CR increases, for CR above about 4 (p. 229;
  Fig. 13). Length scales with the inlet diameter, not with the diameter difference.
- A scaling analysis collapses the charts (Figs. 10–12, Eq. 10) for C_pi > 0.1, C_pe < 0.1, 2 < CR < 25,
  0.75 < L/D₁ < 1.25, 0.2 < X < 0.8.

**Separation at the wide end** (pp. 231–232). Assuming the boundary layer is turbulent, Stratford's criterion,
**C_p (x dC_p/dx)^½ = 0.35 (10⁻⁶ R_x)^0.1** (Eq. 11, with R_x = U_m x/ν "= O(10⁶)"), becomes
**C_pi = 0.7 [(x₀ + 0.9 x_i)/s]^(−1/3) (10⁻⁶ R_x)^(1/15)** (Eq. 12), where x₀ is the distance from the virtual origin of
the boundary layer (taken as the last screen) to the nozzle start. Example: x₀/D₁ = 0.3, x_i/D₁ = 0.15, s/D₁ = 0.09,
Reynolds number 10⁶ on D₁: C_pi ≈ 0.39.

**The narrow end** (p. 231). A nonuniformity of no more than 2 % is usual, which for cubics means C_pe < about 0.06.
The exit pressure rise is then too mild to separate a turbulent boundary layer, and a laminar one tends to resist
separation there; so the exit constraint is usually just ũ₂.

**Total nozzle length** (p. 231–232, Eq. 13): L_t = L + a₁D₁ + a₂D₂, counting the distorted parts of the straight ducts.
For C_pi = 0.35, a₁ > 0.2 keeps the velocity nonuniformity at the last screen under 3 %; a₂ = 0.3 reduces ũ₂ to a
tenth. "Shortening of the nozzle length L by some ΔL always results in an increase in the other two lengths."

**Other wall shapes** (Table 1, p. 232; CR = 9, L/D₁ = 1.0, X = 0.5): raising the power N raises C_pi monotonically
(0.217 at N = 2, 0.267 at 3, 0.473 at 5), C_pe has a minimum near N = 4 (0.032), and ũ₂ falls monotonically (0.0510,
0.0129, 0.0020). "The cubic is the shape which produces the lowest combination of C_pi and C_pe of all the curves."

**Conclusions worth quoting** (pp. 232–233):

- "There is not one optimum wall shape suitable for all contractions, not even for a given contraction ratio."
- "Nozzles with large contraction ratios are tolerant to any irregularities at the low velocity end … nozzles with
  smaller CR (say 4 or 5) demand that greater attention be given to the avoidance of separation."
- "It is advisable to locate the last screen at least 0.2 D₁ upstream of the nozzle." The exit nonuniformity is
  reduced to about 10 % of its exit value "within 0.3 D₂" downstream.
- Rectangular contractions: apply "with some caution" because of circumferential (corner) pressure gradients; for
  moderate aspect ratios an axisymmetric nozzle of "equivalent" diameter D_eq = 2√(A/π) gives a satisfactory estimate of
  average conditions.

## Limitations and caveats

- Inviscid, axisymmetric calculations; separation is judged by a turbulent-boundary-layer criterion that assumes
  R_x of order 10⁶.
- Only matched power-law curves were studied. The 5th-order polynomial chosen for this project (Bell1988) is a single
  polynomial with zero slope and curvature at both ends, not one of Morel's families, so the charts do not apply to it
  directly.
- No experiments in the paper beyond one comparison with an electrolytic-tank result (Fig. 2).

## What it suggests for this project [Proposed]

The planned contraction: square, 250 mm to 100 mm (CR = 6.25), about 250 mm long, 5th-order polynomial walls
([Bell1988 notes](Bell1988.md)). Equivalent diameters: D₁ = 2√(0.0625/π) = 282 mm and D₂ = 113 mm, so L/D₁ ≈ 0.89
(our arithmetic).

1. **Morel's separation criterion does not apply to this tunnel; Bell1988's does.** In the settling chamber at 13 m/s
   test speed the air moves at about 2.1 m/s, so the Reynolds number on D₁ is about 4 × 10⁴, and on a typical x₀ + x_i
   of about 0.1 m, R_x ≈ 1.4 × 10⁴, against the O(10⁶) that Stratford's criterion assumes (our arithmetic,
   ν = 1.5 × 10⁻⁵ m²/s). The boundary layer may well be laminar at the inlet. Bell and Mehta designed for exactly this
   case (small tunnels, laminar criterion), which supports keeping Bell1988 as the design basis and Morel as a
   cross-check of trends only.
2. **Trends agree with Bell1988.** Morel's Table 1 shows that flatter ends (higher N) reduce the exit nonuniformity but
   raise the inlet pressure rise; Bell1988 found the 7th-order polynomial separated at the inlet while the 5th-order did
   not. Both point to a middle choice, and the 5th-order polynomial is it.
3. **Last screen at least 0.2 D₁ before the contraction starts.** The plan has about 50 mm, which is 0.2 × the 250 mm
   side; with the equivalent diameter (282 mm) the rule gives about 56 mm (our arithmetic). Use about 60 mm at sizing;
   it adds a little to the chamber length already flagged in open question 15.
4. **Put the E taps far enough into the test section.** The exit wall-pressure peak lies within about 0.25 D₂ (28 mm)
   inside the contraction, and the nonuniformity falls to a tenth within 0.3 D₂ (34 mm) of the exit (our arithmetic).
   Place the E ring at least about 0.5 D₂ (56 mm) downstream of the contraction exit, where the wall pressure is
   settled; the S − E calibration absorbs any remaining constant offset, but a steep local gradient would make the
   reading sensitive to tap position. Similarly keep the S ring away from the first 0.25 D₁ upstream of the contraction
   inlet. Our suggestion, to be fitted with the Cooper1998 rule (E at least 1.5√C upstream of the sphere).
5. **Square section, corners.** Morel cautions about circumferential gradients in rectangular contractions. Watch the
   corners of the contraction with tufts when the tunnel first runs (also Barlow1999 ch. 6).
6. **A cross-check by chart.** Reading Figs. 4 and 5 (CR = 4 and 9) at X = 0.5 and L/D₁ between 0.85 and 1.0 brackets
   C_pi and C_pe for a cubic contraction of the same proportions (owner check item 4). With ũ₂ ≈ 0.35–0.4 C_pe, that
   gives an order of magnitude for the exit nonuniformity to compare with the flow map. It is a comparison between
   different wall families, so expect only rough agreement.

## References worth following up

- T. Morel, "Design of Two-dimensional Wind Tunnel Contractions," ASME Paper 76-WA/FE-4, 1976 (cited by Bell1988 for
  the exit-nonuniformity decay; closer to a square section than this paper).
- B. S. Stratford, "The Prediction of Separation of the Turbulent Boundary Layer," *J. Fluid Mech.* 5, 1959, pp. 1–16.

## Owner check (values read from the PDF)

Printed page, then PDF page. Figures are linear on both axes.

1. p. 227 (PDF 3), right column: the definitions of C_pe and C_pi, and of ũ₂.
2. p. 228 (PDF 4), right column: "ũ₂ = (0.35 ÷ 0.4) C_pe", and the decay list "0.45, 0.21, 0.1, 0.049, 0.025 of ũ₂ in
   the distance x/D₂ = 0.1, 0.2, 0.3, 0.4, 0.5" (continues onto p. 229).
3. p. 231 (PDF 7), Eqs. (11) and (12), and the worked example ending "= 0.39".
4. **Most important.** p. 228 (PDF 4), Figs. 4 (CR = 4) and 5 (CR = 9). Read blind: at X = 0.5, what are C_pi (solid
   lines, left axis) and C_pe (dashed lines, right axis) for L/D₁ = 0.85 and for L/D₁ = 1? Note that the two axes have
   different scales (left 0–0.5, right 0–0.10).
5. p. 232 (PDF 8), Table 1: the C_pi, C_pe and ũ₂ values for N = 2, 3 and 5 (first row of each).
6. p. 232 (PDF 8), conclusion 6: "at least 0.2 D₁ upstream" and "within 0.3 D₂".
