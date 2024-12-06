from project.formula_teams.formula_team import FormulaTeam
from typing import Dict


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int) -> None:
        super().__init__(budget)

    @property
    def team_data(self) -> tuple:
        expenses: int = 250000
        sponsors: Dict[str, Dict[int, int]] = {'Oracle': {1: 1500000, 2: 800000},
                                               'Honda': {8: 20000, 10: 10000}}
        return expenses, sponsors
