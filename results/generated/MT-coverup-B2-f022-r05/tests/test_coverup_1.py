# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

"""Tests for f022.filter_integers — covering line 6 (the list-comprehension return).

The comprehension on line 6 has two implicit branches introduced by the
``if isinstance(x, int)`` filter: values that pass the filter and values that
are skipped. The tests below exercise both branches, plus the degenerate
empty-input case, and verify postconditions on the results.

``filter_integers`` is a pure function (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required; each test works on its own local
data, avoiding any state pollution.
"""

import pytest

from f022 import filter_integers


def test_filter_integers_mixed_types_covers_both_branches():
    """Line 6: mixed input exercises both the keep and skip branches."""
    values = [1, "two", 3.5, None, 4, [5], {"six": 6}, (7,)]
    result = filter_integers(values)

    # Postcondition: only the genuine ints survive, in original order.
    assert result == [1, 4]
    assert all(isinstance(x, int) and not isinstance(x, bool) for x in result)


def test_filter_integers_all_ints():
    """Line 6: every element passes the filter."""
    result = filter_integers([7, 8, 9])
    assert result == [7, 8, 9]


def test_filter_integers_no_ints():
    """Line 6: every element is skipped by the filter."""
    result = filter_integers(["a", 2.5, None, [1], 3.0])
    assert result == []


def test_filter_integers_empty_list():
    """Line 6: empty input — comprehension body never runs."""
    assert filter_integers([]) == []


def test_filter_integers_does_not_mutate_input():
    """Postcondition: the input list is left unchanged (pure function)."""
    values = [1, "x", 2, 3.0]
    snapshot = list(values)

    result = filter_integers(values)

    assert values == snapshot
    assert result == [1, 2]
    assert result is not values


def test_filter_integers_returns_new_list():
    """Postcondition: a fresh list is returned, not the input object."""
    values = [1, 2, 3]
    result = filter_integers(values)
    assert result == values
    assert result is not values
