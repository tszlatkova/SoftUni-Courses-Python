from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship

from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    ZONE_TYPES = {"PirateZone": PirateZone, "RoyalZone": RoyalZone}
    SHIPS_TYPES = {"PirateBattleship": PirateBattleship,
                   "RoyalBattleship": RoyalBattleship}

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def search_zone_code(self, zone_code: str):
        return next((z for z in self.zones if z.code == zone_code), None)

    def search_ship_name(self, ship_name: str):
        return next((s for s in self.ships if s.name == ship_name), None)

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.ZONE_TYPES:
            raise Exception("Invalid zone type!")
        if self.search_zone_code(zone_code):
            raise Exception("Zone already exists!")
        new_zone = self.ZONE_TYPES[zone_type](zone_code)
        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.SHIPS_TYPES:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        new_ship = self.SHIPS_TYPES[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: 'BaseZone', ship: 'BaseBattleship'):
        if zone.volume - 1 < 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"
        if zone.zone_type() == ship.ship_type():
            ship.is_attacking = True
        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship_to_remove = self.search_ship_name(ship_name)
        if not ship_to_remove:
            return "No ship with this name!"
        if not ship_to_remove.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship_to_remove)
        return f"Successfully removed ship {ship_to_remove.name}."

    def start_battle(self, zone: 'BaseZone'):
        potential_attackers = [ship for ship in zone.ships if ship.is_attacking]
        potential_targets = [ship for ship in zone.ships if not ship.is_attacking]

        if not potential_attackers or not potential_targets:
            return "Not enough participants. The battle is canceled."
        most_powerful_ship = sorted(potential_attackers, key=lambda x: -x.hit_strength)[0]
        most_healthiest_ship = sorted(potential_targets, key=lambda x: -x.health)[0]
        most_powerful_ship.attack()
        most_healthiest_ship.take_damage(most_powerful_ship)
        if most_healthiest_ship.health <= 0:
            zone.ships.remove(most_healthiest_ship)
            self.ships.remove(most_healthiest_ship)
            return f"{most_healthiest_ship.name} lost the battle and was sunk."
        if most_powerful_ship.ammunition <= 0:
            zone.ships.remove(most_powerful_ship)
            self.ships.remove(most_powerful_ship)
            return f"{most_powerful_ship.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship.name for ship in self.ships if ship.is_available]
        ordered_zones = sorted(self.zones, key=lambda x: x.code)
        result = f"Available Battleships: {len(available_ships)}\n" + \
                 (f"#{', '.join(available_ships)}#\n" if available_ships else '')
        zone_info = [zone.zone_info() for zone in ordered_zones]
        result_zones = "***Zones Statistics:***\n" + f"Total Zones: {len(self.zones)}\n" \
                       + '\n'.join(zone_info)
        return result + result_zones
