# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f090 import next_smallest


def test_next_smallest_returns_none_when_fewer_than_two_unique_values():
    values = [3, 3, 3]

    result = next_smallest(values)

    assert result is None
    assert values == [3, 3, 3]


def test_next_smallest_returns_second_smallest_unique_value():
    values = [5, 1, 3, 1, 2]

    result = next_smallest(values)

    assert result == 2
    assert values == [5, 1, 3, 1, 2]
