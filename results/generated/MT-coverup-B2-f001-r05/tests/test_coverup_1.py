# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

"""Tests for f001.separate_paren_groups covering lines 6-22."""

from f001 import separate_paren_groups


def test_separate_paren_groups_empty_string():
    """Lines 6-8, 10, 22: initialization, loop over empty iterable, return."""
    result = separate_paren_groups('')
    # Postcondition: no groups found, empty list returned.
    assert result == []


def test_separate_paren_groups_single_pair():
    """Lines 11-13 ('(' branch), 14-16 (')' branch), 18-20 (depth==0 flush), 22."""
    result = separate_paren_groups('()')
    # Postcondition: the single balanced pair is returned as one group.
    assert result == ['()']


def test_separate_paren_groups_nested_and_multiple_with_spaces():
    """Exercises both outcomes of the depth==0 check (line 18): True flushes a
    completed group (lines 19-20); False keeps accumulating nested parens.
    Spaces hit neither the '(' nor ')' branch and must be ignored."""
    result = separate_paren_groups('( ) (( )) (( )( ))')
    # Postcondition: three separate, non-nested groups, spaces stripped,
    # nesting preserved within each group.
    assert result == ['()', '(())', '(()())']


def test_separate_paren_groups_does_not_mutate_input_or_leak_state():
    """Verifies purity: repeated calls give identical results and the input
    string is untouched (the function has no external state to clean up)."""
    source = '((())) (()())'
    snapshot = source
    first = separate_paren_groups(source)
    second = separate_paren_groups(source)
    assert source == snapshot
    assert first == second == ['((()))', '(()())']
