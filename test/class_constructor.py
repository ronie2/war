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
from war.transaction import Transaction
from war.shop import WarPlanesShop

from test.fixture_params import class_params, test_strategy, test_transaction
from test.example_data import player, equipment


@pytest.fixture(params=class_params)
def constructor(request):
    print(request.param)
    _id = request.param['test_id']
    constructor = eval(request.param['name'])
    init_parameters = eval(request.param['init_parameters'])
    er_parameters = request.param['er']['parameters']

    if isinstance(init_parameters, tuple):
        result = constructor(*init_parameters)
    else:
        result = constructor(init_parameters)

    return {'_id': _id,
            'result': result,
            'er_parameters': er_parameters,
            'type': constructor}
