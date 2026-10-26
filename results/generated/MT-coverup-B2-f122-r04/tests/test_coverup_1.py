# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_basic_sum():
    assert add_elements([1, 2, 3, 100, 200], 3) == 6


def test_add_elements_filters_three_digit_numbers():
    assert add_elements([10, 100, 20, 1000], 4) == 30


def test_add_elements_k_limits_slice():
    assert add_elements([5, 6, 7, 8], 2) == 11


def test_add_elements_k_larger_than_len():
    assert add_elements([1, 2], 5) == 3


def test_add_elements_empty_and_zero_k():
    assert add_elements([], 0) == 0
    assert add_elements([1, 2, 3], 0) == 0


def test_add_elements_all_filtered_out():
    assert add_elements([100, 1000, 1234], 3) == 0


def test_add_elements_boundary_two_digits():
    assert add_elements([99, 100, -5, -10], 4) == 99 + (-5)
    assert add_elements([10, 99], 2) == 109
