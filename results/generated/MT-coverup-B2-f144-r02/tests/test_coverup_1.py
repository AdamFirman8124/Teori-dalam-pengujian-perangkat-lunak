# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

from f144 import simplify


def test_simplify_returns_true_when_product_is_whole_number():
    # (1/2) * (2/1) = 2/2 = 1, which is an integer -> True
    assert simplify("1/2", "2/1") is True


def test_simplify_returns_false_when_product_is_not_whole_number():
    # (1/2) * (2/3) = 2/6 = 1/3, which is not an integer -> False
    assert simplify("1/2", "2/3") is False


def test_simplify_handles_negative_fractions():
    # (-1/2) * (2/1) = -2/2 = -1, an integer -> True
    assert simplify("-1/2", "2/1") is True
    # (-1/2) * (1/3) = -1/6, not an integer -> False
    assert simplify("-1/2", "1/3") is False
