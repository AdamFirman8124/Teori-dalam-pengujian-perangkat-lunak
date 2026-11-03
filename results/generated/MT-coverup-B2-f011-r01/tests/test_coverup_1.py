# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_mixed_bits():
    """Covers both branches of the inner xor() and the join on line 12."""
    assert string_xor('010', '110') == '100'


def test_string_xor_all_equal():
    """Exercises the i == j -> '0' branch for every position."""
    assert string_xor('0000', '0000') == '0000'
    assert string_xor('1111', '1111') == '0000'


def test_string_xor_all_different():
    """Exercises the i != j -> '1' branch for every position."""
    assert string_xor('1111', '0000') == '1111'
    assert string_xor('0000', '1111') == '1111'


def test_string_xor_empty_inputs():
    """Empty strings: zip yields nothing, join returns ''."""
    assert string_xor('', '') == ''


def test_string_xor_single_chars():
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '0') == '1'
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '1') == '0'


def test_string_xor_is_pure():
    """Verify the function does not mutate its inputs (no state pollution)."""
    a, b = '0101', '1010'
    result = string_xor(a, b)
    assert result == '1111'
    assert a == '0101'
    assert b == '1010'
