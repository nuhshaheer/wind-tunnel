# Resources

Reference papers, reports and datasheets used to design the tunnel. Each item has a PDF in this folder and, once it
has been read, a notes file in `notes/` recording what it says (with page and figure numbers), its caveats, and what it
suggests for this project. Conclusions that change the design go to [DECISIONS.md](../DECISIONS.md) or
[PROJECT_BACKGROUND.md](../PROJECT_BACKGROUND.md) and cite the notes file.

Agents: read the notes file first. Open the PDF only when you need a detail the notes do not cover.

## Index

Topics for items **not yet reviewed** come from their title page or abstract only. Items added 2026-10-31 were
downloaded by the owner; their original file names are recorded in the notes (reviewed items) or here.

| Key | Reference | Topic | Status | Files |
|---|---|---|---|---|
| Abdelhamed2014 | A. S. Abdelhamed, Y. El-S. Yassen, M. M. ElSakka, "Design optimization of three dimensional geometry of wind tunnel contraction," *Ain Shams Engineering Journal*, 2014 (article in press). doi:10.1016/j.asej.2014.09.008 | Contraction ratio, length and wall profile; CFD optimization checked with a pitot-static traverse | Reviewed 2026-10-30 | [PDF](Abdelhamed2014_wind-tunnel-contraction-optimization.pdf), [notes](notes/Abdelhamed2014.md) |
| Anthoine2004 | J. Anthoine, D. Olivari, D. Portugaels, "Drag coefficient determination of bluff bodies: analysis of blockage effect," von Karman Institute Reprint 2004-24, COST Action C14 meeting, May 2004. The reprint cover lists P. Cosyn instead of J. Anthoine; the paper's own header lists Anthoine | Circular cylinders (2-D) at three blockage ratios, up to 17 %, sub- to super-critical Re; compares blockage corrections (Allen and Vincenti, Maskell). Per the abstract, no single correction works in all regimes. Cylinders, not spheres | Not yet reviewed | [PDF](Anthoine2004_bluff-body-drag-blockage-effect.pdf) (was `rp200424.pdf372046978rp200424.pdf`) |
| Barlow1999 | J. B. Barlow, W. H. Rae Jr., A. Pope, *Low-Speed Wind Tunnel Testing*, 3rd ed., Wiley, 1999. ISBN 0-471-55774-9 | The standard textbook. Chapters most relevant here: 3 (tunnel design, drive, construction), **4 (pressure, temperature and flow measurement)**, 6 (test-section calibration; **6.4 data systems**), **7 (balances)**, 9–10 (boundary corrections), **12.2 (uncertainty)**, 17 (small wind tunnels) | Not yet reviewed (contents pages only) | **Local only, not in Git:** `Barlow1999_low-speed-wind-tunnel-testing-3rd-ed.pdf` (57 MiB, over the 25 MB limit, and a commercial textbook; ignored by `.gitignore`). OneDrive copies it between the owner's machines; a fresh clone from GitHub will not have it |
| Bell1988 | J. H. Bell, R. D. Mehta, *Contraction Design for Small Low-Speed Wind Tunnels*, NASA CR-177488, Stanford University, August 1988 (also JIAA TR-84, April 1988) | Contraction wall shape (5th-order polynomial), length and separation for small tunnels; panel method + laminar boundary layer, validated on 4 tunnels | Reviewed 2026-10-30 | [PDF](Bell1988_contraction-design-small-low-speed-tunnels.pdf), [notes](notes/Bell1988.md) |
| Bradshaw1964 | P. Bradshaw, R. C. Pankhurst, "The design of low-speed wind tunnels," *Progress in Aerospace Sciences* 5, 1964, p. 1. This copy states "Crown copyright. Reprinted from NPL Aero Report 1039"; the journal details are from the earlier citation check and are not visible in its text layer | Aerodynamic and structural design of low-speed tunnels (wooden construction), with drawings and data for about thirty tunnels. Largely summarized by Mehta1979 | Not yet reviewed | [PDF](Bradshaw1964_design-of-low-speed-wind-tunnels.pdf) (was `bradshaw1964.pdf`) |
| Brown2003 | P. P. Brown, D. F. Lawler, "Sphere Drag and Settling Velocity Revisited," *Journal of Environmental Engineering* 129(3), 2003, pp. 222–231. doi:10.1061/(ASCE)0733-9372(2003)129:3(222) | 480 curated, wall-corrected sphere-drag points (Roos1971's high-Re points excluded for vibration). Recommended correlation, Eq. (19), valid for Re < 2×10⁵, with 81 % of points within ±5 %; Clift et al. (1978) reprinted. Gives C_D ≈ 0.42–0.445 at this project's Re (Morrison2013 is 7–11 % low there). Its own Fig. 3 data sit about 7 % above Eq. (19) at that Re (our pixel measurement), so the reference band there is about ±10 %. The proposed validation reference curve. ASCE copyright, personal use; keep out of a public repository | Reviewed 2026-11-02 | [PDF](Brown2003_sphere-drag-settling-velocity-revisited.pdf) (was `brown2003.pdf`), [notes](notes/Brown2003.md) |
| Cooper1998 | K. R. Cooper, "Bluff-Body Blockage Corrections in Closed- and Open-Test-Section Wind Tunnels," Chapter 6 of B. F. R. Ewald (ed.), *Wind Tunnel Wall Correction*, AGARD-AG-336, October 1998, pp. 6-1 to 6-33 | A modern review of bluff-body blockage corrections: Maskell's analysis, Cowdrey, Hackett's two-step version, wake buoyancy, Mercker; open-section methods (Mercker and Wiedemann); applications. Needed to choose the blockage correction (TODO P1) | Reviewed 2026-10-31 | [PDF](Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf), [notes](notes/Cooper1998.md). The owner printed PDF pages 332–364 of the full volume to PDF on 2026-10-31. **Image only, no text layer**; for searchable text use the full volume (Ewald1998) on this machine |
| Ewald1998 | B. F. R. Ewald (ed.), *Wind Tunnel Wall Correction*, AGARDograph 336 (AGARD-AG-336), RTO/NATO, October 1998. ISBN 92-836-1076-8. Distribution statement: "There are no restrictions on the distribution of this document" | The complete volume, 12 chapters on wall corrections. Chapter 6 is filed separately as Cooper1998 (PDF pages 332–364). The PDF's permission flags forbid page extraction and copying, so agents should not split it; print or download chapters instead | Not yet reviewed | **Local only, not in Git:** `Ewald1998_wind-tunnel-wall-correction-AGARD-AG-336.pdf` (26.1 MiB, over the 25 MiB limit; ignored by `.gitignore`). Has a text layer. Was `AGARD-AG-336-All.pdf` |
| HX711 | Avia Semiconductor, *HX711: 24-Bit ADC for Weigh Scales*, datasheet rev. V2.0 | Load-cell ADC: gains, noise, data rates, serial timing, power. Confirms the specs quoted in docs/experimental_setup.md | Reviewed 2026-10-31 | [PDF](HX711_avia-adc-datasheet-v2.pdf), [notes](notes/HX711.md) |
| Maskell1963 | E. C. Maskell, "A Theory of the Blockage Effects on Bluff Bodies and Stalled Wings in a Closed Wind Tunnel," ARC R&M 3400, November 1963 (published by HMSO, 1965; replaces RAE Report Aero 2685) | The original bluff-body blockage correction, Δq/q = ε·C_D·S/C, with ε a little above 5/2 for axisymmetric bodies (summary, report p. 1). A 27-page scan with **no text layer**: read the page images | Reviewed 2026-10-31 | [PDF](Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf) (was `arc-rm-3400.pdf`), [notes](notes/Maskell1963.md) |
| Mehta1977 | R. D. Mehta, "The aerodynamic design of blower tunnels with wide-angle diffusers," *Progress in Aerospace Sciences* 18, 1977, pp. 59–120 | The detailed data behind Mehta1979: wide-angle diffuser design charts (A against 2θ by number of screens; A < 1.14 K_sum + 1), screens, honeycombs, blower exit swirl, settling chambers. For this project's 3.44:1 fan-to-chamber diffuser: K_sum ≥ 2.1, and two screens allow about 115 mm minimum length. Screen spacing ≥ 500 wire diameters | Reviewed 2026-11-02 | [PDF](Mehta1977_blower-tunnels-wide-angle-diffusers.pdf) (was `mehta1979.pdf`, but it is the 1977 paper), [notes](notes/Mehta1977.md) |
| Mehta1979 | R. D. Mehta, P. Bradshaw, "Design rules for small low speed wind tunnels," *The Aeronautical Journal* 83(827), Nov 1979, pp. 443–449. doi:10.1017/S0001924000031985 | Rules for every component of a small blower tunnel (fan, screens, diffusers, honeycomb, settling chamber, contraction, working section) and the power-factor estimate for fan sizing | Reviewed 2026-10-30 | [PDF](Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf) (PDF pages 8–11 are an unrelated note), [notes](notes/Mehta1979.md) |
| Morel1975 | T. Morel, "Comprehensive Design of Axisymmetric Wind Tunnel Contractions," *ASME Journal of Fluids Engineering*, June 1975, pp. 225–233 | Contraction design charts for a wall of two matched cubic arcs, from inviscid flow analysis. The text layer doubles many characters; read the page images | Not yet reviewed | [PDF](Morel1975_axisymmetric-contraction-design.pdf) (was `morel1975.pdf`) |
| Morrison2013 | F. A. Morrison, "Data Correlation for Drag Coefficient for Sphere," Michigan Technological University, 2013 (2-page handout), plus the CM3110 "Data Correlations for Examinations" sheet that repeats it | One explicit C_D(Re) correlation from creeping flow up to Re = 10⁶ (a curve fit). Gives C_D ≈ 0.39 at this project's Re of 1–2.5×10⁴, not 0.47. Use the handout's Eq. (1): the exam sheet prints a different last term and a typo (236,000) | Reviewed 2026-11-02 | [handout](Morrison2013_sphere-drag-correlation.pdf), [exam sheet](Morrison2013_exam-data-correlations-sheet.pdf), [notes](notes/Morrison2013.md) (were `DataCorrelationForSphereDrag2013.pdf` and `DataCorrelationsforExaminations2013.pdf`; a byte-identical second copy, `…2013-2.pdf`, was removed) |
| Roos1971 | F. W. Roos, W. W. Willmarth, "Some experimental results on sphere and disk drag," *AIAA Journal* 9(2), February 1971, pp. 285–291. doi:10.2514/3.6164 | Towing-tank sphere and disk drag, 5 < Re < 10⁵ (Table 1), with a band of earlier data (Fig. 3). At Re 1–3×10⁴ its own points read high (vibrating shakedown rig, per the authors); the earlier-data band is about 0.38–0.45 at 10⁴ and 0.40–0.49 at 2×10⁴. The copy carries a 2013 university-library download stamp | Reviewed 2026-11-02 | [PDF](Roos1971_sphere-and-disk-drag.pdf) (was `roos1971.pdf`), [notes](notes/Roos1971.md) |
| Scheiman1981 | J. Scheiman, *Comparison of Experimental and Theoretical Turbulence Reduction Characteristics for Screens, Honeycomb, and Honeycomb-Screen Combinations*, NASA TP-1958, Langley Research Center, December 1981 | Turbulence reduction by screens, honeycomb and combinations, measured in a 0.46 m duct at 7.6–18.3 m/s and compared with theory. Screens alone: u′ ≈ 1/(1+K), v′ ≈ 1/√(1+K); a honeycomb followed by a screen is far better than screens alone. Screens ≥ 58 % open, spaced 80–100 mesh lengths | Reviewed 2026-11-02 | [PDF](Scheiman1981_screens-honeycomb-turbulence-reduction.pdf) (was `19820006182.pdf`, the NTRS id), [notes](notes/Scheiman1981.md) |
| SDP8xx | Sensirion AG, *Datasheet SDP8xx-Digital: Digital Differential Pressure Sensor*, Version 1.1, April 2019 | The proposed airspeed sensor (SDP810-125Pa): 0.08 Pa + 3 % of reading accuracy, I²C address 0x25 for every 125 Pa part, Ø3.5/5.2 mm tube barbs, 2 mm pin pitch, specs at 966 mbar. Downloaded by the agent 2026-11-08 | Reviewed 2026-11-08 (owner check pending) | [PDF](SDP8xx_sensirion-digital-dp-sensor-datasheet-v1.1.pdf), [notes](notes/SDP8xx.md) |
| Sensirion2024 | Sensirion AG, *SDP Signal Compensation*, application note, Version 1.0, June 2024 | Ambient-pressure correction for SDP differential-pressure readings: dp × 966 mbar / p_amb (×0.95 at sea level); temperature-compensation modes; condensation. Downloaded by the agent 2026-11-08 | Reviewed 2026-11-08 (owner check pending) | [PDF](Sensirion2024_sdp-signal-compensation-app-note.pdf), [notes](notes/Sensirion2024.md) |
| TAL221 | HT Sensor (HTC), *TAL221 Miniature Load Cell*, one-page datasheet (PDF dated 2018-01-04) | The proposed drag load cell (100 g): 0.6 ± 0.15 mV/V, safe overload 150 % FS, non-linearity, hysteresis, repeatability and creep ±0.05 % FS each, zero tempco ±0.1 % FS/10 °C, M3 mounting. SparkFun's copy, downloaded by the agent 2026-11-08 | Reviewed 2026-11-08 (owner check pending) | [PDF](TAL221_htc-miniature-load-cell-datasheet.pdf), [notes](notes/TAL221.md) |
| Weakly2024 | J. Weakly, S. Ho, E. Feehery, B. D. Kothmann, C. Sung, "A Low-Cost, Adaptable System for Lift and Drag Measurement in an Educational Wind Tunnel," ASEE Annual Conference, 2024, Paper ID #41981 | Two-load-cell balance (TAL220 + HX711 + Arduino Uno, about $121), validated with static loads and sphere drag (C_D within 6 % of 0.47, no blockage or mount correction) | Reviewed 2026-10-31 | [PDF](Weakly2024_low-cost-lift-drag-balance-educational-tunnel.pdf), [notes](notes/Weakly2024.md) |
| Wieghardt1953 | K. E. G. Wieghardt, "On the Resistance of Screens," *The Aeronautical Quarterly* 4, February 1953, pp. 186–192. doi:10.1017/S0001925900000871 | Screen pressure-drop formula k = c(1 − β)/β², c = 6.5·(u₁d/βν)^(−1/3) for u₁d/(βν) between 60 and 600 (the source of "Wieghardt's formula" in Mehta1977/1979). Screens stop shedding eddies below u₁d/(βν) ≈ 85. Cambridge Core download stamp; keep out of a public repository | Reviewed 2026-11-02 | [PDF](Wieghardt1953_resistance-of-screens.pdf) (was `wieghardt1953.pdf`), [notes](notes/Wieghardt1953.md) |

## Videos and web pages

Not stored here: videos stay out of Git (D-004). Summaries come from transcripts the owner provided.

| Reference | What it shows | Notes |
|---|---|---|
| Aki (YouTube), DIY wind tunnel water-mist generator, two videos: [video 1](https://www.youtube.com/watch?v=Xa4YN12IiHg), [video 2](https://www.youtube.com/watch?v=7Zdn8moAwxE). Upload dates not recorded. Added 2026-10-30. | A 3D-printed box with an ultrasonic mist maker sitting in water. The air intake is high and the mist outlet low, because the mist sinks. A rubber tube carries the mist to the inlet of a desktop **suction** tunnel (fan at the back), which draws it in. | Lessons from the videos: the lid has a downward-pointing pyramid to stop splashing; the water level must stay below the outlet or the mist stops; the mist thins and fades at high tunnel speed. The video description links a "variable fan" and a "mist maker" through Amazon short links that could not be opened from here. The mist maker is still unidentified. **The fan is probably identified (2026-11-01):** the owner's link to Amazon item B092C65F3P carries Aki's affiliate tag (`akitechspace-20`). The item is a Qirssyn 120 mm computer fan with an AC plug and a speed controller. Retailer listings give model QYN1225BSP1, about 95 CFM at 3000 RPM; some list a two-fan version. That is far too small for this project's tunnel ([session log](../docs/sessions/2026-11-01-parts-review-and-kit-inventory.md)). Assessment and plan: TODO.md, P2 "flow visualization". |

## Adding a paper

1. Save the PDF here as `<Key>_<short-title>.pdf`. Key = first author's surname + year (add `a`, `b` if two
   clash); for a datasheet, Key = the part number (e.g. `HX711`). Short title in lowercase words joined by hyphens.
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
- Files over 25 MB are not committed ([DECISIONS.md](../DECISIONS.md) D-004). Either store them externally and link
  them here, or keep them in this folder with a `.gitignore` entry and list them in the index as "local only", in
  backticks rather than as a link (so the link check passes on a fresh clone). See D-006 (Tentative). PDFs are
  stored as binary (`.gitattributes`).
- The repository is private (D-003, Tentative). Before making it public, check each paper's licence and replace any
  PDF that may not be redistributed with a link.

## Wanted

Rewritten 2026-10-31. The owner has added everything on the 2026-10-30 list (the last item, AGARD-AG-336 chapter 6,
is Cooper1998 in the index). Citations and availability below were checked online on 2026-10-31. Nothing below has
been read yet, and spec values quoted here come from vendor pages or search summaries, not from datasheets in this
folder: confirm them in the datasheet before using them.

**Electronics (free). The parts were chosen on 2026-11-08; what is still wanted is marked below:**

1. **Differential pressure sensor candidates.** This is the biggest gap: q enters C_D directly, and dynamic pressure
   is only about 15–240 Pa. Our arithmetic (ρ = 1.2 kg/m³): a ±125 Pa sensor reads up to about 14 m/s, ±249 Pa about
   20 m/s, ±500 Pa about 29 m/s. **Chosen 2026-11-08: one SDP810-125Pa** (ordered 2026-11-09), so the SDP3x and
   HSC datasheets below are no longer needed.
   - Sensirion SDP3x, digital I²C, temperature compensated: SDP32 (±125 Pa) and SDP31 (±500 Pa). Sensirion's catalog
     lists zero-point accuracy 0.08 Pa (SDP32) and 0.1 Pa (SDP31).
     [SDP32 catalog page](https://sensirion.com/products/catalog/SDP32) (datasheet linked there).
   - Honeywell TruStability HSC, ±1 inH₂O (±249 Pa) differential, I²C, for example HSCDRRN001ND2A3 (3.3 V) or
     …2A5 (5 V). Get the official HSC datasheet from Honeywell; distributor listings disagree on accuracy and
     temperature range.
   - Added 2026-11-01: **Sensirion SDP810-125Pa and SDP810-500Pa.** **Datasheet filed 2026-11-08 as SDP8xx** (see the
     index). It corrects two points above: the sensor has four solder pins at 2 mm pitch, not a cable connector
     (Sensirion recommends its "SDP800 series cap" for cable mounting), and its supply range is 2.7–5.5 V. Its
     accuracy is 0.08 Pa + 3 % of reading, as the reseller said. The SDP31 is listed as a 3.3 V part, and SparkFun's
     SDP31 breakout is retired.
   - Not suitable: drone airspeed kits built on the TE MS4525DO (±1 psi ≈ ±6.9 kPa; total error band ±1 % of span
     per TE's datasheet as summarized online). The owner found an FPVDrone PX4 kit ($49.99) of this type on
     2026-11-01; its chip is not named in the listing.
2. **Load-cell candidates.** HTC TAL220 (10 kg, the cell Weakly2024 used) and the TAL221 mini family (100 g to
   1.5 kg). **TAL221 datasheet filed 2026-11-08** (see the index): it confirms 0.6 mV/V and 150 % safe overload for
   the 100 g cell, and gives creep and the temperature coefficients. Still wanted: the TAL220 datasheet, only if a
   larger cell is ever considered. The noise trade-off is worked out in [notes/HX711.md](notes/HX711.md).
3. **Datasheets for the parts on hand:** TI [LM741](https://www.ti.com/product/LM741),
   [LM348](https://www.ti.com/product/LM348) (combined LM148/LM248/LM348 datasheet) and
   [LM317](https://www.ti.com/product/LM317). Needed for the TODO P1 task "decide the role of the op-amp circuit".
   Added 2026-11-01, also in the owner's kit:
   - TI [LMC6484](https://www.ti.com/product/LMC6484). TI's page title: "Ultra-low Bias Current, Precision CMOS
     Rail-to-Rail Input and Output Quad Operational Amplifier", 3–15 V supply. It is the single-supply op-amp option.
   - LM7805CT (5 V, 1 A regulator in TO-220), first proposed for a servo supply (no servo is planned since the owner
     chose preset angles, 2026-11-01). Distributors list it under onsemi
     (formerly Fairchild) and mark it obsolete, so take the datasheet from onsemi or from the
     [DigiKey listing](https://www.digikey.com/en/products/detail/onsemi/LM7805CT/458698). TI has no LM7805 product
     page.
4. **Ambient pressure and temperature for air density:** Bosch BME280 (I²C pressure, temperature and humidity).
   Vendor pages give about ±1 hPa absolute pressure accuracy, about 0.1 % in ρ (our arithmetic).
   [Datasheet copy hosted by SparkFun](https://cdn.sparkfun.com/assets/5/3/0/f/7/BME280_Datasheet.pdf); prefer the
   current revision from Bosch Sensortec. **Still wanted:** the Waveshare BME280 board is ordered (2026-11-09).

**Electronics background (free; useful, not blocking):**

5. M. Tomin, M. Scipioni, B. Gatti, "Design, construction and testing of a 3-component force balance for educational
   wind tunnels in undergraduate aerodynamics," *J. Aviation/Aerospace Education & Research* 29(1), 2020,
   pp. 89–105, doi:10.15394/jaaer.2020.1809. [Open access](https://commons.erau.edu/jaaer/vol29/iss1/5). Arduino-based
   balance; Weakly2024's ref. [2].
6. S. Post, M. Morris, "Force balance design for educational wind tunnels," ASEE Annual Conference, 2010.
   [ASEE PEER](https://peer.asee.org/15891). Two-load-cell balance with a sting-drag measurement; Weakly2024's ref. [1].
7. K. Hoffmann, *An Introduction to Stress Analysis using Strain Gauges*, HBM. Free PDF from HBK; a free account may
   be needed. [HBM reference-literature page](https://www.hbm.com/index.php?id=112). Bridge circuits, excitation and
   temperature compensation: the theory inside a load cell.
8. W. Kester, J. Bryant, M. Byrne, "Grounding Data Converters and Solving the Mystery of 'AGND' and 'DGND',"
   Analog Devices tutorial MT-031, Rev. A, 2008.
   [PDF](https://www.analog.com/media/en/training-seminars/tutorials/mt-031.pdf). Grounding and layout for the ADC
   board, which will sit near a fan motor.
9. Dwyer Instruments, Series 160 stainless steel pitot tubes, Bulletin H-11.
   [Distributor copy](https://core.instrumart.com/assets/Dwyer-160-datasheet.pdf). Geometry and use of a standard
   pitot-static tube, if one is bought rather than made.
10. B. N. Taylor, C. E. Kuyatt, *Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement
    Results*, NIST Technical Note 1297, 1994 edition. [NIST page](https://www.nist.gov/pml/pubs/tn1297/index). Short
    and practical, for the C_D uncertainty budget (Barlow1999 §12.2 covers the same ground).

**Added 2026-11-02, after the Morrison2013 / Roos1971 / Mehta1977 review:**

11. **A tabulated sphere C_D reference for Re = 10⁴–3×10⁴.** Morrison2013 is a curve fit (C_D ≈ 0.39 here), and the
    only data in Roos1971 at this Re are flagged by the authors as reading high. The band of earlier data is a small
    figure that the owner and the agent read differently. **Answered by Brown2003**, added 2026-11-02 (see the
    index). Optional now: R. Clift, J. R. Grace, M. E. Weber, *Bubbles, Drops, and Particles*, Academic Press, 1978.
    Brown2003 reprints its correlation (Table 2), so the book is needed only for its data tables.

(Wieghardt 1953, item 12 of the 2026-11-02 list, was added the same day: see the index.)

**Needs a library or purchase:**

- S. F. Hoerner, *Fluid-Dynamic Drag*, 1965. Weakly2024's source for C_D = 0.47. Low priority now that Roos1971 and
  Morrison2013 are here.

**Later:** datasheets for the chosen fan or blower, pressure sensor and load cell. For the microcontroller (Elegoo
Mega 2560 R3, 2026-11-01): Arduino's Mega 2560 Rev3 documentation and pinout, needed for the interface board.

When one of these is added, move it out of this list. Duplicate copies: keep the cleaner one and record the choice
in its notes file.
