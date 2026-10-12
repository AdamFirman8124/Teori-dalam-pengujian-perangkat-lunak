# file: script_122.py:1-15
# asked: {"lines": [15], "branches": []}
# gained: {"lines": [15], "branches": []}

import pytest
from script_122 import add_elements


def test_add_elements_basic():
    """Test basic example from docstring."""
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    result = add_elements(arr, k)
    assert result == 24  # 21 + 3


def test_add_elements_all_single_digit():
    """Test with all single digit numbers."""
    arr = [1, 2, 3, 4, 5]
    k = 5
    result = add_elements(arr, k)
    assert result == 15  # 1 + 2 + 3 + 4 + 5


def test_add_elements_all_three_digit():
    """Test with all three digit numbers."""
    arr = [111, 222, 333, 444]
    k = 4
    result = add_elements(arr, k)
    assert result == 0  # No elements with at most two digits


def test_add_elements_mixed_two_digit():
    """Test with mixed single and two digit numbers."""
    arr = [10, 20, 30, 99, 100]
    k = 4
    result = add_elements(arr, k)
    assert result == 159  # 10 + 20 + 30 + 99


def test_add_elements_k_less_than_length():
    """Test with k less than array length."""
    arr = [1, 2, 3, 100, 200, 300]
    k = 3
    result = add_elements(arr, k)
    assert result == 6  # 1 + 2 + 3


def test_add_elements_negative_single_digit():
    """Test with negative single digit numbers."""
    arr = [-1, -2, -3, -4, 5]
    k = 5
    result = add_elements(arr, k)
    assert result == -5  # -1 + -2 + -3 + -4 + 5


def test_add_elements_negative_two_digit():
    """Test with negative two digit numbers - str includes minus sign."""
    arr = [-1, -2, -9, 100]
    k = 3
    result = add_elements(arr, k)
    assert result == -12  # -1 + -2 + -9 (each str is 2 chars)


def test_add_elements_negative_three_digit():
    """Test with negative three digit numbers."""
    arr = [-100, -200, -300]
    k = 3
    result = add_elements(arr, k)
    assert result == 0  # No elements with at most two digits (str has 4 chars including '-')


def test_add_elements_zero():
    """Test with zero."""
    arr = [0, 1, 2, 3]
    k = 4
    result = add_elements(arr, k)
    assert result == 6  # 0 + 1 + 2 + 3


def test_add_elements_k_equals_one():
    """Test with k equals 1."""
    arr = [5, 100, 200]
    k = 1
    result = add_elements(arr, k)
    assert result == 5


def test_add_elements_large_numbers():
    """Test with very large numbers."""
    arr = [10000, 1, 2, 3]
    k = 4
    result = add_elements(arr, k)
    assert result == 6  # 1 + 2 + 3
