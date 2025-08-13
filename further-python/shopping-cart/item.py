from dataclasses import dataclass
from typing import Self
from uuid import uuid4


@dataclass
class Item:
    name: str
    description: str
    price: float
    _id: str = ""

    def __post_init__(self):
        # store uuid as string for human reading, ideally use UUID object in actual databases etc
        self._id = str(uuid4())

    def change_item_name(self, name: str) -> Self | None:
        pass

    def change_item_description(self, description: str) -> Self | None:
        pass

    def change_item_price(self, price: float) -> Self | None:
        pass
