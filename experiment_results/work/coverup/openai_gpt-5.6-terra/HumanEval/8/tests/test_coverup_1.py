# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

from script_8 import sum_product


def test_sum_product_empty_list_returns_identity_values():
    assert sum_product([]) == (0, 1)


def test_sum_product_accumulates_sum_and_product_for_all_values():
    assert sum_product([1, -2, 3, 0]) == (2, 0)
