# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_returns_word_with_most_unique_characters():
    # "string" has 6 unique characters, more than "name" (4) or "of" (2).
    assert find_max(["name", "of", "string"]) == "string"


def test_find_max_breaks_ties_lexicographically():
    # All three words have 4 unique characters; "enam" is lexicographically
    # smallest, so it must be selected.
    assert find_max(["name", "enam", "game"]) == "enam"


def test_find_max_all_same_unique_count_prefers_smallest_word():
    # Each word has exactly 1 unique character; "aaaaaaa" sorts first.
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"


def test_find_max_single_element_list():
    assert find_max(["aaaaaaa"]) == "aaaaaaa"


def test_find_max_empty_list_raises_index_error():
    # Line 3 is still entered (sorted(...) is evaluated) before [0] raises.
    with pytest.raises(IndexError):
        find_max([])
