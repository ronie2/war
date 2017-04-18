"""These module tests war.transaction.py module"""
from test.unit.fixture_logic import *


def test_tran_init_values(tran_obj, ref_transaction_dummy):
    """Tests that instance values are initialized correct"""
    strategy = tran_obj['tran_obj']._transaction_strategy
    trans_attr = tran_obj['tran_obj'].transaction
    mock = tran_obj['mock']

    assert trans_attr == ref_transaction_dummy
    assert strategy == mock


def test_tran_commit_pass(tran_obj):
    """Tests that commit method executes provided strategy"""
    tran = tran_obj['tran_obj']
    mock = tran_obj['mock']

    tran.commit()

    assert mock.called


def test_tran_commit_wrong_type_one_arg(tran_type):
    with pytest.raises(TypeError, message="Expecting TypeError"):
        tran_type('non_callable_but_string')


def test_tran_commit_wrong_type_two_args(tran_type):
    with pytest.raises(TypeError, message="Expecting TypeError"):
        tran_type('non_callable_but_string', 'non_callable_but_string')


def test_tran_factory_pass(tran_factory, ref_transaction_dummy, tran_type):
    """Tests that get_transaction function returns instance of correct type"""
    tran_obj = tran_factory(ref_transaction_dummy)
    assert isinstance(tran_obj, tran_type)


def test_buy_plane_pass(buy_plane_tran_strategy, buy_plane_tran_strategy_mock):
    """Tests that buy plane transaction strategy is called"""
    buy_plane_tran_strategy(buy_plane_tran_strategy_mock)

    assert buy_plane_tran_strategy_mock.called


def test_buy_gun_pass(buy_gun_tran_strategy, buy_gun_tran_strategy_mock):
    """Tests that buy gun transaction strategy is called"""
    buy_gun_tran_strategy(buy_gun_tran_strategy_mock)

    assert buy_gun_tran_strategy_mock.called


if __name__ == '__main__':
    pytest.main()
