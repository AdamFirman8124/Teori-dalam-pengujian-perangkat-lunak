# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f061 import correct_bracketing


def test_empty_string_is_balanced():
    # Covers line 3 (depth = 0) and line 11 (return depth == 0 -> True),
    # with the loop body never entered.
    assert correct_bracketing("") is True


def test_simple_pair_is_balanced():
    # Covers lines 4-8: both the '(' branch (depth += 1) and the
    # else branch (depth -= 1), ending balanced.
    assert correct_bracketing("()") is True


def test_nested_pairs_are_balanced():
    assert correct_bracketing("(())") is True


def test_sequential_pairs_are_balanced():
    assert correct_bracketing("()()") is True


def test_unclosed_open_is_unbalanced():
    # Covers line 11 returning False (depth > 0 at end).
    assert correct_bracketing("((") is False


def test_extra_open_is_unbalanced():
    assert correct_bracketing("(()") is False


def test_leading_close_returns_false_early():
    # Covers lines 9-10: depth < 0 triggers the early `return False`.
    assert correct_bracketing(")(") is False


def test_single_close_is_unbalanced():
    assert correct_bracketing(")") is False


def test_close_after_prefix_returns_false_early():
    # Depth goes negative mid-string even though it would end at 0.
    assert correct_bracketing("())(") is False
