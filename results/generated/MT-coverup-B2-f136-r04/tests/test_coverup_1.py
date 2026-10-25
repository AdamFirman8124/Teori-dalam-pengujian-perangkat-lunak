# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_largest_smallest_integers_mixed():
    result = largest_smallest_integers([2, -3, 5, -7, 1])
    assert result == (-3, 1)


def test_largest_smallest_integers_only_negatives():
    result = largest_smallest_integers([-4, -1, -9])
    assert result == (-1, None)


def test_largest_smallest_integers_only_positives():
    result = largest_smallest_integers([4, 1, 9])
    assert result == (None, 1)


def test_largest_smallest_integers_empty():
    result = largest_smallest_integers([])
    assert result == (None, None)


def test_largest_smallest_integers_zero_ignored():
    result = largest_smallest_integers([0, 0])
    assert result == (None, None)
