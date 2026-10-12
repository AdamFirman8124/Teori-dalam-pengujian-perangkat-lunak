# file: script_120.py:1-30
# asked: {"lines": [26, 27, 28, 29, 30], "branches": [[26, 27], [26, 28]]}
# gained: {"lines": [26, 27, 28, 29, 30], "branches": [[26, 27], [26, 28]]}

import pytest
from script_120 import maximum


def test_maximum_basic():
    """Test basic functionality with mixed numbers."""
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
    assert maximum([4, -4, 4], 2) == [4, 4]
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]


def test_maximum_k_zero():
    """Test when k is 0, should return empty list."""
    assert maximum([1, 2, 3, 4, 5], 0) == []
    assert maximum([-10, -5, 0, 5, 10], 0) == []
    assert maximum([100], 0) == []


def test_maximum_k_equals_length():
    """Test when k equals array length."""
    assert maximum([3, 1, 2], 3) == [1, 2, 3]
    assert maximum([5], 1) == [5]


def test_maximum_negative_numbers():
    """Test with all negative numbers."""
    assert maximum([-5, -2, -8, -1], 2) == [-2, -1]


def test_maximum_positive_numbers():
    """Test with all positive numbers."""
    assert maximum([5, 2, 8, 1], 2) == [5, 8]


def test_maximum_duplicates():
    """Test with duplicate values."""
    assert maximum([1, 1, 1, 1], 2) == [1, 1]
    assert maximum([5, 3, 5, 3, 5], 3) == [5, 5, 5]


def test_maximum_single_element():
    """Test with single element array."""
    assert maximum([42], 1) == [42]
    assert maximum([-7], 1) == [-7]
