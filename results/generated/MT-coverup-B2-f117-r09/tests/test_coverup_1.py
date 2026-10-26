# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

import pytest

from f117 import select_words


def test_select_words_basic_match():
    result = select_words("Mary had a little lamb", 4)
    assert result == ["little"]


def test_select_words_multiple_matches():
    result = select_words("simple little test", 4)
    assert result == ["simple", "little"]


def test_select_words_no_match_returns_empty_list():
    assert select_words("hello world", 10) == []


def test_select_words_empty_string():
    assert select_words("", 2) == []


def test_select_words_case_insensitive_vowels():
    assert select_words("AEI bcd", 0) == ["AEI"]
    assert select_words("AEI bcd", 3) == ["bcd"]


def test_select_words_inner_loop_counts_each_char():
    assert select_words("xyz", 3) == ["xyz"]
    assert select_words("xyz", 2) == []
