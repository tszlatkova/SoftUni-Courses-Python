from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.WEIGHT)

    @property
    def increase_weight(self) -> int:
        return 1
