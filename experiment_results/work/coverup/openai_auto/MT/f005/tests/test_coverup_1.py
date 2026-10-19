# file: project\f005\__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

from f005 import intersperse


def test_intersperse_empty_list():
    assert intersperse([], 0) == []


def test_intersperse_single_number():
    assert intersperse([42], 0) == [42]


def test_intersperse_multiple_numbers():
    numbers = [1, 2, 3]
    original = numbers.copy()

    assert intersperse(numbers, -1) == [1, -1, 2, -1, 3]
    assert numbers == original
