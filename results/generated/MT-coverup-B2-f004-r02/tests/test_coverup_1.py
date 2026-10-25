# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest
from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    # mean = 2.5, deviations = 1.5, 0.5, 0.5, 1.5 -> avg = 1.0
    assert result == pytest.approx(1.0)


def test_mean_absolute_deviation_single_element():
    result = mean_absolute_deviation([10.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_identical_values():
    result = mean_absolute_deviation([5.0, 5.0, 5.0, 5.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_symmetric():
    result = mean_absolute_deviation([-1.0, 0.0, 1.0])
    # mean = 0.0, deviations = 1, 0, 1 -> avg = 2/3
    assert result == pytest.approx(2.0 / 3.0)
