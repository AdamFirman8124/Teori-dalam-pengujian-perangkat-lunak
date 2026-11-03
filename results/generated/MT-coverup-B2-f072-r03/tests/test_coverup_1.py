# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_too_heavy_returns_false():
    """Covers lines 3-4: sum(q) > w branch."""
    # sum([3, 2, 3]) == 8 > 1, so it cannot fly even though it is a palindrome.
    assert will_it_fly([3, 2, 3], 1) is False


def test_not_palindrome_returns_false():
    """Covers lines 6-9: loop entered and mismatch branch taken."""
    # sum([1, 2]) == 3 <= 5, but [1, 2] is not a palindrome.
    assert will_it_fly([1, 2], 5) is False


def test_palindrome_within_weight_returns_true():
    """Covers lines 6-7, 10-12: loop iterates (i += 1, j -= 1) and returns True."""
    # sum([3, 2, 3]) == 8 <= 9 and [3, 2, 3] is a palindrome.
    assert will_it_fly([3, 2, 3], 9) is True


def test_single_element_returns_true():
    """Covers line 12: loop body never entered (i == j)."""
    # sum([3]) == 3 <= 5 and a single element is trivially a palindrome.
    assert will_it_fly([3], 5) is True


def test_empty_list_returns_true():
    """Covers line 12: loop body never entered (i > j for empty list)."""
    # sum([]) == 0 <= 5 and an empty list is trivially a palindrome.
    assert will_it_fly([], 5) is True


def test_even_length_palindrome_returns_true():
    """Covers lines 10-11 for an even-length list: pointers cross exactly."""
    # sum([1, 2, 2, 1]) == 6 <= 6 and [1, 2, 2, 1] is a palindrome.
    assert will_it_fly([1, 2, 2, 1], 6) is True


def test_exact_weight_boundary_returns_true():
    """Covers line 3 false branch at the exact boundary sum(q) == w."""
    # sum([2, 3]) == 5 == w, not greater, and [2, 3] is not a palindrome -> False
    # via the palindrome check, exercising both boundary and mismatch logic.
    assert will_it_fly([2, 3], 5) is False
    assert will_it_fly([5], 5) is True
