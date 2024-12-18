from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse

from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.PRODUCT_TYPES:
            raise Exception("Invalid product type!")
        new_product = self.PRODUCT_TYPES[product_type](model, price)
        self.products.append(new_product)
        return f"A product of sub-type {new_product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")
        self.stores.append(self.STORE_TYPES[store_type](name, location))
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: 'BaseProduct'):
        if store.capacity - len(products) < 0:
            return f"Store {store.name} has no capacity for this purchase."
        matching_products = [p for p in products if p.sub_type.lower() in
                             store.store_type.lower()]

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        for product in matching_products:
            self.products.remove(product)
            store.products.append(product)
            store.capacity -= 1
            self.income += product.price
        return f"Store {store.name} successfully purchased {len(matching_products)} " \
               f"items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if store_name == s.name), None)
        if not store:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is " \
                   "inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, " \
               f"location: {store.location}."

    def discount_products(self, product_model: str):
        products_according_model = [p for p in self.products if p.model == product_model]
        applied_discount = [p.discount() for p in products_according_model]
        return f"Discount applied to {len(applied_discount)} products with " \
               f"model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if store_name == s.name), None)
        if store:
            return store.store_stats()
        return "There is no store registered under this name!"

    def statistics(self):
        result = f"Factory: {self.name}\nIncome: {self.income:.2f}\n"
        products_sum_price = sum([p.price for p in self.products])
        result += f"***Products Statistics***" + "\n" + \
                  f"Unsold Products: {len(self.products)}. " \
                  f"Total net price: {products_sum_price:.2f}\n"

        models = {}

        for product in self.products:
            if product.model not in models:
                models[product.model] = 0
            models[product.model] += 1

        sorted_models = dict(sorted(models.items()))

        for model, count in sorted_models.items():
            result += f"{model}: {count}\n"

        result += f"***Partner Stores: {len(self.stores)}***\n"

        store_names = sorted([s.name for s in self.stores])

        result += '\n'.join(store_names)

        return result
