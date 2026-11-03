# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest

from f005 import intersperse


def test_intersperse_empty_list_returns_empty():
    """Covers lines 6-7: the 'if not numbers' branch returning []."""
    assert intersperse([], 0) == []
    assert intersperse([], 42) == []


def test_intersperse_single_element():
    """Covers lines 9, 15, 17: loop body skipped (empty numbers[:-1]),
    only the last element is appended."""
    assert intersperse([7], 3) == [7]


def test_intersperse_two_elements():
    """Covers lines 11-13: loop body executes exactly once."""
    assert intersperse([1, 2], 0) == [1, 0, 2]


def test_intersperse_multiple_elements():
    """Covers lines 9, 11-13, 15, 17: full happy path."""
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_negative_delimeter():
    """Delimeter may be any int, including negatives."""
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]


def test_intersperse_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [1, 2, 3]
    snapshot = list(numbers)
    result = intersperse(numbers, 9)
    assert numbers == snapshot
    assert result == [1, 9, 2, 9, 3]
    assert result is not numbers


def test_intersperse_result_length():
    """Postcondition: len(result) == 2 * len(numbers) - 1 for non-empty input."""
    numbers = [10, 20, 30, 40]
    result = intersperse(numbers, 5)
    assert len(result) == 2 * len(numbers) - 1
    assert result[0] == 10
    assert result[-1] == 40
    assert result[1::2] == [5, 5, 5]
    assert result[0::2] == numbers
