# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_true():
    """A sorted list with no element appearing more than twice returns True."""
    assert is_sorted([1, 2, 3, 4]) is True
    assert is_sorted([]) is True
    assert is_sorted([1, 1, 2]) is True


def test_is_sorted_false_unsorted():
    """An unsorted list (with no element appearing more than twice) returns False."""
    assert is_sorted([1, 3, 2, 4]) is False
    assert is_sorted([2, 1]) is False


def test_is_sorted_false_too_many_duplicates():
    """A list where some element appears more than twice returns False,
    even if the list is otherwise sorted."""
    assert is_sorted([1, 1, 1, 2]) is False
    assert is_sorted([1, 2, 2, 2, 3]) is False
    # duplicates exceeding the limit even when unsorted
    assert is_sorted([3, 3, 3, 1]) is False
