# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_simple():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0


def test_mean_absolute_deviation_symmetric_around_mean():
    assert mean_absolute_deviation([-1.0, 1.0]) == 1.0
    assert mean_absolute_deviation([-2.0, 0.0, 2.0]) == pytest.approx(4.0 / 3.0)


def test_mean_absolute_deviation_constant_list():
    assert mean_absolute_deviation([5.0, 5.0, 5.0]) == 0.0


def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([7.5]) == 0.0


def test_mean_absolute_deviation_int_list():
    assert mean_absolute_deviation([2, 3, 4]) == pytest.approx(2.0 / 3.0)


def test_mean_absolute_deviation_negative_and_empty():
    assert mean_absolute_deviation([3, -3]) == pytest.approx(3.0)
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])
