from dataclasses import dataclass, field


class InsufficientFundsError(Exception):
    def __init__(self, amount_to_withdraw, current_balance):
        self.amount_to_withdraw = amount_to_withdraw
        self.current_balance = current_balance


@dataclass
class BankAccount:
    _balance: float = field(init=False)
    initial_balance: float = 0.0

    def __post_init__(self):
        if self.initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = self.initial_balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._balance - amount < 0:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount


account = BankAccount(200)
try:
    account.withdraw(500)
except InsufficientFundsError as e:
    print("You have tried to withdraw more than is in your account")
    print(
        f"You have {e.current_balance} currencies and you tried to withdraw {e.amount_to_withdraw} currencies"
    )
