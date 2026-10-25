# file: project/f128/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 5]]}

from f128 import prod_signs


def test_prod_signs_covers_empty_zero_positive_and_negative_inputs():
    assert prod_signs([]) is None
    assert prod_signs([0, -2, 3]) == 0
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, 2]) == -3
    assert prod_signs([-1, -2, 3]) == 6
