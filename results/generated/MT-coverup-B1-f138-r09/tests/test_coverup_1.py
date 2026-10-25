# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f138 import is_equal_to_sum_even


def test_even_number_at_least_eight_is_accepted():
    assert is_equal_to_sum_even(8) is True


def test_even_number_below_eight_is_rejected():
    assert is_equal_to_sum_even(6) is False


def test_odd_number_is_rejected():
    assert is_equal_to_sum_even(9) is False
