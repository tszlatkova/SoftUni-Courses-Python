from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gain_weight(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gain_weight(self) -> float:
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
