from typing import List


class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price})"


class ShoppingCart:
    def __init__(self):
        self._items: List[Item] = []

    def __repr__(self):
        return f"ShoppingCart(items={self._items[:3]})"

    def add_item(self, name: str, price: float):
        new_item = Item(name, price)
        self._items.append(new_item)
        print(f"New item added: {name}")

    def get_total_price(self) -> float:
        if not self._items:
            return 0.0
        prices = [item.price for item in self._items]
        return round(sum(prices), 2)


cart = ShoppingCart()
print(cart)
print(cart.get_total_price())
cart.add_item("shoe", 4.99)
cart.add_item("hat", 12.99)
cart.add_item("lettuce", 0.99)
cart.add_item("whisky", 55.0)
cart.add_item("shoe", 4.99)
cart.add_item("hat", 12.99)
cart.add_item("lettuce", 0.99)
cart.add_item("whisky", 55.0)
cart.add_item("shoe", 4.99)
cart.add_item("hat", 12.99)
cart.add_item("lettuce", 0.99)
cart.add_item("whisky", 55.0)
print(cart)
print(cart.get_total_price())
