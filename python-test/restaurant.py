from typing import List


class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"MenuItem(item_name={self.name}, price={self.price})"


class Restaurant:
    def __init__(self, name: str, cuisine_type: str):
        self.name = name
        self.cuisine_type = cuisine_type
        self._menu: List[MenuItem] = []

    def __repr__(self):
        return f"Restaurant(name={self.name}, cuisine_type={self.cuisine_type}, menu={self._menu[:5]})"

    def add_menu_item(self, item_name: str, price: float):
        new_item = MenuItem(item_name, price)
        self._menu.append(new_item)

    def display_menu(self):
        for dish in self._menu:
            print(f"{dish.name}: {dish.price}")


diner = Restaurant("American Diner", "American Fast Food")
print(diner)
diner.display_menu()
diner.add_menu_item("Hamburger", 3.99)
diner.add_menu_item("Cheeseburger", 4.99)
diner.add_menu_item("Hamburger", 3.99)
diner.add_menu_item("Cheeseburger", 4.99)
diner.add_menu_item("Hamburger", 3.99)
diner.add_menu_item("Cheeseburger", 4.99)
diner.add_menu_item("Hamburger", 3.99)
diner.add_menu_item("Cheeseburger", 4.99)
diner.add_menu_item("Hamburger", 3.99)
diner.add_menu_item("Cheeseburger", 4.99)
diner.add_menu_item("Hamburger", 3.99)
diner.add_menu_item("Cheeseburger", 4.99)
print(diner)
diner.display_menu()
