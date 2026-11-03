# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest

from f119 import match_parens


def test_yes_when_first_order_balanced():
    # S1 = '()(' + ')' = '()()' is balanced, so check(S1) returns True
    # (final return with val == 0) and short-circuits the 'or' on line 29.
    assert match_parens(['()(', ')']) == 'Yes'


def test_no_when_both_orders_go_negative():
    # S1 = S2 = '))' -> val drops below 0, exercising the early
    # 'return False' inside check (lines 23-24) for both orders.
    assert match_parens([')', ')']) == 'No'


def test_yes_when_only_second_order_balanced():
    # S1 = '())' + '(()' = '())(()' goes negative (early False),
    # then S2 = '(()' + '())' = '(()())' is balanced -> 'Yes'.
    # Covers the 'or' branch where check(S1) is False and check(S2) is True.
    assert match_parens(['())', '(()']) == 'Yes'


def test_no_when_both_orders_end_nonzero():
    # S1 = S2 = '((' never go negative but end with val == 2,
    # exercising the False branch of the final 'return True if val == 0 else False'.
    assert match_parens(['(', '(']) == 'No'


def test_no_first_negative_second_ends_nonzero():
    # S1 = ')(' + '((' = ')((' goes negative (early False),
    # S2 = '((' + ')(' = '(()(' ends nonzero (final False) -> 'No'.
    assert match_parens([')(', '((']) == 'No'


def test_yes_when_first_negative_second_balanced():
    # S1 = ')' + '(' = ')(' goes negative (early False),
    # S2 = '(' + ')' = '()' is balanced -> 'Yes'.
    assert match_parens([')', '(']) == 'Yes'


def test_empty_strings_skip_loop():
    # check('') never enters the for loop and returns True (val == 0),
    # covering the zero-iteration branch of the loop.
    assert match_parens(['', '']) == 'Yes'


def test_single_pair_both_orders():
    # S1 = '()' balanced -> 'Yes'.
    assert match_parens(['(', ')']) == 'Yes'
