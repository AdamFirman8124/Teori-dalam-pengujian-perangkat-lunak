# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_calculates_average_absolute_difference():
    numbers = [1.0, 2.0, 3.0, 4.0]

    result = mean_absolute_deviation(numbers)

    assert result == 1.0


def test_mean_absolute_deviation_returns_zero_for_identical_values():
    numbers = [7.5, 7.5, 7.5]

    result = mean_absolute_deviation(numbers)

    assert result == 0.0
