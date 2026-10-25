# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f116 import sort_array


def test_sort_array_orders_by_popcount_then_value():
    result = sort_array([7, 1, 2, 3, 4, 5, 6])
    assert result == [1, 2, 4, 3, 5, 6, 7]
    assert [bin(x)[2:].count("1") for x in result] == sorted(
        bin(x)[2:].count("1") for x in [7, 1, 2, 3, 4, 5, 6]
    )


def test_sort_array_does_not_mutate_input():
    original = [9, 8, 7]
    snapshot = list(original)
    result = sort_array(original)
    assert original == snapshot
    assert result is not original
    assert result == [8, 9, 7]


def test_sort_array_empty_and_single():
    assert sort_array([]) == []
    assert sort_array([0]) == [0]


def test_sort_array_all_equal_popcount_keeps_ascending_order():
    # 3, 5, 6, 9 all have two set bits
    assert sort_array([9, 6, 5, 3]) == [3, 5, 6, 9]


def test_sort_array_returns_new_list(monkeypatch):
    calls = []
    real_sorted = sorted

    def spy_sorted(iterable, *args, **kwargs):
        calls.append(list(iterable))
        return real_sorted(iterable, *args, **kwargs)

    monkeypatch.setattr("builtins.sorted", spy_sorted)
    try:
        assert sort_array([4, 1, 3]) == [1, 4, 3]
        assert len(calls) == 2
    finally:
        monkeypatch.undo()
    assert sorted is real_sorted
