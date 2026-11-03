# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f086 import anti_shuffle


def test_anti_shuffle_already_sorted():
    """A word whose characters are already in order is returned unchanged."""
    assert anti_shuffle("Hi") == "Hi"


def test_anti_shuffle_sorts_characters_within_word():
    """Characters within a single word are sorted."""
    assert anti_shuffle("hello") == "ehllo"


def test_anti_shuffle_multiple_words():
    """Each word is sorted independently; words remain separated by spaces."""
    assert anti_shuffle("hello world") == "ehllo dlorw"


def test_anti_shuffle_unsorted_single_word():
    """A scrambled word is fully sorted."""
    assert anti_shuffle("bca") == "abc"


def test_anti_shuffle_empty_string():
    """An empty string yields an empty string."""
    assert anti_shuffle("") == ""


def test_anti_shuffle_mixed_case_and_spaces():
    """Sorting is by character code; multiple spaces are preserved as separators."""
    assert anti_shuffle("ba dc") == "ab cd"
