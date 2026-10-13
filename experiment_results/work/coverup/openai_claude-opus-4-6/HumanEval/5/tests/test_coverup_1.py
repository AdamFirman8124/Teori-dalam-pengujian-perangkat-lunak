# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

from typing import List

import pytest

from script_5 import intersperse


def test_intersperse_empty_list():
    numbers: List[int] = []
    result = intersperse(numbers, 4)
    assert result == []
    assert numbers == []


def test_intersperse_single_element():
    numbers = [7]
    result = intersperse(numbers, 4)
    assert result == [7]
    assert numbers == [7]


def test_intersperse_multiple_elements():
    numbers = [1, 2, 3]
    result = intersperse(numbers, 4)
    assert result == [1, 4, 2, 4, 3]
    assert numbers == [1, 2, 3]


def test_intersperse_two_elements():
    numbers = [5, 6]
    result = intersperse(numbers, 0)
    assert result == [5, 0, 6]
    assert numbers == [5, 6]


@pytest.mark.parametrize(
    "numbers, delimeter, expected",
    [
        ([], 4, []),
        ([7], 4, [7]),
        ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
        ([1, 1], 1, [1, 1, 1]),
        ([-1, -2, -3], 0, [-1, 0, -2, 0, -3]),
    ],
)
def test_intersperse_parametrized(numbers, delimeter, expected):
    original = list(numbers)
    result = intersperse(numbers, delimeter)
    assert result == expected
    # postconditions
    assert len(result) == (0 if not expected else 2 * len(numbers) - 1)
    if numbers:
        assert result[0] == numbers[0]
        assert result[-1] == numbers[-1]
        for i in range(1, len(result), 2):
            assert result[i] == delimeter
    else:
        assert result == []
    # input must not be mutated
    assert numbers == original
    # returned object must be a new list, not the input itself
    assert result is not numbers
