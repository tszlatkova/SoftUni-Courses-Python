from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tp = TennisPlayer("Grigor", 37, 100)
        self.tp2 = TennisPlayer("Pesho", 35, 101)

    def test_init(self):
        self.assertEqual("Grigor", self.tp.name)
        self.assertEqual(37, self.tp.age)
        self.assertEqual(100, self.tp.points)
        self.assertEqual([], self.tp.wins)

    def test_tennis_player_set_name_len_raises(self):
        # less than 2
        with self.assertRaises(ValueError) as ex:
            self.tp.name = ""

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

        # equal to 2
        with self.assertRaises(ValueError) as ex:
            self.tp.name = "Gr"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_tennis_player_age_less_than_eighteen_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.tp.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_tennis_player_add_new_win_tournament_name_not_in_wins(self):
        self.assertEqual([], self.tp.wins)

        self.tp.add_new_win("O2")

        self.assertEqual(["O2"], self.tp.wins)

        # If we have some tournament, to add it to the end
        self.tp.add_new_win("Wimbledon")
        self.assertEqual(["O2", "Wimbledon"], self.tp.wins)

    def test_tennis_player_add_new_win_tournament_already_in_wins(self):
        self.assertEqual([], self.tp.wins)

        self.tp.add_new_win("O2")

        self.assertEqual(["O2"], self.tp.wins)

        result = self.tp.add_new_win("O2")
        self.assertEqual("O2 has been already added to the list of wins!", result)

    def test_tennis_player_if_has_lower_points_than_other_player(self):
        self.assertEqual(100, self.tp.points)
        self.assertEqual(101, self.tp2.points)
        result = self.tp.__lt__(self.tp2)

        self.assertEqual("Pesho is a top seeded player and he/she is better than Grigor",
                         result)

        self.assertEqual(100, self.tp.points)
        self.assertEqual(101, self.tp2.points)

    def test_tennis_player_if_has_greater_or_equal_points_than_other_player(self):
        self.assertEqual(100, self.tp.points)
        self.assertEqual(101, self.tp2.points)
        result = self.tp2.__lt__(self.tp)

        self.assertEqual("Pesho is a better player than Grigor", result)

        self.assertEqual(100, self.tp.points)
        self.assertEqual(101, self.tp2.points)

    def test_string_representation_of_tennis_player(self):
        result = str(self.tp)
        self.assertEqual("Tennis Player: Grigor\nAge: 37\nPoints: 100.0\n"
                         "Tournaments won: ", result)

        self.tp.add_new_win("O2")
        self.tp.add_new_win("Wimbledon")
        result = str(self.tp)

        self.assertEqual("Tennis Player: Grigor\nAge: 37\nPoints: 100.0\n"
                         "Tournaments won: O2, Wimbledon", result)


if __name__ == "__main__":
    main()
