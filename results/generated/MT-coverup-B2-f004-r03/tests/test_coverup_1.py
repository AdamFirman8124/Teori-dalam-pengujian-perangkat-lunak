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
    result = mean_absolute_deviation([5.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_symmetric_values():
    # Symmetric values around the mean: deviations cancel in magnitude sum.
    result = mean_absolute_deviation([1.0, 1.0, 1.0, 1.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_numbers():
    # mean of [-1.0, 0.0, 1.0] is 0.0; absolute deviations are [1.0, 0.0, 1.0]
    result = mean_absolute_deviation([-1.0, 0.0, 1.0])
    assert result == pytest.approx(2.0 / 3.0)


def test_mean_absolute_deviation_unsorted_values():
    # Order of elements must not affect the result.
    assert mean_absolute_deviation([4.0, 1.0, 7.0]) == pytest.approx(
        mean_absolute_deviation([7.0, 4.0, 1.0])
    )
    # mean of [4.0, 1.0, 7.0] is 4.0; absolute deviations are [0.0, 3.0, 3.0]
    assert mean_absolute_deviation([4.0, 1.0, 7.0]) == pytest.approx(2.0)
