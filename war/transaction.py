def _buy_plane(owner):
    """
    This is transaction strategy function for plane buy. It implements concrete
    steps to commit transaction.

    Args:
        owner (Transaction): Transaction instance that will use strategy

    Returns: None

    """
    owner.transaction['buyer'].account.decrease(owner.transaction['price'])
    owner.transaction['buyer'].hangar.add_plane(owner.transaction['plane_id'])


def _buy_gun(owner):
    """
    This is transaction strategy function for gun buy. It implements concrete
    steps to commit transaction.

    Args:
        owner (Transaction): Transaction instance that will use strategy

    Returns: None
    """
    owner.transaction['buyer'].account.decrease(owner.transaction['price'])
    owner.transaction['buyer'].hangar.set_weapon(owner.transaction['plane_id'],
                                                 owner.transaction['gun_id'])


def get_transaction(transaction):
    """
    This is factory function for creation of a `Transaction` instances

    Args:
        transaction (dict): Dictionary with transaction details

    Returns (Transaction): `Transaction` instance initialized with appropriate
    transaction data dict and transaction strategy.

    """
    # If a "gun_id" isn't present, assume plane buy
    if 'gun_id' not in transaction:
        return Transaction(_buy_plane, transaction)

    # A "gun_id" is present, assume gun buy validator
    return Transaction(_buy_gun, transaction)


class Transaction:
    """This class is responsible for changing buyers balance and hangar"""

    def __init__(self, strategy, transaction):
        """
        Initializes Transaction with transaction strategy function and
        transaction specific details.

        Args:
            strategy (function): Concrete function to implement transaction
            transaction (dict): Dictionary with transaction specific details
        """
        self._transaction_strategy = strategy
        self.transaction = transaction

    def commit(self):
        """
        Executes transaction strategy function

        Returns: None

        """
        self._transaction_strategy(self)
