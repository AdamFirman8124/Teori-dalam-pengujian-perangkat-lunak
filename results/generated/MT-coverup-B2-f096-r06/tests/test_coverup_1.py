# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

"""Tests for f096.count_up_to.

The function under test is pure (no I/O, no module state, no globals), so no
monkeypatching or teardown is required; each test leaves no state behind.

Coverage plan:
- count_up_to(10): executes lines 3-12, including the composite branch
  (i % j == 0 -> is_prime = False -> break) and the non-prime path of
  `if is_prime`.
- count_up_to(2) / count_up_to(0) / count_up_to(-1): outer loop never runs
  (False branch of the `for i in range(2, n)` loop).
- count_up_to(3): i == 2 so the inner `for j in range(2, i)` loop never runs
  (False branch of the inner loop), while `if is_prime` takes the True branch.
- Boundary checks confirm n is an exclusive upper bound.
"""

import pytest

from f096 import count_up_to


def test_count_up_to_primes_and_composites():
    """Full execution: primes collected, composites rejected via break."""
    assert count_up_to(10) == [2, 3, 5, 7]


def test_count_up_to_empty_for_n_at_or_below_two():
    """Outer loop body never executes when n <= 2."""
    assert count_up_to(2) == []
    assert count_up_to(1) == []
    assert count_up_to(0) == []
    assert count_up_to(-1) == []


def test_count_up_to_inner_loop_skipped_for_first_prime():
    """For i == 2 the inner loop range(2, 2) is empty; 2 is still prime."""
    assert count_up_to(3) == [2]


def test_count_up_to_upper_bound_is_exclusive():
    """n itself must not be included even when it is prime."""
    assert count_up_to(7) == [2, 3, 5]
    assert count_up_to(8) == [2, 3, 5, 7]


def test_count_up_to_larger_range():
    """Sanity check on a slightly larger input exercising many iterations."""
    assert count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_count_up_to_returns_new_list_each_call():
    """No shared state between calls: each invocation returns a fresh list."""
    first = count_up_to(5)
    second = count_up_to(5)
    assert first == second == [2, 3]
    assert first is not second
