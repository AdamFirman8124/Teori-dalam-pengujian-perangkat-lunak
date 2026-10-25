# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

from f107 import even_odd_palindrome


def test_zero_no_loop_iterations():
    assert even_odd_palindrome(0) == (0, 0)


def test_single_odd_palindrome():
    assert even_odd_palindrome(1) == (0, 1)


def test_small_range_odd_and_even_palindromes():
    assert even_odd_palindrome(2) == (1, 1)
    assert even_odd_palindrome(3) == (1, 2)


def test_even_non_palindrome_branch():
    # 10 is even but not a palindrome, counts stay at single-digit totals
    assert even_odd_palindrome(10) == (4, 5)


def test_all_branches_including_two_digit_palindromes():
    # 11 is odd palindrome, 12 is even non-palindrome
    assert even_odd_palindrome(12) == (4, 6)
    # 13 is odd non-palindrome, counts unchanged from n=12
    assert even_odd_palindrome(13) == (4, 6)
    # 22 is even palindrome
    assert even_odd_palindrome(22) == (5, 6)
