# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

from script_8 import sum_product


def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)


def test_sum_product_nonempty_list():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_with_zero_and_negative_numbers():
    assert sum_product([-2, 0, 5]) == (3, 0)
