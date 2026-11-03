# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

"""Tests for f069.search covering lines 12-21 (full body and both branches of the
frequency check). The function under test is pure (no I/O, no globals, no side
effects), so no monkeypatching or teardown is required to avoid state pollution."""

import pytest

from f069 import search


def test_search_docstring_example_1():
    """Mixed frequencies: 1 appears twice, 2 appears twice, 3 and 4 once each.
    Covers: frq allocation, counting loop, scan loop, and both outcomes of the
    'frq[i] >= i' branch (true for i=1,2; false for i=3,4)."""
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_docstring_example_2():
    """Greatest qualifying value wins: 4 appears only 3 times (< 4), so 3 wins.
    Covers the branch where a later candidate fails the check after ans was set."""
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_docstring_example_3():
    """No value meets its own frequency: every branch of the check is False and
    ans stays -1 through the whole scan loop."""
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_qualifies():
    """Smallest possible input: max(lst) == 1, so the scan loop runs exactly once
    and its condition is True (frq[1] == 1 >= 1)."""
    assert search([1]) == 1


def test_search_single_element_does_not_qualify():
    """Single element whose frequency (1) is below its value (2): the scan loop
    runs and every check is False, returning -1."""
    assert search([2]) == -1


def test_search_frequency_strictly_greater_than_value():
    """Frequency exceeds the value (3 > 2): exercises the '>=' boundary from the
    strictly-greater side."""
    assert search([2, 2, 2]) == 2


def test_search_frequency_exactly_equal_to_value():
    """Frequency equals the value exactly (3 == 3): exercises the '==' boundary."""
    assert search([3, 3, 3]) == 3


def test_search_larger_value_qualifies_after_smaller():
    """Both 1 and 4 qualify (each appears 4 times); the later, larger candidate
    must overwrite ans, proving the scan keeps going after a hit."""
    assert search([1, 1, 1, 1, 4, 4, 4, 4]) == 4


def test_search_result_is_greatest_qualifying_not_first():
    """A high-frequency small value must not mask a qualifying larger value:
    2 appears 5 times (>= 2) and 5 appears 5 times (>= 5); answer is 5."""
    assert search([2, 2, 2, 2, 2, 5, 5, 5, 5, 5]) == 5


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([4, 1, 2, 2, 3, 1], 2),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
        ([5, 5, 4, 4, 4], -1),
        ([1], 1),
        ([2], -1),
        ([2, 2, 2], 2),
        ([3, 3, 3], 3),
        ([1, 1, 1, 1, 4, 4, 4, 4], 4),
        ([2, 2, 2, 2, 2, 5, 5, 5, 5, 5], 5),
    ],
)
def test_search_parametrized(lst, expected):
    """Parametrized sweep over all cases to guarantee lines 12-21 and both
    outcomes of the frequency check are executed repeatedly."""
    assert search(lst) == expected
