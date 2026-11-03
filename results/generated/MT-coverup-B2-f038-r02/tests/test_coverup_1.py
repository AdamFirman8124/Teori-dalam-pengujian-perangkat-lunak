# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_full_groups():
    """Every group has exactly 3 chars, so each is cycled (first char moves to end)."""
    assert encode_cyclic("abcdef") == "bcaefd"
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_partial_last_group():
    """Last group has fewer than 3 chars and must be left unchanged."""
    assert encode_cyclic("abcd") == "bcad"
    assert encode_cyclic("abcde") == "bcade"


def test_encode_cyclic_short_strings():
    """Groups shorter than 3 chars are returned as-is."""
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_empty_string():
    """An empty string yields no groups and an empty result."""
    assert encode_cyclic("") == ""


def test_encode_cyclic_triple_application_is_identity():
    """Cycling each 3-char group three times restores the original string."""
    for s in ["", "a", "ab", "abc", "abcd", "abcdefghi", "abcdefghij"]:
        assert encode_cyclic(encode_cyclic(encode_cyclic(s))) == s
