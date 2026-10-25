# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_filters_and_sorts_values():
    values = [246, 57, 135, 70, 3, 11]

    result = unique_digits(values)

    assert result == [3, 11, 57, 135]
    assert values == [246, 57, 135, 70, 3, 11]


def test_unique_digits_with_empty_input():
    assert unique_digits([]) == []
