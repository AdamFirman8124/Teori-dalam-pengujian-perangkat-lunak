# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


def test_same_chars_equal_sets():
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True


def test_same_chars_different_sets():
    assert same_chars("abcd", "adc") is False


def test_same_chars_empty_vs_nonempty():
    assert same_chars("", "a") is False


def test_same_chars_both_empty():
    assert same_chars("", "") is True


def test_same_chars_order_and_duplicates_ignored():
    assert same_chars("aabbcc", "cbacba") is True
