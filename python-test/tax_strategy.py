from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        pass


@dataclass
class MongolianTaxStrategy(TaxStrategy):
    TAX = 5

    def calculate_tax(self, amount: float) -> float:
        return (self.TAX / 100) * amount


@dataclass
class USTaxStrategy(TaxStrategy):
    _tax: float = field(init=False)

    def __post_init__(self):
        self._tax = 5

    def calculate_tax(self, amount: float) -> float:
        return (self._tax / 100) * amount


@dataclass
class EuropeanTaxStrategy(TaxStrategy):
    _tax: float = field(init=False)

    def __post_init__(self):
        self._tax = 20

    def calculate_tax(self, amount: float) -> float:
        return (self._tax / 100) * amount


@dataclass
class Invoice:
    amount: float
    tax_strategy: TaxStrategy

    def get_total(self) -> float:
        return self.amount + self.tax_strategy.calculate_tax(self.amount)


us_tax = USTaxStrategy()
euro_tax = EuropeanTaxStrategy()
mongolian_tax = MongolianTaxStrategy()
invoice1 = Invoice(40, us_tax)
invoice2 = Invoice(30, euro_tax)

print(invoice1.get_total())
print(invoice2.get_total())
