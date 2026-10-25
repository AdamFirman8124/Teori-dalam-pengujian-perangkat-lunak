# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f026 import remove_duplicates


def test_remove_duplicates_empty_list():
    numbers = []
    result = remove_duplicates(numbers)
    assert result == []
    assert numbers == []


def test_remove_duplicates_all_unique_preserves_order():
    numbers = [5, 3, 9, 1]
    result = remove_duplicates(numbers)
    assert result == [5, 3, 9, 1]
    assert numbers == [5, 3, 9, 1]


def test_remove_duplicates_removes_repeated_values():
    numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 5]
    assert numbers == [1, 2, 2, 3, 4, 4, 4, 5]


def test_remove_duplicates_all_duplicates_returns_empty():
    numbers = [7, 7, 7]
    result = remove_duplicates(numbers)
    assert result == []
    assert numbers == [7, 7, 7]


def test_remove_duplicates_negative_and_zero_values():
    numbers = [0, -1, -1, 0, 2]
    result = remove_duplicates(numbers)
    assert result == [2]
    assert numbers == [0, -1, -1, 0, 2]


def test_remove_duplicates_postconditions():
    numbers = [3, 1, 3, 2, 1, 4]
    result = remove_duplicates(numbers)

    # every returned element appears exactly once in the input
    assert all(numbers.count(n) == 1 for n in result)
    # result is a subsequence of the input (order preserved)
    it = iter(numbers)
    assert all(n in it for n in result)
    # no duplicates in the result
    assert len(result) == len(set(result))
    # input not mutated
    assert numbers == [3, 1, 3, 2, 1, 4]


def test_remove_duplicates_does_not_mutate_input(monkeypatch):
    numbers = [1, 1, 2]
    snapshot = list(numbers)
    remove_duplicates(numbers)
    assert numbers == snapshot
