# 2026-11-23: Sensor bring-up on the breadboard

- **Session ID:** 550691f3-d7f2-473c-b161-23519e749225
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** not committed yet

The conversation started on 2026-11-22 (evening, `/catchup`) and the bench work ran into 2026-11-23. Everything here was
done by the owner at the bench, reported in the conversation, or written by the agent; the agent did no physical work.

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `604ee42` (the 2026-11-22 paper reviews, pushed by the owner); no local changes;
  `check_docs.py` 0 failures, 20 tests OK in 20.7 s.
- Starting state: breadboard power and signal rows wired (2026-11-18), no sensor connected; the SDP810 had a PH 2.0 cable
  pushed on but was never powered, with its colour-to-pin map unknown.
- Catch-up discrepancies found (fixed at this wrap): PROJECT_STATUS still said the paper reviews were uncommitted, its
  commit lists stopped at `fd20afe`, and it said "Seventeen references reviewed … Five more … not yet read" although
  only Ewald1998 is still unread.
- Objective (the owner's, set during the session): solder the HX711, wire every sensor on the breadboard as sheet 12 and
  test each one.

## 2. Work completed

- **Advice while the owner soldered** (all advice, recorded where it affects the build):
  - Header on the HX711's Arduino side: male pins or a female socket both work; the owner chose a **female socket**
    with male-to-male jumpers. The load cell's wires go straight onto the pads (no connector in the microvolt path:
    about 30 µV per gram, our arithmetic) and are not lengthened; the TUOFENG wire is for the HX711-to-Arduino run.
  - The HX711 is the load-cell amplifier (the board), and it is not on the I²C bus.
  - Tip tinner bubbling is normal (flux); the tip would not tin at the owner's usual 800 °F. Advised 625–660 °F for
    leaded and 660–715 °F for lead-free; the owner used 700 °F.
  - The TUOFENG 24 AWG wire's rating (owner, from its manual: 2.0 A continuous, 7 A instantaneous) is far above the
    circuit's about 0.1 A; recorded in the buy list.
  - Jumpers on hand: female-to-male, female-to-female and male-to-male (owner); recorded in the buy and shopping lists.
  - The SDP810 cable's far ends were spliced to jumper halves and wrapped in tape at staggered positions (the owner had
    only masking tape; electrical tape or the kit's heat-shrink advised for later).
  - Breadboard rows, the centre gap, jumpering a row to another row; R1 as a pull-up (harmless, about 2.4 kΩ with the
    BME280's 4.7 kΩ); connector pin numbers versus each part's own pin numbers on sheet 12; C1's polarity (a 0.1 µF
    film or ceramic part has none; the owner's has a long leg, which went to 5 V); VDD and VCC rows joined to 5 V.
  - Before power: the SDP810's VDD and GND must not be swapped. The owner wired it by pin number from the moulded "1"
    and confirmed the order on the part (1 SCL, 2 VDD, 3 GND, 4 SDA).
- **Agent wrote four bring-up sketches** in `firmware/` ([README](../../firmware/README.md); [D-019](../../DECISIONS.md),
  Tentative): `i2c_scan`, `hx711_raw_counts` (later given `AVERAGE_OVER = 10` so a whole test fits on screen),
  `sdp810_read` (commands and scale factors rechecked against the SDP8xx datasheet pages 7 and 10), `bme280_read`
  (Adafruit BME280 Library; later given a mode check that re-initializes a reset chip).
- **Owner's bench tests**, all passing (details in §6).
- **Photos:** the owner added four phone photos of the finished circuit; the agent made compressed copies without
  metadata (`docs/images/2026-11-23_breadboard-complete-*.jpg`), and the owner moved the originals, which carry a GPS
  block, out of the repo.
- **Documentation:** experimental_setup (current configuration, instrumentation, data acquisition, the breadboard
  section with every result, change history), walk-through (open items, steps 3 and 4), D-018 note and D-019,
  firmware README, buy list and shopping list (jumpers, wire rating), PROJECT_STATUS, TODO, PROJECT_BACKGROUND (lessons),
  README (status, `firmware/` in the layout), CLAUDE.md (where firmware goes).

## 3. Files and equipment affected

- New: `firmware/README.md`, `firmware/i2c_scan/i2c_scan.ino`, `firmware/hx711_raw_counts/hx711_raw_counts.ino`,
  `firmware/sdp810_read/sdp810_read.ino`, `firmware/bme280_read/bme280_read.ino`, four photos in `docs/images/`, this log.
- Edited: `PROJECT_STATUS.md`, `TODO.md`, `DECISIONS.md`, `PROJECT_BACKGROUND.md`, `README.md` (status, layout),
  `CLAUDE.md` (a firmware convention line), `docs/experimental_setup.md`,
  `docs/electronics_walkthrough.md`, `docs/buy_list.md`, `docs/shopping_list.md`, `docs/sessions/SESSION_LOG.md`, and
  the 2026-11-19 log (commit backfill only).
- Equipment (owner): a 5-way female header soldered to the HX711's VDD–GND side at about 700 °F; one TAL221 soldered to
  the HX711's RED, BLK, WHT and GRN pads (YLW empty); the SDP810's PH 2.0 cable spliced to jumper halves, joints in
  tape; the whole circuit wired on the breadboard as sheet 12; C1 (long leg to 5 V) at the breadboard end; the load
  cell taped at a desk edge; Adafruit BME280 Library installed in the Arduino IDE (version not recorded).

## 4. Experimental procedures performed

All by the owner; the agent only read the reported values and pasted output.

1. TAL221 resistance at the free wire ends before soldering: red–black and green–white "about" 1090 Ω and 1000 Ω
   (exact readings not given).
2. HX711 header continuity check after soldering (owner reported it checked; no numbers).
3. Power-up with every sensor connected, after confirming the SDP810's pin order; heat check; voltages.
4. `i2c_scan`; then `hx711_raw_counts` with a penny on the load cell's free end; then `sdp810_read` with the ports looped,
   then breath toward a tube on High and on Low; then `bme280_read` with breath and a fingertip, repeated after a reset.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                       # catch-up and wrap: UP_TO_DATE at 604ee42
python scripts/check_docs.py
python -m unittest discover -s tests [-v]
# Analysis of pasted output (agent, inline Python 3.11, results in section 6):
#   statistics.mean / stdev of the HX711 counts and time gaps; the penny step against the zero before and after;
#   counts per gram = step / penny mass; implied mV/V = counts per gram / (256 * 2**23 / 100 g)
#   CRC-8 check of the SDP810 algorithm: crc8([0xBE, 0xEF]) == 0x92
# SDP8xx datasheet pages 7 and 10 re-read with PyMuPDF (pymupdf.open(...)[6:10].get_text())
# Photos (scratchpad viewing copies, then the committed copies):
#   Pillow 12.1.1: EXIF read for GPS presence only (contents not read); ImageOps.exif_transpose;
#   thumbnail to 2000 px long edge; saved as new JPEG, quality 82, no EXIF/XMP/ICC
```

Arduino IDE 2.3.10 (owner): each sketch opened, uploaded to the Mega on COM3, Serial Monitor at 115200 baud.

## 6. Measurements and results

All bench values on the owner's meter (model and accuracy Unknown) or from the sketches' output; full pasted outputs in
[experimental_setup.md](../experimental_setup.md#breadboard-as-built). No dataset in `data/` (bench checks, per the
data catalog's rule).

| Quantity | Value | Status |
|---|---|---|
| + rail, all sensors on | 4.947 V | Verified (meter) |
| SDA, SCL to GND, idle | 4.814 V, 4.815 V | Verified (meter): BME280 pull-ups work |
| I²C scan | 0x25 (SDP810), 0x77 (BME280), chip ID 0x60 | Verified |
| HX711 reading interval | 95–97 ms (mean 95.5 ms): RATE at 10 SPS | Verified |
| HX711 zero, 14 single readings over 1.4 s | mean −14,818 counts, standard deviation 26 counts | Preliminary (1.4 s only) |
| HX711 penny step (10-reading means) | about 33,300 counts (33,259 / 33,301 against the zero before / after); back to zero within 42 counts | Verified response; size Preliminary |
| Counts per gram | about 13,300 (2.5 g penny) or 10,700 (3.11 g); implied 0.62 or 0.50 mV/V against the datasheet's 0.6 ± 0.15 | Preliminary: penny not weighed, year unknown |
| SDP810 scale factor (reported by the sensor) | 240 per Pa: the ±125 Pa part | Verified |
| SDP810 zero, ports looped | −0.018 to −0.027 Pa (mean −0.022 Pa), 8 s | Verified (inside the 0.08 Pa zero accuracy); not corrected for ambient pressure |
| SDP810 sign | breath at High up to +30.5 Pa; at Low down to −31.6 Pa | Verified |
| BME280, untouched | 99,606.8–99,613.8 Pa; 23.23–23.31 °C; 44.4–44.6 %; 96600 / p = 0.9698 | Verified that it reads; accuracy not checked against a reference |
| BME280 response | humidity to 78–85 % with breath; temperature to 26.3–31.4 °C with a fingertip | Verified |

Interpretation, not measured: the HX711's scatter (26 counts) is near the datasheet floor (about 21 counts at 10 SPS,
our arithmetic), about 0.002 g by the rated output.

## 7. Tests, calibration checks and validation

- `/catchup`: `python scripts/check_docs.py` 0 failures, 0 warnings; `python -m unittest discover -s tests` 20 tests OK
  in 20.7 s.
- At the wrap: `python -m unittest discover -s tests -v`: 20 tests OK in 16.6 s (Python 3.11.0).
  `python scripts/check_docs.py`: 0 failures, 0 warnings (907 links; 20 session logs, each indexed once; 128
  committable files, none over 25 MiB).
- The sketches were not compiled by the agent (`arduino-cli` is not installed). Each compiled and ran in the owner's
  Arduino IDE in its final form; `hx711_raw_counts` and `bme280_read` also ran in their first forms. The last edit to
  `hx711_raw_counts` (a comment) came after its penny run.
- The SDP810 CRC routine reproduces the datasheet example (0xBEEF → 0x92, Python check of the same algorithm).
- Photos: each new copy is 0.47–0.57 MB, 2000 × 1500 px, with no EXIF, XMP or ICC block.
- **Not performed:** the HX711 excitation voltage (RED to BLK); weighing the penny; any calibration (load cell, SDP810
  span, BME280 against a reference); a long zero-drift run; the 10-minute combined logging test (step 4); a check that
  R1 and R2 are still fitted (seen only in photos).

## 8. Errors, failed approaches and troubleshooting

- **The first HX711 copy held no penny step:** the Serial Monitor copied only the visible 14 lines (1.4 s). Fixed by
  averaging 10 readings per line. A second try was spoiled at the bench (owner: "i messed it up"; at most 252 counts of
  movement); the third worked after the agent advised laying the cell flat on its 12 mm face, taped only at its wire
  end.
- **BME280 froze at its reset values** (71,853.4 Pa, 23.90 °C, 80.2 %) from about 30 s into the first run, after one line
  of nonsense (−12,878.8 Pa, 181.94 °C), while the owner breathed on, blew on and touched the board. The library kept
  reading a chip that had reset to sleep mode. The owner's breath test then showed nothing because the old sketch was
  still running (its time column had reached 250 s). After unplugging, reseating and uploading the version with a mode
  check, the chip reset once more at about 63 s during wiggling and was re-initialized, with normal readings after.
  Cause not pinned down: a momentary VCC or GND contact loss on the Dupont connections, or a static discharge; the
  owner did not say which wire was moving.
- **Agent's early hedges corrected by the owner's answers:** the owner had already soldered and checked when the agent
  asked for the resistance numbers (exact values not given); the owner had wired the SDP810 by pin number before the
  agent asked for a photo, so the mapping was confirmed by the owner's description of the moulded "1" instead.
- The Arduino IDE may keep an open sketch's old copy after the file changes on disk; the owner was told to close and
  reopen it (recorded in the firmware README).
- Name clash avoided in `sdp810_read`: a loop variable first named `word` (an Arduino type name) was renamed before
  upload.

## 9. Decisions and reasoning

- [D-019](../../DECISIONS.md) (Tentative, agent's choice): one plain sketch per sensor in `firmware/`, CSV with units,
  raw values; HX711 and SDP810 from their datasheets, BME280 through the Adafruit library; each sketch checks for the
  failures seen.
- [D-018](../../DECISIONS.md) note: the breadboard test passed for every sensor; status unchanged (Tentative) until the
  owner confirms.
- Owner's choices: a female header on the HX711; the SDP810 by its PH 2.0 cable spliced to jumpers; 700 °F for the board.
- Agent's choices: do not lengthen the load cell's wires; keep the long cable on the digital side; mark the photos'
  observations as "look like" where the bands or rows cannot be read.

## 10. Open questions and blockers

- The penny's year (2.5 g or 3.11 g), to settle the counts-per-gram estimate. Better: weigh it on the school balance.
- The HX711's excitation voltage (RED to BLK), walk-through step 3 item 5.
- The Adafruit BME280 Library version installed.
- Which wire was being wiggled when the BME280 reset at about 63 s.
- Whether R1 and R2 are still fitted (photos suggest yes); remove to match sheet 12, or keep.
- Whether the Mega has its own I²C pull-ups (open question 17, still open).

## 11. Remaining tasks

- **Owner:** commit and push (§13); the four answers above; firm up the BME280's connection (a male header strip in the
  breadboard, and tape the hanging bundle down); mark the SDP810's High barb.
- **Agent:** the combined logging sketch (walk-through step 4) when wanted; then the 10-minute steady-rate test with the
  owner; the sizing (TODO P1) and the ten reading proposals still wait.

## 12. Recommended first task for the next agent

Ask whether the owner is at the bench. If so, write the combined logging sketch (walk-through step 4,
`firmware/logger/`): one CSV line per sample with time, HX711 counts, SDP810 dp (Pa, raw and corrected by
96600 / p_amb), BME280 p, T and RH, and a flag column for BME280 resets and failed reads, following D-019. Run it for 10
minutes and check the sample rate stays steady. Also collect the four open answers (§10). If the owner is away from the
bench, go through the ten reading proposals in TODO P1 first, then start the sizing.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `604ee42`; nothing staged. 12 files modified and 10 new to commit.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add PROJECT_STATUS.md TODO.md DECISIONS.md PROJECT_BACKGROUND.md README.md CLAUDE.md
git add docs/experimental_setup.md docs/electronics_walkthrough.md docs/buy_list.md docs/shopping_list.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-19-bme280-advice-and-mass-weighing.md docs/sessions/2026-11-23-sensor-bring-up.md
git add firmware/README.md firmware/i2c_scan/i2c_scan.ino firmware/hx711_raw_counts/hx711_raw_counts.ino firmware/sdp810_read/sdp810_read.ino firmware/bme280_read/bme280_read.ino
git add docs/images/2026-11-23_breadboard-complete-closeup.jpg docs/images/2026-11-23_breadboard-complete-1.jpg docs/images/2026-11-23_breadboard-complete-2.jpg docs/images/2026-11-23_breadboard-complete-top.jpg
git status
git diff --cached --stat
git commit -m "Bring up all three sensors on the breadboard" -m "The owner wired the SDP810, BME280 and HX711 with a TAL221 as sheet 12 and tested each with new bring-up sketches in firmware/ (D-019): the I2C scan finds 0x25 and 0x77, the HX711 runs at 10 SPS and a penny moves it about 33,300 counts, the SDP810 zeroes at -0.022 Pa with the right sign, and the BME280 reads 99.6 kPa and responds. Records a BME280 reset under handling and the recovery check. Adds compressed photos without metadata. Backfills 604ee42."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should show 22 paths under "Changes to be committed" and nothing left over.
- **Harmless warnings:** "LF will be replaced by CRLF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
