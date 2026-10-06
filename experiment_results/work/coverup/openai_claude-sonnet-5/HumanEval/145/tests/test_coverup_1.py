# file: script_145.py:1-18
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18], "branches": [[14, 14], [14, 15]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18], "branches": [[14, 14], [14, 15]]}

import pytest
from script_145 import order_by_points


def test_order_by_points_with_negative_numbers():
    """Test that negative numbers are handled correctly with digit sum calculation."""
    result = order_by_points([1, 11, -1, -11, -12])
    assert result == [-1, -11, 1, -12, 11]


def test_order_by_points_empty_list():
    """Test that empty list returns empty list."""
    result = order_by_points([])
    assert result == []


def test_order_by_points_single_negative():
    """Test with a single negative number to execute the negative handling path."""
    result = order_by_points([-5])
    assert result == [-5]


def test_order_by_points_mixed_negatives():
    """Test with multiple negative numbers to ensure digit_sum function is called."""
    result = order_by_points([-99, -10, -1])
    # -99: -(9) + 9 = -9 + 9 = 0
    # -10: -(1) + 0 = -1 + 0 = -1
    # -1: -1
    assert result == [-10, -1, -99]


def test_order_by_points_negative_vs_positive():
    """Test that negative numbers with same absolute digit sum are ordered correctly."""
    result = order_by_points([12, -12, 21, -21])
    # 12: 1+2 = 3
    # -12: -(1) + 2 = -1 + 2 = 1
    # 21: 2+1 = 3
    # -21: -(2) + 1 = -2 + 1 = -1
    assert result == [-21, -12, 12, 21]


def test_order_by_points_zero_and_negatives():
    """Test with zero and negative numbers."""
    result = order_by_points([0, -5, -10])
    # 0: 0
    # -5: -5
    # -10: -(1) + 0 = -1
    assert result == [-5, -10, 0]


def test_order_by_points_large_negative():
    """Test with larger negative numbers to ensure all digits are processed."""
    result = order_by_points([-123, -45, -6])
    # -123: -(1) + 2 + 3 = -1 + 2 + 3 = 4
    # -45: -(4) + 5 = -4 + 5 = 1
    # -6: -6
    assert result == [-6, -45, -123]
