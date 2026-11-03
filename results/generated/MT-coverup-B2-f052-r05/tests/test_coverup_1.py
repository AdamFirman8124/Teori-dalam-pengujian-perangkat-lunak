# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

"""Tests for f052.below_threshold, covering all lines and branches."""

from f052 import below_threshold


def test_below_threshold_all_elements_below_returns_true():
    """Covers lines 3, 4 (False branch) and 6: loop runs, no element >= t."""
    assert below_threshold([1, 2, 3], 10) is True


def test_below_threshold_empty_list_returns_true():
    """Covers line 3 (loop-not-taken branch) and line 6: empty list."""
    assert below_threshold([], 5) is True


def test_below_threshold_element_equal_to_threshold_returns_false():
    """Covers lines 3, 4 (True branch) and 5: element == t triggers early return."""
    assert below_threshold([1, 2, 3], 3) is False


def test_below_threshold_element_above_threshold_returns_false():
    """Covers lines 3, 4 (True branch) and 5: element > t triggers early return."""
    assert below_threshold([1, 7, 2], 5) is False


def test_below_threshold_single_element_below_returns_true():
    """Covers lines 3, 4 (False branch) and 6 with a single-element list."""
    assert below_threshold([0], 1) is True
