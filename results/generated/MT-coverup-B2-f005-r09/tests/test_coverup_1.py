# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest

from f005 import intersperse


def test_intersperse_empty_list_returns_empty():
    """Covers lines 6-7: the 'if not numbers' branch returns []."""
    result = intersperse([], 5)
    assert result == []
    assert isinstance(result, list)


def test_intersperse_single_element_skips_loop():
    """Covers lines 9, 15, 17: single element means the loop body (11-13) is skipped."""
    result = intersperse([42], 7)
    assert result == [42]


def test_intersperse_multiple_elements_inserts_delimeter():
    """Covers lines 9, 11-13, 15, 17: delimeter inserted between every pair."""
    result = intersperse([1, 2, 3], 4)
    assert result == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    """Minimal case exercising the loop body exactly once."""
    result = intersperse([10, 20], 0)
    assert result == [10, 0, 20]


def test_intersperse_negative_delimeter():
    """Delimeter may be any int, including negative values."""
    result = intersperse([1, 2, 3], -1)
    assert result == [1, -1, 2, -1, 3]


def test_intersperse_does_not_mutate_input():
    """Postcondition: the input list is left unchanged and a new list is returned."""
    numbers = [1, 2, 3]
    snapshot = list(numbers)
    result = intersperse(numbers, 9)
    assert numbers == snapshot
    assert result == [1, 9, 2, 9, 3]
    assert result is not numbers
