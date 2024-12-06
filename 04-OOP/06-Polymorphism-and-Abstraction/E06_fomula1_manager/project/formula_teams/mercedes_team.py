from project.formula_teams.formula_team import FormulaTeam
from typing import Dict


class MercedesTeam(FormulaTeam):

    def __init__(self, budget: int) -> None:
        super().__init__(budget)

    @property
    def team_data(self) -> tuple:
        expenses: int = 200000
        sponsors: Dict[str, Dict[int, int]] = {'Petronas': {1: 1000000, 3: 500000},
                                               'TeamViewer': {5: 100000, 10: 50000}}
        return expenses, sponsors
