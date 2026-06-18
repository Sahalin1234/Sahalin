from models.base_product import BaseProduct
from models.repr_mixin import ReprMixin


class Product(ReprMixin, BaseProduct):
    def __init__(self, name: str, description: str, prise: float, quantity: int):
        self.name = name
        self.description = description
        self.__prise = prise
        self.quantity = quantity

        print(repr(self))


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

    def __str__(self):
        return f"{self.name}, {self.prise} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.prise * self.quantity + other.prise * other.quantity



