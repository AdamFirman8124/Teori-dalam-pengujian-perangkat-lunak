# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


def test_simplify_returns_true_when_product_is_whole_number():
    """Covers lines 3-8: parsing, arithmetic, condition and the True branch.

    (1/5) * (5/1) = 5/5 = 1, which is an integer, so the result is True.
    """
    assert simplify("1/5", "5/1") is True
    assert simplify("3/2", "2/3") is True  # (3*2)/(2*3) = 6/6 = 1


def test_simplify_returns_false_when_product_is_not_whole_number():
    """Covers the False branch of the condition on line 7 (line 9).

    (1/6) * (2/1) = 2/6 = 1/3, which is not an integer, so the result is False.
    """
    assert simplify("1/6", "2/1") is False
    assert simplify("7/3", "5/2") is False  # 35/6 is not an integer


def test_simplify_handles_negative_and_larger_values():
    """Sanity checks with negative and larger operands on the same code paths."""
    # (-1/2) * (4/1) = -4/2 = -2 -> integer -> True branch (line 8)
    assert simplify("-1/2", "4/1") is True
    # (10/3) * (3/10) = 30/30 = 1 -> integer -> True branch
    assert simplify("10/3", "3/10") is True
    # (5/4) * (3/7) = 15/28 -> not an integer -> False branch (line 9)
    assert simplify("5/4", "3/7") is False
