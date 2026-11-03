# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, "i"),          # minimal input: outer loop runs, inner loop body runs once
        (3, "iii"),        # inner loop body runs repeatedly (div > 1)
        (4, "iv"),
        (9, "ix"),
        (14, "xiv"),
        (19, "xix"),       # div == 0 for the high-value symbols: inner while false branch
        (40, "xl"),
        (90, "xc"),
        (400, "cd"),
        (426, "cdxxvi"),   # walks i all the way down through every symbol position
        (901, "cmi"),
        (999, "cmxcix"),
        (1000, "m"),       # largest single-symbol value
    ],
)
def test_int_to_mini_roman_known_values(number, expected):
    assert int_to_mini_roman(number) == expected


def test_int_to_mini_roman_postconditions():
    for number in (1, 19, 426, 999, 1000):
        result = int_to_mini_roman(number)
        assert result, "result must be non-empty for a positive number"
        assert result == result.lower(), "result must be lowercase"
        assert result.isalpha(), "result must contain only roman numeral letters"
