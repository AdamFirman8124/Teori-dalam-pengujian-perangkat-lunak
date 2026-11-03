# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

"""Tests for f107.even_odd_palindrome.

The function under test is pure (no I/O, no global state, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test leaves
no residual state behind.
"""

from f107 import even_odd_palindrome


def test_counts_palindromes_up_to_twelve():
    """Covers: odd palindromes (1, 3, 5, 7, 9, 11), even palindromes
    (2, 4, 6, 8), and even non-palindromes (10, 12)."""
    assert even_odd_palindrome(12) == (4, 6)


def test_counts_palindromes_up_to_twenty():
    """Covers the branch where i is odd but NOT a palindrome (13, 15, 17, 19),
    so both the 'if' and 'elif' conditions evaluate to False and neither
    counter is incremented for those values."""
    assert even_odd_palindrome(20) == (4, 6)


def test_single_element_range():
    """Covers the loop body executing exactly once with an odd palindrome."""
    assert even_odd_palindrome(1) == (0, 1)


def test_two():
    """Covers one odd palindrome and one even palindrome."""
    assert even_odd_palindrome(2) == (1, 1)


def test_empty_range():
    """Edge case: n = 0 makes the loop body never execute."""
    assert even_odd_palindrome(0) == (0, 0)


def test_result_is_tuple_of_non_negative_ints():
    """Postcondition: the result is always a 2-tuple of non-negative ints."""
    result = even_odd_palindrome(15)
    assert isinstance(result, tuple) and len(result) == 2
    even_count, odd_count = result
    assert isinstance(even_count, int) and even_count >= 0
    assert isinstance(odd_count, int) and odd_count >= 0
    # Independent recomputation for n = 15:
    # even palindromes: 2, 4, 6, 8 -> 4
    # odd palindromes: 1, 3, 5, 7, 9, 11 -> 6
    assert result == (4, 6)
