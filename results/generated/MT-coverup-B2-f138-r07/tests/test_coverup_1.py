# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f138 import is_equal_to_sum_even


def test_odd_returns_false_short_circuit():
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(9) is False


def test_even_below_8_returns_false():
    assert is_equal_to_sum_even(2) is False
    assert is_equal_to_sum_even(4) is False
    assert is_equal_to_sum_even(6) is False


def test_even_at_least_8_returns_true():
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True
    assert is_equal_to_sum_even(28) is True
