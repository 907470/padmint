# PadMint roadmap: every game, from every computer

Updated 26 October 2026, PadMint 0.5.16. This is the working checklist for which
games PadMint can make on which computer, for which device, and what to do next.
Update it in the same pull request as the work: tick the box, change the cell,
and refresh the numbers with `scripts/demand-report.py` and
`scripts/audit-catalog.py`. Earlier decisions are in [DECISIONS.md](DECISIONS.md)
(D5, D13–D16); per-game details are in [COMPATIBILITY.md](COMPATIBILITY.md).
The focused Windows roster and active queue are in [WINDOWS.md](WINDOWS.md).
Tracking issue: #75.

## How PadMint ships today

- **Three ZIPs, one per system** (Mac, Windows, Linux) on PadMint's releases page.
  Each holds a launcher and an `app` folder. There is no installer, and no .dmg
  or .exe. The launcher starts PadMint on the player's own computer and opens its
  page in the web browser at `127.0.0.1`. The Windows ZIP includes Python; Mac
  and Linux use the system's Python 3.9 or newer.
- **PadMint.app** (a native Mac window around the same page, in a .dmg) is made by
  `scripts/package-mac-app.py` but is not published. It is signed ad hoc, so it
  only suits the Mac that built it; publishing it without the **Open Anyway** step
  needs an Apple Developer ID.
- **Updates:** Mac and Linux update themselves from the version button; Windows
  players download the new ZIP.
- **Everything PadMint downloads** (game sources, tools, builds) goes in
  `.padmint` in the player's home folder; finished copies go to Downloads.

### What a Windows player can actually do

1. Download the Windows ZIP, extract it, run PadMint, and get past SmartScreen
   (**More info → Run anyway**). The browser opens PadMint's page.
2. **Build here:** Mario Kart Wii (KartPad) is the only game PadMint compiles
   locally on Windows today. Choose **Android** for the game-data pack, or
   **iPhone or iPad** for an experimental IPA that the player installs with
   Sideloadly.
3. **GitHub Cloud Build:** fifteen games can build an iPhone/iPad IPA on a
   temporary macOS build machine hosted by GitHub. PadMint starts the workflow
   from Windows; Windows does not compile these games locally and nothing
   personal is uploaded.
4. **A ready-made app** (Caesar III, Daggerfall, Diablo, Fallout 2, Kid Pix,
   Pharaoh, Red Alert, Warcraft II): the page links the download and the install
   steps; there's nothing to build.
5. **My games** shows only copies PadMint built on this PC: PadMint can't see
   what's on an iPhone or iPad without a Mac with Xcode, and can't check Android
   phones.
6. **Apple Silicon Mac:** every other buildable game is dimmed with the reason.
   Some have private Windows proofs, but those proofs are not a published route.
   The active release queue is in [WINDOWS.md](WINDOWS.md).

Linux is the same, except that there's no tested way yet to put an iPhone app on
the device from Linux. An Intel Mac is the same as Windows.

### Windows and Linux build routes

Every iPhone/iPad game reaches Windows and Linux by one of two routes, decided by
when it reads the player's game file:

| Route | What compiles | Games |
|---|---|---|
| **Build here** on Windows | The player's Windows PC, from their game file | KartPad only, currently |
| **GitHub Cloud Build** | A temporary macOS build machine hosted by GitHub; PadMint on Windows starts it | BallPad, BarrelPad, BellPad, BrawlerPad, CTRPad, F0X, GalaxyPad, HarkinianPad, MaskPad, OpenRCT2 Touch, PaperPad, SpaghettiPad, StarshipPad, TribesPad, UTP |
| **Apple Silicon Mac** | A Mac with Xcode, or the project's own route | The remaining buildable titles; the seven Windows proofs still need a release and device check |

Uploading a player's disc or ROM to GitHub stays out (D15), which is why the
second group needs the local route.

EctoPad is paused (24 October 2026). It takes its game in the app, but its engine,
Metaforce, and Metaforce's Zeus library were made private by their developers
(AxioDL) until their own public release, so no build can download them. EctoPad
is listed as paused and returns, on the GitHub route too, once they are public.

## The rule

Every route makes the player's copy **on the player's computer, from the
player's own game files**. Releases publish source, recipes and apps with no
game code in them. A route that needs a ready-made app with game code inside
isn't a route; the answer is a PadMint build instead.

That rules out shortcuts such as publishing built decompilation apps, even where
an upstream project publishes builds. It also means some downloads that players
use today need a PadMint route before they can be replaced (see **First**).

## Who can make what, today

Rows are the computer PadMint runs on; columns are the device the player plays on.
"PadMint" means PadMint builds it; "the game's builder" means the game's own
repository builds it from the player's disc, but PadMint doesn't run it yet.

| PadMint on → to play on | iPhone / iPad | Mac | Android | Windows PC | Linux PC |
|---|---|---|---|---|---|
| **Mac, Apple Silicon** | PadMint: all 29 | PadMint: 12 | PadMint: KartPad's game part (see First). The game's builder: BlueWake | — | — |
| **Mac, Intel** | PadMint: KartPad (experimental) | — (needs Apple Silicon) | PadMint: KartPad's game part | — | — |
| **Windows** | PadMint local: KartPad, experimental. GitHub Cloud Build: 15 games. Private Windows proofs are not released | — (needs Apple Silicon) | PadMint: KartPad's game part. The game's builder: BlueWake (checked on a phone) | The game's builder: BlueWake. PadMint builds no Windows desktop games | — |
| **Linux** | PadMint local: KartPad, experimental, with no tested way to install it from Linux. GitHub Cloud Build: 15 games | — (needs Apple Silicon) | PadMint: KartPad's game part. The game's builder: BlueWake (untested past the disc check) | — | The game's builder: BlueWake. PadMint builds no Linux desktop games |
| **Android phone** (Termux) | — | — | PadMint: KartPad's game data (emulator only so far) | — | — |

The 8 apps that hold no game code at all (Caesar III, Daggerfall, Diablo,
Fallout 2, Kid Pix, Pharaoh, Red Alert, Warcraft II) install on an iPhone or iPad
from any computer that runs Sideloadly (Windows or Mac).

**Installing what PadMint made:**

| Device | From Mac | From Windows | From Linux |
|---|---|---|---|
| iPhone / iPad | Sideloadly or AltStore | Sideloadly | **Gap:** no tested tool (Sideloadly has no Linux version) |
| Android | Copy the APK or folder | Same | Same |
| Mac | Unzip to Applications | — | — |
| Windows / Linux PC | — | Unzip and run | Unzip and run |

**Why some cells are empty.** A Mac app has to be built with Apple's SDK, which
only runs on a Mac. An iPhone app can still be made off a Mac when its release
ships an app with no game code and PadMint builds the game part on the player's
computer (D13, D14); KartPad works this way, and every other game needs its code
split first. Android, Windows and Linux copies need a port to that system: only
KartPad, BlueWake (Android, Windows, Linux) and CTRPad (Windows, Linux, from its
upstream code) have one.

## What PadMint shows players

PadMint's library tells each computer what it can make above the search box and
uses three explicit labels: **Build here**, **GitHub Cloud Build**, and **Apple Silicon
Mac**. Every unavailable game explains which route applies. When a recipe or
release changes, the catalog, those labels, [WINDOWS.md](WINDOWS.md) and this
roadmap change in the same pull request.

## Demand

PadMint itself, all releases: Windows 1,299, Mac 1,270, Linux 434 downloads.

| Game | Stars | Visitors, 14 days | iPhone/iPad | Android | Mac | Windows | Linux |
|---|---:|---:|---:|---:|---:|---:|---:|
| kartpad | 685 | 13630 | 12592 | 73921 | 2149 | 0 | 0 |
| bluewake | 414 | 13379 | 869 | 0 | 0 | 13358 | 0 |
| harkinianpad | 393 | 534 | 1934 | 0 | 0 | 0 | 0 |
| goldenpad | 188 | 153 | 853 | 0 | 334 | 0 | 0 |
| sunpad | 188 | 864 | 1775 | 0 | 0 | 0 | 0 |
| openrct2touch | 134 | 35 | 0 | 0 | 0 | 0 | 0 |
| projectreach | 129 | 3198 | 9 | 0 | 9 | 0 | 0 |
| galaxypad | 96 | 2782 | 407 | 0 | 32 | 0 | 0 |
| spaghettipad | 59 | 50 | 525 | 0 | 0 | 0 | 0 |
| maskpad | 51 | 101 | 600 | 0 | 0 | 0 | 0 |
| meleepad | 51 | 275 | 889 | 0 | 0 | 0 | 0 |
| caesarpad | 50 | 30 | 38 | 0 | 0 | 0 | 0 |
| ectopad | 45 | 56 | 0 | 0 | 0 | 0 | 0 |
| paperpad | 42 | 68 | 315 | 0 | 0 | 0 | 0 |
| peonpad | 42 | 31 | 39 | 0 | 0 | 0 | 0 |
| deviltouch | 40 | 27 | 33 | 0 | 0 | 0 | 0 |
| agepad | 37 | 57 | 28 | 0 | 0 | 0 | 0 |
| bellpad | 37 | 108 | 212 | 0 | 0 | 0 | 0 |
| padmint | 28 | 2069 | 0 | 0 | 1270 | 1299 | 434 |
| annepad | 26 | 126 | 198 | 0 | 0 | 0 | 0 |
| ballpad | 25 | 104 | 102 | 0 | 0 | 0 | 0 |
| vaultpad | 21 | 15 | 25 | 0 | 0 | 0 | 0 |
| starshippad | 20 | 13 | 359 | 0 | 0 | 0 | 0 |
| brawlerpad | 18 | 110 | 197 | 0 | 0 | 0 | 0 |
| bearbirdpad | 17 | 42 | 175 | 0 | 0 | 0 | 0 |
| bananapad | 12 | 34 | 77 | 0 | 0 | 0 | 0 |
| snappad | 12 | 38 | 105 | 0 | 0 | 0 | 0 |
| utp | 12 | 36 | 98 | 0 | 0 | 0 | 0 |
| barrelpad | 11 | 27 | 60 | 0 | 0 | 0 | 0 |
| dinopad | 11 | 7 | 28 | 0 | 0 | 0 | 0 |
| f0x | 10 | 18 | 303 | 0 | 0 | 0 | 0 |
| daggerpad | 8 | 23 | 22 | 0 | 0 | 0 | 0 |
| ottsel | 8 | 159 | 0 | 0 | 0 | 0 | 0 |
| ratouch | 7 | 9 | 82 | 0 | 0 | 0 | 0 |
| emeraldtablet | 3 | 29 | 23 | 0 | 0 | 0 | 0 |
| kidpad | 3 | 9 | 56 | 0 | 0 | 0 | 0 |
| squirrelpad | 3 | 58 | 0 | 0 | 0 | 0 | 0 |
| ctrpad | 1 | 91 | 336 | 0 | 52 | 0 | 0 |

Stars and 14-day unique visitors from GitHub on 19 Oct 2026; downloads over all
releases. IPA counts include the code-free apps PadMint downloads while
building. OpenRCT2Touch is a GitHub fork.

## Checklist

### First: PadMint routes for the downloads players use most

- [ ] **KartPad on Android, built by PadMint.** PadMint already builds KartPad's
  Android game part (a library) from the player's disc on every computer. Add a
  KartPad Android app with no game code to KartPad's release, as its iPhone release
  already does (`ios-for-padmint.ipa`); point the recipe's `published_app` at
  it; have PadMint put the game part into it and save the finished APK; check it
  on a real phone, including updating over an older copy with saves.
- [ ] **BlueWake on Windows, built by PadMint.** Add a `windows` target to
  BlueWake's recipe that runs BlueWake's existing Windows builder from the player's
  disc; player-check it on a Windows PC; the game page says how to run it.
- [ ] **BlueWake on Android and Linux, built by PadMint**, the same way, from
  BlueWake's existing builders (Android is checked on a phone; Linux untested past
  the disc check).
- [ ] **Wording.** Once those exist, KartPad's and BlueWake's READMEs and PadMint's
  game pages point Android and Windows players at PadMint.
- [ ] **Android without a computer.** The Termux route makes KartPad's game data.
  With a code-free app it also needs the game part, which is a much heavier build
  for a phone; measure it before promising it.

### Next: iPhone and iPad from Windows and Linux

- [x] Release the shared PadMint 0.5.15 Windows infrastructure: managed tools,
  Unicode paths, safe caches/retries, Windows console handling and cancellation.
- [x] Show exact **Build here / GitHub Cloud Build / Apple Silicon Mac** routes in the
  PadMint UI and document the live Windows roster.
- [ ] Fix and release SnapPad's Windows hosts, then MeleePad's invalid
  `windows-x64` recipe key; add pinned manifest validation to both game CIs.
- [ ] Merge SunPad #57 and #78, then publish its Windows recipe and run the
  physical-device check.
- [ ] Publish SquirrelPad's shell and recipe; reuse the shell workflow for
  GoldenPad, BearBirdPad and BananaPad.
- [ ] Finish BlueWake's original-disc Windows backend, then AnnePad. Resolve
  AgePad's real installed-input mismatch, test DinoPad with its ROM, and design
  Ottsel's portable host-tool route.
- [ ] A tested way to install on an iPhone from Linux, then its steps.
- [ ] Engine ports through spaghettipad#29: SpaghettiPad, then HarkinianPad,
  MaskPad, StarshipPad, PaperPad, BrawlerPad.

### Later

- [ ] CTRPad for Windows and Linux PCs through PadMint, from its upstream code.
- [ ] Local-Windows recipes for games that currently use GitHub Cloud Build; do
  this one engine family at a time so shared fixes are proven before expanding.
- [ ] Real-hardware checks: a PadMint run on a real Windows PC; the Termux route on a
  real Android phone with 8 GB of memory.

### Not planned

- Mac copies made on Windows or Linux (needs Apple's SDK).
- AgePad and HaloPad off a Mac (D15); HaloPad's Xbox edition has its own route
  through GitHub Cloud Build.

Every route that moves needs a check before PadMint offers it: built on that
computer, installed, and the game starts on a real device.
