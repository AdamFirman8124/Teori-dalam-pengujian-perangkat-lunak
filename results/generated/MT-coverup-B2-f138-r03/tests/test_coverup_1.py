# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f138 import is_equal_to_sum_even


def test_is_equal_to_sum_even_true_when_even_and_at_least_eight():
    """Covers the branch where n % 2 == 0 is True and n >= 8 is True."""
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True
    assert is_equal_to_sum_even(100) is True


def test_is_equal_to_sum_even_false_when_even_but_below_eight():
    """Covers the branch where n % 2 == 0 is True but n >= 8 is False."""
    assert is_equal_to_sum_even(6) is False
    assert is_equal_to_sum_even(2) is False
    assert is_equal_to_sum_even(0) is False


def test_is_equal_to_sum_even_false_when_odd():
    """Covers the short-circuit branch where n % 2 == 0 is False."""
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(9) is False
    assert is_equal_to_sum_even(-3) is False
