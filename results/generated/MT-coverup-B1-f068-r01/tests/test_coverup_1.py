# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

from f068 import pluck


def test_pluck_empty_list():
    assert pluck([]) == []


def test_pluck_list_without_even_numbers():
    assert pluck([1, 3, 5, 7]) == []


def test_pluck_returns_smallest_even_and_its_first_index():
    assert pluck([7, 4, 3, 2, 8, 2]) == [2, 3]
