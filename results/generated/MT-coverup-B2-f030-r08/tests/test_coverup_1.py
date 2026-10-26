# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f030 import get_positive


def test_get_positive_returns_only_positive_values():
    values = [-3, 0, 4, 1, -2]

    result = get_positive(values)

    assert result == [4, 1]
    assert values == [-3, 0, 4, 1, -2]


def test_get_positive_returns_empty_list_when_no_values_are_positive():
    values = [-3, 0, -1]

    result = get_positive(values)

    assert result == []
