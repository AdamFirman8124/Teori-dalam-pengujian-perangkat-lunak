# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

import pytest

from f005 import intersperse


def test_intersperse_empty_list_returns_empty():
    numbers = []
    result = intersperse(numbers, 0)
    assert result == []
    assert numbers == []


def test_intersperse_single_element_skips_loop():
    numbers = [7]
    result = intersperse(numbers, 0)
    assert result == [7]
    assert numbers == [7]


def test_intersperse_two_elements():
    assert intersperse([1, 2], 0) == [1, 0, 2]


def test_intersperse_multiple_elements():
    numbers = [1, 2, 3, 4]
    result = intersperse(numbers, -1)
    assert result == [1, -1, 2, -1, 3, -1, 4]
    assert numbers == [1, 2, 3, 4]


def test_intersperse_does_not_mutate_input():
    numbers = [5, 6, 7]
    original = list(numbers)
    intersperse(numbers, 99)
    assert numbers == original
