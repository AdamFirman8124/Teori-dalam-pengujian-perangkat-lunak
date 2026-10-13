# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

from typing import List, Tuple

from script_8 import sum_product


def test_sum_product_empty_list():
    result = sum_product([])
    assert result == (0, 1)
    assert isinstance(result, tuple)
    assert result[0] == 0
    assert result[1] == 1


def test_sum_product_single_element():
    assert sum_product([5]) == (5, 5)


def test_sum_product_multiple_elements():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_includes_zero():
    assert sum_product([1, 0, 3]) == (4, 0)


def test_sum_product_negative_numbers():
    assert sum_product([-1, -2, -3]) == (-6, -6)
    assert sum_product([-1, 2, -3]) == (-2, 6)


def test_sum_product_returns_tuple_of_ints():
    result = sum_product([2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)
