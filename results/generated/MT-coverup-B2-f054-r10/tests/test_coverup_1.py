# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f054 import same_chars


def test_same_chars_equal():
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    assert same_chars("abcd", "dddddddabc") is True
    assert same_chars("abc", "cba") is True
    assert same_chars("", "") is True


def test_same_chars_not_equal():
    assert same_chars("abcd", "dddddddabce") is False
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") is False
    assert same_chars("", "abc") is False
