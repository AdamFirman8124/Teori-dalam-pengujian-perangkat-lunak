# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

from script_5 import intersperse


def test_intersperse_empty_list():
    # Covers line 11-12: the empty-list guard branch.
    result = intersperse([], 4)
    assert result == []
    assert isinstance(result, list)


def test_intersperse_single_element():
    # Covers lines 14, 16 (loop not entered), 20, 22.
    result = intersperse([7], 4)
    assert result == [7]
    assert isinstance(result, list)


def test_intersperse_multiple_elements():
    # Covers lines 16-18 (loop body), 20, 22.
    result = intersperse([1, 2, 3], 4)
    assert result == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    result = intersperse([1, 2], 0)
    assert result == [1, 0, 2]


def test_intersperse_does_not_mutate_input():
    numbers = [1, 2, 3]
    original = list(numbers)
    result = intersperse(numbers, 9)
    assert numbers == original
    assert result is not numbers
