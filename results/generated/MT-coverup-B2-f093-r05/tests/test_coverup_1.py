# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

"""Tests for f093.encode.

encode(message):
  1. builds a vowel -> (vowel + 2 ASCII positions) mapping for 'aeiouAEIOU'
  2. swaps the case of the message
  3. replaces every (case-swapped) vowel with its mapping, leaving other
     characters untouched.

The function is pure (no I/O, no globals mutated), so no monkeypatching or
cleanup is required; each test only relies on local values.
"""

from f093 import encode


def test_encode_empty_string_executes_all_lines():
    # Exercises lines 3-6 with the trivial input; both comprehension
    # branches are vacuously covered, but every statement runs.
    assert encode("") == ""


def test_encode_lowercase_vowels_become_uppercase_replacements():
    # 'hello' -> swapcase -> 'HELLO' -> e->'G', o->'Q'; consonants only swap case.
    assert encode("hello") == "HGLLQ"


def test_encode_uppercase_vowels_become_lowercase_replacements():
    # 'HELLO' -> swapcase -> 'hello' -> e->'g', o->'q'.
    assert encode("HELLO") == "hgllq"


def test_encode_all_vowels_in_both_cases():
    # Covers every entry of vowels_replace on both branches' true side:
    # 'aeiouAEIOU' -> swapcase -> 'AEIOUaeiou' -> each vowel shifted by 2.
    assert encode("aeiouAEIOU") == "CGKQWcgkqw"


def test_encode_non_vowel_characters_take_false_branch():
    # No vowels at all: only the swapcase effect is visible (false branch
    # of the conditional expression for every character).
    assert encode("bcdfg xyz") == "BCDFG XYZ"


def test_encode_digits_and_punctuation_are_untouched():
    # swapcase leaves digits/punctuation alone and they are not vowels.
    assert encode("PyThOn 3.10!") == "pYtHqN 3.10!"


def test_encode_mixed_branches_in_single_string():
    # 'a1B!' -> swapcase -> 'A1b!' -> 'A'->'C', '1' kept, 'b' kept, '!' kept.
    assert encode("a1B!") == "C1b!"
