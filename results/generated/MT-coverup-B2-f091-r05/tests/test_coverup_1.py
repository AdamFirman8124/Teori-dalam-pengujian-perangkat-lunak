# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_is_bored_counts_i_sentences_among_others():
    # Covers both branches of the generator expression:
    # sentences starting with "I " (True) and sentences that do not (False).
    S = "The sky is blue. The sun is shining. I love this weather"
    assert is_bored(S) == 1


def test_is_bored_multiple_i_sentences():
    # Multiple sentences start with "I ", separated by different delimiters.
    assert is_bored("I am bored! I want to sleep? I do.") == 3


def test_is_bored_no_i_sentences():
    # No sentence starts with "I " -> sum is 0.
    assert is_bored("Hello world") == 0


def test_is_bored_empty_string():
    # Edge case: empty input splits into a single empty sentence.
    assert is_bored("") == 0


def test_is_bored_i_without_space_not_counted():
    # "It" starts with "I" but not "I ", so it must not be counted.
    assert is_bored("It is fine. I am fine.") == 1
