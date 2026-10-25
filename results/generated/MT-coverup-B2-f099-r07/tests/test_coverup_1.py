# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

import pytest

from f099 import closest_integer


def test_positive_point_five_uses_ceil():
    assert closest_integer("14.5") == 15
    assert closest_integer("0.5") == 1
    assert closest_integer("2.5") == 3


def test_negative_point_five_uses_floor():
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1
    assert closest_integer("-2.5") == -3


def test_trailing_zeros_stripped_to_point_five():
    assert closest_integer("14.500") == 15
    assert closest_integer("-14.500") == -15
    assert closest_integer("14.50") == 15


def test_trailing_zeros_stripped_to_decimal_point():
    assert closest_integer("10.00") == 10
    assert closest_integer("10.0") == 10
    assert closest_integer("-10.00") == -10


def test_no_decimal_point_rounds_normally():
    assert closest_integer("10") == 10
    assert closest_integer("-10") == -10
    assert closest_integer("0") == 0


def test_decimal_without_trailing_zero_rounds_normally():
    assert closest_integer("14.3") == 14
    assert closest_integer("14.7") == 15
    assert closest_integer("-14.3") == -14
    assert closest_integer("-14.7") == -15
    assert closest_integer("9.9") == 10


def test_zero_length_value_uses_else_branch():
    class ZeroLenStr(str):
        def __len__(self):
            return 0

    # float(ZeroLenStr("10")) == 10.0, value[-2:] != ".5",
    # but len(value) == 0, so the else branch must return 0.
    assert closest_integer(ZeroLenStr("10")) == 0


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("14.5", 15),
        ("-14.5", -15),
        ("14.500", 15),
        ("10.00", 10),
        ("10", 10),
        ("14.3", 14),
        ("14.7", 15),
    ],
)
def test_closest_integer_parametrized(value, expected):
    result = closest_integer(value)
    assert result == expected
    assert isinstance(result, int)
