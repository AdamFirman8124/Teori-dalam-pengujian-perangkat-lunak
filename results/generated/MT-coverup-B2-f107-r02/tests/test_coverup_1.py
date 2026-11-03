# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

import pytest

from f107 import even_odd_palindrome


def test_even_odd_palindrome_single_odd():
    # n=1: only 1 is checked; it is an odd palindrome -> covers loop entry,
    # the odd-palindrome branch, and the return.
    assert even_odd_palindrome(1) == (0, 1)


def test_even_odd_palindrome_both_branches():
    # n=3 covers 1 (odd palindrome), 2 (even palindrome), 3 (odd palindrome),
    # exercising both the odd and even counting branches.
    assert even_odd_palindrome(3) == (1, 2)


def test_even_odd_palindrome_non_palindrome_branches():
    # n=10 includes 10 (even, not a palindrome), so both "short-circuit" cases
    # of the if/elif conditions are exercised (false outcomes of the branches).
    assert even_odd_palindrome(10) == (4, 5)


def test_even_odd_palindrome_multi_digit():
    # n=12 includes 10 (even, not a palindrome) and 11 (odd palindrome),
    # covering all branch outcomes of the loop body.
    assert even_odd_palindrome(12) == (4, 6)


def test_even_odd_palindrome_zero():
    # n=0: the loop body never executes; covers initialization lines and
    # the return statement with counts still zero.
    assert even_odd_palindrome(0) == (0, 0)
