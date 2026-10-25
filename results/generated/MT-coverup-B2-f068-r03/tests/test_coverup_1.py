# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

from f068 import pluck


def test_pluck_empty_returns_empty():
    arr = []
    result = pluck(arr)
    assert result == []
    assert arr == []


def test_pluck_no_evens_returns_empty():
    arr = [1, 3, 5, 7]
    result = pluck(arr)
    assert result == []
    assert arr == [1, 3, 5, 7]


def test_pluck_with_evens_returns_min_even_and_index():
    arr = [5, 0, 3, 0, 4, 2]
    result = pluck(arr)
    assert result == [0, 1]
    assert arr == [5, 0, 3, 0, 4, 2]


def test_pluck_single_even():
    arr = [1, 2, 3]
    result = pluck(arr)
    assert result == [2, 1]
    assert arr == [1, 2, 3]


def test_pluck_min_even_not_first_even():
    arr = [4, 8, 2, 6]
    result = pluck(arr)
    assert result == [2, 2]
    assert arr == [4, 8, 2, 6]
