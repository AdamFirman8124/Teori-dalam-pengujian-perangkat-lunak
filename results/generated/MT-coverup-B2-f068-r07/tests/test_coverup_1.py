# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

from f068 import pluck


def test_pluck_empty_array():
    assert pluck([]) == []


def test_pluck_no_evens():
    assert pluck([1, 3, 5]) == []
    assert pluck([1]) == []


def test_pluck_finds_smallest_even_and_index():
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([5, 4, 2, 8]) == [2, 2]


def test_pluck_single_even_and_zero_and_duplicates():
    assert pluck([1, 3, 4]) == [4, 2]
    assert pluck([2]) == [2, 0]
    assert pluck([0, 1, 2]) == [0, 0]
    assert pluck([2, 2, 4]) == [2, 0]
    assert pluck([-4, -2, 3]) == [-4, 0]
