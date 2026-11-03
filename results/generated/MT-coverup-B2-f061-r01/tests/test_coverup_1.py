# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f061 import correct_bracketing


def test_empty_string_returns_true():
    """Covers line 3 (depth = 0) and line 11 (return depth == 0) with no iterations."""
    assert correct_bracketing("") is True


def test_balanced_single_pair():
    """Covers lines 4-6 (open branch, depth += 1), line 8 (depth -= 1), and line 11."""
    assert correct_bracketing("()") is True


def test_nested_balanced():
    """Covers multiple increments/decrements and final True return."""
    assert correct_bracketing("((()))") is True
    assert correct_bracketing("()()") is True


def test_leading_close_returns_false():
    """Covers lines 8-10: depth goes negative immediately, early return False."""
    assert correct_bracketing(")") is False


def test_close_before_open_returns_false():
    """Covers line 10 via a later negative depth, not just the first character."""
    assert correct_bracketing(")(") is False


def test_unclosed_open_returns_false():
    """Covers line 11 evaluating to False when depth > 0 at the end."""
    assert correct_bracketing("(()") is False


def test_mixed_prefix_negative():
    """Balanced prefix then extra close: exercises both branches and early False."""
    assert correct_bracketing("()())") is False
