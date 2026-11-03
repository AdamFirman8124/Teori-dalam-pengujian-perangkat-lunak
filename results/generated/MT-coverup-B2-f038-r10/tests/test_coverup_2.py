# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic, encode_cyclic


@pytest.mark.parametrize(
    "s",
    [
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefghi",
        "abcdefghij",
        "Hello, World!",
        "xY z_12",
    ],
)
def test_decode_cyclic_inverts_encode(s):
    """decode_cyclic must undo encode_cyclic for every input length."""
    assert decode_cyclic(encode_cyclic(s)) == s


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("abc", "cab"),
        ("abcd", "cabd"),
        ("abcdef", "cabfde"),
    ],
)
def test_decode_cyclic_known_values(s, expected):
    """Each complete group of three characters is rotated right by one."""
    assert decode_cyclic(s) == expected


def test_decode_cyclic_matches_double_encode():
    """decode_cyclic is literally encode_cyclic applied twice."""
    s = "pytest coverage!"
    assert decode_cyclic(s) == encode_cyclic(encode_cyclic(s))
