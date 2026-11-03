# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_picks_word_with_most_unique_characters():
    """Line 3 executes: 'string' has 6 unique chars vs 4 ('name') and 2 ('of')."""
    result = find_max(["name", "of", "string"])
    assert result == "string"


def test_find_max_breaks_ties_lexicographically():
    """All words have 4 unique chars, so the sort must compare the second
    tuple component (the word itself); 'enam' is lexicographically first."""
    result = find_max(["name", "enam", "game"])
    assert result == "enam"


def test_find_max_prefers_unique_count_over_word_length():
    """'aaaaaaa' is the longest word but has only 1 unique char, tying with
    'bb' and 'cc'; the lexicographic tie-break still selects 'aaaaaaa'."""
    result = find_max(["aaaaaaa", "bb", "cc"])
    assert result == "aaaaaaa"


def test_find_max_single_element_list():
    """A one-element list still exercises the key lambda and the [0] index."""
    result = find_max(["hello"])
    assert result == "hello"


def test_find_max_returns_first_on_exact_duplicates():
    """Duplicate words produce identical keys; the first occurrence is kept."""
    result = find_max(["abc", "abc", "ab"])
    assert result == "abc"
