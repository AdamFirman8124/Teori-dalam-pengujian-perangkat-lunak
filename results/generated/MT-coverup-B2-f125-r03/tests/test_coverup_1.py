# file: project/f125/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8]]}

import pytest

from f125 import split_words


def test_split_words_with_space_returns_list_of_words():
    """Lines 3-4: a string containing a space is split on whitespace."""
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("a b  c") == ["a", "b", "c"]  # runs of spaces collapse
    assert split_words("single ") == ["single"]  # trailing space yields one word


def test_split_words_with_comma_no_space():
    """Lines 5-6: no space but a comma -> commas become spaces, then split."""
    assert split_words("hello,world") == ["hello", "world"]
    assert split_words("a,b,c") == ["a", "b", "c"]
    assert split_words(",") == []  # only a comma -> empty list


def test_split_words_space_branch_takes_precedence():
    """Line 3 branch wins when both a space and a comma are present."""
    assert split_words("a b,c") == ["a", "b,c"]


def test_split_words_counts_lowercase_even_ord_chars():
    """Line 8: no space, no comma -> count lowercase chars with even ord."""
    # 'b'(98), 'd'(100), 'f'(102) are lowercase with even ord; the rest don't count.
    assert split_words("abcdef") == 3
    assert split_words("") == 0  # empty string counts nothing
    # Uppercase letters, odd-ord lowercase letters and digits are all excluded.
    assert split_words("bBdD2") == 2  # only 'b' and 'd'
    assert split_words("ace") == 0  # all lowercase but odd ord
    assert split_words("ACE") == 0  # all uppercase
