# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

"""Tests for f096.count_up_to.

These tests execute every line and branch of count_up_to:
  - line 3 (primes = []) and line 12 (return): every call
  - line 4 with an empty range (n <= 2) and a non-empty range (n > 2)
  - line 5 (is_prime = True)
  - line 6 with an empty inner range (i == 2) and a non-empty one (i > 2)
  - line 7 both branches: i % j == 0 (e.g. i == 4, j == 2) and != 0 (e.g. i == 3, j == 2)
  - lines 8-9 (is_prime = False; break)
  - line 10 both branches (is_prime True and False)
  - line 11 (primes.append(i))

count_up_to is a pure function with no side effects, so no monkeypatching
or cleanup is required; the tests are self-contained and stateless.
"""

import pytest

from f096 import count_up_to


def test_count_up_to_full_branch_coverage():
    """n=10 exercises every line and both branches of every condition."""
    assert count_up_to(10) == [2, 3, 5, 7]


@pytest.mark.parametrize("n", [0, 1, 2])
def test_count_up_to_empty_range(n):
    """For n <= 2 the outer loop body never runs; result is empty."""
    assert count_up_to(n) == []


def test_count_up_to_first_prime():
    """i == 2 skips the inner loop entirely (empty range) and is appended."""
    assert count_up_to(3) == [2]


def test_count_up_to_composite_skipped():
    """i == 4 takes the i % j == 0 branch, sets is_prime=False and breaks."""
    assert count_up_to(5) == [2, 3]


def test_count_up_to_bound_is_exclusive():
    """n itself is never included, even when prime."""
    assert count_up_to(7) == [2, 3, 5]
    assert count_up_to(8) == [2, 3, 5, 7]


def test_count_up_to_larger_n():
    """Sanity check on a larger input verifying correctness of all primes."""
    assert count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
