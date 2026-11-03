# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


def test_simplify_returns_true_when_product_is_whole():
    # 1/2 * 2/1 = 2/2 = 1 -> whole number, must take the True branch (line 8)
    assert simplify("1/2", "2/1") is True


def test_simplify_returns_false_when_product_is_not_whole():
    # 1/2 * 1/2 = 1/4 = 0.25 -> not a whole number, must take the False branch (line 9)
    assert simplify("1/2", "1/2") is False


def test_simplify_true_with_multi_digit_and_negative_numerators():
    # 3/4 * 8/3 = 24/12 = 2 -> whole number
    assert simplify("3/4", "8/3") is True
    # -1/2 * 4/1 = -4/2 = -2 -> whole number (int() handles the minus sign)
    assert simplify("-1/2", "4/1") is True


def test_simplify_false_with_multi_digit_and_negative_numerators():
    # 7/3 * 5/2 = 35/6 -> not a whole number
    assert simplify("7/3", "5/2") is False
    # -1/3 * 2/1 = -2/3 -> not a whole number
    assert simplify("-1/3", "2/1") is False


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/2", "2/1", True),
        ("1/2", "1/2", False),
        ("0/1", "5/3", True),   # 0 * anything = 0, which is whole
        ("2/4", "4/2", True),   # 8/8 = 1
        ("3/7", "7/9", False),  # 21/63 = 1/3
    ],
)
def test_simplify_parametrized(x, n, expected):
    assert simplify(x, n) is expected
