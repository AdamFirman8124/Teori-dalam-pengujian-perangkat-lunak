# file: script_72.py:1-28
# asked: {"lines": [19, 20, 22, 23, 24, 25, 26, 27, 28], "branches": [[19, 20], [19, 22], [23, 24], [23, 28], [24, 25], [24, 26]]}
# gained: {"lines": [19, 20, 22, 23, 24, 25, 26, 27, 28], "branches": [[19, 20], [19, 22], [23, 24], [23, 28], [24, 25], [24, 26]]}

import pytest
from script_72 import will_it_fly


def test_will_it_fly_unbalanced_under_weight():
    """Test case where sum is under weight but list is unbalanced"""
    assert will_it_fly([1, 2], 5) == False


def test_will_it_fly_balanced_over_weight():
    """Test case where list is balanced but sum exceeds weight"""
    assert will_it_fly([3, 2, 3], 1) == False


def test_will_it_fly_balanced_under_weight():
    """Test case where list is balanced and sum is under weight"""
    assert will_it_fly([3, 2, 3], 9) == True


def test_will_it_fly_single_element():
    """Test case with single element (always balanced)"""
    assert will_it_fly([3], 5) == True


def test_will_it_fly_empty_list():
    """Test case with empty list (should be balanced and sum is 0)"""
    assert will_it_fly([], 0) == True
    assert will_it_fly([], 10) == True


def test_will_it_fly_balanced_exactly_at_weight():
    """Test case where sum exactly equals the weight"""
    assert will_it_fly([2, 1, 2], 5) == True


def test_will_it_fly_sum_exceeds_weight_early_return():
    """Test case where sum exceeds weight (lines 19-20)"""
    assert will_it_fly([10, 20, 10], 30) == False


def test_will_it_fly_unbalanced_multi_element():
    """Test case with unbalanced multi-element list (lines 24-25)"""
    assert will_it_fly([1, 2, 3], 10) == False


def test_will_it_fly_balanced_even_length():
    """Test case with balanced even-length list"""
    assert will_it_fly([1, 2, 2, 1], 10) == True


def test_will_it_fly_balanced_odd_length():
    """Test case with balanced odd-length list"""
    assert will_it_fly([5, 3, 5], 20) == True
