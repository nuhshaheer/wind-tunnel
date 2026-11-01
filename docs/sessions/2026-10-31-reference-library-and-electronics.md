# 2026-10-31: Reference library and electronics references

- **Session ID:** f4c24302-ea90-49a8-b0a9-e34f7341f0d9 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** `7db221f`

## 1. Starting state and objective

**Starting state** (from `/catchup`, 2026-10-31):

- Sync state `UP_TO_DATE` at `b710093`: the owner had pushed the second `/wrap`'s doc update. Clean working tree.
- `check_docs.py` reported 0 failures and 0 warnings; 20/20 tests passed.
- Discrepancies found (fixed at this wrap):
  - PROJECT_STATUS, TODO, SESSION_LOG and the 2026-10-31 log still said the follow-up commit was not made, although
    `b710093` was on GitHub.
  - docs/experimental_setup.md said "as of 2026-10-29" and had no change-history row for the D-005 construction row.
- Project: planning / pre-build, nothing built. Owner sizing inputs still missing.

**Objectives (owner requests, in order):**

1. "I uploaded a bunch of papers in the resources folder… let me know if we need more, especially for how we design
   the electronics."
2. "Check now": a further upload (the full AGARD-AG-336 volume, then the owner's own chapter 6 extract).
3. "How do you know what electronics we have on hand?"
4. Run `/wrap`.

## 2. Work completed

- **`/catchup`** run and handoff reported (no doc edits, as the skill requires).
- **Identified the 13 PDFs the owner added** by their title pages and text (and page images where there was no text):
  - Every document on the 2026-10-30 "Wanted" list arrived except AGARD-AG-336 chapter 6, which came later (below).
  - `mehta1979.pdf` was actually Mehta (1977), *Prog. Aerospace Sci.* 18, pp. 59–120, the long blower-tunnel paper
    (also on the Wanted list). The existing Mehta1979 PDF is a different file (different MD5).
  - `rp200424.pdf372046978rp200424.pdf` is a von Karman Institute paper on blockage for circular cylinders
    (Anthoine, Olivari, Portugaels 2004), not the AGARD chapter.
  - `DataCorrelationsforExaminations2013.pdf` and `…2013-2.pdf` were byte-identical (same MD5, and `cmp` found no
    difference).
  - `arc-rm-3400.pdf` (Maskell) is a 27-page scan with no text layer; page images show R&M 3400, dated November
    1963, printed by HMSO in 1965.
- **Filed them** under the `<Key>_<short-title>.pdf` rule (12 renames with `mv -n`), deleted the identical duplicate,
  and added a naming rule for datasheets (Key = part number).
- **Barlow1999** (59,952,818 bytes = 57.2 MiB, a commercial textbook) is over the 25 MB limit: added to `.gitignore`
  and listed as "local only" in the index.
- **Reviewed two documents in full and wrote notes:**
  - [HX711 datasheet rev. V2.0](../../resources/notes/HX711.md): gains, noise (50 nV rms at gain 128 and 10 SPS),
    data rates, settling times, serial timing (PD_SCK high 50 µs max; above 60 µs the chip powers down), power. Our
    arithmetic: noise floor in grams for example load cells.
  - [Weakly2024](../../resources/notes/Weakly2024.md) (ASEE 2024 balance): TAL220 10 kg cells + SparkFun HX711 +
    Arduino Uno, about $121; static MAPE 1.6–2.5 %; sphere C_D within ±6 % of 0.47. Caveats recorded: no mount-drag
    subtraction or blockage correction for the sphere (Maskell's formula gives about 4 % for their 3.4 % blockage;
    our arithmetic), manometer airspeed at assumed density.
- **Electronics gap analysis:** web searches checked candidate documents (sources linked in the new "Wanted" list).
  The new list, in priority order:
  - pressure-sensor candidates (Sensirion SDP31/SDP32, Honeywell TruStability HSC ±1 inH₂O);
  - load-cell candidates (TAL220, TAL221);
  - TI datasheets for the on-hand LM741, LM348 and LM317;
  - Bosch BME280 for ambient p and T;
  - background: Tomin 2020, Post & Morris 2010, HBM/Hoffmann, ADI MT-031, Dwyer H-11, NIST TN 1297.
- **AGARD-AG-336** (second upload):
  - The owner added `AGARD-AG-336-All.pdf`: the full 560-page volume, 27,419,864 bytes (26.1 MiB), over the limit.
    Its bookmarks put chapter 6 at PDF pages 332–364. Its distribution statement reads "There are no restrictions on
    the distribution of this document", but the PDF's permission flags forbid page extraction and copying, so the
    agent did not split it.
  - The agent tried to download NATO's separate chapter 6 PDF (failed, §8). The owner said they would extract it and
    asked for the pages (332–364), then printed them to PDF from Firefox.
  - The agent checked the extract: 33 pages, first page 6-1 (title, contents, author Kevin Cooper), last page 6-33
    (end of references). It has no text layer.
  - Filed as Cooper1998 (committable, 3.5 MB) and Ewald1998 (the full volume, local only and in `.gitignore`).
- **Documentation updated:** resources/README.md (index of 16 entries, rules, new "Wanted" list),
  docs/experimental_setup.md (HX711 specs confirmed, header date, change history), PROJECT_BACKGROUND.md (references),
  DECISIONS.md (D-006), PROJECT_STATUS.md, TODO.md, this log and the index, and the `b710093` backfill.
- **Owner's question on parts on hand:** answered from the docs. The only source is the original README's list
  (LM741/LM348 op-amps, LM317), copied into the other docs; nothing else in the ECE kit is recorded. Recorded as open
  question 9 and a P0 owner task.

## 3. Files and equipment affected

**Renamed** (owner downloads, all in `resources/`; original name → new name):

| Original | New |
|---|---|
| `ASEE_Wind_Tunnel_Paperfinal.pdf` | `Weakly2024_low-cost-lift-drag-balance-educational-tunnel.pdf` |
| `DataCorrelationForSphereDrag2013.pdf` | `Morrison2013_sphere-drag-correlation.pdf` |
| `DataCorrelationsforExaminations2013.pdf` | `Morrison2013_exam-data-correlations-sheet.pdf` |
| `HX711.pdf` | `HX711_avia-adc-datasheet-v2.pdf` |
| `arc-rm-3400.pdf` | `Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf` |
| `J._B._Barlow,_W._H._Rae,_Jr,_A._Pope_Low_Speed_Wind_Tunnel_Testing.pdf` | `Barlow1999_low-speed-wind-tunnel-testing-3rd-ed.pdf` (local only) |
| `mehta1979.pdf` | `Mehta1977_blower-tunnels-wide-angle-diffusers.pdf` |
| `bradshaw1964.pdf` | `Bradshaw1964_design-of-low-speed-wind-tunnels.pdf` |
| `morel1975.pdf` | `Morel1975_axisymmetric-contraction-design.pdf` |
| `roos1971.pdf` | `Roos1971_sphere-and-disk-drag.pdf` |
| `19820006182.pdf` | `Scheiman1981_screens-honeycomb-turbulence-reduction.pdf` |
| `rp200424.pdf372046978rp200424.pdf` | `Anthoine2004_bluff-body-drag-blockage-effect.pdf` |
| `AGARD-AG-336-All.pdf` | `Ewald1998_wind-tunnel-wall-correction-AGARD-AG-336.pdf` (local only) |
| `AGARD-AG-336-All chap 6.pdf` (owner's extract) | `Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf` |

**Deleted:** `resources/DataCorrelationsforExaminations2013-2.pdf` (byte-identical duplicate; never tracked).

**Created:** `resources/notes/HX711.md`, `resources/notes/Weakly2024.md`, this log.

**Modified:** `.gitignore` (two local-only PDFs), `DECISIONS.md` (D-006), `PROJECT_BACKGROUND.md`, `PROJECT_STATUS.md`,
`TODO.md`, `docs/experimental_setup.md`, `docs/sessions/SESSION_LOG.md`,
`docs/sessions/2026-10-31-literature-review-and-design-inputs.md` (commit-hash backfill only), `resources/README.md`.

**Equipment:** none.

**Scratch files** (outside the repo, in the session scratchpad): extracted text, page renders, and `render.py`
(PyMuPDF page renderer).

## 4. Experimental procedures performed

None. No physical work this session; no hardware exists yet.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                 # /catchup and /wrap: UP_TO_DATE at b710093
git status --short; git log --oneline -15; git show --stat b710093
python scripts/check_docs.py                          # after each batch of edits
python -m unittest discover -s tests [-v]
pdftotext -layout <pdf> <scratch>/txt/<name>.txt      # text of each new PDF
md5sum <pdf>...; cmp <a> <b>                          # duplicate checks (Morrison exam sheets; mehta1979 vs Mehta1979)
python -I <scratch>/scripts/render.py <pdf> <outdir> <zoom> <pages>   # PyMuPDF page renders (Maskell, HX711, chapter 6)
python -I -c "import pymupdf; ..."                    # PDF outlines, permissions, clipped renders (ASEE Table 1, Fig. 2)
mv -n <owner file> resources/<Key>_<title>.pdf        # 14 renames (§3)
rm -- resources/DataCorrelationsforExaminations2013-2.pdf
curl -sS -L --max-time 120 -o <scratch>/dl_agard_ch6/08chap06.pdf https://www.sto.nato.int/publications/AGARD/AGARD-AG-336/08chap06.pdf   # timed out (§8)
git check-ignore -v resources/Barlow1999_*.pdf resources/Ewald1998_*.pdf
```

Web searches (results are summaries of vendor and publisher pages; the URLs are in resources/README.md "Wanted"):
Sensirion SDP3x, Honeywell TruStability 1 inH₂O, HBM/Hoffmann strain-gauge book, Tomin 2020, Post & Morris 2010,
ADI MT-031, TAL221, BME280, TI LM348, NIST TN 1297, Dwyer 160 pitot tube, AGARD-AG-336 chapter 6.

The load-cell noise table in the HX711 notes came from a short inline Python calculation. Its formula and assumed
values (5 V excitation, rated outputs) are written next to the table.

## 6. Measurements and results

No measurements. Calculated estimates only (status: estimate, not a result):

- **HX711 noise floor** (our arithmetic; 50 nV rms at gain 128 and 10 SPS; 5 V excitation assumed): single-sample
  noise about 0.0017 g for a 100 g, 0.6 mV/V cell; 0.010 g for 1 kg, 1.0 mV/V; 0.10 g for 10 kg, 1.0 mV/V. The
  1.0 mV/V values are assumptions. Details: [HX711 notes](../../resources/notes/HX711.md).
- **Weakly2024 blockage** (our arithmetic): a 63.5 mm sphere in a 304.8 mm square section has S/C ≈ 3.4 %.
  Maskell's Δq/q = ε·C_D·S/C with ε ≈ 2.5 gives about 4 %.
- **Pressure-sensor ranges** (our arithmetic, ρ = 1.2 kg/m³): ±125 Pa reads up to about 14 m/s, ±249 Pa about
  20 m/s, ±500 Pa about 29 m/s.
- **Transcription checks:** Weakly2024 Table 1 rows sum to $121.47, not the printed $121.40 (a slip in the paper).
  Their forces are about 4–40 gf (from their Table 3, ρ = 1.225 kg/m³).

## 7. Tests, calibration checks and validation

| Check | Outcome |
|---|---|
| `python scripts/check_docs.py` (at `/catchup`) | 0 failures, 0 warnings |
| `python -m unittest discover -s tests` (at `/catchup`) | 20 tests, all passed |
| `python scripts/check_docs.py` (after filing, and after the AGARD files) | 0 failures, 0 warnings; 42 committable files, none over 25 MiB |
| `git check-ignore -v` on Barlow1999 and Ewald1998 | Both ignored by the new `.gitignore` lines |
| Chapter 6 extract | 33 pages; first and last page images match pp. 6-1 and 6-33 |
| Paper transcriptions | HX711 Table 2 and timing table, Weakly2024 Table 1 and Fig. 2 checked against page images. Other Weakly2024 figures read from captions and text only; the HX711 reference PCB pages were not examined |
| Web-sourced specs (sensor accuracies, TAL221 output) | Not checked against datasheets; marked as such in the "Wanted" list |
| `/wrap`: `python -m unittest discover -s tests -v` | 20 tests, all passed (no code changed) |
| `/wrap`: `python scripts/check_docs.py` (final, after this log) | 0 failures, 0 warnings: 3 session logs each indexed once, 143 links and anchors resolve, 43 committable files, none over 25 MiB, no secrets |
| `/wrap`: `git status --short` | 24 paths (9 modified, 15 new), matching the §13 `git add` list exactly |
| Calibration or equipment checks | **None performed.** No hardware exists |

## 8. Errors, failed approaches and troubleshooting

- **Text extraction scrambles tables.** `pdftotext` mixed up the HX711 electrical-characteristics and timing tables
  and the Weakly2024 cost table. They were read from PyMuPDF page renders instead.
- **Chapter 6 download failed:** the `curl` request to sto.nato.int timed out after 120 s with 0 bytes. The owner made
  the extract instead.
- **The owner's extract has no text layer** (Firefox print-to-PDF). Workarounds: read page images, or use the text
  of the full volume (Ewald1998, local only). NATO's separate `08chap06.pdf` might be searchable; not checked.
- **Not done:** the agent did not split the full AGARD volume itself, because the PDF's permission flags forbid page
  extraction (recorded in the index).
- **Agent slips, caught and fixed this session:**
  - New index rows were first inserted out of alphabetical order.
  - Renumbering the "Wanted" list first produced two items numbered 1.
  - In chat, the new committable PDFs (before the AGARD files) were described as "about 33 MB". They were about
    31 MB; with Cooper1998 the new committable files total 34.5 MB.

## 9. Decisions and reasoning

- **D-006** (Tentative): reference PDFs over 25 MB stay in `resources/`, each ignored by name in `.gitignore`, and
  are listed as "local only". Applied to Barlow1999 and Ewald1998.
- **Datasheet naming** (recorded in resources/README.md, no D-entry): Key = part number, e.g. `HX711`.
- **Proposed only, not decided:**
  - one HX711 per load cell, with raw counts logged;
  - a load cell smaller than 10 kg;
  - a digital pressure sensor (which would leave the op-amps without an obvious role);
  - BME280 for air density.

## 10. Open questions and blockers

- **Owner inputs needed for sizing:** bench length, target top speed, any fan in mind (unchanged).
- **What else is in the ECE kit?** Only the op-amps and the LM317 are recorded (new open question 9).
- D-003, D-004 and D-006 are Tentative.
- Microcontroller, pressure-sensor range, load-cell capacity, op-amp role, blockage method and C_D reference are
  still open. The papers for the last two are now on disk, not yet read.
- Copyright: several new PDFs are publisher-copyrighted. Fine while the repo is private.

## 11. Remaining tasks

See TODO.md:

- **P0 (owner):**
  - commit and push this session;
  - sizing inputs;
  - list the ECE kit contents;
  - confirm D-003, D-004 and D-006.
- **P1:**
  - review Maskell1963, Cooper1998, Morrison2013 and Roos1971 (an agent can start now);
  - size the contraction and test section;
  - owner downloads the electronics datasheets ("Wanted" items 1–4);
  - choose the fan, blockage method, sphere, microcontroller, pressure sensor, load cell, ambient sensor and op-amp
    role; buy hardware.

## 12. Recommended first task for the next agent

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed this session's commit; the next `/wrap` backfills its
hash into this log and the index.

- **If the owner has given the sizing inputs** (PROJECT_BACKGROUND "Requirements and constraints"), start build
  step 1.
- **If the owner has listed the kit,** record it in PROJECT_STATUS §3 and docs/experimental_setup.md.
- **Otherwise,** review **Maskell1963 and Cooper1998**, then **Morrison2013 and Roos1971**. They decide the blockage
  correction and the C_D reference, which constrain the sphere size and test section.
  - Both blockage scans have no text layer: read them as page images (PyMuPDF is installed). For Cooper1998 you can
    also use `pdftotext` on Ewald1998, PDF pages 332–364, if this machine has it.
  - Write a notes file for each paper and set its index row to "Reviewed".

## 13. Manual Git commands (as given to the owner)

State at this wrap: `UP_TO_DATE` at `b710093`. Nothing is staged or committed. The two local-only PDFs (Barlow1999,
Ewald1998) are ignored by Git and will not appear.

Run in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first. If FETCH_FAILED: fix the network first.
git status
git diff
git add .gitignore DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md TODO.md
git add docs/experimental_setup.md docs/sessions/SESSION_LOG.md docs/sessions/2026-10-31-literature-review-and-design-inputs.md docs/sessions/2026-10-31-reference-library-and-electronics.md
git add resources/README.md resources/notes/HX711.md resources/notes/Weakly2024.md
git add resources/Anthoine2004_bluff-body-drag-blockage-effect.pdf resources/Bradshaw1964_design-of-low-speed-wind-tunnels.pdf resources/Cooper1998_bluff-body-blockage-corrections-AGARD-AG-336-ch6.pdf resources/HX711_avia-adc-datasheet-v2.pdf
git add resources/Maskell1963_blockage-bluff-bodies-closed-tunnel.pdf resources/Mehta1977_blower-tunnels-wide-angle-diffusers.pdf resources/Morel1975_axisymmetric-contraction-design.pdf resources/Morrison2013_exam-data-correlations-sheet.pdf
git add resources/Morrison2013_sphere-drag-correlation.pdf resources/Roos1971_sphere-and-disk-drag.pdf resources/Scheiman1981_screens-honeycomb-turbulence-reduction.pdf resources/Weakly2024_low-cost-lift-drag-balance-educational-tunnel.pdf
git status
git diff --cached --stat
git diff --cached
git commit -m "Add reference library and electronics references" -m "Files the owner's downloads of every paper on the resources Wanted list (Maskell, AGARD-AG-336 chapter 6, Morrison, Roos, Mehta 1977 and others) under the naming rule, with Barlow and the full AGARD volume kept local only because they exceed 25 MB (D-006). Reviews the HX711 datasheet and the ASEE 2024 balance paper, adds a Wanted list for the electronics, records that the ECE kit inventory is incomplete, and backfills b710093."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** after the `git add` lines, `git status` should show 24 files staged: 9 modified and 15 new (this log,
  two notes files, 12 PDFs). Nothing should remain except the two ignored PDFs, which `git status` does not list.
- **The 12 PDFs** total about 34.5 MB; the largest is Weakly2024 at 15.5 MB. All are under the 25 MB limit and are
  stored as binary by `.gitattributes`.
- **After `git diff --cached`**, press `q` to leave the pager.
- **Pushing:** `git push origin HEAD`. The last command should end with `STATE: UP_TO_DATE`.
- **Harmless warnings:** "LF will be replaced by CRLF" can be ignored.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"), GitHub has commits you do not. Do not
  force-push. Run `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then
  `git push origin HEAD`.
