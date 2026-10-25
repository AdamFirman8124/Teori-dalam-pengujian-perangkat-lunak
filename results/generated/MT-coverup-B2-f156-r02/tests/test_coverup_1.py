# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "i"),
        (4, "iv"),
        (5, "v"),
        (9, "ix"),
        (10, "x"),
        (14, "xiv"),
        (19, "xix"),
        (40, "xl"),
        (50, "l"),
        (90, "xc"),
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        (1000, "m"),
        (3, "iii"),
        (8, "viii"),
        (24, "xxiv"),
        (58, "lviii"),
        (426, "cdxxvi"),
        (1994, "mcmxciv"),
        (3549, "mmmdxlix"),
        (3999, "mmmcmxcix"),
    ],
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected


def test_int_to_mini_roman_returns_lowercase():
    result = int_to_mini_roman(2024)
    assert result == "mmxxiv"
    assert result == result.lower()
