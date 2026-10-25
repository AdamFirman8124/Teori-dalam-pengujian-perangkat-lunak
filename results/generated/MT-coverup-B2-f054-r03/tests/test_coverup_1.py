# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f054 import same_chars


def test_same_chars_returns_true_for_matching_character_sets():
    assert same_chars("abc", "cba") is True
    assert same_chars("aabbcc", "abc") is True


def test_same_chars_returns_false_for_different_character_sets():
    assert same_chars("abc", "abd") is False
    assert same_chars("", "a") is False
