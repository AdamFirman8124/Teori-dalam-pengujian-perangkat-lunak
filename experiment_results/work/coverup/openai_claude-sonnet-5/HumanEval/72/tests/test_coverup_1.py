# file: script_72.py:1-28
# asked: {"lines": [19, 20, 22, 23, 24, 25, 26, 27, 28], "branches": [[19, 20], [19, 22], [23, 24], [23, 28], [24, 25], [24, 26]]}
# gained: {"lines": [19, 20, 22, 23, 24, 25, 26, 27, 28], "branches": [[19, 20], [19, 22], [23, 24], [23, 28], [24, 25], [24, 26]]}

import pytest
from script_72 import will_it_fly


def test_will_it_fly_balanced_within_weight():
    """Test a balanced list where sum is within weight limit."""
    assert will_it_fly([3, 2, 3], 9) == True


def test_will_it_fly_unbalanced():
    """Test an unbalanced list."""
    assert will_it_fly([1, 2], 5) == False


def test_will_it_fly_balanced_exceeds_weight():
    """Test a balanced list where sum exceeds weight limit."""
    assert will_it_fly([3, 2, 3], 1) == False


def test_will_it_fly_single_element_within_weight():
    """Test a single element within weight limit."""
    assert will_it_fly([3], 5) == True


def test_will_it_fly_single_element_exceeds_weight():
    """Test a single element that exceeds weight limit."""
    assert will_it_fly([10], 5) == False


def test_will_it_fly_empty_list():
    """Test an empty list."""
    assert will_it_fly([], 10) == True


def test_will_it_fly_sum_equals_weight():
    """Test when sum equals exactly the weight limit."""
    assert will_it_fly([2, 1, 2], 5) == True


def test_will_it_fly_two_element_palindrome_within_weight():
    """Test a two-element palindrome within weight."""
    assert will_it_fly([5, 5], 20) == True


def test_will_it_fly_two_element_not_palindrome():
    """Test a two-element list that is not a palindrome."""
    assert will_it_fly([5, 3], 20) == False


def test_will_it_fly_long_palindrome_within_weight():
    """Test a longer palindrome within weight."""
    assert will_it_fly([1, 2, 3, 2, 1], 10) == True


def test_will_it_fly_long_palindrome_exceeds_weight():
    """Test a longer palindrome that exceeds weight."""
    assert will_it_fly([1, 2, 3, 2, 1], 5) == False


def test_will_it_fly_long_not_palindrome():
    """Test a longer list that is not a palindrome."""
    assert will_it_fly([1, 2, 3, 4, 5], 20) == False
