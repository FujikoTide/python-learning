from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    name: str
    price: float


@dataclass
class OrderItem:
    item: Item
    quantity: int = 0

    def get_total(self):
        return self.quantity * self.item.price


@dataclass
class Order:
    _order_items: List[OrderItem] = field(init=False)

    def __post_init__(self):
        self._order_items = []

    def add_item(self, item, quantity):
        new_item = OrderItem(item, quantity)
        self._order_items.append(new_item)

    def calculate_total_order_price(self):
        item_totals = [item.get_total() for item in self._order_items]
        return round(sum(item_totals), 2)


cat = Item("cat", 5)
shoe = Item("shoe", 6)
horse = Item("horse", 13)
button = Item("button", 2)

print(cat)
print(shoe)
print(horse)
print(button)

order = Order()
print(order)

order.add_item(cat, 3)
order.add_item(shoe, 4)
order.add_item(horse, 4)
order.add_item(button, 57)

print(order)

print(order.calculate_total_order_price())
