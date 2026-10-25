# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

from f008 import sum_product


def test_sum_product_with_numbers():
    assert sum_product([2, 3, 4]) == (9, 24)


def test_sum_product_with_empty_list():
    assert sum_product([]) == (0, 1)
