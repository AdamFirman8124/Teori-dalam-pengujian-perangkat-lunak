# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import math

import pytest

from f002 import truncate_number


@pytest.mark.parametrize(
    "number, expected",
    [
        (3.5, 0.5),        # positive with fractional part
        (4.0, 0.0),        # whole number
        (0.0, 0.0),        # zero
        (-1.25, 0.75),     # negative: Python modulo yields positive remainder
        (123.456, 0.456),  # larger positive value
        (0.999, 0.999),    # value already in [0, 1)
    ],
)
def test_truncate_number_returns_fractional_part(number, expected):
    result = truncate_number(number)
    assert math.isclose(result, expected, abs_tol=1e-9)
    # Postcondition: result is always the remainder of number % 1.0
    assert math.isclose(result, number % 1.0, abs_tol=1e-9)
    # Postcondition: result lies in the interval [0.0, 1.0)
    assert 0.0 <= result < 1.0


def test_truncate_number_matches_modulo_operator():
    for number in (7.25, -3.75, 10.0, 0.5, -0.5):
        assert truncate_number(number) == number % 1.0
