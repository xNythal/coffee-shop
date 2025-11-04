class CoffeeShopError(Exception):
    """Base class for coffee shop errors."""

    def __init__(self, message=None):
        if message is None:
            message = "Something went wrong in the coffee shop."
        super().__init__(message)


class UnknownCommandError(CoffeeShopError):
    def __init__(self, message=None):
        if message is None:
            message = "Unknown command."
        super().__init__(message)
