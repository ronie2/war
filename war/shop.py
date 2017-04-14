from .base_shop import Shop
from .buyer import get_buyer
from .validator import get_validator
from .transaction import get_transaction

from .errors import TransactionValidationError


class WarPlanesShop(Shop):
    def __init__(self, equipment):
        super().__init__(equipment)

    def buy_plane(self, player, plane_id):
        transaction = get_transaction({
            'buyer': get_buyer(player),
            'plane_id': plane_id,
            'price': self._product_price_by_id(plane_id)
        })

        validator = get_validator(transaction.transaction)
        validator.validate()

        transaction.commit()

        self.__update_player(player, transaction.transaction)

    def buy_gun(self, player, plane_id, gun_id):
        transaction = get_transaction({
            'buyer': get_buyer(player),
            'plane_id': plane_id,
            'gun_id': gun_id,
            'comp_guns': self.__compatible_guns(plane_id),
            'price': self._product_price_by_id(gun_id)
        })

        validator = get_validator(transaction.transaction)
        validator.validate()

        transaction.commit()

        self.__update_player(player, transaction.transaction)

    def _product_spec_by_id(self, product_id):
        for product_group in self.db:
            for db_id in product_group:
                if product_id == db_id:
                    return self.db[product_group][product_id]

    def _product_price_by_id(self, product_id):
        product_spec = self._product_spec_by_id(product_id)
        return product_spec['price']

    def __compatible_guns(self, plane_id):
        product_spec = self._product_spec_by_id(plane_id)
        if 'compatible_guns' not in product_spec:
            raise KeyError('Product have no "compatible_guns" key')
        return product_spec['compatible_guns']

    def __update_player(self, player, transaction):
        player['resources'] = transaction['buyer'].account.as_dict()
        player['planes'] = transaction['buyer'].hangar.as_dict()
