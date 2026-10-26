# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

from f005 import intersperse


def test_intersperse_empty_returns_empty():
    assert intersperse([], 4) == []


def test_intersperse_single_element_no_delimiter_added():
    assert intersperse([1], 4) == [1]


def test_intersperse_two_elements():
    assert intersperse([1, 2], 4) == [1, 4, 2]


def test_intersperse_multiple_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
