# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

from f128 import prod_signs


def test_prod_signs_returns_none_for_empty_list():
    assert prod_signs([]) is None


def test_prod_signs_returns_zero_when_array_contains_zero():
    assert prod_signs([-2, 0, 3]) == 0


def test_prod_signs_uses_parity_of_negative_values():
    assert prod_signs([-2, 3]) == -5
    assert prod_signs([-2, -3, 4]) == 9
