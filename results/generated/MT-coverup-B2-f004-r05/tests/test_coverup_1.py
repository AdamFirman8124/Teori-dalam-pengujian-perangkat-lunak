# file: project/f004/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f004 import mean_absolute_deviation


def test_mean_absolute_deviation_basic():
    """Lines 6-7: computes mean and mean absolute deviation for a typical list."""
    numbers = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(numbers)
    # mean = 2.5; absolute deviations = [1.5, 0.5, 0.5, 1.5]; MAD = 4.0 / 4 = 1.0
    assert result == pytest.approx(1.0)


def test_mean_absolute_deviation_single_element():
    """Lines 6-7: single-element list yields zero deviation."""
    result = mean_absolute_deviation([5.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_identical_values():
    """Lines 6-7: identical values yield zero deviation."""
    result = mean_absolute_deviation([3.0, 3.0, 3.0])
    assert result == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_and_floats():
    """Lines 6-7: handles negative numbers and non-integer means."""
    numbers = [-1.0, 0.0, 1.0]
    result = mean_absolute_deviation(numbers)
    # mean = 0.0; absolute deviations = [1.0, 0.0, 1.0]; MAD = 2.0 / 3
    assert result == pytest.approx(2.0 / 3.0)


def test_mean_absolute_deviation_does_not_mutate_input():
    """Lines 6-7: input list is left unchanged (no state pollution)."""
    numbers = [1.0, 2.0, 3.0]
    snapshot = list(numbers)
    mean_absolute_deviation(numbers)
    assert numbers == snapshot
