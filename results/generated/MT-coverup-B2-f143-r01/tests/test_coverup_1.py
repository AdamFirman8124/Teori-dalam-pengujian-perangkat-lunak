# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

import pytest

from f143 import words_in_sentence


def test_empty_sentence_returns_empty_string():
    # Covers the for-loop-not-taken branch on line 4 and the return on line 13
    # with an empty new_lst.
    assert words_in_sentence("") == ""


def test_single_char_word_is_excluded():
    # Covers lines 6-7 (len(word) == 1 True branch) and the False outcome of
    # the condition on line 11.
    assert words_in_sentence("a") == ""


def test_two_char_word_is_included():
    # Covers line 11 True outcome via len(word) == 2; the inner loop on
    # line 8 is not entered (range(2, 2) is empty).
    assert words_in_sentence("is") == "is"


def test_prime_length_word_is_included():
    # Covers lines 8-9 with the loop body executing and the False outcome of
    # the divisibility check on line 9 (no divisor found, flg stays 0).
    assert words_in_sentence("cat") == "cat"           # length 3
    assert words_in_sentence("there") == "there"       # length 5
    assert words_in_sentence("example") == "example"   # length 7


def test_composite_length_word_is_excluded():
    # Covers the True outcome of line 9 and line 10 (flg = 1), plus the
    # False outcome of line 11.
    assert words_in_sentence("four") == ""             # length 4, divisible by 2
    assert words_in_sentence("elephants") == ""        # length 9, divisible by 3


def test_mixed_sentence_joins_prime_length_words():
    # Exercises every line and branch in a single call and verifies the
    # " ".join behaviour on line 13.
    sentence = "a is fun four there example"
    # "a" (len 1) excluded, "is" (len 2) included, "fun" (len 3) included,
    # "four" (len 4) excluded, "there" (len 5) included, "example" (len 7) included.
    assert words_in_sentence(sentence) == "is fun there example"


def test_all_words_excluded_returns_empty_string():
    # Ensures the join on line 13 also works when nothing was appended.
    assert words_in_sentence("a four elephants") == ""
