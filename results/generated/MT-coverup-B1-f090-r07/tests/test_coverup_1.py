# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f090 import next_smallest


def test_next_smallest_returns_none_for_fewer_than_two_unique_values():
    assert next_smallest([]) is None
    assert next_smallest([4, 4]) is None


def test_next_smallest_returns_second_smallest_unique_value():
    values = [5, 1, 3, 1, 2]
    original = values.copy()

    assert next_smallest(values) == 2
    assert values == original
