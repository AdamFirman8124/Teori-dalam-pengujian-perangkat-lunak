# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_calculates_mad_without_mutating_input():
    numbers = [1.0, 2.0, 3.0, 4.0]
    original = numbers.copy()

    result = mean_absolute_deviation(numbers)

    assert result == pytest.approx(1.0)
    assert numbers == original


def test_mean_absolute_deviation_for_single_value():
    assert mean_absolute_deviation([5.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_rejects_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])
