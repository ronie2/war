"""These module tests war.validator.py module"""
from test.unit.fixture_logic import *


def test_validator_init_values(validator_obj, ref_transaction_dummy):
    """Tests that instance values are initialized correct"""
    strategy = validator_obj['validator_obj'].validation_strategy
    kwargs = validator_obj['validator_obj'].kwargs
    mock = validator_obj['mock']

    assert kwargs == ref_transaction_dummy
    assert strategy == mock


def test_validator_validate_pass(validator_obj, ref_transaction_dummy):
    """Tests that validate method was called with correct kwargs"""
    validator = validator_obj['validator_obj']
    mock = validator_obj['mock']
    validator.validate()

    assert mock.called
    assert mock.call_args[1] == ref_transaction_dummy


def test_validation_validate_wrong_type(validator_type):
    with pytest.raises(TypeError, message="Expecting TypeError"):
        validator_type('non_callable_but_string')


def test_validator_get_validator_msg_pass(validator_factory,
                                          ref_equipment,
                                          ref_player,
                                          validator_type):
    """Tests that get_validator correctly resolves messages"""
    assert isinstance(validator_factory({'player': ref_player}),
                      validator_type)

    assert isinstance(validator_factory({'equipment': ref_equipment}),
                      validator_type)


def test_validator_get_validator_tran_pass(validator_factory,
                                           validator_type,
                                           ref_buy_plane_tran,
                                           ref_buy_gun_tran):
    """Tests that get_validator correctly resolves transactions"""
    tran_dict = ref_buy_plane_tran['tran']
    assert isinstance(validator_factory(tran_dict), validator_type)

    tran_dict = ref_buy_gun_tran['tran']
    assert isinstance(validator_factory(tran_dict), validator_type)


def test_validator_get_validator_wrong_value(validator_factory,
                                             ref_transaction_dummy):
    with pytest.raises(TransactionValidationError,
                       message="Expecting TransactionValidationError"):
        validator_factory(ref_transaction_dummy)


if __name__ == '__main__':
    pytest.main()
