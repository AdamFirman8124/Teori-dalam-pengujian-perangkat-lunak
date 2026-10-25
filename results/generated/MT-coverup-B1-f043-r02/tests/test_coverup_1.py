# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true():
    # Branch where l1 + l[j] == 0 -> returns True (lines 5-6)
    assert pairs_sum_to_zero([1, 3, -3, 7]) is True
    assert pairs_sum_to_zero([2, 4, -2, -2]) is True


def test_pairs_sum_to_zero_false():
    # Loop completes without finding a pair -> returns False (line 7)
    assert pairs_sum_to_zero([1, 3, 5, 7]) is False


def test_pairs_sum_to_zero_empty():
    # Outer loop body never runs (line 3 iterates zero times) -> False
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    # Inner range(i+1, len(l)) is empty -> False
    assert pairs_sum_to_zero([0]) is False


def test_pairs_sum_to_zero_zero_pair():
    # Two zeros sum to zero -> True
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_no_mutation():
    # Verify the input list is not modified (no state pollution)
    data = [1, -1, 2]
    snapshot = list(data)
    pairs_sum_to_zero(data)
    assert data == snapshot
