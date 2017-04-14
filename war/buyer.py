def get_hangar(player):
    return Hangar(player['planes'])


def get_buyer(player):
    return Buyer(player)


def get_account(player):
    return Account(player['resources'])


class Account:
    def __init__(self, account):
        self.account = account

    def decrease(self, price):
        for resource_type in price:
            self.account[resource_type] -= price[resource_type]

    def has_enought_resource(self, price):
        for resource in price:
            if resource not in self.account:
                return False
            if self.account[resource] < price[resource]:
                return False
        return True

    def as_dict(self):
        return dict(self.account)


class Hangar:
    def __init__(self, palanes):
        self.planes = palanes

    def __contains__(self, plane_id):
        if not isinstance(plane_id, int):
            raise TypeError
        return plane_id in self.planes

    def __getitem__(self, plane_id):
        if not isinstance(plane_id, int):
            raise TypeError
        if plane_id not in self.planes:
            raise KeyError
        return self.planes[plane_id]

    def __setitem__(self, plane_id, plane_spec):
        if not isinstance(plane_id, int):
            raise TypeError
        self.planes[plane_id] = plane_spec

    def add_plane(self, plane_id):
        self[plane_id] = {'gun': None}

    def has_plane(self, plane_id):
        return plane_id in self

    def current_weapon(self, plane_id):
        return self[plane_id]['gun']

    def set_weapon(self, plane_id, gun_id):
        self[plane_id]['gun'] = gun_id

    def as_dict(self):
        return dict(self.planes)


class Buyer:
    def __init__(self, player):
        try:
            self.id = player['id']
            self.account = get_account(player)
            self.hangar = get_hangar(player)
        except KeyError:
            raise RuntimeError('A player parsing error. The keys are missing')
