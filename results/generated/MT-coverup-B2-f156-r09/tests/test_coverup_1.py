# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

from f156 import int_to_mini_roman


def test_int_to_mini_roman_zero():
    assert int_to_mini_roman(0) == ""


def test_int_to_mini_roman_conversion():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1994) == "mcmxciv"
