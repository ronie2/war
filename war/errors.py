class ShopErrors(Exception):
    pass


class TransactionValidationError(ShopErrors):
    pass

class MessageValidationError(ShopErrors):
    pass


class ProductsNotCompatible(TransactionValidationError):
    pass


class ProductAlreadyBoat(TransactionValidationError):
    pass


class NotEnoughtResources(TransactionValidationError):
    pass


class NoSuchPlaneInHangar(TransactionValidationError):
    pass
