# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

import pytest

from f107 import even_odd_palindrome


def test_even_odd_palindrome_single_digit():
    # n=1: only 1, which is an odd palindrome -> (0 even, 1 odd)
    assert even_odd_palindrome(1) == (0, 1)
    # n=2: 1 (odd palindrome), 2 (even palindrome) -> (1, 1)
    assert even_odd_palindrome(2) == (1, 1)


def test_even_odd_palindrome_all_single_digits():
    # n=9: even palindromes 2,4,6,8 -> 4; odd palindromes 1,3,5,7,9 -> 5
    assert even_odd_palindrome(9) == (4, 5)


def test_even_odd_palindrome_with_non_palindromes():
    # n=12: even palindromes 2,4,6,8 -> 4 (10 and 12 are not palindromes);
    # odd palindromes 1,3,5,7,9,11 -> 6
    assert even_odd_palindrome(12) == (4, 6)


def test_even_odd_palindrome_zero():
    # n=0: empty range, no iterations -> (0, 0)
    assert even_odd_palindrome(0) == (0, 0)


def test_even_odd_palindrome_multi_digit_palindromes():
    # n=22: even palindromes 2,4,6,8,22 -> 5; odd palindromes 1,3,5,7,9,11 -> 6
    assert even_odd_palindrome(22) == (5, 6)
