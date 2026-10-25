# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

import pytest

from f117 import select_words


def test_select_words_basic_match():
    # "world" has 4 consonants (w, r, l, d); "hello" has only 3 (h, l, l)
    result = select_words("hello world", 4)
    assert result == ["world"]


def test_select_words_no_match():
    assert select_words("hello world", 2) == []


def test_select_words_empty_string():
    assert select_words("", 3) == []


def test_select_words_case_insensitive_vowels():
    # "AEIOUbc" -> consonants are b, c -> 2
    result = select_words("AEIOUbc", 2)
    assert result == ["AEIOUbc"]


def test_select_words_mixed_counts():
    # "Mary" -> 3 consonants (M, r, y); "lamb" -> 3 (l, m, b); "a" -> 0
    result = select_words("Mary lamb a little", 3)
    assert result == ["Mary", "lamb"]


def test_select_words_zero_consonants():
    result = select_words("a e i o u", 0)
    assert result == ["a", "e", "i", "o", "u"]


def test_select_words_returns_new_list():
    result = select_words("test", 3)
    assert result == ["test"]
    result.append("mutated")
    # A second call must not be affected by mutation of the previous result
    assert select_words("test", 3) == ["test"]
