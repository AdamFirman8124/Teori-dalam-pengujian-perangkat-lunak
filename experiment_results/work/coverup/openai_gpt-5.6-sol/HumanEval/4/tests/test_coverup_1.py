# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_executes_calculation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    original_numbers = numbers.copy()

    result = mean_absolute_deviation(numbers)

    assert result == pytest.approx(1.0)
    assert numbers == original_numbers
