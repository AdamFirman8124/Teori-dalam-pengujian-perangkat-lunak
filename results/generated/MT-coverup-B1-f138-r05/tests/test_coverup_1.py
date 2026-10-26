# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f138 import is_equal_to_sum_even


def test_is_equal_to_sum_even_returns_true_for_even_number_at_least_eight():
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True


def test_is_equal_to_sum_even_returns_false_for_odd_or_small_even_numbers():
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(6) is False
