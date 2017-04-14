from .errors import (
    ProductsNotCompatible,
    ProductAlreadyBoat,
    NotEnoughtResources,
    NoSuchPlaneInHangar,

)


def _buy_plane(*, buyer, plane_id, price):
    if buyer.hangar.has_plane(plane_id):
        raise ProductAlreadyBoat

    if not buyer.account.has_enought_resource(price):
        raise NotEnoughtResources


def _buy_gun(*, buyer, plane_id, gun_id, comp_guns, price):
    if gun_id not in comp_guns:
        raise ProductsNotCompatible

    if not buyer.hangar.has_plane(plane_id):
        raise NoSuchPlaneInHangar

    if gun_id == buyer.hangar.current_weapon(plane_id):
        raise ProductAlreadyBoat

    if not buyer.account.has_enought_resource(price):
        raise NotEnoughtResources


def get_validator(transaction):
    # If a "gun_id" isn't present, assume plane buy validator
    if 'gun_id' in transaction:
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


class Validator:
    def __init__(self, strategy, *args, **kwargs):
        self.validation_strategy = strategy
        self.args = args
        self.kwargs = kwargs

    def validate(self):
        self.validation_strategy(self.args, self.kwargs)
