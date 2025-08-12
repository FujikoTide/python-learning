from abc import ABC, abstractmethod
from _types import items
from item import Item
from dataclasses import dataclass


@dataclass
class Store(ABC):
    store: items

    @abstractmethod
    def add_item(self, item: Item) -> Item | None:
        pass

    @abstractmethod
    def remove_item(self, product_id: int) -> Item | None:
        pass

    @abstractmethod
    def change_item_quantity(self, product_id: int, quantity: int) -> Item | None:
        pass
