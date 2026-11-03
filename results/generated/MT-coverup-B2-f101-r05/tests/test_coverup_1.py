# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_empty_string_returns_empty_list():
    """Covers lines 3-4: falsy input short-circuits to []."""
    assert words_string("") == []
    assert words_string("") is not None


def test_string_with_commas_replaces_commas_and_splits():
    """Covers lines 6-15 including the comma branch (line 9-10)."""
    result = words_string("one,two,three")
    assert result == ["one", "two", "three"]


def test_string_without_commas_uses_else_branch():
    """Covers lines 8-12 including the else branch (line 12)."""
    result = words_string("one two three")
    assert result == ["one", "two", "three"]


def test_mixed_commas_and_spaces():
    """Both branches exercised in a single call."""
    result = words_string("one, two ,three four")
    assert result == ["one", "two", "three", "four"]


def test_only_commas_yields_empty_list():
    """All characters take the comma branch; split of spaces gives []."""
    assert words_string(",,,") == []


def test_single_word_no_separators():
    """Single non-comma character loop iteration, join, and split."""
    assert words_string("hello") == ["hello"]


def test_leading_and_trailing_commas():
    """Commas at the boundaries produce no empty tokens."""
    assert words_string(",hello,world,") == ["hello", "world"]


def test_input_string_is_not_mutated():
    """The function must not modify its argument (no state pollution)."""
    s = "a,b,c"
    words_string(s)
    assert s == "a,b,c"
