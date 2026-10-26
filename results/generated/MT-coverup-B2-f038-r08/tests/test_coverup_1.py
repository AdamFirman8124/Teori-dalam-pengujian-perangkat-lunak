# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_rotates_complete_groups():
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_preserves_incomplete_group():
    assert encode_cyclic("abcd") == "bcad"


def test_encode_cyclic_handles_empty_string():
    assert encode_cyclic("") == ""
