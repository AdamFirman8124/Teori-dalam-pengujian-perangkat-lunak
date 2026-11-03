# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_roundtrip():
    # decode_cyclic(encode_cyclic(s)) must recover the original string,
    # since decode applies the left-rotation twice more (3 rotations = identity).
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefghi", "hello world"]:
        assert decode_cyclic(encode_cyclic(s)) == s


def test_decode_cyclic_equals_double_encode():
    # decode_cyclic is defined as encode_cyclic applied twice.
    for s in ["", "a", "ab", "abc", "abcd", "abcdefg", "xyzzyx"]:
        assert decode_cyclic(s) == encode_cyclic(encode_cyclic(s))


def test_decode_cyclic_known_values():
    # Each full group of 3 is left-rotated by 2: "abc" -> "bca" -> "cab".
    assert decode_cyclic("abc") == "cab"
    # Trailing partial groups (length 1 or 2) are left untouched.
    assert decode_cyclic("abcd") == "cabd"
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("") == ""
