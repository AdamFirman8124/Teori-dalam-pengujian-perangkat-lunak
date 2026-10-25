# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

from f128 import prod_signs


def test_prod_signs_returns_none_for_empty_input():
    assert prod_signs([]) is None


def test_prod_signs_returns_zero_when_input_contains_zero():
    assert prod_signs([-2, 0, 3]) == 0


def test_prod_signs_handles_positive_and_negative_products():
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, 2, 3]) == -6
    assert prod_signs([-1, -2, 3]) == 6
