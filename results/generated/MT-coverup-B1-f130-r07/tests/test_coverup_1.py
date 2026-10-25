# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

import pytest

from f130 import tri


def test_tri_zero_returns_single_one():
    result = tri(0)
    assert result == [1]
    assert isinstance(result, list)


def test_tri_one_returns_base_pair():
    result = tri(1)
    assert result == [1, 3]


def test_tri_two_exercises_even_branch():
    result = tri(2)
    assert result == [1, 3, 2.0]
    assert len(result) == 3


def test_tri_three_exercises_even_and_odd_branches():
    result = tri(3)
    # i=2 (even): 2/2 + 1 = 2.0
    # i=3 (odd): 2.0 + 3 + (3+3)/2 = 8.0
    assert result == [1, 3, 2.0, 8.0]
    assert len(result) == 4


def test_tri_five_full_sequence():
    result = tri(5)
    # i=2 even -> 2.0
    # i=3 odd  -> 2.0 + 3 + 3.0 = 8.0
    # i=4 even -> 4/2 + 1 = 3.0
    # i=5 odd  -> 3.0 + 8.0 + 4.0 = 15.0
    assert result == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert len(result) == 6


def test_tri_returns_new_list_each_call():
    first = tri(3)
    second = tri(3)
    assert first == second
    assert first is not second
    first.append(999)
    assert tri(3) == [1, 3, 2.0, 8.0]


def test_tri_negative_n_returns_base_pair():
    # range(2, n + 1) is empty for n < 2, so the base pair is returned
    assert tri(-1) == [1, 3]
