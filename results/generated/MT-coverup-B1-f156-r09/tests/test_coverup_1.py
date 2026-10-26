# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


def test_int_to_mini_roman_single_digit():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(9) == "ix"


def test_int_to_mini_roman_tens():
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(90) == "xc"


def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"


def test_int_to_mini_roman_thousand():
    assert int_to_mini_roman(1000) == "m"


def test_int_to_mini_roman_repeated_symbols():
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(2000) == "mm"


def test_int_to_mini_roman_mixed():
    assert int_to_mini_roman(4267) == "mmmmcclxvii"
    assert int_to_mini_roman(1994) == "mcmxciv"
    assert int_to_mini_roman(3549) == "mmmdxlix"
    assert int_to_mini_roman(58) == "lviii"
