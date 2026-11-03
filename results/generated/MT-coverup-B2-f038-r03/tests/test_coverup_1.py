# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        # Empty string: no groups are produced at all.
        ("", ""),
        # Groups shorter than 3 chars must be left untouched (else-branch of line 6).
        ("a", "a"),
        ("ab", "ab"),
        # Full 3-char groups get their first element moved to the end (if-branch of line 6).
        ("abc", "bca"),
        # Mixed: full group cycled plus a trailing short group kept as-is.
        ("abcd", "bcad"),
        ("abcde", "bcade"),
        # Multiple full groups, each cycled independently:
        # "abc" -> "bca", "def" -> "efd".
        ("abcdef", "bcaefd"),
        # "xyz" -> "yzx", "zyx" -> "yxz".
        ("xyzzyx", "yzxyxz"),
    ],
)
def test_encode_cyclic(s, expected):
    """Covers the group-splitting comprehension (line 4), both branches of the
    cycling comprehension (line 6) and the final join/return (line 7)."""
    result = encode_cyclic(s)
    assert isinstance(result, str)
    assert result == expected
    # Encoding preserves the multiset of characters.
    assert sorted(result) == sorted(s)


def test_encode_cyclic_triple_application_is_identity():
    """Cycling every full group three times must restore the original string."""
    s = "abcdefghi"
    once = encode_cyclic(s)
    twice = encode_cyclic(once)
    thrice = encode_cyclic(twice)
    assert once == "bcaefdhig"
    assert twice == "cabfdeigh"
    assert thrice == s
