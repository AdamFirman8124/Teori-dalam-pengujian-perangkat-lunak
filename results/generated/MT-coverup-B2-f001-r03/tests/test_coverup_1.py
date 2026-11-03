# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

"""Tests for f001.separate_paren_groups (HumanEval-style function).

The function is pure (no I/O, no module-level mutable state), so no
monkeypatching/teardown is required; each test leaves no state behind.
"""

from f001 import separate_paren_groups


def test_separates_groups_with_spaces_and_nesting():
    """Groups separated by spaces, with nested parens inside groups.

    Exercises: initialization (lines 6-8), the loop (10), the '(' branch
    (11-13), the ')' branch (14-16), both outcomes of the depth==0 check
    (18-20: True when a group closes, False for ')' inside a nested group),
    ignored non-paren characters, and the return (22).
    """
    result = separate_paren_groups('( ) (( )) (( )( ))')
    assert result == ['()', '(())', '(()())']


def test_separates_adjacent_groups_without_spaces():
    """Adjacent groups with no separator still split at depth 0."""
    result = separate_paren_groups('()()()')
    assert result == ['()', '()', '()']


def test_empty_string_returns_empty_list():
    """Empty input: loop body never runs, empty list returned."""
    assert separate_paren_groups('') == []


def test_non_paren_characters_are_ignored():
    """Characters that are neither '(' nor ')' are skipped entirely."""
    assert separate_paren_groups('   ') == []
    assert separate_paren_groups('abc') == []


def test_unbalanced_group_is_not_returned():
    """A group that never returns to depth 0 is never flushed to result."""
    assert separate_paren_groups('(()') == []


def test_deeply_nested_single_group():
    """A single deeply nested group is returned as one string."""
    result = separate_paren_groups('((()))')
    assert result == ['((()))']


def test_single_pair():
    """Minimal balanced pair."""
    assert separate_paren_groups('()') == ['()']
