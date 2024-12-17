from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):

    INITIAL_AMMUNITION = 100

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.INITIAL_AMMUNITION)

    @staticmethod
    def reducing_ammunition():
        return 25

    @staticmethod
    def ship_type():
        return "Royal"
