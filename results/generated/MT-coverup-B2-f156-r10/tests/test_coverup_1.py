# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

from f156 import int_to_mini_roman


def test_int_to_mini_roman_converts_using_subtractive_notation():
    assert int_to_mini_roman(3944) == "mmmcmxliv"


def test_int_to_mini_roman_zero_returns_empty_string():
    assert int_to_mini_roman(0) == ""
