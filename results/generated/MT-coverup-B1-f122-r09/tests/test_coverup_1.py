# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_sums_values_with_at_most_two_digit_strings():
    values = [1, 12, 123, -9, 1000]

    result = add_elements(values, 4)

    assert result == 4


def test_add_elements_uses_only_the_first_k_elements():
    values = [10, 20, 30]

    result = add_elements(values, 2)

    assert result == 30


def test_add_elements_returns_zero_for_an_empty_slice():
    assert add_elements([1, 2, 3], 0) == 0
