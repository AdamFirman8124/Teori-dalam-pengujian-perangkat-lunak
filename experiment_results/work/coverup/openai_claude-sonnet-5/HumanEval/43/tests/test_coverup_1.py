# file: script_43.py:1-21
# asked: {"lines": [17, 18, 19, 20, 21], "branches": [[17, 18], [17, 21], [18, 17], [18, 19], [19, 18], [19, 20]]}
# gained: {"lines": [17, 18, 19, 20, 21], "branches": [[17, 18], [17, 21], [18, 17], [18, 19], [19, 18], [19, 20]]}

import pytest
from script_43 import pairs_sum_to_zero


def test_pairs_sum_to_zero_with_pair():
    """Test that function returns True when there are two elements that sum to zero."""
    assert pairs_sum_to_zero([1, -1, 2, 3]) == True


def test_pairs_sum_to_zero_with_multiple_pairs():
    """Test that function returns True when there are multiple pairs that sum to zero."""
    assert pairs_sum_to_zero([5, -5, 3, -3, 0]) == True


def test_pairs_sum_to_zero_no_pair():
    """Test that function returns False when no two elements sum to zero."""
    assert pairs_sum_to_zero([1, 2, 3, 4]) == False


def test_pairs_sum_to_zero_empty_list():
    """Test that function returns False for an empty list."""
    assert pairs_sum_to_zero([]) == False


def test_pairs_sum_to_zero_single_element():
    """Test that function returns False for a single element list."""
    assert pairs_sum_to_zero([5]) == False


def test_pairs_sum_to_zero_with_zeros():
    """Test that function returns True when there are two zeros (distinct positions)."""
    assert pairs_sum_to_zero([0, 0]) == True


def test_pairs_sum_to_zero_pair_at_end():
    """Test that function returns True when the pair is at the end of the list."""
    assert pairs_sum_to_zero([1, 2, 3, 7, -7]) == True
