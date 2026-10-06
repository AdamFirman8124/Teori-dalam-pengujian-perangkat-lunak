# file: script_114.py:1-19
# asked: {"lines": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[11, 12], [11, 16], [13, 14], [13, 15], [16, 17], [16, 18]]}
# gained: {"lines": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[11, 12], [11, 16], [13, 14], [13, 15], [16, 17], [16, 18]]}

import pytest
from script_114 import minSubArraySum


def test_minSubArraySum_positive_numbers():
    """Test with all positive numbers - should return minimum single element."""
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1


def test_minSubArraySum_all_negative():
    """Test with all negative numbers - should return sum of all."""
    assert minSubArraySum([-1, -2, -3]) == -6


def test_minSubArraySum_mixed_positive_negative():
    """Test with mixed positive and negative numbers."""
    assert minSubArraySum([1, -3, 2, -1]) == -3


def test_minSubArraySum_single_positive():
    """Test with single positive element."""
    assert minSubArraySum([5]) == 5


def test_minSubArraySum_single_negative():
    """Test with single negative element."""
    assert minSubArraySum([-5]) == -5


def test_minSubArraySum_all_zeros():
    """Test with all zeros - edge case for line 16-17."""
    assert minSubArraySum([0, 0, 0]) == 0


def test_minSubArraySum_zeros_and_positives():
    """Test with zeros and positive numbers."""
    assert minSubArraySum([0, 1, 0, 2]) == 0


def test_minSubArraySum_large_positive_small_negative():
    """Test where a single negative is the minimum."""
    assert minSubArraySum([10, 20, -1, 15, 30]) == -1


def test_minSubArraySum_negative_subarray():
    """Test where minimum is a contiguous negative subarray."""
    assert minSubArraySum([5, -10, 3, -2, 8]) == -10


def test_minSubArraySum_alternating():
    """Test with alternating positive and negative."""
    assert minSubArraySum([-2, 3, -4, 5, -1]) == -4
