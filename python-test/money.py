from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                amount = self.amount + other.amount
                return Money(amount, self.currency)
            raise ValueError(
                f"Currencies must match, first currency: {self.currency}, second currency: {other.currency}"
            )
        raise TypeError(f"Can only add objects of type: {type(self)}")

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        raise TypeError(f"Can only compare objects of type: {type(self)}")


pounds = Money(30, "pounds")
dollars = Money(20, "dollars")
euros = Money(40, "euros")
pounds2 = Money(45, "pounds")

print(pounds)
print(dollars)
print(euros)
print(pounds2)

# print(pounds + dollars)
print(dollars + dollars)
# print(euros + pounds2)
print(pounds2 + pounds)


print(pounds == dollars)
print(dollars == dollars)
print(euros == pounds2)
print(pounds2 == pounds)
print(pounds == pounds)
