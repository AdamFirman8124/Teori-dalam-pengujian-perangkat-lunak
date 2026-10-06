# file: script_68.py:1-38
# asked: {"lines": [35, 36, 37, 38], "branches": [[35, 35], [35, 36], [37, 37], [37, 38]]}
# gained: {"lines": [35, 36, 37, 38], "branches": [[35, 35], [35, 36], [37, 37], [37, 38]]}

import pytest
from script_68 import pluck


def test_pluck_empty_array():
    """Test that empty array returns empty list."""
    result = pluck([])
    assert result == []


def test_pluck_no_even_values():
    """Test that array with only odd values returns empty list."""
    result = pluck([1, 3, 5, 7])
    assert result == []


def test_pluck_single_even_value():
    """Test that array with single even value returns correct result."""
    result = pluck([1, 3, 4, 5])
    assert result == [4, 2]


def test_pluck_multiple_even_values():
    """Test that smallest even value is returned with correct index."""
    result = pluck([4, 2, 3])
    assert result == [2, 1]


def test_pluck_multiple_same_smallest_even():
    """Test that first occurrence of smallest even is returned."""
    result = pluck([5, 0, 3, 0, 4, 2])
    assert result == [0, 1]


def test_pluck_zero_is_even():
    """Test that zero is treated as even."""
    result = pluck([1, 3, 0, 5])
    assert result == [0, 2]


def test_pluck_all_even_values():
    """Test array with all even values."""
    result = pluck([8, 4, 6, 2])
    assert result == [2, 3]


def test_pluck_even_at_start():
    """Test even value at index 0."""
    result = pluck([2, 5, 7])
    assert result == [2, 0]


def test_pluck_large_numbers():
    """Test with larger even numbers."""
    result = pluck([100, 50, 75, 25])
    assert result == [50, 1]
