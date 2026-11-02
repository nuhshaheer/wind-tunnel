# Morrison2013: Data correlation for drag coefficient for sphere

- Citation: F. A. Morrison, "Data Correlation for Drag Coefficient for Sphere," Department of Chemical Engineering,
  Michigan Technological University, 4 April 2013, 2 pp. The handout gives its address as
  www.chem.mtu.edu/~fmorriso/DataCorrelationForSphereDrag2013.pdf (not opened). The correlation itself is from
  F. A. Morrison, *An Introduction to Fluid Mechanics*, Cambridge University Press, 2013: "Figure 8.13 on page 625"
  (handout) or "Morrison equation 8.83" (exam sheet).
- Copies in this folder:
  - [Morrison2013_sphere-drag-correlation.pdf](../Morrison2013_sphere-drag-correlation.pdf), the 2-page handout
    (was `DataCorrelationForSphereDrag2013.pdf`). **Use this one.**
  - [Morrison2013_exam-data-correlations-sheet.pdf](../Morrison2013_exam-data-correlations-sheet.pdf), the CM3110
    "Data Correlations for Examinations" sheet, 4 pages; pipe friction on pp. 1–2, sphere on pp. 3–4 (was
    `DataCorrelationsforExaminations2013.pdf`). It prints a different version of the correlation, with a typo.
- Reviewed: 2026-11-02 by Claude Code. Read both files in full. Every equation and constant was read from zoomed page
  renders (PyMuPDF); the text layer garbles all the equations.
- **Checked by the owner against the PDFs, 2026-11-02:** every constant in Eq. (1); the exam sheet's "236,000"
  (a typo for 263,000, the owner agrees); and the exam sheet's last term.

## What it is

One explicit curve fit of C_D against Re for a smooth sphere in uniform flow, from creeping flow up to Re = 10⁶. It is
a fit, not a measurement. The handout plots it over sphere data from Schlichting (1955) (Fig. 1, p. 2); the exam
sheet plots it over data from White (1974) (Fig. 3, p. 4). Neither file states the fit's error, its residuals or the
free-stream turbulence and sphere roughness behind the data.

## Key numbers

**Eq. (1)** (handout p. 1, read from the page image):

C_D = 24/Re + 2.6·(Re/5.0) / [1 + (Re/5.0)^1.52] + 0.411·(Re/263,000)^−7.94 / [1 + (Re/263,000)^−8.00]
+ Re^0.80 / 461,000

- At low Re it becomes C_D = 24/Re (creeping flow, Re < 2; Fig. 1 caption). Not recommended above Re = 10⁶ (p. 1).
- The handout text (p. 1) places the "highly variable transition region near Re=2x10⁶" (checked on the page image).
  Its Fig. 1 and the 263,000 term put the drag crisis near 2–3×10⁵, so 2×10⁶ is probably a typo for 2×10⁵ (our
  reading).

**Exam sheet Eq. (4)** (p. 3) differs from Eq. (1) in two places:

- The last term is 0.25·(Re/10⁶) / [1 + Re/10⁶] instead of Re^0.80/461,000. The equation printed inside its Fig. 3
  (p. 4) uses the same 0.25 form. At this project's Re the two last terms differ by about 0.001 in C_D (our
  arithmetic), which is negligible.
- **The typed equation's third denominator reads 236,000**; the copy inside its own Fig. 3 reads 263,000. With
  236,000 the formula gives C_D ≈ 0.86 at Re = 10⁴, more than twice the plotted curve (our arithmetic), so it is a
  typo. Do not copy the exam sheet's typed Eq. (4).

**Exam sheet simplified forms** (p. 3, Eqs. 5–8, "Morrison equation 8.82"):

| Range | Form |
|---|---|
| Re < 2 | C_D = 24/Re |
| 0.1 ≤ Re ≤ 1,000 | C_D = (24/Re)(1 + 0.14·Re^0.7) |
| 1,000 ≤ Re ≤ 2.6×10⁵ | **C_D = 0.445** |
| 2.8×10⁵ ≤ Re ≤ 10⁶ | Eq. (8), printed as log C_D / (Re/10⁶) = 4.43 log Re − 27.3 |

**Eq. (1) evaluated (our arithmetic, 2026-11-02, a short Python script):**

| Re | C_D, handout Eq. (1) | C_D, exam Eq. (4) with 263,000 |
|---|---|---|
| 5×10³ | 0.402 | 0.402 |
| 1×10⁴ | 0.394 | 0.393 |
| 1.3×10⁴ | 0.393 | 0.392 |
| 2×10⁴ | 0.394 | 0.393 |
| 3×10⁴ | 0.398 | 0.397 |
| 5×10⁴ | 0.407 | 0.406 |
| 1×10⁵ | 0.425 | 0.426 |

- Between Re = 5×10³ and 2×10⁵, Eq. (1) has its **minimum, 0.393, at Re ≈ 1.34×10⁴**. Its highest value in that range is
  0.435, at Re ≈ 1.5×10⁵. It never reaches 0.47 below the drag crisis.
- At the planned test conditions (ρ = 1.20 kg/m³ and μ = 1.81×10⁻⁵ Pa·s, both assumed):

  | Sphere | 5 m/s | 10 m/s | 13 m/s | 15 m/s |
  |---|---|---|---|---|
  | 20 mm | Re 6.6×10³, C_D 0.397 | Re 1.33×10⁴, 0.393 | Re 1.72×10⁴, 0.393 | Re 1.99×10⁴, 0.394 |
  | 25 mm | Re 8.3×10³, 0.395 | Re 1.66×10⁴, 0.393 | Re 2.15×10⁴, 0.395 | Re 2.49×10⁴, 0.396 |

## Limitations and caveats

- **It is a single fit across ten decades of Re**, plotted on log-log axes that span six decades of C_D. A local misfit
  of 10 % would not show on those plots. No accuracy is stated.
- **Checked against Roos1971 (2026-11-02; [notes](Roos1971.md)):**
  - Eq. (1) sits inside the band of earlier data in Roos Fig. 3 at Re = 10⁴, but only at its lower edge by 2×10⁴.
  - It falls below the band at 5×10⁴ (band about 0.43–0.50, Eq. (1) 0.407; our reading of the figure).
  - Roos's own points at Re = 1–3×10⁴ average 20–28 % above Eq. (1), but Roos says those points read high.
- The exam sheet's simplified plateau, C_D = 0.445, hides the shallow minimum near Re ≈ 10⁴. At this project's Re it
  is about 13 % above Eq. (1).
- The underlying data are textbook compilations (Schlichting 1955; White 1974), not one controlled experiment.

## What it suggests for this project [Proposed]

> **Update 2026-11-02 (same day): superseded as the reference by [Brown2003](Brown2003.md).**
> - Brown and Lawler's Eq. (19), fitted to 480 curated, wall-corrected points, gives C_D ≈ 0.42–0.445 at Re
>   1.3–2.5×10⁴. Clift's standard curve agrees within about 1 %.
> - Morrison's Eq. (1) is **7–11 % below** both in that range, so its minimum near Re ≈ 10⁴ is an artefact of the
>   single fit.
> - Points 1–2 below are kept for the record. Their "about 0.39" is replaced by Eq. (19)'s 0.42–0.445, with a
>   reference band of about ±10 %. The data at this Re sit about 7 % above Eq. (19); see the Brown2003 notes.

1. **"About 0.47" is not the expected C_D at this project's Re.** Eq. (1) gives about 0.39 at Re = 1–2.5×10⁴. The
   planned 20 mm sphere at 10 m/s sits almost exactly at the curve's minimum.
2. **Use Eq. (1) as an explicit, reproducible reference curve, but carry an uncertainty band with it.** The earlier
   data in Roos Fig. 3 span about 0.38–0.45 at Re = 10⁴ and 0.40–0.49 at 2×10⁴. So the reference itself is uncertain
   by roughly ±10 %, about as large as the measurement uncertainty this project hopes for. A validation can show
   agreement only within that band.
3. Take the correlation from the handout (Eq. (1)), never from the exam sheet's typed Eq. (4).
4. A better-documented standard drag curve would narrow the band. One candidate for the "Wanted" list: R. Clift,
   J. R. Grace, M. E. Weber, *Bubbles, Drops, and Particles*, Academic Press, 1978, which includes a standard sphere
   drag curve (citation from memory; not checked, not in `resources/`).

## References worth following up

- F. A. Morrison, *An Introduction to Fluid Mechanics*, CUP 2013, ch. 8 (Fig. 8.13, Eqs. 8.82–8.83): the source of
  the fit; it may state which data were fitted and how well.
- H. Schlichting, *Boundary-Layer Theory*: the sphere C_D chart plotted in the handout's Fig. 1.
- Clift, Grace and Weber (1978), above.
