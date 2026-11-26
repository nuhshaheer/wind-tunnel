# 2026-11-26: Shield order and load-cell bench test (EXP-002)

- **Session ID:** 26e4ecb4-355a-4670-bb0f-77007555aa40
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** `ac895a3`

Started on the evening of 2026-11-25 and ran past 02:00 on 2026-11-26. The owner did the bench work and KiCad edits; the
agent checked files, recorded the load-cell data straight from the Mega's USB port and analysed it.

## 1. Starting state and objective

- `/catchup` (2026-11-25): `UP_TO_DATE` at `397c671`. The owner had committed and pushed the 2026-11-24 continuation
  (TAL221 bench-scale design). No local changes; `check_docs.py` 0 failures, 0 warnings; 20 tests OK in 11.2 s; `origin`
  at the new URL.
- Catch-up discrepancies (fixed at this wrap): `397c671` not recorded (PROJECT_STATUS header, §4, §12 item 1, §13;
  SESSION_LOG; the 2026-11-23 shield log's header); PROJECT_STATUS §9's test-time range stopped at 2026-11-19; the
  "CAD / drawings" row in docs/experimental_setup.md still said "No CAD yet … revision D"; the bench-scale zero was a P0
  task in TODO but "TODO P2" in the setup doc and PROJECT_STATUS §12; three stale KiCad lock files (dated 2026-11-23,
  ignored by Git, KiCad not running).
- Owner's objective: "test the 0.1 micro F capacitor (100 nF) and then order the PCB. Then we can get started on working
  on the CAD". After the order: "lets first do the tal221 calibration".

## 2. Work completed

- **"What did I forget to push?"** Nothing: local `main` and `origin/main` were both `397c671`, which holds all 15 files
  of the last wrap's `git add` list. The "not committed yet" notes in the docs were only waiting for this backfill.
- **Capacitors for the shield's placeholder footprints** (owner, calipers and meter):
  - C2 (10 µF electrolytic): lead spacing matches the 2.0 mm footprint ("approximately"); diameter not reported.
  - C1 (the kit's 0.1 µF film): legs 6.5–6.7 mm apart unbent; the owner will bend them to the 5.0 mm holes. Measured
    **108.9 nF**.
  - The agent measured the room on the board (a copy of `arduino_shield.kicad_pcb`): the nearest other pad is 6.65 mm
    from C1's body centre (R1's, which stays empty) and the nearest edge 19.1 mm; for C2, 6.73 mm to the Mega header row
    and 9.3 mm to the bottom edge, so a can up to about 8 mm fits. **No footprint change needed.**
  - The JLCPCB zip (`arduino_shield-gerbers-2026-11-23.zip`, local only) holds the same 10 files, byte for byte, as
    the committed `gerbers/` folder, which is unchanged since `397c671`.
- **The 0.1 µF film tested as C1 on the breadboard** (owner at the bench, agent's steps). The old C1 was marked **1 µF**
  (owner), which settles the 2026-11-23 question. With the film capacitor, the scan, the SDP810's zero and its sign all
  passed (§6).
- **R1 and R2.** Explained: the red X in KiCad is "do not populate"; the I²C pull-ups are on the Waveshare BME280 board
  (the owner's 2026-11-18 reading of about 4.6 kΩ from its VCC to SDA and SCL); the empty pads are a backup (BME280
  unplugged or replaced, or long cables on the tunnel). The breadboard had them because sheet 12 drew them (marked not
  fitted) and they were built on 2026-11-18; removal was advised then but not confirmed. **The owner removed R1 and R2
  (2026-11-26)**, kept the two wires that carry SDA and SCL to the breadboard's other half (they are the bus), and was
  asked to pull the two +5 V wires that fed the resistors. The scan passed after each step, so the breadboard now matches
  the shield.
- **Title block** (owner, in KiCad, from the agent's suggestions): date 2026-11-25, revision 1, title "Wind Tunnel Sensor
  Shield (Arduino Mega)", company "Nuh Shaheer", comments 1–4 (connections, R1/R2 do not populate, C2 polarity, pointers
  to D-018, D-020 and sheet 12).
- **KiCad local-history restore found and checked.** At 2026-11-25 23:20:53 KiCad restored a version from its local
  history, leaving `_restore_backup_2026-11-25T23-20-53-818/`, and the design was saved at 00:44. The agent compared, on
  copies: the backup equals `397c671` (ignoring line endings); the board on disk has the same 72 tracks, 5 vias, 20
  footprints, net names and outline as the commit. Only the title block, the template's "* Indicates a PWM-capable pin"
  note (moved up), `sch_revision` and KiCad's plot settings changed. **The copper is what was ordered.** The backup
  folder was deleted at the owner's request ("you can delete the backup").
- **The shield PCB ordered from JLCPCB** (owner, 2026-11-26): order Y6-12005915A, 5 boards, as in §6.
- **TAL221 bench scale printed and assembled** (owner): PLA, 20 % infill; the soldered TAL221 screwed on, wire end on the
  base. Slicer estimates: pan 9.34 g (9.42 g with supports, removed), base 9.40 g (9.48 g). The owner pasted the
  designer's Thingiverse print settings: Anet A8, no raft, supports, 0.16 mm layers, 25 % infill, PLA ("Polymaker
  Polyflex" listed as the brand), and **2 × M3 × 10 screws at the base, 2 × M3 × 20 screws with nuts at the top**. The
  photo the owner sent is a crop of the designer's `images/Pic2.jpg`, not the owner's print.
- **EXP-002, the load cell on the bench scale** (owner placing masses, agent recording and checking each step live):
  - The Mega is on this PC (COM3, `Arduino Mega 2560 (COM3)`, USB serial `13448474939351C0E828`), so the agent wrote
    `scripts/serial_capture.ps1` and recorded the HX711 straight to `data/raw/`.
  - The owner set `AVERAGE_OVER = 1` in `hx711_raw_counts` (every raw reading) and uploaded it.
  - Sequence: 9 min empty pan; the low range (2, 2, 2 and 5 g up, then down); the full range (10, 10, 10, 20, 20, 10 g
    up to 79.440 g, then down); 50 g for about 6 min (creep); 4 min empty. Each step checked from the file before the
    next.
  - `analysis/exp002_bench_scale.py` finds the 23 load states, fits them and writes the plateau table and a summary.
    Results in §6; `metadata.md` written beside the raw files.
- **At this wrap:** D-021 (data capture), notes on D-018, D-019 and D-020; docs below; `.gitignore` gains KiCad's
  restore-backup folders.

## 3. Files and equipment affected

- New:
  - `scripts/serial_capture.ps1`
  - `analysis/exp002_bench_scale.py`
  - `data/raw/2026-11-26_EXP-002_tal221-bench-scale/run01.csv` (empty, failed start), `run02.csv`, `metadata.md`
  - `data/processed/2026-11-26_EXP-002_plateaus.csv`
  - `results/2026-11-26_EXP-002_bench-scale-summary.txt`
  - this log
- Changed by the owner: `PCB/arduino_shield/arduino_shield.kicad_sch` (title block; one note moved),
  `arduino_shield.kicad_pro` (`sch_revision` "1"), `arduino_shield.kicad_pcb` (plot settings and track order only;
  copper unchanged); `firmware/hx711_raw_counts/hx711_raw_counts.ino` (`AVERAGE_OVER` 10 → 1).
- Deleted (agent, at the owner's request): `PCB/arduino_shield/_restore_backup_2026-11-25T23-20-53-818/`, untracked,
  identical to `397c671`.
- Edited at the wrap: `.gitignore`, `CLAUDE.md`, `README.md`, `PROJECT_STATUS.md`, `TODO.md`, `DECISIONS.md`,
  `PROJECT_BACKGROUND.md`, `docs/experimental_setup.md`, `docs/data_catalog.md`, `docs/electronics_walkthrough.md`,
  `docs/shopping_list.md`, `firmware/README.md`, `docs/sessions/SESSION_LOG.md`,
  `docs/sessions/2026-11-23-sensor-shield-pcb.md` (commit backfill only), this log.
- Equipment (owner): on the breadboard, C1 changed from the 1 µF electrolytic to the kit's 0.1 µF film capacitor; R1,
  R2 and their two +5 V feed wires removed; the soldered TAL221 mounted on the printed bench scale.

## 4. Experimental procedures performed

All by the owner; the agent gave the steps and read the results.

1. Capacitors: calipers on C1's and C2's leads; C1 on the meter's capacitance range, out of circuit (meter model
   Unknown).
2. C1 swap: USB unplugged; old C1 out (marking read); 0.1 µF film in the same rows; `i2c_scan`; `sdp810_read` with the
   ports looped by a tube; then tube off, a gentle puff on each port.
3. R1/R2: USB unplugged; both resistors out; `i2c_scan` and `sdp810_read` (looped); then the +5 V feed wires; `i2c_scan`.
4. EXP-002: the procedure in `data/raw/2026-11-26_EXP-002_tal221-bench-scale/metadata.md` (tweezers, pieces near the
   pan's centre, 5 g stacked on the 2 g pieces, about 20–60 s per step).

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                       # catch-up and wrap: UP_TO_DATE at 397c671
python scripts/check_docs.py ; python -m unittest discover -s tests
# Capacitor room on the board (a copy in the scratchpad): footprint pads and Edge.Cuts read from the .kicad_pcb text
python -I <scratchpad>/pcbcheck/near.py <copy of arduino_shield.kicad_pcb>
# Zip against gerbers/: sha256 of every member against the file of the same name; zipfile.testzip()
# KiCad versions: git show HEAD:<file> vs the working file vs the restore backup; CR stripped; segments, vias,
# footprints (ref, position, rotation), net names and Edge.Cuts compared as sets (<scratchpad>/pcbcmp/cmp.py)
```

```powershell
[System.IO.Ports.SerialPort]::GetPortNames()               # COM3 (Arduino Mega 2560, serial 13448474939351C0E828)
# EXP-002 recording (background; stopped by creating the stop file):
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\serial_capture.ps1 -Port COM3 -OutFile "data\raw\2026-11-26_EXP-002_tal221-bench-scale\run02.csv" -StopFile "<scratchpad>\exp002_run02.stop"
```

```bash
python -I <scratchpad>/exp002_tail.py <run02.csv> 40        # live 5 s means after each step (not kept)
python analysis/exp002_bench_scale.py                        # writes data/processed/... and results/...
sha256sum data/raw/2026-11-26_EXP-002_tal221-bench-scale/run0*.csv
```

## 6. Measurements and results

**Shield and breadboard** (owner's instruments, models Unknown; uncertainty not quantified):

| Item | Value | Status |
|---|---|---|
| C1 film capacitor (marked 0.1 µF) | 108.9 nF; legs 6.5–6.7 mm apart unbent | Owner's meter and calipers |
| C2 (10 µF) lead spacing | about 2.0 mm, matching the footprint; diameter not reported | Owner |
| Old breadboard C1 | marked 1 µF | Owner |
| I²C scan, 0.1 µF in C1 | 0x25 SDP810; 0x77 BME280, chip ID 0x60 | Verified (function) |
| SDP810 zero, ports looped, 0.1 µF | −0.036 to −0.045 Pa, mean −0.042 Pa over 18 one-second lines; chip 24.4–24.9 °C; 0 bad reads | Verified (function) |
| SDP810 puff test | first set +17.5 to +46.6 Pa, second set −3.0 to −82.3 Pa; 0 bad reads. Taken as High then Low from the order asked; the owner did not say otherwise | Verified (sign), assuming that order |
| R1, R2 removed | scan 0x25 and 0x77 (ID 0x60); zero −0.071 to −0.079 Pa, mean about −0.075 Pa over 10 lines, chip 26.6–26.8 °C (after the puffs), 0 bad reads; scan again after the +5 V wires | Verified (function): the BME280 board's pull-ups alone are enough on the bench |

All three SDP810 zeros (−0.022 Pa on 2026-11-23 with 1 µF; −0.042 and −0.075 Pa tonight) are within the datasheet's
±0.08 Pa zero-point accuracy; their spread (0.053 Pa) is a little over the 0.04 Pa repeatability figure, but the chip
temperature differed. The capacitor does not set the zero.

**Shield order** (owner, 2026-11-26): JLCPCB order Y6-12005915A, file "arduino_shield-gerbers-2026-11-23_Y6"; 5 boards;
FR-4 TG135, 2 layers, 101.6 × 53.34 mm, 1.6 mm, green with white silkscreen (ink-jet), **OSP finish** (not the HASL
suggested), 1 oz outer copper, tented vias, flying-probe full electrical test, order mark removed, IPC Class 2, build
time 2 days, shipping 8–10 days (arrival about 6–8 December, the agent's estimate), weight 0.21 kg. Price not recorded.

**EXP-002** (`data/raw/2026-11-26_EXP-002_tal221-bench-scale/run02.csv`; `python analysis/exp002_bench_scale.py`;
outputs `data/processed/2026-11-26_EXP-002_plateaus.csv`, `results/2026-11-26_EXP-002_bench-scale-summary.txt`).
**Preliminary result:** one run, masses relative to an unchecked balance, room temperature not logged, printed bench
scale (not the tunnel's balance).

| Quantity | Value |
|---|---|
| Sensitivity, straight line through all 23 states (0–79.440 g, up and down) | **13,727.5 counts/g** (standard error 1.4, 0.010 %); 1.399 × 10⁶ counts/N with g = 9.81 m/s² (assumed) |
| Low range only (0–10.963 g) vs full range only (0–79.440 g) | 13,705.9 (se 14.3) vs 13,725.4 (se 1.0) counts/g: −0.14 % |
| Residuals of the all-states line | max 0.025 g, rms 0.012 g; up-going states read low, down-going high |
| Hysteresis, down minus up at the same load | +0.004 to +0.022 g (largest 0.022 g at 5.906 g, after 10.963 g) |
| Return to zero | +0.013 g after the low cycle; +0.011 g after the full cycle; +0.002 g after 50 g; +0.026 g over the whole 32 min |
| Creep, 50.097 g for about 6 min | +0.008 g (30 s means span 0.010 g) |
| Zero, first 9 min empty | 10 s means span 0.034 g (settling −0.014 g over the stretch); after 3 min, sd 0.0045 g, span 0.017 g |
| Noise | reading-to-reading sd 40 counts = 0.003 g (median over 1.4 s windows); about 5× the 2026-11-23 taped-cell scatter |
| Implied cell output | 0.639 mV/V at 100 g, assuming the excitation is the HX711's AVDD reference (datasheet 0.6 ± 0.15) |
| The 2026-11-23 penny (about 33,300 counts) | 2.43 g: a 2.5 g penny (1983 or later); not weighed |

Interpretation: sensitivity and straightness are not the limit (errors well under 0.1 %). The zero is: wander and lag of
about 0.005–0.025 g are 2–8 % of the smallest expected drag (0.3 g, the 3/4 in ball at 6.5 m/s), about 1–2 % at 13 m/s,
under 1 % for the 1 in ball at top speed. Hysteresis and drift cannot be separated in this run. Every value is within the
TAL221 datasheet's ±0.05 % FS (±0.05 g) error figures.

## 7. Tests, calibration checks and validation

- Capacitor fit: board clearances computed from the design file (above); not checked against a fabricated board.
- Zip vs `gerbers/`: 10 of 10 members identical (SHA-256); `testzip()` OK; `gerbers/` identical to `397c671`.
- KiCad versions compared as sets (above): copper, nets, footprints and outline identical to `397c671`.
- `serial_capture.ps1`: parsed by PowerShell's parser after each edit; used once for real (run02: 20,180 lines over
  32 min, 95 ms reading interval throughout, stopped cleanly). No automated test.
- `exp002_bench_scale.py`: found exactly the 23 states of the logged sequence; every state within 0.5 g of a rough
  line before fitting; levels agree with the live checks during the run.
- At the wrap: `python -m unittest discover -s tests -v` and `python scripts/check_docs.py`: results in §13.
- **Not performed:** JLCPCB's Gerber preview was not seen by the agent; the meter's and calipers' accuracy; the HX711's
  excitation voltage; room temperature during EXP-002; the pan's real mass; the screw lengths on the scale; whether the
  laptop was on its charger; any check of the school balance.

## 8. Errors, failed approaches and troubleshooting

- **run01.csv is an empty failed start.** The Arduino IDE still held COM3 ("Access to the port 'COM3' is denied"), and
  the first version of the capture script created the output file before opening the port. Raw files are never
  deleted, so it stays and is catalogued. The script now opens the port first. Closing the IDE completely freed the port.
- **The first 15 lines of run02.csv** are serial-buffer leftovers from before the Mega reset (some repeated); the
  analysis starts at the header.
- **"10 minutes passed"** was 7 minutes by the PC clock; the zero stretch is 9 min including the warm-up checks.
- **Tweezer bumps** at four steps (peaks up to about 77 g above the empty pan, under the cell's 100 g rating);
  excluded by the analysis.
- **The photo of the scale** was the designer's picture, not the owner's print.
- **Agent's statements corrected by the analysis:** during the run the agent said the 50 g creep showed "no steady
  trend"; the analysis gives +0.008 g (last minus first 30 s mean), small but upward. The agent's live remark that the
  SDP810 zero "seems to follow" the chip temperature rests on three points and is not established.
- **The +5 V feed wires:** the owner kept the SDA/SCL wires (correctly) and then ran the scan after being asked to pull
  the two +5 V wires; their removal is implied, not stated.

## 9. Decisions and reasoning

- [D-021](../../DECISIONS.md) (new, Tentative, agent's choice): serial data is captured with `scripts/serial_capture.ps1`
  (Windows PowerShell's built-in serial port; PC time stamp on every line; never overwrites), so no install and no lost
  lines. An exception to "helper scripts are Python standard library only", recorded in CLAUDE.md.
- [D-020](../../DECISIONS.md) note: both capacitors fit their footprints (C1's legs bent from about 6.6 to 5.0 mm), so
  the footprints are Accepted; the shield is ordered.
- [D-018](../../DECISIONS.md) note: the breadboard now matches the shield (0.1 µF film C1; no R1/R2) and passes.
- [D-019](../../DECISIONS.md) note: `hx711_raw_counts` set to `AVERAGE_OVER = 1` for EXP-002; the agent recommends
  keeping it now that lines are captured to a file (owner to confirm).
- Analysis choices (in the script): a state's level is the mean of its last 20 s; jumps over 1,500 counts between
  readings mark disturbances; g = 9.81 m/s² for counts per newton.

## 10. Open questions and blockers

- Confirm the two +5 V feed wires are out; C2's diameter (not needed for the fit); the price paid for the boards.
- Keep `AVERAGE_OVER = 1` as the committed default (agent: yes) or go back to 10.
- Why the HX711 noise is about 5× the 2026-11-23 figure on the scale (vibration or air on the 60 mm pan?): a box over the
  scale, and battery against charger, would tell.
- Hysteresis against drift: a repeat with zeros between loads, and the BME280 logged for temperature.
- Still open from before: the HX711's excitation voltage, the Adafruit library version, which wire moved when the
  BME280 reset, the SDP810's High barb marked, the BME280's connection firmed up, the Mega's own I²C pull-ups.

## 11. Remaining tasks

- **Owner:** commit and push (§13); measure the heat-set inserts (length, outside diameter) for the sizing; when the
  boards arrive (about 6–8 December), keep them sealed until soldering (OSP), then solder and test the shield.
- **Agent:** start the sizing (build step 1) with the contraction, the test section and the test coupons; the combined
  logging sketch, which can now log through `serial_capture.ps1`.

## 12. Recommended first task for the next agent

Ask the owner for the heat-set inserts' length and outside diameter, then start the sizing for the CAD (D-017): the
contraction (250 → 100 mm square, points file for Fusion 360), the test section and the test coupons, settling the
settling-chamber spacing with the owner (open questions 13 and 15). If the shield boards have arrived, help the owner
solder and test them first (TODO P2).

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `397c671`; nothing staged; 18 files modified and 8 new, all from this session. Checks
after editing: `python -m unittest discover -s tests -v` 20 tests OK in 9.2 s; `python scripts/check_docs.py` 0 failures,
0 warnings (22 session logs indexed once, 1,014 links and anchors resolve, 5 catalogued paths exist, 161 committable
files, none over 25 MiB, no secrets); `python analysis/exp002_bench_scale.py` rerun gives byte-identical outputs; the
raw file's SHA-256 is unchanged. Left out on purpose (ignored): KiCad's `.history/`, `.kicad_prl` and the Gerber zip.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add .gitignore CLAUDE.md README.md PROJECT_STATUS.md TODO.md DECISIONS.md PROJECT_BACKGROUND.md
git add docs/experimental_setup.md docs/data_catalog.md docs/electronics_walkthrough.md docs/shopping_list.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-23-sensor-shield-pcb.md docs/sessions/2026-11-26-shield-order-and-load-cell-bench-test.md
git add firmware/README.md firmware/hx711_raw_counts/hx711_raw_counts.ino
git add PCB/arduino_shield/arduino_shield.kicad_sch PCB/arduino_shield/arduino_shield.kicad_pro PCB/arduino_shield/arduino_shield.kicad_pcb
git add scripts/serial_capture.ps1 analysis/exp002_bench_scale.py
git add data/raw/2026-11-26_EXP-002_tal221-bench-scale data/processed/2026-11-26_EXP-002_plateaus.csv results/2026-11-26_EXP-002_bench-scale-summary.txt
git status
git diff --cached --stat
git commit -m "Record shield order and load-cell bench test (EXP-002)" -m "The owner confirmed both shield capacitors fit, brought the breadboard to the shield's configuration (0.1 uF film C1, no R1/R2) and ordered 5 boards from JLCPCB. EXP-002 records the TAL221 on the printed bench scale through the new scripts/serial_capture.ps1 (D-021): 13,727.5 counts/g, straight within 0.025 g to 79 g, with the zero (0.005-0.025 g) as the limit. Adds the first analysis script, the owner's KiCad title block, notes on D-018, D-019 and D-020, and backfills 397c671."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show all 26 paths under "Changes to be committed" and nothing left over.
  `run01.csv` is an empty file on purpose (the catalogued failed start); Git adds it like any other file.
- **Harmless warnings:** "LF will be replaced by CRLF" (or the reverse) can be ignored. `data/raw/` is stored byte for
  byte (`.gitattributes`).
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
