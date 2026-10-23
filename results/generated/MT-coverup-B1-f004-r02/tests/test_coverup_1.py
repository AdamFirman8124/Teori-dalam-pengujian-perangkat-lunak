# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

from typing import List

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_three_values():
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    assert result == 2.0 / 3.0


def test_mean_absolute_deviation_single_value():
    result = mean_absolute_deviation([5.0])
    assert result == 0.0


def test_mean_absolute_deviation_negative_values():
    result = mean_absolute_deviation([-1.0, 1.0])
    assert result == 1.0


def test_mean_absolute_deviation_empty_list_raises_zero_division():
    try:
        mean_absolute_deviation([])
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Expected ZeroDivisionError for empty input")
