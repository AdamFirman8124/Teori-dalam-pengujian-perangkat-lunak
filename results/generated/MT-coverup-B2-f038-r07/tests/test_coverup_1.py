# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_empty():
    assert encode_cyclic("") == ""


def test_encode_cyclic_one_char_partial_group():
    assert encode_cyclic("a") == "a"


def test_encode_cyclic_two_chars_partial_group():
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_exactly_three_chars():
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_multiple_full_groups():
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_trailing_one_char_group():
    assert encode_cyclic("abcd") == "bcad"


def test_encode_cyclic_trailing_two_char_group():
    assert encode_cyclic("abcde") == "bcade"


def test_encode_cyclic_longer_mixed_groups():
    assert encode_cyclic("abcdefghij") == "bcaefdhigj"
