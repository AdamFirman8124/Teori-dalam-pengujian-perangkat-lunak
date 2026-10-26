# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest

from f125 import split_words


def test_split_words_space_branch():
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("a b c") == ["a", "b", "c"]


def test_split_words_space_takes_precedence_over_comma():
    assert split_words("a, b") == ["a,", "b"]


def test_split_words_comma_branch():
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words("hello,world") == ["hello", "world"]


def test_split_words_else_branch_counts_even_lowercase():
    # 'b' (98) and 'd' (100) are lowercase with even ord; 'a' (97) and 'c' (99) are odd
    assert split_words("abcd") == 2
    assert split_words("b") == 1


def test_split_words_else_branch_ignores_uppercase_and_non_letters():
    assert split_words("ABC") == 0
    assert split_words("B2") == 0
    assert split_words("") == 0
