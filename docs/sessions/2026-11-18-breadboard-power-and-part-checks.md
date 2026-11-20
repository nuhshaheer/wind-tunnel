# 2026-11-18: Breadboard power and part checks

- **Session ID:** 3b39cb24-828c-4e6d-8e8a-b0addaef61cc
- **Agent:** Claude Opus 5.5 (Claude Code, VS Code extension)
- **Commit:** `ff2ac6e`

## 1. Starting state and objective

- Started 2026-11-17 with `/catchup`: `UP_TO_DATE` at `8904785`, clean working tree, `check_docs.py` 0 failures and
  0 warnings (744 links), 20 tests OK in 14.4 s.
- The owner had the delivered electronics at the bench. They added photos of the parts, asked circuit questions as
  they went, and wired the breadboard up to, but not including, the sensors. Work ran past midnight, so the breadboard
  photos and every meter reading are dated 2026-11-18.

## 2. Work completed

- **Delivered parts read from the owner's photos** (labels and appearance only; nothing electrical can be judged from a
  photo):
  - SparkFun HX711 board: pads are labelled **RED, BLK, WHT, GRN, YLW** and **VDD, VCC, DAT, CLK, GND**, not E+, E−, A−,
    A+ as sheet 12 and the walk-through said. Two more unlabelled pads sit near CLK and GND. The RATE jumper is not on
    the photographed side.
  - SDP810: marked `SDP810 - 125Pa`, `PN:1-101597-01` (the datasheet's order number for this part),
    `SN:2301553748` (last digits slightly blurred).
  - Waveshare BME280: regulator, two 6-pin translator chips and eight resistors marked 472 (4.7 kΩ), as on the schematic.
    No pin labels on the photographed side. The cable is a white 6-pin plug to six **female** Dupont sockets.
  - TAL221: red, black, white and green wires. No capacity marking on the photographed side. The holes at the wire-exit
    end look smaller and chamfered, probably the M3 tapped end (not confirmed).
  - The owner's elechawk kit: 24 AWG 20-wire ribbon cable, PH2.0 "male" connectors 2P–8P, PH2.0 male crimp pins and
    heat-shrink.
- **Errors found in the walk-through and corrected:** the HX711 pad names; "find pin 1 on p. 12" (p. 12 is the top view,
  so it reads the opposite way from the pin side and could swap VDD and GND).
- **Questions answered:**
  - The sensors are in parallel on power, not in series. C2, R1 and R2 each sit in their own branch between two nets.
  - The breadboard's − rail is GND once jumpered to a Mega GND pin; there is no separate analog ground here.
  - D2 and D3 are digital pins 2 and 3, in the header section marked PWM; PWM itself is not used.
  - How to use continuity, resistance and DC-volts modes, and why a capacitor across the rails stays silent.
- **SDP810 connector advice (not decided):** the kit's parts look male, like the sensor's pins, so they will not mate.
  A pre-crimped female 4-pin JST PH 2.0 cable is the agent's suggestion; its contact is rated for a 0.5 mm post at 2.0 mm
  pitch, matching the pin width and spacing on paper. The fit is unproven. Soldering wires directly remains the fallback.
- **Breadboard built by the owner and traced from photos** (table in
  [docs/experimental_setup.md](../experimental_setup.md#breadboard-as-built)).
- **Eight photos compressed into `docs/images/`** under the naming rule. The owner's originals were left in place.
- **Stale docs fixed:** drawing revision and part statuses in `docs/experimental_setup.md`, the PLA line in `TODO.md`,
  WaveshareBME280 added to the reviewed list in `PROJECT_BACKGROUND.md`, the revision D session link in the drawings
  README, and the README status.

## 3. Files and equipment affected

- New:
  - this log
  - `docs/images/2026-11-17_bme280-board-and-cable.jpg`, `2026-11-17_hx711-board-and-tal221.jpg`,
    `2026-11-17_sdp810-125pa.jpg`, `2026-11-17_ph2-ribbon-connector-kit.jpg`
  - `docs/images/2026-11-18_breadboard-overview-1.jpg`, `2026-11-18_breadboard-overview-2.jpg`,
    `2026-11-18_breadboard-c2-and-r1.jpg`, `2026-11-18_breadboard-signal-rows.jpg`
- Modified: `PROJECT_STATUS.md`, `TODO.md`, `DECISIONS.md` (dated note on D-018), `PROJECT_BACKGROUND.md`, `README.md`,
  `docs/experimental_setup.md`, `docs/electronics_walkthrough.md`, `docs/data_catalog.md`, `docs/drawings/README.md`,
  `docs/sessions/SESSION_LOG.md`, `docs/sessions/2026-11-17-sensor-circuit-design.md` (commit backfill only),
  `resources/notes/SDP8xx.md`, `resources/notes/WaveshareBME280.md`.
- Left out of Git on purpose: the owner's ten original photos in `docs/images/` (§8).
- Equipment: the Mega, breadboard and C2 were wired by the owner. Sheet 12 and `docs/drawings/wtdata.py` were not changed.

## 4. Experimental procedures performed

Bench checks by the owner, with the owner's multimeter (model Unknown). The agent performed none of them.

1. USB unplugged, continuity mode: probes on C2 / across + and −; then left + to right + and left − to right −.
2. USB plugged into the laptop, DC volts: left + to left −, right + to right −, and C2 row 1 to row 6.
3. USB unplugged, resistance mode, cable plugged into the BME280 board and not connected to the breadboard: red to blue,
   yellow, orange and green; black to blue.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                 # UP_TO_DATE at 8904785 (catch-up and wrap)
python scripts/check_docs.py; python -m unittest discover -s tests
# Scratchpad scripts, run with python -I, paths passed as arguments (none kept in the repo):
#   crop.py, kit.py, bb.py, bb2.py   zoomed PyMuPDF crops of the owner's photos and the SDP8xx datasheet pages
#   jst.py                           text and page images of the JST PH datasheet
#   photos.py                        checks photo metadata; writes each copy at 2000 px long edge, JPEG quality 82
```

Web: https://www.jst-mfg.com/product/pdf/eng/ePH.pdf, fetched through the web-fetch agent and read locally with PyMuPDF.
It is not filed in `resources/`, because no connector has been chosen.

## 6. Measurements and results

Raw observations, owner's meter readings, 2026-11-18. Meter model and accuracy Unknown; uncertainty not quantified.
Status: **Verified** for the breadboard's power wiring only. These are equipment checks, not experimental results.

| Check | Condition | Reading |
|---|---|---|
| + to − through C2's legs | USB unplugged, continuity | No beep (expected) |
| Left + to right + | USB unplugged, continuity | Beep (owner: "this works") |
| Left − to right − | USB unplugged, continuity | Beep |
| Left + to left − | USB from laptop, DC volts | 4.962 V |
| Right + to right − | USB from laptop, DC volts | 4.962 V |
| C2 row 1 to row 6 | USB from laptop, DC volts | 4.962 V |
| BME280 red to blue | Unpowered, resistance | 4.605 kΩ |
| BME280 red to yellow | Unpowered, resistance | 4.617 kΩ |
| BME280 red to orange | Unpowered, resistance | 4.597 kΩ |
| BME280 red to green | Unpowered, resistance | 4.617 kΩ |
| BME280 black to blue | Unpowered, resistance | 145.3 kΩ |

The owner gave the first four resistances without a unit. They are taken as kΩ, the unit asked for and the unit given
for the fifth.

Interpretation: the rails and C2 are connected with the right polarity. The red wire is common to four pull-up resistors,
as the schematic predicts for VCC. Blue, yellow, orange and green cannot be told apart by this test, so their assignment
(SDA, SCL, ADDR, CS) is still inferred from the wire order at the plug.

## 7. Tests, calibration checks and validation

- `python -m unittest discover -s tests -v`: 20 tests OK in 15.4 s (Python 3.11.0).
- `python scripts/check_docs.py`: 0 failures, 0 warnings (777 links; 18 session logs, each indexed once; 120 committable
  files, counting the ten untracked originals, none over 25 MiB).
- Photos: each new copy is under 0.6 MB and has no EXIF block (checked by `photos.py`).
- **Not performed:** the BME280 power-only 5 V check, I²C scan or chip ID; any SDP810, HX711 or load-cell test; the Mega's
  pin-20 pull-up measurement. No firmware was written. No sensor has been powered.

## 8. Errors, failed approaches and troubleshooting

- The owner's first attached images did not reach the agent. They were found in `docs/images/` by checking for new files.
- The web-fetch agent could not parse the JST PDF (compressed streams); it was read from the saved file with PyMuPDF.
- `python -I` ignores `PYTHONIOENCODING`, so printing the datasheet text failed on the cp1252 console. The text was
  written to a UTF-8 file instead.
- In angled photos the Mega's silkscreen seems to line up with the wrong header holes: the power wires looked as if they
  were on 3.3 V and 5V. Counting holes from the gap before A0 showed they are on **5V and the first GND**. The 4.962 V
  reading confirms the polarity.
- The red SDA wire's end at the Mega is hidden behind the blue wire, so pin 20 is inferred. The I²C scan will test it.
- **Three of the owner's original photos contain an EXIF GPS block** (the two parts photos and the SDP810 photo). The block's
  contents were not read. They must not be committed; the compressed copies carry no metadata.
- The owner was unsure what the continuity test showed; it was re-explained step by step, and the walk-through now
  says which meter mode goes with power on or off.

## 9. Decisions and reasoning

- No new decision. A dated note was added to [D-018](../../DECISIONS.md), which stays Tentative.
- Agent's choices: correct the walk-through now, because its errors could mislead wiring; leave sheet 12 for the owner's
  go-ahead (it still shows valid chip names and flags the pad names as to be checked); keep originals out of Git.

## 10. Open questions and blockers

- How the SDP810 connects: a pre-crimped female PH 2.0 cable (agent's suggestion) or soldered wires. Owner to choose.
- Whether the owner removed R1, R2 and their feed jumpers, and the loose clipped wire: advised, not confirmed.
- Whether to write the I²C scanner now and update sheet 12 (both offered, not answered).
- To read: HX711 RATE jumper and the back of the board; BME280 back labels; SDP810 pin side.
- **Owner check of values read from PDFs** (printed page = PDF page in both):
  - **Most important:** SDP8xx p. 4, Table 1 drawing: read the pin names left to right, and which pin has the "1".
  - SDP8xx p. 12, Fig. 3: read the pin names left to right. The caption says which side it is viewed from.
  - SDP8xx p. 11, Fig. 2: the pin width and how far the pins project from the body.
  - JST PH p. 1: pitch. p. 2: wire range of SPH-002T-P0.5S. p. 3: PHR-4 dimensions A and B. p. 5: what "P0.5" means.

## 11. Remaining tasks

- **Owner:** commit and push (§13); move the original photos out of the repo; finish walk-through §6 step 1; choose the
  SDP810 connection; send the items in §10.
- **Agent:** the I²C scanner and the other bring-up sketches when wanted; sheet 12 pad names when approved; record each
  bench result in `docs/experimental_setup.md`; sizing (build step 1) when the owner is away from the bench.

## 12. Recommended first task for the next agent

Ask whether the owner is at the bench. If so, confirm R1, R2, their two feed jumpers and the clipped wire are gone, and
continue BME280 step 1:

1. USB unplugged: 4-pin male header in column g, rows 44–47; red 44, black 45, blue 46, yellow 47; orange and green loose.
2. Jumper j44 to the right + rail (inner column) and j45 to the right − rail (outer column).
3. Continuity: row 44 to + beeps, row 45 to − beeps, row 44 to row 45 does not stay beeping.
4. USB in, DC volts: rows 46 and 47 against − should read about 5 V. About 3.3 V or 0 V means stop.
5. USB out, then jumper row 46 to the SDA row (23) and row 47 to the SCL row (39). Write `firmware/` I²C scanner, expect
   0x77, then read chip ID 0x60.

If the owner is away from the bench, start the sizing with the settling-chamber spacing (open questions 13 and 15).

## 13. Manual Git commands (as given to the owner)

State at the wrap: `UP_TO_DATE` at `8904785`; nothing staged. 13 files modified and 9 new to commit. Ten original photos
stay untracked and must not be added.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff --stat
git add DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md README.md TODO.md
git add docs/data_catalog.md docs/drawings/README.md docs/electronics_walkthrough.md docs/experimental_setup.md
git add docs/sessions/SESSION_LOG.md docs/sessions/2026-11-17-sensor-circuit-design.md docs/sessions/2026-11-18-breadboard-power-and-part-checks.md
git add resources/notes/SDP8xx.md resources/notes/WaveshareBME280.md
git add docs/images/2026-11-17_bme280-board-and-cable.jpg docs/images/2026-11-17_hx711-board-and-tal221.jpg docs/images/2026-11-17_sdp810-125pa.jpg docs/images/2026-11-17_ph2-ribbon-connector-kit.jpg
git add docs/images/2026-11-18_breadboard-overview-1.jpg docs/images/2026-11-18_breadboard-overview-2.jpg docs/images/2026-11-18_breadboard-c2-and-r1.jpg docs/images/2026-11-18_breadboard-signal-rows.jpg
git status
git diff --cached --stat
git commit -m "Record breadboard power checks and delivered part details" -m "The owner wired the breadboard and measured 4.962 V at the rails and C2, and checked the BME280 cable by resistance. Photos of the delivered parts corrected the walk-through: the HX711 pads are named by wire colour, and the SDP810 pin order must be read from the bottom view. Adds compressed photos without metadata. Backfills 8904785."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** `git status` should show 22 paths under "Changes to be committed". The ten original photos stay under
  "Untracked files". **Do not add them:** three contain a GPS block.
- **Harmless warnings:** "CRLF will be replaced by LF" (or the reverse) can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"): do not force-push. Run
  `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`.
- **Check:** the last command should end with `STATE: UP_TO_DATE`, apart from the untracked originals if still present.
