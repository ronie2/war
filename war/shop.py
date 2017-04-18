from .base_shop import Shop
from .buyer import get_buyer
from .validator import get_validator
from .transaction import get_transaction
from .errors import ProductDatabaseError


class WarPlanesShop(Shop):
    """Concrete planes shop implementation"""

    def __init__(self, equipment):
        """
        Initializes shop with db. Super '__init__' method is used
        Args:
            equipment (dict): Equipment database like in example data

        """
        msg_validator = get_validator({'equipment': equipment})
        msg_validator.validate()

        super().__init__(equipment)

    def buy_plane(self, player, plane_id):
        """
        Buys plane for `player` by `plane_id`.

        Args:
            player (dict): Original example data `player` dict
            plane_id (int): Plane id

        Returns:
            None

        """
        msg_validator = get_validator({'player': player})
        msg_validator.validate()

        transaction = get_transaction({
            'buyer': get_buyer(player),
            'plane_id': plane_id,
            'price': self._product_price_by_id(plane_id)
        })

        validator = get_validator(transaction.transaction)
        validator.validate()

        transaction.commit()

    def buy_gun(self, player, plane_id, gun_id):
        """
        Buys gun for `player` by `gun_id` and installs it into
        plane by `plane_id`

        Args:
            player (dict): Original example data `player` dict
            plane_id (int): Plane id
            gun_id (int): Gun id

        Returns:
            None

        """
        msg_validator = get_validator({'player': player})
        msg_validator.validate()

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

    def _product_spec_by_id(self, product_id):

        """
        Returns product specification by id stored id DB

        Args:
            product_id (int): Product id to retrieve from DB

        Returns:
            dict: Product specification. None if product not found.

        Raises:
            ProductDatabaseError: if product not found in DB

        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID should be integer")

        for product_group in self.db:
            for db_id in self.db[product_group]:
                if product_id == db_id:
                    return self.db[product_group][product_id]

        raise ProductDatabaseError('Wrong product ID. Not found in DB')

    def _product_price_by_id(self, product_id):
        """
        Returns product price by id stored in DB

        Args:
            product_id (int): Product id to retrieve from DB

        Returns
            dict or None: Returns price dict or None if product_id not found.

        """
        product_spec = self._product_spec_by_id(product_id)
        return product_spec['price']

    def __compatible_guns(self, plane_id):
        """
        Returns compatible guns set or raises KeyError if product record
        has no `compatible_guns` key.

        Args:
            plane_id (int): Plane id

        Returns
            set: Set containing ids of compatible guns

        """
        product_spec = self._product_spec_by_id(plane_id)
        return product_spec['compatible_guns']
