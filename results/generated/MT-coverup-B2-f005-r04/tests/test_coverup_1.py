# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest

from f005 import intersperse


def test_intersperse_empty_list():
    """Covers lines 6-7: empty input short-circuits to an empty list."""
    result = intersperse([], 5)
    assert result == []
    assert isinstance(result, list)


def test_intersperse_single_element():
    """Covers lines 9, 11 (loop body skipped), 15, 17: single element has no delimiters."""
    result = intersperse([42], 0)
    assert result == [42]


def test_intersperse_multiple_elements():
    """Covers lines 9, 11-13 (loop body), 15, 17: delimiters inserted between elements."""
    result = intersperse([1, 2, 3], 4)
    assert result == [1, 4, 2, 4, 3]
    assert len(result) == 2 * len([1, 2, 3]) - 1


def test_intersperse_two_elements():
    """Covers loop body executed exactly once."""
    result = intersperse([7, 8], -1)
    assert result == [7, -1, 8]


def test_intersperse_does_not_mutate_input():
    """Verifies the function is pure: the input list is left unchanged."""
    numbers = [1, 2, 3]
    result = intersperse(numbers, 9)
    assert result == [1, 9, 2, 9, 3]
    assert numbers == [1, 2, 3]
    assert result is not numbers
