# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_returns_absolute_differences():
    """Cover line 3: the list comprehension computing abs differences."""
    result = compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
    assert result == [0, 0, 0, 0, 3, 3]


def test_compare_with_empty_sequences():
    """Cover line 3 with empty inputs: comprehension yields empty list."""
    assert compare([], []) == []


def test_compare_with_negative_differences():
    """Cover line 3 where guess values exceed game values."""
    assert compare([0, 5, -3], [10, 0, 3]) == [10, 5, 6]
