from itertools import product

class CategoryIterator:
    def __init__(self, category):
        self.products = category.get_products()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration

