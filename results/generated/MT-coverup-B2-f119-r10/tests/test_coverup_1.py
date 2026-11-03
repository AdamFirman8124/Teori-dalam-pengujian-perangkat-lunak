# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

"""Tests for f119.match_parens covering lines 16-29 (the check helper and
the concatenation/decision logic)."""

from f119 import match_parens


def test_yes_when_first_concatenation_is_balanced():
    # S1 = '()(' + ')' = '()()' is balanced -> check(S1) True -> 'Yes'.
    # Also exercises: '(' branch (val+1), ')' branch (val-1), val >= 0
    # continuation, and the `val == 0` True arm of the final ternary.
    assert match_parens(['()(', ')']) == 'Yes'


def test_yes_when_only_second_concatenation_is_balanced():
    # S1 = '())' + '(()' = '())(()' dips negative -> check(S1) False,
    # so check(S2) runs: S2 = '(()' + '())' = '(()())' balanced -> 'Yes'.
    # Covers the False path out of check (early return on val < 0) plus
    # the right-hand operand of the `or`.
    assert match_parens(['())', '(()']) == 'Yes'


def test_no_when_val_goes_negative_in_both_orders():
    # S1 = S2 = '))' : val becomes -1 immediately -> early False return
    # from check for both operands -> 'No'.
    assert match_parens([')', ')']) == 'No'


def test_no_when_leftover_open_parens_in_both_orders():
    # S1 = S2 = '((' : loop finishes with val == 2, so the `val == 0`
    # condition is False (False arm of the final ternary) -> 'No'.
    assert match_parens(['(', '(']) == 'No'


def test_no_with_mixed_failure_modes():
    # S1 = ')(' + '(' = ')((' -> first char ')' makes val -1 -> early False.
    # S2 = '(' + ')(' = '()(' -> never negative but ends with val == 1 -> False.
    # Exercises both failure modes of check in one call -> 'No'.
    assert match_parens([')(', '(']) == 'No'


def test_empty_strings_are_balanced():
    # Zero-iteration loop branch of `for i in s`: val stays 0 -> True -> 'Yes'.
    assert match_parens(['', '']) == 'Yes'
