from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam
from typing import Optional


class F1SeasonApp:
    VALID_NAMES = ["Red Bull", "Mercedes"]

    def __init__(self) -> None:
        self.red_bull_team: Optional[RedBullTeam] = None
        self.mercedes_team: Optional[MercedesTeam] = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name not in F1SeasonApp.VALID_NAMES:
            raise ValueError("Invalid team name!")
        if team_name == F1SeasonApp.VALID_NAMES[0]:
            self.red_bull_team = RedBullTeam(budget)
        if team_name == F1SeasonApp.VALID_NAMES[1]:
            self.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str,
                         red_bull_pos: int, mercedes_pos: int) -> str:

        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")
        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        winner = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"
        return f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. " \
               f"{winner} is ahead at the {race_name} race."
