import pytest

from models.lawn_grass import LawnGrass
from models.product import Product
from models.category import Category
from  models.category_iterator import CategoryIterator
from models.smartphone import Smartphone


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


def test_smartphone_init():
    phone = Smartphone("iphone", "Смартфон", 120000, 5, "A17", "15 Pro", 256, "Черный")

    assert phone.name == "iphone"
    assert phone.prise == 120000
    assert phone.quantity == 5
    assert phone.model == "15 Pro"


def test_lawn_grass_init():
    grass = LawnGrass("Газон","Зеленая трава", 500, 20, "Россия", "10 дней", "Зеленый")

    assert grass.name == "Газон"
    assert grass.country == "Россия"
    assert grass.germination_period == ("10 дней")


def test_add_different_classes():
    product = Product("Товары", "Описание", 100, 10)
    phone = Smartphone("iphone", "Телефон", 100000, 5, "Высокая", "15 Pro", 256, "Черный")

    with pytest.raises(TypeError):
        product + phone


def test_add_same_slasses():
    phone1 = Smartphone("iphone", "Телефон", 100000, 5, "Высокая", "15 Pro", 256, "Черный")
    phone2 = Smartphone("Samsung", "Телефон", 80000, 3, "Высокая", "S24", 256, "Белый")

    assert phone2 + phone1 == 740000


