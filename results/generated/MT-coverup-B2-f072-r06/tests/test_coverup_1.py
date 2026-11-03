# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_will_it_fly_weight_too_high():
    """sum(q) > w -> returns False (covers lines 3-4)."""
    assert will_it_fly([3, 2, 3], 7) is False


def test_will_it_fly_not_palindrome():
    """sum(q) <= w but q is not a palindrome -> returns False (covers lines 6-9)."""
    assert will_it_fly([1, 2], 5) is False


def test_will_it_fly_palindrome():
    """sum(q) <= w and q is a palindrome -> returns True (covers lines 6-12,
    including loop body lines 10-11 and the final return on line 12)."""
    assert will_it_fly([3, 2, 3], 9) is True


def test_will_it_fly_even_length_palindrome():
    """Even-length palindrome exercises multiple loop iterations before i >= j."""
    assert will_it_fly([1, 2, 2, 1], 6) is True


def test_will_it_fly_single_element():
    """Single element: while loop body never runs (i == j), returns True."""
    assert will_it_fly([5], 5) is True


def test_will_it_fly_empty_list():
    """Empty list: sum is 0, loop never runs, returns True."""
    assert will_it_fly([], 0) is True
