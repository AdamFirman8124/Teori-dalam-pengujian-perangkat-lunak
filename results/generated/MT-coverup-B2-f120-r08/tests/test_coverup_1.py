# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

from f120 import maximum


def test_maximum_returns_empty_list_when_k_is_zero():
    values = [3, 1, 2]

    result = maximum(values, 0)

    assert result == []
    assert values == [3, 1, 2]


def test_maximum_sorts_input_and_returns_k_largest_values():
    values = [4, 1, 5, 2, 3]

    result = maximum(values, 3)

    assert result == [3, 4, 5]
    assert values == [1, 2, 3, 4, 5]
