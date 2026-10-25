# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

from f005 import intersperse


def test_intersperse_empty_list():
    numbers = []

    assert intersperse(numbers, 0) == []
    assert numbers == []


def test_intersperse_single_item():
    numbers = [7]

    assert intersperse(numbers, 0) == [7]
    assert numbers == [7]


def test_intersperse_multiple_items():
    numbers = [1, 2, 3]

    assert intersperse(numbers, -1) == [1, -1, 2, -1, 3]
    assert numbers == [1, 2, 3]
