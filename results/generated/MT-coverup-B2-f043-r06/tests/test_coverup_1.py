# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

import pytest

from f043 import pairs_sum_to_zero


def test_empty_list_returns_false():
    data = []
    assert pairs_sum_to_zero(data) is False
    assert data == []


def test_single_element_returns_false():
    data = [5]
    assert pairs_sum_to_zero(data) is False
    assert data == [5]


def test_adjacent_pair_sums_to_zero():
    data = [1, -1]
    assert pairs_sum_to_zero(data) is True
    assert data == [1, -1]


def test_non_adjacent_pair_sums_to_zero():
    data = [1, 2, -1]
    assert pairs_sum_to_zero(data) is True
    assert data == [1, 2, -1]


def test_pair_at_end_of_list_sums_to_zero():
    data = [1, 2, 3, -2]
    assert pairs_sum_to_zero(data) is True
    assert data == [1, 2, 3, -2]


def test_no_pair_sums_to_zero_exhausts_loops():
    data = [1, 2, 3, 4]
    assert pairs_sum_to_zero(data) is False
    assert data == [1, 2, 3, 4]


def test_zeros_pair_sums_to_zero():
    data = [0, 0]
    assert pairs_sum_to_zero(data) is True
    assert data == [0, 0]


def test_single_zero_returns_false():
    data = [0]
    assert pairs_sum_to_zero(data) is False
    assert data == [0]


def test_negative_values_without_zero_pair():
    data = [-1, -2, -3]
    assert pairs_sum_to_zero(data) is False
    assert data == [-1, -2, -3]


def test_duplicates_without_zero_pair():
    data = [2, 2, 2]
    assert pairs_sum_to_zero(data) is False
    assert data == [2, 2, 2]


def test_input_list_not_mutated(monkeypatch):
    data = [3, -3, 7]
    snapshot = list(data)
    monkeypatch.setattr("builtins.len", len)
    assert pairs_sum_to_zero(data) is True
    assert data == snapshot
