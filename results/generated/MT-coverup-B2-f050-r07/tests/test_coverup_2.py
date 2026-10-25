# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

from f050 import decode_shift


def test_decode_shift_hello():
    assert decode_shift("mjqqt") == "hello"


def test_decode_shift_empty():
    assert decode_shift("") == ""


def test_decode_shift_wrap_around():
    assert decode_shift("abcde") == "vwxyz"


def test_decode_shift_single_char():
    assert decode_shift("f") == "a"
    assert decode_shift("a") == "v"
