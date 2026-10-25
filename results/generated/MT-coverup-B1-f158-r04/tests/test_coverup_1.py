# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_returns_word_with_most_unique_chars():
    # "apple" has 4 unique chars, "banana" has 3, "cherry" has 5
    assert find_max(["apple", "banana", "cherry"]) == "cherry"


def test_find_max_tie_broken_by_lexicographic_order():
    # "ab" and "cd" both have 2 unique chars -> lexicographically smallest wins
    assert find_max(["cd", "ab"]) == "ab"


def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"


def test_find_max_duplicate_letters_counted_once():
    # "aabb" has only 2 unique chars, same as "xy", so "aabb" wins lexicographically
    assert find_max(["xy", "aabb"]) == "aabb"
