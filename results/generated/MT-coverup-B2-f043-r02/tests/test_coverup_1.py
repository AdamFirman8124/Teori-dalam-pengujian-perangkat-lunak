# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

"""Tests for f043.pairs_sum_to_zero.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required; each test operates
only on local list literals, guaranteeing no state pollution between tests.
"""

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true():
    """A pair summing to zero exists -> True (covers lines 3-6)."""
    assert pairs_sum_to_zero([1, 3, -2, 2]) is True


def test_pairs_sum_to_zero_false():
    """No pair sums to zero -> False (covers lines 3-5 and 7)."""
    assert pairs_sum_to_zero([1, 2, 3]) is False


def test_pairs_sum_to_zero_empty_list():
    """Empty list -> loop body never runs, returns False (line 7)."""
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    """Single element -> no pair possible, returns False (line 7)."""
    assert pairs_sum_to_zero([5]) is False


def test_pairs_sum_to_zero_zero_pair():
    """Two zeros sum to zero -> True; a lone zero -> False."""
    assert pairs_sum_to_zero([0, 0]) is True
    assert pairs_sum_to_zero([0]) is False


def test_pairs_sum_to_zero_pair_at_end():
    """Pair summing to zero found only at the last position -> True."""
    assert pairs_sum_to_zero([1, 2, 3, -3]) is True


def test_pairs_sum_to_zero_negative_first():
    """Negative element followed by its positive counterpart -> True."""
    assert pairs_sum_to_zero([-7, 4, 7]) is True


def test_pairs_sum_to_zero_no_false_positive():
    """Same-sign values and non-opposite magnitudes -> False."""
    assert pairs_sum_to_zero([-1, -2, -3]) is False
    assert pairs_sum_to_zero([2, -3, 4]) is False
