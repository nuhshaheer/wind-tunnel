# 2026-10-31: Literature review and design inputs

- **Session ID:** 0bc1e3bc-a0e1-477c-8a4e-e0e842f9c3f9 (Claude Code, from the scratchpad path)
- **Agent:** Claude Code (Opus 5.5), VS Code extension, Windows 11
- **Commit:** `5bc60f0` (the main work, pushed 2026-10-31). The second `/wrap`'s updates: not committed yet.
- **Dates:** the session ran 2026-10-30 to 2026-10-31. Docs written during it are dated 2026-10-30; the first `/wrap`
  and the second `/wrap` (after the owner's push) are dated 2026-10-31.

## 1. Starting state and objective

**Starting state** (from `/catchup`, 2026-10-30):

- Sync state `UP_TO_DATE`: the owner had pushed the initial commit `cc51fff`, and local `main` equalled `origin/main`.
- Clean working tree. `check_docs.py` reported 0 failures and 0 warnings; 20/20 tests passed.
- Docs were out of date only because of the push: PROJECT_STATUS still said "Last commit: none yet", the TODO P0 push
  task was still open, and the session-index commit was "not committed yet".
- Project: planning / pre-build, nothing built.

**Objectives (owner requests, in order):**

1. Read a contraction-design paper and create a `resources/` folder for papers.
2. Choose the better of two copies of Bell & Mehta (1988) and delete the other.
3. Read Mehta & Bradshaw (1979).
4. Recommend further documents.
5. Assess a water-mist flow-visualization idea from two YouTube videos.
6. Run `/wrap`.
7. Find out why the owner's push failed ("Could not resolve host: github.com").
8. Run `/wrap` again after the push succeeded, to record it.

## 2. Work completed

- **`/catchup`** run and handoff reported (no doc edits, as the skill requires).
- **`resources/` created:** [README.md](../../resources/README.md) holds the index, naming rule
  (`<Key>_<short-title>.pdf`, Key = first-author surname + year), notes template, rules, a "Videos and web pages"
  section and a "Wanted" list. Notes live in `resources/notes/`. CLAUDE.md and README.md now describe the folder.
- **Abdelhamed2014** ([notes](../../resources/notes/Abdelhamed2014.md)): renamed from
  `Design_optimization_of_three_dimensional_geometry_-1.pdf`. Read the full text and checked the key figures against
  extracted images.
  - Contents: CFD optimization of a square contraction (CR 6.25, L / inlet D = 1, three-parameter wall,
    inflection at about 0.41 L).
  - Its Table 1 and Table 2 came out scrambled in text extraction. The columns were reconstructed and cross-checked
    against the reductions the paper states (38.68 % and 28.43 %).
- **Bell1988** ([notes](../../resources/notes/Bell1988.md)): the owner added `19880012661.pdf` (Stanford JIAA TR-84,
  April 1988) and `19890004382.pdf` (NASA CR-177488, August 1988).
  - Same report, with identical text, tables and figures.
  - Kept the NASA CR copy: cleaner scan and OCR (5.2 % vs 6.6 % garbled words), and it is the cited edition. Renamed
    to `Bell1988_contraction-design-small-low-speed-tunnels.pdf`.
  - **Deleted `19880012661.pdf` at the owner's request.** It was untracked, so Git cannot restore it; the same text is
    in the kept copy.
  - Key content: 5th-order-polynomial wall shape, length limits (separation at L/H_i = 0.667 and 1.79), Batchelor
    turbulence factors. The notes also record internal typos in the report.
- **Mehta1979** ([notes](../../resources/notes/Mehta1979.md)): renamed from `10.1017S0001924000031985.pdf`.
  - Rules for every component of a small blower tunnel, plus the power-factor method for fan sizing.
  - PDF pages 8–11 are an unrelated note that came with the scan (recorded, file left as downloaded).
  - Every page carries a Cambridge Core terms-of-use stamp.
- **Owner facts and decisions recorded:**
  - The owner has a Bambu Lab P1S (PROJECT_BACKGROUND constraints; build volume 256 mm, manufacturer spec).
  - The tunnel will be "decently big" and printed in segments with alignment holes, probably glued:
    [D-005](../../DECISIONS.md), Accepted (glue Tentative). docs/experimental_setup.md construction row updated.
- **Design estimates** (assumption-labelled) added to PROJECT_BACKGROUND.md: printable contraction sizes vs sphere
  drag, and fan requirements (open exit vs exit diffuser).
- **References:** the three papers moved to "Reviewed" in PROJECT_BACKGROUND.md. The Achenbach (1972) entry now notes
  that it covers only Re ≥ 5×10⁴.
- **Further-reading list:** citations and availability checked by web search and recorded under "Wanted" in
  resources/README.md: ASEE 2024 low-cost balance paper, Morrison 2013 correlation, AGARD-AG-336 chapter 6, Maskell
  R&M 3400, HX711 datasheet, Roos & Willmarth 1971, Barlow et al. 1999, Mehta 1977, plus lower-priority items. None
  of these have been read.
- **Mist flow visualization** (owner's idea from Aki's YouTube videos): assessed, recorded as an optional P2 task in
  TODO.md with design points, and the videos listed in resources/README.md. Main point: a blower tunnel will not
  draw the mist in the way Aki's suction tunnel does, so the mist must be pushed in and released downstream of the
  screens.
- **First `/wrap`:**
  - PROJECT_STATUS.md rewritten.
  - TODO.md re-prioritized: push task moved to Done, and new P0, P1 and Done items added.
  - `cc51fff` backfilled into the 2026-10-29 log and the index.
  - PROJECT_BACKGROUND Re range corrected (§8).
- **Commit and push** (owner, with the §13 commands):
  - The commit worked first time: `5bc60f0`, 17 files.
  - The push failed with "Could not resolve host: github.com". The agent's read-only checks (§8) found that the PC's
    Wi-Fi had no IPv4 address, only a self-assigned `169.254.41.184`, so only sites with IPv6 addresses loaded.
  - The owner restored the network (the exact fix is not recorded; `ipconfig /renew` alone had not helped when the
    agent rechecked), then pushed: `cc51fff..5bc60f0`, and `sync_status.py --fetch` reported `UP_TO_DATE`.
- **Second `/wrap`:**
  - Backfilled `5bc60f0` and marked `/wrap` Verified.
  - Moved the push task to Done.
  - Corrected the first wrap's wrong explanations of the fetch and Amazon-link failures (§8).
  - Added the network lesson to PROJECT_BACKGROUND.md.

## 3. Files and equipment affected

**Created:**
- `resources/README.md`
- `resources/notes/Abdelhamed2014.md`, `resources/notes/Bell1988.md`, `resources/notes/Mehta1979.md`
- this log

**Added by the owner, then renamed by the agent:**
- `resources/Abdelhamed2014_wind-tunnel-contraction-optimization.pdf` (2.1 MB)
- `resources/Bell1988_contraction-design-small-low-speed-tunnels.pdf` (1.7 MB)
- `resources/Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf` (1.5 MB)

**Deleted:** `resources/19880012661.pdf` (duplicate, owner-requested, never tracked).

**Modified:**
- `CLAUDE.md`, `README.md`: resources convention and layout line.
- `DECISIONS.md`: D-005.
- `PROJECT_BACKGROUND.md`: P1S constraint, two estimate tables, references.
- `PROJECT_STATUS.md`, `TODO.md`
- `docs/experimental_setup.md`: construction row.
- `docs/sessions/SESSION_LOG.md`: new row and backfill.
- `docs/sessions/2026-10-29-github-setup-and-agent-handoff.md`: commit backfill only.

**Modified by the second `/wrap`:** this log, `docs/sessions/SESSION_LOG.md`, `PROJECT_STATUS.md`, `TODO.md`,
`PROJECT_BACKGROUND.md` (Lessons learned).

**Equipment:** none.

**Scratch files** (outside the repo, in the session scratchpad): extracted text, page renders, and the image-extraction
scripts `extract_imgs.py` and `ccitt_pages.py`.

## 4. Experimental procedures performed

None. No physical work this session; no hardware exists yet.

## 5. Commands and scripts executed

```bash
python scripts/sync_status.py --fetch                 # /catchup: UP_TO_DATE; 1st /wrap: FETCH_FAILED (§8); 2nd /wrap: UP_TO_DATE
git status --short; git log --oneline -15
python scripts/check_docs.py                          # run after each batch of edits
python -m unittest discover -s tests [-v]
pdftotext -layout <pdf> <scratch>/<name>.txt          # text extraction (pdftotext from Git for Windows)
python -I <scratch>/extract_imgs.py <pdf> <outdir>    # pull embedded JPEG/Flate images (Abdelhamed2014 figures)
python -I <scratch>/ccitt_pages.py <pdf> <outdir> 1400   # render CCITT-fax page scans to PNG via Pillow (Bell1988, Mehta1979)
mkdir -p resources/notes; mv -n <owner file> resources/<Key>_<title>.pdf   # three renames
rm -- resources/19880012661.pdf                       # owner-requested duplicate removal
nslookup amzn.to; curl -sS -o /dev/null -w "%{http_code} -> %{redirect_url}" https://amzn.to/<id>   # see §8
```

After the first `/wrap`. The owner ran the §13 commands in PowerShell, then `ipconfig /renew`. After fixing the
network, they ran `git fetch origin`, `sync_status.py --fetch` (`AHEAD`), `git push origin HEAD` and
`sync_status.py --fetch` (`UP_TO_DATE`). The agent's network checks (PowerShell, read-only):

```powershell
Resolve-DnsName github.com; Test-NetConnection github.com -Port 443
where.exe git; Select-String C:\Windows\System32\drivers\etc\hosts -Pattern github,amzn; Get-DnsClientServerAddress
nslookup github.com; nslookup github.com 1.1.1.1; nslookup google.com
[System.Net.Dns]::GetHostAddresses('<host>')   # google.com, github.com, amzn.to, microsoft.com, stackoverflow.com
Resolve-DnsName github.com -Type AAAA -DnsOnly
Get-NetIPAddress -AddressFamily IPv4; Get-NetRoute -AddressFamily IPv4 -DestinationPrefix 0.0.0.0/0
Test-Connection 192.168.86.1; Test-Connection 1.1.1.1; Test-Connection 2606:4700:4700::1111
Get-NetAdapter | Where-Object Status -eq 'Up'
```

Design estimates were computed with short inline Python calculations; the formulas and assumed values are written
next to each table in PROJECT_BACKGROUND.md. Web searches were used to check citations and availability; the URLs are
in resources/README.md.

## 6. Measurements and results

No measurements. Calculated estimates only (status: estimate, not a result). Details are in PROJECT_BACKGROUND.md.

- **Printable sizes** (CR 6.25, L = inlet width, 3 % blockage, C_D = 0.47):
  - 100 mm test section: 250 mm contraction inlet, 19.5 mm sphere, 0.86 gf at 10 m/s.
  - 150 mm test section: 375 mm inlet, 29.3 mm sphere, 1.94 gf at 10 m/s, 7.76 gf at 20 m/s.
- **Fan duty** (Mehta1979 typical losses, blower efficiency 0.8), 150 mm section at 20 m/s: 1620 m³/h, fan static
  pressure about 300 Pa and about 169 W shaft power with an open exit; 158 Pa and 89 W with a 2.5:1 exit diffuser.
- **Cross-checks of paper transcriptions** (our arithmetic), all consistent:
  - Abdelhamed2014: 38.68 % and 28.43 % reductions; Re = 4.8×10⁵; porous-jump thickness 10 mm.
  - Bell1988: exp(−2π·0.37) = 0.098; corrected matched-cubic branch.
  - Mehta1979: power-factor terms sum to 0.825.

## 7. Tests, calibration checks and validation

| Check | Outcome |
|---|---|
| `python scripts/check_docs.py` (at `/catchup`, and after each documentation batch) | 0 failures, 0 warnings every time |
| `python -m unittest discover -s tests -v` (this wrap) | 20 tests, all passed (no code changed this session) |
| `python scripts/check_docs.py` (final, after this log) | 0 failures, 0 warnings: 12 required files, 2 session logs each indexed once, all relative links and anchors resolve |
| Paper transcriptions | Equations and tables checked against page images (§6 cross-checks). Figures 2, 7, 8, 9 of Abdelhamed2014, Figs. 1–12 and Table 3 of Bell1988, and Figs. 1(a) and 2 of Mehta1979 were not examined in detail |
| Further-reading citations | Existence and bibliographic details checked by web search; contents not read |
| Owner's commit and push with the §13 commands (2026-10-31) | Commit `5bc60f0` (17 files) worked first time. The push failed because of the PC network fault (§8). After the fix: `git push origin HEAD` gave `cc51fff..5bc60f0`, and `sync_status.py --fetch` gave `UP_TO_DATE`. This completes the independent `/wrap` verification |
| `sync_status.py` states seen live in the owner's terminal | `FETCH_FAILED` (network down), `AHEAD` (1 commit, before the push), `UP_TO_DATE` (after the push), each correct for the situation |
| Second wrap: `python scripts/sync_status.py --fetch` (agent) | `UP_TO_DATE` at `5bc60f0`, clean tree |
| Second wrap: `python -m unittest discover -s tests` | 20 tests, all passed (no code changed) |
| Second wrap: `python scripts/check_docs.py` | 0 failures, 0 warnings: 2 session logs each indexed once, 101 links and anchors resolve, 28 committable files, no secrets |
| Calibration or equipment checks | **None performed.** No hardware exists |

## 8. Errors, failed approaches and troubleshooting

- **PDF page rendering:** the Read tool could not render PDF pages (`pdftoppm` is not installed). Workaround:
  `pdftotext` for text, plus scratch scripts that pull the embedded images.
- **Scratch renderer bugs, both fixed:**
  - The first renders came out colour-inverted (TIFF photometric flag wrong).
  - On Mehta1979, two small JPEG images (author photos) were decoded as fax data and saved over pages 1 and 8.
- **OCR quality:** the text layers garble formulas in Bell1988 and Mehta1979. Every formula in the notes was read
  from page images instead.
- **Agent errors caught and corrected:**
  - Bell1988 notes: a Morel reference was first written from memory with the wrong initial ("J.") and a wrong 1976
    title. Corrected from the report's own reference list (T. Morel, ASME J. Fluids Eng. 1975; ASME Paper
    76-WA/FE-4, 1976).
  - Abdelhamed2014 notes: a guess that the L/D ≈ 1 rule came from that paper's ref 13 was wrong. The paper attributes
    it to ref 14 (Mehta & Bradshaw), which does not contain it. Corrected.
  - PROJECT_BACKGROUND (Achenbach entry): the planned Re range was first written as "about 2–5×10⁴". Corrected at
    this wrap to "roughly 10⁴–10⁵", which matches the estimate tables (about 1.3×10⁴ at 10 m/s up to about 10⁵).
    The same wrong figure was given to the owner in chat.
- **Amazon links not resolved:** the owner could not open two `amzn.to` links in Firefox. WebFetch failed with DNS
  ENOTFOUND, and sandboxed `curl` could not resolve the host, while Windows `nslookup` did resolve it. The products
  remain unidentified. The first wrap guessed Firefox tracking protection or an ad blocker. **Corrected at the second
  wrap: that guess was probably wrong.** amzn.to failed the same Windows lookup as github.com during the IPv4 fault
  below. IPv4 was not checked on 2026-10-30, when the owner first hit the problem, so this is likely but not proven.
- **First `/wrap` sync check returned `FETCH_FAILED`** ("Could not resolve host: github.com"), although the same
  fetch worked at `/catchup`. The first wrap blamed the agent sandbox. **Corrected at the second wrap: that was
  wrong.** The owner's own terminal gave the same error, for the reason below. The remote state at that wrap was
  unknown, so the Git commands started with a fetch.
- **Owner's push failed: the PC had no IPv4 address.** Evidence from the agent's read-only checks (§5):
  - The only connected adapter was Wi-Fi (MediaTek Wi-Fi 7 MT7925). Its IPv4 address was `169.254.41.184`, which
    Windows assigns itself when DHCP gives it none. There was no IPv4 default route, and IPv4 pings to 192.168.86.1
    and 1.1.1.1 failed.
  - IPv6 worked: a ping to 2606:4700:4700::1111 succeeded, and the router's IPv6 DNS server answered.
  - Windows lookups returned IPv6 addresses only. google.com and microsoft.com resolved. github.com, amzn.to and
    stackoverflow.com failed with "No such host is known" (an AAAA query for github.com returned nothing).
  - `nslookup github.com` still printed the IPv4 address 140.82.114.4, which made it look as if DNS was working.
  - Ruled out: the Git in use was Git for Windows (`C:\Program Files\Git`), and the hosts file had no GitHub or
    Amazon entries.
  - `ipconfig /renew` did not restore IPv4 by the time the agent rechecked (its output also said Ethernet, Wi-Fi 3
    and Wi-Fi 5 were disconnected; harmless). The owner then fixed the network, exact step not recorded, and the
    push succeeded.
  - Once the network was fixed, the agent's own `sync_status.py --fetch` worked too, so a fetch failure seen by the
    agent was a real network fault.
  - Lesson recorded in PROJECT_BACKGROUND.md (Lessons learned).

## 9. Decisions and reasoning

- **D-005** (Accepted; glue Tentative): print the tunnel in segments on the P1S with alignment holes. Reason: a
  one-piece print caps the test section at about 100 mm and the sphere drag at about 1 gf at 10 m/s.
- **Resources convention** (recorded in CLAUDE.md and resources/README.md, no D-entry): papers stored as
  `<Key>_<title>.pdf` with notes files. When two copies arrive, keep the cleaner one and record why.
- **Proposed only, not decided:**
  - contraction ratio 6–9, square section, 5th-order-polynomial wall, L ≈ 1.0 × inlet height;
  - blower tunnel with a centrifugal fan;
  - mist injected downstream of the screens.

## 10. Open questions and blockers

- **Owner inputs needed for sizing:** floor or bench length, target top speed, any fan in mind.
- Blower vs suction tunnel; exit diffuser or not (it roughly halves fan power).
- Re-matched C_D reference: Achenbach covers only Re ≥ 5×10⁴.
- Blockage-correction method.
- Microcontroller/DAQ; op-amp role; pressure-sensor and load-cell ranges (unchanged).
- D-003 and D-004 still Tentative.
- Copyright: the Mehta1979 PDF is under Cambridge Core terms; the Abdelhamed2014 licence is not checked. Fine while
  the repo is private.

## 11. Remaining tasks

See TODO.md:

- **P0:** commit and push the second wrap's doc updates; sizing inputs; confirm D-003 and D-004. (`5bc60f0` is
  pushed, and `/wrap` is now Verified.)
- **P1:**
  - size the contraction and test section;
  - get and review the free "Wanted" documents;
  - size the fan;
  - choose the blockage correction;
  - pick the C_D reference;
  - choose the DAQ, sensors and load cell; buy hardware.
- **P2:** optional mist visualization, and the build steps.

## 12. Recommended first task for the next agent

Run `/catchup`. Expect `UP_TO_DATE` once the owner has pushed the second wrap's commit. The next `/wrap` adds that
commit's hash to this log's Commit line, next to `5bc60f0`. If the fetch fails with "Could not resolve host", see the
network lesson in PROJECT_BACKGROUND.md before blaming the sandbox.

If the owner has provided the sizing inputs (check PROJECT_BACKGROUND "Requirements and constraints"), start
**build step 1: size the contraction and test section**. Use the rules in `resources/notes/` (read the notes, not
the PDFs) and recompute the estimate tables for the chosen size and speed. Record the result in
docs/experimental_setup.md and a new D-entry.

If the inputs are still missing, ask for them first. Meanwhile, review any "Wanted" documents the owner has added to
`resources/`.

## 13. Manual Git commands (as given to the owner)

See [Manual Git commands](#manual-git-commands) below.

## Manual Git commands

Two sets: the first `/wrap`'s commands (run by the owner; committed and pushed as `5bc60f0`), then
[the second `/wrap`'s commands](#follow-up-commit-second-wrap) for a small docs-only commit.

### First wrap (committed and pushed as 5bc60f0)

State at the first wrap: `FETCH_FAILED`. The PC's network was down (§8); the first wrap wrongly blamed the agent
sandbox. At `/catchup` (2026-10-30) the state was `UP_TO_DATE` with `cc51fff` on GitHub. Nothing was staged or
committed.

Run in PowerShell or Git Bash (the VS Code terminal is fine):

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# If it says BEHIND: run  git pull --ff-only  before continuing. UP_TO_DATE is expected.
git status
git diff
git add CLAUDE.md DECISIONS.md PROJECT_BACKGROUND.md PROJECT_STATUS.md README.md TODO.md
git add docs/experimental_setup.md docs/sessions/SESSION_LOG.md docs/sessions/2026-10-29-github-setup-and-agent-handoff.md docs/sessions/2026-10-31-literature-review-and-design-inputs.md
git add resources/README.md resources/notes/Abdelhamed2014.md resources/notes/Bell1988.md resources/notes/Mehta1979.md
git add resources/Abdelhamed2014_wind-tunnel-contraction-optimization.pdf resources/Bell1988_contraction-design-small-low-speed-tunnels.pdf resources/Mehta1979_design-rules-small-low-speed-wind-tunnels.pdf
git status
git diff --cached --stat
git diff --cached
git commit -m "Add literature review, resources folder and design inputs" -m "Adds resources/ with three reviewed papers (Abdelhamed 2014, Bell & Mehta 1988, Mehta & Bradshaw 1979) and their reading notes, decision D-005 (segmented printing on the P1S), printable-size and fan estimates, a checked further-reading list and an optional mist-visualization task. Updates status and TODO, and backfills cc51fff into the 2026-10-29 log."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- **Staging:** before staging, `git status` lists 9 modified files plus two untracked entries: the new session log
  and the `resources/` folder. After staging, all 17 files show as "modified" or "new file". Nothing under `scripts/__pycache__` or `tests/__pycache__` should appear (they are ignored).
- **The three PDFs** are binary, about 5.5 MB together, within the D-004 size policy and stored as binary by
  `.gitattributes`. The Mehta1979 PDF is under Cambridge Core terms of use. That is fine in this private repo; review
  it before making the repo public.
- **To keep the PDFs out of Git**, skip the fourth `git add` line. They stay untracked locally, but the "PDF" links in
  the notes will not work on GitHub or another machine.
- **After `git diff --cached`**, press `q` to leave the pager.
- **Pushing:** tracking was set by the first push, so `git push origin HEAD` (or plain `git push`) is enough. The last
  command should end with `STATE: UP_TO_DATE`.
- **If Git warns "LF will be replaced by CRLF"**, that is harmless.
- **If the push asks for credentials:** run `gh auth status` or `gh auth login`, or sign in through Git Credential
  Manager.
- **If the push is rejected** ("fetch first" / "non-fast-forward"), GitHub has commits you do not. Do not force-push.
  Run `git pull --rebase origin main`, then `python -m unittest discover -s tests`, then `git push origin HEAD`. If
  the rebase stops on conflicts: run `git status`, edit the listed files, `git add <file>`, then
  `git rebase --continue`. `git rebase --abort` returns to where you started.

**Outcome (2026-10-31):**
- The owner ran these commands. Both fetches failed, and the owner carried on (the commands did not say to stop on
  `FETCH_FAILED`). The commit worked (`5bc60f0`, 17 files); the push failed.
- After fixing the network, the owner ran `git fetch origin`, `python scripts/sync_status.py --fetch` (`AHEAD`, 1
  commit), `git push origin HEAD` (`cc51fff..5bc60f0`) and `python scripts/sync_status.py --fetch` (`UP_TO_DATE`).

### Follow-up commit (second wrap)

State at the second wrap: `UP_TO_DATE` at `5bc60f0`. Five docs files are modified, with no new files; nothing is
staged or committed.

```bash
cd "C:/Users/nuhbm/OneDrive/Desktop/nuhs projects/2 - Wind Tunnel"
git fetch origin
python scripts/sync_status.py --fetch
# Expect UP_TO_DATE. If BEHIND: run  git pull --ff-only  first.
# If FETCH_FAILED: stop and fix the network first (PROJECT_BACKGROUND.md, Lessons learned).
git status
git diff
git add PROJECT_BACKGROUND.md PROJECT_STATUS.md TODO.md docs/sessions/SESSION_LOG.md docs/sessions/2026-10-31-literature-review-and-design-inputs.md
git diff --cached --stat
git commit -m "Record push of 5bc60f0 and mark /wrap verified" -m "The owner pushed 5bc60f0 with the commands from the first /wrap, which completes the /wrap verification. Backfills the hash, moves the push task to Done, and corrects the session log: the fetch and Amazon-link failures came from the PC losing its IPv4 address, not the agent sandbox or Firefox. Adds that lesson to PROJECT_BACKGROUND.md."
git push origin HEAD
python scripts/sync_status.py --fetch
```

- `git status` should list exactly the five files above as modified, and nothing untracked.
- The last command should end with `STATE: UP_TO_DATE`.
- The LF/CRLF warnings, credentials and rejected-push notes for the first wrap apply here too.
