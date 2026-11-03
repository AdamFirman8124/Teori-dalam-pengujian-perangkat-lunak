# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f061 import correct_bracketing


def test_empty_string_returns_true():
    """Covers lines 3-4 and 11 (loop never runs, depth == 0)."""
    assert correct_bracketing("") is True


def test_single_open_returns_false():
    """Covers lines 5-6 (the '(' branch); unclosed '(' leaves depth > 0."""
    assert correct_bracketing("(") is False


def test_single_close_returns_false_early():
    """Covers lines 8-10 (the else branch and early return False)."""
    assert correct_bracketing(")") is False


def test_balanced_pair_returns_true():
    """Covers both branches of the if/else and line 11 with depth == 0."""
    assert correct_bracketing("()") is True


def test_close_before_open_returns_false_early():
    """Covers the early return False after depth goes negative mid-string."""
    assert correct_bracketing(")(") is False


def test_unclosed_brackets_returns_false_at_end():
    """Covers line 11 with depth != 0 (loop completes but depth > 0)."""
    assert correct_bracketing("((") is False


def test_nested_balanced_returns_true():
    """Covers repeated execution of both branches with a balanced result."""
    assert correct_bracketing("(()())") is True


def test_negative_only_at_end_returns_false():
    """Depth stays non-negative until the final character."""
    assert correct_bracketing("(()") is False
