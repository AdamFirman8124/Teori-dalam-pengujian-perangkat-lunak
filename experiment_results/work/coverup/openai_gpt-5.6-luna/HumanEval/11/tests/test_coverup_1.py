# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest

from script_11 import string_xor


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("000", "000", "000"),
        ("111", "111", "000"),
    ],
)
def test_string_xor_returns_zero_for_matching_bits(a, b, expected):
    assert string_xor(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("010", "110", "100"),
        ("101", "010", "111"),
    ],
)
def test_string_xor_returns_one_for_different_bits(a, b, expected):
    assert string_xor(a, b) == expected
