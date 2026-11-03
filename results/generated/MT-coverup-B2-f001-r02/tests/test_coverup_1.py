# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

"""Tests for f001.separate_paren_groups.

The function under test is pure (no I/O, no module-level mutable state),
so no monkeypatching or cleanup is required; each test only relies on its
own inputs and asserts the exact expected output.
"""

from typing import List

from f001 import separate_paren_groups


def test_multiple_groups_with_spaces_and_nesting():
    """Covers: initialization (lines 6-8), loop (line 10), '(' branch
    (lines 11-13), ')' branch (lines 14-16), both outcomes of the
    depth == 0 check (lines 18-19), and the return (line 22)."""
    result: List[str] = separate_paren_groups('( ) (( )) (( )( ))')
    assert result == ['()', '(())', '(()())']
    # Postcondition: every group is balanced and non-empty.
    for group in result:
        assert group.startswith('(') and group.endswith(')')
        assert group.count('(') == group.count(')')


def test_empty_string_returns_empty_list():
    """Covers the loop-not-taken branch (for loop over empty string)."""
    assert separate_paren_groups('') == []


def test_single_group():
    assert separate_paren_groups('()') == ['()']


def test_deeply_nested_single_group():
    """Covers the current_depth != 0 branch of the inner check (line 18)."""
    assert separate_paren_groups('((()))') == ['((()))']


def test_unbalanced_open_parens_yields_no_groups():
    """Depth never returns to zero, so no group is ever emitted."""
    assert separate_paren_groups('(()') == []


def test_non_paren_characters_are_dropped():
    """Characters other than '(' and ')' fall through both branches and
    are not included in the emitted groups."""
    assert separate_paren_groups('a(b)c (d)e') == ['()', '()']
