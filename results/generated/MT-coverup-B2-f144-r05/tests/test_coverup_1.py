# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

"""Tests for f144.simplify — covering both branches (lines 3-9)."""

import pytest

from f144 import simplify


def test_simplify_returns_true_when_product_is_whole():
    # 1/2 * 2/1 = 2/2 = 1 -> integer -> True (exercises line 8)
    assert simplify("1/2", "2/1") is True
    # 3/4 * 4/3 = 12/12 = 1 -> integer -> True
    assert simplify("3/4", "4/3") is True
    # 3/2 * 4/1 = 12/2 = 6 -> integer greater than 1 -> True
    assert simplify("3/2", "4/1") is True


def test_simplify_returns_false_when_product_is_not_whole():
    # 1/2 * 3/4 = 3/8 = 0.375 -> not integer -> False (exercises line 9)
    assert simplify("1/2", "3/4") is False
    # 7/10 * 10/2 = 70/20 = 3.5 -> not integer -> False
    assert simplify("7/10", "10/2") is False
    # 5/2 * 1/1 = 5/2 = 2.5 -> not integer -> False
    assert simplify("5/2", "1/1") is False


def test_simplify_zero_numerator_is_whole():
    # 0/5 * 3/4 = 0/20 = 0.0 -> int(0.0) == 0.0 -> True
    assert simplify("0/5", "3/4") is True


def test_simplify_negative_values():
    # -1/2 * 2/1 = -2/2 = -1.0 -> int(-1.0) == -1.0 -> True
    assert simplify("-1/2", "2/1") is True
    # -1/2 * 3/4 = -3/8 = -0.375 -> int(-0.375) == 0 -> not equal -> False
    assert simplify("-1/2", "3/4") is False
    # -3/2 * 3/1 = -9/2 = -4.5 -> int(-4.5) == -4 -> not equal -> False
    assert simplify("-3/2", "3/1") is False


def test_simplify_parsing_of_multi_digit_parts():
    # Exercises the split/int parsing on lines 3-6 with multi-digit numbers
    # 12/10 * 5/6 = 60/60 = 1.0 -> True
    assert simplify("12/10", "5/6") is True
    # 12/10 * 5/8 = 60/80 = 0.75 -> False
    assert simplify("12/10", "5/8") is False


def test_simplify_is_pure_and_does_not_mutate_inputs():
    x = "1/2"
    n = "2/1"
    result = simplify(x, n)
    # Inputs are unchanged (function is pure; no state to pollute)
    assert x == "1/2"
    assert n == "2/1"
    assert result is True
