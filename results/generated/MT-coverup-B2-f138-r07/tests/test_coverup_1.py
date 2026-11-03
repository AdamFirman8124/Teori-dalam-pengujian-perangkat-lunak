# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


def test_true_when_even_and_at_least_eight():
    """Even n >= 8: both operands of 'and' evaluate, result is True."""
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True
    assert is_equal_to_sum_even(100) is True


def test_false_when_even_but_below_eight():
    """Even n < 8: both operands of 'and' evaluate, second is False."""
    assert is_equal_to_sum_even(0) is False
    assert is_equal_to_sum_even(2) is False
    assert is_equal_to_sum_even(6) is False
    assert is_equal_to_sum_even(-4) is False


def test_false_when_odd_short_circuits():
    """Odd n: first operand of 'and' is False, short-circuits before n >= 8."""
    assert is_equal_to_sum_even(1) is False
    assert is_equal_to_sum_even(7) is False
    # Odd but large: still False because parity check fails first.
    assert is_equal_to_sum_even(9) is False
    assert is_equal_to_sum_even(-3) is False
