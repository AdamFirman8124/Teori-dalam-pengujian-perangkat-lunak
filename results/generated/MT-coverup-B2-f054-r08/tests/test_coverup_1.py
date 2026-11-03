# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


def test_same_chars_equal_sets():
    """Strings with the same set of characters (order/duplicates differ)."""
    assert same_chars("abc", "cba") is True
    assert same_chars("aabbcc", "abc") is True
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True


def test_same_chars_different_sets():
    """Strings whose character sets differ."""
    assert same_chars("abcd", "abcde") is False
    assert same_chars("abc", "abd") is False


def test_same_chars_empty_strings():
    """Empty strings have equal (empty) character sets."""
    assert same_chars("", "") is True
    assert same_chars("", "a") is False
    assert same_chars("a", "") is False


def test_same_chars_identical_strings():
    """Identical strings trivially have the same character set."""
    assert same_chars("hello", "hello") is True


def test_same_chars_unicode():
    """Works with non-ASCII characters."""
    assert same_chars("héllo", "olléh") is True
    assert same_chars("héllo", "hello") is False
