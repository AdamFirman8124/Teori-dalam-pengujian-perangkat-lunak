# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_with_spaces():
    assert split_words("hello world") == ["hello", "world"]


def test_split_words_with_commas():
    assert split_words("hello,world") == ["hello", "world"]


def test_split_words_counts_even_lowercase_characters():
    assert split_words("abcdefXYZ") == 3
