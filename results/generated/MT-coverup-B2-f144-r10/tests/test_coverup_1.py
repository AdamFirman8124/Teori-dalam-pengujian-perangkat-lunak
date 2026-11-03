# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

"""Tests for f144.simplify covering lines 3-9 (both branches of the if)."""

import pytest

from f144 import simplify


def test_simplify_true_when_product_is_whole_number():
    """Lines 3-8: valid fraction strings whose product is an integer -> True."""
    # 1/5 * 5/1 = 5/5 = 1 (whole number)
    assert simplify("1/5", "5/1") is True
    # 3/2 * 2/3 = 6/6 = 1 (whole number)
    assert simplify("3/2", "2/3") is True
    # 7/4 * 4/7 = 28/28 = 1 (whole number)
    assert simplify("7/4", "4/7") is True


def test_simplify_false_when_product_is_not_whole_number():
    """Lines 3-7 and 9: valid fraction strings whose product is not an integer -> False."""
    # 1/6 * 2/1 = 2/6 (not a whole number)
    assert simplify("1/6", "2/1") is False
    # 1/2 * 1/3 = 1/6 (not a whole number)
    assert simplify("1/2", "1/3") is False
    # 2/3 * 3/5 = 6/15 = 0.4 (not a whole number)
    assert simplify("2/3", "3/5") is False


def test_simplify_is_pure_no_state_pollution():
    """The function must not mutate its inputs or leave any global state behind."""
    x, n = "1/5", "5/1"
    result = simplify(x, n)
    # Inputs are unchanged (strings are immutable, but assert anyway for clarity)
    assert x == "1/5"
    assert n == "5/1"
    # Same inputs always yield the same output (deterministic, no side effects)
    assert simplify(x, n) is result is True
