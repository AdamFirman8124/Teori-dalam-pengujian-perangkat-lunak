# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "i"),        # smallest value, single symbol
        (4, "iv"),       # subtractive pair
        (9, "ix"),       # subtractive pair
        (14, "xiv"),
        (19, "xix"),
        (40, "xl"),
        (90, "xc"),
        (400, "cd"),
        (900, "cm"),
        (1000, "m"),
        (1987, "mcmlxxxvii"),   # mixes many numerals
        (3549, "mmmdxlix"),     # high-end value
        (3000, "mmm"),          # exercises inner "while div" loop 3 times
        (38, "xxxviii"),        # repeated X and I
        (152, "clii"),          # repeated I at the tail
        (426, "cdxxvi"),        # repeated X
    ],
)
def test_int_to_mini_roman_known_values(number, expected):
    result = int_to_mini_roman(number)
    assert result == expected
    # Postcondition: output is always lowercase roman numerals
    assert result == result.lower()
    assert result.islower() or not result


def test_int_to_mini_roman_repeated_symbol_branch():
    # 'while div' must execute its body multiple times (div > 1)
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(2) == "ii"


def test_int_to_mini_roman_all_lines_exercised():
    # Single call that walks every value in num[]/sym[] and both loops
    result = int_to_mini_roman(3888)  # mmmdccclxxxviii
    assert result == "mmmdccclxxxviii"
    assert result == result.lower()


def test_int_to_mini_roman_zero_returns_empty():
    # number == 0 means the outer while loop is skipped entirely
    assert int_to_mini_roman(0) == ""
