from models.base_entity import BaseEntity


class Order (BaseEntity):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self):
        return self.product.prise * self.quantity

    @property
    def name(self):
        return self.product.name