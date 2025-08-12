from item_store import Store
from item import Item
from dataclasses import dataclass


@dataclass
class Cart(Store):
    discount_percentage: int = 0
    gift_card: int = 0
    tax: float = 20  # arbitrary default value

    def add_item(self, item: Item) -> Item | None:
        pass

    def remove_item(self, product_id: int) -> Item | None:
        pass

    def change_item_quantity(self, product_id: int, quantity: int) -> Item | None:
        pass

    def calculate_price(self):
        pass


cart = Cart()
