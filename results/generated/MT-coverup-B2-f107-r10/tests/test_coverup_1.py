# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

"""Tests for f107.even_odd_palindrome covering all lines and branches."""

from f107 import even_odd_palindrome


def test_single_odd_palindrome():
    # n=1: only i=1, which is odd and a palindrome -> (even=0, odd=1)
    assert even_odd_palindrome(1) == (0, 1)


def test_single_even_palindrome():
    # n=2: i=1 (odd palindrome), i=2 (even palindrome) -> (1, 1)
    assert even_odd_palindrome(2) == (1, 1)


def test_mixed_palindromes_and_non_palindromes():
    # n=12: palindromes are 1..9 and 11.
    # odd palindromes: 1,3,5,7,9,11 -> 6 ; even palindromes: 2,4,6,8 -> 4
    # i=10 exercises the "even but not palindrome" branch.
    assert even_odd_palindrome(12) == (4, 6)


def test_all_branches_including_odd_non_palindrome():
    # n=22 covers every branch:
    #   - odd palindrome (e.g. 1, 11) -> odd count incremented
    #   - even palindrome (e.g. 2, 22) -> even count incremented
    #   - odd non-palindrome (e.g. 13, 21): first condition's palindrome
    #     check fails, elif not taken
    #   - even non-palindrome (e.g. 10, 12): elif's palindrome check fails
    # Palindromes 1..22: 1,2,3,4,5,6,7,8,9,11,22
    # odd: 1,3,5,7,9,11 -> 6 ; even: 2,4,6,8,22 -> 5
    assert even_odd_palindrome(22) == (5, 6)


def test_zero_range_loop_not_entered():
    # n=0: range(1, 1) is empty, loop body never runs -> (0, 0)
    assert even_odd_palindrome(0) == (0, 0)


def test_result_is_tuple_of_ints():
    result = even_odd_palindrome(5)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
    # Palindromes 1..5: 1,2,3,4,5 -> odd: 1,3,5 (3), even: 2,4 (2)
    assert result == (2, 3)
