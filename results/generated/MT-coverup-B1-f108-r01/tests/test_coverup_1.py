# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest

from f108 import count_nums


def test_count_nums_empty():
    assert count_nums([]) == 0


def test_count_nums_positive():
    assert count_nums([1, 11, -11]) == 2


def test_count_nums_negative():
    # digits_sum(-1) = -1, digits_sum(-11) = 0, digits_sum(-111) = 1
    assert count_nums([-1, -11, -111]) == 1


def test_count_nums_mixed():
    assert count_nums([1, 1, 2]) == 3
