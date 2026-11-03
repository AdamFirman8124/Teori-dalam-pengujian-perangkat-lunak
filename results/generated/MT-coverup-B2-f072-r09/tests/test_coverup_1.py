# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

import pytest

from f072 import will_it_fly


def test_will_it_fly_too_heavy_returns_false():
    """Covers lines 3-4: sum(q) > w -> False, loop never entered."""
    assert will_it_fly([3, 2, 3], 1) is False
    assert will_it_fly([1, 2], 2) is False


def test_will_it_fly_not_palindrome_returns_false():
    """Covers lines 6-9: sum(q) <= w but q[i] != q[j] -> False."""
    assert will_it_fly([1, 2], 5) is False
    assert will_it_fly([1, 2, 3, 4], 100) is False


def test_will_it_fly_palindrome_returns_true():
    """Covers lines 6-7 and 10-12: palindromic q with sum(q) <= w -> True."""
    assert will_it_fly([3, 2, 3], 9) is True
    assert will_it_fly([1, 2, 1], 4) is True


def test_will_it_fly_single_element_returns_true():
    """Covers line 12 via while-condition false on first check (i == j)."""
    assert will_it_fly([3], 5) is True


def test_will_it_fly_empty_list_returns_true():
    """Covers line 12 with empty q: sum is 0, loop never entered."""
    assert will_it_fly([], 0) is True


def test_will_it_fly_exact_weight_boundary():
    """Boundary: sum(q) == w is allowed (not greater), palindrome -> True."""
    assert will_it_fly([2, 3, 2], 7) is True
