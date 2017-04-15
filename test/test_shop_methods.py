import pytest
import sys
import os

from copy import deepcopy

# Adding a `war` package to the `sys.path` list for easy import
test_root_path = os.path.abspath(__file__ + "/../")
sys.path.insert(0, test_root_path)

from war.shop import WarPlanesShop
from test.example_data import player, equipment

# from war.shop import get_buyer
from war.shop import Shop
# from war.shop import get_transaction
# from war.shop import TransactionValidationError
# from war.shop import get_validator
from war.shop import WarPlanesShop


@pytest.fixture()
def fixture_object():
    return WarPlanesShop(equipment)


def test_db_attribute(fixture_object):
    shop = fixture_object
    assert shop.db == equipment


def test_buy_plane_function(fixture_object):
    plane_id = 1002
    shop = fixture_object

    shop.buy_plane(player, plane_id)

    assert plane_id in player['planes']