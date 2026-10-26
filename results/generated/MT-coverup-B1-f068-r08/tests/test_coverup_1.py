# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

from f068 import pluck


def test_pluck_returns_empty_list_for_empty_input():
    assert pluck([]) == []


def test_pluck_returns_empty_list_when_input_has_no_even_numbers():
    assert pluck([1, 3, 5, 7]) == []


def test_pluck_returns_smallest_even_number_and_its_first_index():
    assert pluck([7, 4, 2, 6, 2]) == [2, 2]
