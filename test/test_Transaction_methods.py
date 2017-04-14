import pytest
import sys
import os

from class_constructor import constructor

# Adding a `war` package to the `sys.path` list for easy import
test_root_path = os.path.abspath(__file__ + "/../")
sys.path.insert(0, test_root_path)

import war

from war.buyer import Account
from war.buyer import Hangar
from war.transaction import Transaction


def test_transaction_attribute(constructor):
    pass


def test_commit_function(constructor):
    pass


def test_transaction_strategy_function(constructor):
    pass
