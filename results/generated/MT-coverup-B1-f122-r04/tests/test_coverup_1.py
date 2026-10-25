# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_all_short():
    # All elements have at most 2 digits: all are summed.
    assert add_elements([1, 22, 33, 4], 3) == 1 + 22 + 33


def test_add_elements_filters_long():
    # Elements with more than 2 digits are excluded from the sum.
    assert add_elements([111, 22, 3, 456], 4) == 22 + 3


def test_add_elements_k_limits_slice():
    # Only the first k elements are considered.
    assert add_elements([5, 999, 7], 2) == 5


def test_add_elements_empty():
    assert add_elements([], 3) == 0


def test_add_elements_k_zero():
    assert add_elements([1, 2, 3], 0) == 0


def test_add_elements_negative_numbers():
    # str(-5) == "-5" (len 2) counts; str(-99) == "-99" (len 3) is excluded.
    assert add_elements([-5, -99, -100], 3) == -5


def test_add_elements_negative_boundary():
    # str(-9) has len 2 (included); str(-10) has len 3 (excluded).
    assert add_elements([-9, -10, 0], 3) == -9
