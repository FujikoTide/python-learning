from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass
