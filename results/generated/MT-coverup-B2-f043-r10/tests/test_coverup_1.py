# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true_when_opposites_present():
    """Covers lines 3-6: outer loop, inner loop, condition true, return True."""
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) is True


def test_pairs_sum_to_zero_true_simple_pair():
    """Covers lines 3-6 with the earliest possible match."""
    assert pairs_sum_to_zero([1, -1]) is True


def test_pairs_sum_to_zero_true_with_zero_pair():
    """Two zeros sum to zero; covers lines 3-6."""
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_false_no_matching_pair():
    """Covers lines 3-5 (condition false) and line 7 (return False)."""
    assert pairs_sum_to_zero([1, 3, 5, 0]) is False


def test_pairs_sum_to_zero_false_all_positive():
    """Covers lines 3-5 and 7 with a longer list."""
    assert pairs_sum_to_zero([1, 2, 3, 4]) is False


def test_pairs_sum_to_zero_false_negative_only():
    """Covers lines 3-5 and 7 with negative values."""
    assert pairs_sum_to_zero([-1, -2, -3]) is False


def test_pairs_sum_to_zero_empty_list():
    """Covers line 3 with the outer loop body never executing, then line 7."""
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    """Covers line 3 and line 7; inner loop (line 4) never executes."""
    assert pairs_sum_to_zero([1]) is False


def test_pairs_sum_to_zero_does_not_mutate_input():
    """Postcondition: the input list is not modified by the call."""
    data = [2, 4, -5, 3, 5, 7]
    snapshot = list(data)
    result = pairs_sum_to_zero(data)
    assert result is True
    assert data == snapshot
