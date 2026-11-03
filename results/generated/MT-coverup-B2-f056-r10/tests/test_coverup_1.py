# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f056 import correct_bracketing


def test_balanced_pair_returns_true():
    # Covers lines 3-6 (depth += 1 branch), 8 (depth -= 1 branch), 9, 11 (True outcome)
    assert correct_bracketing("<>") is True


def test_nested_balanced_returns_true():
    # Exercises both branches multiple times, ends balanced
    assert correct_bracketing("<<><>>") is True


def test_closing_before_opening_returns_false_early():
    # Covers line 10 (return False when depth < 0)
    assert correct_bracketing("><") is False


def test_negative_depth_midway_returns_false():
    # Depth goes negative only at the last character
    assert correct_bracketing("<><>>") is False


def test_unclosed_brackets_returns_false_at_end():
    # Loop completes but depth != 0, covering line 11 (False outcome)
    assert correct_bracketing("<<") is False


def test_empty_string_returns_true():
    # Loop body never runs; only lines 3 and 11 execute
    assert correct_bracketing("") is True
