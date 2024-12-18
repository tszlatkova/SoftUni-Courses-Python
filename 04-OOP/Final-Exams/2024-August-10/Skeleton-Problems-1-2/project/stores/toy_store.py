from project.stores.base_store import BaseStore


class ToyStore(BaseStore):

    TYPE_OF_STORE = "ToyStore"
    CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return self.TYPE_OF_STORE

    @property
    def store_models_information(self):
        models = {}

        for product in self.products:
            if product.model not in models:
                models[product.model] = []
            models[product.model].append(product.price)

        return models
