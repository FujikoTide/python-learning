from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    stock: int
    currency_symbol: str = "$"

    def is_available(self, quantity: int) -> bool:
        return self.stock >= quantity
