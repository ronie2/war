import pytest
import sys
import os

# Adding a `war` package to the `sys.path` list for easy import
test_root_path = os.path.abspath(__file__ + "/../")
sys.path.insert(0, test_root_path)

import war

from war.buyer import get_buyer
from war.buyer import get_account
from war.buyer import get_hangar
from war.buyer import Buyer
from war.buyer import Account
from war.buyer import Hangar

from fixture_params import class_params
from example_data import player
from example_data import equipment


@pytest.fixture(params=class_params)
def constructor(request):
    _id = request.param['test_id']
    constructor = eval(request.param['name'])
    init_parameters = eval(request.param['init_parameters'])
    er_parameters = request.param['er']['parameters']

    return {'_id': _id, 'constructor': constructor,
            'init_parameters': init_parameters,
            'er_parameters': er_parameters}


def test_check_parameters_present(constructor):
    print(constructor['_id'])

    # Call SUT
    constr = constructor['constructor']
    init_parameters = constructor['init_parameters']

    result = constr(init_parameters)

    for parameter in constructor['er_parameters']:
        assert hasattr(result, parameter)


def test_check_parameters_type(constructor):
    print(constructor['_id'])

    # Call SUT
    constr = constructor['constructor']
    init_parameters = constructor['init_parameters']

    result = constr(init_parameters)

    for parameter, value_type in constructor['er_parameters'].items():
        SUT_parameter = getattr(result, parameter)
        ER_parameter = value_type
        if ER_parameter == 'function':
            assert callable(SUT_parameter)
        else:
            ER_parameter = eval(value_type)
            assert isinstance(SUT_parameter, ER_parameter)


if __name__ == '__main__':
    pytest.main()
