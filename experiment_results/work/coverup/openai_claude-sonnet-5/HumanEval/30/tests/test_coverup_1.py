# file: script_30.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_30 import get_positive


def test_get_positive_with_mixed_numbers():
    """Test get_positive with a mix of positive and negative numbers."""
    result = get_positive([-1, 2, -4, 5, 6])
    assert result == [2, 5, 6]


def test_get_positive_with_multiple_numbers():
    """Test get_positive with a longer list including zero."""
    result = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    assert result == [5, 3, 2, 3, 9, 123, 1]


def test_get_positive_empty_list():
    """Test get_positive with an empty list."""
    result = get_positive([])
    assert result == []


def test_get_positive_all_negative():
    """Test get_positive with all negative numbers."""
    result = get_positive([-1, -2, -3, -4])
    assert result == []


def test_get_positive_all_positive():
    """Test get_positive with all positive numbers."""
    result = get_positive([1, 2, 3, 4])
    assert result == [1, 2, 3, 4]


def test_get_positive_with_zero():
    """Test get_positive with only zero."""
    result = get_positive([0])
    assert result == []


def test_get_positive_with_zeros_and_positives():
    """Test get_positive with zeros and positive numbers."""
    result = get_positive([0, 1, 0, 2, 0])
    assert result == [1, 2]
