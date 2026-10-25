# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest

from f125 import split_words


def test_split_words_with_spaces():
    result = split_words("hello world foo")
    assert result == ["hello", "world", "foo"]


def test_split_words_with_commas():
    result = split_words("hello,world,foo")
    assert result == ["hello", "world", "foo"]


def test_split_words_count_even_lowercase():
    # 'b' (98), 'd' (100), 'f' (102), 'h' (104) are lowercase with even ord;
    # uppercase 'B' and odd-ord letters like 'a' (97) are excluded.
    result = split_words("abcdefBgh")
    assert result == 4


def test_split_words_no_matches():
    result = split_words("ACEG")
    assert result == 0
