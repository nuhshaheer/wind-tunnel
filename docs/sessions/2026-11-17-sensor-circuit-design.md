# 2026-11-17: Sensor circuit design

- **Session ID:** bbb9a7ba-f2c8-44a9-b847-71355055abea
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** `8904785`

## 1. Starting state and objective

- `/catchup`: `UP_TO_DATE` at `ce69a57` (the owner had committed and pushed the 2026-11-15/17 time-estimates session).
  Clean working tree. `check_docs.py` 0 failures, 0 warnings (654 links); 20 tests OK in 18.7 s.
- The owner reported that **every package they bought has arrived** (that is, everything ordered on 2026-11-09/10; the
  fan was never bought) and asked to start the circuit: what it looks like, what connects to the Arduino and which
  parts are needed. The owner was away from home for the whole session, so no physical check was possible.
- During the session the owner added: they use **Fusion 360** for CAD; they are **a beginner in electronics with no
  background** and want to understand the theory; they asked for a "professional" schematic and block diagram, and about
  EasyEDA vs KiCad, power, and how the circuit becomes a PCB.

## 2. Work completed

- **Circuit walk-through in chat:** the circuit has no analog design. Three digital sensors, two small capacitors,
  optional pull-ups, all on the laptop's USB power. Nothing new to buy. Wiring table and bring-up order given.
- **Board details looked up:**
  - Waveshare's wiki page and schematic for the BME280 board were read: header order, 4.7 kΩ pull-ups to VCC on SDA, SCL,
    ADDR and CS, address 0x77 with ADDR open, RT9193-33 regulator, NDC7002N translator. The schematic is filed in
    `resources/` with [notes](../../resources/notes/WaveshareBME280.md).
  - SparkFun's HX711 hookup guide could not be read (HTTP 403), so the HX711 board's pad labels and RATE jumper stay
    unchecked.
- **Drawing package revision D:**
  - Sheet 11, **system block diagram** (WT-E01). Lanes run what is measured → sensor → conditioning and ADC → Arduino →
    laptop, with a power row and a line-style legend. The HX711 is drawn as an amplifier and an ADC, in the style of the
    owner's example.
  - Sheet 12, **interface schematic** (WT-E02):
    - reference designators A1–A3, U1, LC1, C1–C2, R1–R2, J1–J3, W1–W4, with real pin numbers, net labels, and +5V and
      ground symbols;
    - regions for each physical location;
    - an electrical parts list and a net list.
  - `wtlib.py` refactored so a sheet can carry its own date, status, units and an electrical key. The rebuilt page was
    byte-identical to the committed one before the new sheets were added.
  - Sheet 9's wiring note and "digital pins TBD" now point to sheet 12, and its date is 2026-11-17.
  - The drawings' parts list statuses changed from Ordered to On hand.
  - Page text, three new TBD rows and the README updated.
- **[D-018](../../DECISIONS.md)** (Tentative): the sensor interface circuit. **D-017** got a dated note: Fusion 360.
- **Owner's questions answered** (advice, recorded here):
  - A block diagram and a schematic are the standard pair. A flow chart is for the firmware's steps.
  - EasyEDA vs KiCad: the agent recommends KiCad (free and open; text files in the repo; used at work; STEP export to
    Fusion 360). EasyEDA is easier, with one-click JLCPCB ordering. Fusion's electronics workspace is a third option.
    The owner has not chosen.
  - The laptop is the power supply: about 100 mA against 500 mA (estimate). Check the load-cell noise on battery
    against on the charger, and keep the laptop from sleeping.
  - The PCB is a **shield** on top of the Mega, carrying only J1–J3, C2 and the R1/R2 pads; the sensors stay on cables.
    On an R3 board it can be Uno-sized. Locking Grove/JST-style plugs are likely for J1–J3; the owner will use female
    jumpers on the bench and order connectors when needed.
- **[docs/electronics_walkthrough.md](../electronics_walkthrough.md)**, for a beginner and future builders:
  - the ideas needed;
  - the six-step recipe for how the wiring and pins were decided;
  - reading the schematic, and power;
  - breadboard bring-up steps 0–4 with pass criteria (Planned);
  - breadboard to PCB;
  - six self-check questions with hidden answers, learning resources, open items and photo rules.

  Snapshots of sheets 11 and 12 are in `docs/images/`. Format: Markdown with images, not PDF (the agent's
  recommendation when the owner asked; a PDF can be exported from it).
- **Parts marked as arrived:** shopping list rows "Got it" (32), a dated note at the top of the buy list,
  PROJECT_STATUS §3, docs/experimental_setup.md (configuration, instruments, parts on hand, change history), README.
- Memory (outside the repo): the owner uses Fusion 360; the owner is an electronics beginner.

## 3. Files and equipment affected

- New:
  - `docs/drawings/s_e.py`
  - `docs/electronics_walkthrough.md`
  - `docs/images/2026-11-17_sheet11-block-diagram-revD.png`
  - `docs/images/2026-11-17_sheet12-schematic-revD.png`
  - `resources/WaveshareBME280_environmental-sensor-schematic.pdf` (129 KB)
  - `resources/notes/WaveshareBME280.md`
  - this log
- Modified, drawings: `docs/drawings/wtlib.py`, `build.py`, `page.py`, `s_d3b.py`, `wtdata.py`, `README.md`,
  `wind-tunnel-drawings.html` (rebuilt).
- Modified, docs:
  - `PROJECT_STATUS.md`, `TODO.md`, `DECISIONS.md`, `PROJECT_BACKGROUND.md`, `README.md`, `data/README.md`
  - `docs/experimental_setup.md`, `docs/buy_list.md`, `docs/shopping_list.md`, `docs/data_catalog.md` ("as of"
    date), `resources/README.md`
  - `docs/sessions/SESSION_LOG.md`, and `docs/sessions/2026-11-17-time-estimates-and-cad.md` (commit backfill only)
- Equipment: none touched. The parts are reported arrived but unchecked.

## 4. Experimental procedures performed

None. No physical work this session (the owner was away from home).

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                 # UP_TO_DATE at ce69a57 (catch-up and wrap)
python scripts/check_docs.py; python -m unittest discover -s tests
# SDP8xx datasheet text search for pull-up / decoupling advice (none found in the text layer):
python -I -c "import fitz ..." resources/SDP8xx_sensirion-digital-dp-sensor-datasheet-v1.1.pdf
# Waveshare schematic, saved by the web-fetch agent; text extracted and the page rendered at 200 dpi (scratchpad):
python -I -c "import sys, pymupdf ..." <tool-results>/webfetch-1794934890368-rutvvx.pdf <scratchpad>/ws
cp <tool-results>/webfetch-1794934890368-rutvvx.pdf resources/WaveshareBME280_environmental-sensor-schematic.pdf
python docs/drawings/page.py          # before the refactor: no diff; after it: still no diff; then with sheets 11-12
python docs/drawings/preview.py 9 11 12   # PNG checks (docs/drawings/png/, ignored by Git)
cp docs/drawings/png/sheet11.png docs/images/2026-11-17_sheet11-block-diagram-revD.png
cp docs/drawings/png/sheet12.png docs/images/2026-11-17_sheet12-schematic-revD.png
```

Web fetches (through the web-fetch agent):

- https://www.waveshare.com/wiki/BME280_Environmental_Sensor (read);
- the schematic PDF linked there (saved and filed);
- https://www.waveshare.com/bme280-environmental-sensor.htm (HTTP 503);
- https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide (HTTP 403);
- https://www.sparkfun.com/products/13879 (navigation only; its summary was not used).

Doc edits were made with Edit and with small Python replacement scripts in the scratchpad. Each replacement asserted a
unique match and kept the file's line endings.

## 6. Measurements and results

No measurements. **Estimates and design values (agent's arithmetic, not results):**

- **Power from USB:** about 100 mA in all.
  - Mega about 50–80 mA (typical, general knowledge).
  - SDP810 ≤ 5.5 mA (datasheet).
  - HX711 1.5 mA (datasheet), plus about 4.6 mA through the load cell (5 V / about 1,090 Ω).
  - BME280 board under 1 mA.

  USB 2.0 supplies 500 mA.
- **I²C bus:** the BME280 board's 4.7 kΩ, in parallel with the Mega's (about 10 kΩ on official boards, unchecked here),
  gives about 3.2 kΩ. With about 1.5 m of wire, estimated at ≤ 200 pF, the rise time is about 0.5–0.8 µs against the
  1 µs allowed at 100 kHz. Adding R1/R2 too would give about 1.9 kΩ, still within limits. So R1 and R2 are not fitted.
- **Load-cell signal:** 0.6 mV/V × 5 V ≈ 30 µV per gram, so about 9–70 µV for the expected 0.3–2.3 gf of drag.
- **q range** 25–101 Pa at 6.5–13 m/s; **drag** about 3–23 mN. Both repeat earlier estimates.

## 7. Tests, calibration checks and validation

- **Drawing refactor:** `python docs/drawings/page.py` reproduced the committed HTML byte for byte before and after the
  `wtlib.py` refactor (`git status` clean for the HTML). After revision D, the HTML diff for sheets 1–8 and 10 is only
  "SHEET n OF 10" → "OF 12" (checked with `git diff | grep`).
- **New sheets:** text-fit check built into `s_e.py` (0 warnings after one fix); previews of sheets 9, 11 and 12
  inspected and their label overlaps fixed.
- **At the wrap:**
  - `python -m unittest discover -s tests -v`: 20 tests OK in 21.2 s (Python 3.11.0);
  - `python scripts/check_docs.py`: 0 failures, 0 warnings (744 links; 17 session logs, each indexed once; 101
    committable files, none over 25 MiB).
- **Not performed:** any physical check. The arrival checks, the BME280 5 V check, I²C scans, and the HX711 labels and
  excitation all wait for the owner. The schematic is a design on paper, not verified against hardware.

## 8. Errors, failed approaches and troubleshooting

- SparkFun's HX711 hookup guide returned **HTTP 403** to the web-fetch agent, and the product page gave only navigation.
  So the board's pad labels, RATE default and excitation are marked TBD, for the owner to read off the board. Waveshare's
  product page returned **HTTP 503**; the wiki and the schematic PDF worked. Recorded as a lesson in PROJECT_BACKGROUND.
- Reading PROJECT_STATUS and TODO in one `cat` exceeded the output limit (117 KB); they were read in parts. This is the
  same as in the last session.
- `check_fit()` printed "≈" to a cp1252 console and raised UnicodeEncodeError; rerun with `PYTHONIOENCODING=utf-8`.
- A replacement in `docs/drawings/README.md` failed its assertion because that file uses CRLF line endings; it was
  redone with Edit. `docs/experimental_setup.md` is also CRLF; its script converted and restored the endings.
- One Bash heredoc with many quotes failed to parse ("unexpected EOF"). The edit script was moved to a scratchpad file.
- First renders of the new sheets:
  - "J1" crowded the interface region label (label moved to the bottom);
  - the "soldered direct" note ran into the wire-colour label (moved below);
  - one net-list cell was 5 px too wide (shortened);
  - "LAPTOP" appeared twice on sheet 11 (renamed SOFTWARE).

## 9. Decisions and reasoning

- [D-018](../../DECISIONS.md) (**Tentative**, the agent's design):
  - laptop USB as the only supply;
  - the SDP810 (0x25) and BME280 (0x77) on one I²C bus, pins 20/21;
  - the HX711 on pins 2/3 (no special job, and they exist on an Uno too);
  - C1 at the SDP810, C2 at the 5 V entry, R1/R2 not fitted;
  - J1–J3 with pin 1 = +5V, 2 = GND;
  - breadboard first, then a shield PCB.

  Reasoning is in the entry. The owner has not confirmed it.
- D-017 note: Fusion 360 (owner).
- Agent's choices:
  - the walk-through as Markdown with images in `docs/images/` (the folder `check_docs.py` already listed as a layout
    root), not a PDF;
  - parts statuses changed on the owner's verbal report, with "arrival checks pending" kept everywhere;
  - the published claude.ai copy of the drawings **not** republished (needs the owner's go-ahead; TODO P0).

## 10. Open questions and blockers

- **Asked this session, not answered:**
  - which PCB program, KiCad (recommended) or EasyEDA;
  - whether to republish the private drawings copy (now revision D);
  - whether the agent should write the commented test sketches.
- **To read off the delivered boards** (PROJECT_STATUS open question 17):
  - HX711 pad labels and RATE jumper;
  - the BME280 cable;
  - whether the Mega is an R3;
  - whether the Mega has its own I²C pull-ups.
- **From before:**
  - whether to start the sizing now;
  - hours a week and any deadline;
  - the heat-set insert dimensions;
  - the fan (D-011);
  - filament amounts and "check house" items;
  - the school balance's readability;
  - the datasheet checklists (now four, with WaveshareBME280);
  - shortening PROJECT_STATUS;
  - room for a cylinder test;
  - the tentative decisions (now including D-018).

## 11. Remaining tasks

- **Owner:**
  - commit and push (§13);
  - the arrival checks;
  - read the walk-through (§2–5) and its first tutorials;
  - breadboard steps 0–4, one sensor at a time;
  - choose the PCB program;
  - answer the questions in §10.
- **Agent:**
  - the commented bring-up sketches in `firmware/` when wanted;
  - build step 1 (sizing), delivering dimension sheets and the contraction points file for Fusion 360 (D-017);
  - check the owner's EasyEDA/KiCad net list against sheet 12 when it exists;
  - record each bench result in docs/experimental_setup.md.

## 12. Recommended first task for the next agent

Ask the owner whether they are at the bench.

- **If they are:** write the commented bring-up sketches (I²C scanner, BME280 chip ID and readings, SDP810, HX711 raw
  counts) in `firmware/`. Then guide walk-through §6 steps 0–1: the arrival checks, then the BME280 power-only 5 V check
  before SDA and SCL touch the Mega. Record every result with its date in docs/experimental_setup.md.
- **If not:** start the sizing with the settling-chamber spacing (Mehta1979's 0.2 D against full-decay spacing; open
  questions 13 and 15), delivered as dimension sheets for Fusion 360.

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `ce69a57`; nothing staged. 20 files modified and 7 new.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md README.md TODO.md data/README.md
git add docs/buy_list.md docs/shopping_list.md docs/experimental_setup.md docs/data_catalog.md docs/electronics_walkthrough.md
git add docs/images/2026-11-17_sheet11-block-diagram-revD.png docs/images/2026-11-17_sheet12-schematic-revD.png
git add docs/drawings/README.md docs/drawings/build.py docs/drawings/page.py docs/drawings/s_d3b.py docs/drawings/s_e.py docs/drawings/wtdata.py docs/drawings/wtlib.py docs/drawings/wind-tunnel-drawings.html
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-17-time-estimates-and-cad.md docs/sessions/2026-11-17-sensor-circuit-design.md
git add resources/README.md resources/WaveshareBME280_environmental-sensor-schematic.pdf resources/notes/WaveshareBME280.md
git status
git diff --cached --stat
git commit -m "Add sensor circuit drawings, walk-through and D-018" -m "Every ordered part has arrived, and the owner, new to electronics, asked how the circuit works. Drawing package revision D adds a block diagram and an interface schematic (sheets 11-12); D-018 records the circuit as tentative; docs/electronics_walkthrough.md explains it step by step. Files the Waveshare BME280 schematic, marks the parts on hand and notes Fusion 360 on D-017. Backfills ce69a57."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should then show 27 paths under "Changes to be committed", with nothing left over.
- **Harmless warnings:** "CRLF will be replaced by LF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`.
