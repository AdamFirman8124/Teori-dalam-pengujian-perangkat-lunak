# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

import pytest

from f099 import closest_integer


def test_positive_point_five_uses_ceil():
    assert closest_integer("2.5") == 3
    assert closest_integer("0.5") == 1
    assert isinstance(closest_integer("2.5"), int)


def test_negative_point_five_uses_floor():
    assert closest_integer("-2.5") == -3
    assert closest_integer("-0.5") == -1
    assert isinstance(closest_integer("-2.5"), int)


def test_trailing_zeros_stripped_before_point_five_check():
    assert closest_integer("2.5000") == 3
    assert closest_integer("-2.5000") == -3
    assert closest_integer("14.500") == 15


def test_trailing_zeros_stripped_then_normal_rounding():
    assert closest_integer("10.0") == 10
    assert closest_integer("1.2000") == 1
    assert closest_integer("3.000") == 3


def test_no_decimal_point_skips_zero_stripping_and_rounds():
    assert closest_integer("10") == 10
    assert closest_integer("-7") == -7
    assert closest_integer("0") == 0


def test_decimal_without_trailing_zero_uses_normal_rounding():
    assert closest_integer("2.4") == 2
    assert closest_integer("2.6") == 3
    assert closest_integer("-2.4") == -2
    assert closest_integer("-2.6") == -3
    assert closest_integer("9.9") == 10


def test_empty_value_after_float_uses_else_branch():
    class FakeValue:
        def __init__(self):
            self.floated = False

        def count(self, _sub):
            return 0

        def __float__(self):
            self.floated = True
            return 2.6

        def __getitem__(self, key):
            if isinstance(key, slice):
                return ""
            return "x"

        def __len__(self):
            return 0 if self.floated else 1

    fake = FakeValue()
    assert closest_integer(fake) == 0
    assert fake.floated is True
