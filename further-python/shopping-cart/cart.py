from item_store import Store
from item import Item
from dataclasses import dataclass


@dataclass
class Cart(Store):
    def add_item(self, item: Item, quantity: int = 1) -> Item | None:
        pass

    def remove_item(self, product_id: int) -> Item | None:
        pass

    def change_item_quantity(self, product_id: int, quantity: int) -> Item | None:
        pass
