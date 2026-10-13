# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest

from script_11 import string_xor


def test_string_xor_all_bits_equal():
    # Exercises the `if i == j` TRUE branch for every position.
    a = "010"
    b = "010"
    a_copy, b_copy = a, b

    result = string_xor(a, b)

    assert result == "000"
    assert isinstance(result, str)
    # Postcondition: inputs are not mutated by the function.
    assert (a, b) == (a_copy, b_copy)


def test_string_xor_all_bits_different():
    # Exercises the `else` (FALSE) branch of the inner `xor` for every position.
    result = string_xor("010", "101")

    assert result == "111"
    assert isinstance(result, str)


def test_string_xor_mixed_bits_both_branches():
    # Mixed input forces both the TRUE and FALSE branches in one call.
    result = string_xor("0011", "0101")

    assert result == "0110"
    assert len(result) == 4


def test_string_xor_docstring_example():
    result = string_xor("010", "110")

    assert result == "100"


def test_string_xor_unequal_lengths_truncates_to_shortest():
    # `zip` stops at the shortest input; the extra characters are dropped.
    result = string_xor("0101", "11")

    assert result == "10"
    assert len(result) == 2


def test_string_xor_empty_inputs():
    # Empty iterables mean the generator never runs and no `xor` branch is hit.
    assert string_xor("", "") == ""
    assert string_xor("", "101") == ""
    assert string_xor("101", "") == ""


def test_string_xor_single_characters():
    assert string_xor("0", "0") == "0"
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"
    assert string_xor("1", "1") == "0"


def test_string_xor_has_no_lingering_state(monkeypatch):
    # Guard against state pollution: the function is pure, so repeated calls
    # with the same arguments must always yield the same result.
    first = string_xor("1010", "1100")
    second = string_xor("1010", "1100")

    assert first == second == "0110"

    # Also verify the function does not depend on any module-level mutable state
    # that a previous test could have changed.
    monkeypatch.setattr("builtins.zip", zip, raising=False)
    assert string_xor("1010", "1100") == "0110"
