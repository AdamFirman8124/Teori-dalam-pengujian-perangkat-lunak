# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f056 import correct_bracketing


def test_correct_bracketing_balanced():
    """Covers lines 3-6 (depth init, loop, '<' branch), line 8 (else branch),
    and line 11 (final return True)."""
    assert correct_bracketing("<>") is True


def test_correct_bracketing_nested_balanced():
    """Covers multiple iterations of both branches and final return True."""
    assert correct_bracketing("<<>>") is True
    assert correct_bracketing("<<><>>") is True


def test_correct_bracketing_negative_depth():
    """Covers lines 9-10: early return False when depth goes negative."""
    assert correct_bracketing("><") is False
    assert correct_bracketing("><><") is False


def test_correct_bracketing_unclosed():
    """Covers line 11 returning False when depth is positive at end."""
    assert correct_bracketing("<") is False
    assert correct_bracketing("<<") is False


def test_correct_bracketing_empty():
    """Covers line 3 and line 11 with an empty string (loop body skipped)."""
    assert correct_bracketing("") is True
