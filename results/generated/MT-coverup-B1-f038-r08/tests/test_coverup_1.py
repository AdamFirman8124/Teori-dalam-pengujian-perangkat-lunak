# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_empty():
    assert encode_cyclic("") == ""


def test_encode_cyclic_single_char():
    assert encode_cyclic("a") == "a"


def test_encode_cyclic_two_chars():
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_exact_group_of_three():
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_multiple_full_groups():
    assert encode_cyclic("abcdef") == "bcaefd"
    assert encode_cyclic("abcdefghi") == "bcaefdhig"


def test_encode_cyclic_partial_tail_len_one():
    # last group has fewer than 3 elements and is left unchanged
    assert encode_cyclic("abcd") == "bcad"
    assert encode_cyclic("abcdefg") == "bcaefdg"


def test_encode_cyclic_partial_tail_len_two():
    # last group has 2 elements and is left unchanged
    assert encode_cyclic("abcde") == "bcade"
    assert encode_cyclic("abcdefgh") == "bcaefdgh"
