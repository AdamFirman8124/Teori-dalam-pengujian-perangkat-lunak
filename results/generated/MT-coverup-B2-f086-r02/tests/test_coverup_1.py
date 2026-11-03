# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f086.anti_shuffle.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required; each test only relies on
its own inputs and therefore cannot pollute state.
"""

import pytest

from f086 import anti_shuffle


def test_anti_shuffle_single_word_already_sorted():
    """A word whose characters are already in ASCII order is unchanged."""
    assert anti_shuffle('Hi') == 'Hi'


def test_anti_shuffle_single_word_unsorted():
    """Characters within a word are rearranged in ascending ASCII order."""
    assert anti_shuffle('hello') == 'ehllo'


def test_anti_shuffle_multiple_words():
    """Each word is sorted independently; word order and spaces are kept."""
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'


def test_anti_shuffle_empty_string():
    """An empty string yields an empty string (exercises the join on [])."""
    assert anti_shuffle('') == ''


def test_anti_shuffle_preserves_blank_words():
    """Spaces (including consecutive/leading/trailing ones) are preserved.

    Note: characters are sorted *within* each word; the words themselves
    are never reordered, so single-character words stay in place.
    """
    assert anti_shuffle('dc ba') == 'cd ab'
    assert anti_shuffle('  hi  ') == '  hi  '
    assert anti_shuffle('a  b') == 'a  b'


def test_anti_shuffle_mixed_digits_symbols_letters():
    """Sorting is by ASCII value: symbols < digits < uppercase < lowercase."""
    assert anti_shuffle('ba21!') == '!12ab'
    assert anti_shuffle('zA9!') == '!9Az'


def test_anti_shuffle_returns_str():
    """The result is always a str instance."""
    assert isinstance(anti_shuffle('anything'), str)
