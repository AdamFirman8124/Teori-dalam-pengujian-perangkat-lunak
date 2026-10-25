# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_lst1_shorter():
    lst1 = ["a", "b"]
    lst2 = ["abc", "def", "ghi"]
    result = total_match(lst1, lst2)
    assert result is lst1
    assert result == ["a", "b"]


def test_total_match_equal_lengths_returns_lst1():
    lst1 = ["ab"]
    lst2 = ["cd"]
    result = total_match(lst1, lst2)
    assert result is lst1
    assert result == ["ab"]


def test_total_match_lst2_shorter():
    lst1 = ["abc", "def"]
    lst2 = ["x"]
    result = total_match(lst1, lst2)
    assert result is lst2
    assert result == ["x"]


def test_total_match_empty_lists():
    assert total_match([], []) == []
    assert total_match([], ["a"]) == []
    assert total_match(["a"], []) == []
