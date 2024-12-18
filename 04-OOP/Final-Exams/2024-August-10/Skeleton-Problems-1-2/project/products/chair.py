from project.products.base_product import BaseProduct


class Chair(BaseProduct):

    MATERIAL = 'Wood'
    SUB_TYPE = 'Furniture'
    DISCOUNT_PERCENTAGE = 10

    def __init__(self, model, price):
        super().__init__(model, price, self.MATERIAL, self.SUB_TYPE)

    def discount(self):
        self.price *= (1 - self.DISCOUNT_PERCENTAGE / 100)
