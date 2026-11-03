# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    # mean of [1.0, 2.0, 3.0] is 2.0; absolute deviations are [1.0, 0.0, 1.0]
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    assert result == pytest.approx(2.0 / 3.0)


def test_mean_absolute_deviation_single_element():
    # A single element has zero deviation from its own mean.
    assert mean_absolute_deviation([5.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_identical_values():
    # All identical values yield zero mean absolute deviation.
    assert mean_absolute_deviation([4.0, 4.0, 4.0, 4.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_and_floats():
    # mean of [-1.5, 0.5, 2.5] is 0.5; absolute deviations are [2.0, 0.0, 2.0]
    result = mean_absolute_deviation([-1.5, 0.5, 2.5])
    assert result == pytest.approx(4.0 / 3.0)


def test_mean_absolute_deviation_result_is_nonnegative():
    result = mean_absolute_deviation([10.0, -10.0])
    assert result >= 0.0
    assert result == pytest.approx(10.0)
