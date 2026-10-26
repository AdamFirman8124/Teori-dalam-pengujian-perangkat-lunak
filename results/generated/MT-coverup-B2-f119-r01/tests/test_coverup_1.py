# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import f119

match_parens = f119.match_parens


def test_s1_balanced_returns_yes():
    # S1 = "()()" is balanced, so check(S1) is True (short-circuit or)
    # Covers: '(' branch, ')' branch, val < 0 False, final val == 0 True
    assert match_parens(['()(', ')']) == 'Yes'


def test_s2_only_balanced_returns_yes():
    # S1 = ")()(" fails on first char (val < 0 True -> False)
    # S2 = "()()" succeeds, so covers check(S1) False, check(S2) True
    assert match_parens([')', '()(']) == 'Yes'


def test_both_negative_returns_no():
    # S1 = "))" and S2 = "))" both fail via val < 0 -> False
    # Covers: else (')') branch with early return, or False/False -> 'No'
    assert match_parens([')', ')']) == 'No'


def test_positive_unbalanced_returns_no():
    # S1 = "((((" and S2 = "((((" never go negative but end with val != 0
    # Covers: loop completes, val < 0 False, final val == 0 False
    assert match_parens(['((', '((']) == 'No'


def test_empty_strings_returns_yes():
    # S1 = "" loop executes zero times, val == 0 -> True
    # Covers: for-loop zero-iteration branch
    assert match_parens(['', '']) == 'Yes'
