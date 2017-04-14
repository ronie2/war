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
        'credits': 100,
        'gold': 100
    },
    'planes': {
        1001: {'gun': 201}
    },
}
