# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

"""Tests for f024.largest_divisor.

The function under test is pure (no I/O, no global state), so no
monkeypatching or teardown is required; each test leaves no state behind.
"""

from f024 import largest_divisor


def test_largest_divisor_composite_returns_largest_proper_divisor():
    # Exercises the loop (line 3) over several iterations where the
    # divisibility check on line 4 is False before it becomes True and
    # line 5 returns the answer: 10 % 9..6 != 0, 10 % 5 == 0.
    assert largest_divisor(10) == 5
    # 12 % 11..7 != 0, 12 % 6 == 0.
    assert largest_divisor(12) == 6


def test_largest_divisor_prime_returns_one():
    # A prime forces the loop to run all the way down to i == 1,
    # exercising the False branch of the check many times before returning.
    assert largest_divisor(3) == 1
    assert largest_divisor(7) == 1


def test_largest_divisor_smallest_valid_input_returns_one():
    # n == 2 makes the check succeed on the very first iteration (i == 1),
    # covering the True branch of line 4 immediately.
    assert largest_divisor(2) == 1


def test_largest_divisor_even_number():
    # 4 % 3 != 0 (False branch), then 4 % 2 == 0 (True branch) -> 2.
    assert largest_divisor(4) == 2


def test_largest_divisor_non_positive_returns_none():
    # For n <= 0, range(n) is empty, so the loop body (lines 4-5) never
    # runs and the function falls through to its implicit `return None`.
    # This covers the loop-exhausted exit branch of line 3.
    assert largest_divisor(0) is None
    assert largest_divisor(-6) is None
