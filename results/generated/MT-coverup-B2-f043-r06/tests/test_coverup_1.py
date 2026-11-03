# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

"""Tests for f043.pairs_sum_to_zero achieving full line and branch coverage.

pairs_sum_to_zero is a pure function: it mutates nothing, touches no globals,
files, or module-level state, so no monkeypatching/teardown is required to
avoid state pollution.
"""

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_returns_true_when_pair_exists():
    # Covers lines 3-5 (outer loop, inner loop, and the if taking the True
    # branch) and line 6 (the `return True`).
    assert pairs_sum_to_zero([1, 3, -3, 5]) is True


def test_pairs_sum_to_zero_with_two_zeros():
    # 0 + 0 == 0; covers lines 3-6 through a different value pattern.
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_returns_false_when_no_pair_exists():
    # Covers lines 3-5 with the if taking the False branch on every
    # iteration, and line 7 (`return False`) reached after both loops
    # complete normally.
    assert pairs_sum_to_zero([1, 2, 3, 4]) is False


def test_pairs_sum_to_zero_empty_list():
    # Covers the outer loop being skipped entirely (line 3 executes with an
    # empty iterable) and line 7 reached directly.
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    # Covers line 3 executing, the inner loop on line 4 never running
    # (range(1, 1) is empty), and line 7 reached.
    assert pairs_sum_to_zero([1]) is False


def test_pairs_sum_to_zero_true_only_with_later_element():
    # Ensures the inner loop actually runs multiple times: the matching
    # element comes after several non-matching ones, exercising the False
    # branch of the if before the True branch on the final iteration.
    assert pairs_sum_to_zero([2, 3, 4, -2]) is True
