# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_true():
    """Covers lines 3-6: outer loop, inner loop, condition, and True return."""
    assert pairs_sum_to_zero([1, -1]) is True


def test_pairs_sum_to_zero_false():
    """Covers lines 3-5 and 7: loops run, condition is False, returns False."""
    assert pairs_sum_to_zero([1, 2, 3]) is False


def test_pairs_sum_to_zero_empty():
    """Covers line 3 and 7 with zero outer-loop iterations (empty list branch)."""
    assert pairs_sum_to_zero([]) is False


def test_pairs_sum_to_zero_single_element():
    """Covers line 3-4 with zero inner-loop iterations (single element branch)."""
    assert pairs_sum_to_zero([5]) is False


def test_pairs_sum_to_zero_pair_later_in_list():
    """Covers lines 3-6 where the zero-sum pair is not the first two elements."""
    assert pairs_sum_to_zero([3, 5, 2, -2, 9]) is True
