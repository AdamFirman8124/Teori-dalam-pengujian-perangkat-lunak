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
    """Test that array with no even values returns empty list."""
    result = pluck([1, 3, 5, 7, 9])
    assert result == []


def test_pluck_single_even_value():
    """Test array with single even value."""
    result = pluck([1, 4, 3])
    assert result == [4, 1]


def test_pluck_multiple_even_values():
    """Test array with multiple even values returns smallest."""
    result = pluck([4, 2, 3])
    assert result == [2, 1]


def test_pluck_duplicate_smallest_even():
    """Test that first index is returned when smallest even appears multiple times."""
    result = pluck([5, 0, 3, 0, 4, 2])
    assert result == [0, 1]


def test_pluck_zero_is_even():
    """Test that zero is correctly identified as even."""
    result = pluck([1, 3, 0, 5])
    assert result == [0, 2]


def test_pluck_all_even_values():
    """Test array with all even values."""
    result = pluck([8, 4, 6, 2])
    assert result == [2, 3]


def test_pluck_even_at_start():
    """Test even value at the beginning of array."""
    result = pluck([2, 5, 7, 9])
    assert result == [2, 0]


def test_pluck_even_at_end():
    """Test even value at the end of array."""
    result = pluck([5, 7, 9, 2])
    assert result == [2, 3]
