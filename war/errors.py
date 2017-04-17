class ShopError(Exception):
    pass


class TransactionError(ShopError):
    pass


class TransactionValidationError(TransactionError):
    pass


class MessageValidationError(TransactionError):
    pass


class ProductDatabaseError(ShopError):
    pass
