# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


def test_encode_cyclic_full_groups():
    """Groups of exactly 3 characters have their first element cycled to the end.

    Covers line 4 (group splitting), the True branch of line 6 (len(group) == 3)
    and line 7 (return).
    """
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcdef") == "bcaefd"
    assert encode_cyclic("abcdefghi") == "bcaefdhig"


def test_encode_cyclic_short_groups():
    """Groups with fewer than 3 characters are left unchanged.

    Covers the False branch of line 6 (len(group) != 3), including the final
    partial group produced by the min() slice on line 4.
    """
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"
    assert encode_cyclic("abcd") == "bcad"
    assert encode_cyclic("abcde") == "bcade"


def test_encode_cyclic_empty_string():
    """An empty string yields an empty result.

    Covers the not-taken arcs of the comprehension loops on lines 4 and 6.
    """
    assert encode_cyclic("") == ""
