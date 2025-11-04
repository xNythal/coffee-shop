from coffee_shop import CoffeeShop

shop = CoffeeShop()


def process_error(error: Exception):
    print(error)


while True:
    try:
        shop.process_command(input("> ").strip())
    except Exception as error:
        process_error(error)
