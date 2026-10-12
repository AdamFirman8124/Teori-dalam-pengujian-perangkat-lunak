# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

import pytest

from script_5 import intersperse


def test_intersperse_empty():
    assert intersperse([], 4) == []


def test_intersperse_single_element():
    assert intersperse([7], 4) == [7]


def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    assert intersperse([1, 2], 0) == [1, 0, 2]


def test_intersperse_four_elements():
    assert intersperse([1, 2, 3, 4], 9) == [1, 9, 2, 9, 3, 9, 4]


def test_intersperse_negative_delimiter():
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]


def test_intersperse_does_not_mutate_input():
    numbers = [1, 2, 3]
    original = list(numbers)
    result = intersperse(numbers, 4)
    assert numbers == original
    assert result is not numbers
