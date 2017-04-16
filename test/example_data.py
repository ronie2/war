equipment = {
    'planes': {
        1001: {
            'price': {'credits': 100},
            'compatible_guns': {201}
        },
        1002: {
            'price': {'credits': 500},
            'compatible_guns': {202}
        },
        1003: {
            'price': {'gold': 50},
            'compatible_guns': {201, 202, 203}
        },
    },
    'guns': {
        201: {
            'price': {'credits': 10},
        },
        202: {
            'price': {'credits': 50},
        },
        203: {
            'price': {'gold': 5},
        }
    }
}

player = {
    'id': 0,
    'resources': {
        'credits': 1000,
        'gold': 1000
    },
    'planes': {
        1001: {'gun': 201}
    },
}

transaction_dummy = {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'}

buy_gun_transaction = {
    'buyer': None,
    'plane_id': None,
    'gun_id': None,
    'comp_guns': None,
    'price': None
}

buy_plane_transaction = {
    'buyer': None,
    'plane_id': None,
    'price': None
}
