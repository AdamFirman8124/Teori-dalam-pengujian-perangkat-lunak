# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_below_threshold_all_below():
    """All elements strictly below the threshold -> returns True."""
    assert below_threshold([1, 2, 3], 5) is True


def test_below_threshold_empty_list():
    """Empty list has no elements at or above threshold -> returns True."""
    assert below_threshold([], 5) is True


def test_below_threshold_element_equal_to_threshold():
    """An element equal to the threshold triggers early return False."""
    assert below_threshold([1, 5, 3], 5) is False


def test_below_threshold_element_above_threshold():
    """An element above the threshold triggers early return False."""
    assert below_threshold([10], 5) is False


def test_below_threshold_negative_values():
    """Negative values below a positive threshold -> True."""
    assert below_threshold([-10, -5, -1], 0) is True


def test_below_threshold_negative_threshold():
    """Negative threshold with a positive element -> False."""
    assert below_threshold([-3, -2, 1], -1) is False
