# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

"""Tests for f038.encode_cyclic.

encode_cyclic is a pure function (no I/O, no module state), so no
monkeypatching/teardown is required; each test simply calls the function and
asserts on its return value. Together the tests exercise every line and both
branches of the conditional expression on line 6:

  * line 4: group splitting (exercised by every call, including the empty case)
  * line 6: True branch  -> group of exactly 3 elements is cycled
            False branch -> shorter group is left untouched
  * line 7: the join/return
"""

from f038 import encode_cyclic


def test_encode_cyclic_all_full_groups():
    """Length divisible by 3: every group has 3 elements and gets cycled."""
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcdef") == "bcaefd"
    assert encode_cyclic("abcdefghi") == "bcaefdhig"


def test_encode_cyclic_partial_trailing_group():
    """Length not divisible by 3: only full groups are cycled, tail untouched."""
    assert encode_cyclic("ab") == "ab"          # single short group
    assert encode_cyclic("abcd") == "bcad"      # one full group + 1 char
    assert encode_cyclic("abcde") == "bcade"    # one full group + 2 chars
    assert encode_cyclic("a") == "a"            # single-char group


def test_encode_cyclic_empty_string():
    """Empty input produces no groups and returns the empty string."""
    assert encode_cyclic("") == ""


def test_encode_cyclic_triple_encode_is_identity():
    """Cycling a 3-element group three times restores it, so encoding three
    times returns the original string (the classic decode property)."""
    for s in ("", "a", "ab", "abc", "abcd", "abcdefgh"):
        assert encode_cyclic(encode_cyclic(encode_cyclic(s))) == s
