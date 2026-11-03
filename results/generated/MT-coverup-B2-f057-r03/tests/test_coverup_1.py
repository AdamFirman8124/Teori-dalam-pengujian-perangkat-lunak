# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

"""Tests for f057.monotonic — covering lines 3-5 (both branches of the if)."""

import pytest

from f057 import monotonic


def test_monotonic_ascending_returns_true():
    # Exercises line 3 (condition) and line 4 via the first disjunct.
    assert monotonic([1, 2, 3, 4]) is True


def test_monotonic_descending_returns_true():
    # Exercises line 3 and line 4 via the second disjunct (reverse=True).
    assert monotonic([4, 3, 2, 1]) is True


def test_monotonic_not_monotonic_returns_false():
    # Exercises line 3 and line 5 (neither disjunct holds).
    assert monotonic([1, 3, 2]) is False


def test_monotonic_empty_list():
    # Edge case: empty list is trivially monotonic (both branches of line 3).
    assert monotonic([]) is True


def test_monotonic_single_element():
    # Edge case: single element is trivially monotonic.
    assert monotonic([42]) is True


def test_monotonic_with_duplicates_ascending():
    # Duplicates still count as monotonic non-decreasing.
    assert monotonic([1, 1, 2, 2, 3]) is True


def test_monotonic_with_duplicates_descending():
    # Duplicates still count as monotonic non-increasing.
    assert monotonic([3, 3, 2, 1, 1]) is True


def test_monotonic_with_duplicates_not_monotonic():
    # Duplicates but direction changes: must hit line 5.
    assert monotonic([1, 2, 2, 1]) is False


def test_monotonic_does_not_mutate_input():
    # Postcondition: the input list is left unchanged (sorted() copies).
    data = [3, 1, 2]
    monotonic(data)
    assert data == [3, 1, 2]
