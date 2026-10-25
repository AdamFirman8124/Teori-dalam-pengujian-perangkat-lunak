# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

from f120 import maximum


def test_maximum_with_zero_k_returns_empty_without_mutating_input():
    values = [3, 1, 2]

    result = maximum(values, 0)

    assert result == []
    assert values == [3, 1, 2]


def test_maximum_sorts_input_and_returns_k_largest_values():
    values = [4, 1, 3, 2]

    result = maximum(values, 2)

    assert result == [3, 4]
    assert values == [1, 2, 3, 4]
