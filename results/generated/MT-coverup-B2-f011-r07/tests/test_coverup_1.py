# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

"""Tests for f011.string_xor covering lines 6-12 (xor helper and join)."""

import pytest

from f011 import string_xor


def test_string_xor_equal_characters_returns_zero():
    # Covers line 6 (def xor), line 7 (if i == j), line 8 (return '0'),
    # and line 12 (the join over zip).
    result = string_xor('0', '0')
    assert result == '0'
    assert isinstance(result, str)


def test_string_xor_different_characters_returns_one():
    # Covers line 10 (return '1' in the else branch) and line 12.
    result = string_xor('0', '1')
    assert result == '1'
    assert isinstance(result, str)


def test_string_xor_mixed_strings_cover_both_branches():
    # Exercises both the equal (-> '0') and different (-> '1') branches
    # within a single call, plus the generator/join on line 12.
    assert string_xor('1100', '1010') == '0110'
    assert string_xor('0101', '1010') == '1111'


def test_string_xor_empty_inputs():
    # zip of two empty strings yields nothing; join returns '' (line 12).
    assert string_xor('', '') == ''


def test_string_xor_length_mismatch_truncates_to_shorter():
    # zip stops at the shorter input; verifies join behavior on line 12.
    assert string_xor('111', '00') == '11'


def test_string_xor_is_pure_no_state_pollution():
    # Calling repeatedly with the same arguments yields identical results,
    # confirming the function has no side effects or hidden state.
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('1010', '0101') == '1111'
