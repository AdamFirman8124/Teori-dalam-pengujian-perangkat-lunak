# file: project/f107/__init__.py:1-14
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14], "branches": [[9, 10], [9, 14], [10, 11], [10, 12], [12, 9], [12, 13]]}

import pytest

from f107 import even_odd_palindrome


def test_even_odd_palindrome_n_zero():
    """n=0: loop body never executes; both counts stay 0."""
    assert even_odd_palindrome(0) == (0, 0)


def test_even_odd_palindrome_n_one():
    """n=1: only an odd palindrome (1) is counted."""
    assert even_odd_palindrome(1) == (0, 1)


def test_even_odd_palindrome_n_two():
    """n=2: one even palindrome (2) and one odd palindrome (1)."""
    assert even_odd_palindrome(2) == (1, 1)


def test_even_odd_palindrome_single_digits():
    """n=9: every single digit is a palindrome; 4 even, 5 odd."""
    assert even_odd_palindrome(9) == (4, 5)


def test_even_odd_palindrome_mixed_branches():
    """n=12 exercises all branches: odd pal (11), even pal (2,4,6,8),
    odd non-pal (10), even non-pal (12)."""
    assert even_odd_palindrome(12) == (4, 6)


def test_even_odd_palindrome_multi_digit():
    """n=22: adds even palindrome 22; odd palindromes 1,3,5,7,9,11."""
    assert even_odd_palindrome(22) == (5, 6)


def test_even_odd_palindrome_negative_n():
    """n<0: range is empty, so both counts remain 0."""
    assert even_odd_palindrome(-5) == (0, 0)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, (0, 0)),
        (1, (0, 1)),
        (2, (1, 1)),
        (9, (4, 5)),
        (10, (4, 5)),
        (11, (4, 6)),
        (12, (4, 6)),
        (22, (5, 6)),
        # Up to 100: even pals 2,4,6,8,22,44,66,88 -> 8;
        # odd pals 1,3,5,7,9,11,33,55,77,99 -> 10 (100 is not a palindrome).
        (100, (8, 10)),
    ],
)
def test_even_odd_palindrome_parametrized(n, expected):
    assert even_odd_palindrome(n) == expected
