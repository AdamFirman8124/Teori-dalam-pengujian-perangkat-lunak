# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

from f093 import encode


def test_encode_lowercase_vowels():
    assert encode("aeiou") == "CGKQW"


def test_encode_uppercase_vowels():
    assert encode("AEIOU") == "cgkqw"


def test_encode_single_vowel_swapcase():
    assert encode("a") == "C"
    assert encode("A") == "c"
    assert encode("e") == "G"
    assert encode("E") == "g"


def test_encode_mixed_word():
    assert encode("test") == "TGST"
    assert encode("TEST") == "tgst"
    assert encode("Hello") == "hGLLQ"


def test_encode_consonants_non_alpha_else_branch():
    assert encode("bcdfg BCDFG 123!") == "BCDFG bcdfg 123!"
    assert encode("xyz XYZ") == "XYZ xyz"


def test_encode_empty():
    assert encode("") == ""
