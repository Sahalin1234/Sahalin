import pytest

from models.product import Product
from models.category import Category
from  models.category_iterator import CategoryIterator
def test_product_init():
    product = Product("iphone 15", "512GB", 120000.500, 5)

    assert product.name == "iphone 15"
    assert product.description == "512GB"
    assert product.prise == 120000.500
    assert product.quantity == 5

def test_category_init():
    product = Product("iphone", "Телефон", 100000, 5)
    category = Category("Смартфоны", "Описание", [product])

    assert category.name == "Смартфоны"
    assert category.description == "Описание"
    assert category.products == "iphone, 100000 руб. Остаток: 5 шт."

def test_category_count():
    Category.category_count = 0
    product = Product("iphone", "Телефон", 100000, 2)
    Category("Смартфоны", "Описание", [product])

    assert Category.category_count == 1

def test_product_count():
    Category.product_count = 0
    product1 = Product("iphone", "Телефон", 120000.500, 5)
    product2 = Product("Samsuhg", "Телефон", 90000.0, 3)
    Category("Смартфоны", "Описание", [product1, product2])

    assert Category.product_count == 2

def test_add_product():
    category = Category("Телефоны", "Смартфоны",[])
    product = Product("iphone", "256GB", 100000, 5)

    category.add_product(product)

    assert "iphone" in category.products

def test_products_property():
    product = Product("Samsung", "s24", 50000, 10)
    category = Category("Телефоны", "Смартфоны", [product])

    assert category.products == ("Samsung, 50000 руб. Остаток: 10 шт.")

def test_create_product():
    product = Product.create_product("Samsung", "Телефон", 50000, 10)

    assert product.name == "Samsung"
    assert product.prise == 50000
    assert product.quantity == 10

def test_duplicate_product():
    products = []

    p1 = Product.create_product("iphone", "512GB", 50000, 10, products)
    products.append(p1)

    Product.create_product("iphone", "512GB", 55000, 5, products)

    assert p1.quantity == 15
    assert p1.prise == 55000

def test_prise_getter():
    product = Product("Samsung", "Телефон", 50000, 10)
    assert product.prise == 50000

def test_prise_setter():
    product = Product("Samsung", "Телефон", 50000, 10)
    product.prise = 60000
    assert product.prise == 60000

def test_prise_setter_negative():
    product = Product("Samsung", "Телефон", 50000, 10)
    product.prise = -100
    assert product.prise == 50000

def test_prise_setter_zero():
    product = Product("Samsung", "Телефон", 50000, 10)
    product.prise = 0
    assert product.prise == 50000

def test_prise_decrease_confirm(monkeypatch):
    product = Product("Samsung", "Телефон", 50000, 10)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.prise = 40000
    assert product.prise == 40000

def test_prise_decrease_cancel(monkeypatch):
    product = Product("Samsung", "Телефон", 50000, 10)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.prise = 40000
    assert product.prise == 50000

def test_product_str():
    product = Product("iphone", "Телефон", 100000, 5)
    assert str(product) == "iphone, 100000 руб. Остаток: 5 шт."

def test_category_str():
    product = Product("iphone", "Телефон", 100000, 5)
    category = Category("Смартфоны", "Описание", [product])
    assert str(category) == "Смартфоны, количество продуктов: 5 шт."

def test_product_add():
    product1 = Product("iphone", "512GB", 100, 10)
    product2 = Product("iphone2", "512GB", 200, 2)
    assert product1 + product2 == 1400

def test_category_iterator():
    product1 = Product("iphone", "Телефон", 100000, 5)
    product2 = Product("Samsung", "Телефон", 80000, 3)

    category = Category("Смартфоны", "Описание", [product1, product2])
    iterator = CategoryIterator(category)
    assert next(iterator) == product1
    assert next(iterator) == product2


def test_category_iterator_stop():
    product = Product("iphone", "Телефон", 100000, 5)
    category = Category("Смартфоны", "Описание", [product])
    iterator = CategoryIterator(category)
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)

def test_category_iterator_for():
    product1 = Product("iphone", "Телефон", 100000, 5)
    product2 = Product("Samsung", "Телефон", 80000, 3)

    category = Category("Смартфоны", "Описание", [product1, product2])
    iterator = CategoryIterator(category)
    result = []
    for product in iterator:
        result.append(product.name)

    assert result == ["iphone", "Samsung"]
