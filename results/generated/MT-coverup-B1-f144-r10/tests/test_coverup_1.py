# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

from f144 import simplify


def test_simplify_returns_true_for_whole_product():
    assert simplify("1/5", "5/1") is True


def test_simplify_returns_false_for_fractional_product():
    assert simplify("1/6", "2/5") is False
