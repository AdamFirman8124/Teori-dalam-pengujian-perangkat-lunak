# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

import pytest

from f107 import even_odd_palindrome


def test_even_odd_palindrome_basic():
    """Covers odd-palindrome branch, even-palindrome branch, and non-palindrome skip."""
    # 1..10: odd palindromes are 1,3,5,7,9 -> 5; even palindromes are 2,4,6,8 -> 4; 10 is not a palindrome.
    assert even_odd_palindrome(10) == (4, 5)


def test_even_odd_palindrome_includes_two_digit_palindrome():
    """Ensures the elif branch and the is_palindrome check on multi-digit numbers are exercised."""
    # 1..12: odd palindromes 1,3,5,7,9,11 -> 6; even palindromes 2,4,6,8 -> 4; 10 and 12 are not palindromes.
    assert even_odd_palindrome(12) == (4, 6)


def test_even_odd_palindrome_single_element():
    """Covers the loop body executing exactly once with an odd palindrome."""
    assert even_odd_palindrome(1) == (0, 1)
    assert even_odd_palindrome(2) == (1, 1)


def test_even_odd_palindrome_empty_range():
    """Covers the case where the loop body never executes (n <= 0)."""
    assert even_odd_palindrome(0) == (0, 0)
    assert even_odd_palindrome(-5) == (0, 0)


def test_even_odd_palindrome_larger_value():
    """Sanity check on a larger input to confirm counting stays consistent."""
    # 1..100: odd palindromes: 1,3,5,7,9 (5) + 11,33,55,77,99 (5) = 10
    # even palindromes: 2,4,6,8 (4) + 22,44,66,88 (4) = 8
    assert even_odd_palindrome(100) == (8, 10)
