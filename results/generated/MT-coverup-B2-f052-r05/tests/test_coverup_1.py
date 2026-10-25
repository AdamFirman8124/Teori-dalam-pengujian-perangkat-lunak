# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_below_threshold_all_below():
    """All elements strictly below t -> True (covers lines 3-4, 6)."""
    assert below_threshold([1, 2, 3], 10) is True


def test_below_threshold_empty_list():
    """Empty list -> True (covers line 6 only, loop body never runs)."""
    assert below_threshold([], 5) is True


def test_below_threshold_element_equal_to_threshold():
    """Element equal to t -> False (covers line 5 via the >= branch)."""
    assert below_threshold([1, 5, 2], 5) is False


def test_below_threshold_element_above_threshold():
    """Element above t -> False (covers line 5)."""
    assert below_threshold([1, 7], 5) is False


def test_below_threshold_negative_values():
    """Negative elements and negative threshold behave correctly."""
    assert below_threshold([-3, -1], 0) is True
    assert below_threshold([-3, 0], -1) is False
