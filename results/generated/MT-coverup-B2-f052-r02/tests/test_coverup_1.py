# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

"""Tests for f052.below_threshold.

Covers every line and branch:
- line 3 (loop body): exercised by non-empty lists; the empty list exercises
  the loop-not-taken branch.
- line 4 (if e >= t): both branches are exercised (true -> return False,
  false -> continue looping).
- line 5 (return False): an element equal to / above the threshold.
- line 6 (return True): empty list and all-elements-below list.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required; each test works only on
locally created data, avoiding any state pollution.
"""

import pytest

from f052 import below_threshold


def test_empty_list_returns_true():
    """Empty list: loop body never runs, falls through to 'return True'."""
    assert below_threshold([], 10) is True


def test_all_elements_below_threshold_returns_true():
    """All elements strictly below t: loop completes, returns True."""
    assert below_threshold([1, 2, 3, 9], 10) is True


def test_element_equal_to_threshold_returns_false():
    """Element equal to t triggers the '>=' branch and returns False."""
    assert below_threshold([1, 2, 10, 0], 10) is False


def test_element_above_threshold_returns_false():
    """Element strictly above t triggers the '>=' branch and returns False."""
    assert below_threshold([1, 2, 11, 0], 10) is False


def test_first_element_at_or_above_threshold_returns_false_immediately():
    """First element already >= t: returns False without scanning the rest."""
    assert below_threshold([10, -100, -200], 10) is False


def test_negative_threshold_and_values():
    """Negative numbers: everything below a negative threshold is True."""
    assert below_threshold([-5, -3, -1], 0) is True
    assert below_threshold([-5, 0, -1], 0) is False


@pytest.mark.parametrize(
    "lst, t, expected",
    [
        ([], 0, True),
        ([0], 1, True),
        ([1], 1, False),
        ([2], 1, False),
        ([1, 2, 3], 4, True),
        ([1, 2, 3], 3, False),
    ],
)
def test_below_threshold_parametrized(lst, t, expected):
    """Table-driven check of both return values across many inputs."""
    assert below_threshold(lst, t) is expected
