from copy import deepcopy
import pytest
from unittest.mock import MagicMock
from war.buyer import Buyer
from war.buyer import get_buyer
from war.buyer import get_hangar
from war.buyer import get_account

from war.validator import Validator, get_validator, _buy_gun, _buy_plane

from war.errors import TransactionValidationError, MessageValidationError

from test.example_data import (
    player,
    equipment,
    transaction_dummy,
    buy_gun_transaction,
    buy_plane_transaction
)


@pytest.fixture()
def ref_player():
    return deepcopy(player)


@pytest.fixture()
def ref_equipment():
    return deepcopy(equipment)


@pytest.fixture()
def present_plane_id(ref_player):
    for plane_id, _ in ref_player['planes'].items():
        return plane_id


@pytest.fixture()
def new_plane_id(ref_equipment, ref_player):
    for plane_id in ref_equipment['planes']:
        if plane_id not in ref_player['planes']:
            return plane_id


@pytest.fixture()
def buy_new_plane(ref_player, new_plane_id):
    ref_player['planes'][new_plane_id] = {'gun': None}


@pytest.fixture()
def compatible_guns(ref_equipment, present_plane_id):
    guns = ref_equipment['planes'][present_plane_id]['compatible_guns']
    return guns


@pytest.fixture()
def not_bought_compatible_guns(ref_player, ref_equipment, buy_new_plane):
    for plane_id, gun in ref_player['planes'].items():
        comp_guns = ref_equipment['planes'][plane_id]['compatible_guns']
        installed_guns = set([ref_player['planes'][plane_id]['gun']])

        not_bought_guns = comp_guns - installed_guns
        if not_bought_guns:
            return {'plane_id': plane_id,
                    'guns': not_bought_guns}


@pytest.fixture()
def buyer_obj(ref_player):
    deepcopy(ref_player)
    from war.buyer import Buyer
    return Buyer(deepcopy(ref_player))


@pytest.fixture()
def shop_obj(ref_equipment):
    from war.shop import WarPlanesShop
    return WarPlanesShop(ref_equipment)


@pytest.fixture()
def account_obj(ref_player):
    from war.buyer import Account
    return Account(ref_player['resources'])


@pytest.fixture()
def hangar_obj(ref_player):
    from war.buyer import Hangar
    return Hangar(ref_player['planes'])


@pytest.fixture()
def validator_obj():
    from war.validator import Validator
    mock = MagicMock()
    validator = Validator(mock, **transaction_dummy)
    return {'mock': mock, 'validator_obj': validator}


@pytest.fixture()
def validator_type():
    from war.validator import Validator
    return Validator


@pytest.fixture()
def validator_factory():
    from war.validator import get_validator
    return get_validator


@pytest.fixture()
def ref_transaction_dummy():
    return deepcopy(transaction_dummy)


@pytest.fixture()
def ref_buy_plane_tran(new_plane_id, ref_equipment):
    buy_plane_tran = deepcopy(buy_plane_transaction)
    mock = MagicMock()

    buy_plane_tran['buyer'] = mock
    buy_plane_tran['plane_id'] = new_plane_id
    buy_plane_tran['price'] = ref_equipment['planes'][new_plane_id]['price']

    return {'tran': buy_plane_tran, 'mock': mock}


@pytest.fixture()
def ref_buy_gun_tran(ref_equipment, not_bought_compatible_guns):
    buy_gun_tran = deepcopy(buy_gun_transaction)

    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(not_bought_compatible_guns['guns']))
    mock = MagicMock()

    plane_spec = ref_equipment['planes'][plane_id]

    buy_gun_tran['buyer'] = mock
    buy_gun_tran['plane_id'] = plane_id
    buy_gun_tran['gun_id'] = gun_id
    buy_gun_tran['comp_guns'] = plane_spec['compatible_guns']
    buy_gun_tran['price'] = plane_spec['price']

    return {'tran': buy_gun_tran, 'mock': mock}
