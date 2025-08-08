from dataclasses import dataclass
from typing import Dict


class ProductNotFoundException(Exception):
    def __init__(self, product_id):
        self.product_id = product_id
        super().__init__(f"Product with ID '{product_id}' not found")


# dummy Product class
@dataclass
class Product:
    name: str


@dataclass
class Inventory:
    products: Dict[int, Product]

    def get_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundException(product_id)
        return self.products[product_id]


prod1 = Product("cat")
prod2 = Product("shoe")
prod3 = Product("horse")

products = {1: prod1, 2: prod2, 3: prod3}

inventory = Inventory(products)

print(inventory.products)
print(inventory)
print(inventory.get_product(1))
print(inventory.get_product(7))
