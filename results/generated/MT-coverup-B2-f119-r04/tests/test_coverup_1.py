# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

"""Tests for f119.match_parens covering lines 16-29 (check() and the return logic)."""

from f119 import match_parens


def test_yes_first_order_balanced():
    # S1 = '()(' + ')' = '()()' is balanced -> check(S1) True -> 'Yes'.
    # Covers: check loop, '(' increment branch, val == 0 True path (line 25),
    # S1/S2 construction (lines 27-28) and 'Yes' via check(S1) (line 29).
    assert match_parens(['()(', ')']) == 'Yes'


def test_yes_second_order_after_early_negative():
    # S1 = ')' + '(' = ')(' goes negative immediately -> early 'return False'
    # (lines 22-24, ')' decrement branch). Short-circuit 'or' then evaluates
    # S2 = '(' + ')' = '()' which is balanced -> 'Yes' via check(S2).
    assert match_parens([')', '(']) == 'Yes'


def test_no_unbalanced_but_never_negative():
    # S1 = S2 = '(()((' never goes negative but ends with val == 3,
    # so line 25 takes the False path for both orders -> 'No'.
    assert match_parens(['(()', '(()']) == 'No'


def test_no_immediate_negative_both_orders():
    # S1 = S2 = '))' both go negative -> early False returns -> 'No'.
    # Also covers the docstring's second example.
    assert match_parens([')', ')']) == 'No'
