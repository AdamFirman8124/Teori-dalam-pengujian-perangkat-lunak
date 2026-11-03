# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest

from f125 import split_words


def test_split_words_with_space():
    """Covers line 3 (True branch) and line 4."""
    result = split_words("hello world")
    assert result == ["hello", "world"]


def test_split_words_with_comma_no_space():
    """Covers line 3 (False branch), line 5 (True branch) and line 6."""
    result = split_words("hello,world")
    assert result == ["hello", "world"]


def test_split_words_no_space_no_comma():
    """Covers line 3 and line 5 (False branches) and line 8.

    Lowercase chars with even ord: 'b' (98), 'd' (100), 'f' (102).
    """
    result = split_words("abcdef")
    assert result == 3


def test_split_words_empty_string():
    """Covers the else branch (line 8) with an empty iterable."""
    result = split_words("")
    assert result == 0
