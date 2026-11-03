# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f056 import correct_bracketing


def test_empty_string_is_balanced():
    """Covers line 3 and the final return on line 11 (loop body never runs)."""
    assert correct_bracketing("") is True


def test_single_open_bracket_is_unbalanced():
    """Covers lines 4-6 (increment branch) and the final return being False."""
    assert correct_bracketing("<") is False


def test_single_close_bracket_is_unbalanced():
    """Covers lines 7-8 (else branch) and lines 9-10 (early-exit False)."""
    assert correct_bracketing(">") is False


def test_well_formed_pair_is_balanced():
    """Covers both if/else branches and reaching the final return with depth 0."""
    assert correct_bracketing("<>") is True


def test_close_before_open_is_unbalanced():
    """Covers the early-exit branch with further loop iterations afterwards."""
    assert correct_bracketing("><") is False


def test_nested_brackets_are_balanced():
    """Covers multiple increments/decrements without going negative."""
    assert correct_bracketing("<<><>>") is True


def test_unbalanced_extra_open_is_unbalanced():
    """Ensures the final return evaluates depth == 0 to False."""
    assert correct_bracketing("<<>>>") is False
