# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

from f144 import simplify


def test_simplify_returns_true_for_integer_product():
    assert simplify("1/2", "2/1") is True


def test_simplify_returns_false_for_non_integer_product():
    assert simplify("1/2", "1/1") is False
