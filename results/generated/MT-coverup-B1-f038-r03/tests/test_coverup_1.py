# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_empty():
    assert encode_cyclic("") == ""


def test_encode_cyclic_short_groups_no_rotation():
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_exact_group_of_three():
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_mixed_full_and_partial_groups():
    # first group len==3 (rotated), last group len<3 (unchanged)
    assert encode_cyclic("abcd") == "bcad"
    assert encode_cyclic("abcde") == "bcade"
    assert encode_cyclic("abcdefg") == "bcaefdg"
