# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f056 import correct_bracketing


def test_empty_string_returns_true():
    """Covers lines 3, 4 (loop over empty), and 11 (depth == 0)."""
    assert correct_bracketing("") is True


def test_balanced_brackets_returns_true():
    """Covers lines 3-6, 8, 11: '<' branch and else branch, balanced."""
    assert correct_bracketing("<><>") is True


def test_unbalanced_extra_open_returns_false():
    """Covers line 11 with depth > 0 (returns False via depth == 0 check)."""
    assert correct_bracketing("<<<") is False


def test_unbalanced_extra_close_returns_false():
    """Covers lines 8-10: depth goes negative, early return False."""
    assert correct_bracketing("><") is False


def test_leading_close_returns_false():
    """Covers line 10 immediately on first character."""
    assert correct_bracketing(">") is False


def test_negative_depth_midway_still_false():
    """Depth dips negative even though it would recover; early return wins."""
    assert correct_bracketing("<<>>><") is False
