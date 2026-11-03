# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest

from f125 import split_words


def test_split_words_with_space():
    """Covers line 3-4: string containing a space is split on whitespace."""
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("a b  c") == ["a", "b", "c"]


def test_split_words_with_comma():
    """Covers line 5-6: string with commas (but no spaces) has commas
    replaced by spaces before splitting."""
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("a,b,,c") == ["a", "b", "c"]


def test_split_words_space_takes_precedence_over_comma():
    """Branch order: a string containing both a space and a comma must
    take the first branch (split on whitespace only)."""
    assert split_words("a,b c") == ["a,b", "c"]


def test_split_words_counts_lowercase_even_ord_chars():
    """Covers line 8: no space and no comma -> count lowercase characters
    whose ordinal value is even."""
    # 'b'(98), 'd'(100), 'f'(102) are lowercase with even ordinals.
    assert split_words("abcdef") == 3
    # Uppercase letters are excluded even when their ordinal is even
    # ('B' is 66, 'D' is 100, 'F' is 102).
    assert split_words("ABCDEF") == 0
    # Digits and punctuation are not lowercase.
    assert split_words("2468!?") == 0
    # Empty string contains neither a space nor a comma.
    assert split_words("") == 0
