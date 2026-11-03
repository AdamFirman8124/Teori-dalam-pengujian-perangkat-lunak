# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

import pytest

from f093 import encode


def test_encode_basic_word():
    """Lines 3-6: lowercase input swaps to uppercase, vowels shift by two."""
    # 'test'.swapcase() -> 'TEST'; 'E' is a vowel -> 'G', others unchanged.
    assert encode("test") == "TGST"


def test_encode_mixed_sentence_exercises_both_branches():
    """Covers both branches of the 'if i in vowels' conditional."""
    # 'This is a message'.swapcase() -> 'tHIS IS A MESSAGE'
    # vowels I, I, A, E, A, E -> K, K, C, G, C, G; everything else unchanged.
    assert encode("This is a message") == "tHKS KS C MGSSCGG"


def test_encode_uppercase_vowels_shift_from_lowercase():
    """Uppercase vowels swap to lowercase first, then shift by two."""
    # 'AEIOU'.swapcase() -> 'aeiou' -> each shifted +2:
    # a->c, e->g, i->k, o->q, u->w
    assert encode("AEIOU") == "cgkqw"


def test_encode_non_alpha_characters_unchanged():
    """Digits and punctuation pass through untouched (else branch)."""
    assert encode("123!@# xyz") == "123!@# XYZ"


def test_encode_empty_string():
    """Empty input yields empty output (join over empty list)."""
    assert encode("") == ""


@pytest.mark.parametrize(
    "message,expected",
    [
        ("a", "C"),          # lowercase vowel -> uppercase shifted
        ("A", "c"),          # uppercase vowel -> lowercase shifted
        ("zZ", "Zz"),        # non-vowels only swap case
        ("Hello, World!", "hGLLQ, wQRLD!"),
    ],
)
def test_encode_parametrized(message, expected):
    assert encode(message) == expected
