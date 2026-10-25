# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_with_space():
    assert split_words("alpha,beta gamma") == ["alpha,beta", "gamma"]


def test_split_words_with_comma():
    assert split_words("alpha,beta") == ["alpha", "beta"]


def test_split_words_without_space_or_comma():
    assert split_words("abcdEF") == 2
