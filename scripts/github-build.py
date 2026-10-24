#!/usr/bin/env python3
"""Prepare GitHub's Mac for one game, the way a player prepares their own Mac.

Runs the game's before-build commands from its catalog entry (the commands PadMint
shows on the game's page), then puts Rust's tools on the next steps' PATH when a game
installed them. Used by .github/workflows/build-for-iphone.yml.

Usage: scripts/github-build.py GAME
"""
import os
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from padmint.manifest import catalog  # noqa: E402

# Rustup puts cargo in ~/.cargo/bin and asks the shell to read ~/.cargo/env.
SHELL_SETUP = 'set -e; if [ -f "$HOME/.cargo/env" ]; then . "$HOME/.cargo/env"; fi; '


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    game = sys.argv[1]
    entry = catalog().get(game)
    if not entry or not entry.get("github_build"):
        raise SystemExit(f"{game} is not built on GitHub's Mac: it reads your game file while it builds")
    for command in (entry.get("before_build") or {}).get("commands", []):
        print(f"+ {command}", flush=True)
        subprocess.run(["/bin/bash", "-c", SHELL_SETUP + command], check=True)
    cargo = Path.home() / ".cargo/bin"
    if cargo.is_dir() and os.environ.get("GITHUB_PATH"):
        with open(os.environ["GITHUB_PATH"], "a") as stream:
            stream.write(f"{cargo}\n")


if __name__ == "__main__":
    main()
