from project.soccer_player import SoccerPlayer

from unittest import TestCase, main


class TestSoccerPlayer(TestCase):

    def setUp(self) -> None:
        self.player1 = SoccerPlayer("Modric", 39, 28, "Real Madrid")
        self.player2 = SoccerPlayer("Rashford", 27, 87, "Manchester United")
        self.valid_teams = ["Barcelona", "Real Madrid", "Manchester United", "Juventus",
                            "PSG"]

    def test_soccer_init(self):
        self.assertEqual("Modric", self.player1.name)
        self.assertEqual(39, self.player1.age)
        self.assertEqual(28, self.player1.goals)
        self.assertEqual("Real Madrid", self.player1.team)
        self.assertEqual({}, self.player1.achievements)

    def test_name_not_valid_raise(self):
        # Under 5
        self.assertEqual("Modric", self.player1.name)

        with self.assertRaises(ValueError) as ex:
            self.player1.name = "Mod"

        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))
        self.assertEqual("Modric", self.player1.name)

        # Exactly 5
        self.assertEqual("Modric", self.player1.name)

        with self.assertRaises(ValueError) as ex:
            self.player1.name = "Modri"

        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))
        self.assertEqual("Modric", self.player1.name)

    def test_age_under_sixteen_raise(self):
        self.assertEqual(39, self.player1.age)

        with self.assertRaises(ValueError) as ex:
            self.player1.age = 15

        self.assertEqual(39, self.player1.age)
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_goals_negative_number_raise(self):
        self.assertEqual(28, self.player1.goals)

        self.player1.goals -= 30

        self.assertEqual(0, self.player1.goals)

    def test_team_not_valid_type_raise(self):
        self.assertEqual("Real Madrid", self.player1.team)

        with self.assertRaises(ValueError) as ex:
            self.player1.team = "Tottenham"

        self.assertEqual("Real Madrid", self.player1.team)
        self.assertEqual("Team must be one of the following: Barcelona, Real Madrid, "
                         "Manchester United, Juventus, PSG!", str(ex.exception))

    def test_change_team_not_valid_new_team(self):
        self.assertEqual("Real Madrid", self.player1.team)

        result = self.player1.change_team("Tottenham")

        self.assertEqual("Real Madrid", self.player1.team)
        self.assertEqual("Invalid team name!", result)

    def test_change_team_valid_new_team(self):
        self.assertEqual("Real Madrid", self.player1.team)

        result = self.player1.change_team("Juventus")

        self.assertEqual("Juventus", self.player1.team)
        self.assertEqual("Team successfully changed!", result)

    def test_add_new_achievement_not_existing_achievement(self):
        self.assertEqual({}, self.player1.achievements)

        result = self.player1.add_new_achievement("World Cup")

        self.assertEqual({"World Cup": 1}, self.player1.achievements)
        self.assertEqual("World Cup has been successfully added to the achievements "
                         "collection!", result)

        # Increase the count of the achievement if it's already existing
        result = self.player1.add_new_achievement("World Cup")
        self.assertEqual({"World Cup": 2}, self.player1.achievements)
        self.assertEqual("World Cup has been successfully added to the achievements "
                         "collection!", result)

    def test_compare_two_player_first_less_goals_than_the_second(self):
        self.assertEqual(28, self.player1.goals)
        self.assertEqual(87, self.player2.goals)

        result = self.player1.__lt__(self.player2)
        self.assertEqual(28, self.player1.goals)
        self.assertEqual(87, self.player2.goals)
        self.assertEqual("Rashford is a top goal scorer! S/he scored more than Modric.",
                         result)

        result = self.player2.__lt__(self.player1)
        self.assertEqual(28, self.player1.goals)
        self.assertEqual(87, self.player2.goals)
        self.assertEqual("Rashford is a better goal scorer than Modric.", result)


if __name__ == "__main__":
    main()
