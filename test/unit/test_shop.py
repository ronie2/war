"""These module tests war.shop.py module"""
from test.unit.fixture_logic import *


def test_shop_init_values(shop_obj, ref_equipment):
    """Tests that instance values are initialized correct"""
    assert shop_obj.db == ref_equipment


def test_buy_plane_pass(shop_obj, ref_player, new_plane_id):
    shop_obj.buy_plane(ref_player, new_plane_id)

    assert new_plane_id in ref_player['planes']


def test_buy_plane_wrong_type(shop_obj, ref_player):
    with pytest.raises(MessageValidationError,
                       message="Expecting MessageValidationError"):
        shop_obj.buy_plane("some_string", "some_string")

    with pytest.raises(TypeError, message="Expecting TypeError"):
        shop_obj.buy_plane(ref_player, "some_string")

    with pytest.raises(MessageValidationError,
                       message="Expecting MessageValidationError"):
        shop_obj.buy_plane("some_string", 101)


def test_buy_plane_wrong_value(shop_obj, ref_player):
    """Tests for plane id that not in DB"""
    with pytest.raises(ProductDatabaseError,
                       message="Expecting ProductDatabaseError"):
        shop_obj.buy_plane(ref_player, 12312421)


def test_buy_gun_pass(shop_obj, ref_player, not_bought_compatible_guns):
    plane_id = not_bought_compatible_guns['plane_id']
    guns = not_bought_compatible_guns['guns']
    gun_id = next(iter(guns))

    shop_obj.buy_gun(ref_player, plane_id, gun_id)

    assert gun_id == ref_player['planes'][plane_id]['gun']


def test_buy_gun_wrong_type(shop_obj, ref_player,
                            not_bought_compatible_guns):
    plane_id = not_bought_compatible_guns['plane_id']
    guns = not_bought_compatible_guns['guns']
    gun_id = next(iter(guns))

    with pytest.raises(MessageValidationError, message="Expecting TypeError"):
        shop_obj.buy_gun("some_string", "some_string", "some_string")

    with pytest.raises(TypeError, message="Expecting TypeError"):
        shop_obj.buy_gun(ref_player, "some_string", "some_string")

    with pytest.raises(MessageValidationError,
                       message="Expecting MessageValidationError"):
        shop_obj.buy_gun("some_string", plane_id, "some_string")

    with pytest.raises(MessageValidationError,
                       message="Expecting MessageValidationError"):
        shop_obj.buy_gun("some_string", "some_string", gun_id)


def test_buy_gun_wrong_value(shop_obj, ref_player, not_bought_compatible_guns):
    """Tests for gun id that not in DB"""
    guns = not_bought_compatible_guns['guns']
    gun_id = next(iter(guns))

    with pytest.raises(ProductDatabaseError,
                       message="Expecting ProductDatabaseError"):
        shop_obj.buy_gun(ref_player, 123123154, gun_id)


def test_product_spec_by_id_pass(shop_obj, new_plane_id, ref_equipment):
    """Checks that _product_spec_by_id method returns correct data"""
    achieved_spec = shop_obj._product_spec_by_id(new_plane_id)
    expected_spec = ref_equipment['planes'][new_plane_id]

    assert achieved_spec == expected_spec


def test_product_spec_by_id_wrong_type(shop_obj):
    with pytest.raises(TypeError, message="Expecting TypeError"):
        shop_obj._product_spec_by_id('some_string')


def test_product_spec_by_id_wrong_value(shop_obj):
    """Checks that _product_spec_by_id with wrong product ID call
     raises ProductDatabaseError
    """
    with pytest.raises(ProductDatabaseError,
                       message="Expecting ProductDatabaseError"):
        shop_obj._product_spec_by_id(12312312343)


def test_product_price_by_id_pass(shop_obj, new_plane_id, ref_equipment):
    """Checks that _price_by_id method returns correct data"""
    achieved_price = shop_obj._product_price_by_id(new_plane_id)
    expected_price = ref_equipment['planes'][new_plane_id]['price']

    assert achieved_price == expected_price


def test_product_price_by_id_wrong_type(shop_obj):
    with pytest.raises(TypeError, message="Expecting TypeError"):
        shop_obj._product_price_by_id('some_string')


def test_product_price_by_id_wrong_value(shop_obj):
    """Checks that _price_by_id with wrong product ID call
     raises ProductDatabaseError
    """

    with pytest.raises(ProductDatabaseError,
                       message='Expecting ProductDatabaseError'):
        shop_obj._product_price_by_id(1323123124)


def test_compatible_guns_pass(shop_obj, new_plane_id, ref_equipment):
    """Checks that __compatible_guns method returns correct data"""
    achieved_guns = shop_obj._WarPlanesShop__compatible_guns(new_plane_id)
    expected_guns = ref_equipment['planes'][new_plane_id]['compatible_guns']

    assert achieved_guns == expected_guns


def test_compatible_guns_wrong_type(shop_obj):
    with pytest.raises(TypeError, message="Expecting TypeError"):
        shop_obj._WarPlanesShop__compatible_guns('some_string')


def test_compatible_guns_wrong_value(shop_obj):
    with pytest.raises(ProductDatabaseError,
                       message='Expecting ProductDatabaseError'):
        shop_obj._WarPlanesShop__compatible_guns(312312312)


if __name__ == '__main__':
    pytest.main()
