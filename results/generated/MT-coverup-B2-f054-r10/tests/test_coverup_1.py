# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f054 import same_chars


def test_same_chars_equal_sets():
    assert same_chars("abc", "cba") is True
    assert same_chars("abc", "abc") is True


def test_same_chars_different_sets():
    assert same_chars("abc", "abcd") is False
    assert same_chars("abc", "abd") is False


def test_same_chars_empty_strings():
    assert same_chars("", "") is True


def test_same_chars_empty_vs_nonempty():
    assert same_chars("", "a") is False
    assert same_chars("a", "") is False


def test_same_chars_ignores_multiplicity_and_order():
    assert same_chars("aab", "ab") is True
    assert same_chars("aabbcc", "cba") is True
