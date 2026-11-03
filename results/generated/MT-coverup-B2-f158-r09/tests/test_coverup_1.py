# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_most_unique_characters():
    """Word with the greatest number of unique characters wins."""
    words = ["name", "of", "string"]
    result = find_max(words)
    # "string" has 6 unique chars; others have fewer.
    assert result == "string"
    assert len(set(result)) == max(len(set(w)) for w in words)


def test_find_max_tie_broken_lexicographically():
    """On equal unique-character counts, the lexicographically smallest word wins."""
    words = ["name", "enam", "game"]
    result = find_max(words)
    # All three words have 4 unique chars -> "enam" is the smallest alphabetically.
    assert result == "enam"
    max_count = max(len(set(w)) for w in words)
    candidates = [w for w in words if len(set(w)) == max_count]
    assert result == min(candidates)


def test_find_max_repeated_letters_count_once():
    """Repeated letters only count once toward uniqueness (set semantics)."""
    words = ["aaaaaaa", "bb", "cc"]
    result = find_max(words)
    # Each word has exactly 1 unique char -> tie broken alphabetically: "aaaaaaa".
    assert result == "aaaaaaa"


def test_find_max_single_word():
    """A single-element list returns that element."""
    assert find_max(["hello"]) == "hello"


def test_find_max_empty_string_element():
    """An empty string is handled gracefully (0 unique chars)."""
    words = ["", "a"]
    result = find_max(words)
    assert result == "a"


def test_find_max_does_not_mutate_input():
    """The input list must remain unchanged (sorted() returns a new list)."""
    words = ["b", "aa", "c"]
    snapshot = list(words)
    find_max(words)
    assert words == snapshot
