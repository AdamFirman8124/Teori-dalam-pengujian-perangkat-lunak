# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


def test_same_chars_equal_sets():
    """Strings with identical character sets (regardless of order/duplicates) return True."""
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    assert same_chars("abcd", "dddddddabc") is True
    assert same_chars("abc", "cba") is True


def test_same_chars_different_sets():
    """Strings with different character sets return False."""
    assert same_chars("abcd", "dddddddabce") is False
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") is False


def test_same_chars_empty_and_single():
    """Edge cases: empty strings and single characters."""
    assert same_chars("", "") is True
    assert same_chars("", "a") is False
    assert same_chars("a", "a") is True
    assert same_chars("a", "b") is False
