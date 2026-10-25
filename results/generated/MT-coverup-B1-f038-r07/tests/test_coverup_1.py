# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_empty_string():
    assert encode_cyclic("") == ""


def test_encode_cyclic_single_full_group():
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_multiple_full_groups():
    assert encode_cyclic("abcdef") == "bcaefd"
    assert encode_cyclic("xyz123") == "yzx231"


def test_encode_cyclic_short_group_unchanged():
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_full_group_plus_remainder_one():
    assert encode_cyclic("abcd") == "bcad"
    assert encode_cyclic("abcdefg") == "bcaefdg"


def test_encode_cyclic_full_group_plus_remainder_two():
    assert encode_cyclic("abcde") == "bcade"
    assert encode_cyclic("abcdefgh") == "bcaefdgh"
