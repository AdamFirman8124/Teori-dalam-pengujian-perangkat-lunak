# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

from pysnooper.utils import shitcode


def test_shitcode_ascii_passthrough():
    assert shitcode("hello") == "hello"
    assert shitcode("ABC xyz 123 !@#") == "ABC xyz 123 !@#"


def test_shitcode_boundary_in_range():
    assert shitcode(chr(1)) == chr(1)
    assert shitcode(chr(255)) == chr(255)
    assert shitcode("a" + chr(1) + chr(255) + "z") == "a" + chr(1) + chr(255) + "z"


def test_shitcode_out_of_range_replaced():
    assert shitcode(chr(256)) == "?"
    assert shitcode("\u0100") == "?"
    assert shitcode("\U0001F600") == "?"
    assert shitcode("a\u0100b\U0001F600c") == "a?b?c"


def test_shitcode_null_char_replaced():
    assert shitcode("\x00") == "?"
    assert shitcode("a\x00b") == "a?b"


def test_shitcode_empty_and_mixed():
    assert shitcode("") == ""
    assert shitcode("Hi\x00\u0100\U0001F600!") == "Hi???!"
