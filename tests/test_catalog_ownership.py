"""PadMint lists only Chris's own game ports (AGENTS.md: "Only Chris's own games")."""
import unittest

from padmint import manifest

OWNER = "https://github.com/chrissotraidis/"
# Recipe-only wrappers around other people's projects were removed and must not return.
NOT_OURS = {"melee-pc", "melee-pc-padmint"}


class OwnershipTests(unittest.TestCase):
    def test_every_entry_is_a_chrissotraidis_game_repository(self):
        for game, entry in manifest.catalog().items():
            with self.subTest(game=game):
                self.assertTrue(entry["repo_url"].startswith(OWNER), entry["repo_url"])
                self.assertNotIn(game, NOT_OURS)
                self.assertNotIn(entry["repo_url"].rstrip("/").rsplit("/", 1)[-1], NOT_OURS)

    def test_other_ports_only_name_our_own_catalog_games(self):
        games = manifest.catalog()
        for game, entry in games.items():
            for port in entry.get("other_ports", []):
                with self.subTest(game=game, port=port):
                    self.assertIn(port, games)
                    self.assertTrue(games[port]["repo_url"].startswith(OWNER))

    def test_the_build_workflow_offers_no_removed_project(self):
        workflow = (manifest.CATALOG.parent / ".github/workflows/build-for-iphone.yml").read_text()
        for name in NOT_OURS:
            self.assertNotIn(name, workflow)


if __name__ == "__main__":
    unittest.main()
