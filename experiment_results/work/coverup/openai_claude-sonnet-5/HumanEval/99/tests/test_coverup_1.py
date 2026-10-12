# file: script_99.py:1-37
# asked: {"lines": [19, 21, 23, 24, 26, 27, 28, 29, 31, 32, 33, 35, 37], "branches": [[21, 23], [21, 26], [23, 24], [23, 26], [27, 28], [27, 32], [28, 29], [28, 31], [32, 33], [32, 35]]}
# gained: {"lines": [19, 21, 23, 24, 26, 27, 28, 29, 31, 32, 33, 37], "branches": [[21, 23], [21, 26], [23, 24], [23, 26], [27, 28], [27, 32], [28, 29], [28, 31], [32, 33]]}

import pytest
from script_99 import closest_integer


def test_closest_integer_positive_half():
    """Test positive number ending in .5 rounds away from zero (up)"""
    assert closest_integer("14.5") == 15
    assert closest_integer("10.5") == 11
    assert closest_integer("0.5") == 1


def test_closest_integer_negative_half():
    """Test negative number ending in .5 rounds away from zero (down)"""
    assert closest_integer("-14.5") == -15
    assert closest_integer("-10.5") == -11
    assert closest_integer("-0.5") == -1


def test_closest_integer_with_trailing_zeros():
    """Test numbers with trailing zeros after decimal point"""
    assert closest_integer("14.50") == 15
    assert closest_integer("14.500") == 15
    assert closest_integer("-14.50") == -15
    assert closest_integer("10.5000") == 11


def test_closest_integer_regular_rounding():
    """Test regular rounding for non-.5 decimals"""
    assert closest_integer("15.3") == 15
    assert closest_integer("15.7") == 16
    assert closest_integer("-15.3") == -15
    assert closest_integer("-15.7") == -16


def test_closest_integer_whole_number():
    """Test whole numbers"""
    assert closest_integer("10") == 10
    assert closest_integer("0") == 0
    assert closest_integer("-10") == -10


def test_closest_integer_decimal_with_trailing_zeros_not_half():
    """Test decimal with trailing zeros that is not .5"""
    assert closest_integer("15.30") == 15
    assert closest_integer("15.700") == 16
