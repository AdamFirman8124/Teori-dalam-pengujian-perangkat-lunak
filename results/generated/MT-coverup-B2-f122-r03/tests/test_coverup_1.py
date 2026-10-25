# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_sums_only_one_and_two_digit_values_within_k():
    assert add_elements([1, 20, 300, 4], 3) == 21


def test_add_elements_with_empty_selected_slice():
    assert add_elements([10, 20], 0) == 0
