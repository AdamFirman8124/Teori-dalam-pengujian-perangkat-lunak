# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

from f107 import even_odd_palindrome


def test_even_odd_palindrome_counts_palindromes_and_skips_non_palindromes():
    assert even_odd_palindrome(22) == (5, 6)


def test_even_odd_palindrome_with_empty_range():
    assert even_odd_palindrome(0) == (0, 0)
