# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

from f050 import decode_shift


def test_decode_shift_single_letter_no_wrap():
    assert decode_shift("f") == "a"
    assert decode_shift("g") == "b"
    assert decode_shift("z") == "u"


def test_decode_shift_wraparound():
    assert decode_shift("a") == "v"
    assert decode_shift("abcde") == "vwxyz"
    assert decode_shift("e") == "z"


def test_decode_shift_word():
    assert decode_shift("mjqqt") == "hello"


def test_decode_shift_full_alphabet():
    assert decode_shift("abcdefghijklmnopqrstuvwxyz") == "vwxyzabcdefghijklmnopqrstu"


def test_decode_shift_empty_string():
    assert decode_shift("") == ""
