# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f086 import anti_shuffle


def test_anti_shuffle_sorts_characters_within_each_word():
    # Each word's characters are sorted; word order and spacing are preserved.
    assert anti_shuffle("Hello World") == "Hello Wdlor"


def test_anti_shuffle_empty_string():
    # Empty input yields empty output (split(' ') produces ['']).
    assert anti_shuffle("") == ""


def test_anti_shuffle_reorders_words_characters():
    # Words whose characters are out of order get fully sorted.
    assert anti_shuffle("bca fed") == "abc def"


def test_anti_shuffle_preserves_multiple_spaces():
    # Consecutive spaces produce empty tokens that are preserved on join.
    assert anti_shuffle("ba  ab") == "ab  ab"


def test_anti_shuffle_single_word_and_single_char():
    assert anti_shuffle("dcba") == "abcd"
    assert anti_shuffle("a") == "a"
