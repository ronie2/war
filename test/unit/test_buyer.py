from test.unit.fixture_logic import *


def test_hangar_init_values(hangar_obj, ref_player):
    """Tests that hangar instance values are initialized correct"""
    hangar = hangar_obj
    for plane_id, plane_spec in hangar.planes.items():
        assert ref_player['planes'][plane_id] == hangar_obj.planes[plane_id]


def test_hangar_add_plane(hangar_obj, new_plane_id):
    """Tests positive adding plane to hangar"""
    hangar_obj.add_plane(new_plane_id)

    assert new_plane_id in hangar_obj.planes


def test_hangar_add_plane_wrong_type(hangar_obj):
    """Tests positive adding plane to hangar"""
    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.add_plane('some_string')


def test_hangar_add_plane_wrong_value(hangar_obj, present_plane_id):
    """Tests positive adding plane to hangar"""
    with pytest.raises(KeyError, message="Expecting TypeError"):
        hangar_obj.add_plane(present_plane_id)


def test_hangar_has_plane_pass(hangar_obj, present_plane_id):
    """Tests a True value of hangar has plane"""

    assert hangar_obj.has_plane(present_plane_id) is True


def test_hangar_has_plane_wrong_type(hangar_obj):
    """Tests a False value of hangar has plane"""
    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.has_plane('some_string')


def test_hangar_has_plane_wrong_value(hangar_obj, new_plane_id):
    """Tests a False value of hangar has plane"""

    assert hangar_obj.has_plane(new_plane_id) is False


def test_hangar_current_weapon_pass(hangar_obj, present_plane_id,
                                    ref_player):
    """Tests value returned by hangar current weapon by plane_id"""
    result = hangar_obj.current_weapon(present_plane_id)
    expected = ref_player['planes'][present_plane_id]['gun']

    assert result == expected


def test_hangar_current_weapon_wrong_type(hangar_obj):
    """Tests exception by hangar current weapon by plane_id with wrong type"""
    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.current_weapon('some_string')


def test_hangar_current_weapon_wrong_value(hangar_obj, new_plane_id):
    """Tests that plane not present in Hangar raises KeyError"""
    with pytest.raises(KeyError, message="Expecting KeyError"):
        hangar_obj.current_weapon(new_plane_id)


def test_hangar_set_weapon_pass(hangar_obj, not_bought_compatible_guns):
    """Tests positive gun setup for plane"""
    guns = not_bought_compatible_guns['guns']
    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(guns))

    hangar_obj.set_weapon(plane_id, gun_id)
    setted_gun = hangar_obj.planes[plane_id]['gun']

    assert setted_gun == gun_id


def test_hangar_set_weapon_wrong_type(hangar_obj,
                                      not_bought_compatible_guns):
    """Tests positive gun setup for plane"""
    guns = not_bought_compatible_guns['guns']
    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(guns))

    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.set_weapon("plane_id_string", 'gun_id_string')

    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.set_weapon(plane_id, 'gun_id_string')

    with pytest.raises(TypeError, message="Expecting TypeError"):
        hangar_obj.set_weapon('plane_id_string', gun_id)


def test_hangar_set_weapon_wrong_value(hangar_obj,
                                       not_bought_compatible_guns):
    """Tests positive gun setup for plane"""
    guns = not_bought_compatible_guns['guns']
    gun_id = next(iter(guns))

    with pytest.raises(KeyError, message="Expecting KeyError"):
        hangar_obj.set_weapon(12312312, gun_id)


def test_account_init_values(account_obj, ref_player):
    """Tests that players account instance values are initialized correct"""
    for resource, amount in account_obj.balance.items():
        expected = ref_player['resources'][resource]
        achieved = account_obj.balance[resource]
        assert expected == achieved


def test_check_decrease_function(account_obj):
    initial_player = deepcopy(player)
    price = {'credits': 10, 'gold': 10}
    account_obj.decrease(price)
    for resource, amount in account_obj.balance.items():
        expected = initial_player['resources'][resource] - price[resource]
        assert expected == amount


def test_has_enought_resource_function(account_obj):
    """Checks that player from example_data.py has enough resource"""
    price = {'credits': 10, 'gold': 10}

    result = account_obj.has_enought_resource(price)

    assert result is True


if __name__ == 'main':
    pytest.main()
