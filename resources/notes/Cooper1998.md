# Cooper1998: Bluff-body blockage corrections in closed- and open-test-section wind tunnels

- Citation: K. R. Cooper, "Bluff-Body Blockage Corrections in Closed- and Open-Test-Section Wind Tunnels," chapter 6
  of B. F. R. Ewald (ed.), *Wind Tunnel Wall Correction*, AGARD-AG-336, October 1998, pp. 6-1 to 6-33.
- Copy in this folder: [Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf](../Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf).
  This is the owner's print-to-PDF extract of PDF pages 332–364 of the full volume (Ewald1998, local only).
  - **Image only, no text layer.** PDF page n = page 6-n.
  - The full volume's text layer has the prose, but its OCR garbles equations and some numbers. For example, it reads
    eq. (6.6) as "0.98 + …" where the page shows **0.96**. Take equations from the page images.
- Licence: the AGARD volume states "There are no restrictions on the distribution of this document."
- Reviewed: 2026-10-31 by Claude Code.
  - Read: all text, from the full volume's text layer.
  - Checked against page images: §§6.1.4–6.2.7, pp. 6-7 to 6-17. That covers every closed-test-section equation and
    Figs. 6.1–6.7. Eqs. (6.6) and (6.13)–(6.15b) were also checked at high zoom.
  - Our check: eq. (6.15b) was confirmed algebraically as the root of (6.15a).
  - Text only: the open-test-section methods (§§6.3 and 6.5, Mercker and Wiedemann) and §6.4.
  - Not read: Mercker's closed-section method (§6.2.6, for automotive shapes) in detail.

## What it is

A 1998 review of bluff-body blockage corrections, written largely from the automotive and wind-engineering point of
view:

- Maskell's analysis and its later forms (Cowdrey, Hackett's two-step version);
- the unsettled wake-buoyancy question;
- Mercker's automotive method;
- the effects of model position along the test section;
- open-jet corrections (Mercker and Wiedemann).

## Key equations and numbers (closed test sections)

Notation: subscript u = uncorrected (measured), c = corrected; θ is Maskell's blockage factor (Maskell1963 calls it
ε).

**Maskell** (§6.2.1, pp. 6-8 to 6-11):

- Assumptions: pressure field invariant under constraint; wake tends to axial symmetry; base pressure constant and
  equal to the static pressure on the wake boundary; wake expansion reduced in proportion to the contraction of the
  outer stream.
- (6.1): q_c/q_u = C_Du/C_D∞ = 1 + θ C_D∞ (S/C), with θ = −1/C_pbc (6.2). Wake distortion is not included and the
  equation needs iteration.
- **(6.3): q_c/q_u = C_Du/C_DcM1 = 1 + θ C_Du (S/C).** This is the full single-step correction. It is solved directly
  and is strictly a correction to drag only (p. 6-9).
- (6.4), for bodies with attached-flow drag as well:
  q_c/q_u = [1 + 2ε_wa + 2ε_ws] = [1 + ½(S/C)(C_Dr + C_D0) + θ(S/C)(C_Du − C_Di − C_D0)].
  - Only the separated-flow drag C_Dus = C_Du − C_Di − C_D0 takes θ. Support-rig drag C_Dr and skin friction C_D0
    take the classical ½.
  - When the breakdown is uncertain (automobiles), the total C_Du is often used instead of C_Dus (p. 6-9).
- (6.5): with a measured base pressure, iterate (1 − C_pbc)_i = (1 − C_pbu) / [1 + (−1/C_pbc)_{i−1} C_Dus S/C]. The
  required pressure is the separation pressure coefficient (Gould).
- **θ values:**
  - within 10 % of 2.5 for plates with aspect ratio 1–10 (square plate C_pbc ≈ −0.4);
  - fit for normal flat plates: θ = 0.96 + 1.94 exp(−0.06 AR) (6.6, Fig. 6.3);
  - 2.5 ≤ θ ≤ 2.8 for aspect ratios 1–3. The slopes in Fig. 6.2 are 2.53 for plates and 2.41 for rectangular blocks
    (p. 6-10).
- **Rounded bodies:** Farell et al. found, for **2-D circular cylinders**, that the pressure rise from peak suction to
  the base was independent of blockage up to S/C = 0.21. "This finding suggests that wall constraint has little effect
  on flow separation on bluff bodies up to this blockage level" (p. 6-10).

**Cowdrey** (§6.2.2): q_c/q_u = 1/[1 − m(S/C)] (6.7), or 1 + m'(S/C) (6.9), with m' = θ C_Du (6.10). For flat
plates, m' = 1.85 + 1.35 exp(−0.05 AR) (6.11). The empirical constant depends on body geometry.

**Hackett's two-step version** (§6.2.3, p. 6-12): splits Maskell's correction into a dynamic-pressure part and a drag
increment ΔC_DM = C_DcM1 − C_D∞.

- (6.13): C_D∞ = C_DcM1 − ΔC_DM = C_Du / [1 + θ(C_DcM1 − ΔC_DM)(S/C)].
- (6.14): C_DcM2 = (C_Du + ΔC_DM) / [1 + θ(C_DcM1 − ΔC_DM)(S/C)].
- (6.15a): ΔC_DM² − [1/(θ S/C) + 2C_DcM1] ΔC_DM − C_DcM1 (C_Du − C_DcM1) = 0. Take the negative root.
- Closed form (6.15b): ΔC_DM = C_Du / [1 + θC_Du(S/C)] + [C_Du / (2θC_Du(S/C))][1 − √(1 + 4θC_Du(S/C))].
- The text refers to "(5.15a)" in one place, a misprint for (6.15a).
- Fig. 6.4: Maskell over-corrects 3-D normal flat plates at large area ratios (S/C up to 0.25), and the two-step form
  removes the over-correction. §6.2.4 says the same holds for 2-D rectangular cylinders.

**Applications** (§6.4):

- Rectangular wing through stall, at S/C = 0.016 and 0.16 (Shindo): Maskell and the two-step method gave corrected
  drag "within a count" of each other. For example, q factor 1.232 (Maskell) against 1.212 plus ΔC_DM = −0.0126
  (Hackett) at C_Du = 0.7072.
- **Parachutes** (Macha and Buffington, six tunnels): θ = 2.5 over-corrected; fitting gave θ = 1.85. The two-step
  method returned nearly the same result (Fig. 6.15).

**Wake buoyancy and the wake-induced drag increment** (§6.2.5): unsettled.

- Classical: ΔC_Dwb = −ε_s C_Du,vis = −T (V/C^{3/2}) C_Du,vis (6.16), with T = 0.36(B/H + H/B), V = model volume
  and C_Du,vis = C_D0 + C_Dus.
- Taylor: −(ε_s + ε_w) C_Du,vis (6.17).
- Hackett: ΔC_Dwi = −C_Du,vis² S/(4C) (6.18). It agrees reasonably with the two-step ΔC_DM for a flat plate
  (Fig. 6.5).

**Model position in the test section** (§6.2.7, pp. 6-16 to 6-17; Gould's flat-plate data and SAE 940414):

- Upstream decay of the model's blockage: ε_u/ε = exp{−[(π/2)(x/√C)]²} (6.21).
- Downstream: ε_d/ε = 0.3 + 0.7 exp{−0.1 (x/√S)^1.7} (6.22).
- **Put the model at least 1.5√C downstream of the reference static-pressure taps,** so the blockage felt at the taps
  is under 0.5 % of its value at the model. The text adds "or no closer than √C to keep the effect at five percent".
  - **Discrepancy (our arithmetic):** eq. (6.21) as printed gives 8.5 % at x = √C and 5 % at about 1.1√C. At 1.5√C
    it gives 0.4 %, which agrees with the text.
- **Keep the model base at least 2√S_b from the end of the test section, and at least 4√S_b where possible.** S_b is
  the area of the separated region on the model base.
  - The end of the test section is the diffuser entry or the end of a ground board.
  - Too close, and base pressure rises and drag falls by about 10 % (Fig. 6.7, automotive models in three tunnels).

**Open test sections** (§§6.1.2, 6.1.4, 6.3; text only):

- The correction has the opposite sign and is smaller. For plates in the linear region it is about 65 % of the
  closed-section correction (Fig. 6.2).
- Finite jet length brings nozzle and collector effects that classical theory misses; these were still being
  developed in 1998.
- Closed-section corrections are "the better developed" (p. 6-6).
- The effective volume for buoyancy is 1.5 V for a sphere and 2.0 V for an axial cylinder (Munk, Glauert; p. 6-27).

## Limitations and caveats

- No sphere data. The constants come from flat plates, rectangular blocks and automotive shapes. The rounded-body
  evidence is for 2-D cylinders (Farell et al.), and the review gives no data for 3-D rounded bodies.
- Much of the chapter targets automotive testing at large blockage (S/C up to 0.1–0.25). At the few-percent
  blockage planned here, the methods differ little (below).
- The wake-buoyancy and wake-induced-drag terms are explicitly "not yet settled" (p. 6-14).

## What it suggests for this project [Proposed]

Not decided. Arithmetic below is ours, from the formulas above. It assumes C_D = 0.47 and square test sections, and
was computed 2026-10-31 with a short Python script (the formulas and assumptions are restated here).

1. **Closed test section.** Its corrections are better understood than open-jet ones, which need nozzle and collector
   terms and empty-tunnel gradient integration.
2. **Method:** Maskell single-step (6.3) with θ = 2.5, applied to the total measured C_Du.
   - At these blockages Hackett's two-step form gives the same drag within 0.1 %. If the true C_D is 0.47, the
     measured C_Du would be about 0.487 at S/C = 3 % and 0.499 at 5 %. Both methods return 0.470.
   - The choice of method therefore matters less than the value of θ.
3. **Uncertainty from θ.** Across the cases in these two papers θ ranges from 1.85 (parachutes) to about 2.8 (square
   plates). The resulting Δq/q:

   | S/C | θ = 1.85 | θ = 2.5 | θ = 2.77 |
   |---|---|---|---|
   | 1 % | 0.9 % | 1.2 % | 1.3 % |
   | 3 % | 2.6 % | 3.5 % | 3.9 % |
   | 5 % | 4.4 % | 5.9 % | 6.5 % |

   - The spread is about ±0.65 % of C_D at 3 % blockage and about ±1.1 % at 5 %. This argues for staying near 3 %,
     or for testing two sphere sizes (Maskell1963 notes, item 3).
4. **Add a solid-blockage term.** Maskell's theory is for zero-volume plates; Mercker's form (6.19) carries a separate
   ε_s.
   - Using eq. (6.16)'s ε_s = T V/C^{3/2} with T = 0.72 (square section), a sphere at 3 % blockage gives ε_s ≈ 0.28 %
     (0.56 % in q). At 5 % it gives 0.61 % (1.2 % in q). Both are independent of tunnel size.
   - Using the sphere's effective volume of 1.5 V would raise these by half.
   - This is not negligible next to the wake term. Confirm the solid-blockage formula in Barlow1999 (boundary
     corrections, ch. 9–10) before using it.
5. **Support (sting or strut) blockage** takes the classical ½ (S/C) C_Dr term in (6.4), not θ.
6. **Positions in the test section** (combine with Mehta1979: the model at least about 0.5 D downstream of the
   contraction exit).

   | Square section h | Pitot or static taps upstream of the sphere: 1.5√C = 1.5 h | Sphere at 3 % / 5 % blockage | Sphere to test-section end: 4√S |
   |---|---|---|---|
   | 150 mm | 225 mm | 29 / 38 mm | 104 / 134 mm |
   | 200 mm | 300 mm | 39 / 50 mm | 139 / 179 mm |
   | 250 mm | 375 mm | 49 / 63 mm | 173 / 224 mm |

   - The last column uses the sphere's frontal area S as an upper bound for S_b; the paper's lower limit is half of it.
   - If the reference pressure is measured inside the test section, these rules plus Mehta's 0.5 D add up to a test
     section about 2.7–2.9 h long for a 3–5 % sphere at h = 200 mm.
   - A pitot tube left in the stream ahead of the sphere would put its wake on the sphere. Where the reference reading
     is taken (wall taps, or a probe off the centreline) is a build-step-1 choice. Barlow1999 ch. 6 (test-section
     calibration) is the place to check.
7. **The wake-induced drag increment** (6.18) for the sphere is about −0.35 % of C_D at 3 % blockage and −0.6 % at
   5 %. It is unsettled and small: note it in the uncertainty budget and do not apply it.

## References worth following up

- J. E. Hackett, "Tunnel-induced gradients and their effect on drag," Lockheed LG83ER0108, 1994; AIAA paper 96-0562;
  and the discussion in *AIAA Journal*, February 1998. The two-step method and its corrected closed form.
- C. Farell, O. Guven, S. Carrasquel, V. C. Patel, "Effect of wind-tunnel walls on the flow past circular cylinders and
  cooling tower models," ASME, 1977. Blockage on rounded bodies; the closest evidence here to a sphere.
- J. M. Macha, R. J. Buffington, "An experimental investigation of wall-interference effects for parachutes in closed
  wind tunnels," Sandia Report SAND89-1485. The chapter prints the date as December 1985, although the report number
  suggests 1989. θ = 1.85 for a rounded, porous bluff body.
- ESDU Data Item 80024, "Blockage corrections for bluff bodies in confined flows," 1980. A design-data summary.
- R. W. F. Gould, ARC R&M 3649, 1970. Upstream and downstream blockage, the basis of eqs. (6.21) and (6.22).
