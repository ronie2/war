class Shop(object):
    """Shop class providing methods to manipulate player's palnes"""

    def __init__(self, equipment):
        """
        Args:
            equipment (dict): DB of the game palnes in the following format:

                'planes': {
                    <plane_id:int>: {
                        'price': {<game_currency:str>: <amount:int>, ...},
                        '__compatible_guns': {<gun_id:int>, ...}
                    },
                    ...
                },
                'guns': {
                    <gun_id:int>: {
                        'price': {<game_currency:str>: <amount:int>, ...}
                    },
                    ...
                }
        """
        self.db = equipment

    def buy_plane(self, player, plane_id):
        """Buy plane with ID `plane_id` for player `player` and update player's
        data as necessary.

        Args:
            player(dict): player's data in the following format:

                'id': <player_id:int>,
                'resources': {<game_currency:str>: <amount:int>, ...},
                'planes': {
                    <plane_id:int>: {'gun': <gun_id:int>},
                    ...
                }

            plane_id(int): Id of plane to buy

        Returns: None
        """

    def buy_gun(self, player, plane_id, gun_id):
        """Buy gun with ID `gun_id` for player `player` and update player's
        data as necessary.

        Args:
            player(dict): Player's data
            plane_id(int): Id of plane to buy gun for
            gun_id(int): Id of gun to buy

        Returns: None
        """
