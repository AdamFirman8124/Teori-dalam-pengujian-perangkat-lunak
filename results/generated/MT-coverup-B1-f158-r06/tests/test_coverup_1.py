# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f158 import find_max
import pytest


def test_find_max_most_distinct_chars():
    words = ["aaa", "ab", "abc"]
    result = find_max(words)
    assert result == "abc"
    # postcondition: result is an element of the input
    assert result in words
    # postcondition: input is not mutated
    assert words == ["aaa", "ab", "abc"]


def test_find_max_prefers_distinct_over_length():
    words = ["aaaaabbbbb", "abcde"]
    result = find_max(words)
    assert result == "abcde"


def test_find_max_tie_break_lexicographically():
    words = ["cba", "bca", "abc"]
    result = find_max(words)
    assert result == "abc"


def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"


def test_find_max_empty_raises():
    with pytest.raises(IndexError):
        find_max([])
