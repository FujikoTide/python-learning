from item_store import Store
from item import Item
from dataclasses import dataclass


@dataclass
class Cart(Store):
    def add_item(self, item: Item, quantity: int = 1) -> Item | None:
        if quantity <= 0:
            return None
        if item._id not in self.items:
            self.items[item._id] = item
        self.quantities[item._id] = self.quantities.get(item._id, 0) + quantity
        return item

    def remove_item(self, item: Item) -> Item | None:
        if item._id not in self.items:
            return None
        del self.items[item._id]
        del self.quantities[item._id]
        return item

    def change_item_quantity(self, item: Item, quantity: int) -> Item | None:
        if item._id not in self.items:
            return None
        if self.quantities[item._id] + quantity <= 0:
            return self.remove_item(item)
        return self.add_item(item, quantity)

    def empty_cart(self):
        self.items = {}
        self.quantities = {}
