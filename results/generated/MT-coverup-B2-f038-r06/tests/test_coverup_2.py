# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_executes_line_12_basic():
    assert decode_cyclic("bca") == "abc"


def test_decode_cyclic_is_double_encode():
    s = "abcdef"
    assert decode_cyclic(s) == encode_cyclic(encode_cyclic(s))


def test_decode_cyclic_empty():
    assert decode_cyclic("") == ""


def test_decode_cyclic_short_strings_unchanged():
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("xy") == "xy"


def test_decode_encode_roundtrip():
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "hello world"]:
        assert decode_cyclic(encode_cyclic(s)) == s


def test_encode_decode_roundtrip():
    for s in ["", "a", "ab", "abc", "abcd", "abcdef", "bcaefd"]:
        assert encode_cyclic(decode_cyclic(s)) == s


def test_decode_cyclic_known_values():
    # encode_cyclic("abc") == "bca", encode twice: "bca" -> "cab"
    assert encode_cyclic("abc") == "bca"
    assert decode_cyclic("abc") == "cab"
    assert decode_cyclic("bcaefd") == "abcdef"
