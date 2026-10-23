# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest

from f005 import intersperse


def test_intersperse_empty_list():
    """Covers lines 6-7: empty input returns an empty list."""
    assert intersperse([], 5) == []


def test_intersperse_single_element():
    """Covers the loop being skipped (numbers[:-1] is empty) and line 15."""
    assert intersperse([7], 3) == [7]


def test_intersperse_multiple_elements():
    """Covers lines 11-13 (loop body) and line 15 (last element)."""
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    assert intersperse([10, 20], -1) == [10, -1, 20]


def test_intersperse_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [1, 2, 3]
    original = list(numbers)
    intersperse(numbers, 0)
    assert numbers == original


def test_intersperse_returns_new_list():
    """Postcondition: result is a distinct list object from the input."""
    numbers = [1, 2]
    result = intersperse(numbers, 9)
    assert result is not numbers
