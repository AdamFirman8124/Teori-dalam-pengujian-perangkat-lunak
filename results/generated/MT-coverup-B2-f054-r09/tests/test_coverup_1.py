# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


def test_same_chars_equal_sets_different_order_and_duplicates():
    """Characters identical but in different order, with duplicates."""
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    assert same_chars("abcd", "dddddddabc") is True
    assert same_chars("abcddd", "abcddd") is True


def test_same_chars_different_sets():
    """Character sets differ, so the result must be False."""
    assert same_chars("eabcd", "dddddddabc") is False
    assert same_chars("abcd", "dddddddabce") is False
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") is False


def test_same_chars_empty_strings():
    """Edge cases: both empty (equal) and one empty (not equal)."""
    assert same_chars("", "") is True
    assert same_chars("", "a") is False
    assert same_chars("a", "") is False


def test_same_chars_single_and_repeated_chars():
    """Single characters and repeated identical characters."""
    assert same_chars("a", "a") is True
    assert same_chars("a", "b") is False
    assert same_chars("aaa", "a") is True
