# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_lst1_shorter():
    result = total_match(["hi", "admin"], ["hI", "Hi", "hI", "hI"])
    assert result == ["hi", "admin"]


def test_total_match_lst2_shorter():
    result = total_match(["hi", "admin"], ["hI", "Hi"])
    assert result == ["hI", "Hi"]


def test_total_match_equal_lengths_returns_lst1():
    result = total_match(["ab"], ["cd"])
    assert result == ["ab"]


def test_total_match_empty_lst1():
    result = total_match([], ["a", "b"])
    assert result == []


def test_total_match_both_empty():
    result = total_match([], [])
    assert result == []
