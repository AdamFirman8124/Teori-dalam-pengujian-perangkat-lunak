# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

import pytest

from f117 import select_words


def test_select_words_collects_matching_words_in_order():
    """Words whose consonant count equals n are returned in order (lines 3-11)."""
    # cat -> c,t = 2 ; dog -> d,g = 2 ; bird -> b,r,d = 3
    assert select_words("cat dog bird", 2) == ["cat", "dog"]


def test_select_words_no_match_returns_empty_list():
    """Covers the False branch of 'n_consonants == n' (line 9)."""
    # hello -> h,l,l = 3 ; world -> w,r,l,d = 4 ; nothing has 10 consonants
    assert select_words("hello world", 10) == []


def test_select_words_empty_string():
    """An empty string skips the outer loop body entirely (zero-iteration branch of line 4)."""
    assert select_words("", 3) == []


def test_select_words_uppercase_letters_are_lowercased():
    """Covers both branches of the vowel check (line 7) with uppercase input."""
    # 'Uncle' -> U(u vowel), n, c, l, e(vowel) => 3 consonants
    assert select_words("Uncle", 3) == ["Uncle"]
    # 'AAAb' -> A,A,A vowels, b consonant => 1 consonant
    assert select_words("AAAb", 1) == ["AAAb"]


def test_select_words_zero_consonants_matches_vowel_only_words():
    """Words made only of vowels have 0 consonants (False branch of line 7)."""
    assert select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]


def test_select_words_mixed_matches_and_non_matches():
    """Both branches of line 9 within a single string."""
    # simple -> s,m,p,l = 4 ; space -> s,p,c = 3
    assert select_words("simple space", 3) == ["space"]
    assert select_words("simple space", 4) == ["simple"]


def test_select_words_single_character_word():
    """Minimal inner-loop coverage: one-character word, consonant counted once."""
    assert select_words("b", 1) == ["b"]
    assert select_words("a", 1) == []
