# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_array():
    """Covers line 3: empty input returns []."""
    assert pluck([]) == []


def test_pluck_no_evens():
    """Covers lines 4-5: array with only odd numbers returns []."""
    assert pluck([1, 3, 5, 7]) == []


def test_pluck_with_evens():
    """Covers line 6: returns [min(evens), index of min(evens) in arr]."""
    assert pluck([1, 2, 3, 4]) == [2, 1]


def test_pluck_min_even_not_first():
    """Covers line 6 where the minimum even value appears later in the array."""
    assert pluck([8, 5, 4, 6]) == [4, 2]


def test_pluck_duplicate_min_evens():
    """Covers line 6 with duplicated minimum even value: first index is used."""
    assert pluck([4, 2, 2, 3]) == [2, 1]


def test_pluck_single_even():
    """Covers line 6 with a single-element array containing an even number."""
    assert pluck([0]) == [0, 0]
