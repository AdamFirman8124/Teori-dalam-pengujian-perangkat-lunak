# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_words_string_empty():
    """An empty string hits the early return (covers lines 3-4)."""
    assert words_string("") == []


def test_words_string_with_commas():
    """Commas are replaced by spaces, then the result is split
    (covers lines 6, 8-10, 14-15)."""
    assert words_string("one,two,three") == ["one", "two", "three"]


def test_words_string_without_commas():
    """Non-comma characters take the else branch (covers line 12)."""
    assert words_string("hello world") == ["hello", "world"]


def test_words_string_only_commas():
    """A string of only commas becomes only spaces, which split to nothing."""
    assert words_string(",,,") == []


def test_words_string_mixed_separators():
    """Mixed commas and spaces, including consecutive separators."""
    assert words_string("a, b,,c  d") == ["a", "b", "c", "d"]
