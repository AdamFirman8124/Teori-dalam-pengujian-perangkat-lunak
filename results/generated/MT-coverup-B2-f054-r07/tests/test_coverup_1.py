# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f054 import same_chars


def test_same_chars_equal_sets_true():
    """Character sets match (duplicates and order irrelevant) -> True."""
    assert same_chars("eabcdzzzz", "dddzzzzzzzddeddabc") is True
    assert same_chars("abc", "cba") is True


def test_same_chars_different_sets_false():
    """Character sets differ -> False."""
    assert same_chars("abcd", "dddddddabce") is False
    assert same_chars("eabcdzzzz", "dddzzzzzzzddddabc") is False


def test_same_chars_empty_strings():
    """Edge cases with empty strings."""
    assert same_chars("", "") is True
    assert same_chars("", "a") is False
    assert same_chars("a", "") is False
