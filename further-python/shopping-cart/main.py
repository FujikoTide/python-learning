from decimal import Decimal
from item import Item
from cart import Cart
from credit_card_payment import CreditCardPayment
from paypal_payment import PaypalPayment
from checkout import Checkout
from calculate_price import CalculatePrice


def main():
    item1 = Item("cat1", "animal1", Decimal("3.5"))
    item2 = Item("cat2", "animal2", Decimal("4.5"))
    item3 = Item("cat3", "animal3", Decimal("6.5"))

    print(item1)
    print(item2)
    print(item3)

    item1.change_item_name("cat5")
    cart = Cart()
    cart.add_item(item1, 4)
    cart.add_item(item2, 2)
    cart.add_item(item3, 5)

    print(cart)

    credit_card_payment = CreditCardPayment()
    paypal_payment = PaypalPayment()
    calculate_price = CalculatePrice(cart)
    checkout = Checkout(credit_card_payment, calculate_price)
    checkout2 = Checkout(paypal_payment, calculate_price)

    checkout.perform_checkout()
    checkout2.perform_checkout()


if __name__ == "__main__":
    main()
