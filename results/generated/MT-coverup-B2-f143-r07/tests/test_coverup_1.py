# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

"""Tests for f143.words_in_sentence.

The function keeps only the words whose length is a prime number
(2, 3, 5, 7, ...) and returns them joined by single spaces.
The function under test is pure (no globals, files, or I/O), so no
monkeypatching/teardown is required to avoid state pollution.
"""

from f143 import words_in_sentence


def test_empty_sentence_returns_empty_string():
    # Exercises the word loop (line 4) with zero iterations.
    assert words_in_sentence("") == ""


def test_single_character_word_is_excluded():
    # len(word) == 1 -> flg = 1 (lines 6-7); line 11 condition is False.
    assert words_in_sentence("a") == ""


def test_two_character_word_is_included():
    # len(word) == 2 -> inner loop range(2, 2) never runs (line 8 exit
    # branch); flg stays 0, so line 11 is True via its first operand.
    assert words_in_sentence("is") == "is"


def test_prime_length_words_are_included():
    # Lengths 3, 5 and 7: inner loop body runs (lines 8-9) but never
    # finds a divisor (line 9 False branch on every iteration).
    assert words_in_sentence("cat hello seven77") == "cat hello seven77"


def test_composite_length_words_are_excluded():
    # "four" (len 4): divisor found immediately (line 9 True -> line 10).
    # "nine9999" (len 9): line 9 False at i=2, then True at i=3 (9 % 3 == 0),
    # covering both outcomes of the divisibility test inside one loop.
    assert words_in_sentence("four nine9999") == ""


def test_mixed_sentence_keeps_only_prime_length_words():
    # One sentence exercising every branch:
    #   "a"      (len 1): flg=1, excluded          -> line 11 False
    #   "is"     (len 2): inner loop skipped, kept -> line 11 True
    #   "four"   (len 4): divisor found, excluded  -> lines 9-10, 11 False
    #   "cat"    (len 3): prime, kept              -> line 9 False, 11 True
    #   "hello"  (len 5): prime, kept              -> line 9 False, 11 True
    #   "sixsix" (len 6): divisor found, excluded  -> lines 9-10, 11 False
    sentence = "a is four cat hello sixsix"
    assert words_in_sentence(sentence) == "is cat hello"


def test_splitting_ignores_extra_whitespace():
    # str.split() with no argument collapses runs of whitespace.
    assert words_in_sentence("   a    is   ") == "is"
