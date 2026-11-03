# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


def test_simplify_returns_true_when_product_is_whole():
    # 1/2 * 2/1 = 2/2 = 1 -> integer, covers lines 3-8 (True branch)
    assert simplify("1/2", "2/1") is True


def test_simplify_returns_false_when_product_is_not_whole():
    # 1/2 * 3/2 = 3/4 = 0.75 -> not an integer, covers line 9 (False branch)
    assert simplify("1/2", "3/2") is False


def test_simplify_negative_fractions_whole_result():
    # -1/2 * 2/1 = -2/2 = -1 -> integer (True branch with negatives)
    assert simplify("-1/2", "2/1") is True


def test_simplify_negative_fractions_non_whole_result():
    # -1/2 * 3/2 = -3/4 = -0.75 -> not an integer (False branch with negatives)
    assert simplify("-1/2", "3/2") is False


def test_simplify_zero_numerator():
    # 0/1 * 3/4 = 0/4 = 0.0 -> integer (True branch)
    assert simplify("0/1", "3/4") is True


def test_simplify_multi_digit_values():
    # 12/4 * 5/3 = 60/12 = 5 -> integer
    assert simplify("12/4", "5/3") is True
    # 12/4 * 5/6 = 60/24 = 2.5 -> not an integer
    assert simplify("12/4", "5/6") is False


def test_simplify_malformed_input_raises_value_error():
    # int("a") raises ValueError, exercising the int() conversions on lines 5-6
    with pytest.raises(ValueError):
        simplify("a/b", "1/2")
