# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_smallest_change_palindrome_returns_zero():
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_smallest_change_single_mismatch():
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4


def test_smallest_change_one_pair_mismatch():
    assert smallest_change([1, 2, 3, 4]) == 2


def test_smallest_change_empty_list():
    assert smallest_change([]) == 0


def test_smallest_change_single_element():
    assert smallest_change([7]) == 0


def test_smallest_change_does_not_mutate_input():
    arr = [1, 2, 3, 4]
    smallest_change(arr)
    assert arr == [1, 2, 3, 4]
