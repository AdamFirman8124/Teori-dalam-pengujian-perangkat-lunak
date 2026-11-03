# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_below_threshold_all_below():
    """All elements strictly below t: loop runs (line 3), condition false (line 4), returns True (line 6)."""
    assert below_threshold([1, 2, 3], 10) is True


def test_below_threshold_empty_list():
    """Empty list: loop body never runs, returns True (line 6)."""
    assert below_threshold([], 5) is True


def test_below_threshold_element_at_threshold():
    """Element equal to t triggers e >= t (line 4) and returns False (line 5)."""
    assert below_threshold([1, 5, 2], 5) is False


def test_below_threshold_element_above_threshold():
    """Element greater than t triggers e >= t (line 4) and returns False (line 5)."""
    assert below_threshold([1, 7], 5) is False


def test_below_threshold_first_element_fails():
    """First element already >= t: returns False immediately (lines 4-5)."""
    assert below_threshold([10, 1, 2], 5) is False


def test_below_threshold_negative_numbers():
    """Negative values below threshold return True; negative threshold with larger element returns False."""
    assert below_threshold([-3, -1], 0) is True
    assert below_threshold([-3, -1], -2) is False
