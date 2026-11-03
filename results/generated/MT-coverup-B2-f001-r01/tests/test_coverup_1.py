# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest

from f001 import separate_paren_groups


def test_empty_string_returns_empty_list():
    """Covers lines 6-8 and 22 without entering the loop (loop-not-taken branch)."""
    assert separate_paren_groups("") == []


def test_single_group():
    """Covers the '(' branch (lines 11-13), the ')' branch (lines 14-16),
    and the depth == 0 true branch (lines 18-20)."""
    assert separate_paren_groups("()") == ["()"]


def test_multiple_groups_are_separated():
    """Verifies current_string is cleared after each completed group."""
    assert separate_paren_groups("()()") == ["()", "()"]


def test_nested_group_kept_together():
    """Covers the depth == 0 false branch (line 18) when a nested group closes."""
    assert separate_paren_groups("(())") == ["(())"]


def test_spaces_are_ignored():
    """Covers the implicit else branch (character that is neither '(' nor ')')."""
    assert separate_paren_groups("( )") == ["()"]


def test_mixed_groups_with_spaces_and_nesting():
    """Exercises every branch: open, close, non-paren char, nested close
    (depth != 0) and top-level close (depth == 0)."""
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]


def test_input_string_is_not_mutated():
    """Postcondition: the function is pure and does not modify its argument."""
    s = "( ) (( ))"
    result = separate_paren_groups(s)
    assert s == "( ) (( ))"
    assert result == ["()", "(())"]


@pytest.mark.parametrize(
    "paren_string, expected",
    [
        ("", []),
        ("()", ["()"]),
        ("()()", ["()", "()"]),
        ("(())", ["(())"]),
        ("(()())", ["(()())"]),
        ("( ) (( )) (( )( ))", ["()", "(())", "(()())"]),
    ],
)
def test_separate_paren_groups_parametrized(paren_string, expected):
    assert separate_paren_groups(paren_string) == expected
