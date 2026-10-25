# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f086 import anti_shuffle


def test_anti_shuffle_sorts_characters_within_each_word():
    result = anti_shuffle("hello world")
    assert result == "ehllo dlorw"


def test_anti_shuffle_single_word():
    assert anti_shuffle("dcba") == "abcd"


def test_anti_shuffle_empty_string():
    assert anti_shuffle("") == ""


def test_anti_shuffle_multiple_spaces_preserved():
    assert anti_shuffle("ab  cd") == "ab  cd"


def test_anti_shuffle_no_state_pollution():
    # Pure function: same input always yields same output, no side effects.
    assert anti_shuffle("cba") == "abc"
    assert anti_shuffle("cba") == "abc"
