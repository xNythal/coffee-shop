from typing import TYPE_CHECKING
import utils

if TYPE_CHECKING:
    from coffee_shop import CoffeeShop


def balance(shop: "CoffeeShop"):
    print(f"Your balance is ${shop.balance}")


def make_coffee(shop: "CoffeeShop"):
    shop.make_coffee()
    print(f"Made one coffee for $10. Your balance is now ${shop.balance}")


def quit(shop):
    print("See you soon!")
    exit()


COMMANDS = {
    "balance": balance,
    "money": balance,
    "quit": quit,
    "make-coffee": make_coffee,
}
