from typing import List

from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient

from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:

    PLANT_TYPES = {"Flower": Flower, "LeafPlant": LeafPlant}
    CLIENT_TYPES = {"BusinessClient": BusinessClient, "RegularClient": RegularClient}

    def __init__(self):
        self.income: float = 0.0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float,
                  plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.PLANT_TYPES:
            raise ValueError("Unknown plant type!")
        new_plant = self.PLANT_TYPES[plant_type](plant_name, plant_price,
                                                 plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.CLIENT_TYPES:
            raise ValueError("Unknown client type!")

        client_with_same_number = next((cl for cl in self.clients if
                                       cl.phone_number == client_phone_number), None)
        if client_with_same_number:
            raise ValueError("This phone number has been used!")

        new_client = self.CLIENT_TYPES[client_type](client_name, client_phone_number)
        self.clients.append(new_client)

        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((cl for cl in self.clients
                       if cl.phone_number == client_phone_number), None)
        if not client:
            raise ValueError("Client not found!")

        plants = [pl for pl in self.plants if pl.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:  # not enough quantity
            return "Not enough plant quantity."

        needed_quantity_plants = plants[:plant_quantity]

        order_amount = 0
        for plant in needed_quantity_plants:
            self.plants.remove(plant)
            order_amount += plant.price * (1-client.discount / 100)
        client.update_total_orders()
        self.income += order_amount
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        plant = next((pl for pl in self.plants if pl.name == plant_name), None)
        if not plant:
            return "No such plant name."
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        clients_with_no_orders = [cl for cl in self.clients if cl.total_orders == 0]
        for cl in clients_with_no_orders:
            self.clients.remove(cl)
        return f"{len(clients_with_no_orders)} client/s removed."

    def shop_report(self):
        unsold_plants = {}

        for plant in self.plants:
            if plant.name not in unsold_plants:
                unsold_plants[plant.name] = 0
            unsold_plants[plant.name] += 1

        sorted_unsold_plants = dict(sorted(unsold_plants.items(),
                                           key=lambda x: (-x[1], x[0])))

        sorted_plants_info = '\n'.join([f"{k}: {v}" for k, v in
                                        sorted_unsold_plants.items()])

        sorted_clients = sorted(self.clients,
                                key=lambda x: (-x.total_orders, x.phone_number))

        sorted_clients_info = '\n'.join([cl.client_details() for cl in sorted_clients])

        count_of_all_orders = sum(cl.total_orders for cl in self.clients)

        result = f"~Flower Shop Report~\nIncome: {self.income:.2f}\n"
        result += f"Count of orders: {count_of_all_orders}\n"
        result += f"~~Unsold plants: {len(self.plants)}~~\n"
        result += sorted_plants_info
        result += '\n' if len(sorted_plants_info) > 0 else ""
        result += f"~~Clients number: {len(self.clients)}~~"
        result += '\n' if len(sorted_clients_info) > 0 else ""
        result += sorted_clients_info

        return result
