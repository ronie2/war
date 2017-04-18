"""This module presents domain specific exceptions"""


class ShopError(Exception):
    """This error is common ancestor for all domain specific exceptions.
    It is not raised in code and only used for type checking (if needed).
    """
    pass


class TransactionError(ShopError):
    """This error is common ancestor for all transaction specific exceptions.
    It is not raised in code and only used for type checking (if needed).
    """
    pass


class TransactionValidationError(TransactionError):
    """This error is specific for validating transaction (business logic).
    It is used by validator.py module.
    """
    pass


class MessageValidationError(TransactionError):
    """This error is specific for validating messages (correct format).
    It is used by validator.py module.
    """
    pass


class ProductDatabaseError(ShopError):
    """
    This error indicates some problems with shop database (ID not found etc.)
    It is used by shop.py module.
    """
    pass
