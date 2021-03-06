"""This module implements buyer abstraction. Buyer type aggregates
Hangar and Account types.
"""


def get_hangar(player):
    """
    This is factory function for creation of a `Hangar` instances

    Args:
        player (dict): Original example data `player` dict

    Returns
        Hangar: `Hangar` instance initialized with player['planes'] data

    """
    return Hangar(player['planes'])


def get_buyer(player):
    """
    This is factory function for creation of a `Buyer` instances

    Args:
        player (dict): Original example data `player` dict

    Returns
        Buyer: `Buyer` instance initialized with player data

    """
    return Buyer(player)


def get_account(player):
    """
    This is factory function for creation of a `Buyer` instances

    Args:
        player (dict): Original example data `player` dict

    Returns
        Account: `Account` instance initialized with player['resources']

    """
    return Account(player['resources'])


class Account:
    """This class is responsible for buyers balance"""

    def __init__(self, balance):
        """
        Initializes players balance

        Args:
            balance (dict): Players balance data as in player['resources']
        """
        self.balance = balance

    def decrease(self, price):
        """
        Decreases balance for specified price

        Args:
            price (dict): product price dict

        Returns:
            None

        """
        for resource_type in price:
            if resource_type not in self.balance:
                raise KeyError('Do not have required resource')
            self.balance[resource_type] -= price[resource_type]

    def has_enought_resource(self, price):
        """
        Checks if balance has enough money

        Args:
            price (dict): product price dict

        Returns
            bool: If balance has enough money

        """
        for resource in price:
            if resource not in self.balance:
                return False
            if self.balance[resource] < price[resource]:
                return False
        return True


class Hangar:
    """A class providing methods for manipulate buyers planes"""

    def __init__(self, palanes):
        """
        Initialize hangar with planes
        Args:
            palanes (dict): Buyers hangar content

        """
        self.planes = palanes

    def __contains__(self, plane_id):
        """
        Returns if plane_id is in hangar

        Args:
            plane_id (int): Id of a plane to check

        Returns
            bool: If buyer hangar contains plane

        """
        if not isinstance(plane_id, int):
            raise TypeError
        return plane_id in self.planes

    def __getitem__(self, plane_id):
        """
        Returns a plane record by plane_id

        Args:
            plane_id (int): Id of a plane to check

        Returns
            dict: Plane content

        """
        if not isinstance(plane_id, int):
            raise TypeError
        if plane_id not in self.planes:
            raise KeyError
        return self.planes[plane_id]

    def __setitem__(self, plane_id, plane_spec):
        """
        Adds a plane into hangar by `plane_id` and `plane_spec` on low level

        Args:
            plane_id (int): A plane id
            plane_spec (dict): A plane content

        Returns:
             None

        """
        if not isinstance(plane_id, int):
            raise TypeError('ID should be of type int')

        if not isinstance(plane_spec, dict):
            raise TypeError('Plane spec should be of type int')

        self.planes[plane_id] = plane_spec

    def add_plane(self, plane_id):
        """
        High level method to add a plane into the hangar by id

        Args:
            plane_id (int): A plane id

        Returns:
            None

        """
        if plane_id in self:
            raise KeyError('Plane already in hangar')

        self[plane_id] = {'gun': None}

    def has_plane(self, plane_id):
        """
        Checks if a hangar contains plane

        Args:
            plane_id (int): A plane ID

        Returns
            bool: True is a plane is in the hangar else returns False

        """
        return plane_id in self

    def current_weapon(self, plane_id):
        """
        Returns current plans gun

        Args:
            plane_id (int): A plane ID

        Returns
            int: Gun ID

        """
        return self[plane_id]['gun']

    def set_weapon(self, plane_id, gun_id):
        """
        Sets new weapon on the plane

        Args:
            plane_id (int): A plane ID
            gun_id (int): A gun ID

        Returns:
            None

        """
        if not isinstance(gun_id, int):
            raise TypeError('A gun id should be integer')
        self[plane_id]['gun'] = gun_id


class Buyer:
    """This class represents plane buyer."""

    def __init__(self, player):
        """
        Initialize buyer instance. No methods here. Functionality if
        aggregated from other objects.

        Args:
            player (dict): Original example data `player` dict

        """
        if not isinstance(player, dict):
            raise TypeError('Player object should be of type dict')
        self.id = player['id']
        self.account = get_account(player)
        self.hangar = get_hangar(player)
