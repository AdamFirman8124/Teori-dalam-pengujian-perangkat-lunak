# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_with_spaces():
    assert split_words("hello world,again") == ["hello", "world,again"]


def test_split_words_with_commas():
    assert split_words("hello,world,again") == ["hello", "world", "again"]


def test_split_words_counts_lowercase_even_codepoints():
    assert split_words("abcdefABC123") == 3
