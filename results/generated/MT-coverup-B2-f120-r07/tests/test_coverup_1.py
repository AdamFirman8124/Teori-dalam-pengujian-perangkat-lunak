# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

from f120 import maximum


def test_maximum_k_zero_returns_empty():
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []


def test_maximum_k_positive_returns_largest_k():
    arr = [4, 1, 3, 5, 2]
    result = maximum(arr, 2)
    assert result == [4, 5]


def test_maximum_k_equals_length_returns_sorted():
    arr = [3, 1, 2]
    result = maximum(arr, 3)
    assert result == [1, 2, 3]
