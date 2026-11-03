# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_sum_exceeds_weight_returns_false():
    """Covers lines 3-4: sum(q) > w short-circuits to False."""
    assert will_it_fly([3, 2, 3], 1) is False


def test_single_element_exceeding_weight_returns_false():
    """Covers lines 3-4 with a single-element list."""
    assert will_it_fly([5], 4) is False


def test_palindromic_odd_length_within_weight_returns_true():
    """Covers lines 6-7, 10-12: odd-length palindrome, loop runs once."""
    assert will_it_fly([3, 2, 3], 9) is True


def test_palindromic_even_length_within_weight_returns_true():
    """Covers lines 6-7, 10-12: even-length palindrome, loop runs twice."""
    assert will_it_fly([1, 2, 2, 1], 10) is True


def test_non_palindromic_within_weight_returns_false():
    """Covers lines 6-9: mismatch found inside the loop."""
    assert will_it_fly([1, 2], 5) is False


def test_empty_list_returns_true():
    """Covers lines 6-7, 12: empty list, loop body never runs."""
    assert will_it_fly([], 0) is True


def test_single_element_within_weight_returns_true():
    """Covers lines 6-7, 12: single element, i == j so loop never runs."""
    assert will_it_fly([5], 5) is True


def test_boundary_sum_equals_weight_is_allowed():
    """sum(q) == w is not greater than w, so a palindrome still flies."""
    assert will_it_fly([2, 3, 2], 7) is True
