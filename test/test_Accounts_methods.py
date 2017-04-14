import pytest
import sys
import os

from copy import deepcopy

# Adding a `war` package to the `sys.path` list for easy import
test_root_path = os.path.abspath(__file__ + "/../")
sys.path.insert(0, test_root_path)

from war.buyer import Account
from test.example_data import player


@pytest.fixture()
def fixture_object():
    init_player = deepcopy(player)
    return Account(init_player['resources'])


def test_account_attribute(fixture_object):
    init_player = deepcopy(player)
    account = fixture_object
    for resource, amount in account.account.items():
        assert init_player['resources'][resource] == account.account[resource]


def test_check_decrease_function(fixture_object):
    init_player = deepcopy(player)
    account = fixture_object

    price = {'credits': 10, 'gold': 10}

    account.decrease(price)
    for resource, amount in account.account.items():
        expected = init_player['resources'][resource] - price[resource]
        assert expected == amount


def test_has_enought_resource_function(fixture_object):
    account = fixture_object
    price = {'credits': 10, 'gold': 10}
    result = account.has_enought_resource(price)
    assert result is True


def test_as_dict_function(fixture_object):
    account = fixture_object
    template = {'credits': int, 'gold': int}
    result = account.as_dict()
    for resource, amount in result.items():
        assert isinstance(amount, template[resource])
