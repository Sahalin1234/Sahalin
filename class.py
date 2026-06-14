from itertools import product
from models.product import Product
from models.category import Category

product1= Product("iphone", "512GB", 100, 10 )
product2 = Product("iphone2", "512GB", 200, 2)

print(product1 + product2)