# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true():
    """Covers lines 3-6: a pair summing to zero is found (True branch of line 5)."""
    assert pairs_sum_to_zero([1, 3, 5, -1]) is True


def test_pairs_sum_to_zero_zero_pair():
    """Covers lines 3-6 with a zero pair (0 + 0 == 0)."""
    assert pairs_sum_to_zero([0, 0]) is True


def test_pairs_sum_to_zero_false():
    """Covers lines 3-5 (False branch of line 5) and line 7."""
    assert pairs_sum_to_zero([1, 2, 3, 4]) is False


def test_pairs_sum_to_zero_empty_list():
    """Covers line 3 with zero outer-loop iterations, then line 7."""
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    """Covers line 3 with one iteration and line 4 with zero inner iterations."""
    assert pairs_sum_to_zero([7]) is False


def test_pairs_sum_to_zero_single_zero():
    """A lone zero cannot pair with itself; covers lines 3-4 (empty inner loop) and 7."""
    assert pairs_sum_to_zero([0]) is False


def test_pairs_sum_to_zero_pair_at_end():
    """Ensures the inner loop scans all j > i before returning False (line 4 fully iterated)."""
    assert pairs_sum_to_zero([2, 3, 4, -2]) is True


def test_pairs_sum_to_zero_does_not_mutate_input():
    """The function must be side-effect free: input list is unchanged afterwards."""
    lst = [1, -1, 2, 3]
    snapshot = list(lst)
    result = pairs_sum_to_zero(lst)
    assert result is True
    assert lst == snapshot
