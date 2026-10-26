# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_unique_by_distinct_chars():
    # Word with the most distinct characters wins.
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"


def test_find_max_tie_broken_lexicographically():
    # Same number of distinct characters -> lexicographically smallest wins.
    assert find_max(["abc", "acb", "bac"]) == "abc"
    assert find_max(["ab", "ba", "cd"]) == "ab"


def test_find_max_single_element_and_duplicates():
    assert find_max(["hello"]) == "hello"
    # Duplicated characters do not increase the distinct count.
    assert find_max(["aabb", "ab", "xy"]) == "aabb"
