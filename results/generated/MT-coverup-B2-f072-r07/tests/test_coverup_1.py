# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

"""Tests for f072.will_it_fly, covering all previously missed lines 3-12
and every branch (overweight, non-palindrome, even/odd/empty palindromes).

will_it_fly is a pure function with no external state, so no monkeypatching
or fixture teardown is required; each test is fully self-contained.
"""

import pytest

from f072 import will_it_fly


@pytest.mark.parametrize(
    "q, w",
    [
        ([3, 2, 3], 5),   # sum(q) == 8 > 5
        ([1, 2, 3], 5),   # sum(q) == 6 > 5
    ],
)
def test_overweight_returns_false(q, w):
    """Lines 3-4: when the total weight exceeds w, the result is False."""
    assert will_it_fly(q, w) is False


def test_balanced_but_not_palindrome_returns_false():
    """Lines 6-9: weight is balanced but objects are asymmetric -> False."""
    assert will_it_fly([1, 2], 5) is False


def test_even_length_palindrome_returns_true():
    """Lines 7-12: balanced even-length palindrome -> True.

    Exercises the mismatch check evaluating False and both pointer
    updates (i += 1, j -= 1) before the loop terminates.
    """
    assert will_it_fly([1, 2, 2, 1], 10) is True


def test_odd_length_palindrome_returns_true():
    """Lines 10-11 with i == j at loop exit, then line 12 -> True."""
    assert will_it_fly([1, 2, 1], 5) is True


def test_empty_list_returns_true():
    """Lines 6-7: the while loop is never entered for an empty q -> True."""
    assert will_it_fly([], 5) is True


def test_single_object_at_exact_capacity_returns_true():
    """Boundary: sum(q) == w (not > w) and trivially palindromic -> True."""
    assert will_it_fly([5], 5) is True
