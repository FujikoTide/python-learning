from abc import ABC, abstractmethod
from item import Item
from _types import items
from dataclasses import dataclass, field


@dataclass
class Store(ABC):
    item_store: items = field(default_factory=items)

    @abstractmethod
    def add_item(self, item: Item) -> Item | None:
        pass

    @abstractmethod
    def remove_item(self, product_id: int) -> Item | None:
        pass

    @abstractmethod
    def change_item_quantity(self, product_id: int, quantity: int) -> Item | None:
        pass
