"""Exercise the release-check wrapper without downloading or building games."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PlayerCheckScriptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="player check ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/player-check.sh", self.root / "scripts/player-check.sh")
        (self.root / "padmint").mkdir()
        (self.root / "padmint/__init__.py").touch()
        (self.root / "padmint/__main__.py").write_text('''import json, os, pathlib, sys
home = pathlib.Path(os.environ['PADMINT_HOME'])
with open(os.environ['TEST_LOG'], 'a') as f:
    f.write(json.dumps({'args': sys.argv[1:], 'home': str(home), 'fresh': not home.exists()}) + '\\n')
if sys.argv[1] == 'tools':
    home.mkdir(parents=True)
    sys.exit(int(os.environ.get('FAIL_TOOLS', '0')))
''')
        self.checkout = self.root / "game source"
        self.checkout.mkdir()
        subprocess.run(["git", "init", "-q", str(self.checkout)], check=True)
        subprocess.run(["git", "-C", str(self.checkout), "-c", "user.name=Fixture",
                        "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture",
                        "--allow-empty"], check=True)
        self.log = self.root / "calls.jsonl"

    def run_check(self, checkout=True, app=None, fail=0):
        args = ["/bin/bash", str(self.root / "scripts/player-check.sh"), "fixture", "ios", "disc with spaces.iso"]
        if checkout:
            args.append(str(self.checkout))
        if app:
            args.append(app)
        env = dict(os.environ, TEST_LOG=str(self.log), TMPDIR=str(self.root), FAIL_TOOLS=str(fail))
        result = subprocess.run(args, cwd=self.root, env=env, capture_output=True, text=True)
        calls = [json.loads(row) for row in self.log.read_text().splitlines()]
        return result, calls

    def test_checkout_prepares_tools_then_passes_exact_app_path(self):
        result, calls = self.run_check(app="/tmp/base app $(no-shell).ipa")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([c['args'][0] for c in calls], ['tools', 'build'])
        self.assertTrue(calls[0]['fresh'])
        self.assertEqual(calls[0]['home'], calls[1]['home'])
        self.assertEqual(calls[1]['args'][-2:], ['--app', '/tmp/base app $(no-shell).ipa'])
        for call in calls:
            self.assertEqual(call['args'][call['args'].index('--target') + 1], 'ios')

    def test_relative_app_path_is_resolved_before_changing_directory(self):
        result, calls = self.run_check(app="base app.ipa")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(calls[-1]['args'][-1], str(self.root / 'base app.ipa'))

    def test_tool_failure_prevents_build_and_success_message(self):
        result, calls = self.run_check(fail=23)
        self.assertEqual(result.returncode, 23)
        self.assertEqual(len(calls), 1)
        self.assertNotIn('Player check passed', result.stdout)

    def test_checkout_without_base_app_still_works(self):
        result, calls = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('--app', calls[-1]['args'])

    def test_published_release_uses_make_with_empty_home(self):
        result, calls = self.run_check(checkout=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]['args'][:3], ['make', 'fixture', 'ios'])
        self.assertTrue(calls[0]['fresh'])


if __name__ == '__main__':
    unittest.main()
