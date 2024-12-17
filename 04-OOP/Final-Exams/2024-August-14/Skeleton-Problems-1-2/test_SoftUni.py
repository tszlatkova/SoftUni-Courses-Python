# RoyalZone zone_info method
from unittest import TestCase, main
from project.zones.royal_zone import RoyalZone


class TestMethodClass(TestCase):
    def test_correct_class_method(self):
        self.obj = RoyalZone(code='123')

        # no ships
        result = self.obj.zone_info()
        self.assertEqual(result.strip(), """@Royal Zone Statistics@
Code: 123; Volume: 10
Battleships currently in the Royal Zone: 0, 0 out of them are Pirate Battleships.""")


if __name__ == '__main__':
    main()

# Manager statistics method - simple cases
import unittest
from project.battle_manager import BattleManager, RoyalBattleship, PirateBattleship, \
    RoyalZone, PirateZone


class TestBattleManager(unittest.TestCase):

    def setUp(self):
        self.manager = BattleManager()

    def test_get_statistics_no_zones_or_no_ships__simple_cases(self):
        expected_output = """Available Battleships: 0
***Zones Statistics:***
Total Zones: 0"""
        self.assertEqual(self.manager.get_statistics().strip(), expected_output)

        # test_get_statistics_no_ships_one_royal_zone
        self.manager.add_zone("RoyalZone", "001")

        expected_output = """Available Battleships: 0
***Zones Statistics:***
Total Zones: 1
@Royal Zone Statistics@
Code: 001; Volume: 10
Battleships currently in the Royal Zone: 0, 0 out of them are Pirate Battleships."""
        self.assertEqual(self.manager.get_statistics().strip(), expected_output)

        # test_get_statistics_no_ships_one_pirate_zone
        self.manager.zones.clear()
        self.manager.add_zone("PirateZone", "002")

        expected_output = """Available Battleships: 0
***Zones Statistics:***
Total Zones: 1
@Pirate Zone Statistics@
Code: 002; Volume: 8
Battleships currently in the Pirate Zone: 0, 0 out of them are Royal Battleships."""
        self.assertEqual(self.manager.get_statistics().strip(), expected_output)

        # test_get_statistics_no_zones_one_ship
        self.manager.zones.clear()
        self.manager.add_battleship("RoyalBattleship", "Royal", 100, 50)

        expected_output = """Available Battleships: 1
#Royal#
***Zones Statistics:***
Total Zones: 0"""
        self.assertEqual(self.manager.get_statistics().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()