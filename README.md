# Planes Shop
This repo implements Shop selling planes.
Task spec: [Shop Task](https://gist.github.com/ybilopolov/54181ade63465a99770144876e43f4a4)

## Requirements
- Python 3
- pytest 3 

## To run tests
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
=========== test session starts ===========
platform linux -- Python 3.6.0, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /home/ronie/projects/war, inifile:
plugins: cov-2.4.0, asyncio-0.5.0
collected 67 items 

test/uat/test_uat.py ............
test/unit/test_buyer.py ................
test/unit/test_classes_initialization.py ..........
test/unit/test_shop.py ................
test/unit/test_transaction.py .......
test/unit/test_validator.py ......

----------- coverage: platform linux, python 3.6.0-final-0 -----------
Name                 Stmts   Miss  Cover
----------------------------------------
war/__init__.py          6      0   100%
war/base_shop.py         5      0   100%
war/buyer.py            59      5    92%
war/errors.py           10      0   100%
war/shop.py             38      0   100%
war/transaction.py      20      1    95%
war/validator.py        65      8    88%
----------------------------------------
TOTAL                  203     14    93%


========= 67 passed in 0.26 seconds =========
```
