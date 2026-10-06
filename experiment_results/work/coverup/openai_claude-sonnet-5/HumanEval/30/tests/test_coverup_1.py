# file: script_30.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_30 import get_positive


def test_get_positive_with_mixed_numbers():
    """Test with a mix of positive, negative, and zero."""
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]


def test_get_positive_with_more_mixed_numbers():
    """Test with another mix including zero."""
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]


def test_get_positive_empty_list():
    """Test with an empty list."""
    assert get_positive([]) == []


def test_get_positive_all_negative():
    """Test with all negative numbers."""
    assert get_positive([-1, -2, -3, -4]) == []


def test_get_positive_all_positive():
    """Test with all positive numbers."""
    assert get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_get_positive_only_zeros():
    """Test with only zeros."""
    assert get_positive([0, 0, 0]) == []


def test_get_positive_single_positive():
    """Test with a single positive number."""
    assert get_positive([5]) == [5]


def test_get_positive_single_negative():
    """Test with a single negative number."""
    assert get_positive([-5]) == []


def test_get_positive_single_zero():
    """Test with a single zero."""
    assert get_positive([0]) == []
