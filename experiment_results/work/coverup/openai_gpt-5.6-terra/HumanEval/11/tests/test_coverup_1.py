# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest

from script_11 import string_xor


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("010", "110", "100"),
        ("000", "000", "000"),
        ("111", "000", "111"),
        ("10101", "00111", "10010"),
    ],
)
def test_string_xor_returns_bitwise_xor(a, b, expected):
    assert string_xor(a, b) == expected


def test_string_xor_uses_only_pairs_from_both_inputs():
    assert string_xor("101", "01") == "11"
