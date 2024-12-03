from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gain_weight(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
