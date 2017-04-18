### Задание 1

Реализовать методы `buy_plane` и `buy_gun` класса `Shop`, обеспечивающие покупку
самолётов и орудий к ним в игре.

Методы `buy_plane` и `buy_gun` должны принимать состояние игрока и ID
соответствующего оборудования, и, при наличии у него достаточного количества 
ресурсов и выполнении дополнительных условий, обновлять состояние игрока, 
списывая ресурсы и начисляя оборудование.

Дополнительные условия:
- нельзя купить один самолёт дважды
- новый самолёт приобретается без орудий (значение поля `'gun'` - `None`)
- нельзя купить орудие, если не куплен соответствующий самолёт
- нельзя купить для самолёта орудие, которое с ним не совместимо
- нельзя купить для самолёта орудие, которое на него уже установлено в данный момент
- при покупке нового орудия на самолёт предыдущее списывается без компенсации ресурсов

При невозможности приобретения по какой-либо из причин вызывать исключение.

Описание класса `Shop`:

```python
class Shop(object):
    """Shop class providing methods to manipulate player's equipment"""

    def __init__(self, equipment):
        """
        Args:
            equipment (dict): DB of the game equipment in the following format:

                'planes': {
                    <plane_id:int>: {
                        'price': {<game_currency:str>: <amount:int>, ...},
                        'compatible_guns': {<gun_id:int>, ...}
                    },
                    ...
                },
                'guns': {
                    <gun_id:int>: {
                        'price': {<game_currency:str>: <amount:int>, ...}
                    },
                    ...
                }
        """
        self.db = equipment

    def buy_plane(self, player, plane_id):
        """Buy plane with ID `plane_id` for player `player` and update player's
        data as necessary.

        Args:
            player(dict): player's data in the following format:

                'id': <player_id:int>,
                'resources': {<game_currency:str>: <amount:int>, ...},
                'planes': {
                    <plane_id:int>: {'gun': <gun_id:int>},
                    ...
                }
            
            plane_id(int): Id of plane to buy

        Returns: None
        """

    def buy_gun(self, player, plane_id, gun_id):
        """Buy gun with ID `gun_id` for player `player` and update player's
        data as necessary.

        Args:
            player(dict): Player's data
            plane_id(int): Id of plane to buy gun for
            gun_id(int): Id of gun to buy

        Returns: None
        """
```

Пример базы оборудования, передаваемой в контруктор класса `Shop`:

```python
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
```

Пример состояния пользователя:

```python
player = {
    'id': 0,
    'resources': {
        'credits': 0,
        'gold': 0
    },
    'planes': {
        1001: {'gun': 201}
    },
}
```

### Задание 2

Покрыть тестами реализацию класса `Shop`.