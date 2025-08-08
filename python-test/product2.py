from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int
    _tax_rate: float = 0.05

    def add_stock(self, quantity: int):
        self.quantity += quantity

    def remove_stock(self, quantity_to_remove: int):
        if self.quantity - quantity_to_remove < 0:
            raise ValueError(
                f"Cannot remove {quantity_to_remove} from stock, stock: {self.quantity}"
            )
        self.quantity -= quantity_to_remove

    @classmethod
    def calculate_price_with_tax(cls, base_price: float) -> float:
        return round((cls._tax_rate + 1) * base_price, 2)


product = Product("hat", 12.99, 3)
print(product.calculate_price_with_tax(product.price))
Product._tax_rate = 0.20
print(product.calculate_price_with_tax(product.price))
