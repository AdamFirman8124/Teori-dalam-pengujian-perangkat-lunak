# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_empty_list_returns_true():
    """Empty list: the loop body never runs, threshold is trivially met.

    Covers line 3 (loop setup) and line 6 (return True).
    """
    assert below_threshold([], 5) is True


def test_all_elements_below_threshold_returns_true():
    """All elements strictly below t: loop completes fully, returns True.

    Covers line 3, line 4 (False branch of the condition) and line 6.
    """
    assert below_threshold([1, 2, 3, 4], 5) is True


def test_element_equal_to_threshold_returns_false():
    """An element equal to t satisfies e >= t, so the result is False.

    Covers line 3, line 4 (True branch) and line 5 (return False).
    """
    assert below_threshold([1, 2, 5, 0], 5) is False


def test_element_above_threshold_returns_false():
    """An element strictly greater than t yields False.

    Covers line 3, line 4 (True branch) and line 5 (return False).
    """
    assert below_threshold([1, 2, 6], 5) is False


def test_early_exit_on_first_element():
    """First element already >= t: returns False without scanning the rest.

    Covers line 3, line 4 (True branch) and line 5 (return False),
    exercising the early-exit branch of the loop.
    """
    assert below_threshold([9, 0, 0], 5) is False


def test_negative_values_below_threshold():
    """Negative elements below a negative threshold still return True.

    Covers line 3, line 4 (False branch) and line 6.
    """
    assert below_threshold([-10, -5, -1], 0) is True
