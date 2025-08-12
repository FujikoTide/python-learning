from item_store import Store
from _types import items
from item import Item
from dataclasses import dataclass


@dataclass
class Cart(Store):
    shopping_cart: items

    def add_item(self, item: Item) -> Item | None:
        pass

    def remove_item(self, product_id: int) -> Item | None:
        pass

    def change_item_quantity(self, product_id: int, quantity: int) -> Item | None:
        pass

    def calculate_total(self) -> float:
        pass
    
    def apply_percentage_discount(self, discount: int) -> float:
        pass
    
    def apply_gift_card(self, card_value: int) -> float: