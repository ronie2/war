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

from fixture_params import factories_params
from example_data import player


@pytest.fixture(params=factories_params)
def factories(request):
    _id = request.param['test_id']
    factory = eval(request.param['name'])
    input = eval(request.param['input'])
    er_type = eval(request.param['er']['type'])

    return {'_id': _id, 'factory': factory, 'input': input, 'er_type': er_type}


def test_check_return_type(factories):
    print(factories['_id'])

    # Call SUT
    func = factories['factory']
    input = factories['input']

    result = func(input)

    assert isinstance(result, factories['er_type'])


# def test_check_return_value(factories):
#     print(factories['_id'])
#
#     # Call SUT
#     func = factories['factory']
#     input = factories['input']
#
#     result = func(input)
#
#     for key, value in
#
#     assert result == factories

if __name__ == '__main__':
    pytest.main()
