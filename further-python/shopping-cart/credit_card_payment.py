from dataclasses import dataclass
from decimal import Decimal
from payment import Payment


# arbitrary payment handler
@dataclass
class CreditCardPayment(Payment):
    def pay(self, amount: Decimal) -> str:
        return f"Paid ${amount} via credit card"
