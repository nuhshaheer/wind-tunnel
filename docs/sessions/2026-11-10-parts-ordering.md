# 2026-11-10: Parts ordering

- **Session ID:** 6e929582-3315-40a6-9c63-d9ec3312aea9 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** `f4fa904` (the wrap); the README follow-up (§13, end) not committed yet

Started 2026-11-09, wrapped 2026-11-10. Buying advice and documentation only. **The owner ordered everything on the
buy list except the fan.** Nothing arrived, was built or was tested.

## 1. Starting state and objective

- `/catchup` on 2026-11-09: `UP_TO_DATE` at `c768e2c` (the owner had committed and pushed the fan-advice session).
  Working tree clean. `check_docs.py` 0 failures, 0 warnings; 20 tests OK in 13.2 s.
- Discrepancies found at catch-up: PROJECT_STATUS still called the fan-advice session "Not committed yet" (normal
  post-commit lag); `docs/experimental_setup.md` still gave the settling chamber as 230–300 mm and two diffuser screens
  (the status had the newer 380–390 mm and three). Both fixed or superseded this session (the first in this wrap).
- No set objective: the owner raised a backlight idea mid-catch-up, then spent the session ordering parts and asking
  about each listing.

## 2. Work completed

**Orders recorded** (owner's reports, 2026-11-09/10; tracker [docs/shopping_list.md](../shopping_list.md)):
- 2026-11-09: Sensirion SDP810-125Pa (Mouser; part number to confirm); two TAL221 100 g and the SparkFun HX711
  (SparkFun); Waveshare BME280; Dupont jumpers; TUOFENG 24 AWG silicone hook-up wire (6 colours × 30 ft, $15.79);
  stainless M3/M4 assortment.
- Reported 2026-11-10: foam weatherstrip tape; 1/8 in silicone tubing; barbed connectors; 1/4 in vinyl tubing; barbed
  reducers; a 20-pack of stick-on polyurethane feet (0.78 × 0.38 in); a 0.7–3.0 mm drill-bit set and a pin vise; an
  LR44; two K&S 1/8 in OD brass tubes; two 1/8 in brass rods; a tube cutter; two 12 × 12 in neoprene sheets; Delrin
  balls (a pack of 10 each, 3/4 in and 1 in); 1/8 in cast acrylic (sheet size not recorded); M3 brass heat-set
  inserts (size not recorded); the 10 mg–100 g weight set; 4 kg of black PLA; duct tape; 220–600 wet/dry sandpaper; an
  acrylic scoring knife; Sharpies and tape; 40 tin-plated breakaway header strips ($10).
- **Not bought:** the fan (bought last); the 4-core cable (optional: four twisted hook-up wires do the job); brass M3
  screws and the 5/32 in tube (not needed); the spring bender (optional). "Check house" items not yet reported.
- Prices paid are mostly not recorded.

**Advice given, with outcome:**
- **Backlight in the test chamber (owner):** the agent first proposed a backlight behind the far side window, outside
  the flow (heat at the load cell, PWM noise in the HX711 leads, a 2–3 mm strip being a wall step). The owner said the
  light is only for mist and wants it shining down through the top, like a display case lit from its top front edge,
  designed at the end. That geometry suits mist (light from above, black background); a backlight washes mist out.
  Recorded in TODO P2 (mist item).
- **BME280:** a WatangTech copy ($14.30) names an RT9193-33 regulator (2.5–5.5 V input) but not level shifting; the
  owner ordered the Waveshare original, whose maker states an onboard 3.3/5 V level translator. Arrival check added:
  with only 5 V and GND connected, SDA and SCL should read about 5 V; then chip ID 0x60.
- **4-core cable:** the owner's "4-core cable tuofeng 24awg" turned out to be the hook-up wire set; recorded as such,
  the cable made optional.
- **Sandpaper:** a 1 in emery roll works but is slow on the curved contraction; a wet/dry sheet pack was advised; the
  owner bought 220–600 grit. Sand PLA wet.
- **Barbed fittings:** plastic is fine; size for 1/8 in ID tubing, not aquarium 3/16 in; at least 10 tees.
- **Rubber feet:** the owner chose the 20-pack (polyurethane, "soft" per the listing) over a "super soft" 4-pack;
  the neoprene collar sleeve does most of the isolating, and the 4-pack is the upgrade if the fan-on noise test shows
  vibration.
- **Brass M3 screws dropped:** estimate below; stainless is fine at the balance.
- **Wall pressure taps:** print the stub socket and a pilot dimple; drill the 0.8–1.0 mm hole with the pin vise;
  flatten the inside edge on 400–600 wet/dry. The M taps matter most (their error enters q at the model directly).
- **Drill bits:** no cheap single set covers 0.8–1.0 mm and 3.0–3.1 mm; inch equivalents recorded (1/32 in or #60–#67
  for taps; #31 for the press fit; not 7/64 or 1/8 in). The owner bought a 0.7–3.0 mm set.
- **Sting (D-016, Tentative):** the owner wanted to avoid the 5/32 in tube (delivery 2026-11-19). The agent proposed
  one full-length 1/8 in sting per ball, since D-015 already lifts the sting out; the owner bought two rods.
- **K&S not required:** any brand with the right sizes (1/8 in OD tube with about 0.014 in wall; true 1/8 in rod).
- **Bender:** none needed now; only the probe bends, and a straight probe through the open exit may avoid it (idea
  for sizing); a printed jig with sand fill is the free fallback.
- **Acrylic:** 8 × 10 in sheets were judged short (254 mm) and often thin or styrene; 8 × 12 in at 1/8 in was judged
  good. Which sheets were ordered is not recorded.
- **Neoprene:** one 12 × 24 in sheet would do; the owner bought two 12 × 12 in sheets, so the collar wrap is two
  ~240 mm pieces butted end to end.
- **Calibration masses:** typical hooked sets start at 10 g, too heavy for the 0.2–3 g check; home-made solder hooks
  were suggested. The owner bought the 10 mg–100 g set; masses hang in a pan on a thread from the printed hook.
- **Delrin balls:** needed? Not strictly; Delrin is the cheapest that is precise, drillable, light and stable
  (aluminium the only real alternative; steel cannot be drilled; nylon swells). Sold in tens; the spares serve
  drilling practice and press-fit trials.
- **Fan:** other uses of an inline fan listed (printer and solder fume venting, ventilation); they do not separate the
  S6 from the VEVOR. The owner will buy the fan last; advice: once the airspeed readout works, so the 30-day return
  window covers the top-speed and noise tests. The fan inlet becomes a separate printed ring.
- **Header strips:** not needed until the PCB; tin plating is fine (no microvolt signal through a header). Bought anyway.

## 3. Files and equipment affected

- `PROJECT_STATUS.md`: header (last commit `c768e2c`), stage, parts chosen, §3 rows (sensors, tools, acrylic, pitot,
  fan joint), budget, §6 work completed, §8 estimate pointer, §9 blockers, open questions 1, 9, 12 and new 16, §11
  magnet finding, §12 next steps, §13 remote.
- `TODO.md`: P0 order task replaced by a reporting task; P1 sizing notes (taps, sting, straight probe, inlet ring,
  fasteners); P2 lighting for mist and arrival checks; Done entries.
- `DECISIONS.md`: D-016 appended.
- `README.md` (owner asked after the wrap; not in `f4fa904`, see the follow-up in §13): status banner, hardware (on hand, ordered, still to buy, changed
  from the original plan), build order marker, the Re-matched C_D in the deliverable, shopping-list description,
  Python version.
- `docs/buy_list.md`: statuses of every ordered row; BME280, sting, sleeve, fasteners, feet, drill sizes, magnets note,
  calibration attachment.
- `docs/shopping_list.md`: rewritten statuses (2026-11-10).
- `docs/experimental_setup.md`: current configuration, airspeed and ambient sensor rows, validation-sphere row,
  change history.
- `docs/sessions/SESSION_LOG.md`, this log; `docs/sessions/2026-11-09-fan-advice-and-screen-order.md` (commit
  backfilled).
- Not updated: `docs/drawings/` (still shows the 5/32 in sleeve and the Adafruit BME280; parts statuses not tracked
  there), left for the sizing update.
- Equipment: none changed; parts ordered, none received.

## 4. Experimental procedures performed

None. No physical work this session.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch        # 2026-11-09 and 2026-11-10: STATE: UP_TO_DATE
python scripts/check_docs.py                 # after each round of edits: 0 failures, 0 warnings
python -m unittest discover -s tests -v      # see §7
```

Magnet pull estimate (run once, 2026-11-09; dipole on-axis field, force on a linearly magnetised rod):

```bash
python -c "
import math
mu0=4e-7*math.pi
Br=1.2                      # T, typical N35-N42 neodymium (assumed)
V=math.pi*(4e-3)**2*2e-3    # 8 x 2 mm disc
m=Br*V/mu0                  # dipole moment, A m^2
Vs=math.pi*(1.5e-3)**2*10e-3  # M3 x 10 screw as a 3 mm rod
for chi in (0.05, 50):      # weakly magnetic stainless / worst-case plain steel
  for r in (0.06, 0.10, 0.13):
    B=mu0/(4*math.pi)*2*m/r**3          # on-axis field (worst direction)
    gradB2=6*B**2/r                     # d(B^2)/dr = 2B*3B/r
    F=chi*Vs/(2*mu0)*gradB2
    print(f'chi={chi:5}  r={r*1000:4.0f} mm  B={B*1e6:6.1f} uT  F={F*1e6:.2e} uN  = {F/9.80665e-5*100:.4f} % of 0.01 gf')
print('m =',round(m,4),'A m^2')
"
```

A scratch script (`mark_ordered.py`, in the session scratchpad, not kept) set the status cell of 20 rows of
`docs/buy_list.md` at once; its edits are in the diff. Web searches (standard mode): the WatangTech BME280 (no spec
page found), the RT9193 input range, Waveshare BME280 price and translator, drill-bit sets (0.5–3.5 mm, 1–6 mm by
0.1 mm, pin-vise kits). Sources are listed in the conversation answers; none was filed in `resources/`.

## 6. Measurements and results

No measurements. Estimates (our arithmetic, assumed inputs stated; not results):

| Quantity | Value | Basis |
|---|---|---|
| Field of one 8 × 2 mm magnet | about 89 µT at 60 mm, 19 µT at 100 mm, 9 µT at 130 mm | dipole, Br 1.2 T assumed (§5) |
| Pull on an M3 × 10 screw at 60 mm | about 0.001 µN (χ 0.05, weakly magnetic stainless); about 1.1 µN (χ_eff 50, plain steel) | §5; 1 µN is about 1 % of 0.01 gf (98 µN) |
| Air heating by a 5 W light in the airstream | about 0.03 °C at 13 m/s | 5 W / (1.2 × 13 × 0.01 kg/s × 1005 J/kg K) |
| Load-cell zero shift per °C | 0.01 g: 3.3 % of 0.30 gf, 0.8 % of 1.27 gf | TAL221 tempco ±0.1 % FS/10 °C |
| Drag signal at the HX711 input | about 9–70 µV for 0.3–2.3 gf | 0.6 mV/V at an assumed 5 V excitation |
| Humidity effect on density | about 0.5 % at 50 % RH, 22 °C; airspeed and Re about 0.25 % | 0.378 p_v/p, p_sat about 2.64 kPa |
| BME280 temperature error ±1 °C | 0.34 % in density, 0.17 % in airspeed | 1/295 K |
| Press-fit interference on the 1/8 in (3.175 mm) stem | 3.0 mm: 0.175 mm; 3.1 mm: 0.075 mm; #31 (3.05 mm): 0.127 mm; #32 (2.95 mm): 0.229 mm; 7/64 in (2.78 mm): 0.40 mm; 1/8 in: 0 | diameter differences |
| Ball mass, 3/4 in / 1 in | Delrin 5.1 / 12.1 g; aluminium about 9.8 / 23 g; steel about 28 / 67 g; nylon about 4.1 / 9.8 g | volume × density |
| 1/8 in tube, 0.014 in wall, as a sting | about 36 % less stiff than solid rod | (D⁴ − d⁴)/D⁴ = 0.637 |
| Solder per gram (0.8 mm, lead-free assumed 7.4 g/cm³) | about 3.7 g/m: 0.2 g ≈ 5 cm, 1 g ≈ 27 cm | for home-made small masses |
| Rubber feet 0.78 × 0.38 in vs 0.75 × 0.30 in | about 15 % softer | k ∝ area / height, same rubber assumed |
| Collar wrap length | about 480 mm | π × 152 mm |
| School balance readability needed | 0.2 g mass to 1 % needs 0.001 g readability; 0.01 g gives about ±5 % | open question 16 |

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests -v`: 20 tests OK in 13.2 s (catch-up, 2026-11-09) and 10.3 s (wrap,
  2026-11-10), Python 3.11.0.
- `python scripts/check_docs.py`: 0 failures, 0 warnings after every round of edits and at the wrap (§13).
- Not performed: any physical check. No part has arrived; every arrival check (TODO P2) is still to do.

## 8. Errors, failed approaches and troubleshooting

- **Wrong order recorded, then corrected:** "4-core cable tuofeng 24awg" was first recorded as a TUOFENG 4-core
  cable; the owner's photo showed the 6-colour hook-up wire set. Rows corrected the same day.
- **A search missed lines:** a `grep "5/32" | grep -v "...DECISIONS.md"` filter also dropped lines that merely link to
  DECISIONS.md, hiding two mentions in PROJECT_STATUS and one in experimental_setup. Found by searching again per file.
  Lesson: filter by path (`--exclude`), not by line content.
- **A table row gained a column:** the buy list's "Tube labels" row got an extra cell; caught by counting pipes and
  fixed.
- **No spec page for the WatangTech BME280** was found; the owner bought the Waveshare original instead.
- The drawing package was not updated (sleeve, BME280 brand); deliberate, left for sizing.

## 9. Decisions and reasoning

- [D-016](../../DECISIONS.md) (Tentative): one full-length sting per ball; the 5/32 in sleeve dropped.
- Owner's choices (recorded in the buy list and tracker, not as D-entries): the Waveshare BME280; stainless screws at
  the balance (agent's estimate); the fan bought last; the 20-pack feet; the 0.7–3.0 mm drill set; 2 × 12 × 12 in
  neoprene; the 10 mg–100 g weight set; 4 kg black PLA; tin header strips; the mist light from the top, designed later.

## 10. Open questions and blockers

- Which acrylic sheets were ordered; the heat-set inserts' length and outside diameter; the SDP810 part number on the
  Mouser order; the owner's list once named "Adafruit BME280" (taken as the Waveshare ordered 2026-11-09).
- Whether the drill set came with a pin vise (both were reported bought); which Dupont jumpers; prices paid.
- Filament amounts on hand and the "check house" items: still not reported.
- What the school balance reads to (open question 16).
- The fan model (D-011, Tentative), needed before the fan stand is designed.

## 11. Remaining tasks

- Owner: commit and push (§13); send the sizing inputs above; report filament and check-house items; mark parts "Got
  it" and do each arrival check; choose the fan.
- Agent: build step 1 (sizing), with this session's inputs: one sting per ball (D-016), the inlet as a separate ring,
  printed tap pilots, the straight-probe idea, windows up to 305 mm long (either acrylic option allows that), and
  updating the drawings (sleeve, BME280, statuses).

## 12. Recommended first task for the next agent

Start build step 1 (sizing) as the previous logs recommend: the settling-chamber spacing and how the 250 mm sections
split in cross-section for the 256 mm bed (PROJECT_STATUS open questions 13 and 15). Ask the owner first for the
heat-set insert size and the acrylic sheets, since the frames and holes depend on them. If the owner reports parts
arriving, record each arrival check in `docs/experimental_setup.md` first.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `c768e2c`; nothing staged; 8 files modified and 1 new (this log).

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add PROJECT_STATUS.md TODO.md DECISIONS.md docs/buy_list.md docs/shopping_list.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-09-fan-advice-and-screen-order.md docs/sessions/2026-11-10-parts-ordering.md
git status
git diff --cached --stat
git commit -m "Record parts orders and sting, sensor and fastener changes" -m "The owner ordered everything on the buy list except the fan, which is bought last so its return window covers the real test. Records the Waveshare BME280 in place of the Adafruit, stainless screws at the balance (panel-magnet pull estimated negligible), D-016 one full-length sting per ball, and advice on taps, drills, lighting and calibration masses. Backfills c768e2c."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 9 paths under "Changes to be committed". Nothing else should be left.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** `gh auth status` or `gh auth login`, or sign in through Git Credential Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- The last command should end with `STATE: UP_TO_DATE`.

**Follow-up after the wrap.** The owner committed and pushed the 9 files above as `f4fa904` (2026-11-10;
`sync_status.py --fetch`: `UP_TO_DATE`). Then, at the owner's request, the agent brought `README.md` up to date and
recorded it here and in PROJECT_STATUS, TODO and the session index. Commands for that follow-up:

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
git status
git diff
git add README.md PROJECT_STATUS.md TODO.md docs/sessions/SESSION_LOG.md docs/sessions/2026-11-10-parts-ordering.md
git diff --cached --stat
git commit -m "Update the README to the current project state" -m "The README still described the original plan (nothing ordered, C_D about 0.47). It now gives the current status, the hardware on hand and ordered, what changed from the original plan, the Re-matched reference C_D (D-009) and the tested Python version. Backfills f4fa904."
git push origin HEAD
python scripts/sync_status.py --fetch
```

`git status` should show 5 paths staged before the commit.
