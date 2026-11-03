# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_sum_matches_first_branch():
    """All ints and x + y == z -> True (line 6)."""
    assert any_int(2, 3, 5) is True


def test_any_int_sum_matches_second_branch():
    """All ints and x + z == y -> True (line 6, second or-branch)."""
    assert any_int(5, 3, 2) is True


def test_any_int_sum_matches_third_branch():
    """All ints and y + z == x -> True (line 6, third or-branch)."""
    assert any_int(3, 5, 2) is True


def test_any_int_no_sum_matches():
    """All ints but no pair sums to the third -> False (line 7)."""
    assert any_int(2, 3, 4) is False


def test_any_int_negative_ints():
    """Negative ints are still ints; both outcomes covered."""
    assert any_int(-2, -3, -5) is True
    assert any_int(-2, -3, -4) is False


def test_any_int_non_int_argument():
    """Any non-int argument short-circuits to False (line 8)."""
    assert any_int(2.5, 3, 5) is False
    assert any_int(2, 3.5, 5) is False
    # 2 + 3 == 5.0 numerically, but 5.0 is not an int, so line 8 must run.
    assert any_int(2, 3, 5.0) is False
    assert any_int("2", 3, 5) is False
    assert any_int(None, 3, 5) is False
