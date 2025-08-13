from dataclasses import dataclass, field
from decimal import Decimal
from config import TAX_RATE_PERCENTAGE, CURRENT_DISCOUNT
from cart import Cart
from uuid import UUID
from item import Item


@dataclass
class CalculatePrice:
    _cart: Cart
    _discount_percentage: Decimal = CURRENT_DISCOUNT
    _tax_rate_percentage: Decimal = TAX_RATE_PERCENTAGE
    _gift_card_value: Decimal = Decimal("0")
    _base_total: Decimal = field(init=False)
    _current_total: Decimal = field(init=False)

    def calculate_final_total(self) -> Decimal:
        self._base_total = self._calculate_cart_total()
        if self._discount_percentage:
            self._current_total = self._apply_percentage_discount()
        if self._gift_card_value:
            self._current_total = self._apply_gift_card()
        self._current_total = self._apply_tax()
        return self._current_total

    def _calculate_cart_total(self) -> Decimal:
        items_and_quantities: dict[UUID, tuple[Item, int]] = {
            key: (self._cart.items[key], self._cart.quantities[key])
            for key in self._cart.items
        }
        return Decimal(
            sum(
                item.price * quantity
                for item, quantity in items_and_quantities.values()
            )
        )

    def _add_gift_card(self, gift_card_amount: Decimal) -> None:
        self._gift_card_value = gift_card_amount

    def _apply_percentage_discount(self) -> Decimal:
        return self._base_total * (1 - (self._discount_percentage / 100))

    def _apply_gift_card(self) -> Decimal:
        return self._current_total - self._gift_card_value

    def _apply_tax(self) -> Decimal:
        return self._current_total * (1 + (self._tax_rate_percentage / 100))
