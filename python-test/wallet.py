from dataclasses import dataclass


@dataclass
class Wallet:
    balance: float

    def __add__(self, other) -> float:
        new_balance = self.balance
        if isinstance(other, Wallet):
            new_balance += other.balance
        elif isinstance(other, float):
            new_balance += other
        else:
            raise TypeError("values can only be of type Wallet or a float")

        return Wallet(new_balance)

    def __sub__(self, other):
        new_balance = self.balance
        if isinstance(other, Wallet):
            new_balance -= other.balance
        elif isinstance(other, float):
            new_balance -= other
        else:
            raise TypeError("values can only be of type Wallet or a float")

        return Wallet(new_balance)

    def __iadd__(self, other) -> float:
        if isinstance(other, Wallet):
            self.balance += other.balance
        elif isinstance(other, float):
            self.balance += other
        else:
            raise TypeError("values can only be of type Wallet or a float")

        return self

    def __isub__(self, other):
        if isinstance(other, Wallet):
            self.balance -= other.balance
        elif isinstance(other, float):
            self.balance -= other
        else:
            raise TypeError("values can only be of type Wallet or a float")

        return self


wallet = Wallet(500)
print(wallet)
wallet = wallet + float(55)
print(wallet)
wallet = wallet - float(234)
print(wallet)
wallet = wallet + float(-534.0)
print(wallet)

wallet2 = Wallet(500)
print(wallet2)
wallet2 += wallet
print(wallet2)
wallet2 -= wallet
print(wallet2)

wallet -= "grapes"
wallet = wallet - "grapes"
wallet += True
