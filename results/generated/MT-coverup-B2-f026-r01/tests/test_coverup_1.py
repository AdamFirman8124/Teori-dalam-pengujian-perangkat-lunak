# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import collections

import pytest

from f026 import remove_duplicates


def test_removes_all_occurrences_of_duplicated_values():
    # Elements appearing more than once are dropped entirely (c[n] <= 1).
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1]


def test_keeps_all_elements_when_all_unique():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_empty_list_returns_empty_list():
    assert remove_duplicates([]) == []


def test_all_duplicates_returns_empty_list():
    assert remove_duplicates([5, 5, 5]) == []


def test_preserves_original_order():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [2]


def test_handles_zero_and_negative_numbers():
    assert remove_duplicates([0, -1, 0, -1, 7]) == [7]


def test_uses_collections_counter(monkeypatch):
    # Verify the function really goes through collections.Counter (line 7),
    # while monkeypatch guarantees the patch is undone afterwards.
    calls = []
    real_counter = collections.Counter

    def counting_counter(iterable):
        calls.append(list(iterable))
        return real_counter(iterable)

    monkeypatch.setattr(collections, "Counter", counting_counter)

    result = remove_duplicates([1, 2, 2, 4])

    assert result == [1, 4]
    assert calls == [[1, 2, 2, 4]]
