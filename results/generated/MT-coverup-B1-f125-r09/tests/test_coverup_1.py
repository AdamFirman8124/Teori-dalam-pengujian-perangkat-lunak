# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

from f125 import split_words


def test_split_on_spaces():
    assert split_words("hello world foo") == ["hello", "world", "foo"]


def test_split_on_commas():
    assert split_words("hello,world,foo") == ["hello", "world", "foo"]


def test_count_lowercase_even_letters():
    assert split_words("abcxyz") == 3
    assert split_words("") == 0
    assert split_words("ABCXYZ") == 0


def test_spaces_take_priority_over_commas():
    assert split_words("a c,b") == ["a", "c,b"]
