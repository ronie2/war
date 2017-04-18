# Planes Shop
This repo implements Shop selling planes.
Task spec: [Shop Task](https://gist.github.com/ybilopolov/54181ade63465a99770144876e43f4a4)

##Requirements
- Python 3
- pytest 3 

##To run tests
```
$ git clone https://github.com/ronie2/war.git
$ cd war
$ python -m pytest
```


## Implementation details
[Class diagram](https://github.com/ronie2/war/blob/master/docs/class_diagram.svg)

[Error class diagram](https://github.com/ronie2/war/blob/master/docs/error_class_diagram.svg)

## Test coverage
Coverage measured with pytest-cov package:
```
Name                 Stmts   Miss  Cover
----------------------------------------
war/__init__.py          6      0   100%
war/base_shop.py         5      0   100%
war/buyer.py            62      7    89%
war/errors.py           10      0   100%
war/shop.py             38      0   100%
war/transaction.py      20      1    95%
war/validator.py        65      8    88%
----------------------------------------
TOTAL                  206     16    92%
```
