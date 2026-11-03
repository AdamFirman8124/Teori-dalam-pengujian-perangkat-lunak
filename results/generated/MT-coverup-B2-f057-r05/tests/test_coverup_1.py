# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


def test_monotonic_ascending():
    """A list sorted in ascending order is monotonic (line 3 first branch True, line 4)."""
    assert monotonic([1, 2, 3, 4, 5]) is True


def test_monotonic_descending():
    """A list sorted in descending order is monotonic (line 3 second branch True, line 4)."""
    assert monotonic([5, 4, 3, 2, 1]) is True


def test_monotonic_not_sorted():
    """A list that is neither ascending nor descending is not monotonic (line 5)."""
    assert monotonic([1, 3, 2, 4]) is False


def test_monotonic_empty_list():
    """An empty list is trivially monotonic."""
    assert monotonic([]) is True


def test_monotonic_single_element():
    """A single-element list is trivially monotonic."""
    assert monotonic([42]) is True


def test_monotonic_duplicates_ascending():
    """A list with duplicates in non-decreasing order is monotonic."""
    assert monotonic([1, 2, 2, 3]) is True


def test_monotonic_duplicates_descending():
    """A list with duplicates in non-increasing order is monotonic."""
    assert monotonic([3, 2, 2, 1]) is True


def test_monotonic_all_equal():
    """A list of identical elements is monotonic."""
    assert monotonic([7, 7, 7]) is True


def test_monotonic_two_elements_out_of_order():
    """A two-element list in descending order is monotonic."""
    assert monotonic([2, 1]) is True


def test_monotonic_negative_numbers():
    """Monotonicity works with negative numbers."""
    assert monotonic([-3, -1, 0, 2]) is True
    assert monotonic([-3, -5, -1]) is False


def test_monotonic_does_not_mutate_input():
    """The function must not modify the input list."""
    original = [3, 1, 2]
    snapshot = list(original)
    monotonic(original)
    assert original == snapshot
