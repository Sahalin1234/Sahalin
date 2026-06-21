from itertools import product

from models.base_entity import BaseEntity
from models.expertion import ProductQuantityError
from models.product import Product
class Category(BaseEntity):

    category_count = 0
    product_count = 0
    def __init__(self, name: str, description: str, products:list):
        self.__name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def name(self):
       return self.__name

    def add_product(self, product):
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добовлять только объекты Product")
            if product.quantity == 0:
                raise ProductQuantityError("Товар с нулевым количеством не может быть добавлен")
            self.__products.append(product)
        except ProductQuantityError as e:
            print(e)
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавленич товара завершина")

    @property
    def products(self):
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.prise} руб. "
                                 f"Остаток: {product.quantity} шт.")
        return "\n".join(products_list)

    def __len__(self):
        #return sum(prod.quantity for ptod in self.__products)
        total = 0
        for prod in self.__products:
            total += prod.quantity
            return total

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def get_products(self):
        return self.__products

    @property
    def average_prise(self):
        try:
            total_prise = sum(product.price for product in self.__products)
            return total_prise / len(self.__products)
        except ZeroDivisionError:
            return 0

