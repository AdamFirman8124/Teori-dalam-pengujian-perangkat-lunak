# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_words_with_space():
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello, world") == ["hello,", "world"]


def test_split_words_with_comma_only():
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("a,b,c") == ["a", "b", "c"]


def test_split_words_no_delimiter():
    # b(98), d(100) are lowercase with even ord -> count 2
    assert split_words("abcd") == 2
    # a(97), c(99) are odd -> count 0, plus uppercase/non-lower excluded
    assert split_words("aAcC1!") == 0
    assert split_words("") == 0
