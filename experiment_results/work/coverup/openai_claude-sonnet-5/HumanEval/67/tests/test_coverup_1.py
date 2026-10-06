# file: script_67.py:1-18
# asked: {"lines": [14, 15, 16, 17, 18], "branches": [[15, 16], [15, 18], [16, 15], [16, 17]]}
# gained: {"lines": [14, 15, 16, 17, 18], "branches": [[15, 16], [15, 18], [16, 15], [16, 17]]}

import pytest
from script_67 import fruit_distribution


def test_fruit_distribution_basic():
    """Test basic case with apples and oranges"""
    result = fruit_distribution("5 apples and 6 oranges", 19)
    assert result == 8


def test_fruit_distribution_with_zeros():
    """Test case with zero apples"""
    result = fruit_distribution("0 apples and 1 oranges", 3)
    assert result == 2


def test_fruit_distribution_large_numbers():
    """Test case with large numbers"""
    result = fruit_distribution("2 apples and 3 oranges", 100)
    assert result == 95


def test_fruit_distribution_large_apples():
    """Test case with 100 apples"""
    result = fruit_distribution("100 apples and 1 oranges", 120)
    assert result == 19


def test_fruit_distribution_single_digit():
    """Test case with single digit numbers"""
    result = fruit_distribution("1 apples and 2 oranges", 10)
    assert result == 7


def test_fruit_distribution_multi_digit():
    """Test case with multi-digit numbers"""
    result = fruit_distribution("25 apples and 35 oranges", 100)
    assert result == 40


def test_fruit_distribution_all_fruits_accounted():
    """Test case where apples and oranges equal total"""
    result = fruit_distribution("10 apples and 10 oranges", 20)
    assert result == 0


def test_fruit_distribution_no_mangos():
    """Test edge case with exact match"""
    result = fruit_distribution("50 apples and 50 oranges", 100)
    assert result == 0
