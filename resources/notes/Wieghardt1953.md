# Wieghardt1953: On the resistance of screens

- Citation: K. E. G. Wieghardt, "On the Resistance of Screens," *The Aeronautical Quarterly* 4, February 1953,
  pp. 186–192. doi:10.1017/S0001925900000871. The author was formerly at the Admiralty Research Laboratory,
  Teddington, then at Hamburg University.
- Copy in this folder: [Wieghardt1953_resistance-of-screens.pdf](../Wieghardt1953_resistance-of-screens.pdf). The owner
  added it on 2026-11-02 as `wieghardt1953.pdf`.
  - Scanned journal pages with a text layer, 7 PDF pages: **PDF page = journal page − 185**.
  - Cambridge Core download stamp (Purdue University Libraries, 6 January 2018), "subject to the Cambridge Core terms of
    use". Keep it out of a public repository (D-003).
- Reviewed: 2026-11-02 by Claude Code. Read the full text. Every equation used here (eqs. 2–6 and 11–15) was read from
  page renders; the text layer garbles them. Figs. 1–2 (data plots) and Fig. 3 (nomogram) were only glanced at.
- **Checked by the owner against the PDF, 2026-11-02:** eq. (11) with its "between 60 and 600" range, eq. (15) = 85,
  and eq. (5).
  - The owner first read eq. (12)'s "5·5" as 5 × 5.
  - **Reading tip:** this paper, like the other British papers here (Mehta1979, Maskell1963), prints the decimal point
    as a raised dot: "6·5", "0·78", "1:1·25". Multiplication is written "×" (worked example, p. 191: "0·1 × 2 × 0·78").
  - So 5·5 = 5.5. This is consistent with the text ("lower values" than eq. (11)'s 6.5) and with the average of 6 in
    eq. (13).

## What it is

A short paper that collapses all the screen pressure-drop data then available (refs. 1, 3, 5, 6, 7: Flachsbart 1932,
Collar 1939, Taylor and Davies 1944, Simmons and Cowdrey 1949, Schubauer et al. 1950) onto one curve.
- It treats a square-mesh round-wire screen as a set of single wires (cylinders) in a stream at the **average velocity
  through the holes, u₁/β**, not at the upstream velocity u₁ (p. 187).
- It gives the source of the formula that Mehta1977 and Mehta1979 call "Wieghardt's formula".

## Key numbers

Notation: d = wire diameter, β = open-area ratio (porosity), u₁ = velocity before the screen, ν = kinematic viscosity,
k = (p₁ − p₂)/(½ρu₁²), c = the wire's drag coefficient.

| Eq. | Statement | Page |
|---|---|---|
| (5) | c = β²·k/(1 − β), i.e. **k = c·(1 − β)/β²** | 187 |
| (6) | k ≈ (1 − β)/β² at high Re (from Simmons and Cowdrey's tests) | 187 |
| (11) | **c = 6.5·(u₁d/βν)^(−1/3)** fits all the tests "for u₁d/(βν) between 60 and 600" (British NPL tube tests) | 190 |
| (12) | c = 5.5·(u₁d/βν)^(−1/3) for the American NBS tests (screens at the end of a duct discharging into free air), about 15 % lower; "No explanation for this difference is obvious" | 190 |
| (13), (14) | Average of all tests: **c ≈ 6·(u₁d/βν)^(−1/3)**, or k ≈ 6·(1 − β)·β^(−5/3)·(u₁d/ν)^(−1/3) | 191 |
| (15) | Onset of eddy shedding behind a screen (start of its own turbulence production), from Schubauer et al.'s hot-wire data: **(u₁d/βν)_crit ≈ 85** | 191 |

- In the data, k ranges from 0.35 to 19, and all points lie along one curve except a rectangular-mesh screen and the
  highest-Re points of Flachsbart (p. 187).
- Worked example (p. 191): d = 1/32 in, β = ½, u₁ = 20 ft/s gives u₁d/ν ≈ 350, c ≈ 0.78 and Δp = 0.16 in of water.
- Turbulent flow round the wires would need u₁d/(βν) of about 3×10⁵ (p. 188).

## Limitations and caveats

- An empirical fit to 1930s–1950 data. The two main data sets differ by about 15 % (eqs. 11 and 12), with no
  explanation; wire surface roughness is suggested. So K from the formula is good to roughly ±10–15 % at best.
- It covers square meshes of round wire only. Woven-wire waviness and the wire crossings are ignored (p. 188).
- The fitted range is u₁d/(βν) = 60–600. Below 60 the formula is an extrapolation.

## What it suggests for this project [Proposed]

1. **This confirms the range in Mehta1977's eq. (9).** Mehta prints it as "60 > Ud/βν > 600"; the source says
   "between 60 and 600". Mehta's inequalities are a typo ([Mehta1977 notes](Mehta1977.md)).
2. **Screen K at this project's speeds** (our arithmetic, 2026-11-02). Assumptions: 13 m/s in the 100 mm test section,
   so about 2.1 m/s in the 250 mm settling chamber and about 7.2 m/s at the 152 mm fan outlet; ν = 1.5×10⁻⁵ m²/s.
   Screen sizes are Scheiman1981's ([notes](Scheiman1981.md)).

   | Screen (d, β) | Where | u₁d/(βν) | k from eq. (11) / (13) / (12) | Collar's high-Re k = 0.9(1 − β)/β² |
   |---|---|---|---|---|
   | 28M (0.19 mm, 0.62) | settling chamber, 2.1 m/s | 42 | 1.84 / 1.70 / 1.56 | 0.89 |
   | 28M | diffuser inlet, 7.2 m/s | 147 | 1.22 / 1.12 / 1.03 | 0.89 |
   | 20M (0.23 mm, 0.67) | settling chamber | 48 | 1.32 / 1.22 / 1.12 | 0.66 |
   | 42M (0.14 mm, 0.59) | settling chamber | 33 | 2.39 / 2.21 / 2.02 | 1.06 |

   - At settling-chamber speeds, fine screens have about **twice the K of the high-speed formula**. Those values are
     extrapolated below the fitted range (u₁d/(βν) < 60), so they are uncertain.
   - Two 28M-type screens in the fan-to-chamber diffuser would give K_sum of roughly 2.6–3. That meets Mehta1977's
     requirement of K_sum ≥ 2.1 for A = 3.44.
   - Use the larger, low-speed K values in the fan-pressure budget, and measure a sample screen if the margin is tight.
3. **The settling-chamber screens should make no turbulence of their own.** At about 2 m/s, u₁d/(βν) ≈ 33–48 is below
   the critical value of 85 (eq. 15), so the wires should not shed eddies. Screens at the diffuser inlet (about
   7 m/s, u₁d/(βν) ≈ 110–165) will shed eddies, but the downstream screens and honeycomb then damp them.
4. **A cross-check with Scheiman1981.** His 28M screen at 9.1 m/s gives K ≈ 0.9 (our reading of his Fig. 5). Eq. (11)
   gives 1.13 and eq. (12) gives 0.95 there, so his data sit nearer the American fit.

## References worth following up

- G. B. Schubauer, W. G. Spangenberg, P. S. Klebanoff, "Aerodynamic Characteristics of Damping Screens," NACA TN 2001,
  1950 (ref. 7): the American screen data and the critical Reynolds number for eddy shedding.
- L. F. G. Simmons, C. F. Cowdrey, "Measurements of the Aerodynamic Forces Acting on Porous Screens," ARC R&M 2276,
  1949 (ref. 6): the "very accurate" British tests.
