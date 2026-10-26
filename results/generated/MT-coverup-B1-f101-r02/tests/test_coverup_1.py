# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_words_string_empty_string():
    """Covers lines 3-4: empty input returns an empty list."""
    assert words_string("") == []


def test_words_string_commas_replaced_with_spaces():
    """Covers lines 6-12 (comma branch): commas become spaces."""
    assert words_string("one,two,three") == ["one", "two", "three"]


def test_words_string_plain_spaces():
    """Covers lines 6-12 (else branch) and line 14-15: existing spaces are kept."""
    assert words_string("one two three") == ["one", "two", "three"]


def test_words_string_mixed_separators():
    """Covers both branches plus the join/split on lines 14-15."""
    assert words_string("one, two ,three four") == ["one", "two", "three", "four"]


def test_words_string_single_word_no_separators():
    """Covers loop with no comma branch taken, join and split."""
    assert words_string("hello") == ["hello"]


def test_words_string_only_commas():
    """Edge case: only separators yields an empty list after split."""
    assert words_string(",,,") == []
