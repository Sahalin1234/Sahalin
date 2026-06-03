class Product:
    def __init__(self, name: str, description: str, prise: float, quantity: int):
        self.name = name
        self.description = description
        self.__prise = prise
        self.quantity = quantity


    @property
    def prise(self):
        return self.__prise

    @prise.setter
    def prise(self, new_prise):
        if new_prise <= 0:
            print("Цена введена некорректная")
            return
        if new_prise < self.__prise:
            answer = input("Цена ниже текущей. Подтвердить изминение?  (y/n):")
            if answer.lower() != "y":
                print("Изминение отменено")
                return

        self.__prise = new_prise


    @classmethod
    def create_product(cls, name, description, prise, quantity, products_list = None):
        if products_list:
            for product in products_list:
                if product.name == name:
                    product.quantity += quantity
                    product.prise = max(product.prise, prise)
                    return product
        return cls(name,  description, prise, quantity)
