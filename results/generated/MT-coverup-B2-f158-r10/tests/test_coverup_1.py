# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_picks_word_with_most_unique_chars():
    words = ["name", "of", "string"]
    # "string" has 6 unique chars, more than "name" (4) or "of" (2)
    assert find_max(words) == "string"


def test_find_max_tie_broken_lexicographically():
    words = ["name", "same"]  # both have 4 unique chars -> lexicographic tie-break
    assert find_max(words) == "name"

    words = ["bcb", "aba"]  # both have 2 unique chars -> "aba" comes first
    assert find_max(words) == "aba"


def test_find_max_single_element():
    assert find_max(["only"]) == "only"
