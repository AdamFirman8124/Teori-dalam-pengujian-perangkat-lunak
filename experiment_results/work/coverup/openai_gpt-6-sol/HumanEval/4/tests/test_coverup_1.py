# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest

from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_for_multiple_values():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])

    assert result == 1.0


def test_mean_absolute_deviation_for_identical_values():
    result = mean_absolute_deviation([5.0, 5.0, 5.0])

    assert result == 0.0


def test_mean_absolute_deviation_rejects_empty_input():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])
