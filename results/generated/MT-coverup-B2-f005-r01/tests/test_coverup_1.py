# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

from typing import List

from f005 import intersperse


def test_intersperse_empty_list():
    """Covers lines 6-7: empty input returns an empty list."""
    result: List[int] = intersperse([], 5)
    assert result == []
    assert isinstance(result, list)


def test_intersperse_single_element():
    """Covers lines 9, 11 (loop body skipped), 15, 17: single element, no delimiter."""
    result: List[int] = intersperse([42], 7)
    assert result == [42]


def test_intersperse_multiple_elements():
    """Covers lines 9, 11-13, 15, 17: delimiters inserted between elements."""
    result: List[int] = intersperse([1, 2, 3], 4)
    assert result == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    result: List[int] = intersperse([10, 20], -1)
    assert result == [10, -1, 20]


def test_intersperse_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [1, 2, 3]
    intersperse(numbers, 0)
    assert numbers == [1, 2, 3]
