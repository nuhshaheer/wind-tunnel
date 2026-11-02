# Brown2003: Sphere drag and settling velocity revisited

- Citation: P. P. Brown, D. F. Lawler, "Sphere Drag and Settling Velocity Revisited," *Journal of Environmental
  Engineering* 129(3), March 2003, pp. 222–231. doi:10.1061/(ASCE)0733-9372(2003)129:3(222). University of Texas at
  Austin.
- Copy in this folder: [Brown2003_sphere-drag-settling-velocity-revisited.pdf](../Brown2003_sphere-drag-settling-velocity-revisited.pdf).
  The owner added it on 2026-11-02 as `brown2003.pdf`.
  - Publisher's PDF with a text layer, 10 pages: **PDF page = journal page − 221**.
  - Stamped "Copyright ASCE. For personal use only; all rights reserved". Keep it out of a public repository (D-003).
- Reviewed: 2026-11-02 by Claude Code. Read the full text.
  - Checked on page images: Eqs. (16)–(19) (p. 225), Table 2 (all the earlier correlations, p. 226) and Table 3 (fit
    statistics, p. 226). Fig. 3 (the corrected data) was looked at.
  - The settling-velocity part (Eqs. (24)–(37), Tables 4–6) was only skimmed; it does not matter here.
- **Checked by the owner against the PDF, 2026-11-02:**
  - the Eq. (19) constants, the Table 3 row for Eq. (19) and Clift's 1.2×10⁴–4.4×10⁴ segment;
  - the sentence excluding Roos's 44 points (p. 223).
  - The owner could not read Fig. 3 precisely, but estimated the dots between Re = 10⁴ and 10⁵ at "around 0.5".

## What it is

A critical compilation of 20th-century sphere drag data that were published **in tabular form** (pp. 222–223):

- **Sixteen papers, 606 points to start with.** The authors removed points they judged unreliable:
  - water-droplet data (deformed drops) and points without drag data;
  - points above Re = 2×10⁵;
  - **Roos and Willmarth (1971): all 44 points above Re = 5,500**, because those authors reported heavy vibration
    there ([Roos1971 notes](Roos1971.md));
  - Vlajinac and Covert points with stated error above 2 %;
  - Lunnon's points above Re = 50,000, where the spheres had not reached terminal velocity.

  That leaves **480 points of "very high quality"**.
- **Wall-effect corrections** from Fidleris and Whitmore (1961) were applied to the 178 points taken in small vessels.
  All corrected points have Re < 80, so the data at this project's Re are uncorrected and were not affected.
- Papers that gave data only as graphs were left out because they cannot be read precisely: Wieselsberger 1922,
  Achenbach 1972 and others (p. 223).
- Existing correlations were scored against the corrected data, and four were re-fitted. Table 3 ranks them.

Most of the data come from spheres falling, or towed, through still fluid. The drag coefficient is from
C_D = (4/3)·[(ρ_p − ρ_f)/ρ_f]·g·d/v² at terminal velocity (eq. 4).

## Key numbers

**Recommended drag correlation, Eq. (19)**, valid for Re < 2×10⁵ (p. 225; checked on the page image):

C_D = (24/Re)·(1 + 0.150·Re^0.681) + 0.407 / (1 + 8,710/Re)

- Eq. (17), nearly as good: C_D = (24/Re)(1 + 0.152 Re^0.677) + 0.417/(1 + 5,070 Re^−0.940).
- **Clift et al. (1978)** (Table 2, p. 226) fits the data best overall but is a 7-piece correlation. The piece for this
  project's Re, **1.2×10⁴ ≤ Re ≤ 4.4×10⁴**, is log C_D = −1.9181 + 0.6370w − 0.0636w², with w = log Re. For
  1,500 ≤ Re ≤ 1.2×10⁴ it is log C_D = −2.4571 + 2.5558w − 0.9295w² + 0.1049w³.

**Fit to the 480 corrected points** (Table 3, p. 226; over the whole Re range):

| Correlation | rms deviation in log C_D | within ±5 % | ±7.5 % | ±10 % | ±15 % |
|---|---|---|---|---|---|
| Eq. (19) | 0.0177 | 81.3 % | 94.4 % | 97.7 % | 99.8 % |
| Eq. (17) | 0.0177 | 81.7 % | 94.2 % | 97.7 % | 99.8 % |
| Clift et al. (1978) | 0.0174 | 81.5 % | 95.0 % | 98.1 % | 99.6 % |
| Fair and Geyer (1954), the old textbook formula | 0.0666 | 39.0 % | 49.0 % | 53.3 % | 62.9 % |

- An rms deviation of 0.0177 in log₁₀ is about **±4 %** in C_D (our arithmetic: 10^0.0177 = 1.042).
- Eq. (19) "fits the data very well throughout the entire range", except slight under-prediction at Re 3–90 and
  over-prediction at 100–400 (p. 226). Neither range is this project's.

**At this project's test conditions** (our arithmetic, 2026-11-02; ρ = 1.20 kg/m³ and μ = 1.81×10⁻⁵ Pa·s assumed):

| Sphere, speed | Re | Eq. (19) | Clift | Morrison2013 Eq. (1) |
|---|---|---|---|---|
| 20 mm, 5 m/s | 6.6×10³ | 0.397 | 0.389 | 0.397 |
| 20 mm, 10 m/s | 1.33×10⁴ | 0.422 | 0.424 | 0.393 |
| 20 mm, 13 m/s | 1.72×10⁴ | 0.432 | 0.436 | 0.393 |
| 20 mm, 15 m/s | 1.99×10⁴ | 0.437 | 0.441 | 0.394 |
| 25 mm, 10 m/s | 1.66×10⁴ | 0.431 | 0.434 | 0.393 |
| 25 mm, 13 m/s | 2.15×10⁴ | 0.440 | 0.445 | 0.395 |
| 25 mm, 15 m/s | 2.49×10⁴ | 0.445 | 0.450 | 0.396 |

- Eq. (17), Turton and Levenspiel (1986) and Haider and Levenspiel (1989) all lie within about 3 % of Eq. (19) at
  Re = 10⁴–3×10⁴.
- **Morrison2013 is 7–11 % below all of them for Re = 1.3–3×10⁴.** Its single fit dips too low there.

**The data near this project's Re: Fig. 3, measured from pixels** (our measurement, 2026-11-02).
- Calibration: from the figure's own decade ticks.
- Check: the dots for Re < 0.1 read 1.01 × Stokes' 24/Re (median), against the paper's "within ±2.5 %" (p. 228). The
  axes are right to about 1–2 %.
- Measurement: every data-dot pixel, converted to C_D and divided by Eq. (19) at its Re.

| Re range | Data C_D, 5th–95th percentile (median) | Data ÷ Eq. (19), 5th–95th percentile (median) |
|---|---|---|
| 5×10³–10⁴ | 0.396–0.452 (0.421) | 1.01–1.12 (1.06) |
| 10⁴–2×10⁴ | 0.426–0.510 (0.452) | 1.02–1.22 (1.07) |
| 2×10⁴–5×10⁴ | 0.441–0.522 (0.480) | 1.00–1.14 (1.07) |
| 5×10⁴–10⁵ | 0.469–0.535 (0.498) | 1.01–1.16 (1.07) |

- The dots lie mostly **above** Eq. (19) at these Re. Their median is about 7 % higher, and the scatter is about
  ±8 %.
- An overlay of Eq. (19) and Clift's curve on the figure shows the same: both curves run along the lower edge of the
  data between Re = 10³ and 3×10⁴, and Clift meets the data at 5×10⁴–10⁵.
- The paper's "81 % within ±5 %" is over all 480 points, and most of them are at much lower Re.
- This reading is a pixel measurement, not a tabulated value. It is consistent with the owner's "around 0.5" for
  10⁴–10⁵ and with Roos1971's statement that existing data scatter by "at least 10 %".

## Limitations and caveats

- **Settling and towing data, not wind-tunnel data.** The fluid was still, with no free-stream turbulence, and the
  spheres had no sting. A tunnel adds turbulence, a sting and blockage. Those are this project's corrections to make,
  not errors in the reference.
- The ±5 % figures are over all Re. The paper gives no scatter for Re = 10⁴–3×10⁴, nor how many points or which
  sources are there. Our Fig. 3 measurement (above) puts the local data about 7 % above Eq. (19), with about ±8 %
  scatter.
- **Clift et al. is not an independent check.** It was fitted to "a subset of this data (478 points)" (p. 223), so
  agreement between the two shows that the choice of formula hardly matters, not that the data are right.
- The fits are local least-squares minimizations in log C_D, "may not be the best global" fits (p. 224).
- The data come from many sources and decades, each with its own sphere finish and method. The paper excludes points
  but does not weight them.

## What it suggests for this project [Proposed]

1. **Use Eq. (19) as the validation reference curve, evaluated at each run's own Re, with a reference band of about
   ±10 %, not ±5 %.** This replaces "about 0.47" (D-001) and Morrison2013. It needs a new DECISIONS.md entry, which is
   the owner's decision.
   - Eq. (19) gives **0.42–0.445** for the planned runs (Re 1.3–2.5×10⁴).
   - The data there sit about 7 % above it, with about ±8 % scatter (Fig. 3, our measurement). So the published
     measurements alone put the true value somewhere in about **0.42–0.50**.
   - The ±5 % in Table 3 is an all-Re figure and too tight at this Re.
   - Clift is a check on the formula, not on the data (above).
   - The band could shrink if the original tables for this Re range are obtained (likely Lunnon 1928 and Vlajinac and
     Covert 1972, not checked).
2. **Add a trend check that does not depend on the band.** Eq. (19) rises about 12 % from Re = 6.6×10³ to 2.5×10⁴.
   - Runs at several speeds should show C_D rising with Re by about that amount.
   - Matching the shape is evidence that the tunnel reads true even while the absolute level is uncertain by ±10 %.
   - It needs a measurement uncertainty well under 12 % at the lowest speed.
3. **C_D is not flat across the test range.** Eq. (19) rises about 12 % from Re = 6.6×10³ (0.397) to 2.5×10⁴
   (0.445).
   - Compare each run with the reference at its own Re, never with one number.
   - The two-sphere blockage check must be done at matched Re. A 25 mm sphere at the same speed as a 20 mm one sits
     at 25 % higher Re, which is about 2 % higher C_D.
4. **The vibration lesson is confirmed.** An independent curation dropped Roos's high-Re points for vibration. Keep
   fan vibration out of the balance (separate stand, flexible coupling).
5. **What the validation can show.** After blockage and sting corrections, a result inside the ±10 % band and following
   the trend counts as agreement. A miss well outside both points to the tunnel or the instruments. The ±10 % is the
   limit set by the reference, not by our instruments.

## References worth following up

- V. Fidleris, R. L. Whitmore, "Experimental determination of the wall effect for spheres falling axially in
  cylindrical vessels," *Br. J. Appl. Phys.* 12, 1961, pp. 490–494: the wall-effect corrections (also cited by
  Roos1971).
- R. Clift, J. R. Grace, M. E. Weber, *Bubbles, Drops, and Particles*, Academic Press, 1978: the best-fitting
  correlation. Its equations are reprinted in Table 2 here, so the book is optional now.
- Vlajinac and Covert (1972) and Lunnon (1928): the data sets likely to cover Re 10⁴–5×10⁴ (not checked).
