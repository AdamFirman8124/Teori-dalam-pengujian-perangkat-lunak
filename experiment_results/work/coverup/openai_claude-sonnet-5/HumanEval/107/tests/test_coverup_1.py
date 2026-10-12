# file: script_107.py:1-35
# asked: {"lines": [24, 25, 27, 28, 30, 31, 32, 33, 34, 35], "branches": [[30, 31], [30, 35], [31, 32], [31, 33], [33, 30], [33, 34]]}
# gained: {"lines": [24, 25, 27, 28, 30, 31, 32, 33, 34, 35], "branches": [[30, 31], [30, 35], [31, 32], [31, 33], [33, 30], [33, 34]]}

import pytest
from script_107 import even_odd_palindrome


def test_even_odd_palindrome_basic():
    """Test basic case with small n"""
    result = even_odd_palindrome(3)
    assert result == (1, 2)


def test_even_odd_palindrome_medium():
    """Test medium case"""
    result = even_odd_palindrome(12)
    assert result == (4, 6)


def test_even_odd_palindrome_single():
    """Test with n=1"""
    result = even_odd_palindrome(1)
    assert result == (0, 1)


def test_even_odd_palindrome_two():
    """Test with n=2 to cover even palindrome"""
    result = even_odd_palindrome(2)
    assert result == (1, 1)


def test_even_odd_palindrome_larger():
    """Test with larger n to cover more palindromes"""
    result = even_odd_palindrome(100)
    # Palindromes 1-100: 1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99
    # Even: 2,4,6,8,22,44,66,88 = 8
    # Odd: 1,3,5,7,9,11,33,55,77,99 = 10
    assert result == (8, 10)


def test_even_odd_palindrome_all_branches():
    """Test to ensure all branches are covered"""
    result = even_odd_palindrome(11)
    assert result == (4, 6)
    
    result = even_odd_palindrome(22)
    # Palindromes 1-22: 1,2,3,4,5,6,7,8,9,11,22
    # Even: 2,4,6,8,22 = 5
    # Odd: 1,3,5,7,9,11 = 6
    assert result == (5, 6)
