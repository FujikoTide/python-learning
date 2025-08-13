from dataclasses import dataclass
import config


@dataclass
class CalculatePrice:
    _items: items
    discount_percentage: int = config.CURRENT_DISCOUNT
    tax: float = config.TAX_RATE_PERCENTAGE
    _gift_card: int = 0
    _tax: float = 20
    # may need some rethinking, but for now this is fine
    _base_total: float = 0
    _current_total: float = 0

    # needs to be own class, for calculation, also solves composition problem for discounts/taxes
    def calculate_final_total(self) -> float:
        self._base_total = self._calculate_cart_total()
        if self._percentage_discount:
            total = self._apply_percentage_discount()

    def _calculate_cart_total(self) -> float:
        return sum(
            item.price * quantity for item, quantity in self.shopping_cart.items()
        )

    def _add_gift_card(self, gift_card_amount: int) -> None:
        self._gift_card = gift_card_amount

    def _apply_percentage_discount(self) -> float:
        return total * (1 - (discount / 100))

    def _apply_gift_card(self) -> float:
        return total - card_value

    def _apply_tax(self) -> float:
        return total * (1 + (tax_percentage / 100))
