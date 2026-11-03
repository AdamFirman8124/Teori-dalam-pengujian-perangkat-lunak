# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

"""Tests for f093.encode (HumanEval-style vowel/case encoder).

encode(message):
  1. builds a map sending each vowel to the letter two ASCII positions ahead
     (a->c, e->g, i->k, o->q, u->w, A->C, E->G, I->K, O->Q, U->W),
  2. swapcases the message,
  3. replaces any vowel (post-swapcase) via the map, leaving other chars intact.

The function is pure (no I/O, no globals, no side effects), so no monkeypatching
or teardown is required; nothing is mutated and no state can leak between tests.
"""

from f093 import encode


def test_encode_swaps_case_and_shifts_vowels():
    # Exercises both branches of the conditional comprehension:
    # 'T'/'S' hit the else branch, 'E' hits the vowel branch.
    assert encode('test') == 'TGST'


def test_encode_mixed_message():
    # Classic example: lowercase letters become uppercase and vice versa,
    # then vowels (in their new case) are shifted two letters ahead.
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'


def test_encode_empty_string():
    # Edge case: empty input yields empty output.
    assert encode('') == ''


def test_encode_no_vowels_only_else_branch():
    # No vowels present: every character takes the else branch.
    assert encode('rhythm') == 'RHYTHM'


def test_encode_all_vowels_both_cases():
    # Every vowel (lower and upper) takes the vowel branch after swapcase:
    # 'aeiouAEIOU' -> swapcase -> 'AEIOUaeiou'
    #   A->C, E->G, I->K, O->Q, U->W, a->c, e->g, i->k, o->q, u->w
    assert encode('aeiouAEIOU') == 'CGKQWcgkqw'


def test_encode_non_letters_unchanged():
    # Digits and punctuation are unaffected by swapcase and are not vowels.
    assert encode('a1!') == 'C1!'


def test_encode_sentence_with_punctuation_and_digits():
    # 'Hello, World! 123' -> swapcase -> 'hELLO, wORLD! 123'
    # -> vowels shifted -> 'hGLLQ, wQRLD! 123'
    assert encode('Hello, World! 123') == 'hGLLQ, wQRLD! 123'


def test_encode_is_pure_and_repeatable():
    # Postcondition: calling encode twice with the same input gives the same
    # result (no hidden state mutation between calls).
    # 'AbCdEfG' -> swapcase -> 'aBcDeFg' -> vowels shifted -> 'cBcDgFg'
    first = encode('AbCdEfG')
    second = encode('AbCdEfG')
    assert first == second == 'cBcDgFg'
