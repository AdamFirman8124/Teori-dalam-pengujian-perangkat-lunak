# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest

from f119 import match_parens


def test_yes_when_first_concatenation_is_balanced():
    # Docstring example. S1 = '()(' + ')' = '()()' is balanced, so check(S1)
    # returns True and check(S2) is short-circuited. Covers: the '(' branch
    # of check's if, the val == 0 -> True outcome of the final conditional
    # expression, S1/S2 construction, and the 'Yes' return on line 29.
    assert match_parens(['()(', ')']) == 'Yes'


def test_yes_when_second_concatenation_is_balanced():
    # S1 = ')' + '(' = ')(' : the very first char is ')' so the else branch
    # runs, val becomes -1 and the early `return False` on line 24 fires.
    # check(S1) is False, so check(S2) = check('()' ) runs and returns True.
    assert match_parens([')', '(']) == 'Yes'


def test_no_when_s1_fails_early_and_s2_ends_positive():
    # S1 = ')' + '((' = ')((' fails early (val < 0); S2 = '((' + ')' = '(()'
    # never goes negative but ends at 1, so the final conditional expression
    # in check yields False -> overall 'No'.
    assert match_parens([')', '((']) == 'No'


def test_no_when_both_orders_go_negative():
    # Docstring example. S1 = S2 = '))' : val drops below zero immediately,
    # triggering the early `return False` in check for both orders, and the
    # 'No' branch of line 29 is taken.
    assert match_parens([')', ')']) == 'No'


def test_no_when_both_orders_end_positive():
    # S1 = S2 = '((' : every char takes the '(' branch, val never goes
    # negative, but it ends at 2, so the final `return True if val == 0
    # else False` yields False -> overall 'No'.
    assert match_parens(['(', '(']) == 'No'


def test_no_when_both_orders_are_unbalanced_mixed():
    # S1 = '(()' + '))' = '(()))' ends at -1 (early False);
    # S2 = '))' + '(()' = '))(()' goes negative immediately (early False).
    assert match_parens(['(()', '))']) == 'No'


def test_yes_trivial_pair():
    # S1 = '()' is balanced -> 'Yes' via the short-circuit on check(S1).
    assert match_parens(['(', ')']) == 'Yes'


def test_yes_when_both_orders_balanced():
    # S1 = S2 = '()' : both concatenations are balanced.
    assert match_parens(['()', '()']) == 'Yes'


def test_yes_nested_pair():
    # S1 = '(()' + '())' = '(()())' is balanced -> 'Yes'.
    assert match_parens(['(()', '())']) == 'Yes'
