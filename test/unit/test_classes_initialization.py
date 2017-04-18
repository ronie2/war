"""Tests static class instances inialization. Test is initialized with
data_initialization_params.py module. Feel free to change data params module
to add/change expected results.
"""
import pytest

from war.buyer import Account
from war.buyer import Hangar
from war.transaction import Transaction

from test.unit.fixture_class_initialization import constructor


def test_check_parameters_present(constructor):
    """Checks that all required attributes are present"""
    for parameter in constructor['er_parameters']:
        assert hasattr(constructor['result'], parameter)


def test_check_parameters_type(constructor):
    """Checks parameters types"""
    for parameter, value_type in constructor['er_parameters'].items():
        SUT_parameter = getattr(constructor['result'], parameter)
        ER_parameter = value_type
        if ER_parameter == 'function':
            assert callable(SUT_parameter)
        else:
            ER_parameter = eval(value_type)
            assert isinstance(SUT_parameter, ER_parameter)


if __name__ == '__main__':
    pytest.main()
