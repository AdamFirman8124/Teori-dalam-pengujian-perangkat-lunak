# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

from f101 import words_string


def test_words_string_returns_empty_list_for_empty_input():
    assert words_string("") == []


def test_words_string_replaces_commas_and_splits_into_words():
    assert words_string("hello,world, pytest") == ["hello", "world", "pytest"]
