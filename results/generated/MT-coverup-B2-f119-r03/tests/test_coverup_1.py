# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

"""Tests for f119.match_parens, covering the previously missing lines 16-29.

Line/branch coverage rationale:
- Lines 16-25 (nested ``check``): exercised by every call to ``match_parens``.
- Lines 19-20 ('(' increment branch): exercised by every test below.
- Lines 21-22 (')' decrement else-branch): exercised by test_yes_when_only_second_order_is_good,
  test_no_when_both_orders_leave_unclosed_parens and test_no_when_both_orders_go_negative.
- Lines 23-24 (early ``return False`` when val < 0): exercised by test_yes_when_only_second_order_is_good,
  test_no_when_both_orders_leave_unclosed_parens and test_no_when_both_orders_go_negative.
- Line 25, True side (val == 0): exercised by test_yes_when_first_order_is_already_good and
  test_yes_when_only_second_order_is_good.
- Line 25, False side (val != 0 at end): exercised by test_no_when_both_orders_leave_unclosed_parens.
- Lines 27-29: both the 'Yes' and 'No' return paths (including the ``or`` short-circuit and its
  fallback to ``check(S2)``) are exercised below.

The function under test is pure (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required and there is no risk of state pollution.
"""

from f119 import match_parens


def test_yes_when_first_order_is_already_good():
    # S1 = '()' is balanced, so 'Yes' is returned without needing S2
    # (the `or` short-circuits: check(S2) is never reached).
    assert match_parens(['(', ')']) == 'Yes'


def test_yes_when_only_second_order_is_good():
    # S1 = ')('  -> first ')' drops val below zero, early False (lines 23-24).
    # S2 = '()'  -> balanced, line 25 returns True (val == 0).
    assert match_parens([')', '(']) == 'Yes'


def test_no_when_both_orders_leave_unclosed_parens():
    # S1 = '()(' -> never negative but ends with val == 1, so line 25 takes
    #               the 'else False' side of the conditional expression.
    # S2 = ')((' -> val drops below zero immediately (lines 23-24).
    assert match_parens(['(', ')(']) == 'No'


def test_no_when_both_orders_go_negative():
    # S1 = '))' and S2 = '))' both fail with val < 0 (lines 23-24),
    # so line 29 returns 'No'.
    assert match_parens([')', ')']) == 'No'


def test_docstring_examples():
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens([')', ')']) == 'No'
