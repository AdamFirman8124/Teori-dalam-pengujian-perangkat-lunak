# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_below_threshold_empty_list_returns_true():
    # Covers line 6 (loop body never runs, falls through to return True)
    assert below_threshold([], 10) is True


def test_below_threshold_all_elements_below_returns_true():
    # Covers lines 3 and 6 (loop iterates, no element >= t)
    assert below_threshold([1, 2, 3], 10) is True


def test_below_threshold_element_at_threshold_returns_false():
    # Covers lines 3, 4, 5 (e >= t triggers early return False)
    assert below_threshold([1, 5, 2], 5) is False


def test_below_threshold_element_above_threshold_returns_false():
    # Covers lines 3, 4, 5
    assert below_threshold([1, 2, 99], 10) is False


def test_below_threshold_first_element_above_returns_false_immediately():
    # Covers lines 3, 4, 5 with early exit on first iteration
    assert below_threshold([10, 1, 2], 5) is False
