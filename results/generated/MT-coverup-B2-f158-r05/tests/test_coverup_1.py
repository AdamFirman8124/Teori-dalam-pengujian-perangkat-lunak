# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_returns_word_with_most_unique_characters():
    words = ["name", "of", "string"]
    result = find_max(words)
    assert result == "string"
    # The input list must not be mutated by the function.
    assert words == ["name", "of", "string"]


def test_find_max_breaks_ties_lexicographically():
    # All words have 4 unique characters; the lexicographically
    # smallest one must be returned.
    assert find_max(["name", "enam", "game"]) == "enam"


def test_find_max_single_word():
    assert find_max(["aaaaaaa"]) == "aaaaaaa"


def test_find_max_empty_strings():
    assert find_max(["", ""]) == ""


def test_find_max_prefers_unique_count_over_length():
    # "abc" has 3 unique chars, "aaaa" has only 1, even though it is longer.
    assert find_max(["aaaa", "abc"]) == "abc"
