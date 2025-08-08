from dataclasses import dataclass
from typing import Any, Optional


class PositiveNumber:
    _expected_type = float

    def __init__(self, default_value: float = 0.0) -> None:
        if not isinstance(default_value, self._expected_type) or default_value <= 0:
            raise ValueError("Default value must be a positive float")
        self.default_value = default_value
        self.private_name: Optional[str] = None

    def __set_name__(self, owner: Any, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance: Any, owner: Any) -> float:
        if instance is None:
            return self
        return getattr(instance, self.private_name, self.default_value)

    def __set__(self, instance: Any, value: float) -> None:
        if not isinstance(value, self._expected_type):
            raise TypeError(
                f"Value must be a {self._expected_type.__name__} not a {type(value).__name__}"
            )
        if value <= 0:
            raise ValueError("Number must be positive")

        setattr(instance, self.private_name, value)


@dataclass
class Product:
    name: str
    price = PositiveNumber(1.0)
    quantity = PositiveNumber(1.0)


cat = Product("cat")
cat.price = 4.0
cat.quantity = 3.0

shoe = Product("balloon")
shoe.price = -3.0

print(cat)

# need more practice on section 9 and 8
