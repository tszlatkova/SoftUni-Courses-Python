from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def food_that_eats(self):
        pass

    @property
    @abstractmethod
    def gain_weight(self) -> float:
        pass

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    def feed(self, food: Food) -> str or None:
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.gain_weight * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, " \
               f"{self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, " \
               f"{self.living_region}, {self.food_eaten}]"
