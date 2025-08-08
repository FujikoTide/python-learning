from dataclasses import dataclass, field


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
            raise ValueError(f"Insufficient funds, current balance: {self._balance}")
        self._balance -= amount

    @property
    def balance(self) -> float:
        return self._balance


ac = BankAccount(200)
print(ac.balance)
print(ac.deposit(30.5))
print(ac.withdraw(127.3))
print(ac.balance)
ac.balance = 300000000
print(ac.balance)
