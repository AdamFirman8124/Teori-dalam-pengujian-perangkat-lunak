# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_words_string_empty():
    """Empty string should return an empty list (covers lines 3-4)."""
    assert words_string("") == []


def test_words_string_with_commas():
    """Commas are replaced by spaces and the result is split (covers lines 6-15)."""
    assert words_string("one,two,three") == ["one", "two", "three"]


def test_words_string_without_commas():
    """A string without commas is simply split on whitespace."""
    assert words_string("hello world") == ["hello", "world"]


def test_words_string_only_commas():
    """A string of only commas becomes only spaces, which split to nothing."""
    assert words_string(",,,") == []


def test_words_string_mixed():
    """Mixed commas and spaces are both treated as separators."""
    assert words_string("a, b,c d") == ["a", "b", "c", "d"]


def test_words_string_single_word():
    """A single word with no separators returns a one-element list."""
    assert words_string("word") == ["word"]
