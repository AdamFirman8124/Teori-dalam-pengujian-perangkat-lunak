# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest
from f156 import int_to_mini_roman


def test_zero_returns_empty():
    result = int_to_mini_roman(0)
    assert result == ""
    assert isinstance(result, str)


def test_single_symbols_lowercase():
    cases = [
        (1, "i"),
        (4, "iv"),
        (5, "v"),
        (9, "ix"),
        (10, "x"),
        (40, "xl"),
        (50, "l"),
        (90, "xc"),
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        (1000, "m"),
    ]
    for number, expected in cases:
        result = int_to_mini_roman(number)
        assert result == expected
        assert result == result.lower()


def test_repeated_symbols_inner_loop_multiple_iterations():
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(2000) == "mm"
    assert int_to_mini_roman(3000) == "mmm"
    assert int_to_mini_roman(30) == "xxx"


@pytest.mark.parametrize(
    "number, expected",
    [
        (6, "vi"),
        (14, "xiv"),
        (44, "xliv"),
        (944, "cmxliv"),
        (1994, "mcmxciv"),
        (3999, "mmmcmxcix"),
        (58, "lviii"),
        (199, "cxcix"),
    ],
)
def test_complex_numbers(number, expected):
    result = int_to_mini_roman(number)
    assert result == expected
