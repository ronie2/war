"""This module is used by fixture_class_inialization.py as parameters
and data source.
"""

# Dummy function to use as strategy when initializing class instances
def dummy_function():
    pass


test_strategy = dummy_function

# Dummy dict to use as dummy kwargs when initializing class instances
test_transaction = {
    'buyer': None,
    'plane_id': None,
    'price': None
}

# Expected results for class initialization.
# Change/add parameters if you had to.
class_params = [
    {
        'name': 'Buyer',
        'test_id': '001_Buyer_class',
        'init_parameters': 'player',
        'er': {
            'parameters': {
                'id': 'int',
                'account': 'Account',
                'hangar': 'Hangar'
            }
        }
    },
    {
        'name': 'Account',
        'test_id': '002_Account_class',
        'init_parameters': 'player',
        'er': {
            'parameters': {
                'balance': 'dict',
                'decrease': 'function',
                'has_enought_resource': 'function',
            }
        }
    },
    {
        'name': 'Hangar',
        'test_id': '003_Hangar_class',
        'init_parameters': 'player',
        'er': {
            'parameters': {
                'planes': 'dict',
                'add_plane': 'function',
                'has_plane': 'function',
                'current_weapon': 'function',
                'set_weapon': 'function',
            }
        }
    },
    {
        'name': 'Transaction',
        'test_id': '004_Transaction_class',
        'init_parameters': 'test_strategy, test_transaction',
        'er': {
            'parameters': {
                '_transaction_strategy': 'function',
                'transaction': 'dict',
                'commit': 'function'
            }
        }
    },
    {
        'name': 'WarPlanesShop',
        'test_id': '004_WarPlanesShop_class',
        'init_parameters': 'equipment',
        'er': {
            'parameters': {
                'db': 'dict',
                'buy_plane': 'function',
                'buy_gun': 'function',
                '_product_spec_by_id': 'function',
                '_product_price_by_id': 'function',
                '_WarPlanesShop__compatible_guns': 'function',
            }
        }
    },
]
