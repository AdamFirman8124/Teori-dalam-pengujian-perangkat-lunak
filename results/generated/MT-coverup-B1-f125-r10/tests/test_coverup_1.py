# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_with_space():
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("a, b") == ["a,", "b"]


def test_split_words_with_comma():
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("a,b,c") == ["a", "b", "c"]


def test_split_words_else_counts_even_lowercase():
    # b=98, d=100, f=102 are even; a=97, c=99, e=101 are odd
    assert split_words("abcdef") == 3
    assert split_words("bdf") == 3
    assert split_words("ace") == 0


def test_split_words_else_ignores_non_lowercase():
    assert split_words("ABC") == 0
    assert split_words("123!@#") == 0
    assert split_words("") == 0


def test_split_words_else_mixed_covers_all_conditions():
    # A: islower False, b: islower True and even, c: islower True but odd
    assert split_words("Abc") == 1
    assert split_words("Abdf") == 3
