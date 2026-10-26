# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

from f120 import maximum


def test_maximum_k_zero_returns_empty():
    arr = [3, 1, 2]
    original = list(arr)
    result = maximum(arr, 0)
    assert result == []
    # early return should not sort / mutate input
    assert arr == original


def test_maximum_k_nonzero_returns_k_largest():
    arr = [5, 1, 3, 2, 4]
    result = maximum(arr, 2)
    assert result == [4, 5]
    # postcondition: input is sorted in place and result is last k elements
    assert arr == [1, 2, 3, 4, 5]
    assert result == arr[-2:]
