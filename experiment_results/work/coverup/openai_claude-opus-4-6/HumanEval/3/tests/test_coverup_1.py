# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

from typing import List

import pytest

import script_3
from script_3 import below_zero

class TrackingList(list):
    """A list that records how many items were actually iterated over."""

    def __init__(self, *args):
        super().__init__(*args)
        self.iterated = 0

    def __iter__(self):
        for item in super().__iter__():
            self.iterated += 1
            yield item

def test_module_exports_callable():
    """Sanity check: the real function from script_3 is imported, not redefined."""
    assert callable(below_zero)
    assert below_zero is script_3.below_zero
    assert below_zero.__module__ == "script_3"

def test_below_zero_empty_list_returns_false():
    """Empty operations: the loop body is skipped and the final return runs."""
    result = below_zero([])

    assert result is False
    assert isinstance(result, bool)

def test_below_zero_never_negative_returns_false():
    """All balances stay >= 0, so the loop completes and the final return runs."""
    assert below_zero([1, 2, 3]) is False
    assert below_zero([0, 0, 0]) is False
    assert below_zero([5, -5, 1, -1, 2]) is False

def test_below_zero_exact_zero_is_not_below_zero():
    """Boundary check: a balance of exactly 0 must NOT trigger the True branch."""
    assert below_zero([1, -1]) is False

def test_below_zero_returns_true_when_balance_goes_negative():
    """A negative running balance takes the early return True branch."""
    assert below_zero([1, 2, -4, 5]) is True
    assert below_zero([-1]) is True
    assert below_zero([10, -20, 100]) is True

def test_below_zero_returns_early_on_first_negative_balance():
    """The function must return True as soon as the balance drops below zero."""
    operations = TrackingList([1, -2, 5, 7])

    result = below_zero(operations)

    assert result is True
    # Only the first two operations should have been consumed before returning.
    assert operations.iterated == 2

def test_below_zero_iterates_full_input_when_never_negative():
    """When no negative balance occurs, every operation is consumed."""
    operations = TrackingList([1, 1, 1])

    result = below_zero(operations)

    assert result is False
    assert operations.iterated == len(operations)

def test_below_zero_does_not_mutate_input():
    """The input list must be left unchanged (no state pollution)."""
    operations = [1, 2, -4, 5]
    snapshot = list(operations)

    below_zero(operations)

    assert operations == snapshot

def test_below_zero_matches_doctests():
    """The documented examples must hold for the imported function."""
    assert below_zero([1, 2, 3]) is False
    assert below_zero([1, 2, -4, 5]) is True
