# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


def test_same_chars_equal_sets():
    """Characters of s0 and s1 form the same set -> True."""
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True


def test_same_chars_equal_sets_subset():
    """One string's characters are a subset of the other's -> True."""
    assert same_chars("abcd", "dddddddabc") is True


def test_same_chars_extra_char():
    """s1 has an extra distinct character -> False."""
    assert same_chars("abcd", "dddddddabce") is False


def test_same_chars_missing_char():
    """s0 has a distinct character missing from s1 -> False."""
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") is False


def test_same_chars_empty_strings():
    """Both empty strings have the same (empty) character set -> True."""
    assert same_chars("", "") is True


def test_same_chars_empty_vs_nonempty():
    """Empty vs non-empty string -> False."""
    assert same_chars("", "a") is False
