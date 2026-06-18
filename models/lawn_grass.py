from models.product import Product

class LawnGrass(Product):
    def __init__(self, name, description, prise, quantity, country, germination_period, color):
        super().__init__(name, description, prise, quantity,)
        self.country = country
        self.germination_period = germination_period
        self.color = color

        print(repr(self))

