# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_splits_whitespace():
    assert split_words("hello   world") == ["hello", "world"]


def test_split_words_replaces_commas_and_splits():
    assert split_words("hello,world,test") == ["hello", "world", "test"]


def test_split_words_counts_lowercase_characters_with_even_code_points():
    assert split_words("abcdefABC!") == 3
