from abc import ABC, abstractmethod
from typing import List, Dict

from project.products.base_product import BaseProduct


class BaseStore(ABC):

    ADDITIONAL_PERCENTAGE = 0.10

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Store name cannot be empty!")
        self.__name = value
        
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, value):
        if ' ' in value or len(value.strip()) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        future_profit = sum([product.price for product in self.products]) * \
                        self.ADDITIONAL_PERCENTAGE

        return f"Estimated future profit for {len(self.products)} products is " \
               f"{future_profit:.2f}"

    @property
    @abstractmethod
    def store_type(self) -> str:
        pass

    @property
    @abstractmethod
    def store_models_information(self) -> Dict:
        pass

    def store_stats(self):
        general_info = f"Store: {self.name}, location: {self.location}, available " \
                       f"capacity: {self.capacity}\n{self.get_estimated_profit()}"
        type_info = 'Furniture' if self.store_type == 'FurnitureStore' else 'Toys'
        result = general_info + '\n' + f"**{type_info} for sale:"
        sorted_models = dict(sorted(self.store_models_information.items()))
        list_models_info = [f"{k}: {len(v)}pcs, average price: {sum(v)/len(v):.2f}"
                            for k, v in sorted_models.items()]
        result += '\n' if len(list_models_info) > 0 else ''
        result += '\n'.join([model for model in list_models_info])

        return result
