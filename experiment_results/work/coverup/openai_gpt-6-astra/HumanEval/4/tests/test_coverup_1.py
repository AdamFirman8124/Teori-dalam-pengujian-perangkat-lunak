# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_for_example_dataset():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])

    assert result == 1.0


def test_mean_absolute_deviation_for_negative_and_positive_values():
    result = mean_absolute_deviation([-2.0, 0.0, 2.0])

    assert result == 4.0 / 3.0
