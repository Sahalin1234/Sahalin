from models.product import Product
class Category:
    category_count = 0
    product_count = 0
    def __init__(self, name: str, description: str, products:list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)

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
