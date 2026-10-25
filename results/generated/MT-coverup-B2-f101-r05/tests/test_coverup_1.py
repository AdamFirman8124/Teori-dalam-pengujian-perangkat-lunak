# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_words_string_empty_returns_empty_list():
    result = words_string("")
    assert result == []
    assert isinstance(result, list)


def test_words_string_none_like_falsy_returns_empty_list():
    # Covers the `if not s` branch for other falsy inputs.
    assert words_string(None) == []


def test_words_string_single_word_no_comma():
    # Covers the else branch only (no comma present).
    assert words_string("hello") == ["hello"]


def test_words_string_comma_separated():
    # Covers the comma branch.
    assert words_string("one,two,three") == ["one", "two", "three"]


def test_words_string_mixed_commas_and_spaces():
    # Covers both branches interleaved plus split() collapsing whitespace.
    assert words_string("one, two,three") == ["one", "two", "three"]
    assert words_string("a,b c,d") == ["a", "b", "c", "d"]


def test_words_string_leading_trailing_and_repeated_commas():
    assert words_string(",a,,b,") == ["a", "b"]


def test_words_string_only_commas_returns_empty_list():
    assert words_string(",,,") == []


def test_words_string_only_whitespace_returns_empty_list():
    assert words_string("   ") == []


def test_words_string_does_not_mutate_input():
    original = "x,y z"
    s = original
    words_string(s)
    assert s == original
