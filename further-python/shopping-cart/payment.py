from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: Decimal) -> str:
        pass
