def _buy_plane(owner):
    owner.transaction['buyer'].account.decrease(owner.transaction['price'])
    owner.transaction['buyer'].hangar.add_plane(owner.transaction['plane_id'])


def _buy_gun(owner):
    owner.transaction['buyer'].account.decrease(owner.transaction['price'])
    owner.transaction['buyer'].hangar.set_weapon(owner.transaction['plane_id'],
                                                 owner.transaction['gun_id'])


# Global logic controller
def get_transaction(transaction):
    # If a "gun_id" isn't present, assume plane buy
    if 'gun_id' not in transaction:
        return Transaction(_buy_plane, transaction)

    # A "gun_id" is present, assume gun buy validator
    return Transaction(_buy_gun, transaction)


class Transaction:
    def __init__(self, strategy, transaction):
        self._transaction_strategy = strategy
        self.transaction = transaction

    def commit(self):
        self._transaction_strategy()
