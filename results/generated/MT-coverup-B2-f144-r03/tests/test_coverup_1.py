# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


def test_simplify_returns_true_when_product_is_integer():
    # 1/2 * 2/1 = 2/2 = 1.0 -> integer
    assert simplify("1/2", "2/1") is True


def test_simplify_returns_true_for_nontrivial_integer_result():
    # 3/4 * 8/3 = 24/12 = 2.0 -> integer
    assert simplify("3/4", "8/3") is True


def test_simplify_returns_false_when_product_is_not_integer():
    # 1/2 * 1/3 = 1/6 -> not an integer
    assert simplify("1/2", "1/3") is False


def test_simplify_returns_false_for_another_fractional_result():
    # 2/5 * 3/7 = 6/35 -> not an integer
    assert simplify("2/5", "3/7") is False


def test_simplify_with_negative_fractions_true():
    # -1/2 * 4/1 = -4/2 = -2.0 -> integer
    assert simplify("-1/2", "4/1") is True


def test_simplify_with_negative_fractions_false():
    # -1/2 * 1/3 = -1/6 -> not an integer
    assert simplify("-1/2", "1/3") is False
