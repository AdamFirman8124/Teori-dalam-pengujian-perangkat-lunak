# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

"""Tests for f011.string_xor.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or teardown is required; each test simply calls the
function and asserts on its return value, leaving no state behind.
"""

from f011 import string_xor


def test_string_xor_identical_characters_take_true_branch():
    # Covers line 6 (nested def), line 7 (if i == j) and line 8 (return '0').
    assert string_xor('0000', '0000') == '0000'
    assert string_xor('aa', 'aa') == '00'


def test_string_xor_different_characters_take_else_branch():
    # Covers line 10 (return '1' in the else branch).
    assert string_xor('1111', '0000') == '1111'
    assert string_xor('ab', 'cd') == '11'


def test_string_xor_mixed_input_covers_both_branches_and_join():
    # Covers line 12 (''.join over the generator) with both branches taken:
    # ('0','0')->'0', ('1','0')->'1', ('0','1')->'1', ('1','1')->'0'
    assert string_xor('0101', '0011') == '0110'


def test_string_xor_empty_strings():
    # Exercises the join over an empty generator.
    assert string_xor('', '') == ''


def test_string_xor_length_mismatch_truncates_to_shorter():
    # zip stops at the shorter string: only ('1','1') is compared -> '0'.
    assert string_xor('10', '1') == '0'
    assert string_xor('1', '10') == '0'
