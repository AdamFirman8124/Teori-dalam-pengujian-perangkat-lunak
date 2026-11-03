# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest

from f005 import intersperse


def test_intersperse_empty_list_returns_empty():
    """Covers lines 6-7: empty input short-circuits to []."""
    assert intersperse([], 4) == []


def test_intersperse_multiple_elements():
    """Covers lines 9, 11-13, 15, 17: delimeter inserted between elements."""
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    """Covers loop body executing exactly once."""
    assert intersperse([1, 2], 0) == [1, 0, 2]


def test_intersperse_single_element_skips_loop():
    """Covers lines 9, 15, 17 with loop body never entered."""
    assert intersperse([5], 4) == [5]


def test_intersperse_negative_delimeter():
    """Delimeter may be any int, including negatives."""
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]


def test_intersperse_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [7, 8, 9]
    result = intersperse(numbers, 0)
    assert numbers == [7, 8, 9]
    assert result == [7, 0, 8, 0, 9]
    assert result is not numbers


def test_intersperse_result_length():
    """Postcondition: result length is 2n-1 for non-empty input of length n."""
    numbers = [1, 2, 3, 4]
    result = intersperse(numbers, 99)
    assert len(result) == 2 * len(numbers) - 1
    assert result == [1, 99, 2, 99, 3, 99, 4]
