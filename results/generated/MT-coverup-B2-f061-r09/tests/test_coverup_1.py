# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f061 import correct_bracketing


def test_empty_string_returns_true():
    assert correct_bracketing("") is True


def test_balanced_simple():
    assert correct_bracketing("()") is True


def test_balanced_nested():
    assert correct_bracketing("(())") is True


def test_unbalanced_closing_first_returns_false():
    assert correct_bracketing(")(") is False


def test_unbalanced_extra_closing_returns_false():
    assert correct_bracketing("())") is False


def test_unbalanced_extra_opening_returns_false():
    assert correct_bracketing("(()") is False


def test_early_exit_on_negative_depth():
    # depth goes negative at the first char; must return False immediately
    assert correct_bracketing(")()") is False
