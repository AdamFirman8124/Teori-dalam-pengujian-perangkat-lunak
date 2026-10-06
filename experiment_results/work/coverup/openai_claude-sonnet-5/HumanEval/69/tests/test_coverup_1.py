# file: script_69.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest
from script_69 import search


def test_search_basic_example():
    """Test basic example from docstring"""
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_valid():
    """Test case where multiple integers satisfy the condition"""
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_valid():
    """Test case where no integer satisfies the condition"""
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_valid():
    """Test single element that satisfies condition"""
    assert search([1]) == 1


def test_search_single_element_invalid():
    """Test single element that does not satisfy condition"""
    assert search([2]) == -1


def test_search_all_same_valid():
    """Test all same elements that satisfy condition"""
    assert search([3, 3, 3]) == 3


def test_search_all_same_invalid():
    """Test all same elements that do not satisfy condition"""
    assert search([5, 5, 5]) == -1


def test_search_exact_frequency_match():
    """Test where frequency exactly matches the value"""
    assert search([2, 2]) == 2


def test_search_frequency_greater_than_value():
    """Test where frequency is greater than the value"""
    assert search([1, 1, 1, 1]) == 1


def test_search_large_numbers():
    """Test with larger numbers"""
    assert search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10


def test_search_mixed_valid_and_invalid():
    """Test mix of valid and invalid values, should return greatest valid"""
    assert search([1, 2, 2, 5, 5]) == 2
