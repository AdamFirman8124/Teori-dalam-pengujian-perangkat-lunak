# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested — achieving full line and branch coverage.

is_nested is a pure function with no side effects, so no monkeypatching
or cleanup is required; each test is self-contained and stateless.
"""

from f132 import is_nested


def test_nested_brackets_returns_true():
    # '[[]]': the first loop takes both the '[' branch (line 7) and the
    # else branch (line 9); the inner condition (line 15) is True twice,
    # incrementing cnt to 2, so the function returns True (line 18).
    assert is_nested('[[]]') is True


def test_single_pair_returns_false():
    # '[]': exactly one match (cnt == 1), so the False side of the
    # return expression (cnt >= 2) is exercised.
    assert is_nested('[]') is False


def test_unmatched_opening_returns_false():
    # '[][]': for the second opening bracket, 'i < l' is True but
    # 'idx < closing_bracket_index[i]' is False (2 < 1), covering the
    # failing branch of the inner condition.
    assert is_nested('[][]') is False


def test_closing_brackets_exhausted_returns_true():
    # '[[]][[': cnt reaches 2, then 'i < l' becomes False (i == l == 2)
    # for the remaining opening brackets, covering the short-circuit
    # failure of the first clause of the inner condition.
    assert is_nested('[[]][[') is True


def test_empty_string_returns_false():
    # '': neither loop body executes; l == 0 and cnt == 0 -> False.
    assert is_nested('') is False


def test_only_closing_brackets_returns_false():
    # ']]]': opening_bracket_index is empty, so the second for loop
    # (line 14) never executes its body; returns False.
    assert is_nested(']]]') is False


def test_only_opening_brackets_returns_false():
    # '[[[': closing_bracket_index is empty, so l == 0 and 'i < l' is
    # False for every opening bracket; returns False.
    assert is_nested('[[[') is False


def test_non_bracket_characters_treated_as_closing():
    # 'a[a]a': every non-'[' character (letters and ']') goes through
    # the else branch (line 9). opening=[1], closing reversed=[4,3,2,0];
    # idx=1 matches once (cnt == 1) -> False.
    assert is_nested('a[a]a') is False
