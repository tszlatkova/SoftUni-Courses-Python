from abc import ABC, abstractmethod
from typing import List

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):

    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: List[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda x: (-x.hit_strength, x.name))

    @staticmethod
    @abstractmethod
    def zone_type():
        pass

    @property
    def zone_information_ships(self):
        ships_from_this_zone = [ship for ship in self.ships if ship.is_attacking]
        ships_from_other_zone = [ship for ship in self.ships if not ship.is_attacking]
        return [ships_from_this_zone, ships_from_other_zone, ]

    def zone_info(self):
        other_zone_type = 'Royal' if self.zone_type() == 'Pirate' else 'Pirate'
        result = f"@{self.zone_type()} Zone Statistics@\n" \
                 f"Code: {self.code}; Volume: {self.volume}\n" \
                 f"Battleships currently in the {self.zone_type()} Zone: " \
                 f"{len(self.ships)}, {len(self.zone_information_ships[1])} out of " \
                 f"them are {other_zone_type} Battleships."
        ships_name = [ship.name for ship in self.get_ships()]

        return result + (f"\n#{', '.join(ships_name)}#" if len(ships_name) > 0 else '')
