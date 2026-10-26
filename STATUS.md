# PadMint status

Updated **26 October 2026**. The [compatibility page](docs/COMPATIBILITY.md) has
the per-game detail, including **Status by game**, which is where the
compatibility work resumes.

**Scope today:** Windows build hardening resumed on 26 October at the owner's
request ([D17](docs/DECISIONS.md#d17-windows-build-hardening-resumes-26-oct-2026)).
The work covers reliable recipes, managed tools, safe retries, and private game
modules built on the player's computer. Current published routes remain the
source of truth: draft build evidence does not enable a catalog button or
establish device launch, audio or save compatibility. Game releases and device
deployment keep their separate approval and validation gates.

## Which games use PadMint

- **KartPad for Android is a ready-to-play download** (the APK has the game code
  built in) on [KartPad's releases](https://github.com/chrissotraidis/kartpad/releases/latest).
  On Android, PadMint makes the `KartPad game data` folder. KartPad for iPhone, iPad
  and Mac is built with PadMint; the release's `ios-for-padmint.ipa` has no game in it
  and is only for PadMint. The 0.7.9–0.7.13 ready-to-play iPhone/iPad and Mac
  downloads won't get updates.
- **HaloPad's Xbox edition** can also be built without a Mac, on GitHub's free Mac
  runner ([steps](https://github.com/chrissotraidis/projectreach#on-windows-linux-or-any-computer)).
  On Windows and Linux PadMint points there instead of saying it needs a Mac.
- **BlueWake on Windows** downloads its ready-to-play build from
  [BlueWake's releases](https://github.com/chrissotraidis/bluewake/releases/latest).
  The iPhone module route from Windows remains
  [draft #100](https://github.com/chrissotraidis/bluewake/pull/100), refreshed on
  current main but still awaiting a complete current Windows disc build.
- **Every other Pad game** builds through PadMint, or is a no-build download
  listed in PadMint.

## PadMint itself

- **v0.5.14**: no Mac? Fifteen games (BallPad, BarrelPad, BellPad, BrawlerPad,
  CTRPad, F0X, GalaxyPad, HarkinianPad, MaskPad, OpenRCT2 Touch, PaperPad,
  SpaghettiPad, StarshipPad, TribesPad, UTP) can be built for iPhone and iPad on
  GitHub's free Mac from Windows, Linux or any browser (\`build-for-iphone.yml\`;
  README "No Mac? Build on GitHub's Mac"). Off a Mac they get their own **Build on
  GitHub** tab, and each game page gives numbered steps with Fork PadMint,
  Step-by-step guide and Get Sideloadly buttons. Game pages on a Mac say how the
  copy gets onto the device (an .ipa installed with Sideloadly), fold the game-file
  note into one line, and label setup as **Setup: Xcode + Homebrew**. EctoPad is
  paused while Metaforce is private. SquirrelPad asks for 6 GB free instead of 30.
  EctoPad's and MeleePad's Rust setup lines work on a fresh Mac again.

- **v0.5.13**: a clearer library. The filters say what they hold (**Build your
  copy**, **Ready-made apps**, **Not on your devices**, **All systems**); a game
  that is already installed and current shows **Details** instead of a build or
  download button; ready-made apps with a newer release show **Update**; and My
  games groups everything without an update as **Installed, nothing to update**,
  with a note on apps PadMint can't check for updates. Tribes 2 (TribesPad) joins
  the catalog with its own icon.

- **v0.5.12**: the iOS 27 heads-up says what players actually see: a copy built
  with Xcode 27 that has no UIKit scene startup will probably close as soon as it
  opens on iOS or iPadOS 27, before it can write a log. PaperPad 0.2.2 did exactly
  that on an iPhone 18 Pro and an iPad ([paperpad#21](https://github.com/chrissotraidis/paperpad/issues/21));
  PaperPad 0.2.3, F0X 0.1.1 and SnapPad 0.2.1 fix it
  ([details](docs/COMPATIBILITY.md#ios-27-on-a-physical-ipad-18-to-21-october)).

- **v0.5.5**: a launcher. A sidebar lists **My games**, **Updates** and each
  iPhone, iPad and Mac PadMint can see; every game shows which version is on
  which device (read with Xcode's devicectl and from the Applications folders),
  and updates are compared with each game's latest release. Storage shows and
  frees PadMint's folder; PadMint can update itself on Mac and Linux.
  New builds: F0X, EctoPad, SnapPad, OpenRCT2 Touch and UTP. New Mac targets:
  F0X, EctoPad, SnapPad, BellPad, AnnePad, SunPad, MeleePad and BrawlerPad. RAtouch is listed as a download.
- **v0.5.5** also: after a newer version of a game builds, PadMint empties the
  `build/` folders that older versions left in `.padmint/games` and says how
  much space it freed. Source and `private/` folders stay, because KartPad's Mac
  guide points players at game files there; a folder another PadMint is using is
  skipped. The README now says KartPad for iPhone and iPad also builds on Windows
  and Linux (experimental, no Xcode).

- **v0.5.4**: KartPad's Mac build asks for about 12 GB free instead of 60 GB
  ([KartPad #489](https://github.com/chrissotraidis/kartpad/issues/489)). A clean
  KartPad 0.8.3 Mac build from an empty PadMint folder peaked at 9.3 GB; the 60 GB
  figure was never measured. Mobile copies keep their 16 GB budget.

- **v0.5.3**: clearer KartPad setup on Mac. PadMint restarts natively when opened
  through Rosetta on Apple Silicon, restoring **This Mac**. Intel Macs show why
  that copy is unavailable while retaining supported choices. KartPad's Mac plan
  showed a 60 GB disk budget (corrected in 0.5.4), and completion
  links directly to the Mac installation guide. Update guidance explains how to
  open the new ZIP without deleting existing builds, caches or saves.

- **v0.5.2**: GalaxyPad. PadMint builds GalaxyPad 0.2.0 for iPhone and iPad on an
  Apple Silicon Mac with Xcode, with no game file during the build: players import
  their own Super Mario Galaxy WBFS image in the app. `scripts/player-check.sh` takes
  `-` as the game file for games like this, whose game is chosen in the app.

- **v0.5.1**: KartPad on a Mac. With KartPad 0.8.0, PadMint offers KartPad's Mac copy
  again on Apple Silicon Macs (**This Mac**), using PadMint's own build tools (no
  Homebrew), and builds KartPad for iPhone and iPad on Intel Macs (with Xcode and its
  iOS platform). A recipe can say a program is needed only for some targets, so
  building KartPad for Android on a Mac doesn't ask for Xcode. When PadMint holds back
  a game's device on purpose, step 3 shows it dimmed and marked **Not yet**, with the
  devices to choose instead.

- **v0.5.0**: easier for someone new. The README starts with direct Mac, Windows and
  Linux download links (the ZIPs are now named `PadMint-macos.zip` and so on), and the
  Mac no longer needs a Terminal step first. On a Mac, each card says how much setup
  the game needs (**Easiest**, **Needs Xcode**, **Needs Xcode + Homebrew**). The file
  step says which version works ("Only the US (North American) version works"). The
  setup list says how to get Xcode when it's missing or not in use, gives one Homebrew
  line for everything missing, marks programs needed only for some files, finds
  Homebrew programs installed after PadMint started, and has **Check again**. A gray
  **Make my copy** says why. The file window opens in front. iPhone and iPad copies
  come with step-by-step Sideloadly instructions, also shown before the build.

- **v0.4.13**: clearer downloads. KartPad's card says its ready-to-play download is
  for Android ("Android: ready-to-play app"), and the download note appears only when
  you choose Android, with a **Download the Android app** button. It no longer
  suggests ready-to-play iPhone, iPad or Mac downloads. The Android plan says you get
  a game data folder. On Windows and Linux, HaloPad points to its Xbox edition's
  GitHub build instead of "Needs an M1+ Mac". README FAQs answer "Can I play KartPad
  on my Mac?" and building iPhone apps without a Mac.

- **v0.4.12**: PadMint checks the file you choose against the game's recipe before it
  builds: HaloPad says when you picked Bungie's 1.10 patch instead of the original
  installer, and choosing an Xbox ISO/XISO asks only for the Xbox tools (no Wine or
  PC tools). HaloPad 0.3.8's install line adds `llvm` and `sdl3`. Answers that arrive
  late from an older file choice no longer overwrite a newer one.

- **v0.4.11**: SquirrelPad joins the catalog for experimental iPhone/iPad personal
  builds on Apple Silicon Macs. Supply your own supported US Conker ROM; full
  Xcode and Metal Toolchain are required. Source and recipe only, no public IPA.
  BlueWake’s setup link now follows its current Install section.

- **v0.3.6**: one directory of every game (tabs for Build with PadMint, Download
  and Not available yet, console badges, search, back buttons). Games this
  computer can't build stay listed with the reason (**Needs an M1+ Mac**) instead
  of disappearing ([bellpad#20](https://github.com/chrissotraidis/bellpad/issues/20)).
  On a Mac the plan shows each game's install-once Homebrew line with a Copy
  button. README rewritten for every game.
- **v0.4.10**: KartPad's iPhone build on Windows and Linux works again. Since v0.4.7
  PadMint asked those computers for Xcode's iOS platform, which only exists on a Mac,
  and stopped before building. The check now runs on Macs only, and
  `scripts/audit-catalog.py` reports any Windows or Linux route that asks for Xcode.
- **v0.4.9**: HaloPad's setup opens its Wine installation guide instead of asking
  Homebrew to install the disabled `wine-stable` cask. Existing working Wine installs
  can still be used. HaloPad 0.3.6 supplies the matching recipe guidance.
- **v0.4.8**: HaloPad builds both editions: Custom Edition and the Xbox edition
  (its engine fetched from upstream and built on your Mac), for iPhone, iPad and Mac.
- **v0.4.7**: every iPhone build made with Xcode checks Xcode's iOS platform before
  it starts (12 games had no check), and a missing program now stops PadMint before
  it downloads the game's source instead of after. PaperPad no longer asks for the
  ROM before building (the app asks for it). `scripts/audit-catalog.py` checks the
  whole catalog against each game's published recipe; it reports no problems.
- **v0.4.6**: HaloPad builds for Mac too: the same app on Apple Silicon Macs, with
  keyboard and mouse and no Apple account needed.
- **v0.4.5**: build-time wording matches reality: the first build takes "a few
  minutes to a few hours" (CTRPad takes about a minute), and the terminal plan no
  longer says the copy is built from your game file when the game asks for it in
  the app. CTRPad v0.2.1 and v0.2.2 from PadMint ran on an iPhone 14 (iOS 26.6.2).
- **v0.4.4**: a release recipe that couldn't be read is tried again on the next
  plan instead of leaving an empty plan for the rest of the window. Copies from
  decompilation ports built without the player's game say only that they hold
  game code. README covers Mac copies.
- **v0.4.3**: a game's Mac copy is offered only on Apple Silicon Macs, where it
  runs, and the choice reads **This Mac**. CTRPad gets Mac finishing steps and a
  PlayStation badge.
- **v0.4.2**: CTRPad is back: PadMint builds Crash Team Racing for iPhone, iPad
  and Apple Silicon Mac from CTRPad's public source, and players choose their own
  disc image in the app. CTRPad's releases publish the recipe only.
- **v0.4.1**: HaloPad can be built: your own Halo Custom Edition installer and
  product key make HaloPad for iPhone and iPad, with your game package handed over
  beside it.
- **v0.4.0**: the unzipped folder shows only the launcher, **Start here.txt**
  (English, Spanish, Portuguese) and an **app** folder. On the page, **How it
  works** is at the top, the PadMint logo takes you back to the game list, and
  **Make another copy** goes back to the list instead of showing the finished
  build again. New logo.
- **v0.3.9**: SwiftUI apps (GoldenPad) are recognised as scene-based, so they get
  no iOS 27 warning.
- **v0.3.8**: the download apps (CaesarPad, DaggerPad, DevilTouch, Emerald
  Tablet, KidPad, PeonPad, VaultPad) show all their steps again; 0.3.6 and 0.3.7
  showed only the first.
- **v0.3.7**: the finish screen warns when a copy may not open on iOS 27
  (see below).
- **v0.3.5**: alphabetical game list with console filters and search, language
  switching that keeps your choices, release lookup that skips releases
  without a PadMint recipe, and the KartPad ready-to-play notice.
- The player page (0.3.4 and later) shows each step as it happens: release,
  source, every tool download with its size and source, the build stages and
  where the result is saved. English, Spanish and Portuguese.
- Checks: source tests, packaged player-flow CI on Windows, Mac and Linux, and
  the packages' content gate.

## Where the compatibility work stands

**Mac builds, 4 October:** every game PadMint builds was built from its latest
public recipe on one Apple Silicon Mac with Xcode 27; all that ran completed,
including StarshipPad v0.2.0, whose old SDK-selection failure no longer happens
([recorded Mac builds](docs/COMPATIBILITY.md#recorded-mac-builds-4-october)).
**iOS 27:** 10 of those apps were linked with the iOS 27 SDK without UIKit scene
startup, which Apple requires. On a physical iPad with iPadOS 27 (18 October), every
game's latest PadMint build opened except PaperPad 0.2.2, whose 4 October fix had
reached only PaperPad Original; F0X 0.1.0 and SnapPad 0.2.0, released later, also
lacked it. PaperPad 0.2.3, F0X 0.1.1 and SnapPad 0.2.1 (21 October) fix them
([details](docs/COMPATIBILITY.md#ios-27-on-a-physical-ipad-18-to-21-october)).

Current Windows work, with [per-game evidence and remaining gates](docs/COMPATIBILITY.md#status-by-game):

- All 15 games offered through the hosted Mac route passed fresh builds at
  PadMint `4a78bb0` ([run](https://github.com/chrissotraidis/padmint/actions/runs/40209016384)).
  This is the existing route available from Windows; the builds execute on Macs.
- Shared drafts [#177](https://github.com/chrissotraidis/padmint/pull/177),
  [#178](https://github.com/chrissotraidis/padmint/pull/178),
  [#179](https://github.com/chrissotraidis/padmint/pull/179),
  [#180](https://github.com/chrissotraidis/padmint/pull/180) and
  [#182](https://github.com/chrissotraidis/padmint/pull/182) preserve failed source
  attempts, validate released recipes, distinguish installed build inputs, package
  revision-specific modules with identity files, and provide Windows MIPS patch
  compilation. Host selection keeps existing Mac packagers and options intact.
  At `05c48ae`, 435 tests and native Windows x64/ARM64 packaged runner and
  compiler probes passed. These are unreleased changes.
- SquirrelPad and GoldenPad have complete private Windows ARM64 module builds
  through packaged PadMint. Their private x64-toolchain backends also passed
  under ARM emulation, with native x64 generator CI as separate evidence.
  Matching empty shells exist locally; recipes and shells still need review,
  device testing and authorized releases.
- MeleePad's offline route builds both supported revisions on Mac without
  rebuilding Slippi. The actual packaged Windows ARM64 build also passed with
  maintained compiler defaults and cached inputs/tools. Native Slippi online
  builds remain a separate developer route.
- BearBirdPad's matching shell/module and static Mac builds passed. Private
  Windows ARM64 and emulated x64 backends passed with identical output. The
  normal packaged Windows ARM64 recipe also passed with fresh source preparation
  and cached tools. BananaPad, AnnePad, DinoPad,
  SnapPad and the remaining private-input ports still need individual work.
  Existing BlueWake and SunPad drafts retain their own release and runtime gates.

No published catalog host flags or releases are changed by this evidence.
The generic pipeline must ship before recipes that require it, followed by each matching game release
and its catalog change. [Issue #75](https://github.com/chrissotraidis/padmint/issues/75)
tracks the broader work.

Personal game outputs stay private. Content scans are technical checks;
publication and rights decisions are reviewed separately.

## Earlier evidence

The [historical status record](STATUS-HISTORY.md) keeps earlier versions of this
page verbatim.
