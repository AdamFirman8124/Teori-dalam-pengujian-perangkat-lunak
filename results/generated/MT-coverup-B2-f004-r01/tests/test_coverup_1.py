# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    # mean = 2.0; absolute deviations = [1.0, 0.0, 1.0]; MAD = 2/3
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    assert result == pytest.approx(2.0 / 3.0)


def test_mean_absolute_deviation_single_element():
    # A single element has zero deviation from its own mean.
    assert mean_absolute_deviation([5.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_symmetric_around_zero():
    # mean = 0.0; absolute deviations = [1.0, 1.0]; MAD = 1.0
    assert mean_absolute_deviation([-1.0, 1.0]) == pytest.approx(1.0)


def test_mean_absolute_deviation_identical_values():
    # All values equal the mean, so deviation is zero.
    assert mean_absolute_deviation([3.5, 3.5, 3.5, 3.5]) == pytest.approx(0.0)


def test_mean_absolute_deviation_mixed_values():
    # mean = 3.0; absolute deviations = [2.0, 1.0, 0.0, 1.0, 2.0]; MAD = 6/5
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == pytest.approx(1.2)
    assert result >= 0.0
