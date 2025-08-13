from dataclasses import dataclass
from payment import Payment


# arbitrary payment handler
@dataclass
class CreditCardPayment(Payment):
    def pay(self, amount: float) -> str:
        return f"Paid ${amount} via credit card"
