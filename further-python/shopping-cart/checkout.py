from dataclasses import dataclass
from _types import items
from payment import Payment


@dataclass
class Checkout:
    items: items
    payment_process: Payment
