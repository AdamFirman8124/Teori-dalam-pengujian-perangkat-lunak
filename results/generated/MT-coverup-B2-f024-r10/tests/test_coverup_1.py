# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_composite():
    """n=10 enters the loop (line 3), takes the False branch of the modulo
    check for i=9..6 (line 4), then the True branch and returns 5 (line 5)."""
    assert largest_divisor(10) == 5


def test_largest_divisor_prime():
    """For a prime, the modulo check is False for every i down to 2, then
    True for i=1; exercises many False iterations before returning."""
    assert largest_divisor(7) == 1


def test_largest_divisor_smallest_valid_input():
    """n=2: loop runs once with i=1, check is immediately True, returns 1."""
    assert largest_divisor(2) == 1


def test_largest_divisor_one_raises_zero_division():
    """n=1: loop is entered (line 3) but i=0 makes 'n % i' raise
    ZeroDivisionError before the if can be evaluated."""
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)


def test_largest_divisor_nonpositive_input_returns_none():
    """n <= 0 makes range(n) empty, so the loop body (lines 4-5) never runs
    and the function falls off the end, returning None. This covers the
    loop-exit branch of the for statement."""
    assert largest_divisor(0) is None
    assert largest_divisor(-3) is None
