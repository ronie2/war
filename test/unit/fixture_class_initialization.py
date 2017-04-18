"""A fixture that prepares classes.
It uses data from data_inialization_params.py file.
You may change data_inialization_params.py file to add/change test params
"""
import pytest

from war.buyer import get_buyer
from war.buyer import get_account
from war.buyer import get_hangar

from war.buyer import Buyer
from war.buyer import Account
from war.buyer import Hangar
from war.transaction import Transaction
from war.shop import WarPlanesShop

from test.example_data import player, equipment
from test.unit.data_initialization_params import (
    class_params,
    test_strategy,
    test_transaction
)


@pytest.fixture(params=class_params)
def constructor(request):
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
