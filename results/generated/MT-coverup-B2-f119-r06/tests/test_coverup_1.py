# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest

from f119 import match_parens


def test_match_parens_yes_first_order():
    # S1 = '()(' + ')' = '()()' is balanced -> 'Yes' via check(S1)
    assert match_parens(['()(', ')']) == 'Yes'


def test_match_parens_yes_second_order():
    # S1 = ')' + '(()' = ')(()' fails early (val < 0),
    # S2 = '(()' + ')' = '(()' + ')' = '(()' + ')' ... balanced -> 'Yes' via check(S2)
    assert match_parens([')', '(()']) == 'Yes'


def test_match_parens_no_unbalanced():
    # Both orders leave an unmatched ')' -> 'No' (check returns False with val != 0)
    assert match_parens([')', ')']) == 'No'


def test_match_parens_no_extra_open():
    # Both orders leave an unmatched '(' -> 'No' (check reaches end with val > 0)
    assert match_parens(['((', '(']) == 'No'


def test_match_parens_empty_strings():
    # Empty concatenations are trivially balanced -> 'Yes'
    assert match_parens(['', '']) == 'Yes'


def test_match_parens_both_orders_balanced():
    assert match_parens(['()', '()']) == 'Yes'
