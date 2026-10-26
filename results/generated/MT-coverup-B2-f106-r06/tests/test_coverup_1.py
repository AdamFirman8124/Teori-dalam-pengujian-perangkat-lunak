# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

import pytest

from f106 import f


def test_f_odd_branch_sums():
    # i = 1, 3 -> triangular numbers
    assert f(3) == [1, 2, 6]


def test_f_even_branch_factorials():
    # i = 2, 4 -> factorials
    assert f(4) == [1, 2, 6, 24]


def test_f_mixed_branches():
    assert f(5) == [1, 2, 6, 24, 15]


def test_f_zero_returns_empty_list():
    assert f(0) == []


def test_f_one_only_odd_branch():
    assert f(1) == [1]


def test_f_two_only_even_branch():
    assert f(2) == [1, 2]


def test_f_returns_new_list_each_call():
    first = f(3)
    second = f(3)
    assert first == second
    assert first is not second
    first.append(999)
    assert f(3) == [1, 2, 6]


def test_f_negative_returns_empty_list():
    assert f(-5) == []


def test_f_larger_input_length_and_values():
    result = f(6)
    assert len(result) == 6
    assert result == [1, 2, 6, 24, 15, 720]
