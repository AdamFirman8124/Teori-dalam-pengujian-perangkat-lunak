# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_words_string_empty():
    """Covers lines 3-4: empty string returns empty list."""
    assert words_string("") == []


def test_words_string_commas_replaced_with_spaces():
    """Covers lines 6-12: comma branch (line 10) and non-comma branch (line 12)."""
    assert words_string("one,two,three") == ["one", "two", "three"]


def test_words_string_mixed_separators():
    """Covers lines 14-15: join and split on mixed commas/spaces."""
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]


def test_words_string_only_commas():
    """Edge case: only commas produce no words."""
    assert words_string(",,,") == []


def test_words_string_single_word_no_comma():
    """Covers loop with only the else branch and final join/split."""
    assert words_string("hello") == ["hello"]
