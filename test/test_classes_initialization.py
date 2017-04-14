import pytest
import sys
import os

from class_constructor import constructor

# Adding a `war` package to the `sys.path` list for easy import
test_root_path = os.path.abspath(__file__ + "/../")
sys.path.insert(0, test_root_path)

import war

from war.buyer import Account
from war.buyer import Hangar
from war.transaction import Transaction


def test_check_parameters_present(constructor):
    for parameter in constructor['er_parameters']:
        assert hasattr(constructor['result'], parameter)


def test_check_parameters_type(constructor):
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
