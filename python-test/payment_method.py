from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def get_currency(self):
        pass


@dataclass
class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing {amount} {self.get_currency()} via Credit Card"

    def get_currency(self):
        return "USD"


@dataclass
class PayPal(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing {amount} {self.get_currency()} via Paypal"

    def get_currency(self):
        return "EUR"


@dataclass
class BitCoin(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing {amount} {self.get_currency()} via Bitcoin stuff"

    def get_currency(self):
        return "BTC"


cc_payment = CreditCard()
pp_payment = PayPal()
bc_payment = BitCoin()


@dataclass
class PaymentTypes:
    method: CreditCard | PayPal | BitCoin
    amount: float


payments = [
    PaymentTypes(method=cc_payment, amount=400),
    PaymentTypes(method=pp_payment, amount=600),
    PaymentTypes(method=bc_payment, amount=300),
]


def display_payments(payments):
    for payment in payments:
        print(payment.method.process_payment(payment.amount))


display_payments(payments)
