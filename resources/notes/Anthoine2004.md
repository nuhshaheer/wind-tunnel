# Anthoine2004: Drag coefficient determination of bluff bodies, analysis of blockage effect

- Citation: J. Anthoine, D. Olivari, D. Portugaels, "Drag Coefficient Determination of Bluff Bodies – Analysis of
  Blockage Effect," von Karman Institute for Fluid Dynamics, Reprint 2004-24; presented at COST Action C14, *Impact of
  Wind and Storm on City Life and Built Environment*, Rhode-Saint-Genèse, Belgium, 5–7 May 2004. Paper pages E.7.1 to
  E.7.10.
- Copy in this folder: [Anthoine2004_bluff-body-drag-blockage-effect.pdf](../Anthoine2004_bluff-body-drag-blockage-effect.pdf)
  (was `rp200424.pdf372046978rp200424.pdf`). Twelve PDF pages: a VKI reprint cover (which lists "P. Cosyn" instead of
  J. Anthoine), a blank page, then the paper. **Paper page E.7.n = PDF page n + 2.**
- Reviewed: 2026-11-22 by Claude Code (Opus 5.5): full text from the text layer (clean); Eqs. (3)–(6) and Fig. 4
  checked on the page images.
- **Owner check pending** (checklist at the end).

## What they did

Drag and base pressure of three smooth circular cylinders, d = 160, 320 and 400 mm, spanning a rectangular insert
with solid walls (a closed 2-D test section) in the VKI L-1A tunnel (3 m free jet, contraction ratio 4, turbulence
about 0.3 %, 2–50 m/s; insert height 2.36 m) (pp. E.7.1–E.7.5). Re = 8 × 10⁴ to 1.3 × 10⁶, covering the sub-critical,
critical and early super-critical regimes. Drag was measured with strain-gauge balances at both ends of the cylinder;
q with a pitot tube. They then compared four published blockage corrections against the scatter between the three
sizes.

## Key numbers

**Models** (Table 2, p. E.7.4):

| d | Blockage S/C | Re max | Aspect ratio l/d |
|---|---|---|---|
| 160 mm | 6.8 % | 5.2 × 10⁵ | 8.12 |
| 320 mm | 13.6 % | 1.0 × 10⁶ | 4.06 |
| 400 mm | 17 % | 1.3 × 10⁶ | 3.25 |

End plates 1.3 m apart, 2.5 m upstream and 1.75 m downstream of the model (more than Kubo's 4.25 d); a reference plane
of uniform static and dynamic pressure was found 1.8 m upstream of the model (p. E.7.5). For two-dimensional flow, the
aspect ratio should exceed 3 (Chen and Doepker; Achenbach) (p. E.7.4).

**Flow regimes of a circular cylinder** (Table 1, p. E.7.3): 0–5 viscous without separation; 5–40 steady recirculation;
40–400 laminar vortex street; **400 – 2 × 10⁵ sub-critical**; 2 × 10⁵ – 5 × 10⁵ critical; 5 × 10⁵ – 3 × 10⁶
super-critical; above 3 × 10⁶ trans-critical. C_D ≈ 1.2 at the end of the sub-critical regime and ≈ 0.3 at the start
of the super-critical regime (p. E.7.3).

**Raw results** (Fig. 4, p. E.7.5): uncorrected C_D and −C_pb both rise with blockage; the difference between the three
curves is the blockage effect.

**The four corrections** (pp. E.7.6–E.7.8; S = projected frontal area, C = test-section area; c = corrected):

1. **Glauert** (Eq. 3): C_D,c/C_D = [(1 − G S/C) / (1 + 0.822 (S/C)²)]². Glauert's G = 0.3 for cylinders; Modi and
   El-Sherbiny's G = 0.6 "gives a considerable improvement." Works in the super-critical regime; **over-corrects in the
   sub-critical regime.**
2. **Allen and Vincenti** (Eq. 4): **C_D,c/C_D = 1 − (π²/4)(S/C)² − (C_D/2)(S/C).** Wake modelled by sources;
   "works much better in the sub-critical regime"; more scatter in the super-critical regime.
3. **Maskell** (Eq. 5): **C_D/C_D,c = 1 + ε C_D S/C**, with ε = 0.96 from Maskell's best fit for two-dimensional
   sharp-edged bluff bodies; in theory ε = −1/C_pb (Eq. 6). With ε = 0.96 it works well sub-critically, like Allen and
   Vincenti, but scatters super-critically. Using the measured base pressure (Eq. 6) did not do better, and "Maskell's
   theory, when based on the base pressure, has proved to fail for circular cylinders" (footnote, p. E.7.8).
4. **Modi and El-Sherbiny** (sources and sinks for the near wake; validated up to 35 % blockage at Re 10⁴ – 1.2 × 10⁵):
   works super-critically, over-corrects sub-critically, like Glauert with G = 0.6.

**Conclusion** (pp. E.7.8–E.7.9): "None of the correction models known in the literature is valid for all the flow
regimes." Sub-critical: Allen and Vincenti, or Maskell with ε = 0.96. Super-critical: Glauert with G = 0.6, or Modi and
El-Sherbiny. Fig. 9 (C_D against 1 − C_pb) shows two different slopes, changing at C_D ≈ 1, at the transition between
the regimes; the change in wake pattern is not in any of the theories, which use a single empirical factor.

**Other statements:**

- "In practice, one can neglect blockage effect of bluff bodies when the wind tunnel cross-section is at least 30 times
  larger than the bluff body cross-section (blockage ratio smaller than 3 %)" (p. E.7.1).
- Closed test sections are preferable because their corrections are better developed and the boundaries better defined
  (p. E.7.6, citing Cooper1998).
- "It was checked that the mean value is independent of the number of acquisition points" (p. E.7.5).

## Limitations and caveats

- Two-dimensional cylinders only, at Re ≥ 8 × 10⁴ and blockage ≥ 6.8 %. No spheres, no three-dimensional bodies.
- No uncertainty is given for the measurements; "best" is judged by eye from the scatter in Figs. 7–8.
- The 3 % "negligible" threshold is stated without support. Barlow1999 ch. 9 puts a 5 % blockage at about 2.6 % in q,
  and our sphere estimate is about 4 % in q at 2.85 % blockage ([Barlow1999 notes](Barlow1999.md), ch. 10), so this
  project corrects regardless.

## What it suggests for this project [Proposed]

1. **For the sphere: little directly.** The value of this paper for the validation run is its warning that a
   correction tuned in one flow regime can fail in another. The sphere runs stay in one regime (sub-critical,
   Re 1–2.5 × 10⁴), so a single wake-blockage constant is reasonable; the matched-Re comparison of the two balls tests
   it.
2. **For a later cylinder test** (a full-span rod, discussed 2026-11-10): a 1/4 in (6.35 mm) rod spanning the 100 mm
   section is sub-critical (Re ≈ 5,500 at 13 m/s), with S/C = d/h = 6.35 % and l/d ≈ 16 (our arithmetic). Use Allen and
   Vincenti or Maskell with ε = 0.96. With C_D ≈ 1.2, they give corrections of about −4.8 % and −6.8 % (our arithmetic);
   the 2 % difference between them is a measure of the correction's uncertainty at that blockage. A thinner rod would
   reduce both.
3. **Use two sizes to check the correction**, as they did with three cylinders: if the corrected C_D of two rod or ball
   sizes agree at the same Re, the correction is working.
4. **Check that the mean is independent of the averaging length** (p. E.7.5): a simple test for the logging firmware;
   compare means over the first and second halves of each record.

## References worth following up

- Hackett and Cooper, "Extensions to Maskell's theory for blockage effects on bluff bodies in a closed wind tunnel,"
  *Aeronautical Journal* 105, 2001, pp. 409–418 (their ref. 6).
- Allen and Vincenti, NACA Report 782, 1944 (their ref. 12; free from NASA NTRS).
- Farell et al., ASME 76-WA/FE-20, 1977, on walls and cylinders (also cited by Cooper1998).

## Owner check (values read from the PDF)

Paper page, then PDF page.

1. p. E.7.6 (PDF 8), **Eq. (3)**: the form of Glauert's formula, the 0.822 and the two values of G (0.3 and 0.6).
2. **Most important.** p. E.7.7 (PDF 9), **Eq. (4)**: Allen and Vincenti's formula, and Eq. (5)–(6): Maskell's form and
   ε = 0.96.
3. p. E.7.4 (PDF 6), Table 2: the three diameters, blockage ratios and aspect ratios.
4. p. E.7.3 (PDF 5), Table 1: the Reynolds-number range of the sub-critical regime.
5. p. E.7.8 (PDF 10): the recommended correction for each regime, and the footnote about base pressure.
6. p. E.7.1 (PDF 3): the "30 times … smaller than 3 %" sentence.
