# file: script_40.py:1-23
# asked: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 23], [19, 18], [19, 20], [20, 19], [20, 21], [21, 20], [21, 22]]}
# gained: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 23], [19, 18], [19, 20], [20, 19], [20, 21], [21, 20], [21, 22]]}

import pytest
from script_40 import triples_sum_to_zero


def test_triples_sum_to_zero_empty_list():
    """Test with empty list - should return False without entering loops."""
    assert triples_sum_to_zero([]) == False


def test_triples_sum_to_zero_single_element():
    """Test with single element - should return False."""
    assert triples_sum_to_zero([1]) == False


def test_triples_sum_to_zero_two_elements():
    """Test with two elements - should return False."""
    assert triples_sum_to_zero([1, 2]) == False


def test_triples_sum_to_zero_three_elements_no_match():
    """Test with three elements that don't sum to zero."""
    assert triples_sum_to_zero([1, 2, 3]) == False


def test_triples_sum_to_zero_three_elements_match():
    """Test with three elements that sum to zero - triggers line 22."""
    assert triples_sum_to_zero([1, -1, 0]) == True


def test_triples_sum_to_zero_four_elements_no_match():
    """Test with four elements that don't sum to zero - executes all lines but returns False."""
    assert triples_sum_to_zero([1, 2, 3, 4]) == False


def test_triples_sum_to_zero_four_elements_match():
    """Test with four elements where a triple sums to zero."""
    assert triples_sum_to_zero([1, 2, -3, 4]) == True


def test_triples_sum_to_zero_negative_numbers():
    """Test with negative numbers that sum to zero."""
    assert triples_sum_to_zero([-1, -2, 3]) == True


def test_triples_sum_to_zero_with_zeros():
    """Test with multiple zeros."""
    assert triples_sum_to_zero([0, 0, 0]) == True


def test_triples_sum_to_zero_no_triple_exists():
    """Test where no triple sums to zero - exercises line 23."""
    assert triples_sum_to_zero([1, 3, 5, 7, 9]) == False


def test_triples_sum_to_zero_larger_list_with_match():
    """Test with larger list containing a triple that sums to zero."""
    assert triples_sum_to_zero([1, 2, 3, 4, 5, -6]) == True


def test_triples_sum_to_zero_larger_list_no_match():
    """Test with larger list with no triple summing to zero."""
    assert triples_sum_to_zero([1, 2, 4, 8, 16]) == False
