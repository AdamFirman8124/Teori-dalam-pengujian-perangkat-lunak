# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_mixed_integers():
    result = largest_smallest_integers([2, -3, 5, -7, 1])
    assert result == (-3, 1)


def test_only_negatives():
    result = largest_smallest_integers([-1, -5, -3])
    assert result == (-1, None)


def test_only_positives():
    result = largest_smallest_integers([4, 2, 9])
    assert result == (None, 2)


def test_empty_list():
    result = largest_smallest_integers([])
    assert result == (None, None)


def test_zero_is_neither():
    result = largest_smallest_integers([0, 0])
    assert result == (None, None)
