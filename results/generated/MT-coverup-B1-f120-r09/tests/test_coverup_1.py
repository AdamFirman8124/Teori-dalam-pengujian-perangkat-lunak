# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest

from f120 import maximum


def test_maximum_k_zero():
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []
    # arr should remain unmodified when k == 0
    assert arr == [3, 1, 2]


def test_maximum_k_positive():
    arr = [3, 1, 2, 5, 4]
    result = maximum(arr, 2)
    assert result == [4, 5]
    # arr is sorted in place by the function
    assert arr == [1, 2, 3, 4, 5]


def test_maximum_k_equals_len():
    arr = [5, -1, 0]
    result = maximum(arr, 3)
    assert result == [-1, 0, 5]


def test_maximum_single_element():
    arr = [7]
    result = maximum(arr, 1)
    assert result == [7]
