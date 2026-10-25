# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_array():
    """Covers line 3: empty input returns []."""
    assert pluck([]) == []


def test_pluck_no_evens():
    """Covers lines 3-5: all-odd input returns []."""
    assert pluck([1, 3, 5]) == []


def test_pluck_with_evens():
    """Covers lines 3-6: returns [smallest even, its index]."""
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]


def test_pluck_single_even():
    assert pluck([7, 8]) == [8, 1]


def test_pluck_pure_function_no_mutation():
    """Postcondition: input list is not modified."""
    arr = [1, 2, 3, 4]
    pluck(arr)
    assert arr == [1, 2, 3, 4]
