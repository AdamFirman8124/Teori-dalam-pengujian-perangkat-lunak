# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_splits_space_separated_text():
    assert split_words("one two three") == ["one", "two", "three"]


def test_split_words_splits_comma_separated_text():
    assert split_words("one,two,three") == ["one", "two", "three"]


def test_split_words_counts_lowercase_characters_with_even_codepoints():
    assert split_words("aBcdef") == 2
