from models.product import Product

class Smartphone(Product):
    def __init__(self, name, description, prise, quantity, efficiency, model, memory, color):
        super().__init__(name, description, prise, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        