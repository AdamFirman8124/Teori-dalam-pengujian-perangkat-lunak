# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

import pytest

from f107 import even_odd_palindrome


def test_single_odd_palindrome():
    """n=1: only candidate is 1, an odd palindrome -> (0, 1)."""
    assert even_odd_palindrome(1) == (0, 1)


def test_even_palindrome_branch():
    """n=2: 1 is an odd palindrome, 2 is an even palindrome -> (1, 1)."""
    assert even_odd_palindrome(2) == (1, 1)


def test_even_non_palindrome_branch():
    """n=10: 10 is an even non-palindrome, so counts stay at (4, 5)."""
    assert even_odd_palindrome(10) == (4, 5)


def test_odd_non_palindrome_branch():
    """n=15: 15 is an odd non-palindrome; 11 (odd palindrome) is included,
    so counts are (4, 6)."""
    assert even_odd_palindrome(15) == (4, 6)


def test_two_digit_palindromes():
    """n=22: 11 is an odd palindrome, 22 is an even palindrome -> (5, 6)."""
    assert even_odd_palindrome(22) == (5, 6)


def test_empty_range():
    """n=0: loop body never executes -> (0, 0)."""
    assert even_odd_palindrome(0) == (0, 0)


def test_all_branches_combined():
    """n=100 exercises every branch: odd/even palindromes and non-palindromes.

    Palindromes in 1..100:
    - 1..9: 1,3,5,7,9 odd (5) and 2,4,6,8 even (4)
    - 11,22,...,99: 11,33,55,77,99 odd (5) and 22,44,66,88 even (4)
    - 100 is not a palindrome ("100" != "001")
    Totals: 8 even, 10 odd.
    """
    result = even_odd_palindrome(100)
    assert result == (8, 10)
    even_count, odd_count = result
    assert even_count == 8
    assert odd_count == 10
