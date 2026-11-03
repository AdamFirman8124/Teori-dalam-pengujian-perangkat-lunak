# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list_returns_zero():
    """Covers lines 4, 5 (loop-exit branch) and 12."""
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_ignored():
    """Covers the False branch of 'if num > 10' (line 6)."""
    # 10 is not strictly greater than 10; negatives and small numbers also skipped.
    assert specialFilter([10, 5, 0, -15, -33]) == 0


def test_numbers_greater_than_ten_with_even_digits_are_ignored():
    """Covers lines 7, 8 and the False branch of line 9.

    - 22: first digit 2 is even (short-circuits the 'and').
    - 12: first digit 1 is odd but last digit 2 is even.
    """
    assert specialFilter([22, 12]) == 0


def test_numbers_with_odd_first_and_last_digits_are_counted():
    """Covers the True branch of line 9 and line 10 (count += 1)."""
    # 15 -> first 1, last 5; 33 -> first 3, last 3; 97 -> first 9, last 7; 111 -> 1 and 1.
    assert specialFilter([15, 33, 97, 111]) == 4


def test_mixed_list():
    """Exercises every branch in a single call: empty-ish, <=10, >10 rejected, >10 accepted."""
    result = specialFilter([15, -2, 11, 22, 33, 10, 97, 5])
    # Counted: 15, 11, 33, 97 -> 4
    assert result == 4


def test_result_is_always_non_negative_int():
    """Sanity check on the return type/value for a list with no qualifying numbers."""
    result = specialFilter([24, 68, 100])
    assert result == 0
    assert isinstance(result, int)
