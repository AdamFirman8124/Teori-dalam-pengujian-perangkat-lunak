# file: script_47.py:1-12
# asked: {"lines": [8, 9, 10, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [8, 9, 10, 12], "branches": [[9, 10], [9, 12]]}

import pytest
from script_47 import median


def test_median_odd_length():
    """Test median with odd number of elements."""
    result = median([3, 1, 2, 4, 5])
    assert result == 3


def test_median_even_length():
    """Test median with even number of elements."""
    result = median([-10, 4, 6, 1000, 10, 20])
    # Sorted: [-10, 4, 6, 10, 20, 1000]
    # Median is average of 6 and 10: (6 + 10) / 2 = 8.0
    assert result == 8.0


def test_median_single_element():
    """Test median with single element."""
    result = median([42])
    assert result == 42


def test_median_two_elements():
    """Test median with two elements."""
    result = median([1, 3])
    assert result == 2.0


def test_median_unsorted_odd():
    """Test median with unsorted odd-length list."""
    result = median([9, 1, 5, 3, 7])
    assert result == 5


def test_median_unsorted_even():
    """Test median with unsorted even-length list."""
    result = median([8, 2, 6, 4])
    assert result == 5.0


def test_median_negative_numbers_odd():
    """Test median with negative numbers and odd length."""
    result = median([-5, -1, -3])
    assert result == -3


def test_median_negative_numbers_even():
    """Test median with negative numbers and even length."""
    result = median([-10, -20, -30, -40])
    assert result == -25.0
