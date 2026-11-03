# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_composite_executes_loop_and_return():
    # Exercises lines 3-5: the loop runs over 9, 8, 7, 6 (false branch of the
    # `if` on line 4) before returning 5 (true branch on line 5).
    assert largest_divisor(10) == 5


def test_largest_divisor_prime_falls_through_to_one():
    # Exercises the false branch of the `if` repeatedly (6, 5, 4, 3, 2 are
    # not divisors of 7) before returning 1 on the final iteration.
    assert largest_divisor(7) == 1


def test_largest_divisor_immediate_hit():
    # Exercises the true branch of the `if` on the very first iteration:
    # reversed(range(2)) yields [1] and 2 % 1 == 0.
    assert largest_divisor(2) == 1


def test_largest_divisor_even():
    # reversed(range(4)) yields 3 (false branch), then 2 (true branch).
    assert largest_divisor(4) == 2
