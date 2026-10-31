# Resources

Reference papers, reports and datasheets used to design the tunnel. Each item has a PDF in this folder and, once it
has been read, a notes file in `notes/` recording what it says (with page and figure numbers), its caveats, and what it
suggests for this project. Conclusions that change the design go to [DECISIONS.md](../DECISIONS.md) or
[PROJECT_BACKGROUND.md](../PROJECT_BACKGROUND.md) and cite the notes file.

Agents: read the notes file first. Open the PDF only when you need a detail the notes do not cover.

## Index

| Key | Reference | Topic | Status | Files |
|---|---|---|---|---|
| Abdelhamed2014 | A. S. Abdelhamed, Y. El-S. Yassen, M. M. ElSakka, "Design optimization of three dimensional geometry of wind tunnel contraction," *Ain Shams Engineering Journal*, 2014 (article in press). doi:10.1016/j.asej.2014.09.008 | Contraction ratio, length and wall profile; CFD optimization checked with a pitot-static traverse | Reviewed 2026-10-30 | [PDF](Abdelhamed2014_wind-tunnel-contraction-optimization.pdf), [notes](notes/Abdelhamed2014.md) |
| Bell1988 | J. H. Bell, R. D. Mehta, *Contraction Design for Small Low-Speed Wind Tunnels*, NASA CR-177488, Stanford University, August 1988 (also JIAA TR-84, April 1988) | Contraction wall shape (5th-order polynomial), length and separation for small tunnels; panel method + laminar boundary layer, validated on 4 tunnels | Reviewed 2026-10-30 | [PDF](Bell1988_contraction-design-small-low-speed-tunnels.pdf), [notes](notes/Bell1988.md) |
| Mehta1979 | R. D. Mehta, P. Bradshaw, "Design rules for small low speed wind tunnels," *The Aeronautical Journal* 83(827), Nov 1979, pp. 443–449. doi:10.1017/S0001924000031985 | Rules for every component of a small blower tunnel (fan, screens, diffusers, honeycomb, settling chamber, contraction, working section) and the power-factor estimate for fan sizing | Reviewed 2026-10-30 | [PDF](Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf) (PDF pages 8–11 are an unrelated note), [notes](notes/Mehta1979.md) |

## Videos and web pages

Not stored here: videos stay out of Git (D-004). Summaries come from transcripts the owner provided.

| Reference | What it shows | Notes |
|---|---|---|
| Aki (YouTube), DIY wind tunnel water-mist generator, two videos: [video 1](https://www.youtube.com/watch?v=Xa4YN12IiHg), [video 2](https://www.youtube.com/watch?v=7Zdn8moAwxE). Upload dates not recorded. Added 2026-10-30. | A 3D-printed box with an ultrasonic mist maker sitting in water. The air intake is high and the mist outlet low, because the mist sinks. A rubber tube carries the mist to the inlet of a desktop **suction** tunnel (fan at the back), which draws it in. | Lessons from the videos: the lid has a downward-pointing pyramid to stop splashing; the water level must stay below the outlet or the mist stops; the mist thins and fades at high tunnel speed. The video description links a "variable fan" and a "mist maker" through Amazon short links that could not be opened from here, so the products are unidentified. Assessment and plan: TODO.md, P2 "flow visualization". |

## Adding a paper

1. Save the PDF here as `<Key>_<short-title>.pdf`. Key = first author's surname + year (add `a`, `b` if two
   clash); short title in lowercase words joined by hyphens.
2. Add a row to the index with status **Not yet reviewed**.
3. When it has been read, write `notes/<Key>.md` from the template below and set the status to **Reviewed YYYY-MM-DD**.
4. If it changes the design, record that in DECISIONS.md or PROJECT_BACKGROUND.md and cite the notes file.

```markdown
# <Key>: <title>

- Citation:
- Copy in this folder: <file name>; original file name; version (preprint / in press / final)
- Reviewed: <date>, <what was read: full text, figures, appendices>

## What they did
## Key numbers (units; page, figure or table)
## Limitations and caveats
## What it suggests for this project [Proposed]
## References worth following up
```

## Rules

- Notes state what the source says, with page, figure or table numbers. Keep our own inferences and arithmetic
  separate and label them.
- Files over 25 MB are not committed; store them externally and link them here ([DECISIONS.md](../DECISIONS.md) D-004).
  PDFs are stored as binary (`.gitattributes`).
- The repository is private (D-003, Tentative). Before making it public, check each paper's licence and replace any
  PDF that may not be redistributed with a link.

## Wanted

Recommended next, in priority order. Citations and availability were checked online on 2026-10-30; nothing below has
been read yet.

**Get now (free):**

1. J. Weakly, S. Ho, E. Feehery, B. D. Kothmann, C. Sung (University of Pennsylvania), "A Low-Cost, Adaptable System
   for Lift and Drag Measurement in an Educational Wind Tunnel," ASEE Annual Conference, 2024.
   [Paper page](https://nemo.asee.org/public/conferences/344/papers/41981/view).
   - The closest match to this project: a force balance built from HX711 load cells and an Arduino for under $125,
     validated by measuring sphere drag.
   - Per its abstract: static-load error 2.5 % and sphere drag within about 4 % of theory.
   - Useful for balance and mount design, and for the microcontroller choice.
2. F. A. Morrison, "Data Correlation for Drag Coefficient for Sphere," Michigan Technological University, 2013.
   [PDF](https://pages.mtu.edu/~fmorriso/cm310/DataCorrelationsforExaminations2013.pdf) (exam-sheet version; the full
   handout is mirrored [here](https://galileoandeinstein.phys.virginia.edu/more_stuff/Applets/Projectile/DataCorrelationForSphereDrag2013.pdf)).
   - One explicit C_D(Re) correlation valid up to Re = 10⁶, easy to code into the analysis.
   - Candidate for the Re-matched reference (TODO P1). It is a curve fit, so it should be backed by primary data
     (item 6).
3. K. R. Cooper, "Bluff-Body Blockage Corrections in Closed- and Open-Test-Section Wind Tunnels," Chapter 6 of
   *Wind Tunnel Wall Correction*, AGARD-AG-336, 1998.
   [PDF](https://www.sto.nato.int/publications/AGARD/AGARD-AG-336/08chap06.pdf).
   - A modern review of blockage corrections (Maskell and later methods).
   - Needed to correct the sphere C_D and to choose the test-section size.
4. E. C. Maskell, "A Theory of the Blockage Effects on Bluff Bodies and Stalled Wings in a Closed Wind Tunnel," ARC
   R&M 3400, 1963. [Cranfield record](https://aerade.cranfield.ac.uk/handle/1826.2/3982),
   [DTIC PDF](https://apps.dtic.mil/sti/pdfs/ADA955243.pdf). The original bluff-body blockage theory that item 3 builds on.
5. Avia Semiconductor, HX711 datasheet (for example the copy
   [hosted on TI's forum](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/73/HX711.pdf)).
   [docs/experimental_setup.md](../docs/experimental_setup.md) quotes HX711 specs as "not yet confirmed". This
   confirms them. Check the revision number.

**Needs a library or purchase:**

6. F. W. Roos, W. W. Willmarth, "Some experimental results on sphere and disk drag," *AIAA Journal* 9(2), 1971,
   pp. 285–291. Primary sphere-drag measurements, widely used to fit C_D(Re) curves.
7. J. B. Barlow, W. H. Rae, A. Pope, *Low-Speed Wind Tunnel Testing*, 3rd ed., Wiley, 1999. The standard textbook:
   pitot-static use, balances, calibration and corrections. Already listed in PROJECT_BACKGROUND.md.
8. R. D. Mehta, "The aerodynamic design of blower tunnels with wide-angle diffusers," *Progress in Aerospace Sciences*
   18(1), 1977, pp. 59–120. The detailed data behind Mehta1979, including wide-angle diffuser and screen design.

**Lower priority:**

- J. Scheiman, *Comparison of experimental and theoretical turbulence reduction characteristics for screens,
  honeycomb, and honeycomb-screen combinations*, NASA TP-1958, 1981 ([NTRS record](https://ntrs.nasa.gov/citations/19820006182);
  full-text availability not checked). Useful when choosing screens and honeycomb.
- P. Bradshaw, R. C. Pankhurst, "The design of low-speed wind tunnels," *Progress in Aerospace Sciences* 5, 1964,
  p. 1. Mostly summarized by Mehta1979.
- T. Morel, "Comprehensive Design of Axisymmetric Wind Tunnel Contractions," *ASME J. Fluids Eng.*, June 1975,
  pp. 225–233. Contraction design charts; Bell1988 already gives a usable shape.
- Datasheets for the pressure sensor and load cell, once chosen.

When one of these is added, move it out of this list. Duplicate copies: keep the cleaner one and record the choice
in its notes file.
