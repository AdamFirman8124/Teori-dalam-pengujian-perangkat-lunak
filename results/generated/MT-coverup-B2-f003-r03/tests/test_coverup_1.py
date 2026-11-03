# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

"""Tests for f003.below_zero covering all lines and branches (lines 6-13).

The function under test is pure (no I/O, no globals, no mutation of its
argument), so no monkeypatching/teardown is required; passing fresh literal
lists guarantees no state pollution between tests.
"""

import pytest

from f003 import below_zero


def test_below_zero_true_when_balance_drops_midway():
    # Covers: balance init (6), loop (8), accumulation (9),
    # if-True branch (10) after several non-negative iterations, return True (11).
    assert below_zero([1, 2, -4]) is True


def test_below_zero_true_on_first_operation():
    # Covers: the if-True branch (10) and return True (11) on the very
    # first iteration.
    assert below_zero([-1]) is True


def test_below_zero_false_when_never_negative():
    # Covers: the if-False branch (10) on every iteration and
    # return False (13) after the loop completes.
    assert below_zero([1, 2, 3]) is False


def test_below_zero_false_for_empty_operations():
    # Covers: balance init (6), loop-not-taken branch of the for
    # statement (8), and return False (13).
    assert below_zero([]) is False


def test_below_zero_false_when_balance_touches_zero():
    # Boundary case: balance == 0 is not below zero, so the if-False
    # branch (10) is taken and return False (13) is reached.
    assert below_zero([1, -1]) is False


@pytest.mark.parametrize(
    "operations, expected",
    [
        ([], False),
        ([0], False),
        ([5], False),
        ([-5], True),
        ([1, 2, 3, -7], True),
        ([10, -10, 10, -10], False),
        ([3, -3, 3, -3, -1], True),
    ],
)
def test_below_zero_parametrized(operations, expected):
    # Exercises every line (6, 8, 9, 10, 11, 13) and both outcomes of the
    # conditional across the parameter set.
    assert below_zero(operations) is expected
