# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == 1.2


def test_mean_absolute_deviation_single_element():
    result = mean_absolute_deviation([10.0])
    assert result == 0.0


def test_mean_absolute_deviation_negative_and_zero_mean():
    result = mean_absolute_deviation([-2.0, 0.0, 2.0])
    assert result == 4.0 / 3.0


def test_mean_absolute_deviation_identical_values():
    result = mean_absolute_deviation([1.0, 1.0, 1.0, 1.0])
    assert result == 0.0
