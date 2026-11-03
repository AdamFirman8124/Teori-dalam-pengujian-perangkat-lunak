# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_weight_exceeded_returns_false():
    """sum(q) > w triggers the early False return (lines 3-4)."""
    assert will_it_fly([3, 2, 3], 5) is False


def test_weight_boundary_returns_true():
    """sum(q) == w does not trigger the early return; palindrome flies."""
    assert will_it_fly([1, 2, 1], 4) is True


def test_palindrome_within_weight_returns_true():
    """Odd-length palindrome exercises loop body and final True (lines 6-12)."""
    assert will_it_fly([3, 2, 3], 9) is True


def test_even_length_palindrome_returns_true():
    """Even-length palindrome requires multiple loop iterations (lines 10-11)."""
    assert will_it_fly([1, 2, 2, 1], 10) is True


def test_non_palindrome_returns_false():
    """Asymmetric list triggers the mid-loop False return (lines 8-9)."""
    assert will_it_fly([1, 2], 10) is False


def test_non_palindrome_longer_returns_false():
    """Mismatch found after a matching pair; loop body runs then exits False."""
    assert will_it_fly([1, 2, 3, 2, 4], 100) is False


def test_single_element_returns_true():
    """Loop body never runs when i == j (line 7 condition false)."""
    assert will_it_fly([5], 5) is True


def test_empty_list_returns_true():
    """Empty list: sum is 0, loop is skipped, returns True."""
    assert will_it_fly([], 0) is True
