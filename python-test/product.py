class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def add_stock(self, quantity: int):
        self.quantity += quantity

    def remove_stock(self, quantity_to_remove: int):
        if self.quantity - quantity_to_remove < 0:
            raise ValueError(
                f"Cannot remove {quantity_to_remove} from stock, stock: {self.quantity}"
            )
        self.quantity -= quantity_to_remove
