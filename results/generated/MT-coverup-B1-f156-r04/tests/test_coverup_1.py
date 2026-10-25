# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "i"),
        (2, "ii"),
        (3, "iii"),
        (4, "iv"),
        (5, "v"),
        (9, "ix"),
        (14, "xiv"),
        (40, "xl"),
        (49, "xlix"),
        (90, "xc"),
        (400, "cd"),
        (900, "cm"),
        (1000, "m"),
        (1994, "mcmxciv"),
        (2024, "mmxxiv"),
        (3999, "mmmcmxcix"),
    ],
)
def test_int_to_mini_roman_values(number, expected):
    result = int_to_mini_roman(number)
    assert result == expected
    # postconditions: lowercase, non-empty, only roman letters
    assert result == result.lower()
    assert result
    assert set(result) <= set("ivxlcdm")


def test_int_to_mini_roman_zero_returns_empty_string():
    assert int_to_mini_roman(0) == ""


def test_int_to_mini_roman_skips_zero_quotient_branches():
    # exercises iterations where div == 0 (inner while never entered)
    assert int_to_mini_roman(1001) == "mi"
    assert int_to_mini_roman(6) == "vi"


def test_int_to_mini_roman_repeated_symbols():
    # exercises the inner while loop running multiple times
    assert int_to_mini_roman(3000) == "mmm"
    assert int_to_mini_roman(88) == "lxxxviii"


def test_int_to_mini_roman_does_not_mutate_input_state():
    number = 1987
    first = int_to_mini_roman(number)
    second = int_to_mini_roman(number)
    assert first == second == "mcmlxxxvii"
    assert number == 1987
