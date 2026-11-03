# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f136 import largest_smallest_integers


def test_both_negative_and_positive():
    # Covers: smallest non-empty, largest non-empty
    result = largest_smallest_integers([-3, -1, -2, 5, 2, 4])
    assert result == (-1, 2)


def test_only_negatives():
    # Covers: smallest non-empty, largest empty -> (max(negatives), None)
    result = largest_smallest_integers([-5, -10, -1])
    assert result == (-1, None)


def test_only_positives():
    # Covers: smallest empty, largest non-empty -> (None, min(positives))
    result = largest_smallest_integers([7, 3, 10])
    assert result == (None, 3)


def test_empty_list():
    # Covers: smallest empty, largest empty -> (None, None)
    result = largest_smallest_integers([])
    assert result == (None, None)


def test_zeros_only():
    # Zeros are neither negative nor positive -> (None, None)
    result = largest_smallest_integers([0, 0])
    assert result == (None, None)


def test_mixed_with_zero():
    # Zero is ignored by both filters
    result = largest_smallest_integers([0, -4, 9])
    assert result == (-4, 9)
