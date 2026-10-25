# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_lst1_shorter():
    assert total_match(["hi", "a"], ["admin"]) == ["hi", "a"]


def test_total_match_lst2_shorter():
    assert total_match(["hii"], ["a"]) == ["a"]


def test_total_match_equal_returns_lst1():
    assert total_match(["hi"], ["ab"]) == ["hi"]


def test_total_match_empty_lst1():
    assert total_match([], ["a", "b"]) == []


def test_total_match_empty_lst2():
    assert total_match(["a", "b"], []) == []


def test_total_match_both_empty():
    assert total_match([], []) == []
