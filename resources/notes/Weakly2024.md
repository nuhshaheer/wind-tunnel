# Weakly2024: A low-cost, adaptable system for lift and drag measurement in an educational wind tunnel

- Citation: J. Weakly, S. Ho, E. Feehery, B. D. Kothmann, C. Sung (University of Pennsylvania), "A Low-Cost,
  Adaptable System for Lift and Drag Measurement in an Educational Wind Tunnel," ASEE Annual Conference & Exposition,
  2024, Paper ID #41981. [Paper page](https://nemo.asee.org/public/conferences/344/papers/41981/view).
  Fabrication files and code: https://sung.seas.upenn.edu/publications/wind-tunnel-force-balance/ (per the paper;
  not opened).
- Copy in this folder: [Weakly2024_low-cost-lift-drag-balance-educational-tunnel.pdf](../Weakly2024_low-cost-lift-drag-balance-educational-tunnel.pdf)
  (15 MB, 23 pages). The owner added it on 2026-10-31 as `ASEE_Wind_Tunnel_Paperfinal.pdf`. Final conference version.
- Reviewed: 2026-10-31 by Claude Code. Read the full text. Checked against page images: Table 1 (cost, p. 7) and
  Fig. 2 (circuit, p. 6). Other figures were read from their captions and text only.

## What they did

Built a two-component (lift and drag) force balance for an existing AEROLAB educational tunnel (12 in × 12 in test
section, about 305 mm square), checked it with static loads, measured sphere drag, characterized wings, and used it in
a sophomore lab.

**Hardware** (§2–3, Table 1, Fig. 2):

- Two **TAL220 10 kg straight-bar load cells**, rigidly coupled at right angles by a machined aluminium bracket: the
  vertical cell reads drag, the horizontal one lift. Earlier versions with rods to separate the axes suffered friction
  and did not return to zero (§3).
- Two **SparkFun HX711 breakouts (SEN-13879)**, one per load cell, and an **Arduino Uno**. Wiring (Fig. 2): drag
  HX711 DAT → pin 4, CLK → pin 5; lift HX711 DAT → pin 6, CLK → pin 7; both modules' VDD and VCC on the Uno's 5 V.
- Data: the Arduino prints drag (g), lift (g), a trial number and time (ms) over USB serial at 57600 baud. The trial
  number is set from the keyboard to flag steady sections. Logged with the serial monitor or PuTTY, then saved as CSV
  (§3.3).
- Sting: a steel beam 220 mm long and 1.6 mm thick (waterjet cut), on 3D-printed connectors and 6.35 mm acrylic
  plates. For the wing tests the sting was 6.35 mm thick.
- Cost (Table 1): HX711 2 × $10.95, TAL220 2 × $9.50, Arduino Uno $32.00, materials $48.57; total printed as $121.40.
  The rows add up to $121.47 (our arithmetic).

**Calibration** (§3.1): each load cell calibrated with SparkFun's code: clamp one end, apply a known load, record the
scale factor. Repeating it six times with three weights, assembled and separately, showed no significant difference
(t-test, 5 % level). They note calibration values "change slightly over time and with environmental changes" and
should be repeated periodically.

**Noise lesson** (§3.1, §3.4, Fig. 2 caption): the signal was noisy and drifting until the load-cell wires were
**soldered directly to the HX711**. A breadboard between the load cell and the amplifier added noise.

## Key numbers

| Test | Result | Source |
|---|---|---|
| Off-axis loading of one TAL220 (0, 200, 0, 50, 0 g in six orientations) | Mean squared error of off-axis readings 0.30 g | §4.1, Fig. 3 |
| Repeatability at a fixed load | Standard deviation averaging 0.05 g | §4.2.1 |
| Static loads 20–200 g at 0–90° | Drag MAPE 1.6 %, lift 0.8 % (standard and reverse combined); max error 5.7 % | Table 2 |
| Same, with a 55 mm offset (cantilever torque) | Drag MAPE 2.5 %, lift 1.3 %; max error 7.6 % | Table 2 |
| Sphere drag, 63.5 mm (2.5 in) sphere printed on a Fortus 450mc, 6.5–20.5 m/s, Re 3.4×10⁴ to 1.1×10⁵ | C_D = 0.4946, 0.4424, 0.4865, 0.4764 against 0.47; all within ±6 %, mean absolute error 4 % | Table 3, §5.1 |

- Airspeed came from a Dwyer Mark II inclined manometer, v = 20.4952 √P_v (P_v in inches of water), assuming 25 °C and
  1 atm (Eq. 4). No air density was measured.
- The reference C_D = 0.47 is from Hoerner (1965), "for Reynolds numbers between 10⁴ and 10⁶".

## Limitations and caveats

- **The sphere test had no mount-drag subtraction and no blockage correction.** The sting was "assumed to have a
  minimal influence" for the sphere (§5.2); sting drag was subtracted only for the wing tests. Our arithmetic: the
  sphere's blockage S/C was about 3.4 % (63.5 mm sphere in a 305 mm square section). Maskell's correction
  Δq/q = ε·C_D·S/C, with ε a little above 5/2 for axisymmetric bodies (Maskell1963, summary on p. 1 of the report),
  gives Δq/q ≈ 2.5 × 0.47 × 0.034 ≈ 4 %. So their uncorrected C_D reads about 4 % high from blockage alone, and the 4 %
  agreement may hide offsetting errors. Agreement is not proof of accuracy.
- Airspeed came from a manometer at an assumed density; reading resolution at 0.1 inH₂O (lowest speed) is coarse.
  Their worst C_D error (−5.9 %) was at 10 m/s, not the lowest speed.
- Four sphere points, one run each, no uncertainty analysis.
- The "0.05 g" standard deviation is not clearly defined (per sample or per loading condition).
- The instructor reported the sting-plus-model natural frequency came close to the vortex-shedding frequency at some
  speeds (§6.2, Q5). A stiffer sting was recommended.
- Their load cells (10 kg) are 250 to 2500 times larger than the forces measured (about 4–40 gf; our arithmetic from
  Table 3 with their ρ = 1.225 kg/m³). It worked, but leaves the HX711 noise floor as a larger fraction of the signal (see the HX711 notes).

## What it suggests for this project [Proposed]

1. **A proven, cheap electronics chain:** bar load cell → one HX711 per cell → Arduino-class microcontroller → USB
   serial → CSV. This answers part of open question 1 (microcontroller/DAQ) as a baseline: an Arduino Uno is enough
   for two HX711s. A pressure sensor on the same board still needs checking (interface, voltage level).
2. **Solder the load-cell leads to the HX711.** No breadboard in the bridge wiring.
3. **Log raw counts plus a timestamp and a run flag**, not just calibrated grams. Their trial-number flag is a good
   idea; keep calibration in analysis scripts so it can be redone from raw data.
4. **Do what they skipped:** subtract mount drag (sphere removed, sting alone, same speeds), correct for blockage
   (Maskell1963 / AGARD-AG-336 chapter 6), measure ambient p and T for density, and repeat runs to get an
   uncertainty. That is how this project can do better than their 4 %.
5. **Consider a smaller load cell** than their 10 kg one. Our expected drag is about 2–8 gf for a 150 mm section
   (estimates). See the noise table in [HX711.md](HX711.md). Trade-off: overload margin while handling.
6. **Make the sting stiff** and check its natural frequency against the sphere's shedding frequency at test speeds.
7. **Rigid coupling** instead of sliding or pivoting parts, if lift is ever measured (airfoil step).

## References worth following up

- S. Post, M. Morris, "Force balance design for educational wind tunnels," ASEE Annual Conference & Exposition, 2010
  ([ASEE PEER](https://peer.asee.org/15891)). Their ref. [1]; a two-load-cell balance about $1000.
- M. Tomin, M. Scipioni, B. Gatti, "Design, construction and testing of a 3-component force balance for educational
  wind tunnels in undergraduate aerodynamics," *J. Aviation/Aerospace Education & Research* 29(1), 2020, pp. 89–105,
  doi:10.15394/jaaer.2020.1809 ([open access](https://commons.erau.edu/jaaer/vol29/iss1/5)). Their ref. [2]; Arduino
  based, similar components.
- S. F. Hoerner, *Fluid-Dynamic Drag*, 1965. Their C_D = 0.47 source (book; library or purchase).
- SparkFun HX711 hookup guide (their ref. [12]); see [HX711.md](HX711.md).
