# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


def test_encode_cyclic_full_groups():
    # "abcdef" -> groups ["abc", "def"] -> ["bca", "efd"] -> "bcaefd"
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_partial_last_group():
    # "abcde" -> groups ["abc", "de"] -> ["bca", "de"] -> "bcade"
    # last group has fewer than 3 elements, so it is left unchanged
    assert encode_cyclic("abcde") == "bcade"


def test_encode_cyclic_single_partial_group():
    # "ab" -> one group of length 2, unchanged
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_empty_string():
    assert encode_cyclic("") == ""
