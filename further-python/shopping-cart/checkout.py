from dataclasses import dataclass
from payment import Payment
from cart import Cart
from config import TAX_RATE_PERCENTAGE, CURRENT_DISCOUNT
from calculate_price import CalculatePrice


@dataclass
class Checkout:
    cart: Cart
    payment_process: Payment
    calculate_price = CalculatePrice
