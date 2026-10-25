# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f158 import find_max


def test_find_max_most_distinct_chars():
    words = ["aaa", "ab", "abc"]
    result = find_max(words)
    assert result == "abc"
    assert words == ["aaa", "ab", "abc"]


def test_find_max_tie_break_lexicographically_smallest():
    words = ["cba", "bca", "abc"]
    assert find_max(words) == "abc"


def test_find_max_tie_break_with_different_lengths():
    assert find_max(["hello", "world"]) == "world"
    assert find_max(["abcd", "abce"]) == "abcd"
    assert find_max(["Abc", "abc"]) == "Abc"


def test_find_max_single_element():
    assert find_max(["zebra"]) == "zebra"


def test_find_max_with_empty_and_duplicates():
    assert find_max(["", "a", "aa"]) == "a"
    assert find_max(["aaa", "ab"]) == "ab"
