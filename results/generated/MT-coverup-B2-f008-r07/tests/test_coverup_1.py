# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

from f008 import sum_product


def test_sum_product_empty_list():
    """Covers lines 6-7 (initialization) and 12 (return) with no loop iterations."""
    assert sum_product([]) == (0, 1)


def test_sum_product_single_element():
    """Covers one loop iteration (lines 9-11)."""
    assert sum_product([5]) == (5, 5)


def test_sum_product_multiple_elements():
    """Covers multiple loop iterations (lines 9-11)."""
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_with_negatives_and_zero():
    """Covers loop iterations with negative values and zero (lines 9-11)."""
    assert sum_product([-1, 0, 3]) == (2, 0)
