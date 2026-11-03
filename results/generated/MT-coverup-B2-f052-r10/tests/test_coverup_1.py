# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_below_threshold_empty_list():
    """Empty list: loop body never runs, so lines 3 and 6 execute."""
    assert below_threshold([], 5) is True


def test_below_threshold_all_below():
    """All elements strictly below threshold: lines 3, 4, 6 execute."""
    assert below_threshold([1, 2, 3], 10) is True


def test_below_threshold_element_at_threshold():
    """Element equal to threshold triggers the False branch (lines 3, 4, 5)."""
    assert below_threshold([1, 5, 2], 5) is False


def test_below_threshold_element_above_threshold():
    """Element greater than threshold triggers the False branch (lines 3, 4, 5)."""
    assert below_threshold([1, 2, 100], 3) is False
