# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

from f120 import maximum


def test_maximum_returns_empty_list_when_k_is_zero():
    arr = [3, 1, 2]

    result = maximum(arr, 0)

    assert result == []
    assert arr == [3, 1, 2]


def test_maximum_sorts_array_and_returns_k_largest_values():
    arr = [3, 1, 4, 2]

    result = maximum(arr, 2)

    assert arr == [1, 2, 3, 4]
    assert result == [3, 4]
