from dataclasses import dataclass


@dataclass
class Item:
    name: str
    description: str
    price: float
    _id: int
