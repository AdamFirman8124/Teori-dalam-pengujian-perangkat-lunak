# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_composite():
    # Executes line 3 (loop), line 4 (condition, both False and True
    # outcomes) and line 5 (return) for composite numbers.
    assert largest_divisor(4) == 2
    assert largest_divisor(10) == 5
    assert largest_divisor(100) == 50


def test_largest_divisor_prime():
    # For a prime, every candidate i > 1 fails the condition (False branch)
    # until i == 1 succeeds (True branch) and line 5 returns.
    assert largest_divisor(7) == 1
    assert largest_divisor(13) == 1


def test_largest_divisor_smallest_valid_case():
    # n == 2: reversed(range(2)) == [1, 0]; i == 1 divides 2 immediately.
    assert largest_divisor(2) == 1


def test_largest_divisor_non_positive_returns_none():
    # For n <= 0, range(n) is empty, so the loop body (lines 4-5) never
    # runs and the function falls through, implicitly returning None.
    assert largest_divisor(0) is None
    assert largest_divisor(-6) is None


def test_largest_divisor_one_raises_zero_division():
    # n == 1 makes the loop iterate with i == 0, so n % i divides by zero.
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)
