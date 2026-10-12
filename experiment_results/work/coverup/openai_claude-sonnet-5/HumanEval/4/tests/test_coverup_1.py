# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

import pytest
from script_4 import mean_absolute_deviation


def test_mean_absolute_deviation_simple():
    """Test MAD with a simple list of numbers."""
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    assert result == 1.0


def test_mean_absolute_deviation_single_element():
    """Test MAD with a single element (should be 0)."""
    result = mean_absolute_deviation([5.0])
    assert result == 0.0


def test_mean_absolute_deviation_identical_elements():
    """Test MAD with identical elements (should be 0)."""
    result = mean_absolute_deviation([3.0, 3.0, 3.0, 3.0])
    assert result == 0.0


def test_mean_absolute_deviation_negative_numbers():
    """Test MAD with negative numbers."""
    result = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
    assert result == 1.0


def test_mean_absolute_deviation_mixed_numbers():
    """Test MAD with mixed positive and negative numbers."""
    result = mean_absolute_deviation([-2.0, 0.0, 2.0])
    assert abs(result - 1.3333333333333333) < 1e-9


def test_mean_absolute_deviation_two_elements():
    """Test MAD with two elements."""
    result = mean_absolute_deviation([1.0, 5.0])
    assert result == 2.0


def test_mean_absolute_deviation_float_precision():
    """Test MAD with floats requiring precision."""
    result = mean_absolute_deviation([1.5, 2.5, 3.5])
    assert abs(result - 0.6666666666666666) < 1e-9
