# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    """Positive number with both even and odd digits exercises every line,
    including both branches of the if/else."""
    assert even_odd_count(123) == (1, 2)


def test_even_odd_count_negative_number():
    """Negative input goes through abs() before digit inspection."""
    assert even_odd_count(-12) == (1, 1)


def test_even_odd_count_zero_is_even():
    """Zero counts as an even digit."""
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_all_even_digits():
    """Only the even branch of the loop body executes."""
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd_digits():
    """Only the odd branch of the loop body executes."""
    assert even_odd_count(13579) == (0, 5)


def test_even_odd_count_returns_tuple_type():
    """Postcondition: result is a tuple of two non-negative ints summing
    to the number of digits."""
    result = even_odd_count(-4056)
    assert isinstance(result, tuple)
    even_count, odd_count = result
    assert even_count >= 0 and odd_count >= 0
    assert even_count + odd_count == len(str(abs(-4056)))
    assert result == (3, 1)
