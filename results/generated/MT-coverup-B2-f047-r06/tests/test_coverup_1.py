# file: project/f047/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f047 import median


def test_median_odd_length():
    assert median([3, 1, 2]) == 2
    assert median([5]) == 5
    assert median([4, 1, 3, 2, 5]) == 3


def test_median_even_length():
    assert median([1, 2]) == 1.5
    assert median([4, 1, 3, 2]) == 2.5
    assert median([10, 20, 30, 40]) == 25.0


def test_median_does_not_mutate_input():
    data = [3, 1, 2]
    median(data)
    assert data == [3, 1, 2]
