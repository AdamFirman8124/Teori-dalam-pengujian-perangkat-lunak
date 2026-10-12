# file: script_47.py:1-12
# asked: {"lines": [8, 9, 10, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [8, 9, 10, 12], "branches": [[9, 10], [9, 12]]}

import pytest
from script_47 import median


def test_median_odd_length():
    """Test median with odd number of elements."""
    result = median([3, 1, 2, 4, 5])
    assert result == 3
    
    result = median([1])
    assert result == 1
    
    result = median([5, 3, 1])
    assert result == 3


def test_median_even_length():
    """Test median with even number of elements."""
    # Sorted: [-10, 4, 6, 10, 20, 1000]
    # Median indices: 2 and 3 (6 and 10)
    # Median: (6 + 10) / 2 = 8.0
    result = median([-10, 4, 6, 1000, 10, 20])
    assert result == 8.0
    
    result = median([1, 2])
    assert result == 1.5
    
    result = median([1, 2, 3, 4])
    assert result == 2.5


def test_median_does_not_modify_input():
    """Test that median does not modify the input list."""
    original = [3, 1, 2, 4, 5]
    input_list = original.copy()
    median(input_list)
    assert input_list == original
