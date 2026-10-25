# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


def test_same_chars_equal_sets():
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True


def test_same_chars_different_sets():
    assert same_chars("abcd", "dddddddabcde") is False


def test_same_chars_empty_string():
    assert same_chars("", "") is True
    assert same_chars("", "a") is False
