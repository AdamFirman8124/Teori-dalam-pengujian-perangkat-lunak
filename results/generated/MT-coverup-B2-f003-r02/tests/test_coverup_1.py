# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest

from f003 import below_zero


def test_below_zero_goes_negative_returns_true():
    """Balance dips below zero mid-sequence -> True (covers lines 6-11)."""
    assert below_zero([1, 2, -5]) is True


def test_below_zero_first_op_negative_returns_true():
    """Very first operation drives balance negative -> True."""
    assert below_zero([-1]) is True


def test_below_zero_never_negative_returns_false():
    """Balance stays non-negative throughout -> False (covers line 13)."""
    assert below_zero([1, 2, 3]) is False


def test_below_zero_empty_list_returns_false():
    """Empty operations list: loop body never runs -> False."""
    assert below_zero([]) is False


def test_below_zero_hits_exactly_zero_returns_false():
    """Balance touching exactly zero is not below zero -> False (boundary branch)."""
    assert below_zero([5, -5]) is False
