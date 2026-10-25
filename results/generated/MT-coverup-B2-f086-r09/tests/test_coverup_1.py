# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f086 import anti_shuffle


def test_anti_shuffle_single_word():
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("cba") == "abc"


def test_anti_shuffle_multiple_words():
    assert anti_shuffle("hello world") == "ehllo dlorw"
    assert anti_shuffle("Hi there") == "Hi eehrt"


def test_anti_shuffle_empty_string():
    assert anti_shuffle("") == ""


def test_anti_shuffle_preserves_spaces_and_misc_chars():
    assert anti_shuffle("ab  cd") == "ab  cd"
    assert anti_shuffle("321 21") == "123 12"
    assert anti_shuffle("!dcba") == "!abcd"
