# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_sum_matches_z():
    """All ints and x + y == z -> True (covers lines 4, 5, 6)."""
    assert any_int(2, 3, 5) is True


def test_any_int_sum_matches_y():
    """All ints and x + z == y -> True (covers second branch of line 5)."""
    assert any_int(2, 7, 5) is True


def test_any_int_sum_matches_x():
    """All ints and y + z == x -> True (covers third branch of line 5)."""
    assert any_int(7, 2, 5) is True


def test_any_int_no_match_returns_false():
    """All ints but no pair sums to the third -> False (covers line 7)."""
    assert any_int(1, 2, 4) is False


def test_any_int_non_int_returns_false():
    """Non-int argument short-circuits the isinstance check -> False (covers line 8)."""
    assert any_int(1.5, 2, 3) is False
    assert any_int(1, "2", 3) is False
    assert any_int(1, 2, None) is False


def test_any_int_negative_and_zero():
    """Edge cases with negatives and zero still satisfy the sum condition."""
    assert any_int(-1, 1, 0) is True
    assert any_int(0, 0, 0) is True
    assert any_int(-1, -2, -3) is True
    assert any_int(-1, -2, 0) is False
