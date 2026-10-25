# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

from f107 import even_odd_palindrome


def test_n_zero_no_iterations():
    assert even_odd_palindrome(0) == (0, 0)


def test_n_one_odd_palindrome_only():
    assert even_odd_palindrome(1) == (0, 1)


def test_n_three_covers_single_digit():
    # 1 odd-pal, 2 even-pal, 3 odd-pal
    assert even_odd_palindrome(3) == (1, 2)


def test_even_non_palindrome_branch():
    # 10 is even non-palindrome, counts unchanged from n=9
    assert even_odd_palindrome(9) == (4, 5)
    assert even_odd_palindrome(10) == (4, 5)
    # 12 is even non-palindrome
    assert even_odd_palindrome(12) == (4, 6)


def test_odd_palindrome_multi_digit():
    # 11 is odd multi-digit palindrome
    assert even_odd_palindrome(11) == (4, 6)


def test_odd_non_palindrome_branch():
    # 13 is the first odd non-palindrome, counts unchanged from n=12
    assert even_odd_palindrome(13) == (4, 6)


def test_even_palindrome_multi_digit():
    # 22 is even multi-digit palindrome
    assert even_odd_palindrome(22) == (5, 6)


def test_negative_no_iterations():
    assert even_odd_palindrome(-5) == (0, 0)
