from .buyer import Buyer
from .errors import (
    TransactionValidationError,
    MessageValidationError

)


def get_validator(transaction):
    """
    This is factory function for creation of a `Validator` instances.
    This factory can decide what validation strategy to use.

    Args:
        transaction (dict): Transaction initialization dict

    Returns (Validator): Initialized object with strategy function

    """
    BUY_PLANE_TRANS = {'buyer', 'plane_id', 'price'}
    BUY_GUN_TRANS = {'buyer', 'plane_id', 'gun_id', 'comp_guns', 'price'}
    PLAYER_MSG = {'player'}
    EQUIPMENT_MESSAGE = {'equipment'}

    if transaction.keys() == BUY_PLANE_TRANS:
        return Validator(_buy_plane, **transaction)

    if transaction.keys() == BUY_GUN_TRANS:
        return Validator(_buy_gun, **transaction)

    if transaction.keys() == PLAYER_MSG:
        return Validator(_player_msg, **transaction)

    if transaction.keys() == EQUIPMENT_MESSAGE:
        return Validator(_equipment_msg, **transaction)

    raise TransactionValidationError('Transaction is not recognized')


def _validate_by_template(msg_template, msg):
    """
    Simple type validator. Will say if msg_template, msg are 'very' different.
    No deep comparision is implemented.

    Args:
        msg_template(dict): Dict with message template
        msg(dict): Message to validate

    Returns: None

    Raises: TypeError if message and template mismatch
    """
    template_type = type(msg_template)

    if not isinstance(msg_template, dict):
        raise TypeError('Tho only templates type allowed is dict!')

    if not isinstance(msg, template_type):
        raise TypeError('Types mismatch! {} and {}'.format(template_type, msg))

    for key, value in msg_template.items():
        if isinstance(msg_template[key], type):
            if not isinstance(msg[key], msg_template[key]):
                raise TypeError


def _equipment_msg(*, equipment):
    """
    Strategy to validate equipment message.

    Args:
        equipment: equipment message in 'Shop DB' format

    Returns: None
    Raises: MessageValidationError if message is not valid

    """
    msg_template = {
        'planes': {
            int: {
                'price': {'credits': int},
                'compatible_guns': {int}
            }
        },
        'guns': {
            int: {
                'price': {'credits': int},
            }
        }
    }
    try:
        _validate_by_template(msg_template, equipment)
    except TypeError:
        raise MessageValidationError('Equipment message is wrong')


def _player_msg(*, player):
    """
    Strategy to validate player message.

    Args:
        player: equipment message in 'Shop DB' format

    Returns: None
    Raises: MessageValidationError if message is not valid

    """
    msg_template = {
        'id': int,
        'resources': {
            'credits': int,
            'gold': int
        },
        'planes': {
            int: {'gun': int}
        },
    }
    try:
        _validate_by_template(msg_template, player)
    except TypeError:
        raise MessageValidationError('Player message is wrong')


def _buy_plane(*, buyer, plane_id, price):
    """
    Strategy to validate buy plane transaction

    Args:
        buyer (Buyer): A buyer to validate
        plane_id (int): A plane id
        price (dict): A plane price

    Returns: None

    """
    if not all([isinstance(buyer, Buyer),
                isinstance(plane_id, int),
                isinstance(price, dict)]):
        raise TypeError('Parameters types wrong')

    if buyer.hangar.has_plane(plane_id):
        raise TransactionValidationError('Product already bought')

    if not buyer.account.has_enought_resource(price):
        raise TransactionValidationError('Buyer has not enough resource')


def _buy_gun(*, buyer, plane_id, gun_id, comp_guns, price):
    """
    Strategy to validate buy gun transaction

    Args:
        buyer (Buyer): A buyer to validate
        plane_id (int): A plane id
        gun_id (int): A gun id
        comp_guns (set): Compatibility set
        price (dict): A gun price

    Returns:
        None

    """
    if not all([isinstance(buyer, Buyer),
                isinstance(plane_id, int),
                isinstance(gun_id, int),
                isinstance(comp_guns, set),
                isinstance(price, dict)]):
        raise TypeError('Parameters types wrong')

    if gun_id not in comp_guns:
        raise TransactionValidationError('Products are not compatible')

    if not buyer.hangar.has_plane(plane_id):
        raise TransactionValidationError('No such plane in hangar')

    if gun_id == buyer.hangar.current_weapon(plane_id):
        raise TransactionValidationError('Product already bought')

    if not buyer.account.has_enought_resource(price):
        raise TransactionValidationError('Buyer has not enough resource')


class Validator:
    """This class responsible for transaction validation"""

    def __init__(self, strategy, *args, **kwargs):
        """
        Initializes validator with validation strategy function and
        function  arguments.

        Args:
            strategy (function):
            args: Positional arguments that will pass to validation strategy
            kwargs: Key words arguments that will pass to validation strategy

        """
        if not callable(strategy):
            raise TypeError('Validation strategy should be callable')

        self.validation_strategy = strategy
        self.args = args
        self.kwargs = kwargs

    def validate(self):
        """
        Validates transaction according to strategy function

        Returns:
             None

        """
        self.validation_strategy(*self.args, **self.kwargs)
