# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

"""Tests for f093.encode.

encode(message) first swaps the case of every character in `message`
(line 5), then maps every vowel (a, e, i, o, u in either case) to the
character two ASCII code points later (lines 3-4, 6). All other
characters pass through unchanged after the case swap.

The function is pure (no module-level state, no I/O), so no monkeypatching
or cleanup is required; each test only relies on its own local data.
"""

from f093 import encode


def test_encode_mixed_case_sentence():
    # Exercises the swapcase (line 5) plus both branches of the conditional
    # in the comprehension (line 6): vowels are shifted by 2, other
    # characters are only case-swapped.
    assert encode("Hello, World!") == "hGLLQ, wQRLD!"


def test_encode_all_vowels_both_cases():
    # Exercises every entry of the vowels_replace dict built on line 4:
    # uppercase vowels and lowercase vowels.
    assert encode("aeiouAEIOU") == "CGKQWcgkqw"


def test_encode_empty_string():
    # Lines 3-6 still run; the comprehension on line 6 yields nothing.
    assert encode("") == ""


def test_encode_no_vowels():
    # Only the "not a vowel" branch of line 6 is taken.
    assert encode("bcdfg xyz 123") == "BCDFG XYZ 123"


def test_encode_digits_and_punctuation_untouched():
    # Non-alphabetic characters pass through unchanged, while letters are
    # case-swapped first and then vowels (in either case) are shifted by 2:
    # "Ab3!_Ei" -> swapcase -> "aB3!_eI" -> a->c, e->g, I->K -> "cB3!_gK".
    assert encode("Ab3!_Ei") == "cB3!_gK"


def test_encode_is_pure_input_not_mutated():
    # Verifies the function does not depend on or modify any external
    # state: repeated calls give identical results and the argument
    # (an immutable str) is left untouched.
    #
    # "Test Message!" -> swapcase -> "tEST mESSAGE!"
    # -> E->G, E->G, A->C, E->G -> "tGST mGSSCGG!"
    message = "Test Message!"
    original = str(message)
    first = encode(message)
    second = encode(message)
    assert first == second == "tGST mGSSCGG!"
    assert message == original
