# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f090 import next_smallest


def test_next_smallest_returns_none_with_fewer_than_two_unique_values():
    assert next_smallest([]) is None
    assert next_smallest([7, 7, 7]) is None


def test_next_smallest_returns_second_distinct_value():
    assert next_smallest([5, 1, 3, 1, 5]) == 3
