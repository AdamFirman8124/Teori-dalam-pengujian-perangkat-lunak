# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_calculates_average_absolute_distance():
    numbers = [1.0, 2.0, 3.0, 4.0]

    result = mean_absolute_deviation(numbers)

    assert result == 1.0


def test_mean_absolute_deviation_handles_values_with_nonzero_mean():
    numbers = [10.0, 10.0, 20.0]

    result = mean_absolute_deviation(numbers)

    assert result == 4.444444444444445
