# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

"""Tests for f119.match_parens covering lines 16-29 (check() and both orders).

The function under test is pure (no globals, no I/O, no mutable state),
so no monkeypatching/teardown is required; each test is self-contained
and leaves no state behind.
"""

from f119 import match_parens


def test_yes_first_order_balanced():
    # S1 = '()(' + ')' = '()()' is balanced -> check(S1) True short-circuits
    # the 'or', so check(S2) is never called. Covers lines 16-25 (True path
    # of line 25) and the 'Yes' outcome of line 29.
    assert match_parens(['()(', ')']) == 'Yes'


def test_yes_second_order_balanced():
    # S1 = ')' + '(()' = ')((' goes negative immediately (lines 23-24,
    # return False), so check(S2) IS evaluated: S2 = '(()' + ')' = '(())'
    # is balanced. Covers the check(S2) side of line 29's 'or'.
    assert match_parens([')', '(()']) == 'Yes'


def test_no_immediate_negative_both_orders():
    # S1 = '))' and S2 = '))' both hit val < 0 -> return False (line 24)
    # for both operands of the 'or' -> 'No'.
    assert match_parens([')', ')']) == 'No'


def test_no_positive_leftover_both_orders():
    # S1 = '((' and S2 = '((' never go negative but end with val == 2,
    # exercising the False branch of line 25 (val != 0) -> 'No'.
    assert match_parens(['(', '(']) == 'No'


def test_no_mixed_failure_modes():
    # S1 = '(' + ')(' = '()(' ends positive (line 25 False branch),
    # S2 = ')(' + '(' = ')(' goes negative (line 24). Both fail -> 'No'.
    assert match_parens(['(', ')(']) == 'No'


def test_yes_trivial_balanced_pair():
    # S1 = '(' + ')' = '()' balanced -> 'Yes'; also covers the '(' branch
    # incrementing val (line 20) followed by ')' decrementing (line 22)
    # without ever going negative.
    assert match_parens(['(', ')']) == 'Yes'
