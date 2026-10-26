# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

from f099 import closest_integer


def test_no_decimal_point_normal_rounding():
    assert closest_integer("2") == 2
    assert closest_integer("-3") == -3


def test_decimal_without_trailing_zero_normal_rounding():
    assert closest_integer("14.3") == 14
    assert closest_integer("14.7") == 15
    assert closest_integer("-14.3") == -14


def test_trailing_zeros_stripped_to_non_half():
    assert closest_integer("10.0") == 10
    assert closest_integer("10.00") == 10
    assert closest_integer("15.30") == 15


def test_positive_half_rounds_up_via_ceil():
    assert closest_integer("14.5") == 15
    assert closest_integer("0.5") == 1


def test_positive_half_with_trailing_zeros():
    assert closest_integer("14.5000") == 15
    assert closest_integer("0.500") == 1


def test_negative_half_rounds_down_via_floor():
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1


def test_negative_half_with_trailing_zeros():
    assert closest_integer("-14.5000") == -15
    assert closest_integer("-0.500") == -1


def test_empty_length_branch():
    class EmptyLenStr(str):
        def __len__(self):
            return 0

    # float("1") succeeds and value[-2:] != ".5", but len(value) == 0
    assert closest_integer(EmptyLenStr("1")) == 0
