# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

import pytest

from f011 import string_xor


def test_string_xor_exercises_both_branches():
    # '0' vs '1' -> '1' (else branch), '1' vs '1' -> '0' (if branch),
    # '0' vs '0' -> '0' (if branch), '1' vs '0' -> '1' (else branch)
    assert string_xor('0110', '1100') == '1010'


def test_string_xor_identical_strings_all_zeros():
    # Covers only the `i == j` -> '0' branch
    assert string_xor('1111', '1111') == '0000'
    assert string_xor('0000', '0000') == '0000'


def test_string_xor_complement_strings_all_ones():
    # Covers only the `i != j` -> '1' branch
    assert string_xor('0101', '1010') == '1111'


def test_string_xor_empty_inputs():
    # zip produces nothing; generator never runs but line 12 still executes
    assert string_xor('', '') == ''


def test_string_xor_is_symmetric():
    a, b = '10101', '01110'
    assert string_xor(a, b) == string_xor(b, a)


def test_string_xor_involution():
    a, b = '10101', '01110'
    assert string_xor(string_xor(a, b), b) == a


def test_string_xor_matches_reference_implementation():
    expected = ''.join('0' if x == y else '1' for x, y in zip('1101001', '0101101'))
    assert string_xor('1101001', '0101101') == expected
