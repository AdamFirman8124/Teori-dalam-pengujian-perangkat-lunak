# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_all_single_digit():
    assert add_elements([1, 2, 3, 4], 4) == 10


def test_add_elements_filters_three_and_four_digit():
    assert add_elements([111, 21, 3, 4000], 4) == 24
    assert add_elements([111, 21, 3, 4000], 2) == 21


def test_add_elements_k_limits_slice():
    assert add_elements([10, 20, 30, 40, 100], 3) == 60
    assert add_elements([10, 100, 20], 2) == 10
    assert add_elements([5, 6, 7], 10) == 18


def test_add_elements_boundary_two_digits():
    assert add_elements([99, 100, 9, 10], 4) == 118
    assert add_elements([100, 200, 300], 3) == 0


def test_add_elements_k_zero_and_negative_values():
    assert add_elements([1, 2, 3], 0) == 0
    # len(str(-2)) == 2 so included, len(str(-10)) == 3 so excluded
    assert add_elements([1, -2, 100, 20], 4) == 19
    assert add_elements([-10, -5, 15], 3) == 10
