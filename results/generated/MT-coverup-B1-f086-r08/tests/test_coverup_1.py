# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f086 import anti_shuffle


def test_anti_shuffle_sorts_characters_within_each_word():
    assert anti_shuffle("hello world") == "ehllo dlorw"


def test_anti_shuffle_preserves_spaces_and_handles_empty_words():
    assert anti_shuffle("ba  dc") == "ab  cd"
