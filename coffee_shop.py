import errors
from commands import COMMANDS


class CoffeeShop:
    def __init__(self):
        self.balance = 0

    def make_coffee(self):
        self.balance += 10

    def process_command(self, command_str: str):
        parts = command_str.split()
        if not parts:
            return
        command = parts[0]
        args = parts[1:]
        try:
            COMMANDS[command](self, *args)
        except KeyError:
            raise errors.UnknownCommandError
