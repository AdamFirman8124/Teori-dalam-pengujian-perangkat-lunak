# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_lst1_shorter_returns_lst1():
    lst1 = ["hi", "a"]
    lst2 = ["hello", "world", "x"]
    result = total_match(lst1, lst2)
    assert result == lst1
    assert result is lst1


def test_total_match_equal_lengths_returns_lst1():
    lst1 = ["ab", "cd"]
    lst2 = ["ef", "gh"]
    result = total_match(lst1, lst2)
    assert result == lst1
    assert result is lst1


def test_total_match_lst2_shorter_returns_lst2():
    lst1 = ["hello", "world"]
    lst2 = ["hi"]
    result = total_match(lst1, lst2)
    assert result == lst2
    assert result is lst2


def test_total_match_empty_lists_returns_lst1():
    lst1 = []
    lst2 = ["a"]
    result = total_match(lst1, lst2)
    assert result == lst1
    assert result is lst1


def test_total_match_both_empty_returns_lst1():
    lst1 = []
    lst2 = []
    result = total_match(lst1, lst2)
    assert result == lst1
    assert result is lst1
