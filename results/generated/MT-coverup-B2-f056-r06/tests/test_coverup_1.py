# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

"""Tests for f056.correct_bracketing, covering all lines and branches.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or cleanup is required; each test is fully
self-contained and cannot pollute state.
"""

from f056 import correct_bracketing


def test_empty_string_is_balanced():
    """Covers lines 3, 4 (loop with zero iterations) and 11 (True)."""
    assert correct_bracketing("") is True


def test_single_open_bracket_is_unbalanced():
    """Covers lines 5-6 ('<' branch) and 11 (depth > 0 -> False)."""
    assert correct_bracketing("<") is False


def test_single_close_bracket_is_unbalanced():
    """Covers lines 8 (else branch), 9-10 (early return False)."""
    assert correct_bracketing(">") is False


def test_simple_pair_is_balanced():
    """Covers both the '<' branch (5-6) and the else branch (8), plus line 11 (True)."""
    assert correct_bracketing("<>") is True


def test_nested_brackets_are_balanced():
    """Exercises the '<' branch multiple times before the else branch; line 11 (True)."""
    assert correct_bracketing("<<>>") is True


def test_close_before_open_is_unbalanced():
    """Covers the else branch (8) followed by the early return (9-10)."""
    assert correct_bracketing("><") is False


def test_unclosed_brackets_are_unbalanced():
    """Covers '<' branch, else branch, and line 11 with depth > 0 (False)."""
    assert correct_bracketing("<<>") is False


def test_mixed_string_ending_negative_is_unbalanced():
    """Covers interleaved branches with the early return on line 9-10."""
    assert correct_bracketing("<><") is False
