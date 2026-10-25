# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

from f005 import intersperse


def test_intersperse_empty_list():
    numbers = []

    assert intersperse(numbers, 0) == []
    assert numbers == []


def test_intersperse_multiple_numbers():
    numbers = [1, 2, 3]

    assert intersperse(numbers, 0) == [1, 0, 2, 0, 3]
    assert numbers == [1, 2, 3]
