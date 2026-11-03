# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_found():
    """Covers lines 3-6: a pair summing to zero exists, so True is returned."""
    # Pair found at the very first comparison (i=0, j=1).
    assert pairs_sum_to_zero([1, -1]) is True
    # Pair found later in the iteration, exercising more loop iterations.
    assert pairs_sum_to_zero([2, 4, 9, -9, 1]) is True
    # Zero paired with itself counts as a valid distinct pair.
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_not_found():
    """Covers lines 3-5 and 7: no pair sums to zero, so False is returned."""
    assert pairs_sum_to_zero([1, 3, 5, 7]) is False
    assert pairs_sum_to_zero([1, 2, -3]) is False


def test_pairs_sum_to_zero_edge_cases():
    """Covers line 3 falling through to line 7 for empty/single-element lists."""
    assert pairs_sum_to_zero([]) is False
    assert pairs_sum_to_zero([5]) is False
