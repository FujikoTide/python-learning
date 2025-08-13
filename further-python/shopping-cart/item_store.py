from abc import ABC, abstractmethod
from item import Item
from _types import items, quantities
from dataclasses import dataclass, field


@dataclass
class Store(ABC):
    items: "items" = field(default_factory=dict)
    quantities: "quantities" = field(default_factory=dict)

    @abstractmethod
    def add_item(self, item: Item) -> Item | None:
        pass

    @abstractmethod
    def remove_item(self, item: Item) -> Item | None:
        pass

    @abstractmethod
    def change_item_quantity(self, item: Item, quantity: int) -> Item | None:
        pass
