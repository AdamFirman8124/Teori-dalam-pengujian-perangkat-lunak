# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_words_string_empty_string():
    """Empty input hits the falsy branch (lines 3-4) and returns an empty list."""
    result = words_string("")
    assert result == []


def test_words_string_none_returns_empty_list():
    """None is falsy, so it also takes the early-return branch and yields []."""
    result = words_string(None)
    assert result == []


def test_words_string_commas_converted_to_spaces():
    """Commas are treated as whitespace separators (lines 6-12, 14-15)."""
    result = words_string("one,two,three")
    assert result == ["one", "two", "three"]


def test_words_string_no_commas():
    """Plain whitespace-separated string splits normally."""
    result = words_string("hello world")
    assert result == ["hello", "world"]


def test_words_string_mixed_separators():
    """Mixed commas and spaces, plus leading/trailing commas, are all handled."""
    result = words_string(",alpha beta, gamma ,")
    assert result == ["alpha", "beta", "gamma"]


def test_words_string_multiple_consecutive_commas():
    """Consecutive commas produce only whitespace, no empty tokens."""
    result = words_string("a,,b")
    assert result == ["a", "b"]


def test_words_string_single_word_no_separator():
    """A single word without separators returns a one-element list."""
    result = words_string("word")
    assert result == ["word"]


def test_words_string_only_commas():
    """A string of only commas yields an empty list (no tokens)."""
    result = words_string(",,,")
    assert result == []


def test_words_string_non_iterable_raises_type_error():
    """A truthy, non-iterable input fails during iteration with TypeError."""
    with pytest.raises(TypeError):
        words_string(42)
