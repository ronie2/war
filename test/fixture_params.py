factories_params = [
    {
        'name': 'get_buyer',
        'test_id': '001_get_buyer',
        'input': 'player',
        'er': {
            'type': 'Buyer',
        }
    },
    {
        'name': 'get_account',
        'test_id': '002_get_account',
        'input': 'player',
        'er': {
            'type': 'Account',
        }
    },
    {
        'name': 'get_hangar',
        'test_id': '003_get_hangar',
        'input': 'player',
        'er': {
            'type': 'Hangar',
        }
    },
    {
        'name': 'get_transaction',
        'test_id': '004_get_transaction',
        'input': '{"dummy_arg": None}',
        'er': {
            'type': 'Transaction'
        }
    }
]

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
    }
]
