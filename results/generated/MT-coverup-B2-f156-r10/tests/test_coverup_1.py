# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


@pytest.mark.parametrize(
    "number, expected",
    [
        # Smallest value: outer loop runs once, inner loop runs once.
        (1, "i"),
        # Each subtractive/special symbol value.
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
        # Inner while loop executes multiple times (repeated symbols).
        (3, "iii"),
        (8, "viii"),
        (38, "xxxviii"),
        # Inner while loop skipped (div == 0) for several i values.
        (19, "xix"),
        (152, "clii"),
        (426, "cdxxvi"),
        (1994, "mcmxciv"),
        # Largest supported value: outer loop iterates through all i values.
        (3999, "mmmcmxcix"),
    ],
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected


def test_int_to_mini_roman_is_lowercase():
    result = int_to_mini_roman(1987)
    assert result == "mcmlxxxvii"
    assert result == result.lower()


def test_int_to_mini_roman_roundtrip_consistency():
    # Greedy reconstruction: converting back must yield the same number.
    values = {1: "i", 4: "iv", 9: "ix", 14: "xiv", 40: "xl", 90: "xc",
              400: "cd", 900: "cm", 1000: "m", 2421: "mmcdxxi"}
    roman_values = {"i": 1, "iv": 4, "v": 5, "ix": 9, "x": 10, "xl": 40,
                    "l": 50, "xc": 90, "c": 100, "cd": 400, "d": 500,
                    "cm": 900, "m": 1000}
    for number, roman in values.items():
        result = int_to_mini_roman(number)
        assert result == roman
        # Verify by greedy decoding of the produced string.
        decoded, idx = 0, 0
        while idx < len(result):
            for sym, val in sorted(roman_values.items(), key=lambda kv: -len(kv[0])):
                if result.startswith(sym, idx):
                    decoded += val
                    idx += len(sym)
                    break
            else:
                pytest.fail(f"Unexpected symbol in {result!r}")
        assert decoded == number
