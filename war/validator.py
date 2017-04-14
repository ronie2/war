from .errors import (
    ProductsNotCompatible,
    ProductAlreadyBoat,
    NotEnoughtResources,
    NoSuchPlaneInHangar,

)


def get_validator(transaction):
    """
    This is factory function for creation of a `Validator` instances.
    This factory can decide what validation strategy to use.

    Args:
        transaction (dict): Transaction initialization dict

    Returns (Validator): Initialized object with strategy function

    """
    # If a "gun_id" isn't present, assume plane buy validator
    if 'gun_id' not in transaction:
        return Validator(_buy_plane,
                         transaction['buyer'],
                         transaction['plane_id'],
                         transaction['price'])

    # A "gun_id" is present, assume gun buy validator
    return Validator(_buy_gun,
                     transaction['buyer'],
                     transaction['plane_id'],
                     transaction['gun_id'],
                     transaction['comp_guns'],
                     transaction['price'])


def _buy_plane(*, buyer, plane_id, price):
    """
    Strategy to validate buy plane transaction

    Args:
        buyer (Buyer): A buyer to validate
        plane_id (int): A plane id
        price (int): A plane price

    Returns: None

    """
    if buyer.hangar.has_plane(plane_id):
        raise ProductAlreadyBoat

    if not buyer.account.has_enought_resource(price):
        raise NotEnoughtResources


def _buy_gun(*, buyer, plane_id, gun_id, comp_guns, price):
    """
    Strategy to validate buy gun transaction

    Args:
        buyer (Buyer): A buyer to validate
        plane_id (int): A plane id
        gun_id (int): A gun id
        comp_guns (set): Compatibility set
        price (int): A gun price

    Returns: None

    """
    if gun_id not in comp_guns:
        raise ProductsNotCompatible

    if not buyer.hangar.has_plane(plane_id):
        raise NoSuchPlaneInHangar

    if gun_id == buyer.hangar.current_weapon(plane_id):
        raise ProductAlreadyBoat

    if not buyer.account.has_enought_resource(price):
        raise NotEnoughtResources


class Validator:
    """This class responsible for transaction validation"""

    def __init__(self, strategy, *args, **kwargs):
        """
        Initializes validator with validation strategy function and
        function  arguments
        Args:
            strategy (function):
            *args: Positional arguments that will pass to validation strategy
            **kwargs: Key words arguments that will pass to validation strategy
        """
        self.validation_strategy = strategy
        self.args = args
        self.kwargs = kwargs

    def validate(self):
        """
        Validates transaction according to strategy function

        Returns: None

        """
        self.validation_strategy(self.args, self.kwargs)
