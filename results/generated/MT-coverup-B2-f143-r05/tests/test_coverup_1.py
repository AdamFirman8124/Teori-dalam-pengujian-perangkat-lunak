# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

import pytest

from f143 import words_in_sentence


def test_words_in_sentence_prime_length_words():
    """Words of prime length (3) are kept; composite length (4) is filtered out.

    Covers: new_lst init, outer loop, flg = 0, len(word) == 1 False branch,
    inner loop entry, len(word) % i == 0 False branch, flg == 0 True branch,
    append, and return.
    """
    assert words_in_sentence("fun code") == "fun"


def test_words_in_sentence_single_char_word():
    """A one-character word is excluded.

    Covers: len(word) == 1 True branch (flg = 1), empty inner loop
    (range(2, 1)), and flg == 0 False branch.
    """
    assert words_in_sentence("a") == ""


def test_words_in_sentence_two_char_word():
    """A two-character word is kept via the len(word) == 2 branch.

    Covers: inner loop not entered (range(2, 2) is empty) and the
    len(word) == 2 True branch of the final condition.
    """
    assert words_in_sentence("is") == "is"


def test_words_in_sentence_composite_length_word():
    """A word whose length has a divisor in [2, len) is excluded.

    Covers: len(word) % i == 0 True branch (flg = 1) and the
    flg == 0 False branch of the final condition.
    """
    assert words_in_sentence("cats") == ""


def test_words_in_sentence_mixed_lengths():
    """One call exercising every line and branch: lengths 1, 2, 3, 4, 5."""
    sentence = "a is fun cats hello"
    # 'a' (len 1) -> excluded; 'is' (len 2) -> kept; 'fun' (len 3, prime) -> kept;
    # 'cats' (len 4, composite) -> excluded; 'hello' (len 5, prime) -> kept.
    assert words_in_sentence(sentence) == "is fun hello"


def test_words_in_sentence_empty_string():
    """An empty sentence yields an empty result (outer loop never runs)."""
    assert words_in_sentence("") == ""
