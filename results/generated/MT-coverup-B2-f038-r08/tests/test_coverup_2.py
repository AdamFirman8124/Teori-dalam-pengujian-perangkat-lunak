# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_roundtrip():
    """decode_cyclic must invert encode_cyclic for strings of every length.

    This exercises line 12 (the return statement) for all branch shapes of
    the underlying encode_cyclic: complete groups of 3 and trailing partial
    groups of length 1 or 2, including the empty string.
    """
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef",
              "abcdefghi", "xyz" * 4 + "x"]:
        assert decode_cyclic(encode_cyclic(s)) == s


def test_decode_cyclic_known_values():
    # encode_cyclic rotates each complete group of 3 chars left by one;
    # decode_cyclic applies it twice, i.e. rotates complete groups right by
    # one, while trailing partial groups (len < 3) are left untouched.
    assert decode_cyclic("") == ""
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("abc") == "cab"
    assert decode_cyclic("abcd") == "cabd"
    assert decode_cyclic("abcde") == "cabde"
    assert decode_cyclic("abcdef") == "cabfde"
    # Decoding an already-encoded string restores the original.
    assert decode_cyclic(encode_cyclic("abcdef")) == "abcdef"
    assert decode_cyclic("bcaefd") == "abcdef"


def test_decode_cyclic_preserves_length_and_characters():
    for s in ["", "a", "ab", "abc", "abcd", "hello world!", "zzz"]:
        decoded = decode_cyclic(s)
        assert len(decoded) == len(s)
        assert sorted(decoded) == sorted(s)
