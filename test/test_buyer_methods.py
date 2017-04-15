import pytest
import sys
import os

from copy import deepcopy

# Adding a `war` package to the `sys.path` list for easy import
# test_root_path = os.path.abspath(__file__ + "/../")
# sys.path.insert(0, test_root_path)


from war.buyer import Account
from war.buyer import Buyer
from war.buyer import Hangar
from war.buyer import get_buyer
from war.buyer import get_hangar
from war.buyer import get_account

from test.example_data import player, equipment


@pytest.fixture()
def account_obj():
    init_player = deepcopy(player)
    return Account(init_player['resources'])


@pytest.fixture()
def hangar_obj():
    init_player = deepcopy(player)
    return Hangar(init_player['planes'])


@pytest.fixture()
def ref_player():
    return deepcopy(player)


@pytest.fixture()
def ref_equipment():
    return deepcopy(equipment)


@pytest.fixture()
def new_plane_id(ref_equipment, ref_player):
    for plane_id in ref_equipment['planes']:
        if plane_id not in ref_player['planes']:
            return plane_id


@pytest.fixture()
def present_plane_id(ref_player):
    for plane_id, _ in ref_player['planes'].items():
        return plane_id


@pytest.fixture()
def compatible_guns(ref_equipment, present_plane_id):
    guns = ref_equipment['planes'][present_plane_id]['compatible_guns']
    return guns


def test_hangar_planes(hangar_obj, ref_player):
    """Tests that hangar is initialized with correct number of planes"""
    hangar = hangar_obj
    for plane_id, plane_spec in hangar.planes.items():
        assert ref_player['planes'][plane_id] == hangar_obj.planes[plane_id]


def test_hangar_add_plane(hangar_obj, new_plane_id):
    """Tests positive adding plane to hangar"""
    hangar_obj.add_plane(new_plane_id)
    assert new_plane_id in hangar_obj.planes


def test_hangar_has_plane_true(hangar_obj, present_plane_id):
    """Tests a True value of hangar has plane"""
    assert hangar_obj.has_plane(present_plane_id) is True


def test_hangar_has_plane_false(hangar_obj, new_plane_id):
    """Tests a False value of hangar has plane"""
    assert hangar_obj.has_plane(new_plane_id) is False


def test_hangar_current_weapon(hangar_obj, present_plane_id, ref_player):
    """Tests value returned by hangar current weapon by plane_id"""
    result = hangar_obj.current_weapon(present_plane_id)
    expected = ref_player['planes'][present_plane_id]['gun']
    assert result == expected


def test_hangar_current_weapon_no_plane(hangar_obj, new_plane_id):
    """Tests that plane not present in Hangar raises KeyError"""
    with pytest.raises(KeyError, message="Expecting KeyError"):
        hangar_obj.current_weapon(new_plane_id)


def test_hangar_current_weapon_wrong_plane_id_type(hangar_obj):
    """Tests request with wrong plane_id type"""
    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.current_weapon('some_string')


def test_hangar_set_weapon(hangar_obj, compatible_guns, present_plane_id):
    """Tests positive gun setup for plane"""
    gun_id = compatible_guns.pop()
    hangar_obj.set_weapon(present_plane_id, gun_id)
    setted_gun = hangar_obj.planes[present_plane_id]['gun']
    assert setted_gun == gun_id


def test_account_attribute(account_obj, ref_player):
    for resource, amount in account_obj.balance.items():
        expected = ref_player['resources'][resource]
        achieved = account_obj.balance[resource]
        assert expected == achieved


def test_check_decrease_function(account_obj, ref_player):
    price = {'credits': 10, 'gold': 10}
    account_obj.decrease(price)
    for resource, amount in account_obj.balance.items():
        expected = ref_player['resources'][resource] - price[resource]
        assert expected == amount


def test_has_enought_resource_function(account_obj):
    price = {'credits': 10, 'gold': 10}
    result = account_obj.has_enought_resource(price)
    assert result is True
