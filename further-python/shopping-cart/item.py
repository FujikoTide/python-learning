from dataclasses import dataclass
from decimal import Decimal
from typing import Self
from uuid import uuid4
from decorators import feature_flag
from config import FeatureFlags


@dataclass
class Item:
    name: str
    description: str
    price: Decimal
    _id: str = ""

    def __post_init__(self):
        if not isinstance(self.price, Decimal):
            self.price = Decimal(self.price)
        # store uuid as string for human reading, ideally use UUID object in actual databases etc
        self._id = str(uuid4())

    @feature_flag(FeatureFlags.PRINT_OUTPUT)
    def change_item_name(self, name: str) -> Self | None:
        self.name = name
        return self

    @feature_flag(FeatureFlags.PRINT_OUTPUT)
    def change_item_description(self, description: str) -> Self | None:
        self.description = description
        return self

    @feature_flag(FeatureFlags.PRINT_OUTPUT)
    def change_item_price(self, price: Decimal) -> Self | None:
        self.price = price
        return self
