import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))

from validate_full_game_content import (
    load,
    validate_data,
    WORLD_PATH,
    GAMEPLAY_PATH,
    CHARACTER_PATH,
)


class FullGameContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.world = load(WORLD_PATH)
        cls.gameplay = load(GAMEPLAY_PATH)
        cls.characters = load(CHARACTER_PATH)

    def test_full_catalogs_validate(self):
        self.assertEqual(
            validate_data(self.world, self.gameplay, self.characters),
            [],
        )

    def test_act_one_keeps_vertical_slice_aliases(self):
        quests = self.world["mainQuests"]
        for index, quest in enumerate(quests[:11], start=1):
            self.assertEqual(quest["id"], f"Q{index:02d}")
            self.assertEqual(quest["verticalSliceId"], f"VS1_Q{index:02d}")

    def test_mandatory_seed_loss_is_explicit(self):
        climax = next(q for q in self.world["mainQuests"] if q["id"] == "Q08")
        self.assertIn("seed reserve is lost", climax["consequence"])

    def test_npc_020_is_not_reused(self):
        self.assertNotIn("NPC-020", {npc["id"] for npc in self.characters["namedNpcs"]})

    def test_inventory_has_no_capacity_limit(self):
        self.assertIsNone(self.gameplay["resources"][0].get("capacityLimit"))
        self.assertEqual(self.world["rules"]["inventoryCapacity"], "unlimited")


if __name__ == "__main__":
    unittest.main()
