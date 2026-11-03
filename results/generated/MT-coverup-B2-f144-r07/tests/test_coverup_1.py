# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


def test_simplify_product_is_integer_returns_true():
    # (1/2) * (4/1) = 4/2 = 2.0 -> integer, covers lines 3-8 and the True branch
    assert simplify("1/2", "4/1") is True


def test_simplify_product_is_not_integer_returns_false():
    # (1/2) * (1/2) = 1/4 = 0.25 -> not an integer, covers line 9 (False branch)
    assert simplify("1/2", "1/2") is False


def test_simplify_negative_and_zero_cases():
    # (-1/2) * (-4/1) = 4/2 = 2.0 -> integer
    assert simplify("-1/2", "-4/1") is True
    # (0/3) * (5/7) = 0/21 = 0.0 -> integer
    assert simplify("0/3", "5/7") is True
    # (3/4) * (2/3) = 6/12 = 0.5 -> not an integer
    assert simplify("3/4", "2/3") is False
