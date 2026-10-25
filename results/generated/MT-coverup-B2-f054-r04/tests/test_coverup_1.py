# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f054 import same_chars


def test_same_chars_with_matching_and_different_character_sets():
    assert same_chars("hello", "oleh") is True
    assert same_chars("hello", "world") is False
