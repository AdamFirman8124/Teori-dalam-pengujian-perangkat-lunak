# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

from f038 import encode_cyclic


def test_encode_cyclic_rotates_complete_groups_and_preserves_remainder():
    assert encode_cyclic("abcdefg") == "bcaefdg"


def test_encode_cyclic_handles_empty_string():
    assert encode_cyclic("") == ""
