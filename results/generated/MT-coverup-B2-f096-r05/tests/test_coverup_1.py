# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

"""Tests for f096.count_up_to.

count_up_to is a pure function (no module state, no I/O), so no
monkeypatching or teardown is required; each test leaves no state behind.

Coverage targets:
- line 3 (primes = []), line 4 loop, line 12 (return): every call.
- line 4 loop *not* taken branch: n <= 2.
- lines 5, 6, 10, 11: n > 2 (i == 2, inner loop empty).
- lines 7, 8, 9 (divisibility check, break): a composite i (n >= 5).
- line 7 both branches: i == 3 (False) and i == 4 (True).
- line 10 both branches: prime appended vs composite skipped.
"""

import pytest

from f096 import count_up_to


def test_count_up_to_below_first_prime():
    """n <= 2: range(2, n) is empty, so the loop body never runs."""
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(2) == []


def test_count_up_to_negative_n():
    """Negative n also yields an empty range(2, n)."""
    assert count_up_to(-7) == []


def test_count_up_to_single_prime():
    """n == 3: only candidate is i == 2, whose inner loop range(2, 2) is empty."""
    result = count_up_to(3)
    assert result == [2]
    assert isinstance(result, list)


def test_count_up_to_composite_is_skipped():
    """n == 5: i == 4 is divisible by j == 2, exercising the if-True branch,
    the is_prime = False assignment and the break (lines 7-9)."""
    assert count_up_to(5) == [2, 3]


def test_count_up_to_typical():
    """Larger input covers both branches of the divisibility test and of
    the is_prime check (primes appended, composites skipped)."""
    assert count_up_to(10) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_count_up_to_returns_new_list_each_call():
    """Postcondition: each call returns a fresh list (no shared state)."""
    first = count_up_to(10)
    second = count_up_to(10)
    assert first == second == [2, 3, 5, 7]
    assert first is not second
