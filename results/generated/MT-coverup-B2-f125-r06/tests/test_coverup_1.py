# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest

from f125 import split_words


def test_split_words_with_spaces():
    """Covers lines 3-4: txt containing spaces is split on whitespace."""
    result = split_words("hello world foo")
    assert result == ["hello", "world", "foo"]


def test_split_words_with_commas():
    """Covers lines 5-6: txt containing commas (but no spaces) is split on commas."""
    result = split_words("one,two,three")
    assert result == ["one", "two", "three"]


def test_split_words_no_space_no_comma_counts_even_lowercase():
    """Covers line 8: counts lowercase chars whose ordinal is even.

    'b' (98), 'd' (100) and 'f' (102) qualify; 'a', 'c', 'e' do not.
    """
    result = split_words("abcdef")
    assert result == 3


def test_split_words_no_space_no_comma_uppercase_and_odd_excluded():
    """Covers line 8 again: uppercase letters and odd-ordinal lowercase letters are excluded."""
    # 'A' is uppercase (excluded), 'a' (97, odd) excluded, 'b' (98, even) counted.
    result = split_words("AaBb")
    assert result == 1


def test_split_words_empty_string():
    """Covers line 8 with an empty string: no characters, count is 0."""
    result = split_words("")
    assert result == 0
