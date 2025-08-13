from dataclasses import dataclass
from payment import Payment
from calculate_price import CalculatePrice


@dataclass
class Checkout:
    payment_process: Payment
    calculate_price: CalculatePrice

    def perform_checkout(self):
        amount = self.calculate_price.calculate_final_total()
        print(self.payment_process.pay(amount))
