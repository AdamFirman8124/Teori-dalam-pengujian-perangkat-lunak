# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true():
    """A list containing a pair of opposite numbers returns True (covers lines 3-6)."""
    assert pairs_sum_to_zero([1, 3, 5, 0, -3]) is True


def test_pairs_sum_to_zero_true_zeros():
    """Two zeros sum to zero, so the result is True (covers lines 3-6)."""
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_pair_at_end():
    """The zero-sum pair appears late in the list; the inner loop must run fully (covers lines 3-6)."""
    assert pairs_sum_to_zero([2, 4, 6, -6]) is True


def test_pairs_sum_to_zero_false():
    """A list with no zero-sum pair returns False (covers lines 3-5 and 7)."""
    assert pairs_sum_to_zero([1, 3, 5, 7]) is False


def test_pairs_sum_to_zero_empty():
    """An empty list has no pairs, so the result is False (covers line 3 only)."""
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    """A single-element list has no pairs, so the result is False (covers lines 3-4, 7)."""
    assert pairs_sum_to_zero([1]) is False


def test_pairs_sum_to_zero_no_self_pairing():
    """An element must not pair with itself: a lone zero cannot sum with itself (covers lines 3-5, 7)."""
    assert pairs_sum_to_zero([0]) is False


def test_pairs_sum_to_zero_duplicates_not_opposites():
    """Duplicate values that do not sum to zero still yield False (covers lines 3-5, 7)."""
    assert pairs_sum_to_zero([1, 1, 2]) is False
