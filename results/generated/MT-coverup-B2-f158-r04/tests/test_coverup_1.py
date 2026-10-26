# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_unique_chars_win():
    # "apple" has 4 unique chars, beats "banana" (3) and "cat" (3)
    assert find_max(["banana", "apple", "cat"]) == "apple"


def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"


def test_find_max_returns_element_from_input_on_tie():
    # "ab" and "aa" both have 2 unique chars; don't assume tie-break direction,
    # only assert the postconditions that must hold.
    words = ["ab", "aa"]
    result = find_max(words)
    assert result in words
    assert len(set(result)) == max(len(set(w)) for w in words)


def test_find_max_duplicates_counted_once():
    # "aabb" has only 2 unique chars, same as "ab"
    words = ["aabb", "ab"]
    result = find_max(words)
    assert result in words
    assert len(set(result)) == 2


def test_find_max_returns_element_not_copy():
    words = ["xyz"]
    result = find_max(words)
    assert result is words[0]
