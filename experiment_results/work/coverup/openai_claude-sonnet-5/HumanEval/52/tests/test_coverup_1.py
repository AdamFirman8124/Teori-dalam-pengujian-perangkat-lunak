# file: script_52.py:1-11
# asked: {"lines": [8, 9, 10, 11], "branches": [[8, 9], [8, 11], [9, 8], [9, 10]]}
# gained: {"lines": [8, 9, 10, 11], "branches": [[8, 9], [8, 11], [9, 8], [9, 10]]}

import pytest
from script_52 import below_threshold


def test_below_threshold_all_below():
    """Test when all elements are below the threshold."""
    assert below_threshold([1, 2, 4, 10], 100) is True


def test_below_threshold_one_above():
    """Test when at least one element is at or above the threshold."""
    assert below_threshold([1, 20, 4, 10], 5) is False


def test_below_threshold_equal_to_threshold():
    """Test when an element equals the threshold."""
    assert below_threshold([1, 2, 5, 10], 5) is False


def test_below_threshold_empty_list():
    """Test with an empty list - should return True."""
    assert below_threshold([], 10) is True


def test_below_threshold_single_element_below():
    """Test with a single element below threshold."""
    assert below_threshold([5], 10) is True


def test_below_threshold_single_element_above():
    """Test with a single element at or above threshold."""
    assert below_threshold([10], 10) is False


def test_below_threshold_negative_numbers():
    """Test with negative numbers."""
    assert below_threshold([-5, -10, -1], 0) is True
    assert below_threshold([-5, 0, -1], 0) is False
