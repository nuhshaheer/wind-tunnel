# Scheiman1981: Turbulence reduction by screens, honeycomb and honeycomb-screen combinations

- Citation: J. Scheiman, *Comparison of Experimental and Theoretical Turbulence Reduction Characteristics for Screens,
  Honeycomb, and Honeycomb-Screen Combinations*, NASA Technical Paper 1958, Langley Research Center, December 1981.
- Copy in this folder: [Scheiman1981_screens-honeycomb-turbulence-reduction.pdf](../Scheiman1981_screens-honeycomb-turbulence-reduction.pdf)
  (was `19820006182.pdf`, the NTRS id). Scanned report with an OCR text layer, 55 PDF pages.
  **PDF page = printed page + 3** (printed p. 1 is PDF p. 4).
- Reviewed: 2026-11-02 by Claude Code. Read the full text, pp. 1–18. Skimmed the appendix (hot-wire equations) and the
  spectra figures. Checked on page images:
  - the reduction formulas on pp. 17–18;
  - Table 1 (p. 24);
  - Fig. 5 (screen pressure loss, p. 31), Fig. 7 (screens alone, p. 33) and Fig. 11 (honeycomb plus screens, p. 37).

  Values from Figs. 7 and 11 are our readings of log-scale plots, good to about ±0.02.
- **Checked by the owner against the PDF, 2026-11-02**, read independently:

  | Point | Owner's reading (u′ / v′) | Our reading (u′ / v′) |
  |---|---|---|
  | Fig. 7, 20M | 0.64–0.65 / 0.85 | 0.65 / 0.85 |
  | Fig. 7, 36M | 0.52 / 0.67 | 0.52 / 0.68 |
  | Fig. 11, HC alone | 0.62 / 0.475 | 0.62 / 0.48 |
  | Fig. 11, HC + 28M | 0.29–0.295 / 0.215 | 0.29 / 0.22 |

  The two readings agree within 0.01.

## What they did

- **Rig:** a 0.46 m (18.25 in) square duct, a half-scale model of part of the Langley 8-Foot Transonic Pressure
  Tunnel's settling chamber (pp. 1, 4).
  - A porous plate (45 % open) made nearly isotropic upstream turbulence.
  - Mean speed was 7.62–18.29 m/s.
- **Measurements:** axial (u′) and lateral (v′) turbulence with hot wires 0.30 m downstream of the last manipulator,
  plus the static-pressure loss across each manipulator. Each manipulator's turbulence was divided by the open-duct
  value at the same point, and the ratio averaged over the speed range.
- **Manipulators tested** (Table 1, p. 24):

  | Screen | Mesh (wires/in) | Wire diameter | Open area |
  |---|---|---|---|
  | 4M | 4 | 1.270 mm | 64 % |
  | 8M | 8 | 0.660 mm | 63 % |
  | 20M | 20 | 0.230 mm | 67 % |
  | 28M | 28 | 0.190 mm | 62 % |
  | 36M | 36 | 0.165 mm | 59 % |
  | 42M | 42 | 0.140 mm | 59 % |

  | Honeycomb | Cell size | Cell length | Foil | Length / cell |
  |---|---|---|---|---|
  | 1/16 HC | 1.59 mm | 12.7 mm | 0.0254 mm | 8 |
  | 1/8 HC | 3.18 mm | 19.0 mm | 0.0254 mm | 6 |
  | 1/4 HC | 6.35 mm | 38.1 mm | 0.0762 mm | 6 |
  | 3/8 HC | 9.52 mm | 76.2 mm | 0.0762 mm | 8 |

  The honeycombs were aluminium or stainless steel.
- **Spacings** (p. 4):
  - Screens were kept at least 58 % open, to stay "subcritical" (citing Schubauer et al. 1950).
  - Screen frames spaced the screens **80–100 mesh lengths** apart. Ref. 16 shows most of a screen's turbulence
    decays within 50–75 mesh lengths.
  - The first screen sat **0.30 m behind the honeycomb**, which is 32–200 cell diameters. Ref. 16 found almost
    complete decay 23–25 cm behind a drinking-straw honeycomb, "about 50 soda-straw diameters".
  - The multiple-screen tests used 10.2 cm spacing (p. 12).

## Key numbers

**Reduction laws that fit the data** (pp. 11–12, 17–18; formulas checked on the page images). Here f is the
turbulence with the manipulator divided by the turbulence without it, and K = Δp/q.

| Configuration | Axial u′ | Lateral v′ |
|---|---|---|
| Screens alone | f ≈ 1/(1 + K) (Prandtl) | f ≈ 1/√(1 + K) (Dryden and Schubauer) |
| Screens behind a honeycomb | f ≈ (2 − K)/(2 + K) (Collar), "better than screens alone" | (same) |

- **Several screens:** treat each screen independently and multiply the factors. That fits better than summing the K
  values into one screen (p. 12).
- Doubling the screen spacing from 10.2 to 20.3 cm, or turning one screen 45°, made "very little difference" (p. 12).
- **No theory fits the honeycomb.** Its cell flow was laminar; Lumley and McMahon's theory assumes turbulent cell flow
  (pp. 16–17).

**Measured reduction factors, averaged over 7.6–18.3 m/s** (our readings of Figs. 7 and 11):

| Manipulator | u′ factor | v′ factor |
|---|---|---|
| 20M screen | about 0.65 | about 0.85 |
| 28M screen | about 0.60 | about 0.75 |
| 36M screen | about 0.52 | about 0.68 |
| 42M screen | about 0.52 | about 0.72 |
| 1/4 HC alone | about 0.62 | about 0.48 |
| 1/4 HC + 20M | about 0.33 | about 0.27 |
| 1/4 HC + 28M | about 0.29 | about 0.22 |
| 1/4 HC + 36M | about 0.24 | about 0.18 |

- **Honeycomb versus screens.** The honeycomb cuts lateral turbulence more than axial; screens do the reverse
  (pp. 13–14, 17–18). "The honeycomb with a downstream screen is an excellent combination for reducing turbulence"
  (p. 18).
- **Honeycomb cell size** (pp. 13–14, Figs. 13–14): the 1/8 HC plus screen "may provide the best performance," but the
  differences were too small to conclude.
- **Screen pressure loss** (Fig. 5, p. 31). At 10 m/s, roughly 30 Pa for 20M and about 65 Pa for 42M (our reading),
  i.e. K ≈ 0.5–1.1 with q ≈ 60 Pa. De Vahl Davis's prediction method (ref. 7) was off by up to 50 % (p. 10).
- **Honeycomb pressure loss** (p. 13). The manufacturer's data fitted poorly. Laminar flat-plate skin friction,
  C_f = 1.328/√R with R based on cell depth, applied to the wetted area, fitted the 1/4 HC well. That HC had a cell
  Reynolds number of about 40,000.
- **Behind the honeycomb** (pp. 14–16, Fig. 16):
  - it removes mainly large-scale, low-frequency turbulence;
  - at 0.30 m downstream it actually raised v′ above about 2000 Hz;
  - by 0.91 m that small-scale turbulence had decayed.

## Limitations and caveats

- The purpose was **very low turbulence for laminar-flow research**, a stricter goal than a sphere-drag check
  (our note). Turbulence intensity mainly moves a sphere's drag crisis, which lies far above this project's Re.
- The speeds and scale differ from this project's. The duct was 0.46 m at 7.6–18.3 m/s; this project's settling chamber
  is 0.25 m at about 2 m/s. Wire Reynolds numbers here will be much lower, so K and the reduction factors will differ.
  K from formulas is uncertain in any case (up to 50 % error).
- **Lateral turbulence (v′) error can be much larger than ±10 %**, while axial stays within ±10 % (p. 5, Fig. 3). Treat
  the v′ values as trends.
- The honeycombs were thin metal foil (0.025–0.076 mm). A 3D-printed honeycomb would have much thicker walls (our note).
- Results are averages over the speed range, from one rig with one upstream turbulence source.

## What it suggests for this project [Proposed]

1. **Order in the settling chamber: honeycomb, then screen(s).** Scheiman and Mehta1977 agree. Even one screen behind
   the honeycomb gave u′ ≈ 0.3 and v′ ≈ 0.2–0.3 of the incoming turbulence in Scheiman's rig. The contraction (ratio
   6.25) reduces the remaining axial turbulence further ([Bell1988 notes](Bell1988.md)).
2. **Screens at least 58 % open.** This matches Mehta's β > 0.57. Fine meshes of 20–30 wires/in with 0.19–0.23 mm wire
   (62–67 % open) are the kind tested here.
3. **Spacing between screens:**
   - 80–100 mesh lengths (most decay within 50–75); for 20–28 mesh that is about 70–125 mm (our arithmetic);
   - Mehta1977's "at least 500 wire diameters" gives 95–115 mm for 0.19–0.23 mm wire; the two rules agree within
     about 20 %;
   - both exceed the 0.2 × 250 mm = 50 mm that Mehta1979 calls successful. Use the longer distances for full
     turbulence benefit.
4. **Spacing from the honeycomb to the first screen.** Scheiman used 0.30 m; drinking straws needed about 50 straw
   diameters. Our arithmetic: with 3 mm cells, 50 cell diameters is about 150 mm.
5. **Possible settling-chamber stack** (our arithmetic): a 3 mm-cell honeycomb about 20–25 mm long, then about 150 mm,
   one screen, about 100 mm, a second screen, then 50 mm to the contraction. That is about 0.3 m, against the length
   budget's 0.15–0.2 m ([PROJECT_BACKGROUND.md](../../PROJECT_BACKGROUND.md#tunnel-length-budget)).
   - With only one settling-chamber screen (the wide-angle diffuser already holds two, Mehta1977) it is about 0.23 m.
   - Settle the length at the sizing task. The trade-off is a little more length against lower turbulence.
6. **A printed honeycomb needs thought** (D-005). With 0.4 mm walls on 3 mm square cells, only about 75 % of the area
   is open, and the thick walls raise both pressure loss and wake turbulence (our arithmetic). Thin bought honeycomb
   (paper, aluminium) or drinking straws, as in Loehrke and Nagib, are the alternatives. Not decided.
7. **Measure the pressure drop of the actual screens and honeycomb** at the real settling-chamber speed if the fan's
   pressure margin gets tight. The formulas can be 50 % off.

## References worth following up

- R. I. Loehrke, H. M. Nagib, "Experiments on Management of Free-Stream Turbulence," AGARD R-598, September 1972
  (ref. 16): drinking-straw honeycombs and decay distances. Also their 1976 *ASME J. Fluids Engng* paper (cited in
  Mehta1977).
- G. B. Schubauer, W. G. Spangenberg, P. S. Klebanoff, "Aerodynamic Characteristics of Damping Screens," NACA TN 2001,
  1950 (ref. 5): the critical open-area ratio.
- H. L. Dryden, G. B. Schubauer, "The Use of Damping Screens for the Reduction of Wind-Tunnel Turbulence," *J.
  Aeronaut. Sci.* 14(4), 1947, pp. 221–228 (ref. 8).
- J. Scheiman, "Considerations for the Installation of Honeycomb and Screens to Reduce Wind-Tunnel Turbulence," NASA
  TM-81868, 1981 (ref. 15).
- J. L. Lumley, J. F. McMahon, "Reducing Water Tunnel Turbulence by Means of a Honeycomb," *Trans. ASME J. Basic Eng.*
  89, 1967, pp. 764–770 (ref. 10).
