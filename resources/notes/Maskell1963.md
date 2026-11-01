# Maskell1963: A theory of the blockage effects on bluff bodies and stalled wings in a closed wind tunnel

- Citation: E. C. Maskell, "A Theory of the Blockage Effects on Bluff Bodies and Stalled Wings in a Closed Wind
  Tunnel," Aeronautical Research Council R&M 3400, November 1963 (HMSO, 1965; replaces RAE Report Aero 2685).
- Copy in this folder: [Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf](../Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf)
  (was `arc-rm-3400.pdf`). A 27-page scan with **no text layer**, carrying a college-library stamp.
  - **PDF page = report page + 1.** PDF page 1 is the cover; report pp. 1–18 are text, tables, symbols and
    references; pp. 19–24 are Figs. 1–11; PDF pages 26–27 are HMSO back matter.
- Reviewed: 2026-10-31 by Claude Code, from page images (PyMuPDF renders). Read every text page, Tables 1–5 and
  Figs. 1–8. Equations (16) and (17) were checked at high zoom. Figs. 9–11 (stalled wings) were not examined.

## What it is

The original bluff-body blockage correction for a **closed** test section. Maskell represents the wake as a
constant-pressure "bubble" (Fig. 1) and writes a momentum balance on the flow outside it. Two empirical relations
close the theory: C_D/k² is invariant under constraint (eq. 1), and the wake contracts under constraint in proportion
to the contraction of the outer stream (eq. 12). The data are square flat plates normal to the flow in two RAE
tunnels (4 ft × 3 ft and 11½ ft × 8½ ft), plus Fage and Johansen's 2-D plates. Most of the work was done in 1955
(p. 4). Section 3 extends the theory to stalled wings.

Symbols: q = dynamic pressure; C_pb = base-pressure coefficient; k² = 1 − C_pb; S = model reference (frontal) area;
C = tunnel cross-section area; suffix c = corrected (effective).

## Key equations and numbers

**Correction formula** (eqs. 13–15, p. 10):

- q_c/q = k²/k_c² = 1 + C_D S / [(k_c² − 1) C] (eq. 13), i.e. **Δq/q = ε C_D S/C** (eq. 14), with ε = 1/(k_c² − 1)
  (eq. 15), where Δq = q_c − q.
- C_D here is the **measured** drag coefficient. Using the measured value, not the corrected one, is how the theory
  includes wake distortion (p. 10).
- If the base pressure is measured, find k_c² by iteration (eq. 16, p. 10):
  (k_c²)_n = k² {1 + C_D S / [((k_c²)_{n−1} − 1) C]}⁻¹, starting from (k_c²)₀ = k².
- Then correct the coefficients (eq. 17): (1 − C_p)/(1 − C_pc) = C_D/C_Dc = k²/k_c² = q_c/q.

**Blockage factor ε**:

- ε ≈ 5/2 for three-dimensional flow and ε ≈ 1 for two-dimensional flow (pp. 4 and 11). Summary: "a little greater
  than 5/2 for axi-symmetric flow to a little less than unity for two-dimensional flow".
- Rectangular plates, Table 5 (p. 13): ε = 2.77 (aspect ratio 1), 2.70 (2), 2.41 (5), 2.13 (10), 1.47 (20),
  0.96 (∞).
- For aspect ratios 1–10, ε = 5/2 ± 1/4. Using a constant 5/2 then errs by at most ±0.1 Δq, which is **at most
  0.01 q if Δq ≤ 0.1 q** (p. 13).
- Footnote (p. 15): "ε = 2.75 is better than ε = 2.5 for the axi-symmetric bluff-body flow."
- Base-pressure background (p. 4): for squares, circles and equilateral triangles C_pb ≈ −0.4, from Fail, Lawford
  and Eyre. That gives Δq/q ≈ (5/2) C_D S/C, about five times the classical streamline-flow correction
  Δq/q = ½ C_D0 S/C (p. 3).

**Evidence** (Tables 1–3, pp. 6, 11–12):

- Square plates in the 4 ft × 3 ft tunnel, S/C from 0.0030 to 0.0451: measured C_D rose from 1.200 to 1.335.
- Corrected, C_Dc = 1.143, 1.131 and 1.144 (mean 1.139). In the large tunnel: 1.151 and 1.154 (mean 1.152).
- C_D/k² = 0.837 throughout (eq. 3).
- The two tunnels differ by about 1 % after correction. Maskell could not explain it; he notes their turbulence
  levels differed, about 0.01 % against about 0.5 % (footnote, p. 11).
- Scatter: "as a rule, less than ± 1%"; each C_D was the mean of about ten balance readings taken over several days.

**Stalled wings, composite form** (eq. 18, p. 14):

q_c/q = 1 + ½ (S/C)(C_DR + C_D0) + (5/2)(S/C)(C_D − C_Di − C_D0)

- C_DR is the support-rig drag and C_D0 the streamline profile drag, both corrected with the classical factor ½.
- Only the separated-flow part of the drag takes the factor 5/2. C_Di is induced drag.

## Limitations and caveats

- **Well-rounded bodies may be outside the theory** (§2.6, p. 10). The theory assumes the separation point does not
  move under constraint. "It may be necessary to exclude well-rounded bluff bodies (like the circular cylinder), for
  which a small change in pressure distribution might lead to a significant movement of the separation front." **A
  sphere is such a body.** The report has no sphere data.
- **Validated on flat plates only.** These have sharp-edged, fixed separation and essentially no volume. The theory
  covers wake blockage. It does not address the model's own volume (solid blockage).
- **ε depends on base pressure.** The constant 5/2 is a generalisation from plates with C_pb ≈ −0.4. A sphere's base
  pressure is not given here.
- **Keep the correction small.** Concluding remarks (p. 16): "Experiments should be designed so as to make the
  correction small, and thus to minimize the effects of errors in the empirical parameters."
- The stalled-wing extension rests mainly on tests of the final formula (p. 15). It matters only for the later
  airfoil phase.

## What it suggests for this project [Proposed]

Not decided. Combined with Cooper1998 in [Cooper1998.md](Cooper1998.md#what-it-suggests-for-this-project-proposed).

1. **Baseline correction:** Δq/q = ε C_Du S/C with ε = 2.5, using the measured (uncorrected) C_D. For S/C = 3 %
   and C_D = 0.47 this is about 3.5 % in q, and so in C_D (our arithmetic).
2. **Keep Δq ≤ 0.1 q.** At C_D = 0.47 and ε = 2.5 that means S/C ≤ 8.5 % (our arithmetic). The sphere sizes in
   [PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#printable-contraction-sizes) (3–5 %) are inside this limit.
3. **Test the correction rather than trust it.** The theory was not validated on spheres, and §2.6 flags rounded
   bodies. Measure C_D with two or more sphere sizes (different S/C) and check that the corrected values agree. This
   is the method behind Tables 1–3, and Fage and Johansen's extrapolation to zero size (p. 3).
4. **Optional base-pressure tap:** a tap at the rear of a printed sphere would give ε = −1/C_pbc for our sphere
   (§2.6; eqs. 15–16) instead of the plate value. It needs a second pressure channel.

## References worth following up

- R. Fail, J. A. Lawford, R. C. W. Eyre, "Low-speed experiments on the wake characteristics of flat plates normal to an
  air stream," ARC R&M 3120, 1957. The wake data behind the theory.
- H. Glauert, "Wind tunnel interference on wings, bodies and airscrews," ARC R&M 1566, 1933. Classical
  (streamline-flow) corrections.
- R. C. Pankhurst, D. W. Holder, *Wind-Tunnel Technique*, Pitman, 1952, ch. 8. The ½ C_D0 S/C wake-blockage formula.
