# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

from pysnooper.utils import shitcode


def test_shitcode_ascii_preserved():
    assert shitcode("hello") == "hello"
    assert shitcode("") == ""


def test_shitcode_latin1_boundary_preserved():
    # 1..255 preserved, 0 and 256+ replaced
    assert shitcode("\x01\x7f\xff\xe9") == "\x01\x7f\xff\xe9"
    assert shitcode("\xff") == "\xff"
    assert shitcode("a\xffb") == "a\xffb"


def test_shitcode_replaces_null_and_out_of_range():
    assert shitcode("\x00") == "?"
    assert shitcode("\u0100") == "?"  # ord == 256 -> not < 256
    assert shitcode("\u20ac") == "?"  # euro sign ord 8364
    assert shitcode("\U0001F600") == "?"  # emoji
    assert shitcode("a\x00b\u0100c\u20acd\U0001F600e") == "a?b?c?d?e"
    assert shitcode("h\u00e9llo\u20ac\U0001F600") == "h\u00e9llo??"
