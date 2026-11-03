# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

"""Tests for f109.move_one_ball covering lines 3-14.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required; each test is self-contained and
leaves no state behind.
"""

from f109 import move_one_ball


def test_empty_array_returns_true():
    """Covers lines 3-4: empty input short-circuits to True."""
    assert move_one_ball([]) is True


def test_single_element_returns_true():
    """Covers lines 5-10, 11 and 14: single element is trivially sortable."""
    assert move_one_ball([7]) is True


def test_already_sorted_returns_true():
    """Covers lines 5-10, 11 and 14 with min_index == 0 (no rotation needed)."""
    assert move_one_ball([1, 2, 3, 4]) is True


def test_rotated_sorted_array_returns_true():
    """Covers lines 5-10, 11 and 14 with min_index > 0 (a valid rotation)."""
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_unsortable_array_returns_false():
    """Covers lines 12-13: mismatch inside the loop triggers early False."""
    assert move_one_ball([3, 5, 4, 1, 2]) is False


def test_duplicates_unsortable_returns_false():
    """Covers lines 12-13 with duplicate minimum values."""
    # min=1 at index 1 -> rotation [1, 3, 1, 2] != sorted [1, 1, 2, 3]
    assert move_one_ball([2, 1, 3, 1]) is False


def test_duplicates_sortable_returns_true():
    """Covers lines 5-10, 11 and 14 with duplicate minimum values."""
    # min=1 at index 2 -> rotation [1, 1, 2, 2, 3] == sorted array
    assert move_one_ball([2, 3, 1, 1, 2]) is True
