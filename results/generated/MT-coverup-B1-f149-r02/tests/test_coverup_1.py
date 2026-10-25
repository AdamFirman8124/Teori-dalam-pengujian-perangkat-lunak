# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f149 import sorted_list_sum


def test_returns_only_even_length_strings():
    result = sorted_list_sum(["abc", "ab", "abcd", "a"])
    assert result == ["ab", "abcd"]


def test_sorts_by_length_then_alphabetically():
    # After lst.sort() (alphabetical), the stable length sort keeps
    # alphabetical order among equal-length strings.
    result = sorted_list_sum(["bbbb", "aa", "cccc", "bb", "dddd"])
    assert result == ["aa", "bb", "bbbb", "cccc", "dddd"]


def test_empty_list_returns_empty_list():
    assert sorted_list_sum([]) == []


def test_all_odd_lengths_returns_empty_list():
    assert sorted_list_sum(["a", "abc", "abcde"]) == []


def test_input_list_is_sorted_in_place():
    lst = ["ccc", "bb", "a"]
    sorted_list_sum(lst)
    assert lst == ["a", "bb", "ccc"]


def test_does_not_mutate_original_when_copied(monkeypatch):
    original = ["zz", "aaa", "b"]
    snapshot = list(original)
    result = sorted_list_sum(original)
    assert result == ["zz"]
    assert original == sorted(snapshot)
    assert result is not original


def test_duplicates_preserved():
    assert sorted_list_sum(["ab", "ab", "abc", "cd"]) == ["ab", "ab", "cd"]


def test_returns_new_list_object():
    lst = ["ab", "cd"]
    result = sorted_list_sum(lst)
    assert result == ["ab", "cd"]
    assert result is not lst
