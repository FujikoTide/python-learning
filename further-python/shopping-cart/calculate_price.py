from dataclasses import dataclass
from decimal import Decimal
from config import TAX_RATE_PERCENTAGE, CURRENT_DISCOUNT
from _types import items, quantities


@dataclass
class CalculatePrice:
    _items: items
    discount_percentage: Decimal = CURRENT_DISCOUNT
    tax: Decimal = TAX_RATE_PERCENTAGE
    _gift_card: Decimal = Decimal("0")
    _tax: Decimal = Decimal("20")
    # may need some rethinking, but for now this is fine
    _base_total: Decimal = Decimal("0")
    _current_total: Decimal = Decimal("0")

    # needs to be own class, for calculation, also solves composition problem for discounts/taxes
    def calculate_final_total(self) -> Decimal:
        self._base_total = self._calculate_cart_total()
        if self._percentage_discount:
            total = self._apply_percentage_discount()

    def _calculate_cart_total(self) -> Decimal:
        return sum(
            item.price * quantity for item, quantity in self.shopping_cart.items()
        )

    def _add_gift_card(self, gift_card_amount: Decimal) -> None:
        self._gift_card = gift_card_amount

    def _apply_percentage_discount(self) -> Decimal:
        return total * (1 - (discount / 100))

    def _apply_gift_card(self) -> Decimal:
        return total - card_value

    def _apply_tax(self) -> Decimal:
        return total * (1 + (tax_percentage / 100))
