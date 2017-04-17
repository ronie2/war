from test.fixtures import *


def test_01_001_valid_buy_plane(ref_player, new_plane_id, shop_type,
                                ref_equipment):
    shop = shop_type(ref_equipment)
    shop.buy_plane(ref_player, new_plane_id)


def test_01_001_valid_buy_plane_hangar_change(ref_player, new_plane_id,
                                              shop_type, ref_equipment):
    shop = shop_type(ref_equipment)
    shop.buy_plane(ref_player, new_plane_id)
    assert new_plane_id in ref_player['planes']


def test_01_001_valid_buy_plane_no_gun(ref_player, new_plane_id,
                                       shop_type, ref_equipment):
    shop = shop_type(ref_equipment)
    shop.buy_plane(ref_player, new_plane_id)
    assert ref_player['planes'][new_plane_id]['gun'] is None


def test_01_001_valid_buy_plane_money_withdrawn(ref_player, new_plane_id,
                                                shop_type, ref_equipment):
    init_player = deepcopy(ref_player)
    shop = shop_type(ref_equipment)
    price = ref_equipment['planes'][new_plane_id]['price']
    for resource, amount in price.items():
        init_player['resources'][resource] -= price[resource]

    shop.buy_plane(ref_player, new_plane_id)

    assert ref_player['resources'] == init_player['resources']


def test_01_001_valid_buy_gun_money_withdrawn(ref_player,
                                              not_bought_compatible_guns,
                                              shop_type, ref_equipment):
    init_player = deepcopy(ref_player)
    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(not_bought_compatible_guns['guns']))
    price = ref_equipment['guns'][gun_id]['price']
    for resource, amount in price.items():
        init_player['resources'][resource] -= price[resource]

    shop = shop_type(ref_equipment)
    shop.buy_gun(ref_player, plane_id, gun_id)

    assert ref_player['resources'] == init_player['resources']


def test_01_002_valid_buy_gun(ref_player, not_bought_compatible_guns,
                              shop_type, ref_equipment):
    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(not_bought_compatible_guns['guns']))
    shop = shop_type(ref_equipment)

    shop.buy_gun(ref_player, plane_id, gun_id)


def test_01_002_valid_buy_gun_plane_change(ref_player,
                                           not_bought_compatible_guns,
                                           shop_type, ref_equipment):
    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(not_bought_compatible_guns['guns']))
    shop = shop_type(ref_equipment)

    shop.buy_gun(ref_player, plane_id, gun_id)

    assert gun_id == ref_player['planes'][plane_id]['gun']


def test_01_003_little_money_plane(ref_poor_player, new_plane_id, shop_type,
                                   ref_equipment):
    shop = shop_type(ref_equipment)
    with pytest.raises(TransactionValidationError):
        shop.buy_plane(ref_poor_player, new_plane_id)


def test_01_004_little_money_gun(ref_poor_player, not_bought_compatible_guns,
                                 shop_type, ref_equipment):
    plane_id = not_bought_compatible_guns['plane_id']
    gun_id = next(iter(not_bought_compatible_guns['guns']))
    shop = shop_type(ref_equipment)
    with pytest.raises(TransactionValidationError):
        shop.buy_gun(ref_poor_player, plane_id, gun_id)


def test_01_004_same_plane(ref_player, present_plane_id,
                           shop_type, ref_equipment):
    shop = shop_type(ref_equipment)
    with pytest.raises(TransactionValidationError):
        shop.buy_plane(ref_player, present_plane_id)


def test_01_005_same_gun(ref_player, present_plane_id,
                         shop_type, ref_equipment, present_gun_id):
    shop = shop_type(ref_equipment)

    with pytest.raises(TransactionValidationError):
        shop.buy_gun(ref_player, present_plane_id, present_gun_id)


def test_01_006_incompatible_gun(ref_player, incompatible_gun,
                                 present_plane_id, shop_type, ref_equipment):
    shop = shop_type(ref_equipment)

    with pytest.raises(ProductDatabaseError):
        shop.buy_gun(ref_player, present_plane_id, incompatible_gun)
