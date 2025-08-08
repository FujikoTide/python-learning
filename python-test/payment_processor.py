from dataclasses import dataclass


@dataclass
class CreditCardPayment:
    def process_payment(self, amount: float) -> str:
        return f"Processing credit card payment for ${amount}"


@dataclass
class PayPalPayment:
    def process_payment(self, amount: float) -> str:
        return f"Processing PayPal payment for ${amount}"


@dataclass
class BankTransferPayment:
    def process_payment(self, amount: float) -> str:
        return f"Processing Bank Transfer for ${amount}"


@dataclass
class PaymentTransaction:
    method: CreditCardPayment | PayPalPayment | BankTransferPayment
    amount: float


cc_payment = CreditCardPayment()
pp_payment = PayPalPayment()
bt_payment = BankTransferPayment()

transactions = [
    PaymentTransaction(method=cc_payment, amount=500),
    PaymentTransaction(method=pp_payment, amount=300),
    PaymentTransaction(method=bt_payment, amount=400),
    PaymentTransaction(method=cc_payment, amount=200),
]


def pay(transactions: list[PaymentTransaction]):
    for transaction in transactions:
        print(transaction.method.process_payment(transaction.amount))


pay(transactions)


# this also needs practice, this is beyond me at the moment !
