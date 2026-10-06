# file: script_69.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest
from script_69 import search


def test_search_basic_case():
    """Test basic case where 2 appears twice"""
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_valid():
    """Test case where multiple integers satisfy condition, returns greatest"""
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_valid():
    """Test case where no integer satisfies condition"""
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element():
    """Test single element equal to 1"""
    assert search([1]) == 1


def test_search_single_element_greater_than_one():
    """Test single element greater than 1, should return -1"""
    assert search([5]) == -1


def test_search_all_same_valid():
    """Test all elements same and frequency >= value"""
    assert search([2, 2, 2]) == 2


def test_search_all_same_invalid():
    """Test all elements same but frequency < value"""
    assert search([5, 5]) == -1


def test_search_one_appears_once():
    """Test edge case where 1 appears once"""
    assert search([1, 5, 6, 7]) == 1


def test_search_large_numbers_low_frequency():
    """Test large numbers with low frequency"""
    assert search([10, 20, 30]) == -1


def test_search_multiple_ones():
    """Test multiple 1s"""
    assert search([1, 1, 1, 1]) == 1


def test_search_sequential():
    """Test sequential numbers"""
    assert search([1, 2, 2, 3, 3, 3]) == 3


def test_search_two_valid_candidates():
    """Test two valid candidates, should return the greater"""
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
