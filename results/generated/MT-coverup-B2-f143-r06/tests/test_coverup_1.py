# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

"""Tests for f143.words_in_sentence.

The function keeps only the words whose length is a prime number
(length 1 is excluded, length 2 is kept, composite lengths are excluded)
and returns them joined by single spaces.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test
operates only on local string literals, avoiding any state pollution.
"""

import pytest

from f143 import words_in_sentence


def test_empty_sentence_returns_empty_string():
    # Exercises lines 3 and 13 with the loop body never entered.
    assert words_in_sentence("") == ""


def test_single_character_word_is_excluded():
    # Covers the True branch of `if len(word) == 1` (flg = 1),
    # an empty inner loop (range(2, 1)), and the False outcome of
    # `if flg == 0 or len(word) == 2` (word not appended).
    assert words_in_sentence("a") == ""


def test_two_character_word_is_included():
    # Covers the False branch of `if len(word) == 1`, an empty inner
    # loop (range(2, 2)), and appending via the `flg == 0` condition.
    assert words_in_sentence("ab") == "ab"


def test_prime_length_word_is_included():
    # Length 3: inner loop runs once, 3 % 2 != 0 covers the False
    # branch of `if len(word) % i == 0`, flg stays 0, word appended.
    assert words_in_sentence("abc") == "abc"


def test_composite_length_word_is_excluded():
    # Length 4: 4 % 2 == 0 covers the True branch of
    # `if len(word) % i == 0` (flg = 1), word not appended.
    assert words_in_sentence("abcd") == ""


def test_mixed_sentence_keeps_only_prime_length_words():
    # Single call exercising every branch:
    #   "lets"    -> len 4, composite, excluded (divisor branch True)
    #   "go"      -> len 2, included (empty inner loop, flg == 0)
    #   "for"     -> len 3, prime, included (divisor branch False)
    #   "swimming"-> len 8, composite, excluded (divisor branch True)
    assert words_in_sentence("lets go for swimming") == "go for"


def test_multiple_matching_words_are_joined_in_order():
    # "a" (len 1, excluded), "bb" (len 2), "ccc" (len 3),
    # "dddd" (len 4, excluded), "eeeee" (len 5, prime).
    assert words_in_sentence("a bb ccc dddd eeeee") == "bb ccc eeeee"


def test_result_is_space_joined_string():
    result = words_in_sentence("is it true")
    # "is" (2, kept), "it" (2, kept), "true" (4, dropped)
    assert result == "is it"
    assert isinstance(result, str)
    assert " " in result
