# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    numbers = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(1.0)
    assert isinstance(result, float)


def test_mean_absolute_deviation_single_element():
    result = mean_absolute_deviation([42.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_and_positive():
    numbers = [-2.0, 0.0, 2.0]
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(4.0 / 3.0)


def test_mean_absolute_deviation_identical_values():
    numbers = [5.5, 5.5, 5.5, 5.5]
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_floats():
    numbers = [1.5, 2.5, 3.5]
    result = mean_absolute_deviation(numbers)
    assert result == pytest.approx(2.0 / 3.0)
