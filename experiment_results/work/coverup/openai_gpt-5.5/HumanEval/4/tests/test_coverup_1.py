# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_for_evenly_spaced_numbers():
    numbers = [1.0, 2.0, 3.0, 4.0]

    result = mean_absolute_deviation(numbers)

    assert result == pytest.approx(1.0)


def test_mean_absolute_deviation_for_single_number():
    numbers = [7.5]

    result = mean_absolute_deviation(numbers)

    assert result == pytest.approx(0.0)
