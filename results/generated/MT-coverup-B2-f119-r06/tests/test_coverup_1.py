# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

"""Tests for f119.match_parens covering lines 16-29 and all branches."""

from f119 import match_parens


def test_yes_when_first_concatenation_is_good():
    # S1 = '()(' + ')' = '()()' is balanced -> check(S1) True short-circuits,
    # so check(S2) is never evaluated.
    # Covers: '(' branch (val+1), ')' branch (val-1), val >= 0 path,
    # final 'return True if val == 0' True branch, and 'Yes' return.
    assert match_parens(['()(', ')']) == 'Yes'


def test_no_when_both_orders_fail_early_negative():
    # S1 = '))' and S2 = '))' both drive val negative immediately,
    # exercising the 'if val < 0: return False' early-exit branch (line 24)
    # in both calls, and the final 'No' return.
    assert match_parens([')', ')']) == 'No'


def test_yes_when_only_second_concatenation_is_good():
    # S1 = ')' + '(' = ')(' fails via val < 0 (line 24),
    # then check(S2) = check('()' ) succeeds -> 'Yes'.
    # Covers: check(S1) False followed by check(S2) True in the 'or'.
    assert match_parens([')', '(']) == 'Yes'


def test_no_when_unbalanced_but_never_negative():
    # S1 = '()' + '(' = '()(' never goes negative but ends with val == 1,
    # exercising the 'return True if val == 0 else False' False branch (line 25).
    # S2 = '(' + '()' = '(()' also ends unbalanced -> 'No'.
    assert match_parens(['()', '(']) == 'No'
