from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):

    MATERIAL = 'Wood/Plastic'
    SUB_TYPE = 'Toys'
    DISCOUNT_PERCENTAGE = 20

    def __init__(self, model, price):
        super().__init__(model, price, self.MATERIAL, self.SUB_TYPE)

    def discount(self):
        self.price *= (1 - self.DISCOUNT_PERCENTAGE / 100)
