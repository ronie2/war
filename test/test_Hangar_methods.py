import pytest
import sys
import os

from class_constructor import constructor

# Adding a `war` package to the `sys.path` list for easy import
test_root_path = os.path.abspath(__file__ + "/../")
sys.path.insert(0, test_root_path)

import war

from war.buyer import Account
from war.buyer import Hangar
from war.transaction import Transaction


def test_planes_attribute(constructor):
    pass


def test_add_plane_function(constructor):
    pass


def test_has_plane_function(constructor):
    pass


def test_current_weapon_function(constructor):
    pass


def test_set_weapon_function(constructor):
    pass


def test_as_dict_function(constructor):
    pass
