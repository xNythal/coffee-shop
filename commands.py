from typing import TYPE_CHECKING
import utils

if TYPE_CHECKING:
    from coffee_shop import CoffeeShop


def balance(shop: "CoffeeShop"):
    money = utils.style(f"${shop.balance}", fg=(0, 100, 0))
    print(utils.style(f"Your balance is {money}", "bold", fg=(200, 150, 50)))


COMMANDS = {"balance": balance, "money": balance}
